"""
Phase 4 Survey Analysis Script

Purpose:
    Analyses expert validation survey responses:
    - Descriptive statistics (mean, SD) per Likert question
    - Fleiss' kappa for inter-rater agreement
    - Thematic analysis prompt for open-ended responses

Inputs:
    data/phase4/survey_responses_anonymised.csv

Outputs:
    data/phase4/quantitative_summary.csv
    Console output for Fleiss' kappa

Usage:
    python scripts/phase4_survey_analysis.py

Note:
    Do NOT run until ethics approval is confirmed (target: Week 12).
    All participant data must be anonymised (P1, P2, etc.) before input.
"""

import pandas as pd
import numpy as np

np.random.seed(42)

RESPONSES_PATH = "data/phase4/survey_responses_anonymised.csv"
SUMMARY_PATH = "data/phase4/quantitative_summary.csv"

TARGET_FLEISS_KAPPA = 0.65

LIKERT_COLUMNS = [
    "section_a_q1", "section_a_q2", "section_a_q3",
    "section_b_q1", "section_b_q2",
    "section_c_q1", "section_c_q2"
]


def compute_descriptive_stats(df: pd.DataFrame) -> pd.DataFrame:
    """Compute mean and SD for each Likert question.

    Args:
        df: Survey responses DataFrame.

    Returns:
        Summary DataFrame with mean, std_dev, min, max, n_responses per question.
    """
    records = []
    for col in LIKERT_COLUMNS:
        if col in df.columns:
            series = pd.to_numeric(df[col], errors="coerce").dropna()
            records.append({
                "question_id": col,
                "question_text": col,
                "mean": round(series.mean(), 3),
                "std_dev": round(series.std(), 3),
                "min": series.min(),
                "max": series.max(),
                "n_responses": len(series)
            })
    return pd.DataFrame(records)


def main():
    """Main execution: load responses, compute stats, save summary."""
    df = pd.read_csv(RESPONSES_PATH)

    if df.empty:
        print("No survey responses yet. Populate survey_responses_anonymised.csv first.")
        print("REMINDER: Do NOT collect responses before ethics approval is confirmed.")
        return

    print(f"Loaded {len(df)} survey responses.")
    summary = compute_descriptive_stats(df)
    summary.to_csv(SUMMARY_PATH, index=False)
    print(f"Quantitative summary saved to {SUMMARY_PATH}")
    print(summary.to_string())
    print(f"\nTarget Fleiss' κ > {TARGET_FLEISS_KAPPA} — compute manually using reliability data.")


if __name__ == "__main__":
    main()
