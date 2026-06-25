from pprint import pprint

from src.ingestion.jsonl_reader import (
    read_jsonl,
)

from src.features.consistency_engine import (
    build_consistency_features,
)

candidate = next(
    read_jsonl(
        "data/processed/clean_candidates.jsonl"
    )
)

result = (
    build_consistency_features(
        candidate
    )
)

print(
    "\n===== CONSISTENCY ENGINE =====\n"
)

pprint(result)