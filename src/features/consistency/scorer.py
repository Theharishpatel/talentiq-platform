"""
Consistency Scoring.

Converts raw consistency features into normalized scores.
"""

from src.features.scoring import percentile_score


def score_consistency_features(
    features: dict,
) -> dict:

    experience_ratio = features.get(
        "experience_ratio",
        0,
    )

    job_duration_variance = features.get(
        "job_duration_variance",
        0,
    )

    skill_ratio = features.get(
        "skill_ratio",
        0,
    )

    current_job_duration = features.get(
        "current_job_duration",
        0,
    )

    # ------ Experience Consistency -----

    experience_consistency_score = 100 - min(

        abs(
            experience_ratio - 1
        ) * 200,

        100,

    )

    # ------ Job Stability ------

    stability_score = 100 - percentile_score(

        job_duration_variance,

        p25=15,

        p50=24,

        p75=32,

        p90=40,

    )

    # ----- Skill Consistency -----

    skill_consistency_score = percentile_score(

        skill_ratio,

        p25=0.40,

        p50=0.60,

        p75=0.80,

        p90=0.95,

    )

    # ----- Current Job Commitment -----

    commitment_score = percentile_score(

        current_job_duration,

        p25=12,

        p50=24,

        p75=36,

        p90=48,

    )

    # ----- Final Score -----

    consistency_score = round(

        (

            experience_consistency_score * 0.35 +

            stability_score * 0.30 +

            skill_consistency_score * 0.20 +

            commitment_score * 0.15

        ),

        2,

    )

    return {

        "experience_consistency_score":
            round(
                experience_consistency_score,
                2,
            ),

        "stability_score":
            round(
                stability_score,
                2,
            ),

        "skill_consistency_score":
            skill_consistency_score,

        "commitment_score":
            commitment_score,

        "consistency_score":
            consistency_score,

    }