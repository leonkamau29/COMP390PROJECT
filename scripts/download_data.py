"""
Download large datasets from Hugging Face that are excluded from GitHub.

Usage:
    python scripts/download_data.py

Requires:
    pip install huggingface_hub
    huggingface-cli login   (only needed for private repos)
"""

import os
from huggingface_hub import hf_hub_download

# TODO: replace with your actual Hugging Face username
REPO_ID = "Kiunga/COMP390HONOURS"

FILES = [
    "data/phase1/anthropic/aei_raw_1p_api_2025-11-13_to_2025-11-20.csv",
    "data/phase1/anthropic/aei_raw_claude_ai_2025-11-13_to_2025-11-20.csv",
    "data/phase1/onet/onet_task_mappings.csv",
    "data/phase1/onet/onet_task_statements.csv",
]

# Resolve project root relative to this script
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

for file_path in FILES:
    local_path = os.path.join(PROJECT_ROOT, file_path)
    if os.path.exists(local_path):
        print(f"Already exists, skipping: {file_path}")
        continue

    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    print(f"Downloading: {file_path} ...")
    hf_hub_download(
        repo_id=REPO_ID,
        filename=file_path,
        repo_type="dataset",
        local_dir=PROJECT_ROOT,
    )
    print(f"  -> saved to {local_path}")

print("\nAll files ready.")
