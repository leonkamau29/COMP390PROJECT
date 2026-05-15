"""
Calculate Phase 3 usage-weighted gap scores.

Purpose:
    Aggregate Anthropic AEI task usage by Phase 1 capability and calculate:
    Gap Score = Usage_Frequency x (1 - Normalized_Coverage_Score).

Inputs:
    data/phase1/anthropic_top100_mapping.csv
    data/phase1/anthropic/top_tasks_by_frequency.csv
    data/phase3/capability_coverage_metrics.csv

Outputs:
    data/phase3/gap_scores.csv
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from phase3_config import GAP_SCORES_PATH, METRICS_PATH, ensure_directories, load_inputs


np.random.seed(42)


def compute_usage_frequencies(
    taxonomy: pd.DataFrame, mapping: pd.DataFrame, usage: pd.DataFrame
) -> pd.DataFrame:
    """Aggregate Anthropic task-level usage percentages by mapped capability."""
    merged = usage.merge(mapping, left_on="task_description", right_on="task", how="left")
    missing = merged[merged["mapped_capability"].isna()]
    if not missing.empty:
        raise ValueError(f"Anthropic usage rows without capability mapping: {len(missing)}")

    usage_by_capability = (
        merged.groupby("mapped_capability", as_index=False)["usage_pct"].sum()
        .rename(columns={"mapped_capability": "capability_id"})
    )
    all_caps = taxonomy[["capability_id", "capability_name"]].merge(
        usage_by_capability, on="capability_id", how="left"
    )
    all_caps["usage_pct"] = all_caps["usage_pct"].fillna(0.0)
    all_caps["usage_frequency"] = all_caps["usage_pct"] / 100.0
    total_pct = all_caps["usage_pct"].sum()
    all_caps["usage_share_of_top_tasks"] = all_caps["usage_pct"] / total_pct
    return all_caps


def compute_gap_scores(metrics: pd.DataFrame, usage_by_capability: pd.DataFrame) -> pd.DataFrame:
    """Compute usage-weighted gap scores for every capability."""
    gap = metrics.merge(
        usage_by_capability[
            ["capability_id", "usage_pct", "usage_frequency", "usage_share_of_top_tasks"]
        ],
        on="capability_id",
        how="left",
    )
    gap["usage_pct"] = gap["usage_pct"].fillna(0.0)
    gap["usage_frequency"] = gap["usage_frequency"].fillna(0.0)
    gap["usage_share_of_top_tasks"] = gap["usage_share_of_top_tasks"].fillna(0.0)
    gap["gap_score"] = gap["usage_frequency"] * (1 - gap["total_coverage_score"])
    gap["gap_rank"] = gap["gap_score"].rank(method="first", ascending=False).astype(int)
    gap["severity"] = pd.cut(
        gap["gap_score"],
        bins=[-0.001, 0.025, 0.075, 1.0],
        labels=["Low", "Medium", "High"],
    )
    gap = gap.sort_values("gap_score", ascending=False)
    gap.to_csv(GAP_SCORES_PATH, index=False)
    return gap


def main() -> None:
    """Generate Phase 3 gap score file from existing coverage metrics."""
    ensure_directories()
    taxonomy, _, mapping, usage = load_inputs()
    metrics = pd.read_csv(METRICS_PATH)
    usage_by_capability = compute_usage_frequencies(taxonomy, mapping, usage)
    gap_scores = compute_gap_scores(metrics, usage_by_capability)
    print(f"Gap scores saved to {GAP_SCORES_PATH}")
    print(gap_scores[["capability_id", "usage_frequency", "total_coverage_score", "gap_score"]])


if __name__ == "__main__":
    main()
