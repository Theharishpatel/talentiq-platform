"""
Behavior feature extraction engine.
"""

from datetime import datetime

from src.features.behavior.constants import (
    PIPELINE_DATE,
)


def build_behavior_features(
    candidate: dict,
) -> dict:

    signals = candidate.get(
        "redrob_signals",
        {}
    )

    # ----- Activity -----

    last_active = signals.get(
        "last_active_date"
    )

    if last_active:

        days_since_active = (

            PIPELINE_DATE

            - datetime.strptime(

                last_active,

                "%Y-%m-%d",

            )

        ).days

    else:

        days_since_active = 999

    applications = signals.get(
        "applications_submitted_30d",
        0,
    )

    # ---- Responsiveness ----

    response_rate = signals.get(
        "recruiter_response_rate",
        0,
    )

    response_time = signals.get(
        "avg_response_time_hours",
        999,
    )

    # ----- Market Interest ----

    views = signals.get(
        "profile_views_received_30d",
        0,
    )

    searches = signals.get(
        "search_appearance_30d",
        0,
    )

    saved = signals.get(
        "saved_by_recruiters_30d",
        0,
    )

    # ---- Reliability ----

    interview_rate = signals.get(
        "interview_completion_rate",
        0,
    )

    offer_rate = signals.get(
        "offer_acceptance_rate"
    )

    # ----- Return Raw Features ----

    return {

        "days_since_active":
            days_since_active,

        "applications":
            applications,

        "response_rate":
            response_rate,

        "response_time":
            response_time,

        "views":
            views,

        "searches":
            searches,

        "saved":
            saved,

        "interview_rate":
            interview_rate,

        "offer_rate":
            offer_rate,

    }