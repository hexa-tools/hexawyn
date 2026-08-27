"""Unit tests for the cloud auth domain model."""

from __future__ import annotations

from hexawyn.domain.models.auth import LoginOutcome, TokenValidationResult, TokenValidationState


class TestTokenValidationResult:
    def test_valid_is_valid(self) -> None:
        result = TokenValidationResult(TokenValidationState.VALID)
        assert result.is_valid is True
        assert result.state == TokenValidationState.VALID

    def test_invalid_is_not_valid(self) -> None:
        result = TokenValidationResult(TokenValidationState.INVALID)
        assert result.is_valid is False

    def test_unavailable_is_not_valid(self) -> None:
        result = TokenValidationResult(TokenValidationState.UNAVAILABLE, "timeout")
        assert result.is_valid is False
        assert result.message == "timeout"

    def test_enum_values(self) -> None:
        assert TokenValidationState.VALID.value == "valid"
        assert TokenValidationState.INVALID.value == "invalid"
        assert TokenValidationState.UNAVAILABLE.value == "unavailable"

    def test_login_outcome_values(self) -> None:
        assert LoginOutcome.STARTED_WITH_EXISTING.value == "started_existing"
        assert LoginOutcome.AUTHENTICATED.value == "authenticated"
        assert LoginOutcome.INVALID_TOKEN.value == "invalid_token"
        assert LoginOutcome.UNAVAILABLE.value == "unavailable"
        assert LoginOutcome.CANCELLED.value == "cancelled"
