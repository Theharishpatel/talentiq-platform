from pprint import pprint

from src.ingestion.jsonl_reader import read_jsonl

from src.cleaning.candidate_cleaner import (
    clean_candidate,
)

record = next(
    read_jsonl(
        "data/raw/candidates.jsonl"
    )
)
print("\n===== before =====\n")
pprint(record["skills"][:5])

cleaned = clean_candidate(record)

print(
    "\n===== after =====\n"
)
pprint(cleaned["skills"][:5])