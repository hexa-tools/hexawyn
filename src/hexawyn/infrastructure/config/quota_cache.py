"""Encrypted local cache of the last control-plane quota response.

The investigation quota is owned by the control plane (``/api/v1/quota``).
This cache persists the last successfully fetched response so that, when the
control plane is unreachable, the client can still report a *last-known*
server value instead of a hardcoded per-tier grid.

Trust model (Option A / neutral):
- The cache holds only a per-install mirror; it is encrypted at rest (0o600)
  so it does not leak usage figures.
- It is a *freshness/confidentiality* mirror, NOT an authenticity boundary.
  A missing or undecryptable cache is treated as "quota unknown locally",
  never as a fabricated number.
"""

from __future__ import annotations

import json
import logging
import secrets
from datetime import UTC, datetime
from pathlib import Path
from typing import TypedDict, cast

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

from hexawyn.application.ports.driven.runtime_port import QuotaCheckResult
from hexawyn.domain.errors import EncryptionError
from hexawyn.infrastructure.memory.encryption import derive_key, is_encryption_disabled

logger = logging.getLogger(__name__)

QUOTA_CACHE_PATH = Path.home() / ".hexawyn" / "quota.cache"


class CachedQuota(TypedDict):
    allowed: bool
    used: int
    limit: int
    remaining: int
    stored_at: str


def _encrypt_data(key: bytes, plaintext: bytes) -> bytes:
    nonce = secrets.token_bytes(12)
    aesgcm = AESGCM(key)
    return nonce + aesgcm.encrypt(nonce, plaintext, None)


def _decrypt_data(key: bytes, data: bytes) -> bytes:
    if len(data) < 13:  # noqa: PLR2004
        raise EncryptionError("Quota cache is too short to decrypt.")
    nonce, ciphertext = data[:12], data[12:]
    return AESGCM(key).decrypt(nonce, ciphertext, None)


def _payload(result: QuotaCheckResult) -> CachedQuota:
    return {
        "allowed": result["allowed"],
        "used": int(result["used"]),
        "limit": int(result["limit"]),
        "remaining": int(result["remaining"]),
        "stored_at": datetime.now(UTC).isoformat(),
    }


def save_quota(result: QuotaCheckResult) -> None:
    """Persist the last control-plane quota response (encrypted, 0o600)."""
    plaintext = json.dumps(_payload(result)).encode("utf-8")
    data = plaintext if is_encryption_disabled() else _encrypt_data(derive_key(), plaintext)
    QUOTA_CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    QUOTA_CACHE_PATH.write_bytes(data)
    QUOTA_CACHE_PATH.chmod(0o600)


def load_quota() -> QuotaCheckResult | None:
    """Return the cached quota, or ``None`` when absent or unreadable.

    ``None`` means "quota unknown locally" (Option A neutral) — never a
    fabricated number.
    """
    if not QUOTA_CACHE_PATH.exists():
        return None
    try:
        data = QUOTA_CACHE_PATH.read_bytes()
        if not is_encryption_disabled():
            data = _decrypt_data(derive_key(), data)
        payload = cast(CachedQuota, json.loads(data.decode("utf-8")))
        return QuotaCheckResult(
            allowed=bool(payload["allowed"]),
            used=int(payload["used"]),
            limit=int(payload["limit"]),
            remaining=int(payload["remaining"]),
        )
    except (EncryptionError, KeyError, ValueError, json.JSONDecodeError) as exc:
        logger.warning("Could not read quota cache: %s", exc)
        return None


def clear_quota() -> None:
    """Remove the cached quota (used by tests and forced resync)."""
    QUOTA_CACHE_PATH.unlink(missing_ok=True)
