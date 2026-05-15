"""
Generate Phase 3 visualisations.

Purpose:
    Produce all five required Phase 3 charts at 300 DPI using the regenerated
    coverage matrix, gap scores, taxonomy, and benchmark database.

Inputs:
    data/phase3/coverage_matrix.csv
    data/phase3/gap_scores.csv
    outputs/phase1/capability_taxonomy_FINAL.csv
    outputs/phase2/benchmark_database_FINAL.csv

Outputs:
    outputs/phase3/charts/coverage_heatmap.png
    outputs/phase3/charts/gap_scores.png
    outputs/phase3/charts/usage_vs_coverage_scatter.png
    outputs/phase3/charts/temporal_trends.png
    outputs/phase3/charts/quality_radar.png
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from phase3_config import CHARTS_DIR, GAP_SCORES_PATH, MATRIX_PATH, ensure_directories, load_inputs, prepare_benchmarks


np.random.seed(42)
plt.rcParams["figure.dpi"] = 300


def benchmark_label(row: pd.Series) -> str:
    """Return a compact benchmark label for chart axes."""
    return f"{row.name} {row['abbreviation']}"


def add_source_note(ax: plt.Axes, text: str) -> None:
    """Add a small source attribution note to a chart."""
    ax.text(
        0,
        -0.16,
        text,
        transform=ax.transAxes,
        fontsize=8,
        color="dimgray",
        va="top",
    )


def plot_charts(
    taxonomy: pd.DataFrame, benchmarks: pd.DataFrame, matrix: pd.DataFrame, gap_scores: pd.DataFrame
) -> None:
    """Generate all five required Phase 3 charts at 300 DPI."""
    sns.set_theme(style="whitegrid")
    cap_name_map = taxonomy.set_index("capability_id")["capability_name"].to_dict()
    benchmark_labels = benchmarks.set_index("benchmark_id").apply(benchmark_label, axis=1).to_dict()

    heatmap_data = matrix.T.rename(index=cap_name_map, columns=benchmark_labels)
    fig, ax = plt.subplots(figsize=(18, 8))
    sns.heatmap(
        heatmap_data,
        cmap="YlOrRd",
        vmin=0,
        vmax=5,
        linewidths=0.35,
        linecolor="white",
        cbar_kws={"label": "Coverage quality rating (0-5)"},
        ax=ax,
    )
    ax.set_title("Phase 3 Coverage Heatmap: Capabilities by Benchmark", fontsize=15, weight="bold")
    ax.set_xlabel("Benchmark")
    ax.set_ylabel("Capability")
    ax.tick_params(axis="x", rotation=75, labelsize=7)
    ax.tick_params(axis="y", labelsize=9)
    add_source_note(ax, "Source: Phase 2 benchmark database and Phase 1 capability taxonomy.")
    fig.tight_layout()
    fig.savefig(CHARTS_DIR / "coverage_heatmap.png", dpi=300, bbox_inches="tight")
    plt.close(fig)

    gap_plot = gap_scores.sort_values("gap_score", ascending=True)
    colors = gap_plot["severity"].map({"High": "#c0392b", "Medium": "#f39c12", "Low": "#2e86c1"})
    fig, ax = plt.subplots(figsize=(11, 7))
    ax.barh(gap_plot["capability_name"], gap_plot["gap_score"], color=colors)
    ax.set_title("Usage-Weighted Gap Scores by Capability", fontsize=15, weight="bold")
    ax.set_xlabel("Gap score = usage frequency x (1 - coverage score)")
    ax.set_ylabel("Capability")
    for _, row in gap_plot.iterrows():
        ax.text(
            row["gap_score"] + 0.002,
            row["capability_name"],
            f"{row['gap_score']:.3f}",
            va="center",
            fontsize=8,
        )
    add_source_note(ax, "Source: Anthropic AEI task usage mapped to Phase 1 taxonomy; coverage from Phase 3 matrix.")
    fig.tight_layout()
    fig.savefig(CHARTS_DIR / "gap_scores.png", dpi=300, bbox_inches="tight")
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 7))
    ax.scatter(
        gap_scores["usage_frequency"],
        gap_scores["total_coverage_score"],
        s=120,
        c=gap_scores["gap_score"],
        cmap="viridis_r",
        edgecolor="black",
    )
    for _, row in gap_scores.iterrows():
        ax.annotate(
            row["capability_id"],
            (row["usage_frequency"], row["total_coverage_score"]),
            xytext=(6, 5),
            textcoords="offset points",
            fontsize=9,
        )
    ax.set_title("Usage Frequency vs Normalised Coverage Score", fontsize=15, weight="bold")
    ax.set_xlabel("Usage frequency from Anthropic top-task data")
    ax.set_ylabel("Normalised coverage score")
    add_source_note(ax, "Source: Handa et al. (2025) task usage and Phase 3 benchmark coverage ratings.")
    fig.tight_layout()
    fig.savefig(CHARTS_DIR / "usage_vs_coverage_scatter.png", dpi=300, bbox_inches="tight")
    plt.close(fig)

    years = list(range(2020, 2026))
    temporal_rows = []
    for capability_id, capability_name in cap_name_map.items():
        for year in years:
            ids_in_year = benchmarks.loc[benchmarks["year_clean"] == year, "benchmark_id"].tolist()
            temporal_rows.append(
                {
                    "year": year,
                    "capability": f"{capability_id} {capability_name}",
                    "benchmark_count": int((matrix.loc[ids_in_year, capability_id] >= 1).sum()),
                }
            )
    temporal_df = pd.DataFrame(temporal_rows)
    fig, ax = plt.subplots(figsize=(12, 7))
    sns.lineplot(
        data=temporal_df,
        x="year",
        y="benchmark_count",
        hue="capability",
        marker="o",
        ax=ax,
    )
    ax.set_title("Annual Benchmark Count per Capability, 2020-2025", fontsize=15, weight="bold")
    ax.set_xlabel("Publication year")
    ax.set_ylabel("Benchmark count")
    ax.legend(fontsize=7, loc="upper left", bbox_to_anchor=(1.02, 1))
    add_source_note(ax, "Source: Phase 2 benchmark publication years and Phase 3 non-zero coverage cells.")
    fig.tight_layout()
    fig.savefig(CHARTS_DIR / "temporal_trends.png", dpi=300, bbox_inches="tight")
    plt.close(fig)

    dims = [
        "quality_coherence",
        "quality_accuracy",
        "quality_clarity",
        "quality_relevance",
        "quality_efficiency",
    ]
    dim_labels = ["Coherence", "Accuracy", "Clarity", "Relevance", "Efficiency"]
    angles = np.linspace(0, 2 * np.pi, len(dims), endpoint=False).tolist()
    angles += angles[:1]
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={"polar": True})
    for capability_id, capability_name in cap_name_map.items():
        benchmark_ids = matrix.index[matrix[capability_id] >= 1].tolist()
        if not benchmark_ids:
            continue
        subset = benchmarks[benchmarks["benchmark_id"].isin(benchmark_ids)]
        values = [subset[d].astype(float).mean() for d in dims]
        values += values[:1]
        ax.plot(angles, values, linewidth=1.8, label=f"{capability_id} {capability_name}")
        ax.fill(angles, values, alpha=0.04)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(dim_labels)
    ax.set_ylim(0, 5)
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_title("Average Quality Dimensions for Benchmarks Covering Each Capability", fontsize=13, weight="bold", pad=24)
    ax.legend(fontsize=7, loc="upper left", bbox_to_anchor=(1.15, 1.1))
    fig.text(
        0.12,
        0.03,
        "Source: Phase 2 quality ratings averaged over non-zero Phase 3 coverage cells.",
        fontsize=8,
        color="dimgray",
    )
    fig.tight_layout()
    fig.savefig(CHARTS_DIR / "quality_radar.png", dpi=300, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    """Generate all Phase 3 visualisations from existing generated CSVs."""
    ensure_directories()
    taxonomy, benchmarks, _, _ = load_inputs()
    benchmarks = prepare_benchmarks(benchmarks)
    matrix = pd.read_csv(MATRIX_PATH, index_col=0)
    gap_scores = pd.read_csv(GAP_SCORES_PATH)
    plot_charts(taxonomy, benchmarks, matrix, gap_scores)
    print(f"Charts saved to {CHARTS_DIR}")


if __name__ == "__main__":
    main()
