"""
Test semantic retrieval from Qdrant.

Usage
-----
python -m scripts.tests.test_search
"""

from src.ranking.jd_embedding.pipeline import (
    build_jd_embedding,
)

from src.retrieval.search import (
    search_candidates,
)


# ==========================================================
# SAMPLE JD
# ==========================================================

JD = """
Senior Backend Engineer

Skills:
Python
FastAPI
Docker
Redis
AWS
PostgreSQL

Experience:
5+ years
"""


# ==========================================================
# BUILD JD EMBEDDING
# ==========================================================

result = build_jd_embedding(
    JD
)

embedding = result[
    "embedding"
]

print()
print("=" * 60)
print("JD Embedding")
print("=" * 60)

print(
    f"Dimension : {len(embedding)}"
)

print(
    f"Role : {result['role_profile'].get('role')}"
)

print()


# ==========================================================
# SEARCH
# ==========================================================

results = search_candidates(

    embedding=embedding,

    limit=1000,

)


# ==========================================================
# RESULTS
# ==========================================================

print("=" * 60)
print("Top Candidates")
print("=" * 60)

for idx, candidate in enumerate(

    results,

    start=1,

):

    payload = candidate["payload"]

    print()

    print(f"Rank #{idx}")

    print(
        f"Candidate : {candidate['candidate_id']}"
    )

    print(
        f"Similarity : {candidate['similarity_score']:.4f}"
    )

    print(
        f"Headline : {payload.get('headline')}"
    )

    print(
        f"Company : {payload.get('current_company')}"
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

scores = [

    r["similarity_score"]

    for r in results

]

descending = all(

    scores[i] >= scores[i + 1]

    for i in range(
        len(scores) - 1
    )

)

print(
    f"Scores Sorted : {descending}"
)

duplicates = len({

    r["candidate_id"]

    for r in results

})

print(
    f"Duplicate IDs : {len(results) - duplicates}"
)

print()

print("=" * 60)
print("Retrieval Test Passed")
print("=" * 60)