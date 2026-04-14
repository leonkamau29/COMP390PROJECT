"""
Phase 3 Gap Scores Script

Purpose:
    Calculates usage-weighted gap scores for each capability using the formula:
        Gap Score = Usage_Frequency × (1 - Normalized_Coverage_Score)

Inputs:
    data/phase3/capability_coverage_metrics.csv
    (usage frequency values from Handa et al. (2025) must be manually populated)

Outputs:
    data/phase3/gap_scores.csv

Usage:
    python scripts/phase3_gap_scores.py
"""

import pandas as pd
import numpy as np

np.random.seed(42)

METRICS_PATH = "data/phase3/capability_coverage_metrics.csv"
GAP_SCORES_PATH = "data/phase3/gap_scores.csv"


def compute_gap_scores(metrics: pd.DataFrame) -> pd.DataFrame:
    """Compute usage-weighted gap score per capability.

    Gap Score = Usage_Frequency × (1 - Normalized_Coverage_Score)

    Args:
        metrics: DataFrame with columns: capability_id, capability_name,
                 total_coverage_score, usage_frequency.

    Returns:
        DataFrame with gap_score column added, sorted descending by gap score.
    """
    metrics["gap_score"] = (
        metrics["usage_frequency"] * (1 - metrics["total_coverage_score"])
    )
    return metrics.sort_values("gap_score", ascending=False)


def main():
    """Main execution: load metrics, compute gap scores, save results."""
    metrics = pd.read_csv(METRICS_PATH)

    if "usage_frequency" not in metrics.columns:
        print("ERROR: 'usage_frequency' column not found in capability_coverage_metrics.csv.")
        print("Add usage frequency values from Handa et al. (2025) before running this script.")
        return

    result = compute_gap_scores(metrics)
    result.to_csv(GAP_SCORES_PATH, index=False)
    print(f"Gap scores saved to {GAP_SCORES_PATH}")
    print(result[["capability_id", "usage_frequency", "total_coverage_score", "gap_score"]])


if __name__ == "__main__":
    main()
