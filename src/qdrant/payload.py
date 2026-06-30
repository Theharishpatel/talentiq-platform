"""
Qdrant payload builder.
"""

from typing import Any
import numpy as np


def serialize(value: Any) -> Any:
    """
    Convert NumPy values into native Python values.
    """

    if isinstance(value, np.ndarray):
        return value.astype(object).tolist()

    if isinstance(value, np.generic):
        return value.item()

    if isinstance(value, tuple):
        return list(value)

    return value


def build_payload(candidate: dict) -> dict[str, Any]:

    payload = {
        "candidate_id": candidate["candidate_id"],
        "headline": candidate["headline"],
        "current_title": candidate["current_title"],
        "current_company": candidate["current_company"],
        "current_industry": candidate["current_industry"],
        "location": candidate["location"],
        "country": candidate["country"],
        "years_experience": candidate["years_experience"],
        "skills": candidate["skills"],
        "open_to_work": candidate["open_to_work"],
        "experience_score": candidate["experience_score"],
        "behavior_score": candidate["behavior_score"],
        "growth_score": candidate["growth_score"],
        "recruitability_score": candidate["recruitability_score"],
        "consistency_score": candidate["consistency_score"],
        "risk_score": candidate["risk_score"],
    }

    return {
        key: serialize(value)
        for key, value in payload.items()
    }