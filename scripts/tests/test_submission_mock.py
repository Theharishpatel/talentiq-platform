"""
Mock test for submission engine.
"""

from pathlib import Path

from src.submission.generator import (
    build_submission,
)

from src.submission.validator import (
    validate_submission,
)

from src.submission.exporter import (
    export_submission,
)


# ==========================================================
# MOCK RANKED CANDIDATES
# ==========================================================

mock_candidates = [

    {

        "final_score": 96.45,

        "payload": {

            "candidate_id": "CAND_0000001",

        },

        "reasoning": {

            "summary":

                "Excellent overall match.",

            "highlights": [

                "Strong semantic similarity.",

                "High recruitability.",

                "Low hiring risk.",

            ],

        },

    },

    {

        "final_score": 92.11,

        "payload": {

            "candidate_id": "CAND_0000002",

        },

        "reasoning": {

            "summary":

                "Strong candidate.",

            "highlights": [

                "Relevant experience.",

                "Career growth.",

                "Open to work.",

            ],

        },

    },

]


# ==========================================================
# GENERATE SUBMISSION
# ==========================================================

print()

print("=" * 60)
print("Generating Submission")
print("=" * 60)

submission = build_submission(
    mock_candidates
)

print(
    f"Records : {len(submission)}"
)


# ==========================================================
# VALIDATE
# ==========================================================

validate_submission(
    submission
)


# ==========================================================
# EXPORT
# ==========================================================

output = Path(
    "outputs/submission_mock.csv"
)

export_submission(

    submission,

    output,

)


# ==========================================================
# DISPLAY
# ==========================================================

print()

print("=" * 60)
print("Submission Preview")
print("=" * 60)

for row in submission:

    print(row)

print()

print("=" * 60)
print("Mock Submission Test : PASSED")
print("=" * 60)