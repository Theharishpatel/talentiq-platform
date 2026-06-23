"""
Candidate clening logic.
"""

from copy import deepcopy

from src.cleaning.rules import (
    replace_negative_one,
    clean_string,
)

def clean_candidate(candidate: dict) -> dict:
    """
    Clean one candidate record.
    """

    candidate = deepcopy(candidate)

    #------- profile -----

    profile = candidate.get("profile", {})

    if "headline" in profile:
        profile["headline"] = clean_string(
            profile["headline"]
        )

    if "summary" in profile:
        profile["summary"] = clean_string(
            profile["summary"]
        )

    #------ skills ------
    skills = candidate.get(
        "skills",
        []
    )

    seen = set()
    cleaned_skills = []

    for skill in skills:

        name = clean_string(
            skill.get("name")
        )

        if not name:
            continue

        normalized = name.lower()

        if normalized in seen:
            continue

        seen.add(normalized)

        skill["name"] = normalized

        cleaned_skills.append(skill)

    candidate["skills"] = cleaned_skills

    #------ signals ------

    signals = candidate.get(
        "redrob_signals",
        {}
    )

    if "github_activity_score" in signals:
        signals["github_activity_score"] = (
            replace_negative_one(
                signals["github_activity_score"]
            )
        )
    return candidate  