from src.embeddings.embedding_generator import (
    generate_embedding,
    generate_embeddings,
)

text = """
Backend Engineer with Python,
SQL, Spark and AWS experience.
"""

vector = generate_embedding(text)

print(type(vector))
print()

print("Vector Length:", len(vector))
print()

print("First 10 Values:")
print(vector[:10])

print("\n" + "=" * 50)
print("BATCH TEST")
print("=" * 50)

vectors = generate_embeddings(
    [
        text,
        "Data Engineer with Airflow",
        "ML Engineer with PyTorch",
    ]
)

print(
    "Embeddings Generated:",
    len(vectors)
)

print(
    "Dimension:",
    len(vectors[0])
)