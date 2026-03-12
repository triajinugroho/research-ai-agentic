"""
Full SemSpace-MaLSTM Pipeline Runner
====================================
Runs the complete ASAG pipeline for all WSD conditions:
  Content Words → WSD → SemSpace Vectors → MaLSTM → Score

Usage:
    python 03-pipeline-runner.py --wsd_method lesk --output_dir ./data/results/
    python 03-pipeline-runner.py --wsd_method qwen --prompt P3 --output_dir ./data/results/
"""

import os
import json
import time
import argparse
import logging
from typing import List, Dict, Optional, Tuple

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from nltk.corpus import wordnet as wn

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)


# --- SemSpace Vector Lookup ---

class SemSpaceVectors:
    """
    SemSpace sense vector lookup.

    Loads pre-trained synset → vector mappings.
    Fallback: zero vector for unknown synsets.
    """

    def __init__(self, vectors_path: str, dim: int = 300):
        self.dim = dim
        self.vectors = {}
        self.zero_vector = np.zeros(dim)
        self.hit_count = 0
        self.miss_count = 0

        if os.path.exists(vectors_path):
            self._load_vectors(vectors_path)
            logger.info(f"Loaded {len(self.vectors)} SemSpace vectors (dim={dim})")
        else:
            logger.warning(f"SemSpace vectors not found at {vectors_path}. "
                          f"Using zero vectors (Plan B needed).")

    def _load_vectors(self, path: str):
        """
        Load vectors from file.
        Expected format: one line per synset: "synset_id v1 v2 v3 ... vN"
        """
        with open(path, 'r') as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) == self.dim + 1:
                    synset_id = parts[0]
                    vector = np.array([float(x) for x in parts[1:]])
                    self.vectors[synset_id] = vector

    def get_vector(self, synset_id: str) -> np.ndarray:
        """Look up sense vector for a synset."""
        if synset_id in self.vectors:
            self.hit_count += 1
            return self.vectors[synset_id]
        else:
            self.miss_count += 1
            return self.zero_vector.copy()

    def get_coverage_stats(self) -> Dict:
        total = self.hit_count + self.miss_count
        return {
            'total_lookups': total,
            'hits': self.hit_count,
            'misses': self.miss_count,
            'coverage': self.hit_count / total if total > 0 else 0,
        }


# --- MaLSTM (Manhattan LSTM) ---

class MaLSTM(nn.Module):
    """
    Manhattan LSTM for sequence similarity.

    Takes two sequences of sense vectors, passes through shared LSTM,
    computes Manhattan distance between final hidden states.
    Score = exp(-||h1 - h2||_1) scaled to [0, 5].

    Reference: Mueller & Thyagarajan (2016)
    """

    def __init__(self, input_dim: int = 300, hidden_dim: int = 50):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.lstm = nn.LSTM(input_dim, hidden_dim, batch_first=True)

    def forward_one(self, sequence: torch.Tensor) -> torch.Tensor:
        """
        Process one sequence through LSTM.

        Args:
            sequence: (batch, seq_len, input_dim)
        Returns:
            Final hidden state: (batch, hidden_dim)
        """
        _, (h_n, _) = self.lstm(sequence)
        return h_n.squeeze(0)  # (batch, hidden_dim)

    def forward(self, seq1: torch.Tensor, seq2: torch.Tensor) -> torch.Tensor:
        """
        Compute Manhattan similarity between two sequences.

        Returns:
            Similarity scores: (batch,) in range [0, 1]
        """
        h1 = self.forward_one(seq1)
        h2 = self.forward_one(seq2)

        # Manhattan distance
        manhattan_dist = torch.sum(torch.abs(h1 - h2), dim=1)

        # Convert to similarity: exp(-distance)
        similarity = torch.exp(-manhattan_dist)
        return similarity


def compute_asag_score(similarity: float, scale: float = 5.0) -> float:
    """Convert MaLSTM similarity [0,1] to grade [0, scale]."""
    return similarity * scale


# --- Pipeline Runner ---

class ASAGPipeline:
    """
    Complete ASAG pipeline: WSD → SemSpace → MaLSTM → Score.
    """

    def __init__(self, wsd_engine, semspace: SemSpaceVectors,
                 malstm: MaLSTM, device: str = 'cpu'):
        self.wsd_engine = wsd_engine
        self.semspace = semspace
        self.malstm = malstm
        self.device = device
        self.malstm.to(device)
        self.malstm.eval()

    def _text_to_sense_vectors(self, text: str, question_text: str = "") -> List[np.ndarray]:
        """
        Convert text to sequence of sense vectors.
        Steps: tokenize → extract content words → WSD → SemSpace lookup
        """
        from wsd_engine import extract_content_words  # type: ignore

        # Import from 01-mohler-loader
        import sys
        sys.path.insert(0, os.path.dirname(__file__))

        from importlib import import_module
        try:
            loader = import_module('01-mohler-loader')
            extract_fn = loader.extract_content_words
        except (ImportError, ModuleNotFoundError):
            # Fallback: inline extraction
            import nltk
            from nltk.tokenize import word_tokenize
            from nltk.tag import pos_tag

            CONTENT_POS = {'NN', 'NNS', 'NNP', 'NNPS', 'VB', 'VBD', 'VBG',
                          'VBN', 'VBP', 'VBZ', 'JJ', 'JJR', 'JJS'}
            PENN_TO_WN = {
                'NN': wn.NOUN, 'NNS': wn.NOUN, 'NNP': wn.NOUN, 'NNPS': wn.NOUN,
                'VB': wn.VERB, 'VBD': wn.VERB, 'VBG': wn.VERB, 'VBN': wn.VERB,
                'VBP': wn.VERB, 'VBZ': wn.VERB,
                'JJ': wn.ADJ, 'JJR': wn.ADJ, 'JJS': wn.ADJ,
            }

            tokens = word_tokenize(text.lower())
            tagged = pos_tag(tokens)
            content_words = []
            for word, pos in tagged:
                if pos in CONTENT_POS and len(word) > 1 and word.isalpha():
                    content_words.append({
                        'word': word, 'pos_wn': PENN_TO_WN.get(pos),
                    })
            extract_fn = None  # Not used in this fallback path

        if extract_fn:
            content_words = extract_fn(text)

        vectors = []
        for cw in content_words:
            # WSD
            result = self.wsd_engine.disambiguate(
                word=cw['word'],
                sentence=text,
                pos=cw.get('pos_wn'),
                question_text=question_text,
            )

            # SemSpace lookup
            if result['synset_id']:
                vec = self.semspace.get_vector(result['synset_id'])
            else:
                vec = self.semspace.zero_vector.copy()

            vectors.append(vec)

        return vectors

    def predict_score(self, student_answer: str, reference_answer: str,
                      question_text: str = "") -> Dict:
        """
        Predict ASAG score for a student answer.

        Returns dict with predicted_score, similarity, and metadata.
        """
        start_time = time.time()

        # Convert to sense vectors
        student_vectors = self._text_to_sense_vectors(student_answer, question_text)
        reference_vectors = self._text_to_sense_vectors(reference_answer, question_text)

        # Handle empty sequences
        if len(student_vectors) == 0 or len(reference_vectors) == 0:
            return {
                'predicted_score': 0.0,
                'similarity': 0.0,
                'student_vec_count': len(student_vectors),
                'reference_vec_count': len(reference_vectors),
                'latency_ms': (time.time() - start_time) * 1000,
                'error': 'empty_sequence',
            }

        # Pad/truncate sequences to same length (or handle variable length)
        # MaLSTM handles variable length via LSTM
        with torch.no_grad():
            s_tensor = torch.FloatTensor([student_vectors]).to(self.device)
            r_tensor = torch.FloatTensor([reference_vectors]).to(self.device)
            similarity = self.malstm(s_tensor, r_tensor).item()

        predicted_score = compute_asag_score(similarity)
        latency_ms = (time.time() - start_time) * 1000

        return {
            'predicted_score': round(predicted_score, 4),
            'similarity': round(similarity, 6),
            'student_vec_count': len(student_vectors),
            'reference_vec_count': len(reference_vectors),
            'latency_ms': round(latency_ms, 2),
            'error': None,
        }


def run_experiment(dataset_path: str, wsd_method: str,
                   prompt_variant: str, semspace_path: str,
                   output_dir: str, api_key: Optional[str] = None):
    """
    Run full ASAG experiment for one WSD condition.
    """
    os.makedirs(output_dir, exist_ok=True)

    # Load dataset
    df = pd.read_csv(dataset_path)
    logger.info(f"Loaded {len(df)} answers")

    # Initialize components
    from importlib import import_module
    sys_path_added = False
    import sys
    if os.path.dirname(__file__) not in sys.path:
        sys.path.insert(0, os.path.dirname(__file__))
        sys_path_added = True

    wsd_mod = import_module('02-wsd-engine')
    wsd_engine = wsd_mod.create_wsd_engine(wsd_method, prompt_variant, api_key)

    semspace = SemSpaceVectors(semspace_path)
    malstm = MaLSTM(input_dim=300, hidden_dim=50)
    # TODO: Load pre-trained MaLSTM weights if available
    # malstm.load_state_dict(torch.load('malstm_weights.pt'))

    pipeline = ASAGPipeline(wsd_engine, semspace, malstm)

    # Run pipeline on all answers
    results = []
    total = len(df)

    for i, row in df.iterrows():
        result = pipeline.predict_score(
            student_answer=row['student_answer'],
            reference_answer=row['reference_answer'],
            question_text=row.get('question_text', ''),
        )
        result['question_id'] = row['question_id']
        result['answer_idx'] = row.get('answer_idx', i)
        result['actual_score'] = row['avg_score']
        result['wsd_method'] = wsd_method
        result['prompt_variant'] = prompt_variant
        results.append(result)

        if (i + 1) % 100 == 0:
            logger.info(f"Progress: {i + 1}/{total} ({(i+1)/total*100:.1f}%)")

    # Save results
    results_df = pd.DataFrame(results)
    output_file = os.path.join(output_dir, f'asag_scores_{wsd_method}_{prompt_variant}.csv')
    results_df.to_csv(output_file, index=False)
    logger.info(f"Results saved to {output_file}")

    # Print summary
    from scipy.stats import pearsonr
    valid = results_df[results_df['error'].isna()]
    if len(valid) > 0:
        r, p = pearsonr(valid['predicted_score'], valid['actual_score'])
        rmse = np.sqrt(np.mean((valid['predicted_score'] - valid['actual_score']) ** 2))
        logger.info(f"\n=== Results: {wsd_method} ({prompt_variant}) ===")
        logger.info(f"  Aggregate Pearson r: {r:.4f} (p={p:.2e})")
        logger.info(f"  Aggregate RMSE: {rmse:.4f}")
        logger.info(f"  Valid predictions: {len(valid)}/{total}")
        logger.info(f"  SemSpace coverage: {semspace.get_coverage_stats()}")

    return results_df


def main():
    parser = argparse.ArgumentParser(description='Run ASAG pipeline experiment')
    parser.add_argument('--dataset', type=str, default='./data/processed/mohler_parsed.csv')
    parser.add_argument('--wsd_method', type=str, required=True,
                        choices=['lesk', 'qwen', 'mistral', 'llama', 'gemini'])
    parser.add_argument('--prompt', type=str, default='P1',
                        choices=['P1', 'P2', 'P3', 'P4'])
    parser.add_argument('--semspace', type=str, default='./data/semspace/vectors.txt')
    parser.add_argument('--output_dir', type=str, default='./data/results/pipeline/')
    parser.add_argument('--gemini_key', type=str, default=None)
    args = parser.parse_args()

    run_experiment(
        dataset_path=args.dataset,
        wsd_method=args.wsd_method,
        prompt_variant=args.prompt,
        semspace_path=args.semspace,
        output_dir=args.output_dir,
        api_key=args.gemini_key,
    )


if __name__ == '__main__':
    main()
