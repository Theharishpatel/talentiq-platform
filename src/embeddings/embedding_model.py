"""
Embedding model loader.
"""

from sentence_transformers import (
    SentenceTransformer,
)

MODEL_NAME = (
    "BAAI/bge-base-en-v1.5"
)

_model = None

def get_embedding_model():

    global _model

    if _model is None:

        _model = SentenceTransformer(
            MODEL_NAME
        )

    return _model