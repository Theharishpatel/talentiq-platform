from enum import Enum
from pydantic import ConfigDict


MODEL_CONFIG = ConfigDict(
    extra="forbid",      # Unknown fields reject
    validate_assignment=True,
    str_strip_whitespace=True,
)