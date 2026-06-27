"""
Benchmark embedding generation speed.
"""

import time
from pathlib import Path
import torch

from src.ingestion.jsonl_reader import read_jsonl
from src.text_builder.candidate_text_builder import (
    build_candidate_text,
)
from src.embeddings.embedding_generator import (
    generate_embedding,
    generate_embeddings,
)

INPUT_FILE = Path(
    "data/processed/clean_candidates.jsonl"
)


def benchmark_single():

    candidate = next(
        read_jsonl(INPUT_FILE)
    )

    text = build_candidate_text(
        candidate
    )

    print("=" * 60)
    print("Single Candidate")
    print("=" * 60)

    start = time.perf_counter()

    generate_embedding(text)

    elapsed = (
        time.perf_counter() - start
    )

    print(
        f"Inference : {elapsed:.4f} sec"
    )

    print()


def benchmark_batch(
    candidate_count,
):

    texts = []

    for i, candidate in enumerate(
        read_jsonl(INPUT_FILE)
    ):

        texts.append(
            build_candidate_text(
                candidate
            )
        )

        if (
            i + 1
            == candidate_count
        ):
            break

    internal_batch = (
        1024
        if torch.cuda.is_available()
        else 128
    )

    print("=" * 60)
    print(
        f"{candidate_count} Candidate Benchmark"
    )
    print("=" * 60)

    start = time.perf_counter()

    vectors = generate_embeddings(
        texts,
        batch_size=internal_batch,
    )

    elapsed = (
        time.perf_counter() - start
    )

    cps = (
        candidate_count
        / elapsed
    )

    estimate = (
        100000
        / cps
    )

    print(
        f"Vectors          : {len(vectors)}"
    )

    print(
        f"Internal Batch   : {internal_batch}"
    )

    print(
        f"Time             : {elapsed:.2f} sec"
    )

    print(
        f"Candidates / sec : {cps:.2f}"
    )

    print(
        f"Estimated 100K   : {estimate/60:.2f} min"
    )

    print()


def main():

    benchmark_single()

    benchmark_batch(1000)

    benchmark_batch(10000)


if __name__ == "__main__":
    main()