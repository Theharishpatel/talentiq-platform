from collections import Counter
from io import StringIO
import sys

from src.ingestion.jsonl_reader import read_jsonl

buffer = StringIO()
old_stdout = sys.stdout
sys.stdout = buffer

company_counter = Counter()
title_counter = Counter()

total_jobs = 0
current_jobs = 0

missing_company = 0
missing_title = 0

negative_duration = 0

durations = []

for candidate in read_jsonl(
    "data/raw/candidates.jsonl"
):

    for job in candidate.get(
        "career_history",
        []
    ):

        total_jobs += 1

        company = job.get(
            "company",
            ""
        )

        title = job.get(
            "title",
            ""
        )

        duration = job.get(
            "duration_months"
        )

        if not company:
            missing_company += 1
        else:
            company_counter[company] += 1

        if not title:
            missing_title += 1
        else:
            title_counter[title] += 1

        if job.get("is_current"):
            current_jobs += 1

        if duration is not None:

            durations.append(duration)

            if duration < 0:
                negative_duration += 1

print("\n" + "=" * 60)
print("CAREER PROFILE")
print("=" * 60)

print(f"\nTotal Jobs             : {total_jobs}")
print(f"Current Jobs           : {current_jobs}")

print(f"Missing Company        : {missing_company}")
print(f"Missing Title          : {missing_title}")

print(f"Negative Durations     : {negative_duration}")

if durations:

    print(
        f"\nDuration Min           : "
        f"{min(durations)}"
    )

    print(
        f"Duration Max           : "
        f"{max(durations)}"
    )

    print(
        f"Duration Avg           : "
        f"{sum(durations)/len(durations):.2f}"
    )

print("\n" + "=" * 60)
print("TOP COMPANIES")
print("=" * 60)

for company, count in company_counter.most_common(20):
    print(f"{company:<35} {count}")

print("\n" + "=" * 60)
print("TOP TITLES")
print("=" * 60)

for title, count in title_counter.most_common(20):
    print(f"{title:<35} {count}")

sys.stdout = old_stdout

report = buffer.getvalue()

print(report)

with open(
    "data/reports/profiling/career_profile.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write(report)