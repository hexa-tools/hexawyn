"""Driven port abstraction for Hexawyn Cloud authentication.

The application core depends on this port, never on an HTTP or config
implementation. Adapters (HTTP validator, config-backed token store) satisfy
it and are wired in the CLI command factory.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.domain.models.auth import TokenValidationResult


class CloudAuthPort(ABC):
    """Authentication operations against Hexawyn Cloud / Control Plane."""

    @abstractmethod
    def validate_token(self, token: str) -> TokenValidationResult:
        """Validate a token against the Control Plane (Bearer)."""

    @abstractmethod
    def get_token(self) -> str | None:
        """Resolve the configured token (env › config), if any."""

    @abstractmethod
    def save_token(self, token: str) -> None:
        """Persist a validated token locally."""
