"""
Reason generator.

Generate recruiter-friendly
explanations for a single
candidate based on the
ranking score breakdown.
"""

from src.reasoning.templates import (
    EXCELLENT_MATCH,
    STRONG_MATCH,
    GOOD_MATCH,
    MODERATE_MATCH,
    HIGH_SIMILARITY,
    GOOD_SIMILARITY,
    HIGH_EXPERIENCE,
    GOOD_EXPERIENCE,
    HIGH_RECRUITABILITY,
    GOOD_RECRUITABILITY,
    HIGH_GROWTH,
    GOOD_GROWTH,
    HIGH_BEHAVIOR,
    GOOD_BEHAVIOR,
    HIGH_CONSISTENCY,
    GOOD_CONSISTENCY,
    LOW_RISK,
    MEDIUM_RISK,
    HIGH_RISK,
    OPEN_TO_WORK,
    NO_REASON,
)


def generate_reason(
    candidate: dict,
) -> dict:
    """
    Generate reasoning for
    one ranked candidate.

    Parameters
    ----------
    candidate : dict

    Returns
    -------
    dict

        {
            "summary": str,
            "highlights": list[str]
        }
    """

    breakdown = candidate[
        "score_breakdown"
    ]

    payload = candidate[
        "payload"
    ]

    final_score = candidate[
        "final_score"
    ]

    highlights = []

    # ----- Semantic Match -----

    if breakdown["similarity"] >= 30:

        highlights.append(
            HIGH_SIMILARITY
        )

    elif breakdown["similarity"] >= 20:

        highlights.append(
            GOOD_SIMILARITY
        )

    # ----- Experience ------

    if breakdown["experience"] >= 15:

        highlights.append(
            HIGH_EXPERIENCE
        )

    elif breakdown["experience"] >= 10:

        highlights.append(
            GOOD_EXPERIENCE
        )

    # ------ Recruitability ------

    if breakdown["recruitability"] >= 12:

        highlights.append(
            HIGH_RECRUITABILITY
        )

    elif breakdown["recruitability"] >= 8:

        highlights.append(
            GOOD_RECRUITABILITY
        )

    # ----- Career Growth -----

    if breakdown["growth"] >= 8:

        highlights.append(
            HIGH_GROWTH
        )

    elif breakdown["growth"] >= 5:

        highlights.append(
            GOOD_GROWTH
        )

    # ------ Behavior ----

    if breakdown["behavior"] >= 8:

        highlights.append(
            HIGH_BEHAVIOR
        )

    elif breakdown["behavior"] >= 5:

        highlights.append(
            GOOD_BEHAVIOR
        )

    # ----- Consistency -----

    if breakdown["consistency"] >= 8:

        highlights.append(
            HIGH_CONSISTENCY
        )

    elif breakdown["consistency"] >= 5:

        highlights.append(
            GOOD_CONSISTENCY
        )

    # ------ Risk ------

    risk = payload.get(
        "risk_score",
        100,
    )

    if risk <= 20:

        highlights.append(
            LOW_RISK
        )

    elif risk <= 50:

        highlights.append(
            MEDIUM_RISK
        )

    else:

        highlights.append(
            HIGH_RISK
        )

    # -----  Open To Work -----

    if payload.get(
        "open_to_work",
        False,
    ):

        highlights.append(
            OPEN_TO_WORK
        )

    # ----- Fallback -----

    if not highlights:

        highlights.append(
            NO_REASON
        )

    # ----- Summary -----

    if final_score >= 90:

        summary = EXCELLENT_MATCH

    elif final_score >= 80:

        summary = STRONG_MATCH

    elif final_score >= 70:

        summary = GOOD_MATCH

    else:

        summary = MODERATE_MATCH

    return {

        "summary":
            summary,

        "highlights":
            highlights,

    }