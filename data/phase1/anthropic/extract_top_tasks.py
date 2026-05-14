"""
Extract Top O*NET Tasks per Country from Anthropic Economic Index Raw Data

Purpose:
    Loads both AEI raw CSV files and extracts the top O*NET task
    (by request_count from the value column) for each country.
    Tasks are identified in the cluster_name column at level 1
    (broader task groups, ~112 unique tasks).

Inputs:
    aei_raw_claude_ai_2025-11-13_to_2025-11-20.csv
    aei_raw_1p_api_2025-11-13_to_2025-11-20.csv  (in the same directory)

Outputs:
    top_task_per_country.csv    — one row per country: geo_id, country top task,
                                  request_count, request_pct
    top_tasks_by_frequency.csv  — global ranked list of all tasks
    task_instances_raw.csv      — written to data/phase1/ with Phase 1 fields

Usage:
    cd data/phase1/anthropic
    python extract_top_tasks.py
"""

import pandas as pd
import os

# Paths
HERE = os.path.dirname(os.path.abspath(__file__))
RAW_CLAUDE = os.path.join(HERE, "aei_raw_claude_ai_2026-02-05_to_2026-02-12.csv")
RAW_API    = os.path.join(HERE, "aei_raw_1p_api_2026-02-05_to_2026-02-12.csv")
OUT_PER_COUNTRY = os.path.join(HERE, "top_task_per_country.csv")
OUT_GLOBAL      = os.path.join(HERE, "top_tasks_by_frequency.csv")
OUT_PHASE1      = os.path.join(HERE, "..", "task_instances_raw.csv")

TOP_N = 200   # for global ranked list and Phase 1 output
TASK_LEVEL = 1  # level 1 = broader O*NET task groups (~112 tasks)


def load_raw(path: str) -> pd.DataFrame:
    """Load a raw AEI CSV file.

    Args:
        path: Absolute path to the CSV file.

    Returns:
        DataFrame with columns: geo_id, geography, date_start, date_end,
        platform_and_product, facet, level, variable, cluster_name, value.
    """
    return pd.read_csv(path)


def filter_task_rows(df: pd.DataFrame, task_level: int) -> pd.DataFrame:
    """Filter to country-level rows with request_count for O*NET tasks.

    Args:
        df:         Combined raw DataFrame.
        task_level: The level value containing O*NET task names.

    Returns:
        Filtered DataFrame with country-level task request counts.
    """
    mask = (
        (df["variable"] == "request_count") &
        (df["level"] == task_level) &
        (df["geography"] == "country") &
        df["cluster_name"].notna() &
        (df["cluster_name"].str.strip() != "") &
        (df["cluster_name"] != "not_classified")
    )
    return df[mask].copy()


def extract_top_task_per_country(task_rows: pd.DataFrame) -> pd.DataFrame:
    """Find the single most common O*NET task for each country.

    Args:
        task_rows: Filtered DataFrame from filter_task_rows().

    Returns:
        DataFrame with one row per country: geo_id, top_task,
        request_count, request_pct (% of that country's total).
    """
    # For each country, find the task with the highest request_count.
    idx = task_rows.groupby("geo_id")["value"].idxmax()
    top = task_rows.loc[idx, ["geo_id", "cluster_name", "value"]].copy()
    top = top.rename(columns={"cluster_name": "top_task", "value": "request_count"})

    # Calculate each country's total request count for percentage.
    country_totals = task_rows.groupby("geo_id")["value"].sum().rename("country_total")
    top = top.merge(country_totals, on="geo_id", how="left")
    top["request_pct"] = (top["request_count"] / top["country_total"] * 100).round(2)
    top = top.drop(columns="country_total")
    top = top.sort_values("request_count", ascending=False).reset_index(drop=True)

    return top


def extract_global_task_frequencies(task_rows: pd.DataFrame) -> pd.DataFrame:
    """Sum task request counts across all countries for a global ranking.

    Args:
        task_rows: Filtered DataFrame from filter_task_rows().

    Returns:
        DataFrame sorted descending by usage_pct, with columns:
        rank, task_description, usage_count, usage_pct.
    """
    grouped = (
        task_rows.groupby("cluster_name")["value"]
        .sum()
        .reset_index()
        .rename(columns={"cluster_name": "task_description", "value": "usage_count"})
    )

    total = grouped["usage_count"].sum()
    grouped["usage_pct"] = (grouped["usage_count"] / total * 100).round(4)
    grouped = grouped.sort_values("usage_pct", ascending=False).reset_index(drop=True)
    grouped.insert(0, "rank", grouped.index + 1)

    return grouped[["rank", "task_description", "usage_count", "usage_pct"]]


def build_phase1_csv(tasks: pd.DataFrame, top_n: int) -> pd.DataFrame:
    """Convert top tasks into the Phase 1 task_instances_raw.csv format.

    Required fields per CLAUDE.md Phase 1 Week 1:
        source, task_description, domain, frequency, context, source_type

    Args:
        tasks:  DataFrame from extract_global_task_frequencies().
        top_n:  Number of top tasks to include.

    Returns:
        DataFrame in Phase 1 format.
    """
    top = tasks.head(top_n).copy()
    top["source"]      = "Handa et al. (2025) — Anthropic Economic Index arXiv:2503.04761"
    top["domain"]      = ""   # to be filled during open coding (Week 2)
    top["frequency"]   = top["usage_pct"].astype(str) + "%"
    top["context"]     = "occupational/personal"
    top["source_type"] = "usage log"
    return top[["source", "task_description", "domain", "frequency", "context", "source_type"]]


def main():
    """Main execution."""
    print("Loading raw data...")
    df_claude = load_raw(RAW_CLAUDE)
    df_api    = load_raw(RAW_API)
    df_all    = pd.concat([df_claude, df_api], ignore_index=True)
    print(f"Total rows loaded: {len(df_all)}")

    # ── Step 1: Filter to country-level O*NET task rows ──────────────────────
    print(f"\nFiltering to country-level task rows at level={TASK_LEVEL}...")
    task_rows = filter_task_rows(df_all, task_level=TASK_LEVEL)
    print(f"Task rows found: {len(task_rows)}")
    print(f"Unique countries: {task_rows['geo_id'].nunique()}")
    print(f"Unique tasks: {task_rows['cluster_name'].nunique()}")

    if task_rows.empty:
        print("No task rows found. Check level and variable filters.")
        return

    # ── Step 2: Extract top task per country ─────────────────────────────────
    print("\n=== Top O*NET Task per Country ===")
    top_per_country = extract_top_task_per_country(task_rows)
    print(top_per_country.head(20).to_string(index=False))

    top_per_country.to_csv(OUT_PER_COUNTRY, index=False)
    print(f"\nTop task per country ({len(top_per_country)} countries) saved to: {OUT_PER_COUNTRY}")

    # ── Step 3: Global ranked list ───────────────────────────────────────────
    print("\n=== Global Task Ranking ===")
    global_tasks = extract_global_task_frequencies(task_rows)
    print(global_tasks.head(20).to_string(index=False))

    global_tasks.to_csv(OUT_GLOBAL, index=False)
    print(f"\nFull global ranking ({len(global_tasks)} tasks) saved to: {OUT_GLOBAL}")

    # ── Step 4: Write Phase 1 task_instances_raw.csv ─────────────────────────
    phase1_df = build_phase1_csv(global_tasks, top_n=TOP_N)
    phase1_df.to_csv(OUT_PHASE1, index=False)
    print(f"\nPhase 1 task_instances_raw.csv written to: {OUT_PHASE1}")
    print(f"Rows written: {len(phase1_df)} (target: 100–200)")


if __name__ == "__main__":
    main()
