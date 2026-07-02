"""
Recruitability scoring engine.
"""

from src.features.scoring import (
    percentile_score,
    reverse_percentile_score,
)


def score_recruitability_features(
    features: dict,
) -> dict:

    # ----- Raw Features -----

    open_to_work = features[
        "open_to_work"
    ]

    notice_period = features[
        "notice_period"
    ]

    verified_email = features[
        "verified_email"
    ]

    verified_phone = features[
        "verified_phone"
    ]

    linkedin_connected = features[
        "linkedin_connected"
    ]

    profile_completeness_score = features[
        "profile_completeness_score"
    ]

    github_activity_score = features[
        "github_activity_score"
    ]

    connection_count = features[
        "connection_count"
    ]

    willing_to_relocate = features[
        "willing_to_relocate"
    ]

    preferred_work_mode = features[
        "preferred_work_mode"
    ]

    salary_ratio = features[
        "salary_ratio"
    ]

    # ----- Availability -----

    open_to_work_score = (

        100

        if open_to_work

        else 25

    )

    notice_score = (

        reverse_percentile_score(

            notice_period,

            p25=60,
            p50=90,
            p75=120,
            p90=150,

        )

    )

    availability_score = round(

        open_to_work_score * 0.70

        +

        notice_score * 0.30,

        2,

    )

    # ---- Verification ----- 

    email_score = (

        100

        if verified_email

        else 0

    )

    phone_score = (

        100

        if verified_phone

        else 0

    )

    linkedin_score = (

        100

        if linkedin_connected

        else 0

    )

    completeness_score = (

        percentile_score(

            profile_completeness_score,

            p25=55,
            p50=70,
            p75=82,
            p90=92,

        )

    )

    verification_score = round(

        email_score * 0.30

        +

        phone_score * 0.30

        +

        linkedin_score * 0.20

        +

        completeness_score * 0.20,

        2,

    )

    # ----- Technical Presence -----

    if github_activity_score < 0:

        github_score = 0

    else:

        github_score = percentile_score(

            github_activity_score,

            p25=2,
            p50=5,
            p75=7,
            p90=9,

        )

    connection_score = percentile_score(

        connection_count,

        p25=90,
        p50=180,
        p75=320,
        p90=520,

    )

    technical_presence_score = round(

        github_score * 0.60

        +

        connection_score * 0.40,

        2,

    )

    # ----- Mobility -----

    relocate_score = (

        100

        if willing_to_relocate

        else 50

    )

    work_mode_scores = {

        "flexible": 100,

        "hybrid": 90,

        "remote": 80,

        "onsite": 75,

    }

    work_mode_score = work_mode_scores.get(

        preferred_work_mode,

        75,

    )

    mobility_score = round(

        relocate_score * 0.40

        +

        work_mode_score * 0.60,

        2,

    )

    # ----- Salary ----

    if salary_ratio is None:

        salary_score = 50

    elif salary_ratio <= 1.5:

        salary_score = 70

    elif salary_ratio <= 4.5:

        salary_score = 100

    elif salary_ratio <= 7.5:

        salary_score = 80

    else:

        salary_score = 50

    # ----- Final Recruitability Score -----

    recruitability_score = round(

        availability_score * 0.35

        +

        verification_score * 0.25

        +

        technical_presence_score * 0.20

        +

        mobility_score * 0.10

        +

        salary_score * 0.10,

        2,

    )

    # ----- Return -----

    return {

        "availability_score":
            availability_score,

        "verification_score":
            verification_score,

        "technical_presence_score":
            technical_presence_score,

        "mobility_score":
            mobility_score,

        "salary_score":
            salary_score,

        "recruitability_score":
            recruitability_score,

    }