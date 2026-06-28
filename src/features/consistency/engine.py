"""
Consistency Feature Engineering Engine.

Extracts raw consistency related features.

No scoring logic should exist in this file.
"""

from statistics import mean


def build_consistency_features(
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

    # ------- Experience Consistency ------

    years_experience = profile.get(
        "years_of_experience",
        0,
    )

    total_job_months = 0

    job_durations = []

    current_job_duration = 0

    for job in jobs:

        duration = job.get(
            "duration_months"
        )

        if duration is None:

            continue

        total_job_months += duration

        job_durations.append(
            duration
        )

        if job.get("is_current"):

            current_job_duration = duration

    career_years = (
        total_job_months / 12
    )

    experience_ratio = 0

    if years_experience > 0:

        experience_ratio = (
            career_years /
            years_experience
        )

    # ----- Job Stability ------

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

    shortest_job_duration = (

        min(job_durations)

        if job_durations

        else 0

    )

    job_duration_variance = (

        longest_job_duration -
        shortest_job_duration

        if job_durations

        else 0

    )

    # ---- Skill Consostency ----

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

    shortest_skill_duration = (

        min(skill_durations)

        if skill_durations

        else 0

    )

    skill_ratio = 0

    if longest_skill_duration > 0:

        skill_ratio = (

            avg_skill_duration /

            longest_skill_duration

        )

    # ----- Return ----

    return {

        "career_years":
            round(
                career_years,
                2,
            ),

        "years_experience":
            years_experience,

        "experience_ratio":
            round(
                experience_ratio,
                2,
            ),

        "avg_job_duration":
            round(
                avg_job_duration,
                2,
            ),

        "current_job_duration":
            current_job_duration,

        "longest_job_duration":
            longest_job_duration,

        "shortest_job_duration":
            shortest_job_duration,

        "job_duration_variance":
            job_duration_variance,

        "avg_skill_duration":
            round(
                avg_skill_duration,
                2,
            ),

        "longest_skill_duration":
            longest_skill_duration,

        "shortest_skill_duration":
            shortest_skill_duration,

        "skill_ratio":
            round(
                skill_ratio,
                2,
            ),
    }