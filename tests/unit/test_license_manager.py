import base64
from pathlib import Path
from unittest.mock import patch

import pytest
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from hexawyn.domain.models.quota import LicenseTier
from hexawyn.infrastructure.config.license_manager import (
    LicenseValidationError,
    _decode_token,
    activate_license,
    get_current_tier,
    get_license_tier,
    is_pro,
)


def _generate_key_pair() -> tuple[Ed25519PrivateKey, str]:
    sk = Ed25519PrivateKey.generate()
    pk_b64 = base64.b64encode(sk.public_key().public_bytes_raw()).decode()
    return sk, pk_b64


def _make_token(
    sk: Ed25519PrivateKey,
    tier: str = "free",
    expires: str = "2099-12-31",
    licensee: str = "test@hexawyn.com",
) -> str:
    payload = f"{tier}:{expires}:{licensee}".encode()
    sig = sk.sign(payload)
    sig_b64 = base64.urlsafe_b64encode(sig).decode().rstrip("=")
    payload_b64 = base64.urlsafe_b64encode(payload).decode().rstrip("=")
    return f"{payload_b64}.{sig_b64}."


class TestLicenseKeyValidation:
    def test_valid_token_decodes_correctly(self) -> None:
        sk, pk_b64 = _generate_key_pair()
        token = _make_token(sk, tier="dev", licensee="dev@company.com")

        with patch(
            "hexawyn.infrastructure.config.license_manager.HEXAWYN_PUBLIC_KEY_B64",
            pk_b64,
        ):
            key = _decode_token(token)
            assert key.tier == LicenseTier.DEV
            assert key.licensee == "dev@company.com"
            assert key.is_valid is True

    def test_expired_token_raises_error(self) -> None:
        sk, pk_b64 = _generate_key_pair()
        token = _make_token(sk, tier="startup", expires="2020-01-01")

        with patch(
            "hexawyn.infrastructure.config.license_manager.HEXAWYN_PUBLIC_KEY_B64",
            pk_b64,
        ):
            with pytest.raises(LicenseValidationError) as exc_info:
                _decode_token(token)
            assert "expired" in str(exc_info.value).lower()

    def test_wrong_signature_raises_error(self) -> None:
        sk1, pk_b64 = _generate_key_pair()
        sk2, _ = _generate_key_pair()
        # Tamper: sign with different key — simulate by signing with sk2 but using sk1's public key
        payload = b"enterprise:2099-12-31:bad@actor.com"
        sig = sk2.sign(payload)
        sig_b64 = base64.urlsafe_b64encode(sig).decode().rstrip("=")
        payload_b64 = base64.urlsafe_b64encode(payload).decode().rstrip("=")
        bad_token = f"{payload_b64}.{sig_b64}."

        with patch(
            "hexawyn.infrastructure.config.license_manager.HEXAWYN_PUBLIC_KEY_B64",
            pk_b64,
        ):
            with pytest.raises(LicenseValidationError) as exc_info:
                _decode_token(bad_token)
            assert "signature" in str(exc_info.value).lower()

    def test_tampered_payload_raises_error(self) -> None:
        sk, pk_b64 = _generate_key_pair()
        token = _make_token(sk, tier="free")
        # Flip a character in payload
        parts = token.split(".")
        payload_b64 = parts[0]
        # toggle last char before padding
        last_char = payload_b64[-1]
        flipped = "A" if last_char != "A" else "B"
        tampered_payload = payload_b64[:-1] + flipped
        bad_token = f"{tampered_payload}.{parts[1]}.{parts[2]}"

        with patch(
            "hexawyn.infrastructure.config.license_manager.HEXAWYN_PUBLIC_KEY_B64",
            pk_b64,
        ):
            with pytest.raises(LicenseValidationError):
                _decode_token(bad_token)

    def test_invalid_format_raises_error(self) -> None:
        _, pk_b64 = _generate_key_pair()
        with patch(
            "hexawyn.infrastructure.config.license_manager.HEXAWYN_PUBLIC_KEY_B64",
            pk_b64,
        ):
            with pytest.raises(LicenseValidationError):
                _decode_token("not-a-valid-token")

    def test_unknown_tier_raises_error(self) -> None:
        sk, pk_b64 = _generate_key_pair()
        token = _make_token(sk, tier="platinum")

        with patch(
            "hexawyn.infrastructure.config.license_manager.HEXAWYN_PUBLIC_KEY_B64",
            pk_b64,
        ):
            with pytest.raises(LicenseValidationError) as exc_info:
                _decode_token(token)
            assert "tier" in str(exc_info.value).lower()

    def test_perpetual_license_no_expiration(self) -> None:
        sk, pk_b64 = _generate_key_pair()
        payload = b"enterprise::enterprise@bigcorp.com"
        sig = sk.sign(payload)
        sig_b64 = base64.urlsafe_b64encode(sig).decode().rstrip("=")
        payload_b64 = base64.urlsafe_b64encode(payload).decode().rstrip("=")
        token = f"{payload_b64}.{sig_b64}."

        with patch(
            "hexawyn.infrastructure.config.license_manager.HEXAWYN_PUBLIC_KEY_B64",
            pk_b64,
        ):
            key = _decode_token(token)
            assert key.tier == LicenseTier.ENTERPRISE
            assert key.is_expired is False
            assert key.is_valid is True


class TestGetLicenseTier:
    def test_returns_free_when_no_license_set(self) -> None:
        with patch.dict("os.environ", {}, clear=True):
            with patch(
                "hexawyn.infrastructure.config.license_manager._read_license_key",
                return_value=None,
            ):
                assert get_license_tier() == LicenseTier.FREE

    def test_returns_free_when_invalid_license(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.license_manager._read_license_key",
            return_value="invalid-token",
        ):
            assert get_license_tier() == LicenseTier.FREE

    def test_returns_tier_from_valid_license(self) -> None:
        sk, pk_b64 = _generate_key_pair()
        token = _make_token(sk, tier="startup")

        with patch(
            "hexawyn.infrastructure.config.license_manager.HEXAWYN_PUBLIC_KEY_B64",
            pk_b64,
        ):
            with patch(
                "hexawyn.infrastructure.config.license_manager._read_license_key",
                return_value=token,
            ):
                assert get_license_tier() == LicenseTier.STARTUP


class TestActivateLicense:
    def test_activates_valid_license(self, tmp_path: Path) -> None:
        sk, pk_b64 = _generate_key_pair()
        token = _make_token(sk, tier="dev", licensee="dev@startup.io")
        key_path = tmp_path / "license.key"

        with patch(
            "hexawyn.infrastructure.config.license_manager.HEXAWYN_PUBLIC_KEY_B64",
            pk_b64,
        ):
            with patch(
                "hexawyn.infrastructure.config.license_manager.LICENSE_KEY_PATH",
                key_path,
            ):
                key = activate_license(token)
                assert key.tier == LicenseTier.DEV
                assert key_path.exists()
                assert token in key_path.read_text()

    def test_rejects_invalid_license(self, tmp_path: Path) -> None:
        _, pk_b64 = _generate_key_pair()
        key_path = tmp_path / "license.key"

        with patch(
            "hexawyn.infrastructure.config.license_manager.HEXAWYN_PUBLIC_KEY_B64",
            pk_b64,
        ):
            with patch(
                "hexawyn.infrastructure.config.license_manager.LICENSE_KEY_PATH",
                key_path,
            ):
                with pytest.raises(LicenseValidationError):
                    activate_license("bad-token")
                assert not key_path.exists()


class TestLicenseBackwardCompat:
    def test_get_current_tier_alias(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.license_manager._read_license_key",
            return_value=None,
        ):
            assert get_current_tier() == LicenseTier.FREE

    def test_is_pro_returns_false_for_free(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.license_manager._read_license_key",
            return_value=None,
        ):
            assert is_pro() is False
