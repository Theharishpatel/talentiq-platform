"""
Skill models.
"""

from enum import Enum

from pydantic import BaseModel, Field

from .base import MODEL_CONFIG

class SkillLevel(str, Enum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    EXPERT = "expert"

class Skill(BaseModel):
    """
    Candidate skill.
    """    

    model_config = MODEL_CONFIG

    name: str

    proficiency: SkillLevel

    endorsements: int = Field(
        ge=0
    )

    duration_months: int | None = Field(
        default=None,
        ge=0
    )