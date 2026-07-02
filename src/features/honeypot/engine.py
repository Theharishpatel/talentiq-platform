"""
Honeypot / Fraud Risk Feature Engineering Engine.

Extracts raw suspicious signals.

No scoring logic should exist in this file.
"""

from statistics import mean


def build_honeypot_features(
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

    signals = candidate.get(
        "redrob_signals",
        {}
    )

    preferences = candidate.get(
        "preferences",
        {}
    )

    # ----- Experience -----

    years_experience = profile.get(
        "years_of_experience",
        0,
    )

    salary = preferences.get(
        "desired_salary"
    )

    salary_per_year = 0

    if salary and years_experience > 0:

        salary_per_year = (
            salary /
            years_experience
        )

    # ------ Skills -----

    skill_count = len(
        skills
    )

    # ------ Career ------

    total_job_months = 0

    job_durations = []

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

    career_years = (
        total_job_months / 12
    )

    experience_ratio = 0

    if years_experience > 0:

        experience_ratio = (

            career_years /

            years_experience

        )

    avg_job_duration = (

        mean(job_durations)

        if job_durations

        else 0

    )

    # ----- Profile Activity -----

    recruiter_response_rate = signals.get(
        "recruiter_response_rate",
        0,
    )

    interview_completion_rate = signals.get(
        "interview_completion_rate",
        0,
    )

    search_appearance = signals.get(
        "search_appearance_30d",
        0,
    )

    saved_by_recruiters = signals.get(
        "saved_by_recruiters_30d",
        0,
    )

    verified_email = signals.get(
        "verified_email",
        False,
    )

    verified_phone = signals.get(
        "verified_phone",
        False,
    )

    linkedin_connected = signals.get(
        "linkedin_connected",
        False,
    )

    profile_completeness = signals.get(
        "profile_completeness_score",
        0,
    )

    # ---- retrun ---

    return {

        "salary_per_year":
            round(
                salary_per_year,
                2,
            ),

        "skill_count":
            skill_count,

        "career_years":
            round(
                career_years,
                2,
            ),

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

        "recruiter_response_rate":
            recruiter_response_rate,

        "interview_completion_rate":
            interview_completion_rate,

        "search_appearance":
            search_appearance,

        "saved_by_recruiters":
            saved_by_recruiters,

        "verified_email":
            verified_email,

        "verified_phone":
            verified_phone,

        "linkedin_connected":
            linkedin_connected,

        "profile_completeness":
            profile_completeness,

    }