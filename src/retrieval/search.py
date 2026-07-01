"""
Semantic candidate retrieval using Qdrant.
"""

from typing import Any

from qdrant_client.models import (
    ScoredPoint,
)

from src.config.settings import (
    QDRANT_COLLECTION,
)

from src.qdrant.client import (
    get_qdrant_client,
)


def _format_result(
    point: ScoredPoint,
) -> dict[str, Any]:
    """
    Convert Qdrant ScoredPoint into a
    project-specific result format.
    """

    return {

        "candidate_id":
            point.payload.get(
                "candidate_id"
            ),

        "similarity_score":
            round(
                float(point.score),
                6,
            ),

        "payload":
            point.payload,

    }


def search_candidates(
    embedding: list[float],
    limit: int = 1000,
) -> list[dict]:
    """
    Perform semantic search over
    candidate embeddings.

    Parameters
    ----------
    embedding : list[float]

    limit : int

    Returns
    -------
    list[dict]
    """

    client = get_qdrant_client()

    results = client.query_points(

        collection_name=QDRANT_COLLECTION,

        query=embedding,

        limit=limit,

        with_payload=True,

        with_vectors=False,

    )

    return [

        _format_result(
            point
        )

        for point in results.points

    ]