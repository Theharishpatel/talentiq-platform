"""
Honeypot / Fraud Risk Features.
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

    risk_score = 0

    # ----- salary anomaly -----

    years_exp = profile.get(
        "years_of_experience",
        0
    )

    salary = preferences.get(
        "desired_salary"
    )

    salary_anomaly = False

    if (
        salary
        and years_exp > 0
    ):

        salary_ratio = (
            salary /
            years_exp
        )

        if salary_ratio > 15:

            salary_anomaly = True

            risk_score += 25

    # ----- skill stuffing ------

    skill_count = len(
        skills
    )

    skill_stuffing = False

    if skill_count > 20:

        skill_stuffing = True

        risk_score += 20

    # ------ experience mismatch ------

    total_months = 0

    for job in jobs:

        duration = job.get(
            "duration_months"
        )

        if duration:

            total_months += duration

    career_years = (
        total_months / 12
    )

    experience_mismatch = False

    if years_exp > 0:

        ratio = (
            career_years /
            years_exp
        )

        if (
            ratio < 0.50
            or ratio > 1.50
        ):

            experience_mismatch = True

            risk_score += 25

    # ------ job hopper ------

    durations = []

    for job in jobs:

        duration = job.get(
            "duration_months"
        )

        if duration is not None:

            durations.append(
                duration
            )

    avg_job_duration = (
        mean(durations)
        if durations
        else 0
    )

    job_hopper = False

    if (
        avg_job_duration > 0
        and avg_job_duration < 12
    ):

        job_hopper = True

        risk_score += 15

    # ---- inactive profile -----

    last_active_days = signals.get(
        "last_active_days",
        0
    )

    response_rate = signals.get(
        "recruiter_response_rate",
        0
    )

    inactive_profile = False

    if (
        last_active_days > 200
        and response_rate < 0.10
    ):

        inactive_profile = True

        risk_score += 15

    # ---- risk level ----

    if risk_score >= 51:

        risk_level = "HIGH"

    elif risk_score >= 21:

        risk_level = "MEDIUM"

    else:

        risk_level = "LOW"

    return {

        "salary_anomaly":
            salary_anomaly,

        "skill_stuffing":
            skill_stuffing,

        "experience_mismatch":
            experience_mismatch,

        "job_hopper":
            job_hopper,

        "inactive_profile":
            inactive_profile,

        "risk_score":
            risk_score,

        "risk_level":
            risk_level,

        "skill_count":
            skill_count,

        "career_years":
            round(
                career_years,
                2
            ),

        "avg_job_duration":
            round(
                avg_job_duration,
                2
            ),
    }