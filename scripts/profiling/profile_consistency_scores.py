from statistics import mean, median

from src.ingestion.jsonl_reader import (
    read_jsonl,
)

from features.consistency.consistency_engine import (
    build_consistency_features,
)

scores = []

print(
    "Scanning candidates..."
)

for candidate in read_jsonl(
    "data/processed/clean_candidates.jsonl"
):

    features = (
        build_consistency_features(
            candidate
        )
    )

    scores.append(
        features["consistency_score"]
    )

scores = sorted(scores)


def percentile(values, p):

    index = int(
        (len(values) - 1) * p
    )

    return values[index]


report = f"""
============================================================
CONSISTENCY SCORE DISTRIBUTION
============================================================

count     : {len(scores)}
min       : {min(scores)}
max       : {max(scores)}
avg       : {mean(scores):.2f}
median    : {median(scores):.2f}

p25       : {percentile(scores, 0.25)}
p50       : {percentile(scores, 0.50)}
p75       : {percentile(scores, 0.75)}
p90       : {percentile(scores, 0.90)}
"""

print(report)

with open(
    "data/reports/profiling/consistency_score_distribution.txt",
    "w",
    encoding="utf-8"
) as f:

    f.write(report)

print(
    "\nSaved: data/reports/profiling/consistency_score_distribution.txt"
)