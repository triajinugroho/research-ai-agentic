"""
Visualization Module — Publication-Ready Figures
=================================================
Generates all figures for Paper 1 in publication quality.
- 300 DPI, colorblind-safe palette
- IEEE two-column compatible sizes
- Both PDF and PNG output

Usage:
    python 05-visualization.py --results_dir ./data/results/ --output_dir ./paper/figures/
"""

import os
import argparse
from typing import Dict, List, Optional

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

# --- Publication Style Configuration ---

# Colorblind-safe palette (Wong, 2011 — Nature Methods)
COLORS = {
    'lesk': '#999999',       # Gray (baseline)
    'qwen': '#E69F00',       # Orange
    'mistral': '#56B4E9',    # Sky blue
    'llama': '#009E73',      # Bluish green
    'gemini': '#CC79A7',     # Reddish purple
}

METHOD_LABELS = {
    'lesk': 'Lesk (baseline)',
    'qwen': 'Qwen-2.5',
    'mistral': 'Mistral-7B',
    'llama': 'Llama-3.1-8B',
    'gemini': 'Gemini-1.5-Flash',
}

METHOD_ORDER = ['lesk', 'qwen', 'mistral', 'llama', 'gemini']

def setup_publication_style():
    """Configure matplotlib for IEEE publication quality."""
    plt.rcParams.update({
        'font.family': 'serif',
        'font.serif': ['Times New Roman', 'DejaVu Serif'],
        'font.size': 9,
        'axes.labelsize': 10,
        'axes.titlesize': 10,
        'xtick.labelsize': 8,
        'ytick.labelsize': 8,
        'legend.fontsize': 8,
        'figure.dpi': 300,
        'savefig.dpi': 300,
        'savefig.bbox': 'tight',
        'savefig.pad_inches': 0.05,
        'axes.linewidth': 0.8,
        'grid.linewidth': 0.5,
        'lines.linewidth': 1.2,
    })
    sns.set_style("whitegrid", {
        'grid.linestyle': '--',
        'grid.alpha': 0.5,
    })


# IEEE column widths
SINGLE_COL_WIDTH = 3.5   # inches (single column)
DOUBLE_COL_WIDTH = 7.16  # inches (double column)
FIG_HEIGHT = 2.5         # inches (default height)


def save_figure(fig, name: str, output_dir: str):
    """Save figure in both PDF and PNG formats."""
    os.makedirs(output_dir, exist_ok=True)
    fig.savefig(os.path.join(output_dir, f'{name}.pdf'), format='pdf')
    fig.savefig(os.path.join(output_dir, f'{name}.png'), format='png')
    plt.close(fig)
    print(f"  Saved: {name}.pdf, {name}.png")


# --- Figure 1: Pipeline Architecture ---
# Note: This is best created in a vector tool (draw.io, TikZ, etc.)
# Placeholder function generates a simplified version

def fig1_pipeline_architecture(output_dir: str):
    """
    Figure 1: Pipeline architecture diagram.
    For publication, consider replacing with TikZ or draw.io version.
    """
    fig, ax = plt.subplots(figsize=(DOUBLE_COL_WIDTH, 3.0))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)
    ax.axis('off')

    # Pipeline boxes
    boxes = [
        (0.5, 2, 'Preprocessing\n(Tokenize, POS Tag,\nContent Filter)'),
        (3.0, 2, 'WSD\n(Experimental\nVariable)'),
        (5.5, 2, 'SemSpace\nVector\nLookup'),
        (8.0, 2, 'MaLSTM\nScoring'),
    ]

    for x, y, text in boxes:
        color = '#FFD700' if 'WSD' in text else '#B0C4DE'
        bbox = dict(boxstyle='round,pad=0.5', facecolor=color,
                   edgecolor='black', linewidth=1.5 if 'WSD' in text else 0.8)
        ax.text(x, y, text, fontsize=8, ha='center', va='center', bbox=bbox)

    # Arrows
    for x_start in [1.5, 4.0, 6.5]:
        ax.annotate('', xy=(x_start + 0.5, 2), xytext=(x_start, 2),
                    arrowprops=dict(arrowstyle='->', lw=1.2))

    # Input/Output labels
    ax.text(0.5, 3.5, 'Input:\nStudent + Reference\nAnswers', fontsize=7,
            ha='center', va='center', style='italic')
    ax.text(9.5, 2, 'Score\n[0-5]', fontsize=8, ha='center', va='center',
            bbox=dict(boxstyle='round', facecolor='#90EE90', edgecolor='black'))

    ax.set_title('Figure 1: ASAG Pipeline Architecture (WSD step highlighted)',
                fontsize=9, fontweight='bold')

    save_figure(fig, 'fig1_pipeline_architecture', output_dir)


# --- Figure 2: WSD Accuracy by Ambiguity Level ---

def fig2_wsd_accuracy_by_ambiguity(accuracy_data: Optional[pd.DataFrame],
                                    output_dir: str):
    """
    Figure 2: Grouped bar chart of WSD accuracy by ambiguity level.

    Expected accuracy_data columns: method, ambiguity_level, accuracy, ci_lower, ci_upper
    """
    # Demo data (replace with actual after experiments)
    if accuracy_data is None:
        data = []
        np.random.seed(42)
        for method in METHOD_ORDER:
            for level in ['Low (2-3)', 'Medium (4-7)', 'High (8+)']:
                base = {'lesk': 55, 'qwen': 68, 'mistral': 65,
                        'llama': 63, 'gemini': 71}[method]
                penalty = {'Low (2-3)': 0, 'Medium (4-7)': -8, 'High (8+)': -18}[level]
                acc = base + penalty + np.random.randint(-3, 4)
                data.append({
                    'method': method, 'ambiguity_level': level,
                    'accuracy': acc, 'ci_lower': acc - 4, 'ci_upper': acc + 4,
                })
        accuracy_data = pd.DataFrame(data)

    fig, ax = plt.subplots(figsize=(SINGLE_COL_WIDTH, FIG_HEIGHT))

    levels = accuracy_data['ambiguity_level'].unique()
    x = np.arange(len(levels))
    width = 0.15
    offsets = np.arange(len(METHOD_ORDER)) - len(METHOD_ORDER) / 2 + 0.5

    for i, method in enumerate(METHOD_ORDER):
        method_data = accuracy_data[accuracy_data['method'] == method]
        accs = [method_data[method_data['ambiguity_level'] == l]['accuracy'].values[0]
                for l in levels]
        yerr_lo = [method_data[method_data['ambiguity_level'] == l]['accuracy'].values[0] -
                   method_data[method_data['ambiguity_level'] == l]['ci_lower'].values[0]
                   for l in levels]
        yerr_hi = [method_data[method_data['ambiguity_level'] == l]['ci_upper'].values[0] -
                   method_data[method_data['ambiguity_level'] == l]['accuracy'].values[0]
                   for l in levels]

        bars = ax.bar(x + offsets[i] * width, accs, width,
                      label=METHOD_LABELS[method], color=COLORS[method],
                      yerr=[yerr_lo, yerr_hi], capsize=2, edgecolor='black', linewidth=0.3)

    ax.set_xlabel('Ambiguity Level')
    ax.set_ylabel('WSD Accuracy (%)')
    ax.set_xticks(x)
    ax.set_xticklabels(levels)
    ax.legend(loc='upper right', framealpha=0.9, edgecolor='gray')
    ax.set_ylim(0, 100)
    ax.yaxis.set_major_locator(plt.MultipleLocator(20))

    fig.tight_layout()
    save_figure(fig, 'fig2_wsd_accuracy_by_ambiguity', output_dir)


# --- Figure 3: Per-Question Pearson r Distribution ---

def fig3_per_question_boxplot(per_q_data: Optional[pd.DataFrame], output_dir: str):
    """
    Figure 3: Box plot of per-question Pearson r across WSD conditions.

    Expected per_q_data columns: method, question_id, pearson_r
    """
    # Demo data
    if per_q_data is None:
        data = []
        np.random.seed(42)
        for method in METHOD_ORDER:
            base_r = {'lesk': 0.35, 'qwen': 0.42, 'mistral': 0.39,
                      'llama': 0.38, 'gemini': 0.44}[method]
            for q in range(87):
                r = np.clip(np.random.normal(base_r, 0.35), -1, 1)
                data.append({'method': method, 'question_id': q, 'pearson_r': r})
        per_q_data = pd.DataFrame(data)

    fig, ax = plt.subplots(figsize=(SINGLE_COL_WIDTH, FIG_HEIGHT))

    bp_data = [per_q_data[per_q_data['method'] == m]['pearson_r'].dropna().values
               for m in METHOD_ORDER]

    bp = ax.boxplot(bp_data, labels=[METHOD_LABELS[m] for m in METHOD_ORDER],
                    patch_artist=True, showfliers=True, flierprops={'markersize': 3})

    for patch, method in zip(bp['boxes'], METHOD_ORDER):
        patch.set_facecolor(COLORS[method])
        patch.set_alpha(0.7)

    ax.axhline(y=0, color='red', linestyle='--', linewidth=0.8, alpha=0.5)
    ax.set_ylabel('Per-Question Pearson r')
    ax.set_xticklabels([METHOD_LABELS[m].split('\n')[0] for m in METHOD_ORDER],
                       rotation=30, ha='right')

    fig.tight_layout()
    save_figure(fig, 'fig3_per_question_boxplot', output_dir)


# --- Figure 4: WSD Accuracy vs ASAG Improvement ---

def fig4_accuracy_vs_improvement(scatter_data: Optional[pd.DataFrame], output_dir: str):
    """
    Figure 4: Scatter plot — WSD accuracy vs change in aggregate Pearson r.

    Expected scatter_data columns: method, wsd_accuracy, delta_pearson_r
    """
    # Demo data
    if scatter_data is None:
        scatter_data = pd.DataFrame([
            {'method': 'qwen', 'wsd_accuracy': 68, 'delta_pearson_r': 0.05},
            {'method': 'mistral', 'wsd_accuracy': 65, 'delta_pearson_r': 0.03},
            {'method': 'llama', 'wsd_accuracy': 63, 'delta_pearson_r': 0.02},
            {'method': 'gemini', 'wsd_accuracy': 71, 'delta_pearson_r': 0.07},
        ])

    fig, ax = plt.subplots(figsize=(SINGLE_COL_WIDTH, SINGLE_COL_WIDTH))

    for _, row in scatter_data.iterrows():
        m = row['method']
        ax.scatter(row['wsd_accuracy'], row['delta_pearson_r'],
                  color=COLORS[m], s=100, edgecolors='black', linewidth=0.8,
                  zorder=5)
        ax.annotate(METHOD_LABELS[m], (row['wsd_accuracy'], row['delta_pearson_r']),
                   fontsize=7, xytext=(5, 5), textcoords='offset points')

    # Baseline reference
    ax.axhline(y=0, color='gray', linestyle='--', linewidth=0.8, alpha=0.5)

    ax.set_xlabel('WSD Accuracy (%)')
    ax.set_ylabel('Δ Aggregate Pearson r\n(vs. Lesk baseline)')

    fig.tight_layout()
    save_figure(fig, 'fig4_accuracy_vs_improvement', output_dir)


# --- Figure 5: Error Type Distribution ---

def fig5_error_distribution(error_data: Optional[pd.DataFrame], output_dir: str):
    """
    Figure 5: Stacked bar chart of error types per LLM.

    Expected error_data columns: method, error_type, count
    """
    # Demo data
    if error_data is None:
        error_data = pd.DataFrame([
            {'method': 'qwen', 'A: Domain': 12, 'B: POS': 8, 'C: Fine-grained': 25, 'D: OOV': 5},
            {'method': 'mistral', 'A: Domain': 18, 'B: POS': 10, 'C: Fine-grained': 22, 'D: OOV': 7},
            {'method': 'llama', 'A: Domain': 20, 'B: POS': 12, 'C: Fine-grained': 20, 'D: OOV': 8},
            {'method': 'gemini', 'A: Domain': 8, 'B: POS': 6, 'C: Fine-grained': 28, 'D: OOV': 3},
        ])

    fig, ax = plt.subplots(figsize=(SINGLE_COL_WIDTH, FIG_HEIGHT))

    error_types = ['A: Domain', 'B: POS', 'C: Fine-grained', 'D: OOV']
    error_colors = ['#D55E00', '#F0E442', '#0072B2', '#999999']

    methods = error_data['method'].values
    labels = [METHOD_LABELS.get(m, m) for m in methods]
    x = np.arange(len(methods))

    bottom = np.zeros(len(methods))
    for etype, color in zip(error_types, error_colors):
        values = error_data[etype].values
        ax.bar(x, values, bottom=bottom, label=etype, color=color,
               edgecolor='black', linewidth=0.3)
        bottom += values

    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=30, ha='right')
    ax.set_ylabel('Number of WSD Disagreements')
    ax.legend(title='Error Type', loc='upper right', fontsize=7)

    fig.tight_layout()
    save_figure(fig, 'fig5_error_distribution', output_dir)


# --- Figure 6: Prompt Sensitivity ---

def fig6_prompt_sensitivity(prompt_data: Optional[pd.DataFrame], output_dir: str):
    """
    Figure 6: Line chart showing WSD accuracy across prompt variants per LLM.
    """
    # Demo data
    if prompt_data is None:
        prompt_data = pd.DataFrame([
            {'method': 'qwen', 'P1': 62, 'P2': 65, 'P3': 68, 'P4': 66},
            {'method': 'mistral', 'P1': 58, 'P2': 62, 'P3': 65, 'P4': 63},
            {'method': 'llama', 'P1': 56, 'P2': 60, 'P3': 63, 'P4': 61},
            {'method': 'gemini', 'P1': 65, 'P2': 69, 'P3': 71, 'P4': 70},
        ])

    fig, ax = plt.subplots(figsize=(SINGLE_COL_WIDTH, FIG_HEIGHT))

    prompts = ['P1', 'P2', 'P3', 'P4']
    prompt_labels = ['P1: Basic', 'P2: Examples', 'P3: Domain', 'P4: CoT']

    for _, row in prompt_data.iterrows():
        m = row['method']
        values = [row[p] for p in prompts]
        ax.plot(range(4), values, marker='o', label=METHOD_LABELS[m],
                color=COLORS[m], linewidth=1.5, markersize=5)

    ax.set_xticks(range(4))
    ax.set_xticklabels(prompt_labels)
    ax.set_ylabel('WSD Accuracy (%)')
    ax.legend(loc='lower right', fontsize=7)

    fig.tight_layout()
    save_figure(fig, 'fig6_prompt_sensitivity', output_dir)


def generate_all_figures(output_dir: str):
    """Generate all publication figures (demo data)."""
    setup_publication_style()
    print("Generating publication-ready figures...")

    fig1_pipeline_architecture(output_dir)
    fig2_wsd_accuracy_by_ambiguity(None, output_dir)
    fig3_per_question_boxplot(None, output_dir)
    fig4_accuracy_vs_improvement(None, output_dir)
    fig5_error_distribution(None, output_dir)
    fig6_prompt_sensitivity(None, output_dir)

    print(f"\nAll figures saved to {output_dir}")


def main():
    parser = argparse.ArgumentParser(description='Generate publication figures')
    parser.add_argument('--results_dir', type=str, default='./data/results/')
    parser.add_argument('--output_dir', type=str, default='./paper/figures/')
    parser.add_argument('--demo', action='store_true', help='Generate with demo data')
    args = parser.parse_args()

    if args.demo:
        generate_all_figures(args.output_dir)
    else:
        print("Run with --demo for placeholder figures, or provide actual results.")


if __name__ == '__main__':
    main()
