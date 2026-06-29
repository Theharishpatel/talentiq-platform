"""
Candidate profile model.
"""

from enum import Enum

from pydantic import BaseModel, Field

from .base import MODEL_CONFIG

class CompanySize(str, Enum):
    SIZE_1_10 = "1-10"
    SIZE_11_50 = "11-50"
    SIZE_51_200 = "51-200"
    SIZE_201_500 = "201-500"
    SIZE_501_1000 = "501-1000"
    SIZE_1001_5000 = "1001-5000"
    SIZE_5001_10000 = "5001-10000"
    SIZE_10001_PLUS = "10001+"

class Profile(BaseModel):
    """
    Core candidate profile information.
    """

    model_config = MODEL_CONFIG
    
    anonymized_name: str
    headline: str
    summary: str

    location: str
    country: str

    years_of_experience: float = Field(
        ge=0,
        le=50,
    )

    current_title:str

    current_company: str

    current_company_size: CompanySize

    current_industry: str
    
