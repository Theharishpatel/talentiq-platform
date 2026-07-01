"""
Test ranking engine.

Usage
-----
python -m scripts.tests.test_ranking
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

from src.ranking.engine import (
    rank_candidates,
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

retrieved = search_candidates(

    embedding=embedding,

    limit=300,

)

print("=" * 60)
print("Semantic Search")
print("=" * 60)

print(
    f"Retrieved Candidates : {len(retrieved)}"
)

print()


# ==========================================================
# FILTER
# ==========================================================

filtered = filter_candidates(

    candidates=retrieved,

    min_experience=5,

    max_risk_score=80,

)

print("=" * 60)
print("Filtering")
print("=" * 60)

print(
    f"Remaining Candidates : {len(filtered)}"
)

print()


# ==========================================================
# RANKING
# ==========================================================

ranked = rank_candidates(
    filtered
)

print("=" * 60)
print("Ranking")
print("=" * 60)

print(
    f"Ranked Candidates : {len(ranked)}"
)

print()


# ==========================================================
# TOP 10
# ==========================================================

print("=" * 60)
print("Top 10 Ranked Candidates")
print("=" * 60)

for candidate in ranked[:10]:

    payload = candidate[
        "payload"
    ]

    print()

    print(
        f"Rank : {candidate['rank']}"
    )

    print(
        f"Candidate : {candidate['candidate_id']}"
    )

    print(
        f"Final Score : {candidate['final_score']}"
    )

    print(
        f"Similarity : {candidate['similarity_score']:.4f}"
    )

    print(
        f"Experience : {payload.get('years_experience')}"
    )

    print(
        f"Company : {payload.get('current_company')}"
    )


# ==========================================================
# SCORE BREAKDOWN
# ==========================================================

print()

print("=" * 60)
print("Top Candidate Breakdown")
print("=" * 60)

top = ranked[0]

for key, value in top[
    "score_breakdown"
].items():

    print(
        f"{key:<20}: {value}"
    )


# ==========================================================
# VALIDATION
# ==========================================================

print()

print("=" * 60)
print("Validation")
print("=" * 60)

# ---------- sorted ----------

scores = [

    c["final_score"]

    for c in ranked

]

sorted_scores = all(

    scores[i] >= scores[i + 1]

    for i in range(
        len(scores) - 1
    )

)

print(
    f"Scores Sorted : {sorted_scores}"
)

# ---------- ranks ----------

correct_ranks = all(

    ranked[i]["rank"] == i + 1

    for i in range(
        len(ranked)
    )

)

print(
    f"Ranks Correct : {correct_ranks}"
)

# ---------- breakdown ----------

breakdown_exists = all(

    "score_breakdown" in c

    for c in ranked

)

print(
    f"Breakdown Present : {breakdown_exists}"
)

print()

print("=" * 60)

if (

    sorted_scores

    and

    correct_ranks

    and

    breakdown_exists

):

    print(
        "Ranking Test : PASSED"
    )

else:

    print(
        "Ranking Test : FAILED"
    )

print("=" * 60)