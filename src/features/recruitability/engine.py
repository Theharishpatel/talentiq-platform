"""
Recruitability feature extraction engine.
"""


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

    # ----- Availability -----

    open_to_work = signals.get(
        "open_to_work_flag"
    )

    if open_to_work is None:
        open_to_work = False

    notice_period = signals.get(
        "notice_period_days"
    )

    if notice_period is None:
        notice_period = 150

    # ----- Verification -----

    verified_email = signals.get(
        "verified_email"
    )

    if verified_email is None:
        verified_email = False

    verified_phone = signals.get(
        "verified_phone"
    )

    if verified_phone is None:
        verified_phone = False

    linkedin_connected = signals.get(
        "linkedin_connected"
    )

    if linkedin_connected is None:
        linkedin_connected = False

    profile_completeness_score = signals.get(
        "profile_completeness_score"
    )

    if profile_completeness_score is None:
        profile_completeness_score = 0

    # ----- Technical Presence -----

    github_activity_score = signals.get(
        "github_activity_score"
    )

    if github_activity_score is None:
        github_activity_score = -1

    connection_count = signals.get(
        "connection_count"
    )

    if connection_count is None:
        connection_count = 0

    # ----- Mobility -----

    willing_to_relocate = signals.get(
        "willing_to_relocate"
    )

    if willing_to_relocate is None:
        willing_to_relocate = False

    preferred_work_mode = signals.get(
        "preferred_work_mode"
    )

    if preferred_work_mode is None:
        preferred_work_mode = "onsite"

    # ----- Salary -----

    salary = signals.get(
        "expected_salary_range_inr_lpa"
    )

    if salary is None:
        salary = {}

    salary_min = salary.get(
        "min"
    )

    salary_max = salary.get(
        "max"
    )

    years_experience = profile.get(
        "years_of_experience"
    )

    if years_experience is None:
        years_experience = 0

    salary_ratio = None

    if (
        salary_min is not None
        and salary_max is not None
        and years_experience > 0
    ):

        midpoint = (
            salary_min +
            salary_max
        ) / 2

        salary_ratio = round(
            midpoint / years_experience,
            2,
        )

    # ----- Derived Features -----

    is_verified = (
        verified_email
        and verified_phone
    )

    has_github = (
        github_activity_score >= 0
    )

    # ----- Return -----

    return {

        "open_to_work":
            open_to_work,

        "notice_period":
            notice_period,

        "verified_email":
            verified_email,

        "verified_phone":
            verified_phone,

        "linkedin_connected":
            linkedin_connected,

        "profile_completeness_score":
            profile_completeness_score,

        "github_activity_score":
            github_activity_score,

        "connection_count":
            connection_count,

        "preferred_work_mode":
            preferred_work_mode,

        "willing_to_relocate":
            willing_to_relocate,

        "salary_ratio":
            salary_ratio,

        "is_verified":
            is_verified,

        "has_github":
            has_github,

    }