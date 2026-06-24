from pprint import pprint

from src.ingestion.jsonl_reader import (
    read_jsonl,
)

from src.features.recruitability_engine import (
    build_recruitability_features,
)

candidate = next(
    read_jsonl(
        "data/processed/clean_candidates.jsonl"
    )
)

result = (
    build_recruitability_features(
        candidate
    )
)

print(
    "\n===== RECRUITABILITY ENGINE =====\n"
)

pprint(result)