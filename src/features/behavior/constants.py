"""
Behavior engine constants.

Contains:

- Pipeline reference date
- Percentile thresholds
- Component weights
"""

from datetime import datetime

# ---- Pipline Date ----

PIPELINE_DATE = datetime.strptime(
    "2026-05-27",
    "%Y-%m-%d",
)

# ---- Percentiles -----

ACTIVITY_RECENCY = {

    "p25": 52,
    "p50": 105,
    "p75": 162,
    "p90": 206,

}

APPLICATIONS = {

    "p25": 2,
    "p50": 5,
    "p75": 8,
    "p90": 10,

}

RESPONSE_RATE = {

    "p25": 0.25,
    "p50": 0.44,
    "p75": 0.62,
    "p90": 0.73,

}

RESPONSE_TIME = {

    "p25": 68.3,
    "p50": 129.9,
    "p75": 193.3,
    "p90": 240.4,

}

PROFILE_VIEWS = {

    "p25": 23,
    "p50": 45,
    "p75": 68,
    "p90": 86,

}

SEARCH_APPEARANCE = {

    "p25": 52,
    "p50": 105,
    "p75": 158,
    "p90": 226,

}

SAVED_BY_RECRUITERS = {

    "p25": 3,
    "p50": 7,
    "p75": 11,
    "p90": 15,

}

INTERVIEW_RATE = {

    "p25": 0.48,
    "p50": 0.62,
    "p75": 0.76,
    "p90": 0.85,

}

OFFER_RATE = {

    "p25": 0.32,
    "p50": 0.48,
    "p75": 0.63,
    "p90": 0.72,

}

# ----- Component Weights -----

ACTIVITY_SCORE_WEIGHT = 0.30

RESPONSIVENESS_SCORE_WEIGHT = 0.30

MARKET_INTEREST_WEIGHT = 0.20

RELIABILITY_WEIGHT = 0.20

# --- Sub Weights ----

ACTIVITY_RECENCY_WEIGHT = 0.60

APPLICATION_WEIGHT = 0.40

RESPONSE_RATE_WEIGHT = 0.60

RESPONSE_TIME_WEIGHT = 0.40

PROFILE_VIEW_WEIGHT = 0.30

SEARCH_WEIGHT = 0.30

SAVED_WEIGHT = 0.40

INTERVIEW_WEIGHT = 0.70

OFFER_WEIGHT = 0.30