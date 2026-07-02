from statistics import mean
from collections import Counter

from src.ingestion.jsonl_reader import read_jsonl


title_counter = Counter()

job_counts = []
skill_counts = []

skill_durations = []

education_counts = []

for candidate in read_jsonl(
    "data/processed/clean_candidates.jsonl"
):

    # ------ Career History -----

    jobs = candidate.get(
        "career_history",
        []
    )

    job_counts.append(
        len(jobs)
    )

    for job in jobs:

        title = job.get(
            "title"
        )

        if title:
            title_counter[title] += 1

    # ----- Skills -----

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

    # ----- Education -----

    education = candidate.get(
        "education",
        []
    )

    education_counts.append(
        len(education)
    )


def percentile(values, p):

    values = sorted(values)

    index = int(
        (len(values) - 1) * p
    )

    return values[index]


report = ""

# ----- JOB COUNTS ----- 

report += f"""
============================================================
JOB COUNT
============================================================

count   : {len(job_counts)}
min     : {min(job_counts)}
max     : {max(job_counts)}
avg     : {mean(job_counts):.2f}

p25     : {percentile(job_counts, 0.25)}
p50     : {percentile(job_counts, 0.50)}
p75     : {percentile(job_counts, 0.75)}
p90     : {percentile(job_counts, 0.90)}
"""

# ----- SKILL COUNTS -----

report += f"""

============================================================
SKILL COUNT
============================================================

count   : {len(skill_counts)}
min     : {min(skill_counts)}
max     : {max(skill_counts)}
avg     : {mean(skill_counts):.2f}

p25     : {percentile(skill_counts, 0.25)}
p50     : {percentile(skill_counts, 0.50)}
p75     : {percentile(skill_counts, 0.75)}
p90     : {percentile(skill_counts, 0.90)}
"""

# ---- SKILL DURATION ----- 

report += f"""

============================================================
SKILL DURATION
============================================================

count   : {len(skill_durations)}
min     : {min(skill_durations)}
max     : {max(skill_durations)}
avg     : {mean(skill_durations):.2f}

p25     : {percentile(skill_durations, 0.25)}
p50     : {percentile(skill_durations, 0.50)}
p75     : {percentile(skill_durations, 0.75)}
p90     : {percentile(skill_durations, 0.90)}
"""

# ------ EDUCATION COUNT ----

report += f"""

============================================================
EDUCATION COUNT
============================================================

count   : {len(education_counts)}
min     : {min(education_counts)}
max     : {max(education_counts)}
avg     : {mean(education_counts):.2f}

p25     : {percentile(education_counts, 0.25)}
p50     : {percentile(education_counts, 0.50)}
p75     : {percentile(education_counts, 0.75)}
p90     : {percentile(education_counts, 0.90)}
"""

# ----- TOP TITLES -----

report += """

============================================================
TOP TITLES
============================================================
"""

for title, count in title_counter.most_common(30):

    report += (
        f"\n{title:<35} {count}"
    )

print(report)

with open(
    "data/reports/profiling/growth_metrics_profile.txt",
    "w",
    encoding="utf-8"
) as f:

    f.write(report)

print(
    "\n\nSaved: data/reports/profiling/growth_metrics_profile.txt"
)