from src.demo.loader import (
    load_demo_candidates,
)

df = load_demo_candidates()

print()

print("=" * 60)

print("Demo Candidates")

print("=" * 60)

print()

print(df.head())

print()

print("Rows :", len(df))

print("Columns :", len(df.columns))