"""Regression tests: an expired license must not keep a paid tier (quota 200).

``verify_license`` falls back to an unverified decode when the public key is a
placeholder (or invalid); PyJWT's fallback there does not raise on an expired
``exp``, so ``get_license_tier`` kept returning a paid tier — and the CLI kept
showing 200 investigations even though the token had expired.
"""

from __future__ import annotations

from unittest.mock import patch

from hexawyn.domain.models.quota import LicenseTier
from hexawyn.infrastructure.license.license_exceptions import LicenseExpiredError
from hexawyn.infrastructure.license.license_manager import get_license_tier, verify_license
from jwt.exceptions import InvalidKeyError

_EXPIRED_PAYLOAD = {
    "sub": "test",
    "plan": "team",
    "clusters_max": 5,
    "users_max": 3,
    "investigations_monthly": 200,
    "history_days": 30,
    "exp": 1000,  # in the past
    "iat": 100,
}


class TestExpiredLicenseFallsBackToStarter:
    def test_get_license_tier_is_starter_when_token_expired(self) -> None:
        with patch(
            "hexawyn.infrastructure.license.license_manager._read_license_key",
            return_value="dummy.token",
        ):
            with patch(
                "hexawyn.infrastructure.license.license_manager.jwt.decode",
                side_effect=[InvalidKeyError("bad key"), _EXPIRED_PAYLOAD],
            ):
                assert get_license_tier() == LicenseTier.STARTER

    def test_verify_license_raises_for_expired_token(self) -> None:
        with patch(
            "hexawyn.infrastructure.license.license_manager._read_license_key",
            return_value="dummy.token",
        ):
            with patch(
                "hexawyn.infrastructure.license.license_manager.jwt.decode",
                side_effect=[InvalidKeyError("bad key"), _EXPIRED_PAYLOAD],
            ):
                with __import__("pytest").raises(LicenseExpiredError):
                    verify_license()
