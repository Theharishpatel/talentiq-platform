"""
Qdrant collection management.
"""

from qdrant_client.http.models import (
    VectorParams,
    Distance,
)

from src.config.settings import (
    QDRANT_COLLECTION,
    QDRANT_VECTOR_SIZE,
)

from src.qdrant.client import (
    get_qdrant_client,
)


def collection_exists() -> bool:
    """
    Check if collection exists.
    """

    client = get_qdrant_client()

    collections = client.get_collections()

    names = {

        collection.name

        for collection in collections.collections

    }

    return QDRANT_COLLECTION in names


def create_collection() -> None:
    """
    Create collection if it does not exist.
    """

    client = get_qdrant_client()

    if collection_exists():

        print(
            f"Collection '{QDRANT_COLLECTION}' already exists."
        )

        return

    client.create_collection(

        collection_name=QDRANT_COLLECTION,

        vectors_config=VectorParams(

            size=QDRANT_VECTOR_SIZE,

            distance=Distance.COSINE,

        ),

    )

    print(
        f"Collection '{QDRANT_COLLECTION}' created."
    )


def delete_collection() -> None:
    """
    Delete collection.
    """

    client = get_qdrant_client()

    if not collection_exists():

        print(
            f"Collection '{QDRANT_COLLECTION}' does not exist."
        )

        return

    client.delete_collection(
        collection_name=QDRANT_COLLECTION
    )

    print(
        f"Collection '{QDRANT_COLLECTION}' deleted."
    )


def get_collection_info():
    """
    Return collection metadata.
    """

    client = get_qdrant_client()

    return client.get_collection(
        collection_name=QDRANT_COLLECTION
    )