"""
Semantic search over the local
demo Qdrant collection.

This module mirrors
src/retrieval/search.py
but uses the in-memory
Qdrant instance.
"""

from typing import Any

from qdrant_client.models import (
    ScoredPoint,
)

from src.demo.qdrant import (
    COLLECTION_NAME,
    get_demo_client,
)


def _format_result(
    point: ScoredPoint,
) -> dict[str, Any]:
    """
    Convert a Qdrant ScoredPoint
    into the project-specific
    candidate format.
    """

    return {

        "candidate_id":
            point.payload.get(
                "candidate_id"
            ),

        "similarity_score":
            round(
                float(
                    point.score
                ),
                6,
            ),

        "payload":
            point.payload,

    }


def search_candidates(
    embedding: list[float],
    limit: int = 100,
) -> list[dict]:
    """
    Perform semantic search over
    the demo candidate collection.

    Parameters
    ----------
    embedding : list[float]

    limit : int

    Returns
    -------
    list[dict]
    """

    client = get_demo_client()

    results = client.query_points(

        collection_name=COLLECTION_NAME,

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