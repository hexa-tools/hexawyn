from pathlib import Path
from unittest.mock import patch

import jwt
import pytest
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from hexawyn.domain.models.quota import LicenseTier
from hexawyn.infrastructure.config.license_manager import (
    LicenseValidationError,
    activate_license,
    get_current_tier,
    get_license_tier,
    is_pro,
)


def _generate_keypair() -> tuple[str, str]:
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    ).decode()
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    ).decode()
    return private_pem, public_pem


def _make_jwt(
    private_pem: str,
    plan: str = "free",
    exp: int | None = 4102444800,
    sub: str = "test@hexawyn.com",
) -> str:
    payload: dict = {"sub": sub, "plan": plan, "iat": 1700000000}
    if exp is not None:
        payload["exp"] = exp
    return jwt.encode(payload, private_pem, algorithm="RS256")


class TestLicenseKeyValidation:
    def test_valid_token_decodes_correctly(self) -> None:
        sk, pk = _generate_keypair()
        token = _make_jwt(sk, plan="dev", sub="dev@company.com")

        with patch(
            "hexawyn.infrastructure.license.license_manager._read_license_key",
            return_value=token,
        ):
            with patch("hexawyn.infrastructure.license.license_manager.PUBLIC_KEY_PEM", pk):
                from hexawyn.infrastructure.license.license_manager import verify_license

                claims = verify_license()
                assert claims.plan == "dev"
                assert claims.sub == "dev@company.com"

    def test_expired_token_falls_back_to_free(self) -> None:
        sk, pk = _generate_keypair()
        token = _make_jwt(sk, plan="startup", exp=1000000000)

        with patch(
            "hexawyn.infrastructure.license.license_manager._read_license_key",
            return_value=token,
        ):
            with patch("hexawyn.infrastructure.license.license_manager.PUBLIC_KEY_PEM", pk):
                from hexawyn.infrastructure.license.license_manager import get_license_tier

                assert get_license_tier() == LicenseTier.FREE

    def test_wrong_signature_falls_back_to_free(self) -> None:
        sk1, pk1 = _generate_keypair()
        sk2, _ = _generate_keypair()
        token = _make_jwt(sk2, plan="enterprise")

        with patch(
            "hexawyn.infrastructure.license.license_manager._read_license_key",
            return_value=token,
        ):
            with patch("hexawyn.infrastructure.license.license_manager.PUBLIC_KEY_PEM", pk1):
                from hexawyn.infrastructure.license.license_manager import verify_license

                claims = verify_license()
                assert claims.plan == "free"

    def test_invalid_format_falls_back_to_free(self) -> None:
        _, pk = _generate_keypair()
        with patch(
            "hexawyn.infrastructure.license.license_manager._read_license_key",
            return_value="not-a-valid-jwt",
        ):
            with patch("hexawyn.infrastructure.license.license_manager.PUBLIC_KEY_PEM", pk):
                from hexawyn.infrastructure.license.license_manager import verify_license

                claims = verify_license()
                assert claims.plan == "free"


class TestGetLicenseTier:
    def test_returns_free_when_no_license_set(self) -> None:
        with patch(
            "hexawyn.infrastructure.license.license_manager._read_license_key",
            return_value=None,
        ):
            assert get_license_tier() == LicenseTier.FREE

    def test_returns_tier_from_valid_license(self) -> None:
        sk, pk = _generate_keypair()
        token = _make_jwt(sk, plan="startup")

        with patch("hexawyn.infrastructure.license.license_manager.PUBLIC_KEY_PEM", pk):
            with patch(
                "hexawyn.infrastructure.license.license_manager._read_license_key",
                return_value=token,
            ):
                assert get_license_tier() == LicenseTier.STARTUP


class TestActivateLicense:
    def test_activates_valid_license(self, tmp_path: Path) -> None:
        sk, pk = _generate_keypair()
        token = _make_jwt(sk, plan="dev", sub="dev@startup.io")
        key_path = tmp_path / "license.key"

        with patch("hexawyn.infrastructure.license.license_manager.PUBLIC_KEY_PEM", pk):
            with patch(
                "hexawyn.infrastructure.license.license_manager.LICENSE_KEY_PATH",
                key_path,
            ):
                with patch(
                    "hexawyn.infrastructure.license.license_manager._read_license_key",
                    return_value=token,
                ):
                    claims = activate_license(token)
                    assert claims.plan == "dev"
                    assert key_path.exists()
                    assert token in key_path.read_text()

    def test_rejects_invalid_license(self, tmp_path: Path) -> None:
        _, pk = _generate_keypair()
        key_path = tmp_path / "license.key"

        with patch("hexawyn.infrastructure.license.license_manager.PUBLIC_KEY_PEM", pk):
            with patch(
                "hexawyn.infrastructure.license.license_manager.LICENSE_KEY_PATH",
                key_path,
            ):
                with pytest.raises(LicenseValidationError):
                    activate_license("not-a-jwt")
                assert not key_path.exists()


class TestLicenseBackwardCompat:
    def test_get_current_tier_alias(self) -> None:
        with patch(
            "hexawyn.infrastructure.license.license_manager._read_license_key",
            return_value=None,
        ):
            assert get_current_tier() == LicenseTier.FREE

    def test_is_pro_returns_false_for_free(self) -> None:
        with patch(
            "hexawyn.infrastructure.license.license_manager._read_license_key",
            return_value=None,
        ):
            assert is_pro() is False
