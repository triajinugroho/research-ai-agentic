"""
WSD Engine — Lesk Baseline + LLM-Based Disambiguation
=====================================================
Implements all 5 WSD conditions for the Paper 1 experiment:
- Condition A: NLTK Lesk (baseline)
- Condition B: Qwen-2.5 via Ollama
- Condition C: Mistral-7B via Ollama
- Condition D: Llama-3.1-8B via Ollama
- Condition E: Gemini-1.5-Flash via Google AI Studio

Usage:
    from wsd_engine import LeskWSD, LLMWSD
    lesk = LeskWSD()
    llm = LLMWSD(model='qwen2.5:7b', prompt_variant='P3')
"""

import re
import time
import json
import logging
from abc import ABC, abstractmethod
from typing import Optional, Dict, List, Tuple

import nltk
from nltk.wsd import lesk
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize

logger = logging.getLogger(__name__)


# --- Prompt Templates ---

PROMPT_TEMPLATES = {
    'P1': """Given the sentence: "{sentence}"
The word "{word}" (as a {pos}) can have these meanings:
{synset_list}
Which meaning number best fits the word in this sentence?
Answer with only the number.""",

    'P2': """Given the sentence: "{sentence}"
The word "{word}" (as a {pos}) can have these meanings:
{synset_list_with_examples}
Which meaning number best fits the word in this sentence?
Answer with only the number.""",

    'P3': """You are analyzing a student's answer to a computer science exam question.
The exam question was: "{question_text}"
The student answered: "{sentence}"

The word "{word}" (as a {pos}) can have these meanings:
{synset_list_with_examples}
Which meaning number best fits how the word is used in the student's answer?
Answer with only the number.""",

    'P4': """You are analyzing a student's answer to a computer science exam question.
The exam question was: "{question_text}"
The student answered: "{sentence}"

The word "{word}" (as a {pos}) can have these meanings:
{synset_list_with_examples}

Think step by step:
1. What is the sentence about?
2. What role does "{word}" play in this sentence?
3. Which meaning best matches?

Provide your reasoning, then state your final answer as a single number on the last line.""",
}


def format_synset_list(synsets: List, include_examples: bool = False) -> str:
    """Format synset candidates as numbered list for prompts."""
    lines = []
    for i, s in enumerate(synsets, 1):
        line = f"{i}. {s.name()}: {s.definition()}"
        if include_examples and s.examples():
            examples_str = '; '.join(s.examples()[:2])
            line += f'\n   Examples: "{examples_str}"'
        lines.append(line)
    return '\n'.join(lines)


def parse_synset_response(response: str, num_options: int) -> Optional[int]:
    """
    Parse LLM response to extract synset choice number.

    Strategy:
    1. Look for a standalone number on the last line
    2. If not found, look for any number in the response
    3. Validate range [1, num_options]
    4. Return None if unparseable
    """
    if not response or not response.strip():
        return None

    # Coba ambil angka dari baris terakhir
    last_line = response.strip().split('\n')[-1].strip()

    # Match standalone number
    match = re.search(r'\b(\d+)\b', last_line)
    if match:
        num = int(match.group(1))
        if 1 <= num <= num_options:
            return num

    # Fallback: cari semua angka di seluruh response, ambil yang terakhir
    all_numbers = re.findall(r'\b(\d+)\b', response)
    for num_str in reversed(all_numbers):
        num = int(num_str)
        if 1 <= num <= num_options:
            return num

    return None


# --- Abstract WSD Engine ---

class WSDEngine(ABC):
    """Abstract base class for WSD engines."""

    @abstractmethod
    def disambiguate(self, word: str, sentence: str, pos: Optional[str] = None,
                     question_text: str = "") -> Dict:
        """
        Disambiguate a word in context.

        Args:
            word: Target word to disambiguate
            sentence: Full sentence containing the word
            pos: WordNet POS (wn.NOUN, wn.VERB, etc.)
            question_text: Original exam question (for P3/P4 prompts)

        Returns:
            dict with keys:
                synset: WordNet synset object (or None)
                synset_id: Synset name string
                confidence: float [0, 1]
                method: str (e.g., 'lesk', 'qwen-2.5-P3')
                latency_ms: float
                raw_response: str (for LLM methods)
                fallback_used: bool
        """
        pass


# --- Lesk Implementation ---

class LeskWSD(WSDEngine):
    """NLTK Lesk algorithm — baseline WSD method."""

    def disambiguate(self, word: str, sentence: str, pos: Optional[str] = None,
                     question_text: str = "") -> Dict:
        start_time = time.time()

        tokens = word_tokenize(sentence.lower())
        result_synset = lesk(tokens, word.lower(), pos=pos)

        # Fallback ke most frequent sense (synset pertama)
        fallback_used = False
        if result_synset is None:
            synsets = wn.synsets(word.lower(), pos=pos)
            if synsets:
                result_synset = synsets[0]
                fallback_used = True

        latency_ms = (time.time() - start_time) * 1000

        return {
            'synset': result_synset,
            'synset_id': result_synset.name() if result_synset else None,
            'confidence': 1.0 if not fallback_used else 0.5,
            'method': 'lesk',
            'latency_ms': latency_ms,
            'raw_response': None,
            'fallback_used': fallback_used,
        }


# --- LLM WSD Implementation ---

class LLMWSD(WSDEngine):
    """LLM-based WSD engine supporting multiple models and prompt variants."""

    def __init__(self, model: str, prompt_variant: str = 'P1',
                 backend: str = 'ollama', api_key: Optional[str] = None,
                 max_retries: int = 3, retry_delay: float = 2.0):
        """
        Args:
            model: Model identifier
                Ollama: 'qwen2.5:7b', 'mistral:7b-instruct', 'llama3.1:8b'
                Gemini: 'gemini-1.5-flash'
            prompt_variant: 'P1', 'P2', 'P3', or 'P4'
            backend: 'ollama' or 'gemini'
            api_key: API key for Gemini (not needed for Ollama)
            max_retries: Maximum retry attempts on API failure
            retry_delay: Base delay between retries (seconds)
        """
        self.model = model
        self.prompt_variant = prompt_variant
        self.backend = backend
        self.api_key = api_key
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.client = self._init_client()

    def _init_client(self):
        """Initialize API client based on backend."""
        if self.backend == 'ollama':
            try:
                import requests
                # Verify Ollama is running
                resp = requests.get('http://localhost:11434/api/tags', timeout=5)
                resp.raise_for_status()
                return 'ollama'
            except Exception as e:
                logger.warning(f"Ollama not available: {e}. Will retry on each call.")
                return 'ollama'

        elif self.backend == 'gemini':
            try:
                import google.generativeai as genai
                genai.configure(api_key=self.api_key)
                return genai.GenerativeModel(self.model)
            except ImportError:
                raise ImportError("Install google-generativeai: pip install google-generativeai")

        else:
            raise ValueError(f"Unknown backend: {self.backend}")

    def _build_prompt(self, word: str, sentence: str, pos: str,
                      synsets: List, question_text: str) -> str:
        """Build prompt from template and parameters."""
        template = PROMPT_TEMPLATES[self.prompt_variant]

        # Format POS for display
        pos_display = {'n': 'noun', 'v': 'verb', 'a': 'adjective', 'r': 'adverb'}.get(pos, pos or 'word')

        include_examples = self.prompt_variant in ('P2', 'P3', 'P4')

        if include_examples:
            synset_list = format_synset_list(synsets, include_examples=True)
            return template.format(
                sentence=sentence, word=word, pos=pos_display,
                synset_list_with_examples=synset_list,
                question_text=question_text,
            )
        else:
            synset_list = format_synset_list(synsets, include_examples=False)
            return template.format(
                sentence=sentence, word=word, pos=pos_display,
                synset_list=synset_list,
                question_text=question_text,
            )

    def _call_ollama(self, prompt: str, max_tokens: int) -> str:
        """Call Ollama local API."""
        import requests

        payload = {
            'model': self.model,
            'prompt': prompt,
            'stream': False,
            'options': {
                'temperature': 0.0,
                'num_predict': max_tokens,
            }
        }

        response = requests.post(
            'http://localhost:11434/api/generate',
            json=payload,
            timeout=60,
        )
        response.raise_for_status()
        return response.json()['response']

    def _call_gemini(self, prompt: str, max_tokens: int) -> str:
        """Call Gemini API."""
        import google.generativeai as genai

        generation_config = genai.GenerationConfig(
            temperature=0.0,
            max_output_tokens=max_tokens,
        )

        response = self.client.generate_content(
            prompt,
            generation_config=generation_config,
        )
        return response.text

    def _call_llm(self, prompt: str, max_tokens: int) -> str:
        """Call LLM with retry logic."""
        for attempt in range(self.max_retries):
            try:
                if self.backend == 'ollama':
                    return self._call_ollama(prompt, max_tokens)
                elif self.backend == 'gemini':
                    return self._call_gemini(prompt, max_tokens)
            except Exception as e:
                logger.warning(f"LLM call failed (attempt {attempt + 1}/{self.max_retries}): {e}")
                if attempt < self.max_retries - 1:
                    delay = self.retry_delay * (2 ** attempt)
                    time.sleep(delay)
                else:
                    raise

    def disambiguate(self, word: str, sentence: str, pos: Optional[str] = None,
                     question_text: str = "") -> Dict:
        start_time = time.time()

        # Get candidate synsets
        synsets = wn.synsets(word.lower(), pos=pos)

        # If no synsets or only 1 synset, no disambiguation needed
        if len(synsets) == 0:
            return {
                'synset': None, 'synset_id': None,
                'confidence': 0.0, 'method': f'{self.model}-{self.prompt_variant}',
                'latency_ms': (time.time() - start_time) * 1000,
                'raw_response': None, 'fallback_used': False,
            }

        if len(synsets) == 1:
            return {
                'synset': synsets[0], 'synset_id': synsets[0].name(),
                'confidence': 1.0, 'method': f'{self.model}-{self.prompt_variant}',
                'latency_ms': (time.time() - start_time) * 1000,
                'raw_response': 'single_synset', 'fallback_used': False,
            }

        # Build prompt
        prompt = self._build_prompt(word, sentence, pos, synsets, question_text)

        # Determine max tokens based on prompt variant
        max_tokens = 300 if self.prompt_variant == 'P4' else 10

        # Call LLM
        try:
            raw_response = self._call_llm(prompt, max_tokens)
        except Exception as e:
            logger.error(f"LLM call failed for '{word}': {e}")
            # Fallback to Lesk
            lesk_engine = LeskWSD()
            result = lesk_engine.disambiguate(word, sentence, pos, question_text)
            result['method'] = f'{self.model}-{self.prompt_variant}-FALLBACK'
            result['fallback_used'] = True
            result['raw_response'] = f'ERROR: {e}'
            return result

        # Parse response
        choice = parse_synset_response(raw_response, len(synsets))

        if choice is not None:
            selected_synset = synsets[choice - 1]
            fallback_used = False
        else:
            # Unparseable response — fallback to Lesk
            logger.warning(f"Unparseable response for '{word}': {raw_response[:100]}")
            lesk_result = LeskWSD().disambiguate(word, sentence, pos, question_text)
            selected_synset = lesk_result['synset']
            fallback_used = True

        latency_ms = (time.time() - start_time) * 1000

        return {
            'synset': selected_synset,
            'synset_id': selected_synset.name() if selected_synset else None,
            'confidence': 0.9 if not fallback_used else 0.3,
            'method': f'{self.model}-{self.prompt_variant}',
            'latency_ms': latency_ms,
            'raw_response': raw_response,
            'fallback_used': fallback_used,
        }


# --- Batch Processing ---

def batch_disambiguate(engine: WSDEngine, words: List[Dict],
                       progress_interval: int = 100) -> List[Dict]:
    """
    Run WSD on a batch of words.

    Args:
        engine: WSD engine instance
        words: List of dicts with keys: word, sentence, pos_wn, question_text
        progress_interval: Log progress every N words

    Returns:
        List of result dicts (one per word)
    """
    results = []
    total = len(words)

    for i, item in enumerate(words):
        result = engine.disambiguate(
            word=item['word'],
            sentence=item['sentence'],
            pos=item.get('pos_wn'),
            question_text=item.get('question_text', ''),
        )
        result['word_id'] = item.get('word_id', i)
        result['word'] = item['word']
        result['sentence'] = item['sentence']
        results.append(result)

        if (i + 1) % progress_interval == 0:
            logger.info(f"Progress: {i + 1}/{total} ({(i+1)/total*100:.1f}%)")

    return results


# --- Factory ---

def create_wsd_engine(method: str, prompt_variant: str = 'P1',
                      api_key: Optional[str] = None) -> WSDEngine:
    """
    Factory function to create WSD engines.

    Args:
        method: 'lesk', 'qwen', 'mistral', 'llama', 'gemini'
        prompt_variant: 'P1', 'P2', 'P3', 'P4'
        api_key: Gemini API key (if needed)
    """
    if method == 'lesk':
        return LeskWSD()

    model_map = {
        'qwen': ('qwen2.5:7b', 'ollama'),
        'mistral': ('mistral:7b-instruct', 'ollama'),
        'llama': ('llama3.1:8b', 'ollama'),
        'gemini': ('gemini-1.5-flash', 'gemini'),
    }

    if method not in model_map:
        raise ValueError(f"Unknown method: {method}. Use: {list(model_map.keys())}")

    model_name, backend = model_map[method]
    return LLMWSD(
        model=model_name,
        prompt_variant=prompt_variant,
        backend=backend,
        api_key=api_key,
    )


if __name__ == '__main__':
    # Quick sanity test
    print("Testing Lesk WSD...")
    lesk_engine = LeskWSD()
    result = lesk_engine.disambiguate(
        word='stack',
        sentence='A stack is a data structure that uses LIFO ordering.',
        pos=wn.NOUN,
    )
    print(f"  'stack' → {result['synset_id']} (latency: {result['latency_ms']:.1f}ms)")

    print("\nTo test LLM WSD, ensure Ollama is running and models are pulled.")
    print("Example: LLMWSD(model='qwen2.5:7b', prompt_variant='P3')")
