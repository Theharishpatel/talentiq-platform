"""
Test Qdrant connection.
"""

from src.qdrant.client import (
    get_qdrant_client,
)

print("=" * 60)
print("Testing Qdrant Connection")
print("=" * 60)

client = get_qdrant_client()

collections = client.get_collections()

print()

print("Connected Successfully")

print()

print("Collections")

for collection in collections.collections:

    print("-", collection.name)

print()

print("=" * 60)