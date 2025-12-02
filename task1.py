# task1/task1.py
import pandas as pd
import os

os.makedirs("task1", exist_ok=True)

all_pr_df = pd.read_parquet("hf://datasets/hao-li/AIDev/all_pull_request.parquet")

# Select columns required by assignment (exact names requested)
cols_needed = ['title', 'id', 'agent', 'body', 'repo_id', 'repo_url']

missing = [c for c in cols_needed if c not in all_pr_df.columns]
if missing:
    raise KeyError(f"Missing columns in all_pull_request.parquet: {missing}")

out = all_pr_df[cols_needed].rename(columns={
    'title': 'TITLE',
    'id': 'ID',
    'agent': 'AGENTNAME',
    'body': 'BODYSTRING',
    'repo_id': 'REPOID',
    'repo_url': 'REPOURL'
})

out.to_csv("task1/task1_output.csv", index=False)
print("Task 1 complete — wrote task1/task1_output.csv")
