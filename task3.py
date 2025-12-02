# task3/task3.py
import pandas as pd
import os

os.makedirs("task3", exist_ok=True)

pr_task_type_df = pd.read_parquet("hf://datasets/hao-li/AIDev/pr_task_type.parquet")

cols_needed = ['id', 'title', 'reason', 'type', 'confidence']
missing = [c for c in cols_needed if c not in pr_task_type_df.columns]
if missing:
    raise KeyError(f"Missing columns in pr_task_type.parquet: {missing}")

out = pr_task_type_df[cols_needed].rename(columns={
    'id': 'PRID',
    'title': 'PRTITLE',
    'reason': 'PRREASON',
    'type': 'PRTYPE',
    'confidence': 'CONFIDENCE'
})

out.to_csv("task3/task3_output.csv", index=False)
print("Task 3 complete — wrote task3/task3_output.csv")
