"""
Mohler Dataset Loader
=====================
Loads and parses the Mohler et al. (2011) ASAG dataset.
Extracts content words and computes polysemy statistics.

Dataset: 87 questions, 2,273 student answers, Computer Science domain.
Source: https://www.cs.unt.edu/~rodrigo/data/

Usage:
    python 01-mohler-loader.py --data_dir ./data/mohler/ --output_dir ./data/processed/
"""

import os
import re
import json
import argparse
from collections import Counter
from typing import Dict, List, Tuple, Optional

import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn
from nltk.tag import pos_tag

# Download NLTK resources (run once)
nltk.download('punkt', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('averaged_perceptron_tagger_eng', quiet=True)


# --- POS Mapping ---

PENN_TO_WN = {
    'NN': wn.NOUN, 'NNS': wn.NOUN, 'NNP': wn.NOUN, 'NNPS': wn.NOUN,
    'VB': wn.VERB, 'VBD': wn.VERB, 'VBG': wn.VERB, 'VBN': wn.VERB,
    'VBP': wn.VERB, 'VBZ': wn.VERB,
    'JJ': wn.ADJ, 'JJR': wn.ADJ, 'JJS': wn.ADJ,
    'RB': wn.ADV, 'RBR': wn.ADV, 'RBS': wn.ADV,
}

CONTENT_POS = {'NN', 'NNS', 'NNP', 'NNPS', 'VB', 'VBD', 'VBG', 'VBN',
               'VBP', 'VBZ', 'JJ', 'JJR', 'JJS'}


def load_mohler_dataset(data_dir: str) -> pd.DataFrame:
    """
    Load Mohler dataset from directory.

    Expected structure:
        data_dir/
        ├── questions/       # One file per question
        ├── raw/             # Student answers
        ├── scores/          # Human grades
        └── ref_answers/     # Reference (model) answers

    Returns DataFrame with columns:
        question_id, question_text, reference_answer,
        student_answer, score_me, score_other, avg_score
    """
    records = []

    # Adaptasi format tergantung struktur file yang tersedia
    # Format 1: File terpisah per pertanyaan
    questions_dir = os.path.join(data_dir, 'questions')
    answers_dir = os.path.join(data_dir, 'raw')
    scores_dir = os.path.join(data_dir, 'scores')
    ref_dir = os.path.join(data_dir, 'ref_answers')

    if os.path.exists(questions_dir):
        for q_file in sorted(os.listdir(questions_dir)):
            q_id = q_file.replace('.txt', '')

            # Baca pertanyaan
            with open(os.path.join(questions_dir, q_file), 'r') as f:
                question_text = f.read().strip()

            # Baca reference answer
            ref_file = os.path.join(ref_dir, q_file)
            with open(ref_file, 'r') as f:
                ref_answer = f.read().strip()

            # Baca student answers dan scores
            ans_file = os.path.join(answers_dir, q_file)
            score_file = os.path.join(scores_dir, q_file)

            with open(ans_file, 'r') as f:
                student_answers = f.readlines()
            with open(score_file, 'r') as f:
                scores = f.readlines()

            for i, (answer, score_line) in enumerate(zip(student_answers, scores)):
                parts = score_line.strip().split()
                score_me = float(parts[0]) if len(parts) > 0 else 0.0
                score_other = float(parts[1]) if len(parts) > 1 else score_me

                records.append({
                    'question_id': q_id,
                    'question_text': question_text,
                    'reference_answer': ref_answer,
                    'student_answer': answer.strip(),
                    'answer_idx': i,
                    'score_me': score_me,
                    'score_other': score_other,
                    'avg_score': (score_me + score_other) / 2.0,
                })

    # Format 2: Single CSV file (alternative)
    csv_path = os.path.join(data_dir, 'mohler_dataset.csv')
    if os.path.exists(csv_path) and len(records) == 0:
        df = pd.read_csv(csv_path)
        return df

    df = pd.DataFrame(records)
    return df


def extract_content_words(text: str) -> List[Dict]:
    """
    Extract content words (nouns, verbs, adjectives) with POS tags.

    Returns list of dicts:
        [{'word': str, 'pos_penn': str, 'pos_wn': str, 'position': int}, ...]
    """
    tokens = word_tokenize(text.lower())
    tagged = pos_tag(tokens)

    content_words = []
    for i, (word, pos) in enumerate(tagged):
        if pos in CONTENT_POS and len(word) > 1 and word.isalpha():
            wn_pos = PENN_TO_WN.get(pos)
            content_words.append({
                'word': word,
                'pos_penn': pos,
                'pos_wn': wn_pos,
                'position': i,
            })

    return content_words


def get_polysemy_info(word: str, pos: Optional[str] = None) -> Dict:
    """
    Get WordNet polysemy information for a word.

    Returns dict with synset count, synset IDs, glosses.
    """
    synsets = wn.synsets(word, pos=pos)

    return {
        'word': word,
        'pos': pos,
        'num_synsets': len(synsets),
        'is_polysemous': len(synsets) >= 2,
        'synsets': [
            {
                'synset_id': s.name(),
                'gloss': s.definition(),
                'examples': s.examples(),
                'lexname': s.lexname(),
            }
            for s in synsets
        ],
    }


def compute_dataset_statistics(df: pd.DataFrame) -> Dict:
    """
    Compute comprehensive statistics for the Mohler dataset.
    """
    all_content_words = []

    # Ekstrak content words dari semua jawaban
    for _, row in df.iterrows():
        # Student answers
        words = extract_content_words(row['student_answer'])
        for w in words:
            w['source'] = 'student'
            w['question_id'] = row['question_id']
            w['sentence'] = row['student_answer']
        all_content_words.extend(words)

        # Reference answers (hanya sekali per pertanyaan)
        # Akan di-deduplicate nanti

    cw_df = pd.DataFrame(all_content_words)

    # Polysemy analysis
    unique_words = cw_df[['word', 'pos_wn']].drop_duplicates()
    polysemy_records = []

    for _, row in unique_words.iterrows():
        info = get_polysemy_info(row['word'], row['pos_wn'])
        polysemy_records.append({
            'word': row['word'],
            'pos_wn': row['pos_wn'],
            'num_synsets': info['num_synsets'],
            'is_polysemous': info['is_polysemous'],
        })

    poly_df = pd.DataFrame(polysemy_records)

    stats = {
        'dataset': {
            'num_questions': df['question_id'].nunique(),
            'num_answers': len(df),
            'avg_answer_length': df['student_answer'].str.split().str.len().mean(),
            'std_answer_length': df['student_answer'].str.split().str.len().std(),
            'score_mean': df['avg_score'].mean(),
            'score_std': df['avg_score'].std(),
        },
        'content_words': {
            'total_extracted': len(cw_df),
            'unique_words': len(unique_words),
            'total_polysemous': int(poly_df['is_polysemous'].sum()),
            'pct_polysemous': float(poly_df['is_polysemous'].mean() * 100),
        },
        'polysemy_distribution': {
            'monosemous_1': int((poly_df['num_synsets'] == 1).sum()),
            'low_2_3': int(((poly_df['num_synsets'] >= 2) & (poly_df['num_synsets'] <= 3)).sum()),
            'medium_4_7': int(((poly_df['num_synsets'] >= 4) & (poly_df['num_synsets'] <= 7)).sum()),
            'high_8_plus': int((poly_df['num_synsets'] >= 8).sum()),
        },
        'top_polysemous_words': poly_df.nlargest(20, 'num_synsets')[['word', 'pos_wn', 'num_synsets']].to_dict('records'),
    }

    return stats, cw_df, poly_df


def stratified_sample(poly_df: pd.DataFrame,
                      n_low: int = 200,
                      n_med: int = 200,
                      n_high: int = 100,
                      seed: int = 42) -> pd.DataFrame:
    """
    Stratified sampling of polysemous words for gold standard construction.

    Strata:
        - Low ambiguity: 2-3 synsets (n=200)
        - Medium ambiguity: 4-7 synsets (n=200)
        - High ambiguity: 8+ synsets (n=100)
    """
    poly_only = poly_df[poly_df['is_polysemous']].copy()

    # Assign ambiguity level
    conditions = [
        (poly_only['num_synsets'] >= 2) & (poly_only['num_synsets'] <= 3),
        (poly_only['num_synsets'] >= 4) & (poly_only['num_synsets'] <= 7),
        poly_only['num_synsets'] >= 8,
    ]
    labels = ['low', 'medium', 'high']
    poly_only['ambiguity_level'] = pd.np.select(conditions, labels, default='low') if hasattr(pd, 'np') else 'low'

    # Manually assign since pd.np might not exist
    poly_only.loc[(poly_only['num_synsets'] >= 2) & (poly_only['num_synsets'] <= 3), 'ambiguity_level'] = 'low'
    poly_only.loc[(poly_only['num_synsets'] >= 4) & (poly_only['num_synsets'] <= 7), 'ambiguity_level'] = 'medium'
    poly_only.loc[poly_only['num_synsets'] >= 8, 'ambiguity_level'] = 'high'

    samples = []
    for level, n_target in [('low', n_low), ('medium', n_med), ('high', n_high)]:
        stratum = poly_only[poly_only['ambiguity_level'] == level]
        n_actual = min(n_target, len(stratum))
        sample = stratum.sample(n=n_actual, random_state=seed)
        samples.append(sample)

    result = pd.concat(samples, ignore_index=True)
    print(f"Sampled {len(result)} words: "
          f"low={len(result[result['ambiguity_level']=='low'])}, "
          f"medium={len(result[result['ambiguity_level']=='medium'])}, "
          f"high={len(result[result['ambiguity_level']=='high'])}")

    return result


def main():
    parser = argparse.ArgumentParser(description='Load and analyze Mohler ASAG dataset')
    parser.add_argument('--data_dir', type=str, default='./data/mohler/',
                        help='Path to Mohler dataset directory')
    parser.add_argument('--output_dir', type=str, default='./data/processed/',
                        help='Path to save processed data')
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    # 1. Load dataset
    print("Loading Mohler dataset...")
    df = load_mohler_dataset(args.data_dir)
    print(f"  Loaded {len(df)} answers for {df['question_id'].nunique()} questions")

    # 2. Compute statistics
    print("\nComputing dataset statistics...")
    stats, cw_df, poly_df = compute_dataset_statistics(df)

    # 3. Save results
    df.to_csv(os.path.join(args.output_dir, 'mohler_parsed.csv'), index=False)
    cw_df.to_csv(os.path.join(args.output_dir, 'content_words.csv'), index=False)
    poly_df.to_csv(os.path.join(args.output_dir, 'polysemy_info.csv'), index=False)

    with open(os.path.join(args.output_dir, 'dataset_stats.json'), 'w') as f:
        json.dump(stats, f, indent=2, default=str)

    # 4. Generate gold standard sample
    print("\nGenerating stratified sample for gold standard...")
    sample = stratified_sample(poly_df)
    sample.to_csv(os.path.join(args.output_dir, 'gold_standard_sample.csv'), index=False)

    # 5. Print summary
    print("\n=== Dataset Summary ===")
    print(f"Questions: {stats['dataset']['num_questions']}")
    print(f"Answers: {stats['dataset']['num_answers']}")
    print(f"Avg answer length: {stats['dataset']['avg_answer_length']:.1f} ± {stats['dataset']['std_answer_length']:.1f} words")
    print(f"Content words (unique): {stats['content_words']['unique_words']}")
    print(f"Polysemous words: {stats['content_words']['total_polysemous']} ({stats['content_words']['pct_polysemous']:.1f}%)")
    print(f"\nPolysemy distribution:")
    for k, v in stats['polysemy_distribution'].items():
        print(f"  {k}: {v}")

    print(f"\nAll outputs saved to {args.output_dir}")


if __name__ == '__main__':
    main()
