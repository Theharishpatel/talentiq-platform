"""
Submission generator.

Convert ranked candidates into
submission records that match
the organization submission
format.
"""

from typing import Any


def build_submission(
    candidates: list[dict],
) -> list[dict[str, Any]]:
    """
    Build submission records.

    Parameters
    ----------
    candidates : list[dict]

    Returns
    -------
    list[dict]
        Submission records ready
        for CSV export.
    """

    submission = []

    for rank, candidate in enumerate(

        candidates,

        start=1,

    ):

        payload = candidate[
            "payload"
        ]

        reasoning = candidate[
            "reasoning"
        ]

        reasoning_text = (

            reasoning[
                "summary"
            ]

            + " "

            + " ".join(

                reasoning[
                    "highlights"
                ]

            )

        )

        record = {

            "candidate_id":

                payload[
                    "candidate_id"
                ],

            "rank":

                rank,

            "score":

                round(

                    candidate[
                        "final_score"
                    ],

                    2,

                ),

            "reasoning":

                reasoning_text,

        }

        submission.append(
            record
        )

    return submission