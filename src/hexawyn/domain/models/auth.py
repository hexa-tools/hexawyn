"""Cloud authentication domain model."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class TokenValidationState(str, Enum):
    """Outcome of validating a cloud token against the Control Plane."""

    VALID = "valid"
    INVALID = "invalid"
    UNAVAILABLE = "unavailable"


class LoginOutcome(str, Enum):
    """Result of the hexa login command."""

    STARTED_WITH_EXISTING = "started_existing"
    AUTHENTICATED = "authenticated"
    INVALID_TOKEN = "invalid_token"
    UNAVAILABLE = "unavailable"
    CANCELLED = "cancelled"


@dataclass(frozen=True)
class TokenValidationResult:
    """Result of a single token validation request."""

    state: TokenValidationState
    message: str = ""

    @property
    def is_valid(self) -> bool:
        return self.state == TokenValidationState.VALID
