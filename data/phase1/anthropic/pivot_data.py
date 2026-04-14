import pandas as pd

df_claude = pd.read_csv("aei_raw_claude_ai_2025-11-13_to_2025-11-20.csv")
df_api    = pd.read_csv("aei_raw_1p_api_2025-11-13_to_2025-11-20.csv")

df_all = pd.concat([df_claude, df_api], ignore_index=True)

# Step 1: Keep only level 0 (top-level, no sub-breakdowns)
df_all = df_all[df_all["level"] == 0]

# Step 2: Keep only the summary metrics (drop CI bounds)
keep_variables = [
    "ai_autonomy_mean",
    "ai_autonomy_median",
    "ai_education_years_mean",
    "human_education_years_mean",
    "human_only_time_mean",
    "human_with_ai_time_mean",
    "usage_count",
    "usage_pct",
    "collaboration_pct",
    "task_success_pct",
    "use_case_pct",
    "human_only_ability_pct",
    "multitasking_pct",
]
df_all = df_all[df_all["variable"].isin(keep_variables)]

# Step 3: Build col key and pivot
df_all["col_key"] = df_all["variable"] + df_all["cluster_name"].apply(
    lambda x: f"__{x}" if pd.notna(x) and str(x).strip() != "" else ""
)

pivot = df_all.pivot_table(
    index=["geo_id", "geography", "date_start", "date_end", "platform_and_product"],
    columns="col_key",
    values="value",
    aggfunc="first"
).reset_index()

pivot.columns.name = None

print(pivot.shape)
print(pivot.head())

# Save it
pivot.to_csv("aei_pivot.csv", index=False)

