"""
Generate embeddings from candidate_text.jsonl and store them as candidate_embeddings.parquet.

Recommended usage:
    - Google Colab (GPU T4)
    - Offline preprocessing pipline

output:
candidate_embeddings.parquet

"""

import time

from embeddings.model import load_embedding_model

from embeddings.data_loader import (
    load_candidate_texts,
)

from embeddings.parquet_writer import (
    EmbeddingWriter,
)

from embeddings.generator import (
    generate_embeddings,
)

def main():

    start = time.time()

    model = load_embedding_model()

    records = load_candidate_texts()

    writer = EmbeddingWriter()

    generate_embeddings(
        
        model,

        records,

        writer,

    )

    writer.close()

    elapsed = time.time() - start

    print()

    print("=" * 60)

    print("Embedding generation completed")

    print("=" * 60)

    print(f"Candidates : {len(records)}")

    print(f"Time : {elapsed/60:.2f} minutes")

if __name__ == "__main__":

    main()