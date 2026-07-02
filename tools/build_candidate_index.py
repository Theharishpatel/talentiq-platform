"""
Build candidate index dataset.

Reads

- clean_candidates.jsonl
- candidate_features.parquet
- candidate_embeddings.parquet

Generates

candidate_index.parquet

Usage
-----
python -m tools.build_candidate_index
"""

from pathlib import Path

import orjson
import pandas as pd

import pyarrow as pa
import pyarrow.parquet as pq

from tqdm import tqdm

from src.index.builder import (
    build_candidate_index,
)

# ------- Config -----

CANDIDATES_FILE = Path(
    "data/processed/clean_candidates.jsonl"
)

FEATURES_FILE = Path(
    "data/processed/candidate_features.parquet"
)

EMBEDDINGS_FILE = Path(
    "data/artifacts/candidate_embeddings.parquet"
)

OUTPUT_FILE = Path(
    "data/processed/candidate_index.parquet"
)

BATCH_SIZE = 1000

# ----Load Candidates ------

candidates = []

with open(CANDIDATES_FILE, "rb") as f:

    for line in f:

        candidates.append(
            orjson.loads(line)
        )

print(f"\nCandidates : {len(candidates)}")

# ----- Load Features -----

features_df = pd.read_parquet(
    FEATURES_FILE
)

print(f"Features : {len(features_df)}")

# ----- Load Embeddings ----

embeddings_df = pd.read_parquet(
    EMBEDDINGS_FILE
)

print(f"Embeddings : {len(embeddings_df)}")

# ------ Validation ------

if not (

    len(candidates)

    ==

    len(features_df)

    ==

    len(embeddings_df)

):

    raise ValueError(

        "Dataset size mismatch."

    )

# ---- Lookups ----

feature_lookup = {

    row["candidate_id"]: row

    for row in features_df.to_dict(
        orient="records"
    )

}

embedding_lookup = {

    row["candidate_id"]: row["embedding"]

    for row in embeddings_df.to_dict(
        orient="records"
    )

}

# ------ Parquet Writer ------

writer = None

# ---- Build Index ----

for i in tqdm(

    range(
        0,
        len(candidates),
        BATCH_SIZE,
    ),

    desc="Building Candidate Index",

):

    batch = candidates[
        i:i + BATCH_SIZE
    ]

    rows = build_candidate_index(

        candidates=batch,

        feature_lookup=feature_lookup,

        embedding_lookup=embedding_lookup,

    )

    table = pa.Table.from_pylist(
        rows
    )

    if writer is None:

        writer = pq.ParquetWriter(

            OUTPUT_FILE,

            table.schema,

            compression="snappy",

        )

    writer.write_table(
        table)

# ----- Close Writer -----

if writer:

    writer.close()

print()

print("=" * 60)

print("Candidate Index Generated")

print("=" * 60)

print(f"Saved : {OUTPUT_FILE}")