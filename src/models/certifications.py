"""
Certification model.
"""

from pydantic import BaseModel

from .base import MODEL_CONFIG

class Certification(BaseModel):
    """
    Professional certification.
    """

    model_config = MODEL_CONFIG

    name: str

    issuer: str

    year: int