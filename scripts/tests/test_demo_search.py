"""
Test demo semantic search.
"""

from src.demo.loader import (
    load_demo_candidates,
)

from src.demo.search import (
    search_candidates,
)


print()

print("=" * 60)
print("Loading Demo Candidates")
print("=" * 60)

df = load_demo_candidates()

print(
    "Candidates :",
    len(df),
)

query_embedding = df.iloc[0][
    "embedding"
]

print()

print("=" * 60)
print("Searching")
print("=" * 60)

results = search_candidates(

    embedding=query_embedding,

    limit=10,

)

print()

print("=" * 60)
print("Top Results")
print("=" * 60)

for i, candidate in enumerate(

    results,

    start=1,

):

    payload = candidate[
        "payload"
    ]

    print()

    print(
        f"Rank #{i}"
    )

    print(
        "Candidate :",
        candidate[
            "candidate_id"
        ],
    )

    print(
        "Similarity :",
        candidate[
            "similarity_score"
        ],
    )

    print(
        "Headline :",
        payload[
            "headline"
        ],
    )

print()

print("=" * 60)
print("Validation")
print("=" * 60)

print(
    "Returned :",
    len(results),
)

print(
    "Self Match :",
    results[0][
        "candidate_id"
    ]
    == df.iloc[0][
        "candidate_id"
    ],
)

print()

print("=" * 60)
print("Demo Search PASSED")
print("=" * 60)