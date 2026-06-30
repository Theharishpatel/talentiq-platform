"""
JD Parsing Engine.

Converts raw job description into a structured format
that downstream ranking components can consume.
"""

import re

from src.ranking.role_intelligence.metadata import (
    ROLE_ALIASES,
    SKILL_ALIASES,
)


# ----- Helpers -----

def normalize_text(
    text: str,
) -> str:

    text = text.lower()

    text = re.sub(
        r"[^a-z0-9+#./ ]",
        " ",
        text,
    )

    text = re.sub(
        r"\s+",
        " ",
        text,
    )

    return text.strip()


# ----- Role Extraction ------

def extract_role(
    jd: str,
) -> str | None:

    text = normalize_text(jd)

    for alias, canonical in ROLE_ALIASES.items():

        if alias in text:

            return canonical

    return None


# ------ Skill Extraction -----

def extract_skills(
    jd: str,
) -> list[str]:

    text = normalize_text(jd)

    found = set()

    for alias, canonical in SKILL_ALIASES.items():

        pattern = rf"\b{re.escape(alias.lower())}\b"

        if re.search(pattern, text):

            found.add(canonical)

    return sorted(found)


# ----- Experience Extraction -----

EXPERIENCE_REGEX = re.compile(

    r"(\d+)\s*\+?\s*(?:years|year|yrs|yr)",

    re.IGNORECASE,

)


def extract_min_experience(
    jd: str,
) -> int | None:

    matches = EXPERIENCE_REGEX.findall(jd)

    if not matches:

        return None

    return min(

        int(x)

        for x in matches

    )


# ----- Work Mode ------

def extract_work_mode(
    jd: str,
) -> str | None:

    text = normalize_text(jd)

    if "remote" in text:

        return "remote"

    if "hybrid" in text:

        return "hybrid"

    if "onsite" in text:

        return "onsite"

    return None


# ----- Employment Type -----

def extract_employment_type(
    jd: str,
) -> str | None:

    text = normalize_text(jd)

    if "full time" in text:

        return "full_time"

    if "contract" in text:

        return "contract"

    if "intern" in text:

        return "internship"

    if "part time" in text:

        return "part_time"

    return None


# ----- Location -----

LOCATION_REGEX = re.compile(

    r"(bangalore|bengaluru|hyderabad|pune|mumbai|delhi|gurgaon|noida|chennai)",

    re.IGNORECASE,

)


def extract_location(
    jd: str,
) -> str |None:

    match = LOCATION_REGEX.search(jd)

    if not match:

        return None

    return match.group(1).lower()


# ------ Main Parser -----

def parse_job_description(
    jd: str,
) -> dict:

    return {

        "role": extract_role(jd),

        "skills": extract_skills(jd),

        "min_experience": extract_min_experience(jd),

        "location": extract_location(jd),

        "work_mode": extract_work_mode(jd),

        "employment_type": extract_employment_type(jd),

        "normalized_text": normalize_text(jd),

    }