"""
Experience scoring engine.

Converts raw experience features into normalized scores.
"""

from src.features.scoring import (
    percentile_score,
)


def score_experience_features(
    features: dict,
) -> dict:
    """
    Calculate experience-related scores.

    Parameters
    ----------
    features : dict
        Raw features extracted by experience.engine

    Returns
    -------
    dict
        Experience scores.
    """

    # ------ Individual Scores -----

    exp_score = percentile_score(
        features["years_experience"],
        p25=3.9,
        p50=6.8,
        p75=9.9,
        p90=13.0,
    )

    stability_score = percentile_score(
        features["avg_job_duration"],
        p25=18,
        p50=27,
        p75=38,
        p90=46,
    )

    maturity_score = percentile_score(
        features["avg_skill_duration"],
        p25=10,
        p50=16,
        p75=25,
        p90=33,
    )

    breadth_score = percentile_score(
        features["skill_count"],
        p25=7,
        p50=9,
        p75=11,
        p90=14,
    )

    # --- Final Experience Score ----

    experience_score = round(
        (
            exp_score * 0.40
            + stability_score * 0.30
            + maturity_score * 0.20
            + breadth_score * 0.10
        ),
        2,
    )

    # ----- Output ----

    return {

        "exp_score":
            exp_score,

        "stability_score":
            stability_score,

        "maturity_score":
            maturity_score,

        "breadth_score":
            breadth_score,

        "experience_score":
            experience_score,
    }