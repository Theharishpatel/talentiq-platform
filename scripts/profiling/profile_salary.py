from src.ingestion.jsonl_reader import read_jsonl

mins = []
maxs = []

for candidate in read_jsonl(
    "data/raw/candidates.jsonl"
):
    salary = candidate.get(
        "redrob_signals",
        {}
    ).get(
        "expected_salary_range_inr_lpa",
        {}
    )

    mins.append(
        salary.get("min", 0)
    )

    maxs.append(
        salary.get("max", 0)
    )

print(
    "Min Salary:",
    min(mins),
    max(mins)
)

print(
    "Max Salary:",
    min(maxs),
    max(maxs)
)