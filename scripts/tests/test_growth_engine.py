from pprint import pprint

from src.ingestion.jsonl_reader import (
    read_jsonl,
)

from src.features.growth_engine import (
    build_growth_features,
)

candidate = next(
    read_jsonl(
        "data/processed/clean_candidates.jsonl"
    )
)

result = (
    build_growth_features(
        candidate
    )
)

print(
    "\n===== GROWTH ENGINE =====\n"
)

pprint(result)