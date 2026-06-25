"""
Consistency Engine.
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

    # ------- experience consistency ----

    years_experience = profile.get(
        "years_of_experience",
        0
    )

    total_months = 0

    job_durations = []

    for job in jobs:

        duration = job.get(
            "duration_months"
        )

        if duration is None:
            continue

        total_months += duration

        job_durations.append(
            duration
        )

    career_years = (
        total_months / 12
    )

    ratio = 0

    if years_experience > 0:

        ratio = (
            career_years
            / years_experience
        )

    if 0.90 <= ratio <= 1.10:

        experience_consistency_score = 100

    elif 0.80 <= ratio <= 1.20:

        experience_consistency_score = 80

    elif 0.70 <= ratio <= 1.30:

        experience_consistency_score = 60

    else:

        experience_consistency_score = 30

    # ------ career stability -----

    variance = 0

    if len(job_durations) > 1:

        variance = (
            max(job_durations)
            - min(job_durations)
        )

    if variance <= 15:

        stability_score = 100

    elif variance <= 24:

        stability_score = 90

    elif variance <= 32:

        stability_score = 75

    elif variance <= 38:

        stability_score = 50

    else:

        stability_score = 25

    # ----- skill consistency ------ 

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

    skill_ratio = 0

    if longest_skill_duration > 0:

        skill_ratio = (
            avg_skill_duration
            / longest_skill_duration
        )

    if skill_ratio >= 0.80:

        skill_consistency_score = 100

    elif skill_ratio >= 0.60:

        skill_consistency_score = 80

    elif skill_ratio >= 0.40:

        skill_consistency_score = 60

    else:

        skill_consistency_score = 30

    # ----- Final Score -----

    consistency_score = round(
        (
            experience_consistency_score * 0.40
            + stability_score * 0.35
            + skill_consistency_score * 0.25
        ),
        2,
    )

    return {

        "career_years":
            round(
                career_years,
                2
            ),

        "years_experience":
            years_experience,

        "experience_ratio":
            round(
                ratio,
                2
            ),

        "job_variance":
            variance,

        "avg_skill_duration":
            round(
                avg_skill_duration,
                2
            ),

        "longest_skill_duration":
            longest_skill_duration,

        "skill_ratio":
            round(
                skill_ratio,
                2
            ),

        "experience_consistency_score":
            experience_consistency_score,

        "stability_score":
            stability_score,

        "skill_consistency_score":
            skill_consistency_score,

        "consistency_score":
            consistency_score,
    }