"""
Education model.
"""

from enum import Enum

from pydantic import BaseModel, Field

from .base import MODEL_CONFIG

class InstitutionTier(str, Enum):
    """
    Institution quality tier.
    """

    TIER_1 = "tier_1"
    TIER_2 = "tier_2"
    TIER_3 = "tier_3"
    TIER_4 = "tier_4"
    UNKNOWN = "unknown"

class Education(BaseModel):
    """
    Education qualification.
    """

    model_config = MODEL_CONFIG

    institution: str

    degree: str

    field_of_study: str

    start_year: int = Field(
        ge=1970,
        le=2035
    )

    end_year: int = Field(
        default=None,
        ge=1970,
        le=2035
    )

    grade: str | None = None

    tier: InstitutionTier = InstitutionTier.UNKNOWN

