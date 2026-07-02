from pathlib import Path
import json

from src.ingestion.jsonl_reader import read_jsonl
from src.cleaning.candidate_cleaner import clean_candidate


INPUT_FILE = "data/raw/candidates.jsonl"

OUTPUT_FILE = (
    "data/processed/clean_candidates.jsonl"
)


def main():

    Path(
        "data/processed"
    ).mkdir(
        parents=True,
        exist_ok=True
    )

    total = 0

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as outfile:

        for candidate in read_jsonl(
            INPUT_FILE
        ):

            cleaned = clean_candidate(
                candidate
            )

            outfile.write(
                json.dumps(
                    cleaned,
                    ensure_ascii=False
                )
                + "\n"
            )

            total += 1

            if total % 10000 == 0:
                print(
                    f"Processed {total}"
                )

    print("\nCleaning Complete")
    print(
        f"Records Written : {total}"
    )
    print(
        f"Output File     : {OUTPUT_FILE}"
    )


if __name__ == "__main__":
    main()