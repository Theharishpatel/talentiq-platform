from statistics import mean, median

from src.ingestion.jsonl_reader import read_jsonl


years_exp = []
job_counts = []
job_durations = []

skill_counts = []
skill_durations = []


def percentile(values, p):
    """
    Simple percentile calculation.
    """

    if not values:
        return 0

    values = sorted(values)

    index = int(
        (len(values) - 1) * p
    )

    return values[index]


for candidate in read_jsonl(
    "data/raw/candidates.jsonl"
):

    # ------------------
    # Years Experience
    # ------------------

    profile = candidate.get(
        "profile",
        {}
    )

    exp = profile.get(
        "years_of_experience"
    )

    if exp is not None:
        years_exp.append(exp)

    # ------------------
    # Career History
    # ------------------

    jobs = candidate.get(
        "career_history",
        []
    )

    job_counts.append(
        len(jobs)
    )

    for job in jobs:

        duration = job.get(
            "duration_months"
        )

        if duration is not None:
            job_durations.append(
                duration
            )

    # ------------------
    # Skills
    # ------------------

    skills = candidate.get(
        "skills",
        []
    )

    skill_counts.append(
        len(skills)
    )

    for skill in skills:

        duration = skill.get(
            "duration_months"
        )

        if duration is not None:
            skill_durations.append(
                duration
            )


def print_stats(
    name,
    values
):

    print("\n" + "=" * 60)
    print(name)
    print("=" * 60)

    print(
        f"count     : {len(values)}"
    )

    print(
        f"min       : {min(values)}"
    )

    print(
        f"max       : {max(values)}"
    )

    print(
        f"avg       : {mean(values):.2f}"
    )

    print(
        f"median    : {median(values):.2f}"
    )

    print(
        f"p25       : {percentile(values, 0.25)}"
    )

    print(
        f"p50       : {percentile(values, 0.50)}"
    )

    print(
        f"p75       : {percentile(values, 0.75)}"
    )

    print(
        f"p90       : {percentile(values, 0.90)}"
    )


print_stats(
    "YEARS EXPERIENCE",
    years_exp
)

print_stats(
    "JOB COUNT",
    job_counts
)

print_stats(
    "JOB DURATIONS",
    job_durations
)

print_stats(
    "SKILL COUNT",
    skill_counts
)

print_stats(
    "SKILL DURATIONS",
    skill_durations
)

report = []

def add_stats(name, values):

    report.append("\n" + "=" * 60)
    report.append(name)
    report.append("=" * 60)

    report.append(f"count     : {len(values)}")
    report.append(f"min       : {min(values)}")
    report.append(f"max       : {max(values)}")
    report.append(f"avg       : {mean(values):.2f}")
    report.append(f"median    : {median(values):.2f}")
    report.append(f"p25       : {percentile(values, 0.25)}")
    report.append(f"p50       : {percentile(values, 0.50)}")
    report.append(f"p75       : {percentile(values, 0.75)}")
    report.append(f"p90       : {percentile(values, 0.90)}")


add_stats("YEARS EXPERIENCE", years_exp)
add_stats("JOB COUNT", job_counts)
add_stats("JOB DURATIONS", job_durations)
add_stats("SKILL COUNT", skill_counts)
add_stats("SKILL DURATIONS", skill_durations)

report_text = "\n".join(report)

with open(
    "data/reports/profiling/experience_metrics_profile.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write(report_text)

print(
    "\nSaved: data/reports/profiling/experience_metrics_profile.txt"
)