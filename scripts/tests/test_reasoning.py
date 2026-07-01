"""
Integration test for the
reasoning engine.
"""

import pandas as pd

from src.config.settings import (
    CANDIDATE_INDEX_FILE,
)

from src.retrieval.search import (
    search_candidates,
)

from src.ranking.engine import (
    rank_candidates,
)

from src.reasoning.engine import (
    generate_reasons,
)


# ==========================================================
# LOAD DATA
# ==========================================================

print()

print("=" * 60)
print("Loading Candidate Index")
print("=" * 60)

df = pd.read_parquet(
    CANDIDATE_INDEX_FILE
)

print(
    f"Candidates : {len(df)}"
)

print()


# ==========================================================
# BUILD MOCK QUERY
# ==========================================================

query_embedding = df.iloc[0][
    "embedding"
]

print("=" * 60)
print("Searching Candidates")
print("=" * 60)

retrieved = search_candidates(

    embedding=query_embedding,

    limit=10,

)

print(
    f"Retrieved : {len(retrieved)}"
)

print()


# ==========================================================
# RANK
# ==========================================================

print("=" * 60)
print("Ranking Candidates")
print("=" * 60)

ranked = rank_candidates(
    retrieved
)

print(
    f"Ranked : {len(ranked)}"
)

print()


# ==========================================================
# GENERATE REASONING
# ==========================================================

print("=" * 60)
print("Generating Reasons")
print("=" * 60)

results = generate_reasons(
    ranked
)

print(
    f"Generated : {len(results)}"
)

print()


# ==========================================================
# DISPLAY TOP 5
# ==========================================================

print("=" * 60)
print("Top Candidates")
print("=" * 60)

for rank, candidate in enumerate(

    results[:5],

    start=1,

):

    reasoning = candidate[
        "reasoning"
    ]

    print()

    print(
        f"Rank #{rank}"
    )

    print(
        "Candidate :",
        candidate["payload"][
            "candidate_id"
        ]
    )

    print(
        "Final Score :",
        round(
            candidate[
                "final_score"
            ],
            2,
        )
    )

    print(
        "Summary :",
        reasoning[
            "summary"
        ]
    )

    print(
        "Highlights :"
    )

    for item in reasoning[
        "highlights"
    ]:

        print(
            f"  • {item}"
        )


# ==========================================================
# VALIDATION
# ==========================================================

print()

print("=" * 60)
print("Validation")
print("=" * 60)

assert len(results) > 0

for candidate in results:

    assert (
        "reasoning"
        in candidate
    )

    assert (
        "summary"
        in candidate[
            "reasoning"
        ]
    )

    assert (
        "highlights"
        in candidate[
            "reasoning"
        ]
    )

    assert len(

        candidate[
            "reasoning"
        ][
            "highlights"
        ]

    ) > 0

print(
    "Candidates Checked :",
    len(results)
)

print(
    "Reasoning Added : YES"
)

print()

print("=" * 60)
print("Reasoning Integration Test : PASSED")
print("=" * 60)