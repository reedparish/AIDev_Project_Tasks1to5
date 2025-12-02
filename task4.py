# task4/task4.py
import pandas as pd
import os
import re

os.makedirs("task4", exist_ok=True)

pr_commit_details_df = pd.read_parquet("hf://datasets/hao-li/AIDev/pr_commit_details.parquet")

cols_expected = ['pr_id', 'sha', 'message', 'filename', 'status', 'additions', 'deletions', 'changes', 'patch']
missing = [c for c in cols_expected if c not in pr_commit_details_df.columns]
if missing:
    raise KeyError(f"Missing columns in pr_commit_details.parquet: {missing}")

def clean_diff(patch):
    if patch is None:
        return ""
    s = str(patch)
    # Replace non-printable / non-ASCII characters with space to avoid encoding issues
    s = re.sub(r'[^\x20-\x7E]+', ' ', s)
    # Optionally collapse multi-space/newlines into single space
    s = re.sub(r'\s+', ' ', s).strip()
    return s

out = pd.DataFrame({
    'PRID': pr_commit_details_df['pr_id'],
    'PRSHA': pr_commit_details_df['sha'],
    'PRCOMMITMESSAGE': pr_commit_details_df['message'],
    'PRFILE': pr_commit_details_df['filename'],
    'PRSTATUS': pr_commit_details_df['status'],
    'PRADDS': pr_commit_details_df['additions'],
    'PRDELSS': pr_commit_details_df['deletions'],
    'PRCHANGECOUNT': pr_commit_details_df['changes'],
    'PRDIFF': pr_commit_details_df['patch'].apply(clean_diff)
})

out.to_csv("task4/task4_output.csv", index=False)
print("Task 4 complete — wrote task4/task4_output.csv")
