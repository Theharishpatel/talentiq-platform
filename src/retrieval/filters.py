"""
Candidate retrieval filters.
"""

from typing import Any


def filter_candidates(
    candidates: list[dict[str, Any]],

    min_experience: float | None = None,

    max_risk_score: int = 80,

    require_open_to_work: bool = False,

    min_recruitability: float = 0,

    min_consistency: float = 0,

) -> list[dict[str, Any]]:
    """
    Apply lightweight filters on retrieved
    candidates before ranking.

    Parameters
    ----------
    candidates

    min_experience

    max_risk_score

    require_open_to_work

    min_recruitability

    min_consistency
    """

    filtered = []

    for candidate in candidates:

        payload = candidate.get(
            "payload",
            {},
        )

        # ----------------------------
        # Experience
        # ----------------------------

        if min_experience is not None:

            if payload.get(
                "years_experience",
                0,
            ) < min_experience:

                continue

        # ----------------------------
        # Risk
        # ----------------------------

        if payload.get(
            "risk_score",
            0,
        ) > max_risk_score:

            continue

        # ----------------------------
        # Open To Work
        # ----------------------------

        if require_open_to_work:

            if not payload.get(
                "open_to_work",
                False,
            ):

                continue

        # ----------------------------
        # Recruitability
        # ----------------------------

        if payload.get(
            "recruitability_score",
            0,
        ) < min_recruitability:

            continue

        # ----------------------------
        # Consistency
        # ----------------------------

        if payload.get(
            "consistency_score",
            0,
        ) < min_consistency:

            continue

        filtered.append(
            candidate
        )

    return filtered