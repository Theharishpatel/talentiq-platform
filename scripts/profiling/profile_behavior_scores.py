from statistics import median

from src.ingestion.jsonl_reader import (
    read_jsonl,
)

from src.features.behavior_engine import (
    build_behavior_features,
)

scores = []

print("Scanning candidates...")

for candidate in read_jsonl(
    "data/processed/clean_candidates.jsonl"
):

    features = (
        build_behavior_features(
            candidate
        )
    )

    scores.append(
        features["behavior_score"]
    )

scores.sort()

count = len(scores)

p25 = scores[int(count * 0.25)]
p50 = scores[int(count * 0.50)]
p75 = scores[int(count * 0.75)]
p90 = scores[int(count * 0.90)]

report = f"""
============================================================
BEHAVIOR SCORE DISTRIBUTION
============================================================

count     : {count}
min       : {min(scores)}
max       : {max(scores)}
avg       : {sum(scores)/count:.2f}
median    : {median(scores):.2f}

p25       : {p25}
p50       : {p50}
p75       : {p75}
p90       : {p90}
"""

print(report)

with open(
    "data/reports/profiling/behavior_score_distribution.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write(report)

print(
    "\nSaved: data/reports/profiling/"
    "behavior_score_distribution.txt"
)