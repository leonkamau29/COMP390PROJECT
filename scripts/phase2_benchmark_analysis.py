"""
Phase 2 Benchmark Analysis Script

Purpose:
    Loads the benchmark database, checks completeness, runs descriptive
    statistics, and generates summary charts for the benchmark inventory.

Inputs:
    data/phase2/benchmark_database.csv

Outputs:
    outputs/phase2/benchmark_database_FINAL.csv
    outputs/phase2/charts/benchmarks_by_year.png
    outputs/phase2/charts/benchmarks_by_capability.png
    outputs/phase2/charts/benchmarks_by_venue.png
    outputs/phase2/charts/quality_ratings.png
    outputs/phase2/charts/contamination_risk.png

Usage:
    python scripts/phase2_benchmark_analysis.py
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

np.random.seed(42)

DB_PATH = "data/phase2/benchmark_database.csv"
FINAL_PATH = "outputs/phase2/benchmark_database_FINAL.csv"
CHARTS_DIR = "outputs/phase2/charts"

os.makedirs(CHARTS_DIR, exist_ok=True)


def check_completeness(df: pd.DataFrame) -> None:
    """Audit database for completeness; print missing field summary.

    Args:
        df: Benchmark database DataFrame.
    """
    missing = df.isnull().sum()
    missing = missing[missing > 0]
    if missing.empty:
        print("Completeness check PASSED: no missing fields.")
    else:
        print("Missing fields found:")
        print(missing)


def plot_by_year(df: pd.DataFrame) -> None:
    """Bar chart of benchmark count by publication year.

    Args:
        df: Benchmark database DataFrame.
    """
    fig, ax = plt.subplots(figsize=(10, 5))
    df["year"].value_counts().sort_index().plot(kind="bar", ax=ax, color="steelblue")
    ax.set_title("Benchmarks by Year of Publication", fontsize=14)
    ax.set_xlabel("Year")
    ax.set_ylabel("Count")
    ax.legend(["Benchmarks"])
    plt.tight_layout()
    path = os.path.join(CHARTS_DIR, "benchmarks_by_year.png")
    plt.savefig(path, dpi=300)
    plt.close()
    print(f"Saved: {path}")


def plot_by_capability(df: pd.DataFrame) -> None:
    """Bar chart of benchmark count by primary capability.

    Args:
        df: Benchmark database DataFrame.
    """
    fig, ax = plt.subplots(figsize=(10, 5))
    df["primary_capability"].value_counts().plot(kind="bar", ax=ax, color="coral")
    ax.set_title("Benchmarks by Primary Capability", fontsize=14)
    ax.set_xlabel("Capability")
    ax.set_ylabel("Count")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    path = os.path.join(CHARTS_DIR, "benchmarks_by_capability.png")
    plt.savefig(path, dpi=300)
    plt.close()
    print(f"Saved: {path}")


def plot_contamination_risk(df: pd.DataFrame) -> None:
    """Pie chart of contamination risk distribution.

    Args:
        df: Benchmark database DataFrame.
    """
    fig, ax = plt.subplots(figsize=(6, 6))
    df["contamination_risk"].value_counts().plot(
        kind="pie", ax=ax, autopct="%1.1f%%", colors=["#d9534f", "#f0ad4e", "#5cb85c"]
    )
    ax.set_title("Contamination Risk Distribution", fontsize=14)
    ax.set_ylabel("")
    plt.tight_layout()
    path = os.path.join(CHARTS_DIR, "contamination_risk.png")
    plt.savefig(path, dpi=300)
    plt.close()
    print(f"Saved: {path}")


def main():
    """Main execution: load, audit, analyse, and chart benchmark database."""
    df = pd.read_csv(DB_PATH)
    print(f"Loaded {len(df)} benchmarks.")
    check_completeness(df)

    if df.empty:
        print("Database is empty. Populate benchmark_database.csv first.")
        return

    plot_by_year(df)
    plot_by_capability(df)
    plot_contamination_risk(df)

    df.to_csv(FINAL_PATH, index=False)
    print(f"Final database saved to {FINAL_PATH}")


if __name__ == "__main__":
    main()
