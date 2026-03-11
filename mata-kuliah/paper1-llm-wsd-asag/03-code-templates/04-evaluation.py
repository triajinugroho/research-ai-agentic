"""
Evaluation Module — Metrics & Statistical Tests
================================================
Computes all evaluation metrics for Paper 1:
- Intrinsic: WSD accuracy, McNemar's test
- Extrinsic: Pearson r, RMSE, paired t-test, Wilcoxon
- Inter-annotator agreement: Cohen's Kappa

Usage:
    python 04-evaluation.py --results_dir ./data/results/ --gold_standard ./data/gold_standard/gold_standard.csv
"""

import os
import json
import argparse
from typing import Dict, List, Tuple, Optional
from itertools import combinations

import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import pearsonr, spearmanr, wilcoxon
from sklearn.metrics import cohen_kappa_score, confusion_matrix


# --- Intrinsic WSD Evaluation ---

def compute_wsd_accuracy(predictions: pd.Series, gold: pd.Series) -> Dict:
    """
    Compute WSD accuracy and confidence interval.

    Args:
        predictions: Series of predicted synset IDs
        gold: Series of gold standard synset IDs

    Returns:
        Dict with accuracy, CI, counts
    """
    valid = predictions.notna() & gold.notna()
    pred_valid = predictions[valid]
    gold_valid = gold[valid]

    correct = (pred_valid == gold_valid).sum()
    total = len(pred_valid)
    accuracy = correct / total if total > 0 else 0

    # Wilson score 95% CI
    z = 1.96
    p_hat = accuracy
    n = total
    denom = 1 + z**2 / n
    center = (p_hat + z**2 / (2 * n)) / denom
    margin = z * np.sqrt((p_hat * (1 - p_hat) + z**2 / (4 * n)) / n) / denom

    return {
        'accuracy': accuracy,
        'correct': int(correct),
        'total': int(total),
        'ci_lower': max(0, center - margin),
        'ci_upper': min(1, center + margin),
    }


def compute_accuracy_by_stratum(predictions: pd.Series, gold: pd.Series,
                                 strata: pd.Series) -> Dict[str, Dict]:
    """Compute accuracy per stratum (ambiguity level, POS, etc.)."""
    results = {}
    for stratum_val in strata.unique():
        mask = strata == stratum_val
        results[str(stratum_val)] = compute_wsd_accuracy(
            predictions[mask], gold[mask]
        )
    return results


def mcnemar_test(pred_a: pd.Series, pred_b: pd.Series, gold: pd.Series) -> Dict:
    """
    McNemar's test for comparing two WSD methods.

    Tests whether the two methods disagree with the gold standard
    in systematically different ways.

    Returns chi-squared statistic, p-value, and effect size (Cohen's h).
    """
    a_correct = (pred_a == gold)
    b_correct = (pred_b == gold)

    # Contingency table
    both_correct = (a_correct & b_correct).sum()
    a_only = (a_correct & ~b_correct).sum()
    b_only = (~a_correct & b_correct).sum()
    both_wrong = (~a_correct & ~b_correct).sum()

    # McNemar's chi-squared (with continuity correction)
    n_discordant = a_only + b_only
    if n_discordant == 0:
        return {
            'chi2': 0.0, 'p_value': 1.0, 'cohens_h': 0.0,
            'a_only_correct': int(a_only), 'b_only_correct': int(b_only),
            'significant': False,
        }

    chi2 = (abs(a_only - b_only) - 1) ** 2 / (a_only + b_only)
    p_value = 1 - stats.chi2.cdf(chi2, df=1)

    # Effect size: Cohen's h for proportion differences
    p_a = a_correct.mean()
    p_b = b_correct.mean()
    cohens_h = 2 * np.arcsin(np.sqrt(p_a)) - 2 * np.arcsin(np.sqrt(p_b))

    return {
        'chi2': float(chi2),
        'p_value': float(p_value),
        'cohens_h': float(cohens_h),
        'a_only_correct': int(a_only),
        'b_only_correct': int(b_only),
        'significant': p_value < 0.05,
    }


def pairwise_mcnemar(results_dict: Dict[str, pd.Series], gold: pd.Series,
                     alpha: float = 0.05) -> pd.DataFrame:
    """
    Run pairwise McNemar tests between all WSD methods.
    Apply Bonferroni correction.
    """
    methods = list(results_dict.keys())
    n_comparisons = len(list(combinations(methods, 2)))
    bonferroni_alpha = alpha / n_comparisons

    rows = []
    for m_a, m_b in combinations(methods, 2):
        result = mcnemar_test(results_dict[m_a], results_dict[m_b], gold)
        result['method_a'] = m_a
        result['method_b'] = m_b
        result['bonferroni_significant'] = result['p_value'] < bonferroni_alpha
        result['bonferroni_alpha'] = bonferroni_alpha
        rows.append(result)

    return pd.DataFrame(rows)


# --- Extrinsic ASAG Evaluation ---

def compute_asag_metrics(predicted: pd.Series, actual: pd.Series,
                         question_ids: Optional[pd.Series] = None) -> Dict:
    """
    Compute ASAG evaluation metrics.

    Returns:
        Aggregate Pearson r, RMSE, and per-question metrics if question_ids provided.
    """
    valid = predicted.notna() & actual.notna()
    pred = predicted[valid]
    act = actual[valid]

    # Aggregate metrics
    agg_r, agg_p = pearsonr(pred, act)
    agg_rmse = np.sqrt(np.mean((pred - act) ** 2))
    agg_mae = np.mean(np.abs(pred - act))

    result = {
        'aggregate': {
            'pearson_r': float(agg_r),
            'pearson_p': float(agg_p),
            'rmse': float(agg_rmse),
            'mae': float(agg_mae),
            'n': int(len(pred)),
        }
    }

    # Per-question metrics
    if question_ids is not None:
        qids = question_ids[valid]
        per_q = []
        for qid in qids.unique():
            q_mask = qids == qid
            q_pred = pred[q_mask]
            q_act = act[q_mask]

            if len(q_pred) >= 3:  # Minimum 3 answers for meaningful correlation
                q_r, q_p = pearsonr(q_pred, q_act)
                q_rmse = np.sqrt(np.mean((q_pred - q_act) ** 2))
            else:
                q_r, q_p, q_rmse = np.nan, np.nan, np.nan

            per_q.append({
                'question_id': qid,
                'pearson_r': float(q_r) if not np.isnan(q_r) else None,
                'pearson_p': float(q_p) if not np.isnan(q_p) else None,
                'rmse': float(q_rmse) if not np.isnan(q_rmse) else None,
                'n_answers': int(len(q_pred)),
            })

        per_q_df = pd.DataFrame(per_q)
        valid_r = per_q_df['pearson_r'].dropna()

        result['per_question'] = per_q
        result['per_question_summary'] = {
            'mean_r': float(valid_r.mean()) if len(valid_r) > 0 else None,
            'median_r': float(valid_r.median()) if len(valid_r) > 0 else None,
            'std_r': float(valid_r.std()) if len(valid_r) > 0 else None,
            'min_r': float(valid_r.min()) if len(valid_r) > 0 else None,
            'max_r': float(valid_r.max()) if len(valid_r) > 0 else None,
            'n_questions_valid': int(len(valid_r)),
        }

    return result


def compare_asag_conditions(baseline_results: pd.DataFrame,
                            treatment_results: pd.DataFrame,
                            question_col: str = 'question_id') -> Dict:
    """
    Statistical comparison between two ASAG conditions using per-question Pearson r.

    Returns: paired t-test, Wilcoxon signed-rank, Cohen's d
    """
    # Compute per-question Pearson for both conditions
    baseline_per_q = {}
    for qid, group in baseline_results.groupby(question_col):
        if len(group) >= 3:
            r, _ = pearsonr(group['predicted_score'], group['actual_score'])
            baseline_per_q[qid] = r

    treatment_per_q = {}
    for qid, group in treatment_results.groupby(question_col):
        if len(group) >= 3:
            r, _ = pearsonr(group['predicted_score'], group['actual_score'])
            treatment_per_q[qid] = r

    # Align on common questions
    common_qs = set(baseline_per_q.keys()) & set(treatment_per_q.keys())
    b_values = np.array([baseline_per_q[q] for q in common_qs])
    t_values = np.array([treatment_per_q[q] for q in common_qs])

    # Remove NaN pairs
    valid = ~(np.isnan(b_values) | np.isnan(t_values))
    b_valid = b_values[valid]
    t_valid = t_values[valid]

    if len(b_valid) < 3:
        return {'error': 'Too few valid question pairs for comparison'}

    # Paired t-test
    t_stat, t_pvalue = stats.ttest_rel(t_valid, b_valid)

    # Wilcoxon signed-rank
    try:
        w_stat, w_pvalue = wilcoxon(t_valid - b_valid)
    except ValueError:
        w_stat, w_pvalue = np.nan, np.nan

    # Cohen's d (paired)
    diff = t_valid - b_valid
    cohens_d = diff.mean() / diff.std() if diff.std() > 0 else 0

    return {
        'n_questions': int(len(b_valid)),
        'baseline_mean_r': float(b_valid.mean()),
        'treatment_mean_r': float(t_valid.mean()),
        'mean_improvement': float(diff.mean()),
        'paired_t': {
            'statistic': float(t_stat),
            'p_value': float(t_pvalue),
        },
        'wilcoxon': {
            'statistic': float(w_stat) if not np.isnan(w_stat) else None,
            'p_value': float(w_pvalue) if not np.isnan(w_pvalue) else None,
        },
        'cohens_d': float(cohens_d),
        'improved_questions': int((diff > 0).sum()),
        'degraded_questions': int((diff < 0).sum()),
        'unchanged_questions': int((diff == 0).sum()),
    }


# --- Inter-Annotator Agreement ---

def compute_iaa(annotator_1: pd.Series, annotator_2: pd.Series) -> Dict:
    """
    Compute inter-annotator agreement using Cohen's Kappa.
    """
    valid = annotator_1.notna() & annotator_2.notna()
    a1 = annotator_1[valid]
    a2 = annotator_2[valid]

    kappa = cohen_kappa_score(a1, a2)

    # Percentage agreement
    pct_agree = (a1 == a2).mean()

    # Interpretation
    if kappa > 0.8:
        interpretation = 'almost perfect'
    elif kappa > 0.6:
        interpretation = 'substantial'
    elif kappa > 0.4:
        interpretation = 'moderate'
    elif kappa > 0.2:
        interpretation = 'fair'
    else:
        interpretation = 'poor'

    return {
        'cohens_kappa': float(kappa),
        'percentage_agreement': float(pct_agree),
        'interpretation': interpretation,
        'n_items': int(len(a1)),
        'n_disagreements': int((a1 != a2).sum()),
    }


# --- Error Cascade Analysis ---

def analyze_error_cascade(baseline_wsd: pd.DataFrame, treatment_wsd: pd.DataFrame,
                          baseline_scores: pd.DataFrame, treatment_scores: pd.DataFrame) -> Dict:
    """
    Analyze how WSD differences cascade into score differences.

    Identifies high-impact WSD disagreements between baseline and treatment.
    """
    # Merge WSD results
    merged_wsd = baseline_wsd.merge(
        treatment_wsd,
        on=['word_id', 'word'],
        suffixes=('_baseline', '_treatment'),
    )

    # Find disagreements
    disagreements = merged_wsd[
        merged_wsd['synset_id_baseline'] != merged_wsd['synset_id_treatment']
    ]

    # Merge with score differences
    score_diff = baseline_scores.merge(
        treatment_scores,
        on=['question_id', 'answer_idx'],
        suffixes=('_baseline', '_treatment'),
    )
    score_diff['score_delta'] = (
        score_diff['predicted_score_treatment'] - score_diff['predicted_score_baseline']
    )

    # Find high-impact cases
    high_impact = score_diff[score_diff['score_delta'].abs() > 0.5]

    return {
        'total_wsd_decisions': len(merged_wsd),
        'wsd_disagreements': len(disagreements),
        'disagreement_rate': len(disagreements) / len(merged_wsd) if len(merged_wsd) > 0 else 0,
        'high_impact_answers': len(high_impact),
        'mean_score_delta': float(score_diff['score_delta'].mean()),
        'std_score_delta': float(score_diff['score_delta'].std()),
        'max_positive_delta': float(score_diff['score_delta'].max()),
        'max_negative_delta': float(score_diff['score_delta'].min()),
    }


# --- Report Generation ---

def generate_evaluation_report(intrinsic_results: Dict, extrinsic_results: Dict,
                                comparison_results: Dict, output_path: str):
    """Generate comprehensive evaluation report as JSON."""
    report = {
        'intrinsic_wsd': intrinsic_results,
        'extrinsic_asag': extrinsic_results,
        'statistical_comparison': comparison_results,
        'generated_at': pd.Timestamp.now().isoformat(),
    }

    with open(output_path, 'w') as f:
        json.dump(report, f, indent=2, default=str)

    print(f"Report saved to {output_path}")
    return report


def main():
    parser = argparse.ArgumentParser(description='Evaluate WSD and ASAG results')
    parser.add_argument('--results_dir', type=str, default='./data/results/')
    parser.add_argument('--gold_standard', type=str, default='./data/gold_standard/gold_standard.csv')
    parser.add_argument('--output_dir', type=str, default='./data/results/evaluation/')
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    print(f"Evaluation module ready. Results dir: {args.results_dir}")
    print("Run with actual data after experiments are complete.")


if __name__ == '__main__':
    main()
