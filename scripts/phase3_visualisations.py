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


def plot_temporal_trends(benchmarks: pd.DataFrame, gap_df: pd.DataFrame) -> None:
    """Line chart: cumulative benchmark count per capability over years 2017–2025.

    Args:
        benchmarks: Benchmark database DataFrame with year_clean and primary_capability.
        gap_df: Gap scores DataFrame with capability_id and capability_name.
    """
    cap_names = gap_df.set_index("capability_id")["capability_name"].to_dict()
    years = sorted(benchmarks["year_clean"].dropna().unique())
    years = [y for y in years if 2017 <= y <= 2025]

    fig, ax = plt.subplots(figsize=(12, 7))
    for cap_id, cap_name in cap_names.items():
        subset = benchmarks[benchmarks["primary_capability"] == cap_id]
        counts = [len(subset[subset["year_clean"] <= yr]) for yr in years]
        if max(counts) > 0:
            ax.plot(years, counts, marker="o", label=f"{cap_id}: {cap_name}")

    ax.set_title("Cumulative Benchmark Count per Capability (2017–2025)\n(Source: Phase 2 Benchmark Database)", fontsize=13)
    ax.set_xlabel("Year")
    ax.set_ylabel("Cumulative Benchmark Count")
    ax.set_xticks(years)
    ax.legend(fontsize=8, loc="upper left")
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    path = os.path.join(CHARTS_DIR, "temporal_trends.png")
    plt.savefig(path, dpi=300)
    plt.close()
    print(f"Saved: {path}")


def plot_quality_radar(benchmarks: pd.DataFrame, gap_df: pd.DataFrame) -> None:
    """Radar/spider chart: average quality across 5 dimensions per capability.

    Args:
        benchmarks: Benchmark database DataFrame with quality dimension columns.
        gap_df: Gap scores DataFrame with capability_id and capability_name.
    """
    dims = ["quality_coherence", "quality_accuracy", "quality_clarity",
            "quality_relevance", "quality_efficiency"]
    dim_labels = ["Coherence", "Accuracy", "Clarity", "Relevance", "Efficiency"]
    n = len(dims)
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()
    angles += angles[:1]

    cap_names = gap_df.set_index("capability_id")["capability_name"].to_dict()
    fig, ax = plt.subplots(figsize=(9, 9), subplot_kw={"polar": True})

    colors = plt.cm.tab10(np.linspace(0, 1, len(cap_names)))
    for (cap_id, cap_name), color in zip(cap_names.items(), colors):
        subset = benchmarks[benchmarks["primary_capability"] == cap_id]
        if subset.empty:
            continue
        values = [subset[d].mean() for d in dims]
        values += values[:1]
        ax.plot(angles, values, "o-", linewidth=2, label=f"{cap_id}: {cap_name}", color=color)
        ax.fill(angles, values, alpha=0.05, color=color)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(dim_labels, fontsize=10)
    ax.set_ylim(0, 5)
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(["1", "2", "3", "4", "5"], fontsize=8)
    ax.set_title("Average Quality Dimensions per Capability\n(Source: Phase 2 Benchmark Database)", fontsize=13, pad=20)
    ax.legend(loc="upper right", bbox_to_anchor=(1.35, 1.1), fontsize=8)
    plt.tight_layout()
    path = os.path.join(CHARTS_DIR, "quality_radar.png")
    plt.savefig(path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"Saved: {path}")


def main():
    """Main execution: load data and generate all 5 charts."""
    matrix = pd.read_csv(MATRIX_PATH, index_col=0)
    gap_df = pd.read_csv(GAP_SCORES_PATH)
    benchmarks = pd.read_csv(BENCHMARK_DB)

    if matrix.empty or gap_df.empty:
        print("Populate coverage_matrix.csv and gap_scores.csv before generating charts.")
        return

    plot_coverage_heatmap(matrix)
    plot_gap_scores(gap_df)
    plot_usage_vs_coverage(gap_df)
    plot_temporal_trends(benchmarks, gap_df)
    plot_quality_radar(benchmarks, gap_df)


if __name__ == "__main__":
    main()
