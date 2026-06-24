"""
Recruitability scoring engine.
"""

from src.features.scoring import (
    reverse_percentile_score,
)


def build_recruitability_features(
    candidate: dict,
) -> dict:

    profile = candidate.get(
        "profile",
        {}
    )

    signals = candidate.get(
        "redrob_signals",
        {}
    )

    # ------ Availability -------

    open_to_work = signals.get(
        "open_to_work_flag",
        False,
    )

    notice_period = signals.get(
        "notice_period_days",
        150,
    )

    open_to_work_score = (
        100 if open_to_work else 25
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

    availability_score = (
        open_to_work_score * 0.70
        + notice_score * 0.30
    )

    # ----- Verification ------

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

    email_score = (
        100 if verified_email else 0
    )

    phone_score = (
        100 if verified_phone else 0
    )

    linkedin_score = (
        100 if linkedin_connected else 0
    )

    verification_score = (
        email_score * 0.40
        + phone_score * 0.40
        + linkedin_score * 0.20
    )

    # ------ Mobility -----

    willing_to_relocate = signals.get(
        "willing_to_relocate",
        False,
    )

    preferred_work_mode = signals.get(
        "preferred_work_mode",
        "onsite",
    )

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

    work_mode_score = (
        work_mode_scores.get(
            preferred_work_mode,
            75,
        )
    )

    mobility_score = (
        relocate_score * 0.40
        + work_mode_score * 0.60
    )

    # ----- Salary Realism ------

    salary = signals.get(
        "expected_salary_range_inr_lpa",
        {},
    )

    salary_min = salary.get("min")
    salary_max = salary.get("max")

    salary_ratio = None

    years_exp = profile.get(
        "years_of_experience",
        0,
    )

    if (
        salary_min is not None
        and salary_max is not None
        and years_exp > 0
    ):

        midpoint = (
            salary_min
            + salary_max
        ) / 2

        salary_ratio = (
            midpoint
            / years_exp
        )

        if salary_ratio <= 1.37:

            salary_score = 70

        elif salary_ratio <= 4.37:

            salary_score = 100

        elif salary_ratio <= 7.69:

            salary_score = 80

        else:

            salary_score = 50

    else:

        salary_score = 50

    # ------ Final Recruitability Score -----

    recruitability_score = round(
        (
            availability_score * 0.40
            + verification_score * 0.25
            + mobility_score * 0.15
            + salary_score * 0.20
        ),
        2,
    )

    return {

        "open_to_work":
            open_to_work,

        "notice_period":
            notice_period,

        "availability_score":
            round(
                availability_score,
                2,
            ),

        "verification_score":
            round(
                verification_score,
                2,
            ),

        "mobility_score":
            round(
                mobility_score,
                2,
            ),

        "salary_ratio":
            round(
                salary_ratio,
                2,
            )
            if salary_ratio
            else None,

        "salary_score":
            salary_score,

        "recruitability_score":
            recruitability_score,
    }