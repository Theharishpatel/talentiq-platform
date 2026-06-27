"""
Candidate embedding generation.
"""

import torch

from src.embeddings.embedding_model import (
    get_embedding_model,
)


def generate_embedding(
    text: str,
) -> list[float]:

    model = get_embedding_model()

    vector = model.encode(
        text,
        normalize_embeddings=True,
        convert_to_numpy=True,
        show_progress_bar=False,
    )

    return vector.tolist()


def generate_embeddings(
    texts: list[str],
    batch_size: int | None = None,
) -> list[list[float]]:

    model = get_embedding_model()

    if batch_size is None:

        if torch.cuda.is_available():
            batch_size = 1024
        else:
            batch_size = 128

    vectors = model.encode(
        texts,
        batch_size=batch_size,
        normalize_embeddings=True,
        convert_to_numpy=True,
        show_progress_bar=False,
    )

    return vectors.tolist()