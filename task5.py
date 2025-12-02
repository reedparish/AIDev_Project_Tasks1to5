# task5/task5.py
import pandas as pd
import os
import re

os.makedirs("task5", exist_ok=True)

# Load outputs from Tasks 1-4 (we only need 1 & 3 for fields requested)
t1 = pd.read_csv("task1/task1_output.csv", dtype=str).fillna("")
t3 = pd.read_csv("task3/task3_output.csv", dtype=str).fillna("")

# Merge: t1.ID  <->  t3.PRID
merged = t1.merge(t3, left_on="ID", right_on="PRID", how="left", suffixes=("", "_t3"))

# Ensure required columns exist
# ID (from t1), AGENT (AGENTNAME from t1), TYPE (PRTYPE from t3), CONFIDENCE (CONFIDENCE from t3)
if 'ID' not in merged.columns:
    raise KeyError("ID column missing after merge.")

# Security keyword list (use exactly as provided)
keywords = [
    "race","racy","buffer","overflow","stack","integer","signedness","underflow",
    "improper","unauthenticated","gain access","permission","cross site","css","xss",
    "denial service","dos","crash","deadlock","injection","request forgery","csrf",
    "xsrf","forged","security","vulnerability","vulnerable","exploit","attack","bypass",
    "backdoor","threat","expose","breach","violate","fatal","blacklist","overrun","insecure"
]

# Build regex: escape and allow multi-word phrases; use word boundaries where suitable
escaped = [re.escape(k) for k in keywords]
# join with alternation; use case-insensitive
pattern = re.compile(r'(' + r'|'.join(escaped) + r')', re.IGNORECASE)

def detect_security(title, body):
    text = (str(title) + " " + str(body)).lower()
    return 1 if pattern.search(text) else 0

merged['SECURITY'] = merged.apply(lambda r: detect_security(r.get('TITLE', ''), r.get('BODYSTRING', '')), axis=1)

final = merged[['ID']].copy()
final['AGENT'] = merged.get('AGENTNAME', "")
final['TYPE'] = merged.get('PRTYPE', "")
final['CONFIDENCE'] = merged.get('CONFIDENCE', "")
final['SECURITY'] = merged['SECURITY'].astype(int)

final.to_csv("task5/task5_output.csv", index=False)
print("Task 5 complete — wrote task5/task5_output.csv")
