"""
Configuration for JD embedding.

this module contains all configurable parameters used by the JD embedding pipeline.
"""

# ------ embedding model -----

MODEL_NAME = (
    "BAAI/bge-base-en-v1.5"
)

# ------ embedding settings ----

EMBEDDING_DIMENSION = 768

NORMALIZE_EMBEDDINGS = True

# -----runtime ----

DEVICE = "cpu"

BATCH_SIZE = 32