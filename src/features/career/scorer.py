"""
Career Growth Scoring.

Converts raw growth features into normalized scores.
"""

from src.features.scoring import (
    percentile_score,
)


def score_growth_features(
    features: dict,
) -> dict:

    # ----- Raw Features -----

    promotion_count = features.get(
        "promotion_count",
        0,
    )

    highest_role_level = features.get(
        "highest_role_level",
        0,
    )

    company_size_growth = features.get(
        "company_size_growth",
        0,
    )

    skill_count = features.get(
        "skill_count",
        0,
    )

    advanced_skill_count = features.get(
        "advanced_skill_count",
        0,
    )

    avg_skill_duration = features.get(
        "avg_skill_duration",
        0,
    )

    highest_degree_level = features.get(
        "highest_degree_level",
        0,
    )

    certification_count = features.get(
        "certification_count",
        0,
    )

    # ----- Individual Scores -----

    promotion_score = percentile_score(
        promotion_count,
        p25=0,
        p50=1,
        p75=2,
        p90=3,
    )

    seniority_score = percentile_score(
        highest_role_level,
        p25=3,
        p50=4,
        p75=5,
        p90=6,
    )

    company_growth_score = percentile_score(
        company_size_growth,
        p25=0,
        p50=1,
        p75=2,
        p90=3,
    )

    skill_breadth_score = percentile_score(
        skill_count,
        p25=7,
        p50=9,
        p75=11,
        p90=14,
    )

    expertise_score = percentile_score(
        advanced_skill_count,
        p25=2,
        p50=4,
        p75=6,
        p90=8,
    )

    skill_maturity_score = percentile_score(
        avg_skill_duration,
        p25=10,
        p50=16,
        p75=25,
        p90=33,
    )

    education_score = percentile_score(
        highest_degree_level,
        p25=2,
        p50=3,
        p75=4,
        p90=5,
    )

    certification_score = percentile_score(
        certification_count,
        p25=0,
        p50=1,
        p75=2,
        p90=4,
    )

    # ----- Final Score ----

    growth_score = round(

        (

            promotion_score * 0.20 +

            seniority_score * 0.20 +

            company_growth_score * 0.10 +

            skill_breadth_score * 0.15 +

            expertise_score * 0.10 +

            skill_maturity_score * 0.10 +

            education_score * 0.10 +

            certification_score * 0.05

        ),

        2,

    )

    # ---- return ----

    return {

        "promotion_score":
            promotion_score,

        "seniority_score":
            seniority_score,

        "company_growth_score":
            company_growth_score,

        "skill_breadth_score":
            skill_breadth_score,

        "expertise_score":
            expertise_score,

        "skill_maturity_score":
            skill_maturity_score,

        "education_score":
            education_score,

        "certification_score":
            certification_score,

        "growth_score":
            growth_score,

    }