# task2/task2.py
import pandas as pd
import os

os.makedirs("task2", exist_ok=True)

all_repo_df = pd.read_parquet("hf://datasets/hao-li/AIDev/all_repository.parquet")

cols_needed = ['id', 'language', 'stars', 'url']
missing = [c for c in cols_needed if c not in all_repo_df.columns]
if missing:
    raise KeyError(f"Missing columns in all_repository.parquet: {missing}")

out = all_repo_df[cols_needed].rename(columns={
    'id': 'REPOID',
    'language': 'LANG',
    'stars': 'STARS',
    'url': 'REPOURL'
})

out.to_csv("task2/task2_output.csv", index=False)
print("Task 2 complete — wrote task2/task2_output.csv")
