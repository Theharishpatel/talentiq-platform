from collections import Counter

from src.ingestion.jsonl_reader import (
    read_jsonl,
)

from src.features.honeypot_features import (
    build_honeypot_features,
)

risk_scores = []

risk_levels = Counter()

salary_anomaly_count = 0
skill_stuffing_count = 0
experience_mismatch_count = 0
job_hopper_count = 0
inactive_profile_count = 0

print(
    "Scanning candidates..."
)

for candidate in read_jsonl(
    "data/processed/clean_candidates.jsonl"
):

    features = (
        build_honeypot_features(
            candidate
        )
    )

    risk_scores.append(
        features["risk_score"]
    )

    risk_levels[
        features["risk_level"]
    ] += 1

    if features["salary_anomaly"]:
        salary_anomaly_count += 1

    if features["skill_stuffing"]:
        skill_stuffing_count += 1

    if features["experience_mismatch"]:
        experience_mismatch_count += 1

    if features["job_hopper"]:
        job_hopper_count += 1

    if features["inactive_profile"]:
        inactive_profile_count += 1


report = f"""
============================================================
HONEYPOT FEATURE DISTRIBUTION
============================================================

Candidates              : {len(risk_scores)}

LOW RISK                : {risk_levels['LOW']}
MEDIUM RISK             : {risk_levels['MEDIUM']}
HIGH RISK               : {risk_levels['HIGH']}

============================================================
TRIGGER COUNTS
============================================================

Salary Anomaly          : {salary_anomaly_count}
Skill Stuffing          : {skill_stuffing_count}
Experience Mismatch     : {experience_mismatch_count}
Job Hopper              : {job_hopper_count}
Inactive Profile        : {inactive_profile_count}

============================================================
RISK SCORE
============================================================

Min                     : {min(risk_scores)}
Max                     : {max(risk_scores)}
Avg                     : {sum(risk_scores)/len(risk_scores):.2f}
"""

print(report)

with open(
    "data/reports/profiling/honeypot_distribution.txt",
    "w",
    encoding="utf-8"
) as f:

    f.write(report)

print(
    "\nSaved: data/reports/profiling/honeypot_distribution.txt"
)
