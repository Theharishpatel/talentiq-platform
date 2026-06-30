"""
Test Point Builder.
"""

import pandas as pd

from src.config.settings import (
    CANDIDATE_INDEX_FILE,
)

from src.qdrant.point import (
    build_point,
)

df = pd.read_parquet(
    CANDIDATE_INDEX_FILE
)

candidate = df.iloc[0].to_dict()

point = build_point(
    candidate
)

print("=" * 60)
print("Point")
print("=" * 60)

print(point.id)

print(len(point.vector))

print(point.payload.keys())