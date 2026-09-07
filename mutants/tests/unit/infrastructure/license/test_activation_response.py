import pytest
from pydantic import ValidationError


class TestActivationResponseContract:
    def test_valid_parses(self) -> None:
        from hexawyn.infrastructure.license.activation_response import ActivationResponse

        result = ActivationResponse.model_validate(
            {"token": "eyJ.abc.xyz", "plan": "starter", "expires_at": "2026-08-18T00:00:00Z"}
        )
        assert result.token == "eyJ.abc.xyz"
        assert result.plan == "starter"

    def test_bad_plan_rejected(self) -> None:
        from hexawyn.infrastructure.license.activation_response import ActivationResponse

        with pytest.raises(ValidationError):
            ActivationResponse.model_validate(
                {"token": "x", "plan": "enterprise", "expires_at": "2026-01-01T00:00:00Z"}
            )

    def test_missing_token_rejected(self) -> None:
        from hexawyn.infrastructure.license.activation_response import ActivationResponse

        with pytest.raises(ValidationError):
            ActivationResponse.model_validate(
                {"plan": "starter", "expires_at": "2026-01-01T00:00:00Z"}
            )

    def test_non_iso_expires_at_rejected(self) -> None:
        from hexawyn.infrastructure.license.activation_response import ActivationResponse

        with pytest.raises(ValidationError):
            ActivationResponse.model_validate(
                {"token": "x", "plan": "starter", "expires_at": "not-a-date"}
            )
