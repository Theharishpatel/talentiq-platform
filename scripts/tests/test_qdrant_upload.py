"""
Verify uploaded vectors.
"""

from src.config.settings import (
    QDRANT_COLLECTION,
)

from src.qdrant.client import (
    get_qdrant_client,
)

client = get_qdrant_client()

info = client.get_collection(
    collection_name=QDRANT_COLLECTION
)

print("=" * 60)
print("Collection Statistics")
print("=" * 60)

print(info)