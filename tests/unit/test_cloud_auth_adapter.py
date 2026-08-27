"""Unit tests for the CloudAuthAdapter composition."""

from __future__ import annotations

from hexawyn.adapters.secondary.auth.cloud_auth_adapter import CloudAuthAdapter
from hexawyn.adapters.secondary.auth.config_token_store import ConfigTokenStore
from hexawyn.adapters.secondary.auth.token_validator import HttpTokenValidator
from hexawyn.domain.models.auth import TokenValidationResult, TokenValidationState


class _FakeValidator:
    def __init__(self) -> None:
        self.calls: list[tuple[str, str]] = []

    def validate_token(self, token: str) -> TokenValidationResult:
        self.calls.append(("validate", token))
        valid = token == "hxw_ok"
        return TokenValidationResult(
            TokenValidationState.VALID if valid else TokenValidationState.INVALID
        )


class _FakeStore:
    def __init__(self, existing: str | None = None) -> None:
        self._token = existing
        self.saved: list[str] = []

    def get_token(self) -> str | None:
        return self._token

    def save_token(self, token: str) -> None:
        self._token = token
        self.saved.append(token)


class TestCloudAuthAdapter:
    def test_validate_delegates_to_validator(self) -> None:
        validator = _FakeValidator()
        adapter = CloudAuthAdapter(validator, _FakeStore())
        result = adapter.validate_token("hxw_ok")
        assert result.state == TokenValidationState.VALID
        assert validator.calls == [("validate", "hxw_ok")]

    def test_get_token_delegates_to_store(self) -> None:
        adapter = CloudAuthAdapter(_FakeValidator(), _FakeStore("hxw_existing"))
        assert adapter.get_token() == "hxw_existing"

    def test_save_token_delegates_to_store(self) -> None:
        store = _FakeStore()
        adapter = CloudAuthAdapter(_FakeValidator(), store)
        adapter.save_token("hxw_new")
        assert store.saved == ["hxw_new"]

    def test_concrete_adapter_is_cloud_auth_port(self) -> None:
        adapter = CloudAuthAdapter(
            HttpTokenValidator.__new__(HttpTokenValidator), ConfigTokenStore()
        )
        from hexawyn.application.ports.driven.cloud_auth_port import CloudAuthPort

        assert isinstance(adapter, CloudAuthPort)
