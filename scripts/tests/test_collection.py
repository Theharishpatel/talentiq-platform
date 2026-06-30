"""
Test Qdrant collection.
"""

from src.qdrant.collection import (
    create_collection,
    collection_exists,
    get_collection_info,
)

print("=" * 60)
print("Testing Collection")
print("=" * 60)

create_collection()

print()

print(
    "Exists :",
    collection_exists(),
)

print()

info = get_collection_info()

print(info)

print()

print("=" * 60)