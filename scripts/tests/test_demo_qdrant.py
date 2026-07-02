from src.demo.qdrant import (
    get_demo_client,
    COLLECTION_NAME,
)


client = get_demo_client()

info = client.get_collection(
    COLLECTION_NAME
)

print()

print("=" * 60)

print("Demo Collection")

print("=" * 60)

print()

print(info)

print()

print(

    "Points :",

    info.points_count,

)
