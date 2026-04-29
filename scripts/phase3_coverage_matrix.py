"""
Phase 3 Coverage Matrix Script

Purpose:
    Constructs the capability-benchmark coverage matrix from benchmark database
    and capability taxonomy. Computes per-capability aggregate metrics.

Inputs:
    outputs/phase2/benchmark_database_FINAL.csv
    outputs/phase1/capability_taxonomy_FINAL.csv

Outputs:
    data/phase3/coverage_matrix.csv
    data/phase3/coverage_matrix_notes.csv
    data/phase3/capability_coverage_metrics.csv

Usage:
    python scripts/phase3_coverage_matrix.py
"""

import pandas as pd
import numpy as np
import os

np.random.seed(42)

BENCHMARK_DB = "outputs/phase2/benchmark_database_FINAL.csv"
TAXONOMY_PATH = "outputs/phase1/capability_taxonomy_FINAL.csv"
MATRIX_PATH = "data/phase3/coverage_matrix.csv"
NOTES_PATH = "data/phase3/coverage_matrix_notes.csv"
METRICS_PATH = "data/phase3/capability_coverage_metrics.csv"


def build_coverage_matrix(benchmarks: pd.DataFrame, capabilities: pd.DataFrame) -> pd.DataFrame:
    """Build empty coverage matrix (benchmarks × capabilities).

    Args:
        benchmarks: Benchmark database DataFrame.
        capabilities: Capability taxonomy DataFrame.

    Returns:
        Coverage matrix DataFrame with benchmark_id as index and
        capability_id as columns. All values initialised to 0.
    """
    matrix = pd.DataFrame(
        0,
        index=benchmarks["benchmark_id"],
        columns=capabilities["capability_id"]
    )
    return matrix


def compute_capability_metrics(matrix: pd.DataFrame) -> pd.DataFrame:
    """Compute per-capability aggregate metrics from coverage matrix.

    Args:
        matrix: Coverage matrix (benchmarks × capabilities).

    Returns:
        DataFrame with total_coverage_score, benchmark_count, average_quality
        per capability.
    """
    max_possible = len(matrix) * 5  # max rating per benchmark = 5
    metrics = pd.DataFrame({
        "capability_id": matrix.columns,
        "total_coverage_score": matrix.sum(axis=0).values / max_possible,
        "benchmark_count": (matrix >= 1).sum(axis=0).values,
        "average_quality": matrix[matrix >= 1].mean(axis=0).values
    })
    return metrics


def main():
    """Main execution: build coverage matrix and compute metrics."""
    benchmarks = pd.read_csv(BENCHMARK_DB)
    capabilities = pd.read_csv(TAXONOMY_PATH)

    if benchmarks.empty or capabilities.empty:
        print("Populate benchmark_database_FINAL.csv and capability_taxonomy_FINAL.csv first.")
        return

    # If matrix already exists and has non-zero values, use it; otherwise initialise empty.
    if os.path.exists(MATRIX_PATH):
        existing = pd.read_csv(MATRIX_PATH, index_col=0)
        if existing.values.sum() > 0:
            matrix = existing
            print(f"Loaded existing coverage matrix from {MATRIX_PATH}")
        else:
            matrix = build_coverage_matrix(benchmarks, capabilities)
            matrix.to_csv(MATRIX_PATH)
            print(f"Coverage matrix saved to {MATRIX_PATH}")
    else:
        matrix = build_coverage_matrix(benchmarks, capabilities)
        matrix.to_csv(MATRIX_PATH)
        print(f"Coverage matrix saved to {MATRIX_PATH}")

    metrics = compute_capability_metrics(matrix)
    metrics.to_csv(METRICS_PATH, index=False)
    print(f"Capability metrics saved to {METRICS_PATH}")


if __name__ == "__main__":
    main()
