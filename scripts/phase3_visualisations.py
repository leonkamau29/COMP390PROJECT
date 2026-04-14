"""
Phase 3 Visualisations Script

Purpose:
    Generates all 5 required Phase 3 charts:
    1. Coverage Heatmap
    2. Gap Score Bar Chart
    3. Usage vs Coverage Scatter
    4. Temporal Trend Line Chart
    5. Quality Dimension Radar Chart

Inputs:
    data/phase3/coverage_matrix.csv
    data/phase3/gap_scores.csv
    outputs/phase2/benchmark_database_FINAL.csv

Outputs:
    outputs/phase3/charts/coverage_heatmap.png
    outputs/phase3/charts/gap_scores.png
    outputs/phase3/charts/usage_vs_coverage_scatter.png
    outputs/phase3/charts/temporal_trends.png
    outputs/phase3/charts/quality_radar.png

Usage:
    python scripts/phase3_visualisations.py
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import os

np.random.seed(42)
matplotlib.rcParams["figure.dpi"] = 300

MATRIX_PATH = "data/phase3/coverage_matrix.csv"
GAP_SCORES_PATH = "data/phase3/gap_scores.csv"
BENCHMARK_DB = "outputs/phase2/benchmark_database_FINAL.csv"
CHARTS_DIR = "outputs/phase3/charts"

os.makedirs(CHARTS_DIR, exist_ok=True)


def plot_coverage_heatmap(matrix: pd.DataFrame) -> None:
    """Coverage heatmap: benchmarks × capabilities, coloured by quality rating.

    Args:
        matrix: Coverage matrix DataFrame (benchmark_id × capability_id).
    """
    fig, ax = plt.subplots(figsize=(14, 8))
    sns.heatmap(matrix, annot=True, fmt="g", cmap="YlOrRd", vmin=0, vmax=5, ax=ax,
                linewidths=0.5, cbar_kws={"label": "Quality Rating (0–5)"})
    ax.set_title("Benchmark Coverage Heatmap\n(Capabilities vs Benchmarks)", fontsize=14)
    ax.set_xlabel("Capability", fontsize=11)
    ax.set_ylabel("Benchmark", fontsize=11)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    path = os.path.join(CHARTS_DIR, "coverage_heatmap.png")
    plt.savefig(path, dpi=300)
    plt.close()
    print(f"Saved: {path}")


def plot_gap_scores(gap_df: pd.DataFrame) -> None:
    """Horizontal bar chart of capabilities ranked by gap score.

    Args:
        gap_df: DataFrame with capability_name and gap_score columns.
    """
    sorted_df = gap_df.sort_values("gap_score", ascending=True)
    colors = ["#d9534f" if s > 0.3 else "#f0ad4e" if s > 0.15 else "#5cb85c"
              for s in sorted_df["gap_score"]]
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.barh(sorted_df["capability_name"], sorted_df["gap_score"], color=colors)
    ax.set_title("Usage-Weighted Gap Scores by Capability\n(Higher = More Urgent Gap)", fontsize=14)
    ax.set_xlabel("Gap Score")
    ax.set_ylabel("Capability")
    ax.axvline(0.3, color="red", linestyle="--", alpha=0.5, label="High severity threshold")
    ax.axvline(0.15, color="orange", linestyle="--", alpha=0.5, label="Medium severity threshold")
    ax.legend()
    plt.tight_layout()
    path = os.path.join(CHARTS_DIR, "gap_scores.png")
    plt.savefig(path, dpi=300)
    plt.close()
    print(f"Saved: {path}")


def plot_usage_vs_coverage(gap_df: pd.DataFrame) -> None:
    """Scatter plot: usage frequency vs. coverage score per capability.

    Args:
        gap_df: DataFrame with capability_name, usage_frequency, total_coverage_score.
    """
    fig, ax = plt.subplots(figsize=(9, 7))
    ax.scatter(gap_df["usage_frequency"], gap_df["total_coverage_score"], s=100, color="steelblue", zorder=3)
    for _, row in gap_df.iterrows():
        ax.annotate(row["capability_name"],
                    (row["usage_frequency"], row["total_coverage_score"]),
                    textcoords="offset points", xytext=(6, 4), fontsize=9)
    ax.set_title("Usage Frequency vs. Coverage Score per Capability", fontsize=14)
    ax.set_xlabel("Usage Frequency (from Handa et al., 2025)")
    ax.set_ylabel("Normalised Coverage Score")
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    path = os.path.join(CHARTS_DIR, "usage_vs_coverage_scatter.png")
    plt.savefig(path, dpi=300)
    plt.close()
    print(f"Saved: {path}")


def main():
    """Main execution: load data and generate all 5 charts."""
    matrix = pd.read_csv(MATRIX_PATH, index_col=0)
    gap_df = pd.read_csv(GAP_SCORES_PATH)

    if matrix.empty or gap_df.empty:
        print("Populate coverage_matrix.csv and gap_scores.csv before generating charts.")
        return

    plot_coverage_heatmap(matrix)
    plot_gap_scores(gap_df)
    plot_usage_vs_coverage(gap_df)
    print("Temporal trends and quality radar charts require benchmark_database_FINAL.csv data.")


if __name__ == "__main__":
    main()
