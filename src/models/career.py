"""
Career history model.
"""

from datetime import date

from pydantic import BaseModel, Field

from .base import MODEL_CONFIG
from .profile import CompanySize


class CareerHistory(BaseModel):
    """
    Single employment record.
    """

    model_config = MODEL_CONFIG

    company: str

    title: str
    
    start_date: date

    end_date: date | None = None

    duration_months: int = Field(
        ge=0
    )

    is_current: bool

    industry: str

    company_size: CompanySize

    description: str