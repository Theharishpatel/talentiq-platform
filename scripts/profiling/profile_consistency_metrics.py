from statistics import mean, median

from src.ingestion.jsonl_reader import (
    read_jsonl,
)

career_gap_ratios = []

job_duration_variances = []

profile_completeness_scores = []

filled_sections_counts = []

for candidate in read_jsonl(
    "data/processed/clean_candidates.jsonl"
):

    profile = candidate.get(
        "profile",
        {}
    )

    jobs = candidate.get(
        "career_history",
        []
    )

    skills = candidate.get(
        "skills",
        []
    )

    education = candidate.get(
        "education",
        []
    )

    # ------  profile completness  -----

    filled = 0

    if profile.get("headline"):
        filled += 1

    if profile.get("summary"):
        filled += 1

    if jobs:
        filled += 1

    if skills:
        filled += 1

    if education:
        filled += 1

    filled_sections_counts.append(
        filled
    )

    profile_completeness_scores.append(
        (filled / 5) * 100
    )

    # ----- experience consistency ----- 

    years_exp = profile.get(
        "years_of_experience",
        0
    )

    total_months = 0

    durations = []

    for job in jobs:

        duration = job.get(
            "duration_months"
        )

        if duration is None:
            continue

        total_months += duration

        durations.append(
            duration
        )

    career_years = (
        total_months / 12
    )

    if years_exp > 0:

        ratio = (
            career_years /
            years_exp
        )

        career_gap_ratios.append(
            ratio
        )

    # ---- job duration variance  ---- 

    if len(durations) > 1:

        variance = (
            max(durations)
            - min(durations)
        )

        job_duration_variances.append(
            variance
        )


def percentile(values, p):

    values = sorted(values)

    index = int(
        (len(values) - 1) * p
    )

    return values[index]


report = f"""
============================================================
PROFILE COMPLETENESS
============================================================

count   : {len(profile_completeness_scores)}
min     : {min(profile_completeness_scores)}
max     : {max(profile_completeness_scores)}
avg     : {mean(profile_completeness_scores):.2f}
median  : {median(profile_completeness_scores):.2f}

p25     : {percentile(profile_completeness_scores, 0.25)}
p50     : {percentile(profile_completeness_scores, 0.50)}
p75     : {percentile(profile_completeness_scores, 0.75)}
p90     : {percentile(profile_completeness_scores, 0.90)}
"""

report += f"""

============================================================
FILLED SECTIONS
============================================================

count   : {len(filled_sections_counts)}
min     : {min(filled_sections_counts)}
max     : {max(filled_sections_counts)}
avg     : {mean(filled_sections_counts):.2f}
median  : {median(filled_sections_counts):.2f}

p25     : {percentile(filled_sections_counts, 0.25)}
p50     : {percentile(filled_sections_counts, 0.50)}
p75     : {percentile(filled_sections_counts, 0.75)}
p90     : {percentile(filled_sections_counts, 0.90)}
"""

report += f"""

============================================================
CAREER YEARS / PROFILE YEARS RATIO
============================================================

count   : {len(career_gap_ratios)}
min     : {min(career_gap_ratios):.2f}
max     : {max(career_gap_ratios):.2f}
avg     : {mean(career_gap_ratios):.2f}
median  : {median(career_gap_ratios):.2f}

p25     : {percentile(career_gap_ratios, 0.25):.2f}
p50     : {percentile(career_gap_ratios, 0.50):.2f}
p75     : {percentile(career_gap_ratios, 0.75):.2f}
p90     : {percentile(career_gap_ratios, 0.90):.2f}
"""

report += f"""

============================================================
JOB DURATION VARIANCE
============================================================

count   : {len(job_duration_variances)}
min     : {min(job_duration_variances)}
max     : {max(job_duration_variances)}
avg     : {mean(job_duration_variances):.2f}
median  : {median(job_duration_variances):.2f}

p25     : {percentile(job_duration_variances, 0.25)}
p50     : {percentile(job_duration_variances, 0.50)}
p75     : {percentile(job_duration_variances, 0.75)}
p90     : {percentile(job_duration_variances, 0.90)}
"""

print(report)

with open(
    "data/reports/profiling/consistency_metrics_profile.txt",
    "w",
    encoding="utf-8"
) as f:

    f.write(report)

print(
    "\nSaved: data/reports/profiling/consistency_metrics_profile.txt"
)