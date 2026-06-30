"""
Validate Qdrant collection.
"""

from src.config.settings import (
    QDRANT_COLLECTION,
)

from src.qdrant.client import (
    get_qdrant_client,
)


def validate_collection() -> None:

    client = get_qdrant_client()

    info = client.get_collection(
        collection_name=QDRANT_COLLECTION
    )

    data = info.model_dump()

    print()

    print("=" * 60)
    print("Collection Validation")
    print("=" * 60)

    print(f"Status              : {data['status']}")
    print(f"Points              : {data['points_count']}")
    print(f"Indexed Vectors     : {data['indexed_vectors_count']}")
    print(f"Segments            : {data['segments_count']}")
    print(f"Payload Schema      : {len(data['payload_schema'])}")

    print("=" * 60)