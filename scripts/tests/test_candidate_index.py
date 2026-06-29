"""
Test candidate index dataset.
"""

from pathlib import Path

import pandas as pd


# ----- Config ----

INPUT_FILE = Path(
    "data/processed/candidate_index.parquet"
)

# ----- Load  ------

df = pd.read_parquet(
    INPUT_FILE
)

# ---- Shape ----

print("=" * 60)
print("Shape")
print("=" * 60)

print(df.shape)

# ------ Colunms ----

print()

print("=" * 60)
print("Columns")
print("=" * 60)

print(df.columns.tolist())

# ------ First Ccandidate ------

print()

print("=" * 60)
print("First Candidate")
print("=" * 60)

print(df.iloc[0])

# ---- Data Types -----

print()

print("=" * 60)
print("Data Types")
print("=" * 60)

print(df.dtypes)

# ------ Null Values -----

print()

print("=" * 60)
print("Null Values")
print("=" * 60)

print(df.isnull().sum())

# ----- Duplicate IDs -----

print()

print("=" * 60)
print("Duplicate Candidate IDs")
print("=" * 60)

duplicates = df["candidate_id"].duplicated().sum()

print(duplicates)

# ------ Embeddig Check ---- 

print()

print("=" * 60)
print("Embedding Check")
print("=" * 60)

embedding = df.iloc[0]["embedding"]

print("Embedding Length :", len(embedding))

print("First 10 Values :")

print(embedding[:10])

# ----- Summary -----

print()

print("=" * 60)
print("Summary")
print("=" * 60)

print(f"Rows      : {len(df)}")
print(f"Columns   : {len(df.columns)}")
print(f"Duplicates: {duplicates}")
print(f"Embedding : {len(embedding)} dimensions")