"""
Honeypot / Fraud Risk Scorer.
"""

from src.features.scoring import percentile_score


def score_honeypot_features(
    features: dict,
) -> dict:

    risk_score = 0

    salary_per_year = features.get(
        "salary_per_year",
        0,
    )

    skill_count = features.get(
        "skill_count",
        0,
    )

    experience_ratio = features.get(
        "experience_ratio",
        0,
    )

    avg_job_duration = features.get(
        "avg_job_duration",
        0,
    )

    recruiter_response_rate = features.get(
        "recruiter_response_rate",
        0,
    )

    profile_completeness = features.get(
        "profile_completeness",
        0,
    )

    verified_email = features.get(
        "verified_email",
        False,
    )

    verified_phone = features.get(
        "verified_phone",
        False,
    )

    linkedin_connected = features.get(
        "linkedin_connected",
        False,
    )

    # ----- Flags -----

    salary_anomaly = salary_per_year > 15

    skill_stuffing = skill_count > 20

    experience_mismatch = (
        experience_ratio < 0.70
        or experience_ratio > 1.30
    )

    job_hopper = (
        avg_job_duration > 0
        and avg_job_duration < 12
    )

    # ----- Risk Score ------

    if salary_anomaly:
        risk_score += 25

    if skill_stuffing:
        risk_score += 20

    if experience_mismatch:
        risk_score += 20

    if job_hopper:
        risk_score += 15

    if recruiter_response_rate < 0.10:
        risk_score += 10

    if profile_completeness < 50:
        risk_score += 5

    if not verified_email:
        risk_score += 3

    if not verified_phone:
        risk_score += 3

    if not linkedin_connected:
        risk_score += 2

    risk_score = min(
        risk_score,
        100,
    )

    # ----- Trust Score ----

    trust_score = round(
        100 - risk_score,
        2,
    )

    # ----- Risk Level -----

    if risk_score >= 60:

        risk_level = "HIGH"

    elif risk_score >= 30:

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

        "risk_score":
            risk_score,

        "trust_score":
            trust_score,

        "risk_level":
            risk_level,

    }