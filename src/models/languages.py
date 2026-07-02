"""
Language model.
"""

from enum import Enum

from pydantic import BaseModel

from .base import MODEL_CONFIG

class LanguageLevel(str, Enum):
    BASIC = "basic"
    CONVERSATIONAL = "conversational"
    PROFESSIONAL = "professional"
    NATIVE = "native"

class Language(BaseModel):
    """
    Spoken language.
    """

    model_config = MODEL_CONFIG

    language: str

    proficiency: LanguageLevel