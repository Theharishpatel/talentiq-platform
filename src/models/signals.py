"""
Redrob activity and engagement signals.
"""

from datetime import date
from enum import Enum

from pydantic import BaseModel, Field

from .base import MODEL_CONFIG

class WorkMode(str, Enum):
    REMOTE = "remote"
    HYBRID = "hybrid"
    ONSITE = "onsite"
    FLEXIBLE = "flexible"

class SalaryRange(BaseModel):
    """
    Expected salary range.
    """

    model_config = MODEL_CONFIG

    min: float = Field(ge=0)

    max: float = Field(ge=0)

class RedrobSignals(BaseModel):
    """
    Platfrom engangement metrics.
    """

    model_config = MODEL_CONFIG

    profile_completeness_score: float = Field(
        ge=0,
        le=100
    )

    signup_date: date

    last_active_date: date

    open_to_work_flag: bool

    profile_views_received_30d: int = Field(ge=0)

    applications_submitted_30d: int = Field(ge=0)

    recruiter_response_rate: float = Field(
        ge=0,
        le=1
    )

    avg_response_time_hours: float = Field(
        ge=0
    )

    skill_assessment_scores: dict[str, float]

    connection_count: int = Field(ge=0)

    endorsements_received: int = Field(ge=0)

    notice_period_days: int = Field(
    ge=0,
    le=180
)

    expected_salary_range_inr_lpa: SalaryRange

    preferred_work_mode: WorkMode

    willing_to_relocate: bool

    github_activity_score: float = Field(
    ge=-1,
    le=100
)

    search_appearance_30d: int = Field(
        ge=0
    )

    saved_by_recruiters_30d: int = Field(
        ge=0
    )

    interview_completion_rate: float = Field(
        ge=0,
        le=1
    )

    offer_acceptance_rate: float = Field(
        ge=-1,
        le=1
    )

    verified_email: bool

    verified_phone: bool

    linkedin_connected: bool