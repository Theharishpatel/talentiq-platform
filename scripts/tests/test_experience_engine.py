from pprint import pprint

from src.ingestion.jsonl_reader import (
    read_jsonl,
)

from src.features.experience_engine import (
    build_experience_features,
)

candidate = next(
    read_jsonl(
        "data/processed/clean_candidates.jsonl"
    )
)

features = (
    build_experience_features(
        candidate
    )
)

print("\n ======= EXPERIENCE ENGINE ==== \n")

pprint(features)
      