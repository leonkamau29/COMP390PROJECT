"""
Shared configuration and IO helpers for Phase 3 coverage analysis.

Purpose:
    Centralise project-relative paths, input loading, year parsing, output
    directory creation, and final completeness validation for the modular
    Phase 3 scripts.

Inputs:
    outputs/phase1/capability_taxonomy_FINAL.csv
    data/phase1/anthropic_top100_mapping.csv
    data/phase1/anthropic/top_tasks_by_frequency.csv
    outputs/phase2/benchmark_database_FINAL.csv

Outputs:
    Shared paths and loaded DataFrames used by Phase 3 modules.
"""

from __future__ import annotations

import math
import re
from pathlib import Path

import numpy as np
import pandas as pd


np.random.seed(42)

PROJECT_ROOT = Path(__file__).resolve().parents[1]

TAXONOMY_PATH = PROJECT_ROOT / "outputs" / "phase1" / "capability_taxonomy_FINAL.csv"
ANTHROPIC_MAPPING_PATH = PROJECT_ROOT / "data" / "phase1" / "anthropic_top100_mapping.csv"
ANTHROPIC_USAGE_PATH = PROJECT_ROOT / "data" / "phase1" / "anthropic" / "top_tasks_by_frequency.csv"
BENCHMARK_DB_PATH = PROJECT_ROOT / "outputs" / "phase2" / "benchmark_database_FINAL.csv"

PHASE3_DATA = PROJECT_ROOT / "data" / "phase3"
PHASE3_OUTPUTS = PROJECT_ROOT / "outputs" / "phase3"
CHARTS_DIR = PHASE3_OUTPUTS / "charts"

MATRIX_PATH = PHASE3_DATA / "coverage_matrix.csv"
NOTES_PATH = PHASE3_DATA / "coverage_matrix_notes.csv"
METRICS_PATH = PHASE3_DATA / "capability_coverage_metrics.csv"
GAP_SCORES_PATH = PHASE3_DATA / "gap_scores.csv"
STATS_PATH = PHASE3_DATA / "statistical_analysis_results.csv"
REPORT_PATH = PHASE3_OUTPUTS / "statistical_analysis_report.md"
CASE_STUDIES_PATH = PHASE3_OUTPUTS / "case_studies.md"


def ensure_directories() -> None:
    """Create Phase 3 data, output, and chart directories."""
    PHASE3_DATA.mkdir(parents=True, exist_ok=True)
    PHASE3_OUTPUTS.mkdir(parents=True, exist_ok=True)
    CHARTS_DIR.mkdir(parents=True, exist_ok=True)


def load_inputs() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Load taxonomy, benchmark database, Anthropic mapping, and usage data."""
    taxonomy = pd.read_csv(TAXONOMY_PATH)
    benchmarks = pd.read_csv(BENCHMARK_DB_PATH)
    mapping = pd.read_csv(
        ANTHROPIC_MAPPING_PATH,
        engine="python",
        on_bad_lines=lambda row: row[:3] + [",".join(row[3:])],
    )
    usage = pd.read_csv(ANTHROPIC_USAGE_PATH)
    return taxonomy, benchmarks, mapping, usage


def parse_first_year(value: object) -> int | float:
    """Extract the first publication year from a year field."""
    match = re.search(r"20\d{2}", str(value))
    if not match:
        return math.nan
    return int(match.group(0))


def prepare_benchmarks(benchmarks: pd.DataFrame) -> pd.DataFrame:
    """Return benchmark data with derived year fields kept in memory only."""
    prepared = benchmarks.copy()
    if "year_clean" in prepared.columns:
        prepared = prepared.drop(columns=["year_clean"])
    prepared["year_clean"] = prepared["year"].apply(parse_first_year)
    return prepared


def format_float(value: float) -> str:
    """Format a float for Markdown reports."""
    if pd.isna(value):
        return "not available"
    return f"{value:.4f}"


def validate_outputs() -> None:
    """Run a lightweight completeness check over generated Phase 3 outputs."""
    expected_files = [
        MATRIX_PATH,
        NOTES_PATH,
        METRICS_PATH,
        GAP_SCORES_PATH,
        STATS_PATH,
        REPORT_PATH,
        CASE_STUDIES_PATH,
        CHARTS_DIR / "coverage_heatmap.png",
        CHARTS_DIR / "gap_scores.png",
        CHARTS_DIR / "usage_vs_coverage_scatter.png",
        CHARTS_DIR / "temporal_trends.png",
        CHARTS_DIR / "quality_radar.png",
    ]
    missing = [path for path in expected_files if not path.exists()]
    if missing:
        raise FileNotFoundError(f"Missing generated outputs: {missing}")

    matrix = pd.read_csv(MATRIX_PATH)
    notes = pd.read_csv(NOTES_PATH)
    gaps = pd.read_csv(GAP_SCORES_PATH)
    stats_df = pd.read_csv(STATS_PATH)
    if matrix.isna().any().any():
        raise ValueError("Coverage matrix contains missing values.")
    if notes["justification"].isna().any():
        raise ValueError("Coverage notes contain missing justifications.")
    if gaps["gap_score"].isna().any():
        raise ValueError("Gap scores contain missing values.")
    if len(stats_df) < 5:
        raise ValueError("Fewer than five statistical tests were reported.")
