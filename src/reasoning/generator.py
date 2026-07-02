"""
Reason generator.

Generate recruiter-friendly
explanations for a single
candidate based on the
ranking score breakdown.
"""

import random

from src.reasoning.templates import *


def choose(
    templates,
    seed=None,
):
    """
    Deterministic template selection.
    """

    if seed is None:

        return random.choice(
            templates
        )

    index = abs(

        hash(str(seed))

    ) % len(templates)

    return templates[index]


def format_skills(

    skills,

):

    if not skills:

        return None

    if isinstance(

        skills,

        str,

    ):

        skills = [

            s.strip()

            for s in skills.split(",")

            if s.strip()

        ]

    priority = [

        "Python",

        "Java",

        "JavaScript",

        "React",

        "Node.js",

        "SQL",

        "Docker",

        "Kubernetes",

        "AWS",

        "Azure",

        "GCP",

    ]

    ordered = []

    for p in priority:

        if p in skills:

            ordered.append(

                p

            )

    for skill in skills:

        if skill not in ordered:

            ordered.append(

                skill

            )

    return ", ".join(

        ordered[:4]

    )


def add_highlight(highlights, text):

    """
    Avoid duplicate highlights.
    """

    if text and text not in highlights:
        highlights.append(text)


def build_explanation(
    summary: str,
    highlights: list[str],
) -> str:
    """
    Build a recruiter-friendly
    explanation.
    """

    explanation = summary.rstrip(".")

    if highlights:

        explanation += ". "

        explanation += " ".join(

            h.rstrip(".") + "."

            for h in highlights

        )

    return explanation


def generate_reason(
    candidate: dict,
) -> dict:
    """
    Generate reasoning for
    one ranked candidate.

    Parameters
    ----------
    candidate : dict

    Returns
    -------
    dict

        {
            "summary": str,
            "highlights": list[str]
        }
    """

    breakdown = candidate[
        "score_breakdown"
    ]

    payload = candidate[
        "payload"
    ]

    final_score = candidate[
        "final_score"
    ]

    highlights = []

    title = payload.get(
        "current_title",
        ""
    )

    company = payload.get(
        "current_company",
        ""
    )

    years = payload.get(
        "years_experience",
        0
    )

    candidate_seed = payload.get(
    "candidate_id",
    ""
    )

    skills = format_skills(

        payload.get(
            "skills",
            []
        )

    )

    # ------------------------------
    # Candidate Facts
    # ------------------------------

    # ======================================================
    # PROFILE SUMMARY
    # ======================================================

    profile = []

    if title:

        profile.append(

            f"{title}"

        )

    if company:

        if profile:

            profile[-1] += (

                f" at {company}"

            )

    if years:

        if profile:

            profile[-1] += (

                f" with {years:.1f} years of professional experience"

            )

    if profile:

        add_highlight(

            highlights,

            "Currently working as "

            + profile[0]

            + "."

        )

    if skills:

        add_highlight(

            highlights,

            f"Technical expertise includes {skills}."

        )

    # ======================================================
    # SEMANTIC MATCH
    # ======================================================

    similarity = breakdown.get("similarity", 0)

    if similarity >= 35:

        add_highlight(
            highlights,
            choose(VERY_HIGH_SIMILARITY),
        )

    elif similarity >= 30:

        add_highlight(
            highlights,
            choose(
                HIGH_SIMILARITY,
                candidate_seed,
            ),
        )

    elif similarity >= 22:

        add_highlight(
            highlights,
            choose(GOOD_SIMILARITY),
        )

    else:

        add_highlight(
            highlights,
            choose(MODERATE_SIMILARITY),
        )

    # ======================================================
    # EXPERIENCE
    # ======================================================

    exp_score = breakdown.get("experience", 0)

    if years >= 10:

        add_highlight(
            highlights,
            choose(EXPERT_EXPERIENCE),
        )

    elif exp_score >= 15:

        add_highlight(
            highlights,
            choose(HIGH_EXPERIENCE),
        )

    elif exp_score >= 10:

        add_highlight(
            highlights,
            choose(GOOD_EXPERIENCE),
        )

    elif exp_score >= 5:

        add_highlight(
            highlights,
            choose(MODERATE_EXPERIENCE),
        )

    else:

        add_highlight(
            highlights,
            choose(LIMITED_EXPERIENCE),
        )

    # ======================================================
    # RECRUITABILITY
    # ======================================================

    recruitability = payload.get(
        "recruitability_score",
        0,
    )

    if recruitability >= 90:

        add_highlight(
            highlights,
            choose(EXCELLENT_RECRUITABILITY),
        )

    elif recruitability >= 75:

        add_highlight(
            highlights,
            choose(HIGH_RECRUITABILITY),
        )

    elif recruitability >= 60:

        add_highlight(
            highlights,
            choose(GOOD_RECRUITABILITY),
        )

    elif recruitability >= 40:

        add_highlight(
            highlights,
            choose(MODERATE_RECRUITABILITY),
        )

    else:

        add_highlight(
            highlights,
            choose(LOW_RECRUITABILITY),
        )

    # ======================================================
    # GROWTH
    # ======================================================

    growth = payload.get(
        "growth_score",
        0,
    )

    if growth < 40:

        add_highlight(
            highlights,
            choose(LOW_GROWTH_CONCERN),
        )

    # ======================================================
    # BEHAVIOR
    # ======================================================

    behavior = payload.get(
        "behavior_score",
        0,
    )

    if behavior < 40:

        add_highlight(
            highlights,
            choose(LOW_BEHAVIOR_CONCERN),
        )

    # ======================================================
    # RISK
    # ======================================================

    risk = payload.get(
        "risk_score",
        100,
    )

    if risk <= 10:

        add_highlight(
            highlights,
            choose(VERY_LOW_RISK),
        )

    elif risk <= 20:

        add_highlight(
            highlights,
            choose(LOW_RISK),
        )

    elif risk <= 45:

        add_highlight(
            highlights,
            choose(MEDIUM_RISK),
        )

    elif risk <= 70:

        add_highlight(
            highlights,
            choose(HIGH_RISK),
        )

    else:

        add_highlight(
            highlights,
            choose(VERY_HIGH_RISK),
        )

        add_highlight(
            highlights,
            choose(HIGH_RISK_CONCERN),
        )

    # ======================================================
    # OPEN TO WORK
    # ======================================================

    if payload.get(
        "open_to_work",
        False,
    ):

        add_highlight(
            highlights,
            choose(OPEN_TO_WORK),
        )

    # ======================================================
    # SHUFFLE
    # ======================================================

    profile = highlights[:4]

    remaining = highlights[4:]

    random.shuffle(
        remaining
    )

    highlights = profile + remaining

    # ======================================================
    # SUMMARY
    # ======================================================

    if final_score >= 90:

        summary = choose(
            EXCELLENT_MATCH
        )

    elif final_score >= 80:

        summary = choose(
            STRONG_MATCH
        )

    elif final_score >= 70:

        summary = choose(
            GOOD_MATCH
        )

    else:

        summary = choose(
            MODERATE_MATCH
        )

    return {

        "summary": summary,

        "highlights": highlights,

        "explanation": build_explanation(

            summary,

            highlights,

        ),

    }