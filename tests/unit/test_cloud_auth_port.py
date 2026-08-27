"""Unit tests for the CloudAuthPort abstraction."""

from __future__ import annotations

import pytest
from hexawyn.application.ports.driven.cloud_auth_port import CloudAuthPort
from hexawyn.domain.models.auth import TokenValidationResult, TokenValidationState


class _FakePort(CloudAuthPort):
    def validate_token(self, token: str) -> TokenValidationResult:
        return TokenValidationResult(TokenValidationState.VALID)

    def get_token(self) -> str | None:
        return "hxw_example"

    def save_token(self, token: str) -> None:
        return None


def test_port_cannot_be_instantiated_directly() -> None:
    with pytest.raises(TypeError):
        CloudAuthPort()  # type: ignore[abstract]


def test_concrete_subclass_implements_contract() -> None:
    port = _FakePort()
    assert port.validate_token("t").state == TokenValidationState.VALID
    assert port.get_token() == "hxw_example"
    assert port.save_token("t") is None
