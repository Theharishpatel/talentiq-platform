"""
JD Embedding Pipeline.

Converts a raw Job Description into

1. Structured JD
2. Embedding Text
3. Dense Embedding
"""

from src.ranking.role_intelligence.builder import (
    build_role_intelligence,
)

from src.ranking.jd_embedding.text_builder import (
    build_jd_text,
)

from src.ranking.jd_embedding.embedder import (
    embed_text,
)


def build_jd_embedding(
    jd: str,
) -> dict:
    """
    Complete JD embedding pipeline.

    Parameters
    ----------
    jd : str

    Returns
    -------
    dict
    """

    # ------ Role Intelligence ------

    role_profile = build_role_intelligence(
        jd
    )

    # ------ Build Embedding Text ------

    embedding_text = build_jd_text(
        role_profile
    )

    # ------ Generate Embedding ------

    embedding = embed_text(
        embedding_text
    )

    # ------ Return ------

    return {

        "role_profile":
            role_profile,

        "embedding_text":
            embedding_text,

        "embedding":
            embedding,

    }