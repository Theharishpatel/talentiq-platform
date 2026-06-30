"""
Mock test for ranking engine.

This test validates only the ranking
logic without requiring Qdrant,
retrieval or embeddings.

Usage
-----
python -m scripts.tests.test_ranking_mock
"""

from src.ranking.engine import (
    rank_candidates,
)


# ==========================================================
# MOCK CANDIDATES
# ==========================================================

mock_candidates = [

    {

        "candidate_id":
            "CAND_001",

        "similarity_score":
            0.95,

        "payload": {

            "experience_score":
                90,

            "behavior_score":
                80,

            "growth_score":
                70,

            "recruitability_score":
                92,

            "consistency_score":
                90,

            "risk_score":
                5,

        },

    },

    {

        "candidate_id":
            "CAND_002",

        "similarity_score":
            0.82,

        "payload": {

            "experience_score":
                78,

            "behavior_score":
                75,

            "growth_score":
                81,

            "recruitability_score":
                84,

            "consistency_score":
                83,

            "risk_score":
                12,

        },

    },

    {

        "candidate_id":
            "CAND_003",

        "similarity_score":
            0.90,

        "payload": {

            "experience_score":
                88,

            "behavior_score":
                89,

            "growth_score":
                91,

            "recruitability_score":
                87,

            "consistency_score":
                86,

            "risk_score":
                3,

        },

    },

]


# ==========================================================
# RANK
# ==========================================================

ranked = rank_candidates(
    mock_candidates
)


# ==========================================================
# RESULTS
# ==========================================================

print()

print("=" * 60)
print("Ranking Results")
print("=" * 60)

for candidate in ranked:

    print()

    print(
        f"Rank           : {candidate['rank']}"
    )

    print(
        f"Candidate      : {candidate['candidate_id']}"
    )

    print(
        f"Final Score    : {candidate['final_score']}"
    )

    print(
        f"Similarity     : {candidate['similarity_score']}"
    )


# ==========================================================
# TOP CANDIDATE
# ==========================================================

print()

print("=" * 60)
print("Top Candidate Breakdown")
print("=" * 60)

for key, value in ranked[
    0
][
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

# ---------- ranking ----------

sorted_scores = all(

    ranked[i][
        "final_score"
    ]

    >=

    ranked[i + 1][
        "final_score"
    ]

    for i in range(

        len(ranked) - 1

    )

)

print(
    f"Scores Sorted      : {sorted_scores}"
)


# ---------- ranks ----------

correct_ranks = all(

    ranked[i][
        "rank"
    ]

    ==

    i + 1

    for i in range(

        len(ranked)

    )

)

print(
    f"Ranks Correct      : {correct_ranks}"
)


# ---------- breakdown ----------

breakdown = all(

    "score_breakdown"

    in

    candidate

    for candidate in ranked

)

print(
    f"Breakdown Present  : {breakdown}"
)


# ---------- final score ----------

final_scores = all(

    "final_score"

    in

    candidate

    for candidate in ranked

)

print(
    f"Final Score Exists : {final_scores}"
)


# ---------- duplicate ----------

duplicates = (

    len(ranked)

    -

    len({

        c[
            "candidate_id"
        ]

        for c in ranked

    })

)

print(
    f"Duplicate IDs      : {duplicates}"
)

print()

print("=" * 60)

if (

    sorted_scores

    and

    correct_ranks

    and

    breakdown

    and

    final_scores

    and

    duplicates == 0

):

    print(
        "Ranking Mock Test : PASSED"
    )

else:

    print(
        "Ranking Mock Test : FAILED"
    )

print("=" * 60)