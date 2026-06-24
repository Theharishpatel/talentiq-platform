from pprint import pprint

from src.ingestion.jsonl_reader import (
    read_jsonl,
)

from src.features.behavior_engine import (
    build_behavior_features,
)

candidate = next(
    read_jsonl(
        "data/processed/clean_candidates.jsonl"
    )
)

result = build_behavior_features(
    candidate
)

print(
    "\n===== BEHAVIOR ENGINE =====\n"
)

pprint(result)