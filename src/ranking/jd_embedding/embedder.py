"""
JD Embedding Generator.

Generates dense vector embeddings
for structured Job Descriptions.
"""

from functools import lru_cache

import numpy as np

from sentence_transformers import (
    SentenceTransformer,
)

from src.ranking.jd_embedding.config import (
    MODEL_NAME,
    DEVICE,
    NORMALIZE_EMBEDDINGS,
)


# ------ Model Loader ------

@lru_cache(maxsize=1)
def load_model() -> SentenceTransformer:
    """
    Load embedding model only once.
    """

    return SentenceTransformer(
        MODEL_NAME,
        device=DEVICE,
    )


# ------- Single Embedding ------

def embed_text(
    text: str,
) -> np.ndarray:
    """
    Generate embedding for one JD.
    """

    model = load_model()

    embedding = model.encode(

        text,

        normalize_embeddings=
        NORMALIZE_EMBEDDINGS,

        convert_to_numpy=True,

        show_progress_bar=False,

    )

    return embedding.astype(
        np.float32
    )


# ----- Batch Embedding ------

def embed_batch(
    texts: list[str],
) -> np.ndarray:
    """
    Generate embeddings for
    multiple JDs.
    """

    model = load_model()

    embeddings = model.encode(

        texts,

        normalize_embeddings=
        NORMALIZE_EMBEDDINGS,

        convert_to_numpy=True,

        show_progress_bar=False,

    )

    return embeddings.astype(
        np.float32
    )