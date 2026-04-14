"""
Phase 1 Thematic Analysis Script

Purpose:
    Supports Braun & Clarke (2006) six-phase thematic analysis of task instances.
    Loads task_instances_raw.csv, performs open/axial/selective coding workflows,
    and exports task_instances_coded.csv with coding columns.

Inputs:
    data/phase1/task_instances_raw.csv

Outputs:
    data/phase1/task_instances_coded.csv

Usage:
    python scripts/phase1_thematic_analysis.py
"""

import pandas as pd
import numpy as np

np.random.seed(42)

# Paths (relative to project root)
RAW_PATH = "data/phase1/task_instances_raw.csv"
CODED_PATH = "data/phase1/task_instances_coded.csv"


def load_tasks(path: str) -> pd.DataFrame:
    """Load raw task instances from CSV.

    Args:
        path: Relative path to the raw CSV file.

    Returns:
        DataFrame of raw task instances.
    """
    df = pd.read_csv(path)
    print(f"Loaded {len(df)} task instances from {path}")
    return df


def add_coding_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Add placeholder coding columns for thematic analysis.

    Args:
        df: Raw task instances DataFrame.

    Returns:
        DataFrame with open_code, axial_category, core_capability columns added.
    """
    if "open_code" not in df.columns:
        df["open_code"] = ""
    if "axial_category" not in df.columns:
        df["axial_category"] = ""
    if "core_capability" not in df.columns:
        df["core_capability"] = ""
    return df


def main():
    """Main execution: load tasks, add coding columns, save coded file."""
    df = load_tasks(RAW_PATH)
    df = add_coding_columns(df)
    df.to_csv(CODED_PATH, index=False)
    print(f"Coded template saved to {CODED_PATH}")
    print(f"Columns: {list(df.columns)}")


if __name__ == "__main__":
    main()
