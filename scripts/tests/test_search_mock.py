"""
Test Qdrant semantic search using an
existing candidate embedding.

This test does NOT require the
Role Intelligence or JD Embedding
modules.

Usage
-----
python -m scripts.tests.test_search_mock
"""

import pandas as pd

from src.config.settings import (
    CANDIDATE_INDEX_FILE,
)

from src.retrieval.search import (
    search_candidates,
)


# ==========================================================
# LOAD CANDIDATE INDEX
# ==========================================================

print()
print("=" * 60)
print("Loading Candidate Index")
print("=" * 60)

df = pd.read_parquet(
    CANDIDATE_INDEX_FILE
)

print(f"Candidates : {len(df)}")

print()


# ==========================================================
# USE FIRST CANDIDATE EMBEDDING
# ==========================================================

candidate = df.iloc[0]

embedding = candidate[
    "embedding"
]

print("=" * 60)
print("Mock Query")
print("=" * 60)

print(
    f"Candidate ID : {candidate['candidate_id']}"
)

print(
    f"Embedding Dimension : {len(embedding)}"
)

print()


# ==========================================================
# SEARCH
# ==========================================================

results = search_candidates(

    embedding=embedding,

    limit=10,

)


# ==========================================================
# RESULTS
# ==========================================================

print("=" * 60)
print("Top 10 Results")
print("=" * 60)

for rank, result in enumerate(

    results,

    start=1,

):

    payload = result["payload"]

    print()

    print(f"Rank #{rank}")

    print(
        f"Candidate ID : {result['candidate_id']}"
    )

    print(
        f"Similarity : {result['similarity_score']:.6f}"
    )

    print(
        f"Headline : {payload.get('headline')}"
    )

    print(
        f"Current Company : {payload.get('current_company')}"
    )

    print(
        f"Experience : {payload.get('years_experience')}"
    )


# ==========================================================
# VALIDATION
# ==========================================================

print()

print("=" * 60)
print("Validation")
print("=" * 60)

print(
    f"Returned Candidates : {len(results)}"
)

# ---------- duplicate ----------

duplicate_count = (

    len(results)

    -

    len({

        r["candidate_id"]

        for r in results

    })

)

print(
    f"Duplicate IDs : {duplicate_count}"
)

# ---------- sorted ----------

scores = [

    r["similarity_score"]

    for r in results

]

sorted_scores = all(

    scores[i] >= scores[i + 1]

    for i in range(
        len(scores) - 1
    )

)

print(
    f"Sorted Scores : {sorted_scores}"
)

# ---------- self match ----------

top_candidate = results[0]

print(
    f"Top Candidate : {top_candidate['candidate_id']}"
)

print(
    f"Expected Candidate : {candidate['candidate_id']}"
)

self_match = (

    top_candidate["candidate_id"]

    ==

    candidate["candidate_id"]

)

print(
    f"Self Match : {self_match}"
)

print()

print("=" * 60)

if (

    len(results) == 10

    and

    duplicate_count == 0

    and

    sorted_scores

):

    print(
        "Semantic Search Test : PASSED"
    )

else:

    print(
        "Semantic Search Test : FAILED"
    )

print("=" * 60)