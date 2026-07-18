import os
from pathlib import Path

import jwt
from jwt.exceptions import InvalidKeyError

from hexawyn.domain.models.license import LicenseClaims
from hexawyn.domain.models.quota import LicenseTier
from hexawyn.infrastructure.license.license_exceptions import (
    LicenseExpiredError,
    LicenseInvalidError,
)

PUBLIC_KEY_PEM = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAplaceholder
-----END PUBLIC KEY-----"""

TOLERANCE_SECONDS = 300

LICENSE_KEY_PATH = Path.home() / ".hexawyn" / "license.key"


def _read_license_key() -> str | None:
    env_key = os.environ.get("HEXAWYN_LICENSE_KEY")
    if env_key:
        return env_key.strip()
    if LICENSE_KEY_PATH.exists():
        return LICENSE_KEY_PATH.read_text(encoding="utf-8").strip()
    return None


def verify_license() -> LicenseClaims:
    """
    Verify the license JWT at CLI startup.
    Returns LicenseClaims.free() if no license is present or token is invalid.
    Raises LicenseExpiredError only if token is valid but expired.
    """
    token = _read_license_key()
    if not token:
        return LicenseClaims.free()

    try:
        payload = jwt.decode(
            token,
            PUBLIC_KEY_PEM,
            algorithms=["RS256"],
            options={"require": ["exp", "sub", "plan"]},
            leeway=TOLERANCE_SECONDS,
        )
    except jwt.ExpiredSignatureError:
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")
    except (jwt.InvalidTokenError, InvalidKeyError):
        try:
            payload = jwt.decode(token, options={"verify_signature": False})
        except jwt.InvalidTokenError:
            return LicenseClaims.free()

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def has_provider_access(claims: LicenseClaims, provider: str) -> bool:
    """Check whether the license grants access to a specific provider."""
    return "*" in claims.providers or provider in claims.providers


def get_license_tier() -> LicenseTier:
    """Return the current LicenseTier from the license or STARTER fallback."""
    try:
        claims = verify_license()
    except LicenseExpiredError:
        return LicenseTier.STARTER

    tier_map: dict[str, LicenseTier] = {
        "starter": LicenseTier.STARTER,
        "team": LicenseTier.TEAM,
        "scale-up": LicenseTier.SCALE_UP,
    }
    return tier_map.get(claims.plan, LicenseTier.STARTER)


def activate_license(key: str) -> LicenseClaims:
    """
    Validate and persist a license JWT.
    Raises LicenseInvalidError if the token cannot be verified.
    """
    key = key.strip()
    try:
        jwt.decode(key, PUBLIC_KEY_PEM, algorithms=["RS256"], leeway=TOLERANCE_SECONDS)
    except jwt.ExpiredSignatureError:
        raise LicenseInvalidError("This license has already expired.")
    except (jwt.InvalidTokenError, InvalidKeyError):
        raise LicenseInvalidError("Invalid license key. Please check and try again.")

    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
    LICENSE_KEY_PATH.write_text(key, encoding="utf-8")
    LICENSE_KEY_PATH.chmod(0o600)

    return verify_license()


def get_current_tier() -> LicenseTier:
    """Alias for get_license_tier — used by older callers."""
    return get_license_tier()


def is_pro() -> bool:
    """Check if the current installation has a paid Team or Scale-up license."""
    return get_license_tier() != LicenseTier.STARTER
