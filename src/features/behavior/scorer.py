"""
Behavior scoring engine.
"""

from src.features.scoring import (
    percentile_score,
    reverse_percentile_score,
)

from src.features.behavior.constants import (

    ACTIVITY_RECENCY,
    APPLICATIONS,

    RESPONSE_RATE,
    RESPONSE_TIME,

    PROFILE_VIEWS,
    SEARCH_APPEARANCE,
    SAVED_BY_RECRUITERS,

    INTERVIEW_RATE,
    OFFER_RATE,

    ACTIVITY_SCORE_WEIGHT,
    RESPONSIVENESS_SCORE_WEIGHT,
    MARKET_INTEREST_WEIGHT,
    RELIABILITY_WEIGHT,

    ACTIVITY_RECENCY_WEIGHT,
    APPLICATION_WEIGHT,

    RESPONSE_RATE_WEIGHT,
    RESPONSE_TIME_WEIGHT,

    PROFILE_VIEW_WEIGHT,
    SEARCH_WEIGHT,
    SAVED_WEIGHT,

    INTERVIEW_WEIGHT,
    OFFER_WEIGHT,

)


def score_behavior_features(
    features: dict,
) -> dict:

    # ----- Raw Features ----

    days_since_active = features[
        "days_since_active"
    ]

    applications = features[
        "applications"
    ]

    response_rate = features[
        "response_rate"
    ]

    response_time = features[
        "response_time"
    ]

    views = features[
        "views"
    ]

    searches = features[
        "searches"
    ]

    saved = features[
        "saved"
    ]

    interview_rate = features[
        "interview_rate"
    ]

    offer_rate = features[
        "offer_rate"
    ]

    # ---- Activity ----

    activity_recency_score = (

        reverse_percentile_score(

            days_since_active,

            **ACTIVITY_RECENCY,

        )

    )

    application_score = (

        percentile_score(

            applications,

            **APPLICATIONS,

        )

    )

    activity_score = round(

        activity_recency_score
        * ACTIVITY_RECENCY_WEIGHT

        +

        application_score
        * APPLICATION_WEIGHT,

        2,

    )

    # ---- Responsiveness -----

    response_rate_score = (

        percentile_score(

            response_rate,

            **RESPONSE_RATE,

        )

    )

    response_time_score = (

        reverse_percentile_score(

            response_time,

            **RESPONSE_TIME,

        )

    )

    responsiveness_score = round(

        response_rate_score
        * RESPONSE_RATE_WEIGHT

        +

        response_time_score
        * RESPONSE_TIME_WEIGHT,

        2,

    )

    # ----- Market Interest ----

    views_score = (

        percentile_score(

            views,

            **PROFILE_VIEWS,

        )

    )

    search_score = (

        percentile_score(

            searches,

            **SEARCH_APPEARANCE,

        )

    )

    saved_score = (

        percentile_score(

            saved,

            **SAVED_BY_RECRUITERS,

        )

    )

    market_interest_score = round(

        views_score
        * PROFILE_VIEW_WEIGHT

        +

        search_score
        * SEARCH_WEIGHT

        +

        saved_score
        * SAVED_WEIGHT,

        2,

    )

    # ---- Reliability ----

    interview_score = (

        percentile_score(

            interview_rate,

            **INTERVIEW_RATE,

        )

    )

    if offer_rate is None:

        offer_score = 50

    else:

        offer_score = (

            percentile_score(

                offer_rate,

                **OFFER_RATE,

            )

        )

    reliability_score = round(

        interview_score
        * INTERVIEW_WEIGHT

        +

        offer_score
        * OFFER_WEIGHT,

        2,

    )

    # ---- Final Score ----

    behavior_score = round(

        activity_score
        * ACTIVITY_SCORE_WEIGHT

        +

        responsiveness_score
        * RESPONSIVENESS_SCORE_WEIGHT

        +

        market_interest_score
        * MARKET_INTEREST_WEIGHT

        +

        reliability_score
        * RELIABILITY_WEIGHT,

        2,

    )

    # --- Return ----

    return {

        "activity_score":
            activity_score,

        "responsiveness_score":
            responsiveness_score,

        "market_interest_score":
            market_interest_score,

        "reliability_score":
            reliability_score,

        "behavior_score":
            behavior_score,

    }