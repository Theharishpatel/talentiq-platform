"""
Test payload builder.
"""

import pandas as pd

from src.qdrant.payload import (
    build_payload,
)

df = pd.read_parquet(
    "data/processed/candidate_index.parquet"
)

candidate = df.iloc[0].to_dict()

payload = build_payload(
    candidate
)

print("=" * 60)
print("Payload")
print("=" * 60)

for key, value in payload.items():

    print(
        f"{key}: {value}"
    )