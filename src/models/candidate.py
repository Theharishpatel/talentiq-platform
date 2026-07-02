"""
Root candidate model.
"""

from pydantic import BaseModel, Field

from .base import MODEL_CONFIG
from .career import CareerHistory
from .certifications import Certification
from .education import Education
from .languages import Language
from .profile import Profile
from .signals import RedrobSignals
from .skills import Skill

class Candidate(BaseModel):
    """
    Complete candidate profile.
    """

    model_config = MODEL_CONFIG

    candidate_id: str = Field(
        pattern=r"^CAND_[0-9]{7}$"
    )

    profile: Profile

    career_history: list[CareerHistory] = Field(
        min_length=1,
        max_length=10
    )

    education: list[Education] = Field(
        default_factory=list,
        max_length=5
    )

    skills: list[Skill] = Field(
        default_factory=list
    )

    certifications: list[Certification] = Field(
        default_factory=list
    )

    languages: list[Language] = Field(
        default_factory=list
    )

    redrob_signals: RedrobSignals