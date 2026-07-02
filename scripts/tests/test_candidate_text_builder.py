from src.ingestion.jsonl_reader import (
    read_jsonl,
)

from src.text_builder.candidate_text_builder import (
    build_candidate_text,
)

candidate = next(
    read_jsonl(
        "data/processed/clean_candidates.jsonl"
    )
)

text = build_candidate_text(
    candidate
)

print(
    "\n===== CANDIDATE TEXT =====\n"
)

print(text)