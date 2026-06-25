import random

from src.ingestion.jsonl_reader import read_jsonl
from src.text_builder.candidate_text_builder import build_candidate_text

candidates = list(
    read_jsonl(
        "data/processed/clean_candidates.jsonl"
    )
)

samples = random.sample(
    candidates,
    5,
)

for idx, candidate in enumerate(samples):

    print(
        f"\n{'=' * 80}"
    )

    print(
        f"SAMPLE {idx + 1}"
    )

    print(
        '=' * 80
    )

    print(
        build_candidate_text(
            candidate
        )
    )

with open(
    "data/reports/candidate_text_samples.txt",
    "w",
    encoding="utf-8",
) as f:

    for candidate in samples:
        f.write(
            build_candidate_text(candidate)
        )
        f.write("\n\n")