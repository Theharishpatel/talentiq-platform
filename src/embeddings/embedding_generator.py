"""
Candidate embedding generation.
"""

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
    )

    return vector.tolist()


def generate_embeddings(
        texts: list[str],
        batch_size: int = 64,
) -> list[list[float]]:

    model = get_embedding_model()

    vectors = model.encode(
        texts,
        normalize_embeddings=True,
        batch_size=batch_size,
        show_progress_bar=False,
    )

    return vectors.tolist()