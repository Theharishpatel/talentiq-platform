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

# ==========================================================
# SUMMARY TEMPLATES
# ==========================================================

EXCELLENT_MATCH = [

    "Excellent overall fit with the job requirements, supported by strong technical alignment and consistently positive hiring signals.",

    "Outstanding candidate with a strong balance of relevant experience, semantic relevance, and hiring readiness.",

    "Highly recommended candidate demonstrating exceptional overall suitability for the role.",

    "Top-tier profile showing excellent alignment across experience, technical relevance, and overall candidate quality.",

]

STRONG_MATCH = [

    "Strong overall match with the job requirements and positive hiring indicators.",

    "Well-qualified candidate with relevant experience and consistently strong evaluation signals.",

    "Strong candidate profile with good technical relevance and hiring potential.",

    "Highly suitable candidate expected to perform well in the target role.",

]

GOOD_MATCH = [

    "Good overall fit with the role and satisfies most evaluation criteria.",

    "Candidate demonstrates relevant qualifications with several positive hiring signals.",

    "Solid candidate profile with good potential for the position.",

    "Suitable candidate matching most of the important hiring requirements.",

]

MODERATE_MATCH = [

    "Reasonable fit for the role, although additional evaluation is recommended.",

    "Candidate satisfies several important hiring requirements but also presents areas for further assessment.",

    "Moderate overall suitability with a balanced mix of strengths and improvement areas.",

    "Potentially suitable candidate requiring additional recruiter validation.",

]


# ==========================================================
# SEMANTIC MATCH
# ==========================================================

VERY_HIGH_SIMILARITY = [

    "Profile aligns exceptionally well with the responsibilities of the target role.",

    "Candidate demonstrates outstanding alignment with the expected role requirements.",

    "Professional background closely matches the target position.",

]

HIGH_SIMILARITY = [

    "Profile aligns strongly with the responsibilities of the target role.",

    "Professional experience closely matches the expectations of the position.",

    "Candidate demonstrates strong overall role alignment.",

]

GOOD_SIMILARITY = [

    "Profile shows good alignment with the responsibilities of the target role.",

    "Professional background is relevant to the expected role.",

    "Candidate satisfies many of the important role expectations.",

]

MODERATE_SIMILARITY = [

    "Profile partially aligns with the responsibilities of the target role.",

    "Candidate demonstrates reasonable alignment with the position.",

]


# ==========================================================
# EXPERIENCE
# ==========================================================

EXPERT_EXPERIENCE = [

    "Extensive professional experience strengthens suitability for senior responsibilities.",

    "Highly experienced candidate with a mature professional background.",

]

HIGH_EXPERIENCE = [

    "Strong professional experience supports this recommendation.",

    "Relevant industry experience contributes positively to the ranking.",

    "Experience profile aligns well with expected responsibilities.",

]

GOOD_EXPERIENCE = [

    "Possesses solid professional experience relevant to the position.",

    "Experience demonstrates practical exposure to similar responsibilities.",

]

MODERATE_EXPERIENCE = [

    "Experience is adequate but may benefit from further technical validation.",

]

LIMITED_EXPERIENCE = [

    "Professional experience appears relatively limited for highly senior responsibilities.",

]


# ==========================================================
# RECRUITABILITY
# ==========================================================

EXCELLENT_RECRUITABILITY = [

    "Excellent recruitability score further strengthens this recommendation.",

    "High hiring readiness makes this candidate immediately attractive for recruitment.",

    "Excellent recruitability reflects strong overall hiring potential.",

]

HIGH_RECRUITABILITY = [

    "High recruitability score strengthens the overall recommendation.",

    "Strong hiring readiness supports this candidate profile.",

    "Recruitability indicators reinforce overall suitability for the role.",

]

GOOD_RECRUITABILITY = [

    "Good recruitability supports the hiring recommendation.",

    "Overall hiring readiness is positive.",

    "Recruitability profile contributes positively to the final recommendation.",

]

MODERATE_RECRUITABILITY = [

    "Recruitability indicators are acceptable but not exceptional.",

]

LOW_RECRUITABILITY = [

    "Recruitability indicators suggest additional recruiter assessment.",

]


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


# ==========================================================
# RISK
# ==========================================================

VERY_LOW_RISK = [

    "Very low hiring risk further strengthens this recommendation.",

    "Minimal hiring risk supports confidence in the candidate profile.",

    "Risk indicators suggest a highly dependable candidate.",

]

LOW_RISK = [

    "Low hiring risk strengthens the overall recommendation.",

    "Risk profile supports confident hiring decisions.",

    "The candidate demonstrates a stable and low-risk professional profile.",

]

MEDIUM_RISK = [

    "Moderate hiring risk suggests additional recruiter evaluation.",

    "Some hiring risks should be validated during interviews.",

]

HIGH_RISK = [

    "Higher hiring risk indicates additional assessment is recommended.",

    "Recruiters may wish to further evaluate potential hiring risks.",

]

VERY_HIGH_RISK = [

    "Elevated hiring risk suggests careful recruiter review before proceeding.",

]


# ==========================================================
# OPEN TO WORK
# ==========================================================

OPEN_TO_WORK = [

    "Candidate is currently open to new opportunities.",

    "Availability for new opportunities may support faster hiring.",

    "Open-to-work status increases near-term hiring potential.",

]


# ---- FALLBACK ----

NO_REASON = (
    "Candidate satisfies the minimum selection criteria."
)


# ==========================================================
# CONCERNS
# ==========================================================

LOW_EXPERIENCE_CONCERN = [

    "Professional experience may be limited for highly senior positions.",

]

HIGH_RISK_CONCERN = [

    "Risk indicators suggest additional interview validation.",

]

LOW_GROWTH_CONCERN = [

    "Career progression appears relatively moderate.",

]

LOW_BEHAVIOR_CONCERN = [

    "Employment history may require additional review.",

]