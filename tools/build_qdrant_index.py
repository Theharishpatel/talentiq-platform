"""
Build Qdrant vector index from
candidate_index.parquet.

Usage
-----
python -m tools.build_qdrant_index
"""

import sys

import pandas as pd

from src.config.settings import (
    CANDIDATE_INDEX_FILE,
)

from src.qdrant.collection import (
    create_collection,
)

from src.qdrant.uploader import (
    upload_candidates,
)


# ==========================================================
# LOAD DATA
# ==========================================================

print("=" * 60)
print("Loading Candidate Index")
print("=" * 60)

df = pd.read_parquet(
    CANDIDATE_INDEX_FILE
)

print(f"Candidates : {len(df)}")
print()

# ==========================================================
# VALIDATE REQUIRED COLUMNS
# ==========================================================

required_columns = {

    "candidate_id",

    "embedding",

}

missing_columns = (

    required_columns

    - set(df.columns)

)

if missing_columns:

    raise ValueError(

        f"Missing columns : {missing_columns}"

    )

# ==========================================================
# DUPLICATE CHECK
# ==========================================================

duplicates = df[
    "candidate_id"
].duplicated().sum()

if duplicates:

    raise ValueError(

        f"Duplicate candidate IDs : {duplicates}"

    )

print("Duplicate Check : PASSED")

# ==========================================================
# EMBEDDING CHECK
# ==========================================================

embedding_size = len(

    df.iloc[0][
        "embedding"
    ]

)

if embedding_size != 768:

    raise ValueError(

        f"Expected 768 dimensions, got {embedding_size}"

    )

print("Embedding Dimension : PASSED")

print()

# ==========================================================
# CREATE COLLECTION
# ==========================================================

create_collection()

print()

# ==========================================================
# UPLOAD
# ==========================================================

upload_candidates(
    dataframe=df,
)

print()

# ==========================================================
# SUMMARY
# ==========================================================

print("=" * 60)

print("Qdrant Index Build Completed")

print("=" * 60)

print(f"Candidates : {len(df)}")

print(f"Embedding Dimension : {embedding_size}")

print("Status : SUCCESS")

print("=" * 60)

sys.exit(0)