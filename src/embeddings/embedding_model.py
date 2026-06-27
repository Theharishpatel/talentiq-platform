"""
Embedding model loader.
"""

import torch

from sentence_transformers import (
    SentenceTransformer,
)

MODEL_NAME = "BAAI/bge-base-en-v1.5"

_model = None


def get_embedding_model():

    global _model

    if _model is None:

        device = (
            "cuda"
            if torch.cuda.is_available()
            else "cpu"
        )

        print(f"Embedding Device : {device}")

        _model = SentenceTransformer(
            MODEL_NAME,
            device=device,
        )

    return _model