import base64
import os
from datetime import UTC, datetime
from pathlib import Path

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

from hexawyn.domain.errors import HexawynError
from hexawyn.domain.models.license import LicenseKey
from hexawyn.domain.models.quota import LicenseTier

HEXAWYN_PUBLIC_KEY_B64 = "TBD_REPLACE_WITH_REAL_ED25519_PUBLIC_KEY_BASE64"

LICENSE_KEY_PATH = Path.home() / ".hexawyn" / "license.key"

_SEPARATOR = "."


class LicenseValidationError(HexawynError):
    """Raised when a license key is invalid or expired."""


def _load_public_key() -> Ed25519PublicKey:
    raw = base64.b64decode(HEXAWYN_PUBLIC_KEY_B64)
    return Ed25519PublicKey.from_public_bytes(raw)


def _read_license_key() -> str | None:
    env_key = os.environ.get("HEXAWYN_LICENSE_KEY")
    if env_key:
        return env_key.strip()
    if LICENSE_KEY_PATH.exists():
        return LICENSE_KEY_PATH.read_text(encoding="utf-8").strip()
    return None


def _decode_token(token: str) -> LicenseKey:
    parts = token.split(_SEPARATOR)
    if len(parts) != 3:
        raise LicenseValidationError(
            "Invalid license key format. Expected: payload.signature (3 parts)."
        )
    payload_b64, sig_b64, _ = parts

    try:
        payload_bytes = base64.urlsafe_b64decode(payload_b64 + "==")
        sig_bytes = base64.urlsafe_b64decode(sig_b64 + "==")
    except Exception as e:
        raise LicenseValidationError("Invalid license key encoding.") from e

    public_key = _load_public_key()
    try:
        public_key.verify(sig_bytes, payload_bytes)
    except InvalidSignature as e:
        raise LicenseValidationError(
            "License key signature invalid. The key may have been tampered with."
        ) from e

    payload_str = payload_bytes.decode("utf-8")
    fields = payload_str.split(":")
    if len(fields) < 2:
        raise LicenseValidationError("Invalid license key payload.")

    tier_str = fields[0].lower()
    try:
        tier = LicenseTier(tier_str)
    except ValueError:
        raise LicenseValidationError(f"Unknown tier in license key: {tier_str}")

    expires_at: datetime | None = None
    if len(fields) >= 2 and fields[1]:
        try:
            expires_at = datetime.fromisoformat(fields[1]).replace(tzinfo=UTC)
        except ValueError as e:
            raise LicenseValidationError("Invalid expiration date in license key.") from e

    licensee = fields[2] if len(fields) >= 3 else "unknown"

    key = LicenseKey(tier=tier, expires_at=expires_at, licensee=licensee)

    if key.is_expired:
        raise LicenseValidationError(
            f"License key expired on {expires_at.strftime('%Y-%m-%d') if expires_at else 'unknown'}."
        )

    return key


def get_license_tier() -> LicenseTier:
    """
    Returns the current license tier.

    Priority:
    1. HEXAWYN_LICENSE_KEY env var
    2. ~/.hexawyn/license.key file
    3. Fallback to FREE tier

    Returns:
        LicenseTier.FREE if no valid license found.
    """
    token = _read_license_key()
    if token is None:
        return LicenseTier.FREE

    try:
        key = _decode_token(token)
        return key.tier
    except LicenseValidationError:
        return LicenseTier.FREE
    except Exception:
        return LicenseTier.FREE


def activate_license(key: str) -> LicenseKey:
    """
    Validate and persist a license key.

    Args:
        key: The raw license key string.

    Returns:
        The decoded LicenseKey.

    Raises:
        LicenseValidationError: if the key is invalid or expired.
    """
    license_key = _decode_token(key.strip())
    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
    LICENSE_KEY_PATH.write_text(key.strip(), encoding="utf-8")
    LICENSE_KEY_PATH.chmod(0o600)
    return license_key


def get_current_tier() -> LicenseTier:
    """Alias for get_license_tier — used by older callers."""
    return get_license_tier()


def is_pro() -> bool:
    """Check if the current installation has a valid Pro license."""
    return get_license_tier() != LicenseTier.FREE
