"""
phase2_benchmark_analysis.py
-----------------------------
Phase 2, Week 9: Descriptive analysis and visualisations for the benchmark inventory.

Inputs:
    data/phase2/benchmark_database.csv   — Phase 2 master benchmark database

Outputs:
    outputs/phase2/benchmark_database_FINAL.csv   — verified final database copy
    outputs/phase2/charts/
        chart1_benchmarks_by_year.png        — Bar chart: benchmarks by publication year
        chart2_benchmarks_by_capability.png  — Bar chart: benchmarks by primary capability
        chart3_benchmarks_by_venue.png       — Bar chart: benchmarks by publication venue type
        chart4_quality_ratings.png           — Grouped bar chart: quality across 5 dimensions
        chart5_contamination_risk.png        — Pie chart: contamination risk distribution

Usage:
    cd <project_root>
    python scripts/phase2_benchmark_analysis.py

All charts exported at 300 DPI minimum.
"""

import os
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

# ── Paths (relative to project root) ─────────────────────────────────────────
DB_PATH    = os.path.join("data",    "phase2", "benchmark_database.csv")
FINAL_PATH = os.path.join("outputs", "phase2", "benchmark_database_FINAL.csv")
CHARTS_DIR = os.path.join("outputs", "phase2", "charts")
os.makedirs(CHARTS_DIR, exist_ok=True)

# ── Design constants ──────────────────────────────────────────────────────────
sns.set_theme(style="whitegrid", font_scale=1.1)
PALETTE_CAP = {
    "C01": "#4CAF50",
    "C02": "#2196F3",
    "C03": "#9C27B0",
    "C04": "#FF9800",
    "C05": "#F44336",
    "C06": "#795548",
    "C07": "#009688",
    "C08": "#607D8B",
}
DPI = 300
SOURCE = "Source: Phase 2 Benchmark Inventory — Kamau Kiunga (2026)"
CAP_ORDER = ["C02", "C03", "C01", "C07", "C04", "C05", "C08", "C06"]


# ── Helpers ───────────────────────────────────────────────────────────────────

def load_db() -> pd.DataFrame:
    """Load benchmark database and derive a clean integer publication year."""
    df = pd.read_csv(DB_PATH)
    df["year_clean"] = (
        df["year"].astype(str).str.extract(r"(\d{4})")[0].astype(int)
    )
    return df


def check_completeness(df: pd.DataFrame) -> None:
    """Audit every field for blanks; print result.

    secondary_capabilities is intentionally sparse (not all benchmarks have
    secondary capabilities) so it is excluded from the completeness check.
    """
    # Fields that are intentionally optional / sparse
    optional = {"secondary_capabilities"}
    missing = df.isnull().sum()
    missing = missing[missing > 0]
    missing = missing.drop(labels=[c for c in optional if c in missing.index])
    if missing.empty:
        print("  Completeness check PASSED — all required fields populated.")
    else:
        print("  Missing fields detected (investigate before Phase 3):")
        print(missing.to_string())


def classify_risk(v: str) -> str:
    """Normalise contamination_risk text to High / Medium / Low."""
    v = str(v).lower()
    if v.startswith("high"):
        return "High"
    if v.startswith("medium"):
        return "Medium"
    return "Low"


def classify_venue(v: str) -> str:
    """Bucket venue strings into broad publication-type categories."""
    v = str(v).lower()
    if any(kw in v for kw in ("neurips", "acl", "emnlp", "naacl", "tmlr", "tacl", "iclr", "icml")):
        return "Peer-reviewed\nConference / Journal"
    if "arxiv" in v:
        return "arXiv Preprint"
    if any(kw in v for kw in ("blog", "openai", "leaderboard", "eqbench")):
        return "Technical Blog /\nLeaderboard"
    return "Other"


# ── Chart 1: Benchmarks by publication year ───────────────────────────────────

def chart_by_year(df: pd.DataFrame) -> None:
    """Bar chart showing how many benchmarks per publication year."""
    year_counts = df["year_clean"].value_counts().sort_index()

    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.bar(
        year_counts.index.astype(str),
        year_counts.values,
        color="#2196F3",
        edgecolor="white",
        linewidth=0.8,
        width=0.55,
    )
    for bar in bars:
        h = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            h + 0.05,
            str(int(h)),
            ha="center", va="bottom", fontsize=12, fontweight="bold",
        )

    ax.set_title("Phase 2 Benchmarks by Publication Year",
                 fontsize=14, fontweight="bold", pad=12)
    ax.set_xlabel("Publication Year", fontsize=12)
    ax.set_ylabel("Number of Benchmarks", fontsize=12)
    ax.set_ylim(0, year_counts.max() + 1.8)
    ax.yaxis.set_major_locator(plt.MaxNLocator(integer=True))
    ax.text(0.99, -0.13, SOURCE,
            transform=ax.transAxes, ha="right", fontsize=8, color="grey")

    fig.tight_layout()
    out = os.path.join(CHARTS_DIR, "chart1_benchmarks_by_year.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {out}")


# ── Chart 2: Benchmarks by primary capability ─────────────────────────────────

def chart_by_capability(df: pd.DataFrame) -> None:
    """Bar chart of benchmark count per capability, ordered by usage share."""
    cap_labels = {
        "C01": "C01\nContent Generation",
        "C02": "C02\nCode Development",
        "C03": "C03\nInformation Retrieval",
        "C04": "C04\nLearning & Education",
        "C05": "C05\nReview & Feedback",
        "C06": "C06\nTranslation",
        "C07": "C07\nData Analysis",
        "C08": "C08\nConversation",
    }
    usage = {
        "C02": "34.0%",
        "C03": "21.4%",
        "C01": "17.5%",
        "C07": "10.7%",
        "C04": "7.8%",
        "C05": "3.9%",
        "C08": "2.9%",
        "C06": "1.9%",
    }
    counts = df["primary_capability"].value_counts().reindex(CAP_ORDER, fill_value=0)

    fig, ax = plt.subplots(figsize=(10, 5.5))
    bars = ax.bar(
        [cap_labels[c] for c in CAP_ORDER],
        counts.values,
        color=[PALETTE_CAP[c] for c in CAP_ORDER],
        edgecolor="white",
        linewidth=0.8,
        width=0.55,
    )
    for bar, cap in zip(bars, CAP_ORDER):
        h = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            h + 0.05,
            str(int(h)),
            ha="center", va="bottom", fontsize=13, fontweight="bold",
        )

    # Annotate with real-world usage share beneath each x-tick label
    tick_positions = [bar.get_x() + bar.get_width() / 2 for bar in bars]
    for pos, cap in zip(tick_positions, CAP_ORDER):
        ax.annotate(
            f"Usage: {usage[cap]}",
            xy=(pos, 0), xycoords=("data", "axes fraction"),
            xytext=(0, -32), textcoords="offset points",
            ha="center", fontsize=8, color="grey",
        )

    ax.set_title("Phase 2 Benchmarks by Primary Capability Area\n"
                 "(v3 inventory ordered by Anthropic AEI Feb 2026 usage share)",
                 fontsize=14, fontweight="bold", pad=12)
    ax.set_ylabel("Number of Benchmarks", fontsize=12)
    ax.set_ylim(0, counts.max() + 1.8)
    ax.yaxis.set_major_locator(plt.MaxNLocator(integer=True))
    ax.text(0.99, -0.25, SOURCE,
            transform=ax.transAxes, ha="right", fontsize=8, color="grey")

    fig.tight_layout()
    out = os.path.join(CHARTS_DIR, "chart2_benchmarks_by_capability.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {out}")


# ── Chart 3: Benchmarks by publication venue type ─────────────────────────────

def chart_by_venue(df: pd.DataFrame) -> None:
    """Bar chart grouping benchmarks by broad venue category."""
    venue_colors = {
        "Peer-reviewed\nConference / Journal": "#4CAF50",
        "arXiv Preprint":                      "#FF9800",
        "Technical Blog /\nLeaderboard":        "#9C27B0",
        "Other":                               "#607D8B",
    }
    df = df.copy()
    df["venue_type"] = df["venue"].apply(classify_venue)
    vcounts = df["venue_type"].value_counts()
    colors = [venue_colors.get(v, "#607D8B") for v in vcounts.index]

    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.bar(
        vcounts.index,
        vcounts.values,
        color=colors,
        edgecolor="white",
        linewidth=0.8,
        width=0.5,
    )
    for bar in bars:
        h = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            h + 0.05,
            str(int(h)),
            ha="center", va="bottom", fontsize=12, fontweight="bold",
        )

    ax.set_title("Phase 2 Benchmarks by Publication Venue Type",
                 fontsize=14, fontweight="bold", pad=12)
    ax.set_ylabel("Number of Benchmarks", fontsize=12)
    ax.set_ylim(0, vcounts.max() + 1.8)
    ax.yaxis.set_major_locator(plt.MaxNLocator(integer=True))
    ax.text(0.99, -0.13, SOURCE,
            transform=ax.transAxes, ha="right", fontsize=8, color="grey")

    fig.tight_layout()
    out = os.path.join(CHARTS_DIR, "chart3_benchmarks_by_venue.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {out}")


# ── Chart 4: Quality ratings — grouped bar by capability ──────────────────────

def chart_quality_ratings(df: pd.DataFrame) -> None:
    """Grouped bar chart: mean quality on each of 5 dimensions, per capability."""
    dims = [
        "quality_coherence",
        "quality_accuracy",
        "quality_clarity",
        "quality_relevance",
        "quality_efficiency",
    ]
    dim_labels = ["Coherence", "Accuracy", "Clarity", "Relevance", "Efficiency"]

    grouped = df.groupby("primary_capability")[dims].mean().reindex(CAP_ORDER)

    x = np.arange(len(dim_labels))
    n_caps = len(CAP_ORDER)
    total_width = 0.78
    bar_w = total_width / n_caps

    fig, ax = plt.subplots(figsize=(12, 6))
    for i, cap in enumerate(CAP_ORDER):
        offset = (i - n_caps / 2 + 0.5) * bar_w
        vals = grouped.loc[cap, dims].values
        ax.bar(
            x + offset,
            vals,
            width=bar_w * 0.88,
            color=PALETTE_CAP[cap],
            edgecolor="white",
            linewidth=0.5,
            label=cap,
        )

    ax.set_title("Average Quality Ratings by Capability Area\n(5 evaluation dimensions, scale 1–5)",
                 fontsize=14, fontweight="bold", pad=12)
    ax.set_xticks(x)
    ax.set_xticklabels(dim_labels, fontsize=12)
    ax.set_ylabel("Mean Quality Rating (1–5)", fontsize=12)
    ax.set_ylim(0, 5.8)
    ax.axhline(y=3, color="grey", linestyle="--", linewidth=0.8, alpha=0.6)
    ax.text(0.01, 3.08, "Midpoint (3)", transform=ax.get_yaxis_transform(),
            fontsize=8, color="grey")
    ax.legend(title="Capability", title_fontsize=10, fontsize=9, loc="upper right",
              framealpha=0.9)
    ax.text(0.99, -0.11, SOURCE,
            transform=ax.transAxes, ha="right", fontsize=8, color="grey")

    fig.tight_layout()
    out = os.path.join(CHARTS_DIR, "chart4_quality_ratings.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {out}")


# ── Chart 5: Contamination risk pie ───────────────────────────────────────────

def chart_contamination_risk(df: pd.DataFrame) -> None:
    """Pie chart of High / Medium / Low contamination risk across all benchmarks."""
    df = df.copy()
    df["risk_clean"] = df["contamination_risk"].apply(classify_risk)
    risk_counts = df["risk_clean"].value_counts().reindex(
        ["High", "Medium", "Low"], fill_value=0
    )
    risk_colors = {"High": "#F44336", "Medium": "#FF9800", "Low": "#4CAF50"}
    colors = [risk_colors[r] for r in risk_counts.index]

    total = risk_counts.sum()

    fig, ax = plt.subplots(figsize=(7, 6))
    wedges, texts, autotexts = ax.pie(
        risk_counts.values,
        labels=risk_counts.index,
        colors=colors,
        autopct=lambda p: f"{p:.1f}%\n(n={int(round(p * total / 100))})",
        startangle=140,
        pctdistance=0.72,
        wedgeprops=dict(edgecolor="white", linewidth=1.8),
    )
    for t in texts:
        t.set_fontsize(12)
        t.set_fontweight("bold")
    for at in autotexts:
        at.set_fontsize(10)

    ax.set_title(f"Contamination Risk Distribution\nAcross {len(df)} Shortlisted Benchmarks",
                 fontsize=14, fontweight="bold", pad=16)
    ax.text(0.5, -0.04, SOURCE,
            transform=ax.transAxes, ha="center", fontsize=8, color="grey")

    fig.tight_layout()
    out = os.path.join(CHARTS_DIR, "chart5_contamination_risk.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {out}")


# ── Descriptive stats console report ─────────────────────────────────────────

def print_stats(df: pd.DataFrame) -> None:
    """Print a brief descriptive statistics report to stdout."""
    dims = [
        "quality_coherence", "quality_accuracy", "quality_clarity",
        "quality_relevance", "quality_efficiency",
    ]
    print("\n--- Descriptive statistics -------------------------------------------")
    print(f"  Total benchmarks: {len(df)}")
    print(f"  Year range: {df['year_clean'].min()} – {df['year_clean'].max()}")
    print("\n  Capability distribution:")
    for cap in CAP_ORDER:
        n = (df["primary_capability"] == cap).sum()
        print(f"    {cap}: {n}")
    print(f"\n  Quality ratings (mean across all {len(df)} benchmarks):")
    for d in dims:
        label = d.replace("quality_", "").capitalize()
        print(f"    {label:12s}: {df[d].mean():.2f}  "
              f"(min {df[d].min()}, max {df[d].max()})")
    print(f"    {'Overall':12s}: {df[dims].stack().mean():.2f}")
    df["risk_clean"] = df["contamination_risk"].apply(classify_risk)
    print("\n  Contamination risk:")
    for lvl in ["High", "Medium", "Low"]:
        n = (df["risk_clean"] == lvl).sum()
        print(f"    {lvl}: {n}")


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    """Run all Phase 2 Week 9 analysis tasks."""
    print("Loading benchmark database …")
    df = load_db()
    print(f"  {len(df)} benchmarks loaded from {DB_PATH}")

    print("\nRunning completeness check …")
    check_completeness(df)

    print("\nGenerating charts …")
    chart_by_year(df)
    chart_by_capability(df)
    chart_by_venue(df)
    chart_quality_ratings(df)
    chart_contamination_risk(df)

    print("\nSaving benchmark_database_FINAL.csv …")
    final_df = df.drop(columns=["year_clean"], errors="ignore")
    final_df.to_csv(FINAL_PATH, index=False)
    print(f"  Saved: {FINAL_PATH}")

    print_stats(df)
    print("\nPhase 2 Week 9 analysis complete.")


if __name__ == "__main__":
    main()
