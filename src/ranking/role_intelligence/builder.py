"""
Role Intelligence Builder.

Converts a raw Job Description into a
structured representation.
"""

from src.ranking.role_intelligence.parser import (
    parse_job_description,
)


def build_role_intelligence(
    jd: str,
) -> dict:
    """
    Build structured Job Description.
    """

    parsed = parse_job_description(jd)

    return {

        "raw_jd":
            jd,

        "normalized_text":
            parsed["normalized_text"],

        "role":
            parsed["role"],

        "skills":
            parsed["skills"],

        "min_experience":
            parsed["min_experience"],

        "location":
            parsed["location"],

        "work_mode":
            parsed["work_mode"],

        "employment_type":
            parsed["employment_type"],

    }