"""Login orchestration service for `hexa login`.

Resolves any existing token (env › config), validates it, prompts a new token
when needed, persists it only after successful validation, and starts the
Hexawyn application after a successful authentication.

The Control Plane is the sole authority for token validity.
"""

from __future__ import annotations

from collections.abc import Callable

from hexawyn.application.ports.driven.cloud_auth_port import CloudAuthPort
from hexawyn.domain.models.auth import LoginOutcome, TokenValidationState


class LoginService:
    """Authenticates a Hexawyn Cloud session and starts the CLI."""

    def __init__(
        self,
        auth: CloudAuthPort,
        prompt_token: Callable[[], str | None],
        emit: Callable[[str], None],
        app_start: Callable[[], None],
    ) -> None:
        self._auth = auth
        self._prompt_token = prompt_token
        self._emit = emit
        self._app_start = app_start

    def authenticate(self) -> LoginOutcome:
        """Run the login flow and return its outcome."""
        existing = self._auth.get_token()
        if existing:
            existing_result = self._auth.validate_token(existing)
            if existing_result.is_valid:
                self._emit("✓ Existing Hexawyn Cloud token is valid")
                self._start()
                return LoginOutcome.STARTED_WITH_EXISTING
            if existing_result.state == TokenValidationState.UNAVAILABLE:
                self._emit("✗ Authentication service unavailable")
                return LoginOutcome.UNAVAILABLE
            self._emit("✗ Existing Hexawyn Cloud token is invalid")

        token = self._prompt_token()
        if token is None:
            self._emit("Login cancelled")
            return LoginOutcome.CANCELLED

        token = token.strip()
        if not token:
            self._emit("✗ Invalid Hexawyn Cloud token")
            return LoginOutcome.INVALID_TOKEN

        result = self._auth.validate_token(token)
        if result.state == TokenValidationState.UNAVAILABLE:
            self._emit("✗ Authentication service unavailable")
            return LoginOutcome.UNAVAILABLE
        if not result.is_valid:
            self._emit("✗ Invalid Hexawyn Cloud token")
            return LoginOutcome.INVALID_TOKEN

        self._auth.save_token(token)
        self._emit("✓ Token validated")
        self._emit("✓ Token saved")
        self._start()
        return LoginOutcome.AUTHENTICATED

    def _start(self) -> None:
        self._emit("Starting Hexawyn...")
        self._app_start()
