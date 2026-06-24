from collections import Counter
from io import StringIO
import sys

from src.ingestion.jsonl_reader import read_jsonl

buffer = StringIO()
old_stdout = sys.stdout
sys.stdout = buffer

degree_counter = Counter()
tier_counter = Counter()
field_counter = Counter()
institution_counter = Counter()

total_records = 0

missing_degree = 0
missing_field = 0
missing_institution = 0
missing_tier = 0

invalid_years = 0

for candidate in read_jsonl(
    "data/raw/candidates.jsonl"
):

    for edu in candidate.get(
        "education",
        []
    ):

        total_records += 1

        degree = edu.get("degree")
        field = edu.get("field_of_study")
        institution = edu.get("institution")
        tier = edu.get("tier")

        start_year = edu.get("start_year")
        end_year = edu.get("end_year")

        if not degree:
            missing_degree += 1
        else:
            degree_counter[degree] += 1

        if not field:
            missing_field += 1
        else:
            field_counter[field] += 1

        if not institution:
            missing_institution += 1
        else:
            institution_counter[institution] += 1

        if not tier:
            missing_tier += 1
        else:
            tier_counter[tier] += 1

        if (
            start_year
            and end_year
            and start_year > end_year
        ):
            invalid_years += 1


print("\n" + "=" * 60)
print("EDUCATION PROFILE")
print("=" * 60)

print(f"\nTotal Education Records : {total_records}")

print(f"Missing Degree          : {missing_degree}")
print(f"Missing Field           : {missing_field}")
print(f"Missing Institution     : {missing_institution}")
print(f"Missing Tier            : {missing_tier}")

print(f"Invalid Years           : {invalid_years}")

print("\n" + "=" * 60)
print("DEGREES")
print("=" * 60)

for degree, count in degree_counter.most_common():
    print(f"{degree:<20} {count}")

print("\n" + "=" * 60)
print("TIERS")
print("=" * 60)

for tier, count in tier_counter.most_common():
    print(f"{tier:<20} {count}")

print("\n" + "=" * 60)
print("TOP FIELDS")
print("=" * 60)

for field, count in field_counter.most_common(20):
    print(f"{field:<35} {count}")

print("\n" + "=" * 60)
print("TOP INSTITUTIONS")
print("=" * 60)

for institution, count in institution_counter.most_common(20):
    print(f"{institution:<45} {count}")

sys.stdout = old_stdout

report = buffer.getvalue()

print(report)

with open(
    "data/reports/profiling/education_profile.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write(report)