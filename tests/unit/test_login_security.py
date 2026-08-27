"""Security and edge-case invariants for `hexa login`.

Verifies the token is never logged, printed, present in exception messages,
or placed in a URL, and that invalid tokens or failed validations never
persist or overwrite a valid existing token.
"""

from __future__ import annotations

import logging
from unittest.mock import patch

import httpx
from hexawyn.adapters.secondary.auth.config_token_store import ConfigTokenStore
from hexawyn.adapters.secondary.auth.token_validator import HttpTokenValidator
from hexawyn.application.ports.driven.cloud_auth_port import CloudAuthPort
from hexawyn.application.service.login_service import LoginService
from hexawyn.domain.models.auth import (
    LoginOutcome,
    TokenValidationResult,
    TokenValidationState,
)

SECRET = "hxw_s3cr3t_12345"


class _ValidAuth(CloudAuthPort):
    def __init__(self) -> None:
        self.saved: list[str] = []

    def get_token(self) -> str | None:
        return None

    def save_token(self, token: str) -> None:
        self.saved.append(token)

    def validate_token(self, token: str) -> TokenValidationResult:
        return TokenValidationResult(TokenValidationState.VALID)


class _InvalidAuth(CloudAuthPort):
    def get_token(self) -> str | None:
        return None

    def save_token(self, token: str) -> None:
        raise AssertionError("save_token must not be called on an invalid token")

    def validate_token(self, token: str) -> TokenValidationResult:
        return TokenValidationResult(TokenValidationState.INVALID)


class _UnavailableAuth(CloudAuthPort):
    def get_token(self) -> str | None:
        return None

    def save_token(self, token: str) -> None:
        raise AssertionError("save_token must not be called on an unavailable validation")

    def validate_token(self, token: str) -> TokenValidationResult:
        return TokenValidationResult(TokenValidationState.UNAVAILABLE)


class TestTokenNeverInUrl:
    def test_validator_url_never_contains_token(self) -> None:
        captured: dict[str, str] = {}

        def _handler(request: httpx.Request) -> httpx.Response:
            captured["url"] = str(request.url)
            return httpx.Response(200)

        HttpTokenValidator(_client(_handler), "http://cloud.test").validate_token(SECRET)
        assert SECRET not in captured["url"]
        assert "Bearer" not in captured["url"]


class TestTokenNeverLogged:
    def test_validator_logs_never_contain_token(self, caplog) -> None:
        def _handler(_request: httpx.Request) -> httpx.Response:
            return httpx.Response(401)

        with caplog.at_level(logging.DEBUG):
            HttpTokenValidator(_client(_handler), "http://cloud.test").validate_token(SECRET)
        assert SECRET not in caplog.text


class TestTokenNeverPrinted:
    def test_service_emit_never_contains_token(self) -> None:
        emitted: list[str] = []
        started: list[int] = []
        service = LoginService(
            auth=_ValidAuth(),
            prompt_token=lambda: SECRET,
            emit=emitted.append,
            app_start=lambda: started.append(1),
        )
        service.authenticate()
        assert started == [1]
        assert all(SECRET not in message for message in emitted)


class TestTokenNeverInException:
    def test_store_failure_exception_never_contains_token(self) -> None:
        with patch(
            "hexawyn.adapters.secondary.auth.config_token_store.save_config",
            side_effect=OSError("disk full"),
        ):
            try:
                ConfigTokenStore().save_token(SECRET)
            except OSError as error:
                assert SECRET not in str(error)
            else:
                raise AssertionError("expected an OSError")


class TestInvalidNeverPersisted:
    def test_invalid_token_not_saved(self) -> None:
        service = LoginService(
            auth=_InvalidAuth(),
            prompt_token=lambda: SECRET,
            emit=lambda _m: None,
            app_start=lambda: None,
        )
        assert service.authenticate() == LoginOutcome.INVALID_TOKEN

    def test_unavailable_token_not_saved(self) -> None:
        service = LoginService(
            auth=_UnavailableAuth(),
            prompt_token=lambda: SECRET,
            emit=lambda _m: None,
            app_start=lambda: None,
        )
        assert service.authenticate() == LoginOutcome.UNAVAILABLE


class TestExistingPreserved:
    def test_invalid_replacement_preserves_existing(self) -> None:
        class _ExistingAuth(CloudAuthPort):
            def __init__(self) -> None:
                self.existing = "hxw_good"
                self.saved: list[str] = []

            def get_token(self) -> str | None:
                return self.existing

            def save_token(self, token: str) -> None:
                self.saved.append(token)

            def validate_token(self, token: str) -> TokenValidationResult:
                if token == self.existing:
                    return TokenValidationResult(TokenValidationState.INVALID)
                return TokenValidationResult(TokenValidationState.INVALID)

        auth = _ExistingAuth()
        started: list[int] = []
        service = LoginService(
            auth=auth,
            prompt_token=lambda: SECRET,
            emit=lambda _m: None,
            app_start=lambda: started.append(1),
        )
        outcome = service.authenticate()
        assert outcome == LoginOutcome.INVALID_TOKEN
        assert started == []
        assert auth.saved == []
        assert auth.existing == "hxw_good"


def _client(handler: object) -> httpx.Client:
    return httpx.Client(transport=httpx.MockTransport(handler))  # type: ignore[arg-type]
