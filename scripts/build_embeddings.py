"""
Build embeddings for all candidates.
"""

from pathlib import Path
import json
import time
import torch

from src.ingestion.jsonl_reader import read_jsonl
from src.text_builder.candidate_text_builder import (
    build_candidate_text,
)
from src.embeddings.embedding_generator import (
    generate_embeddings,
)

INPUT_FILE = Path(
    "data/processed/clean_candidates.jsonl"
)

OUTPUT_FILE = Path(
    "data/processed/candidate_embeddings.jsonl"
)

# Automatically choose batch size
WRITE_BATCH_SIZE = (
    1024
    if torch.cuda.is_available()
    else 128
)


def main():

    batch_ids = []
    batch_texts = []

    total = 0

    start = time.perf_counter()

    print("=" * 60)

    if torch.cuda.is_available():

        print("Device : GPU")

    else:

        print("Device : CPU")

    print(
        f"Batch Size : {WRITE_BATCH_SIZE}"
    )

    print("=" * 60)

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8",
    ) as writer:

        for candidate in read_jsonl(INPUT_FILE):

            batch_ids.append(
                candidate["candidate_id"]
            )

            batch_texts.append(
                build_candidate_text(candidate)
            )

            if len(batch_texts) >= WRITE_BATCH_SIZE:

                vectors = generate_embeddings(
                    batch_texts,
                    batch_size=WRITE_BATCH_SIZE,
                )

                for cid, vector in zip(
                    batch_ids,
                    vectors,
                ):

                    writer.write(
                        json.dumps(
                            {
                                "candidate_id": cid,
                                "embedding": vector,
                            }
                        )
                        + "\n"
                    )

                total += len(batch_ids)

                print(
                    f"Processed : {total}"
                )

                batch_ids.clear()
                batch_texts.clear()

        if batch_texts:

            vectors = generate_embeddings(
                batch_texts,
                batch_size=WRITE_BATCH_SIZE,
            )

            for cid, vector in zip(
                batch_ids,
                vectors,
            ):

                writer.write(
                    json.dumps(
                        {
                            "candidate_id": cid,
                            "embedding": vector,
                        }
                    )
                    + "\n"
                )

            total += len(batch_ids)

    elapsed = (
        time.perf_counter()
        - start
    )

    print()

    print("=" * 60)

    print(
        f"Completed : {total}"
    )

    print(
        f"Time : {elapsed:.2f} sec"
    )

    print(
        f"Speed : {total/elapsed:.2f} candidates/sec"
    )

    print("=" * 60)


if __name__ == "__main__":

    main()