"""
Demo Qdrant.

Creates an in-memory Qdrant collection
using a small candidate sample.

This module is only used by the
Hugging Face demo.
"""

from qdrant_client import QdrantClient

from qdrant_client.models import (
    Distance,
    PointStruct,
    VectorParams,
)

from src.demo.utils import make_json_serializable

from src.demo.loader import (
    load_demo_candidates,
)


COLLECTION_NAME = "demo_candidates"

EMBEDDING_DIMENSION = 768


_client = None


def get_demo_client() -> QdrantClient:
    """
    Return singleton in-memory
    Qdrant client.
    """

    global _client

    if _client is None:

        _client = QdrantClient(
            ":memory:"
        )

        _build_collection(
            _client
        )

    return _client


def _build_collection(
    client: QdrantClient,
):
    """
    Build demo collection.
    """

    if client.collection_exists(
        COLLECTION_NAME
    ):
        return

    client.create_collection(

        collection_name=COLLECTION_NAME,

        vectors_config=VectorParams(

            size=EMBEDDING_DIMENSION,

            distance=Distance.COSINE,

        ),

    )

    dataframe = load_demo_candidates()

    points = []

    for _, row in dataframe.iterrows():

        payload = make_json_serializable(row.drop(
            "embedding"
        ).to_dict())

        points.append(

            PointStruct(

                id=len(points),

                vector=row[
                    "embedding"
                ],

                payload=payload,

            )

        )

    client.upsert(

        collection_name=COLLECTION_NAME,

        wait=True,

        points=points,

    )