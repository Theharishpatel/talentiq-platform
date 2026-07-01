"""
Reasoning engine.

Generate recruiter-friendly
reasoning for all ranked
candidates.
"""

from src.reasoning.generator import (
    generate_reason,
)


def generate_reasons(
    candidates: list[dict],
) -> list[dict]:
    """
    Generate reasoning for all
    ranked candidates.

    Parameters
    ----------
    candidates : list[dict]

    Returns
    -------
    list[dict]
    """

    enriched_candidates = []

    for candidate in candidates:

        candidate["reasoning"] = (

            generate_reason(
                candidate
            )

        )

        enriched_candidates.append(
            candidate
        )

    return enriched_candidates