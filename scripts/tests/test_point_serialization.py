import pandas as pd

from src.config.settings import (
    CANDIDATE_INDEX_FILE,
)

from src.qdrant.point import build_point

df = pd.read_parquet(
    CANDIDATE_INDEX_FILE
)

candidate = df.iloc[0].to_dict()

point = build_point(candidate)

print("=" * 60)
print(type(point.id))
print(type(point.vector))
print(type(point.payload))

for k, v in point.payload.items():
    print(k, type(v))

print("=" * 60)

# THIS IS THE IMPORTANT PART
print(point.model_dump())