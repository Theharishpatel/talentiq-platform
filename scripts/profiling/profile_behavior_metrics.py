from datetime import datetime
from statistics import mean, median

from src.ingestion.jsonl_reader import read_jsonl

today = datetime.strptime(
    "2026-05-27",
    "%Y-%m-%d"
)

last_active_days = []

response_rates = []
response_times = []

applications = []
profile_views = []

search_appearances = []
saved_by_recruiters = []

interview_completion_rates = []

offer_acceptance_rates = []


def percentile(values, p):

    values = sorted(values)

    index = int(
        (len(values) - 1) * p
    )

    return values[index]


for candidate in read_jsonl(
    "data/processed/clean_candidates.jsonl"
):

    signals = candidate.get(
        "redrob_signals",
        {}
    )

    # ------------------------
    # Last Active
    # ------------------------

    last_active = signals.get(
        "last_active_date"
    )

    if last_active:

        days = (
            today
            - datetime.strptime(
                last_active,
                "%Y-%m-%d"
            )
        ).days

        last_active_days.append(
            days
        )

    # ------------------------
    # Response Rate
    # ------------------------

    value = signals.get(
        "recruiter_response_rate"
    )

    if value is not None:
        response_rates.append(
            value
        )

    # ------------------------
    # Response Time
    # ------------------------

    value = signals.get(
        "avg_response_time_hours"
    )

    if value is not None:
        response_times.append(
            value
        )

    # ------------------------
    # Applications
    # ------------------------

    value = signals.get(
        "applications_submitted_30d"
    )

    if value is not None:
        applications.append(
            value
        )

    # ------------------------
    # Views
    # ------------------------

    value = signals.get(
        "profile_views_received_30d"
    )

    if value is not None:
        profile_views.append(
            value
        )

    # ------------------------
    # Search Appearance
    # ------------------------

    value = signals.get(
        "search_appearance_30d"
    )

    if value is not None:
        search_appearances.append(
            value
        )

    # ------------------------
    # Saved By Recruiters
    # ------------------------

    value = signals.get(
        "saved_by_recruiters_30d"
    )

    if value is not None:
        saved_by_recruiters.append(
            value
        )

    # ------------------------
    # Interview Completion
    # ------------------------

    value = signals.get(
        "interview_completion_rate"
    )

    if value is not None:
        interview_completion_rates.append(
            value
        )

    # ------------------------
    # Offer Acceptance
    # ------------------------

    value = signals.get(
        "offer_acceptance_rate"
    )

    if value is not None:
        offer_acceptance_rates.append(
            value
        )


def build_section(
    name,
    values
):

    return f"""
============================================================
{name}
============================================================

count   : {len(values)}
min     : {min(values)}
max     : {max(values)}
avg     : {mean(values):.2f}
median  : {median(values):.2f}

p25     : {percentile(values, 0.25)}
p50     : {percentile(values, 0.50)}
p75     : {percentile(values, 0.75)}
p90     : {percentile(values, 0.90)}
"""


report = ""

report += build_section(
    "LAST ACTIVE DAYS",
    last_active_days
)

report += build_section(
    "RECRUITER RESPONSE RATE",
    response_rates
)

report += build_section(
    "RESPONSE TIME HOURS",
    response_times
)

report += build_section(
    "APPLICATIONS SUBMITTED",
    applications
)

report += build_section(
    "PROFILE VIEWS",
    profile_views
)

report += build_section(
    "SEARCH APPEARANCE",
    search_appearances
)

report += build_section(
    "SAVED BY RECRUITERS",
    saved_by_recruiters
)

report += build_section(
    "INTERVIEW COMPLETION RATE",
    interview_completion_rates
)

report += build_section(
    "OFFER ACCEPTANCE RATE",
    offer_acceptance_rates
)

print(report)

with open(
    "data/reports/profiling/behavior_metrics_profile.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write(report)

print(
    "\nSaved: data/reports/profiling/behavior_metrics_profile.txt"
)