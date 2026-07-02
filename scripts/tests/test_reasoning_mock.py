"""
Mock test for reasoning engine.
"""

from src.reasoning.engine import (
    generate_reasons,
)


# ------- MOCK RANKED CANDIDATE -----

candidate = {

    "candidate_id": "CAND_0000001",

    "final_score": 92.6,

    "score_breakdown": {

        "similarity": 33.8,

        "experience": 18.4,

        "recruitability": 13.7,

        "growth": 8.8,

        "behavior": 9.1,

        "consistency": 9.5,

        "risk_penalty": 1.2,

    },

    "payload": {

        "risk_score": 12,

        "open_to_work": True,

    },

}


# ----- GENERATE REASONING -----

results = generate_reasons(

    [candidate]

)

result = results[0]

reasoning = result["reasoning"]


# ------ DISPLAY ------

print()

print("=" * 60)
print("Reasoning Engine Mock Test")
print("=" * 60)

print()

print("Candidate ID")
print(result["candidate_id"])

print()

print("Final Score")
print(result["final_score"])

print()

print("Summary")
print()

print("Recruiter Explanation")

print(

    reasoning[
        "explanation"
    ]

)
print(reasoning["summary"])

print()

print("Highlights")

for i, item in enumerate(

    reasoning["highlights"],

    start=1,

):

    print(f"{i}. {item}")

print()

print("=" * 60)
print("Validation")
print("=" * 60)

print(

    "Summary Exists :",

    bool(reasoning["summary"])

)

print(

    "Highlights :",

    len(reasoning["highlights"])

)

print(

    "Reasoning Generated :",

    "reasoning" in result

)

assert (

    "reasoning"

    in result

)

assert (

    "explanation"

    in reasoning

)

assert (

    len(

        reasoning["highlights"]

    ) > 0

)

assert (

    isinstance(

        reasoning["summary"],

        str,

    )

)

print()

print("=" * 60)
print("Reasoning Mock Test : PASSED")
print("=" * 60)