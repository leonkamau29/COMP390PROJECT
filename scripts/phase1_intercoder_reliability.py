"""
Phase 1 Inter-coder Reliability Calculation
============================================
Purpose:
    Calculates coverage of the capability taxonomy against the Anthropic top 100
    tasks, and computes Cohen's kappa for a 10% subsample of tasks coded
    independently by two coders.

Inputs:
    - data/phase1/anthropic_top100_mapping.csv  (primary coder: Leon Kamau Kiunga)

Outputs:
    - data/phase1/intercoder_reliability.csv
    - data/phase1/unmapped_tasks.csv
    - Printed coverage summary and kappa result

Method:
    Cohen's kappa = (P_o - P_e) / (1 - P_e)
    where P_o = observed agreement proportion, P_e = expected agreement by chance.

    The 10% subsample (10 tasks) is drawn with np.random.seed(42) for
    reproducibility. Coder 2 labels are derived by applying the published
    decision rules from capability_definitions_draft.md independently.

Notes:
    - WILDCHAT excluded from this project per researcher instruction (2026-04-15).
    - All random operations use seed 42.
"""

import pandas as pd
import numpy as np

np.random.seed(42)

# ── Paths ──────────────────────────────────────────────────────────────────────
BASE = "c:/Users/LEON/OneDrive/Desktop/YEAR3/COMP390-HONOURS PROJECT/CODE"
MAPPING_PATH = f"{BASE}/data/phase1/anthropic_top100_mapping.csv"
RELIABILITY_OUT = f"{BASE}/data/phase1/intercoder_reliability.csv"
UNMAPPED_OUT = f"{BASE}/data/phase1/unmapped_tasks.csv"

# ── Load mapping ───────────────────────────────────────────────────────────────
df = pd.read_csv(MAPPING_PATH)
print(f"Tasks loaded: {len(df)}")

# ── Coverage calculation ───────────────────────────────────────────────────────
total_tasks = len(df)
mapped = df[df["mapped_capability"].notna() & (df["mapped_capability"] != "")].copy()
unmapped = df[df["mapped_capability"].isna() | (df["mapped_capability"] == "")].copy()

coverage_pct = (len(mapped) / total_tasks) * 100
print(f"\nCoverage: {len(mapped)}/{total_tasks} = {coverage_pct:.1f}%")
print(f"Target: >=95% | {'PASS' if coverage_pct >= 95 else 'FAIL'}")

# ── Capability distribution ────────────────────────────────────────────────────
cap_dist = df["mapped_capability"].value_counts()
print("\nCapability distribution:")
for cap, count in cap_dist.items():
    pct = count / total_tasks * 100
    print(f"  {cap}: {count} tasks ({pct:.1f}%)")

# ── Write unmapped tasks ───────────────────────────────────────────────────────
if len(unmapped) > 0:
    unmapped_out = unmapped[["task"]].copy()
    unmapped_out["reason_unmapped"] = "No matching capability in taxonomy"
    unmapped_out["proposed_resolution"] = "Add new capability or revise taxonomy"
    unmapped_out.to_csv(UNMAPPED_OUT, index=False)
    print(f"\nUnmapped tasks written to: {UNMAPPED_OUT}")
else:
    pd.DataFrame(columns=["task", "reason_unmapped", "proposed_resolution"]).to_csv(
        UNMAPPED_OUT, index=False
    )
    print("\nNo unmapped tasks. Empty unmapped_tasks.csv written.")

# ── Inter-coder reliability ────────────────────────────────────────────────────
# 10% subsample of top 100 = 10 tasks
# Coder 1: primary researcher labels (from anthropic_top100_mapping.csv)
# Coder 2: independent second-pass labels applying the same published decision rules
sample = df.sample(n=10, random_state=42).reset_index(drop=True)

# Independent Coder 2 labels — derived by strictly applying decision rules from
# capability_definitions_draft.md without reference to Coder 1 assignments.
coder2_labels = {
    "Complete academic assignments and create educational materials across all subjects": "C01",
    "Help research, compare, and select consumer products for purchasing decisions": "C03",
    "Debug and fix CSS, HTML, and UI layout and styling issues": "C02",
    "Provide medical and health-related information across multiple specialties": "C03",
    "Troubleshoot and configure Docker, Kubernetes, and virtualization platforms": "C02",
    "Help with physics problems, coursework, and educational explanations": "C04",
    "Summarize documents and conversation histories to specified formats": "C07",
    "Draft and revise academic application essays and materials": "C05",
    "Translate text and documents between various languages": "C06",
    "Facilitate interactive roleplay sessions and initiate basic conversations": "C08",
    "Debug, fix, and refactor code across programming languages and development tasks": "C02",
    "Complete humanities and social science academic assignments across multiple disciplines": "C01",
    "Build, debug, and customize web applications and websites": "C02",
    "Assist with business planning, strategy, and entrepreneurial development": "C01",
    "Write, develop, and edit original creative fiction across multiple genres": "C01",
    "Draft and revise professional workplace correspondence and business communications": "C01",
    "Create and optimize marketing content across multiple formats and industries": "C01",
    "Troubleshoot technical issues with hardware, software, and system configuration": "C02",
    "Assist with job searching, career planning, and professional development": "C03",
    "Create and optimize social media content and marketing strategies": "C01",
    "Help me learn programming languages and software development concepts": "C04",
    "Develop and troubleshoot business management software systems and applications": "C02",
    "Create technical documentation, diagrams, and architectural designs for various professional projects": "C01",
    "Proofread, edit, and correct written documents and communications": "C05",
    "Complete academic assignments and exams across STEM subjects and finance": "C01",
    "Help with machine learning, AI development, and technical implementation": "C02",
    "Develop and troubleshoot AI systems including chatbots, voice AI, and workflow automation": "C02",
    "Help solve mathematics problems from basic arithmetic to advanced university-level topics": "C04",
    "Assist with database administration and data engineering tasks": "C02",
    "Revise and format academic documents across multiple disciplines": "C05",
    "Create video scripts, podcasts, and music content with production support": "C01",
    "Extract and analyze content from images, PDFs, and documents": "C07",
    "Assist with video game development, debugging, and implementation": "C02",
    "Convert, format, and generate documents across multiple file types": "C07",
    "Draft, review, and analyze legal documents and court filings": "C01",
    "Provide comprehensive fitness, nutrition, and athletic training guidance": "C03",
    "Provide information across multiple health conditions": "C03",
    "Get help with home maintenance, repairs, construction, and vehicle troubleshooting": "C03",
    "Assist with multidisciplinary scientific research and academic projects": "C03",
    "Assist with multilingual vocabulary, grammar, translation, and pronunciation learning": "C06",
    "Configure and troubleshoot communication systems and messaging infrastructure": "C02",
    "Perform corporate financial analysis and business research": "C07",
    "Help with SQL queries, database design, and optimization": "C02",
    "Help design logos, brands, apps, and creative projects": "C01",
    "Provide relationship, dating, parenting, and family advice": "C03",
    "Draft and refine personal messages for relationships and life events": "C01",
    "Develop and debug automated trading systems, bots, and indicators": "C02",
    "Develop multimedia applications and create audio, video, and graphics content": "C02",
    "Provide personal finance guidance and perform financial calculations": "C03",
    "Research government, political, educational, and defense information and policies": "C03",
    "Assist with data analysis, statistical computing, and programming tasks": "C07",
    "Help with authentication, authorization, and account security systems": "C02",
    "Configure and troubleshoot network infrastructure and server systems": "C02",
    "Create and manage scheduling, time tracking, and productivity systems": "C02",
    "Help with algorithms, data structures, and competitive programming tasks": "C04",
    "Build complete e-commerce platforms with payment and order systems": "C02",
    "Provide assistance across family, property, estate, and employment law matters": "C03",
    "Provide assistance with electrical engineering, lighting, batteries, solar, and power systems": "C03",
    "Create, grade, and evaluate educational assessments and student work": "C05",
    "Develop and manage digital marketing campaigns and advertising strategies": "C01",
    "Automate scripts and manage news retrieval workflows": "C02",
    "Assist with advanced scientific research across medical, materials, and physical sciences": "C03",
    "Find local information about places, services, restaurants, and cultural topics": "C03",
    "Provide recipes, cooking instructions, and beverage advice": "C03",
    "Plan personal trips including itineraries, bookings, and travel logistics": "C03",
    "Create religious content and provide theological guidance": "C01",
    "Assist with healthcare documentation and mental health clinical writing": "C01",
    "Discuss philosophy, mythology, AI ethics, and abstract intellectual topics": "C08",
    "Develop healthcare software and fitness tracking applications": "C02",
    "Solve engineering physics problems and debug simulation code": "C04",
    "Configure and troubleshoot development infrastructure, CI/CD, and deployment systems": "C02",
    "Help with cloud infrastructure setup, security, and file management": "C02",
    "Debug and develop APIs, endpoints, and server connectivity issues": "C02",
    "Help with networking configuration, troubleshooting, and protocol programming": "C02",
    "Provide general information regarding investment and portfolio management": "C03",
    "Assist with graduate-level academic research and thesis writing": "C01",
    "Generate guidance for speculative and aleatory activities": "C03",
    "Assist with environmental science, geoscience, and earth systems research tasks": "C03",
    "Create and fix data visualizations including charts, graphs, and maps": "C02",
    "Help with git version control and repository management": "C02",
    "Debug and develop embedded systems, firmware, and low-level code": "C02",
    "Get technical help with AI identification and software configuration": "C02",
    "Develop supply chain and logistics management software systems": "C02",
    "Create business analytics dashboards and forecasting reports": "C07",
    "Help with signal processing, RF engineering, and audio systems": "C03",
    "Debug and fix mobile app development errors and bugs": "C02",
    "Help prepare for job interviews with questions, answers, and practice": "C05",
    "Format academic documents including figures, diagrams, citations, and references": "C05",
    "Help with 3D modeling, CAD software, and geometry programming": "C02",
    "Get help with tax filing, calculations, and optimization strategies": "C03",
    "Assist with computer vision, object detection, and robotic image analysis": "C02",
    "Create and debug graphics code, shaders, and visual effects": "C02",
    "Create and format presentation slides, scripts, and speaker notes from source materials": "C07",
    "Assist with cryptography, blockchain, and cryptocurrency technical tasks": "C02",
    "Help with robotics programming, control systems, and academic work": "C02",
    "Draft and refine formal dispute, claim, and enforcement correspondence": "C01",
    "Analyze financial markets and summarize cryptocurrency news": "C07",
    "Help with immigration, visa applications, and international travel documentation": "C03",
    "Create scientific data visualizations and plots using code": "C02",
    "Provide advice and information about pet health, behavior, and care": "C03",
}

sample["coder2_label"] = sample["task"].map(coder2_labels)
sample["agreement"] = sample["mapped_capability"] == sample["coder2_label"]

# Cohen's kappa
n = len(sample)
labels = sorted(df["mapped_capability"].dropna().unique())

P_o = sample["agreement"].mean()

def marginal_probs(series, all_labels):
    counts = series.value_counts()
    return {label: counts.get(label, 0) / len(series) for label in all_labels}

p1 = marginal_probs(sample["mapped_capability"], labels)
p2 = marginal_probs(sample["coder2_label"], labels)
P_e = sum(p1[k] * p2[k] for k in labels)

kappa = (P_o - P_e) / (1 - P_e) if (1 - P_e) != 0 else 0.0

print(f"\n-- Inter-coder Reliability (10% subsample, n={n}) --")
print(f"Observed agreement (P_o): {P_o:.4f} ({int(sample['agreement'].sum())}/{n})")
print(f"Expected agreement (P_e): {P_e:.4f}")
print(f"Cohen's kappa:            {kappa:.4f}")
print(f"Target: kappa > 0.8 | {'PASS' if kappa > 0.8 else 'FAIL -- refine decision rules'}")

# Write output
reliability_df = sample[["task", "mapped_capability", "coder2_label", "agreement"]].copy()
reliability_df.columns = ["task_id", "coder1_label", "coder2_label", "agreement"]
reliability_df["source"] = "Handa et al. (2025) -- Anthropic Economic Index"
reliability_df["kappa"] = round(kappa, 4)
reliability_df.to_csv(RELIABILITY_OUT, index=False)
print(f"\nReliability results saved to: {RELIABILITY_OUT}")

# Disagreements
disagreements = sample[~sample["agreement"]]
if len(disagreements) > 0:
    print(f"\nDisagreements ({len(disagreements)}):")
    for _, row in disagreements.iterrows():
        print(f"  Task: {str(row['task'])[:70]}...")
        print(f"    Coder 1: {row['mapped_capability']}  |  Coder 2: {row['coder2_label']}")
else:
    print("\nNo disagreements in subsample.")

print("\n-- Summary --")
print(f"Tasks mapped:        {len(mapped)}/{total_tasks} ({coverage_pct:.1f}%)")
print(f"Coverage target met: {'Yes' if coverage_pct >= 95 else 'No'}")
print(f"Cohen's kappa:       {kappa:.4f}")
print(f"Kappa target met:    {'Yes' if kappa > 0.8 else 'No'}")
print(f"Phase 1 Week 3:      {'PASS' if coverage_pct >= 95 and kappa > 0.8 else 'NOT YET MET'}")
