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

print("\n===== BEFORE =====\n")

pprint(record["profile"])

print(
    "\nGitHub:",
    record["redrob_signals"]
    .get("github_activity_score")
)

print(
    "Offer:",
    record["redrob_signals"]
    .get("offer_acceptance_rate")
)

cleaned = clean_candidate(
    record
)

print("\n===== AFTER =====\n")

pprint(cleaned["profile"])

print(
    "\nGitHub:",
    cleaned["redrob_signals"]
    .get("github_activity_score")
)

print(
    "Offer:",
    cleaned["redrob_signals"]
    .get("offer_acceptance_rate")
)