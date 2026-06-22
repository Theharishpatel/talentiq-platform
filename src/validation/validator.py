"""
Candidate validation.
"""

from pydantic import ValidationError

from src.models.candidate import Candidate


def validate_candidate(
        candidate_data: dict
):
    """
    Validate candidate against schema.
    """

    try:

        candidate = Candidate.model_validate(
            candidate_data
        )

        return True, candidate
    
    except ValidationError as error:

        return False, error.errors()