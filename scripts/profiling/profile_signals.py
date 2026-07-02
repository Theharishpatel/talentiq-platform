from collections import Counter
from datetime import date

from io import StringIO
import sys

from src.ingestion.jsonl_reader import read_jsonl

buffer = StringIO()
old_stdout = sys.stdout
sys.stdout = buffer
numeric_signals = [
    "profile_completeness_score",
    "profile_views_received_30d",
    "applications_submitted_30d",
    "recruiter_response_rate",
    "avg_response_time_hours",
    "connection_count",
    "endorsements_received",
    "notice_period_days",
    "github_activity_score",
    "search_appearance_30d",
    "saved_by_recruiters_30d",
    "interview_completion_rate",
    "offer_acceptance_rate",
]

boolean_signals = [
    "open_to_work_flag",
    "willing_to_relocate",
    "verified_email",
    "verified_phone",
    "linkedin_connected",
]

enum_signals = [
    "preferred_work_mode",
]

date_signals = [
    "signup_date",
    "last_active_date",
]

numeric_stats = {
    field: []
    for field in numeric_signals
}

boolean_stats = {
    field: Counter()
    for field in boolean_signals
}

enum_stats = {
    field: Counter()
    for field in enum_signals
}

date_stats = {
    field: []
    for field in date_signals
}

assessment_counter = Counter()
assessment_scores = []

for candidate in read_jsonl(
    "data/raw/candidates.jsonl"
):
    
    signals = candidate.get(
        "redrob_signals",
        {}
    )

    #---- numeric ------
    for field in numeric_signals:
        value = signals.get(field)

        if isinstance(
            value,
            (int, float)
        ):
            numeric_stats[field].append(
                value
            )

    # ------ boolean -----
    for field in boolean_signals:

        value = signals.get(field)

        boolean_stats[field][value] += 1

    #---- enum ------
    for field in enum_signals:

        value = signals.get(field)

        enum_stats[field][value] += 1

    # ------ date -----
    for field in date_signals:

        value = signals.get(field)

        if value:
            date_stats[field].append(
                value
            )

    # ---- assessments ----

    assessments = signals.get(
        "skill_assessment_scores",
        {}
    )

    for skill, score in assessments.items():

        assessment_counter[skill] += 1

        if isinstance(
            score,
            (int, float)
        ):
            assessment_scores.append(
                score
            )

print("\n")
print("=" * 60)
print("NUMERIC SIGNALS")
print("=" * 60)

for field, values in numeric_stats.items():

    if not values:
        continue

    avg = sum(values) / len(values)

    print(f"\n{field}")
    print(f"count      : {len(values)}")
    print(f"min      : {min(values)}")
    print(f"max      : {max(values)}")
    print(f"avg      : {avg:.2f}")
    print(f"-1 count      : {values.count(-1)}")

print("\n")
print("=" * 60)
print("BOOLEAN SIGNALS")
print("=" * 60)

for field, counts in boolean_stats.items():

    print(f"\n{field}")

    for value, count in counts.items():

        print(
            f"{value} : {count}"
        )

print("\n")
print("=" * 60)
print("ENUM SIGNALS")
print("=" * 60)


for field, counts in enum_stats.items():

    print(f"\n{field}")

    for value, count in counts.items():

        print(
            f"{value} : {count}"
        )

print("\n")
print("=" * 60)
print("DATE SIGNALS")
print("=" * 60)

for field, values in date_stats.items():

    if not values:
        continue

    print(f"{field}")
    print(f"earliest : {min(values)}")
    print(f"latest : {max(values)}")

print("\n")
print("=" * 60)
print("SKILL ASSESSMENTS")
print("=" * 60)

print("\nTop Assessed Skills:\n")

for skill, count in assessment_counter.most_common(20):

    print(
        f"{skill:<35} {count}"
    )

if assessment_scores:

    print("\nAssessment Score Range")

    print(
        f"min : {min(assessment_scores)}"
    )

    print(
        f"max : {max(assessment_scores)}"
    )

    avg = (
        sum(assessment_scores) / len(assessment_scores)
    )

    print(
        f"avg : {avg:.2f}"
    )

sys.stdout = old_stdout

report = buffer.getvalue()

print(report)

with open(
    "data/reports/profiling/signals_profile.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write(report)

