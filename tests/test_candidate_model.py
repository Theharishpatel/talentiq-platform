import json

from src.models.candidate import Candidate


with open(
    "data/raw/candidates.jsonl",
    "r",
    encoding="utf-8"
) as f:

    first_line = f.readline()

candidate_json = json.loads(first_line)

candidate = Candidate.model_validate(
    candidate_json
)

print(candidate.candidate_id)

print("Validation Successful")