from pprint import pprint

from src.ingestion.jsonl_reader import (
    read_jsonl,
)

from src.features.honeypot_features import (
    build_honeypot_features,
)

candidate = next(
    read_jsonl(
        "data/processed/clean_candidates.jsonl"
    )
)

result = (
    build_honeypot_features(
        candidate
    )
)

print(
    "\n===== HONEYPOT FEATURES =====\n"
)

pprint(result)