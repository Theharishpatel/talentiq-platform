"""
Build candidate text dataset.

Reads:
    data/processed/clean_candidates.jsonl

Writes:
    data/processed/candidate_text.jsonl
"""

import json
import time
from pathlib import Path

from src.ingestion.jsonl_reader import (
    read_jsonl,
)

from src.text_builder.candidate_text_builder import (
    build_candidate_text,
)

INPUT_FILE = Path(
    "data/processed/clean_candidates.jsonl"
)

OUTPUT_FILE = Path(
    "data/processed/candidate_text.jsonl"
)

LOG_INTERVAL = 1000


def main():

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    total = 0

    start_time = time.time()

    with OUTPUT_FILE.open(
        "w",
        encoding="utf-8",
    ) as writer:

        for candidate in read_jsonl(INPUT_FILE):

            record = {

                "candidate_id": candidate.get(
                    "candidate_id",
                    "",
                ),

                "text": build_candidate_text(
                    candidate
                ),

            }

            writer.write(
                json.dumps(
                    record,
                    ensure_ascii=False,
                )
            )

            writer.write("\n")

            total += 1

            if total % LOG_INTERVAL == 0:

                elapsed = (
                    time.time() - start_time
                )

                rate = (
                    total / elapsed
                )

                print(
                    f"Processed: {total:,} | "
                    f"{rate:.2f} candidates/sec"
                )

    elapsed = (
        time.time() - start_time
    )

    print()

    print("=" * 60)
    print("Candidate Text Dataset Created Successfully")
    print("=" * 60)
    print(f"Output File : {OUTPUT_FILE}")
    print(f"Candidates  : {total:,}")
    print(f"Time Taken  : {elapsed:.2f} sec")
    print(
        f"Speed       : {total/elapsed:.2f} candidates/sec"
    )


if __name__ == "__main__":
    main()