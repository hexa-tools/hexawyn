"""Unit tests for the login service orchestration."""

from __future__ import annotations

from collections.abc import Callable

from hexawyn.application.ports.driven.cloud_auth_port import CloudAuthPort
from hexawyn.application.service.login_service import LoginService
from hexawyn.domain.models.auth import LoginOutcome, TokenValidationResult, TokenValidationState


class _FakeAuth(CloudAuthPort):
    def __init__(self, existing: str | None = None, valid_values: set[str] | None = None) -> None:
        self._existing = existing
        self._valid = valid_values if valid_values is not None else {"hxw_ok"}
        self.saved: list[str] = []
        self.validation_count = 0

    def get_token(self) -> str | None:
        return self._existing

    def save_token(self, token: str) -> None:
        self.saved.append(token)

    def validate_token(self, token: str) -> TokenValidationResult:
        self.validation_count += 1
        if token in self._valid:
            return TokenValidationResult(TokenValidationState.VALID)
        return TokenValidationResult(TokenValidationState.INVALID)


class _UnavailableAuth(CloudAuthPort):
    def get_token(self) -> str | None:
        return None

    def save_token(self, token: str) -> None:
        return None

    def validate_token(self, token: str) -> TokenValidationResult:
        return TokenValidationResult(TokenValidationState.UNAVAILABLE, "network")


def _service(
    auth: CloudAuthPort, prompt: Callable[[], str | None], started: list[int]
) -> LoginService:
    return LoginService(
        auth=auth,
        prompt_token=prompt,
        emit=lambda msg: None,
        app_start=lambda: started.append(1),
    )


class TestLoginService:
    def test_no_token_prompt_then_validate_save_start(self) -> None:
        auth = _FakeAuth(existing=None)
        started: list[int] = []
        service = _service(auth, lambda: "hxw_ok", started)

        outcome = service.authenticate()

        assert outcome == LoginOutcome.AUTHENTICATED
        assert auth.saved == ["hxw_ok"]
        assert started == [1]

    def test_existing_valid_skips_prompt_and_starts(self) -> None:
        auth = _FakeAuth(existing="hxw_ok")
        prompt_called: list[bool] = []
        started: list[int] = []
        service = _service(auth, lambda: prompt_called.append(True) or None, started)

        outcome = service.authenticate()

        assert outcome == LoginOutcome.STARTED_WITH_EXISTING
        assert not prompt_called
        assert started == [1]
        assert auth.saved == []

    def test_existing_invalid_returns_invalid_without_prompt(self) -> None:
        auth = _FakeAuth(existing="hxw_bad", valid_values={"hxw_ok"})
        prompt_called: list[bool] = []
        started: list[int] = []
        service = _service(auth, lambda: prompt_called.append(True) or "hxw_ok", started)

        outcome = service.authenticate()

        assert outcome == LoginOutcome.INVALID_TOKEN
        assert not prompt_called
        assert auth.saved == []
        assert started == []

    def test_new_token_invalid_exits_without_saving_or_starting(self) -> None:
        auth = _FakeAuth(existing=None, valid_values={"hxw_ok"})
        started: list[int] = []
        service = _service(auth, lambda: "hxw_bad", started)

        outcome = service.authenticate()

        assert outcome == LoginOutcome.INVALID_TOKEN
        assert auth.saved == []
        assert started == []

    def test_unavailable_exits_without_saving_or_starting(self) -> None:
        started: list[int] = []
        service = _service(_UnavailableAuth(), lambda: "hxw_anything", started)

        outcome = service.authenticate()

        assert outcome == LoginOutcome.UNAVAILABLE
        assert started == []

    def test_cancelled_exits_cleanly_without_touching_token(self) -> None:
        auth = _FakeAuth(existing=None)
        started: list[int] = []
        service = _service(auth, lambda: None, started)

        outcome = service.authenticate()

        assert outcome == LoginOutcome.CANCELLED
        assert auth.saved == []
        assert started == []

    def test_empty_prompt_is_invalid(self) -> None:
        auth = _FakeAuth(existing=None)
        started: list[int] = []
        service = _service(auth, lambda: "   ", started)

        outcome = service.authenticate()

        assert outcome == LoginOutcome.INVALID_TOKEN
        assert auth.saved == []
        assert started == []

    def test_existing_unavailable_is_not_invalid(self) -> None:
        class _UnavailableExisting(CloudAuthPort):
            def get_token(self) -> str | None:
                return "hxw_x"

            def save_token(self, token: str) -> None:
                return None

            def validate_token(self, token: str) -> TokenValidationResult:
                return TokenValidationResult(TokenValidationState.UNAVAILABLE, "timeout")

        started: list[int] = []
        service = _service(_UnavailableExisting(), lambda: None, started)

        outcome = service.authenticate()

        assert outcome == LoginOutcome.UNAVAILABLE
        assert started == []
