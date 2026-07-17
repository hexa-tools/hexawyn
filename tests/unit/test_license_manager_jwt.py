import os
from pathlib import Path
from unittest.mock import patch

import jwt
import pytest
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from hexawyn.domain.errors import HexawynError
from hexawyn.domain.models.license import LicenseClaims
from hexawyn.domain.models.quota import LicenseTier


def _generate_rsa_keypair() -> tuple[str, str]:
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


def _sign_jwt(private_pem: str, claims: dict) -> str:
    return jwt.encode(
        payload={
            "sub": claims.get("sub", "test@hexawyn.com"),
            "plan": claims.get("plan", "starter"),
            "clusters_max": claims.get("clusters_max", 1),
            "users_max": claims.get("users_max", 1),
            "investigations_monthly": claims.get("investigations_monthly", 50),
            "history_days": claims.get("history_days", 7),
            "providers": claims.get("providers", ["vanilla"]),
            "iat": claims.get("iat", 1700000000),
            "exp": claims.get("exp", 4102444800),
        },
        key=private_pem,
        algorithm="RS256",
    )


class TestLicenseClaims:
    def test_default_free_claims(self) -> None:
        claims = LicenseClaims.free()
        assert claims.plan == "starter"
        assert claims.clusters_max == 1
        assert claims.users_max == 1
        assert claims.investigations_monthly == 50
        assert claims.history_days == 7
        assert claims.providers == ["vanilla"]


class TestVerifyLicense:
    def test_no_license_returns_free_claims(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            with patch(
                "hexawyn.infrastructure.license.license_manager._read_license_key",
                return_value=None,
            ):
                from hexawyn.infrastructure.license.license_manager import verify_license

                claims = verify_license()
                assert claims.plan == "starter"
                assert claims.clusters_max == 1

    def test_valid_jwt_decodes_correctly(self) -> None:
        private_pem, public_pem = _generate_rsa_keypair()
        token = _sign_jwt(
            private_pem,
            {"plan": "dev", "clusters_max": 1, "providers": ["vanilla", "aws", "azure", "gcp"]},
        )

        with patch(
            "hexawyn.infrastructure.license.license_manager._read_license_key",
            return_value=token,
        ):
            with patch(
                "hexawyn.infrastructure.license.license_manager.PUBLIC_KEY_PEM",
                public_pem,
            ):
                from hexawyn.infrastructure.license.license_manager import verify_license

                claims = verify_license()
                assert claims.plan == "dev"
                assert claims.providers == ["vanilla", "aws", "azure", "gcp"]

    def test_startup_plan_decodes(self) -> None:
        private_pem, public_pem = _generate_rsa_keypair()
        token = _sign_jwt(
            private_pem,
            {
                "plan": "team",
                "clusters_max": 3,
                "users_max": 5,
                "investigations_monthly": 500,
                "history_days": 90,
                "providers": ["vanilla", "aws", "azure", "gcp", "openshift", "datadog"],
            },
        )

        with patch(
            "hexawyn.infrastructure.license.license_manager._read_license_key",
            return_value=token,
        ):
            with patch(
                "hexawyn.infrastructure.license.license_manager.PUBLIC_KEY_PEM",
                public_pem,
            ):
                from hexawyn.infrastructure.license.license_manager import verify_license

                claims = verify_license()
                assert claims.plan == "team"
                assert claims.clusters_max == 3
                assert claims.investigations_monthly == 500

    def test_expired_jwt_raises_error(self) -> None:
        private_pem, public_pem = _generate_rsa_keypair()
        token = _sign_jwt(private_pem, {"plan": "dev", "exp": 1000000000})

        with patch(
            "hexawyn.infrastructure.license.license_manager._read_license_key",
            return_value=token,
        ):
            with patch(
                "hexawyn.infrastructure.license.license_manager.PUBLIC_KEY_PEM",
                public_pem,
            ):
                from hexawyn.infrastructure.license.license_exceptions import (
                    LicenseExpiredError,
                )
                from hexawyn.infrastructure.license.license_manager import verify_license

                with pytest.raises(LicenseExpiredError):
                    verify_license()

    def test_invalid_jwt_returns_free_fallback(self) -> None:
        from hexawyn.infrastructure.license.license_manager import verify_license

        with patch(
            "hexawyn.infrastructure.license.license_manager._read_license_key",
            return_value="not-a-valid-jwt",
        ):
            claims = verify_license()
            assert claims.plan == "starter"


class TestHasProviderAccess:
    def test_wildcard_providers_grant_all(self) -> None:
        claims = LicenseClaims(
            sub="test",
            plan="scale-up",
            clusters_max=-1,
            users_max=20,
            investigations_monthly=-1,
            history_days=-1,
            providers=["*"],
            exp=4102444800,
            iat=1700000000,
        )
        from hexawyn.infrastructure.license.license_manager import has_provider_access

        assert has_provider_access(claims, "aws") is True
        assert has_provider_access(claims, "gcp") is True
        assert has_provider_access(claims, "datadog") is True

    def test_specific_providers_only(self) -> None:
        claims = LicenseClaims(
            sub="test",
            plan="dev",
            clusters_max=1,
            users_max=1,
            investigations_monthly=200,
            history_days=30,
            providers=["vanilla", "aws", "azure"],
            exp=4102444800,
            iat=1700000000,
        )
        from hexawyn.infrastructure.license.license_manager import has_provider_access

        assert has_provider_access(claims, "aws") is True
        assert has_provider_access(claims, "vanilla") is True
        assert has_provider_access(claims, "gcp") is False
        assert has_provider_access(claims, "openshift") is False

    def test_free_only_vanilla(self) -> None:
        claims = LicenseClaims.free()
        from hexawyn.infrastructure.license.license_manager import has_provider_access

        assert has_provider_access(claims, "vanilla") is True
        assert has_provider_access(claims, "aws") is False


class TestLicenseExceptions:
    def test_license_invalid_error_is_hexawyn_error(self) -> None:
        from hexawyn.infrastructure.license.license_exceptions import LicenseInvalidError

        error = LicenseInvalidError("bad token")
        assert isinstance(error, HexawynError)
        assert str(error) == "bad token"

    def test_license_expired_error_is_hexawyn_error(self) -> None:
        from hexawyn.infrastructure.license.license_exceptions import LicenseExpiredError

        error = LicenseExpiredError("expired")
        assert isinstance(error, HexawynError)

    def test_provider_not_licensed_error_is_hexawyn_error(self) -> None:
        from hexawyn.infrastructure.license.license_exceptions import ProviderNotLicensedError

        error = ProviderNotLicensedError("gcp not licensed")
        assert isinstance(error, HexawynError)


class TestActivateLicense:
    def test_activates_valid_jwt_and_returns_claims(self, tmp_path: Path) -> None:
        private_pem, public_pem = _generate_rsa_keypair()
        token = _sign_jwt(private_pem, {"plan": "scale-up", "clusters_max": -1, "providers": ["*"]})

        key_path = tmp_path / "license.key"

        with patch(
            "hexawyn.infrastructure.license.license_manager.PUBLIC_KEY_PEM",
            public_pem,
        ):
            with patch(
                "hexawyn.infrastructure.license.license_manager.LICENSE_KEY_PATH",
                key_path,
            ):
                from hexawyn.infrastructure.license.license_manager import activate_license

                claims = activate_license(token)
                assert claims.plan == "scale-up"
                assert key_path.exists()
                assert token in key_path.read_text()

    def test_rejects_invalid_jwt(self, tmp_path: Path) -> None:
        _, public_pem = _generate_rsa_keypair()
        key_path = tmp_path / "license.key"

        with patch(
            "hexawyn.infrastructure.license.license_manager.PUBLIC_KEY_PEM",
            public_pem,
        ):
            with patch(
                "hexawyn.infrastructure.license.license_manager.LICENSE_KEY_PATH",
                key_path,
            ):
                from hexawyn.infrastructure.license.license_exceptions import LicenseInvalidError
                from hexawyn.infrastructure.license.license_manager import activate_license

                with pytest.raises(LicenseInvalidError):
                    activate_license("not-a-jwt")
                assert not key_path.exists()

    def test_activate_license_rejects_expired_jwt(self, tmp_path: Path) -> None:
        private_pem, public_pem = _generate_rsa_keypair()
        token = _sign_jwt(private_pem, {"plan": "dev", "exp": 1000000000})
        key_path = tmp_path / "license.key"

        with patch(
            "hexawyn.infrastructure.license.license_manager.PUBLIC_KEY_PEM",
            public_pem,
        ):
            with patch(
                "hexawyn.infrastructure.license.license_manager.LICENSE_KEY_PATH",
                key_path,
            ):
                from hexawyn.infrastructure.license.license_exceptions import LicenseInvalidError
                from hexawyn.infrastructure.license.license_manager import activate_license

                with pytest.raises(LicenseInvalidError):
                    activate_license(token)
                assert not key_path.exists()


class TestBackwardCompatibility:
    def test_get_license_tier_returns_tier_from_jwt(self) -> None:
        private_pem, public_pem = _generate_rsa_keypair()
        token = _sign_jwt(private_pem, {"plan": "team"})

        with patch(
            "hexawyn.infrastructure.license.license_manager._read_license_key",
            return_value=token,
        ):
            with patch(
                "hexawyn.infrastructure.license.license_manager.PUBLIC_KEY_PEM",
                public_pem,
            ):
                from hexawyn.infrastructure.license.license_manager import get_license_tier

                assert get_license_tier() == LicenseTier.TEAM

    def test_get_current_tier_alias(self) -> None:
        with patch(
            "hexawyn.infrastructure.license.license_manager._read_license_key",
            return_value=None,
        ):
            from hexawyn.infrastructure.license.license_manager import get_current_tier

            assert get_current_tier() == LicenseTier.STARTER

    def test_is_pro_returns_true_for_paid_plan(self) -> None:
        private_pem, public_pem = _generate_rsa_keypair()
        token = _sign_jwt(private_pem, {"plan": "team"})

        with patch(
            "hexawyn.infrastructure.license.license_manager._read_license_key",
            return_value=token,
        ):
            with patch(
                "hexawyn.infrastructure.license.license_manager.PUBLIC_KEY_PEM",
                public_pem,
            ):
                from hexawyn.infrastructure.license.license_manager import is_pro

                assert is_pro() is True

    def test_is_pro_returns_false_for_free(self) -> None:
        with patch(
            "hexawyn.infrastructure.license.license_manager._read_license_key",
            return_value=None,
        ):
            from hexawyn.infrastructure.license.license_manager import is_pro

            assert is_pro() is False

    def test_get_license_tier_with_expired_jwt_returns_free(self) -> None:
        private_pem, public_pem = _generate_rsa_keypair()
        token = _sign_jwt(private_pem, {"plan": "dev", "exp": 1000000000})

        with patch(
            "hexawyn.infrastructure.license.license_manager._read_license_key",
            return_value=token,
        ):
            with patch(
                "hexawyn.infrastructure.license.license_manager.PUBLIC_KEY_PEM",
                public_pem,
            ):
                from hexawyn.infrastructure.license.license_manager import get_license_tier

                assert get_license_tier() == LicenseTier.STARTER

    def test_read_license_key_from_file(self, tmp_path: Path) -> None:
        private_pem, public_pem = _generate_rsa_keypair()
        token = _sign_jwt(private_pem, {"plan": "scale-up", "providers": ["*"]})
        key_path = tmp_path / "license.key"
        key_path.write_text(token)

        with patch.dict(os.environ, {}, clear=True):
            with patch(
                "hexawyn.infrastructure.license.license_manager.LICENSE_KEY_PATH",
                key_path,
            ):
                with patch(
                    "hexawyn.infrastructure.license.license_manager.PUBLIC_KEY_PEM",
                    public_pem,
                ):
                    from hexawyn.infrastructure.license.license_manager import (
                        _read_license_key,
                    )

                    result = _read_license_key()
                    assert result == token

    def test_read_license_key_file_not_found(self, tmp_path: Path) -> None:
        key_path = tmp_path / "missing.key"

        with patch.dict(os.environ, {}, clear=True):
            with patch(
                "hexawyn.infrastructure.license.license_manager.LICENSE_KEY_PATH",
                key_path,
            ):
                from hexawyn.infrastructure.license.license_manager import (
                    _read_license_key,
                )

                result = _read_license_key()
                assert result is None

    def test_read_license_key_from_env(self) -> None:
        private_pem, _ = _generate_rsa_keypair()
        token = _sign_jwt(private_pem, {"plan": "dev"})

        with patch.dict(os.environ, {"HEXAWYN_LICENSE_KEY": token}):
            from hexawyn.infrastructure.license.license_manager import _read_license_key

            result = _read_license_key()
            assert result == token
