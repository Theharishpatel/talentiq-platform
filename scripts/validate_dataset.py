from collections import Counter

from src.ingestion.jsonl_reader import read_jsonl
from src.validation.validator import validate_candidate

error_counter = Counter()

total = 0
valid = 0
invalid = 0

for record in read_jsonl(
    "data/raw/candidates.jsonl"
):

    total += 1

    is_valid, result = validate_candidate(
        record
    )

    if is_valid:
        valid += 1

    else:
        invalid += 1

        # Count validation errors
        for err in result:

            field = ".".join(
                str(x)
                for x in err["loc"]
            )

            error_counter[field] += 1

print(f"Total   : {total}")
print(f"Valid   : {valid}")
print(f"Invalid : {invalid}")

print("\nTop Validation Errors:\n")

for field, count in error_counter.most_common(20):

    print(f"{field:<50} {count}")