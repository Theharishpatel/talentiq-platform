"""
Candidate ranking scorer.
"""

from src.ranking.weights import (
    BEHAVIOR_WEIGHT,
    CONSISTENCY_WEIGHT,
    EXPERIENCE_WEIGHT,
    GROWTH_WEIGHT,
    RECRUITABILITY_WEIGHT,
    RISK_WEIGHT,
    SIMILARITY_WEIGHT,
)


def score_candidate(
    candidate: dict,
) -> dict:
    """
    Compute ranking score for a
    single candidate.

    Parameters
    ----------
    candidate : dict

    Returns
    -------
    dict

        {
            "final_score": float,
            "score_breakdown": dict
        }
    """

    payload = candidate.get(
        "payload",
        {},
    )

    # ======================================================
    # FEATURES
    # ======================================================

    similarity = (

        candidate.get(
            "similarity_score",
            0,
        )

        * 100

    )

    experience = payload.get(
        "experience_score",
        0,
    )

    recruitability = payload.get(
        "recruitability_score",
        0,
    )

    growth = payload.get(
        "growth_score",
        0,
    )

    behavior = payload.get(
        "behavior_score",
        0,
    )

    consistency = payload.get(
        "consistency_score",
        0,
    )

    risk = payload.get(
        "risk_score",
        0,
    )

    # ======================================================
    # INDIVIDUAL CONTRIBUTIONS
    # ======================================================

    similarity_score = (
        similarity
        * SIMILARITY_WEIGHT
    )

    experience_score = (
        experience
        * EXPERIENCE_WEIGHT
    )

    recruitability_score = (
        recruitability
        * RECRUITABILITY_WEIGHT
    )

    growth_score = (
        growth
        * GROWTH_WEIGHT
    )

    behavior_score = (
        behavior
        * BEHAVIOR_WEIGHT
    )

    consistency_score = (
        consistency
        * CONSISTENCY_WEIGHT
    )

    risk_penalty = (
        risk
        * RISK_WEIGHT
    )

    # ======================================================
    # FINAL SCORE
    # ======================================================

    final_score = (

        similarity_score

        + experience_score

        + recruitability_score

        + growth_score

        + behavior_score

        + consistency_score

        - risk_penalty

    )

    final_score = round(
        final_score,
        4,
    )

    # ======================================================
    # RETURN
    # ======================================================

    return {

        "final_score":
            final_score,

        "score_breakdown": {

            "similarity":
                round(
                    similarity_score,
                    4,
                ),

            "experience":
                round(
                    experience_score,
                    4,
                ),

            "recruitability":
                round(
                    recruitability_score,
                    4,
                ),

            "growth":
                round(
                    growth_score,
                    4,
                ),

            "behavior":
                round(
                    behavior_score,
                    4,
                ),

            "consistency":
                round(
                    consistency_score,
                    4,
                ),

            "risk_penalty":
                round(
                    risk_penalty,
                    4,
                ),

        },

    }