"""
Reasoning templates.

This module contains reusable
natural language templates
used for explaining why a
candidate was recommended.

No business logic should be
implemented here.
"""


# ----- SUMMARY TEMPLATES ------

EXCELLENT_MATCH = (
    "Excellent overall match for the job requirements."
)

STRONG_MATCH = (
    "Strong overall match for the job requirements."
)

GOOD_MATCH = (
    "Good match for the job requirements."
)

MODERATE_MATCH = (
    "Moderate match for the job requirements."
)


# ----- SEMANTIC MATCH -----

HIGH_SIMILARITY = (
    "Excellent semantic match with the job description."
)

GOOD_SIMILARITY = (
    "Good semantic alignment with the required role."
)


# ----- EXPERIENCE -----

HIGH_EXPERIENCE = (
    "Strong relevant professional experience."
)

GOOD_EXPERIENCE = (
    "Relevant industry experience."
)


# ----- RECRUITABILITY -----

HIGH_RECRUITABILITY = (
    "Highly recruitable candidate."
)

GOOD_RECRUITABILITY = (
    "Good recruitability profile."
)


# ----- CAREER GROWTH -----

HIGH_GROWTH = (
    "Demonstrates strong career progression."
)

GOOD_GROWTH = (
    "Shows positive career growth."
)


# ------ BEHAVIOR ------

HIGH_BEHAVIOR = (
    "Positive employment behavior."
)

GOOD_BEHAVIOR = (
    "Stable employment history."
)


# ----- CONSISTENCY -----

HIGH_CONSISTENCY = (
    "Consistent career progression."
)

GOOD_CONSISTENCY = (
    "Maintains a stable career path."
)


# ----- RISK ----

LOW_RISK = (
    "Low hiring risk profile."
)

MEDIUM_RISK = (
    "Acceptable hiring risk profile."
)

HIGH_RISK = (
    "Some hiring risks were identified."
)


# ---- OPEN TO WORK -----

OPEN_TO_WORK = (
    "Currently open to new opportunities."
)


# ---- FALLBACK ----

NO_REASON = (
    "Candidate satisfies the minimum selection criteria."
)