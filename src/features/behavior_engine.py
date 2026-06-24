"""
Behavior scoring engine.
"""

from datetime import datetime

from src.features.scoring import (
    percentile_score,
    reverse_percentile_score,
)


TODAY = datetime.strptime(
    "2026-05-27",
    "%Y-%m-%d",
)


def build_behavior_features(
    candidate: dict,
) -> dict:

    signals = candidate.get(
        "redrob_signals",
        {}
    )

    # ----- Raw Features ----- 

    last_active = signals.get(
        "last_active_date"
    )

    if last_active:

        days_since_active = (
            TODAY
            - datetime.strptime(
                last_active,
                "%Y-%m-%d"
            )
        ).days

    else:
        days_since_active = 999

    response_rate = signals.get(
        "recruiter_response_rate",
        0,
    )

    response_time = signals.get(
        "avg_response_time_hours",
        999,
    )

    applications = signals.get(
        "applications_submitted_30d",
        0,
    )

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

    interview_rate = signals.get(
        "interview_completion_rate",
        0,
    )

    offer_rate = signals.get(
        "offer_acceptance_rate"
    )

    # ------ Activity Scores ------

    activity_recency_score = (
        reverse_percentile_score(
            days_since_active,
            p25=52,
            p50=105,
            p75=162,
            p90=206,
        )
    )

    application_score = (
        percentile_score(
            applications,
            p25=2,
            p50=5,
            p75=8,
            p90=10,
        )
    )

    activity_score = (
        activity_recency_score * 0.60
        + application_score * 0.40
    )

    # ------ Responsiveness Scores ------

    response_rate_score = (
        percentile_score(
            response_rate,
            p25=0.25,
            p50=0.44,
            p75=0.62,
            p90=0.73,
        )
    )

    response_time_score = (
        reverse_percentile_score(
            response_time,
            p25=68.3,
            p50=129.9,
            p75=193.3,
            p90=240.4,
        )
    )

    responsiveness_score = (
        response_rate_score * 0.60
        + response_time_score * 0.40
    )

    # ------ Market Interest Scores ----- 

    views_score = (
        percentile_score(
            views,
            p25=23,
            p50=45,
            p75=68,
            p90=86,
        )
    )

    search_score = (
        percentile_score(
            searches,
            p25=52,
            p50=105,
            p75=158,
            p90=226,
        )
    )

    saved_score = (
        percentile_score(
            saved,
            p25=3,
            p50=7,
            p75=11,
            p90=15,
        )
    )

    market_interest_score = (
        views_score * 0.30
        + search_score * 0.30
        + saved_score * 0.40
    )

    # ------- Reliability Scores ----

    interview_score = (
        percentile_score(
            interview_rate,
            p25=0.48,
            p50=0.62,
            p75=0.76,
            p90=0.85,
        )
    )

    if offer_rate is None:

        offer_score = 50

    else:

        offer_score = (
            percentile_score(
                offer_rate,
                p25=0.32,
                p50=0.48,
                p75=0.63,
                p90=0.72,
            )
        )

    reliability_score = (
        interview_score * 0.70
        + offer_score * 0.30
    )

    # ------ Final Behavior Score ------

    behavior_score = round(
        (
            activity_score * 0.30
            + responsiveness_score * 0.30
            + market_interest_score * 0.20
            + reliability_score * 0.20
        ),
        2,
    )

    return {

        # Raw Features

        "days_since_active":
            days_since_active,

        "response_rate":
            response_rate,

        "response_time":
            response_time,

        "applications":
            applications,

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

        # Component Scores

        "activity_score":
            round(
                activity_score,
                2,
            ),

        "responsiveness_score":
            round(
                responsiveness_score,
                2,
            ),

        "market_interest_score":
            round(
                market_interest_score,
                2,
            ),

        "reliability_score":
            round(
                reliability_score,
                2,
            ),

        # Final

        "behavior_score":
            behavior_score,
    }