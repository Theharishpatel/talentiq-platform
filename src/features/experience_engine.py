"""
Experience scoring engine.
"""

from statistics import mean

from src.features.scoring import (
    percentile_score,
)

def build_experience_features(
        candidate: dict,
) -> dict:
    
    profile = candidate.get(
        "profile",
        {}
    )

    jobs = candidate.get(
        "career_history",
        []
    )

    skills = candidate.get(
        "skills",
        []
    )

    #----- experience -----

    years_experience = profile.get(
        "years_of_experience",
        0,
    )

    #----- job feature ----

    job_count = len(jobs)

    job_durations = []

    current_job_duration = 0

    for job in jobs:

        duration = job.get(
            "duration_months"
        )

        if duration is not None:
            job_durations.append(
                duration
            )

        if job.get("is_current"):

            current_job_duration = (
                duration or 0
            )
        
    avg_job_duration = (
        mean(job_durations)
        if job_durations
        else 0
    )

    longest_job_duration = (
        max(job_durations)
        if job_durations
        else 0
    )

    #----- skills features ----

    skill_count = len(skills)

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

    longest_skill_duration = (
        max(skill_durations)
        if skill_durations
        else 0
    )

    #---- percentile score -----

    exp_score = percentile_score(
        years_experience,
        p25=3.9,
        p50=6.8,
        p75=9.9,
        p90=13.0,
    )

    stability_score = percentile_score(
        avg_job_duration,
        p25=18,
        p50=27,
        p75=38,
        p90=46,
    )

    maturity_score = percentile_score(
        avg_skill_duration,
        p25=10,
        p50=16,
        p75=25,
        p90=33,
    )

    breadth_score = percentile_score(
        skill_count,
        p25=7,
        p50=9,
        p75=11,
        p90=14,
    )

    #----- final experience score -----

    experience_score = round(
        (
            exp_score * 0.40 + stability_score * 0.30 + maturity_score * 0.20 + breadth_score * 0.10
        ),
        2,
    )

    return {
        "years_experience":
            years_experience,

        "job_count":
            job_count,

        "avg_job_duration":
            round(
                avg_job_duration,
                2,
            ),

        "longest_job_duration":
            longest_job_duration,

        "current_job_duration":
            current_job_duration,

        "skill_count":
            skill_count,

        "avg_skill_duration":
            round(
                avg_skill_duration,
                2,
            ),

        "longest_skill_duration":
            longest_skill_duration,

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

