"""
Test candidate retrieval filters.

Usage
-----
python -m scripts.tests.test_filters
"""

import pandas as pd

from src.config.settings import (
    CANDIDATE_INDEX_FILE,
)

from src.retrieval.search import (
    search_candidates,
)

from src.retrieval.filters import (
    filter_candidates,
)


# ==========================================================
# LOAD MOCK EMBEDDING
# ==========================================================

print()

print("=" * 60)
print("Loading Candidate Index")
print("=" * 60)

df = pd.read_parquet(
    CANDIDATE_INDEX_FILE
)

candidate = df.iloc[0]

embedding = candidate[
    "embedding"
]

print(
    f"Candidate : {candidate['candidate_id']}"
)

print(
    f"Embedding Dimension : {len(embedding)}"
)

print()


# ==========================================================
# SEARCH
# ==========================================================

print("=" * 60)
print("Semantic Search")
print("=" * 60)

retrieved = search_candidates(

    embedding=embedding,

    limit=300,

)

print(
    f"Retrieved Candidates : {len(retrieved)}"
)

print()


# ==========================================================
# FILTER
# ==========================================================

print("=" * 60)
print("Applying Filters")
print("=" * 60)

filtered = filter_candidates(

    candidates=retrieved,

    min_experience=5,

    max_risk_score=80,

    require_open_to_work=False,

    min_recruitability=0,

    min_consistency=0,

)

print(
    f"Remaining Candidates : {len(filtered)}"
)

print(
    f"Removed Candidates : {len(retrieved)-len(filtered)}"
)

print()


# ==========================================================
# SAMPLE RESULTS
# ==========================================================

print("=" * 60)
print("Top 10 Filtered Candidates")
print("=" * 60)

for idx, candidate in enumerate(

    filtered[:10],

    start=1,

):

    payload = candidate[
        "payload"
    ]

    print()

    print(
        f"Rank #{idx}"
    )

    print(
        f"Candidate : {candidate['candidate_id']}"
    )

    print(
        f"Similarity : {candidate['similarity_score']:.4f}"
    )

    print(
        f"Experience : {payload.get('years_experience')}"
    )

    print(
        f"Risk Score : {payload.get('risk_score')}"
    )

    print(
        f"Recruitability : {payload.get('recruitability_score')}"
    )

    print(
        f"Consistency : {payload.get('consistency_score')}"
    )


# ==========================================================
# VALIDATION
# ==========================================================

print()

print("=" * 60)
print("Validation")
print("=" * 60)

valid = True

for candidate in filtered:

    payload = candidate[
        "payload"
    ]

    if payload.get(
        "years_experience",
        0,
    ) < 5:

        valid = False

        break

    if payload.get(
        "risk_score",
        0,
    ) > 80:

        valid = False

        break

print(
    f"All Candidates Valid : {valid}"
)

print(
    f"Filtered Candidates : {len(filtered)}"
)

print()

print("=" * 60)

if valid:

    print(
        "Filter Test : PASSED"
    )

else:

    print(
        "Filter Test : FAILED"
    )

print("=" * 60)