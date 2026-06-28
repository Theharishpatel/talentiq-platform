"""
Build candidate feature dataset.

Reads cleaned candidates and generates
candidate_features.parquet.

Usage
-----
python tools/build_candidate_features.py
"""

from pathlib import Path

import orjson
import pyarrow as pa
import pyarrow.parquet as pq

from tqdm import tqdm

from src.features.feature_builder import (
    build_candidate_features,
)

# ------ Config -----

INPUT_FILE = Path(
    "data/processed/clean_candidates.jsonl"
)

OUTPUT_FILE = Path(
    "data/processed/candidate_features.parquet"
)

BATCH_SIZE = 1000


# ----- Load Data ----

records = []

with open(INPUT_FILE, "rb") as f:

    for line in f:

        records.append(
            orjson.loads(line)
        )

print(f"\nCandidates : {len(records)}")


# ----- Parquet Writer ----- 

writer = None


# ---- Process -----

for i in tqdm(

    range(
        0,
        len(records),
        BATCH_SIZE,
    ),

    desc="Building Features",

):

    batch = records[
        i:i + BATCH_SIZE
    ]

    feature_rows = []

    for candidate in batch:

        feature_rows.append(

            build_candidate_features(
                candidate
            )

        )

    table = pa.Table.from_pylist(
        feature_rows
    )

    if writer is None:

        writer = pq.ParquetWriter(

            OUTPUT_FILE,

            table.schema,

            compression="snappy",

        )

    writer.write_table(
        table
    )

if writer:

    writer.close()


print()
print("=" * 60)
print("Feature Dataset Generated")
print("=" * 60)
print(f"Saved : {OUTPUT_FILE}")