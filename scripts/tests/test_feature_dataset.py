import pandas as pd

df = pd.read_parquet(
    "data/processed/candidate_features.parquet"
)

print("=" * 60)
print("Shape")
print("=" * 60)
print(df.shape)

print()

print("=" * 60)
print("Columns")
print("=" * 60)
print(df.columns.tolist())

print()

print("=" * 60)
print("First Candidate")
print("=" * 60)
print(df.iloc[0])

print()

print("=" * 60)
print("Data Types")
print("=" * 60)
print(df.dtypes)