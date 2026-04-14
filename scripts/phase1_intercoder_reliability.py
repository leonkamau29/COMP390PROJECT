"""
Phase 1 Inter-coder Reliability Script

Purpose:
    Calculates Cohen's kappa (κ) for inter-coder reliability on a subsample
    of coded task instances. Target: κ > 0.8.

Inputs:
    data/phase1/intercoder_reliability.csv
        Columns: task_id, coder1_label, coder2_label, agreement, source

Outputs:
    Console output with κ value and interpretation.

Usage:
    python scripts/phase1_intercoder_reliability.py
"""

import pandas as pd
import numpy as np
from sklearn.metrics import cohen_kappa_score

np.random.seed(42)

RELIABILITY_PATH = "data/phase1/intercoder_reliability.csv"
TARGET_KAPPA = 0.8


def calculate_kappa(df: pd.DataFrame) -> float:
    """Calculate Cohen's kappa from coder labels.

    Args:
        df: DataFrame with coder1_label and coder2_label columns.

    Returns:
        Cohen's kappa score.
    """
    kappa = cohen_kappa_score(df["coder1_label"], df["coder2_label"])
    return kappa


def main():
    """Main execution: load reliability data and compute kappa."""
    df = pd.read_csv(RELIABILITY_PATH)
    if df.empty or df["coder1_label"].isna().all():
        print("No coded data yet. Populate intercoder_reliability.csv first.")
        return

    kappa = calculate_kappa(df)
    print(f"Cohen's κ = {kappa:.4f}")
    if kappa >= TARGET_KAPPA:
        print(f"PASS: κ ≥ {TARGET_KAPPA} — acceptable inter-coder reliability.")
    else:
        print(f"FAIL: κ < {TARGET_KAPPA} — refine decision rules and re-code before proceeding.")


if __name__ == "__main__":
    main()
