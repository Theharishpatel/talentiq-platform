"""
Candidate cleaning logic.
"""

from copy import deepcopy

from src.cleaning.rules import (
    clean_string,
)

from src.cleaning.skill_cleaner import (
    clean_skills,
)

from src.cleaning.signal_cleaner import (
    clean_signals,
)

from src.cleaning.title_cleaner import (
    clean_title,
)

from src.cleaning.location_cleaner import (
    clean_location,
)


def clean_candidate(
    candidate: dict,
) -> dict:

    candidate = deepcopy(
        candidate
    )

    profile = candidate.get(
        "profile",
        {}
    )

    if "headline" in profile:
        profile["headline"] = clean_string(
            profile["headline"]
        )

    if "summary" in profile:
        profile["summary"] = clean_string(
            profile["summary"]
        )

    if "current_title" in profile:
        profile["current_title"] = (
            clean_title(
                profile["current_title"]
            )
        )

    if "location" in profile:
        profile["location"] = (
            clean_location(
                profile["location"]
            )
        )

    candidate["skills"] = (
        clean_skills(
            candidate.get(
                "skills",
                []
            )
        )
    )

    candidate["redrob_signals"] = (
        clean_signals(
            candidate.get(
                "redrob_signals",
                {}
            )
        )
    )

    return candidate