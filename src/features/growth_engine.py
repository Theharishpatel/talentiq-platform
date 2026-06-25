"""
Career Growth Engine.
"""

from statistics import mean

from src.features.scoring import (
    percentile_score,
)

def build_growth_features(
        candidate: dict,
) -> dict:
    
    jobs = candidate.get(
        "career_history",
        []
    )

    skills = candidate.get(
        "skills",
        []
    )

    education = candidate.get(
        "education",
        []
    )

    # ----- job breadth ----

    job_count = len(jobs)

    breadth_score = percentile_score(
        job_count,
        p25=2,
        p50=3,
        p75=4,
        p90=5,
    )

    # ----- skill breadth ---- 

    skill_count = len(skills)

    skill_breadth_score = percentile_score(
        skill_count,
        p25=7,
        p50=9,
        p75=11,
        p90=14,
    )

    # ---- skill maturity ----

    skill_durations = []

    for skill in skills:

        duration = skill.get(
            "duration_months"
        )

        if duration is not None:
            
            skill_durations.append(
                duration
            )

    avg_skill_duration = (
        mean(skill_durations)
        if skill_durations
        else 0
    )

    skill_maturity_score = percentile_score(
        avg_skill_duration,
        p25=10,
        p50=16,
        p75=25,
        p90=33,
    )

    # ----- education depth ------

    education_count = len(
        education
    )

    if education_count >= 2:

        education_score = 100

    else:

        education_score = 60

    # ----- final growth score -----

    growth_score = round(
        (
            breadth_score *0.30 + 
            skill_breadth_score * 0.25 + 
            skill_maturity_score * 0.30 + 
            education_score * 0.15
        ),
        2,
    )

    return {
        "job_count":
            job_count,

        "skill_count":
            skill_count,

        "avg_skill_duration":
            round(
                avg_skill_duration,
                2,
            ),

        "education_count":
            education_count,

        "breadth_score":
            breadth_score,

        "skill_breadth_score":
            skill_breadth_score,

        "skill_maturity_score":
            skill_maturity_score,

        "education_score":
            education_score,

        "growth_score":
            growth_score,

        
    }