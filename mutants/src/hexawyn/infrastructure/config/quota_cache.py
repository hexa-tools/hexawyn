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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class CachedQuota(TypedDict):
    allowed: bool
    used: int
    limit: int
    remaining: int
    stored_at: str
mutants_x__encrypt_data__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__encrypt_data__mutmut)
def _encrypt_data(key: bytes, plaintext: bytes) -> bytes:
    nonce = secrets.token_bytes(12)
    aesgcm = AESGCM(key)
    return nonce + aesgcm.encrypt(nonce, plaintext, None)


def x__encrypt_data__mutmut_orig(key: bytes, plaintext: bytes) -> bytes:
    nonce = secrets.token_bytes(12)
    aesgcm = AESGCM(key)
    return nonce + aesgcm.encrypt(nonce, plaintext, None)


def x__encrypt_data__mutmut_1(key: bytes, plaintext: bytes) -> bytes:
    nonce = None
    aesgcm = AESGCM(key)
    return nonce + aesgcm.encrypt(nonce, plaintext, None)


def x__encrypt_data__mutmut_2(key: bytes, plaintext: bytes) -> bytes:
    nonce = secrets.token_bytes(None)
    aesgcm = AESGCM(key)
    return nonce + aesgcm.encrypt(nonce, plaintext, None)


def x__encrypt_data__mutmut_3(key: bytes, plaintext: bytes) -> bytes:
    nonce = secrets.token_bytes(13)
    aesgcm = AESGCM(key)
    return nonce + aesgcm.encrypt(nonce, plaintext, None)


def x__encrypt_data__mutmut_4(key: bytes, plaintext: bytes) -> bytes:
    nonce = secrets.token_bytes(12)
    aesgcm = None
    return nonce + aesgcm.encrypt(nonce, plaintext, None)


def x__encrypt_data__mutmut_5(key: bytes, plaintext: bytes) -> bytes:
    nonce = secrets.token_bytes(12)
    aesgcm = AESGCM(None)
    return nonce + aesgcm.encrypt(nonce, plaintext, None)


def x__encrypt_data__mutmut_6(key: bytes, plaintext: bytes) -> bytes:
    nonce = secrets.token_bytes(12)
    aesgcm = AESGCM(key)
    return nonce - aesgcm.encrypt(nonce, plaintext, None)


def x__encrypt_data__mutmut_7(key: bytes, plaintext: bytes) -> bytes:
    nonce = secrets.token_bytes(12)
    aesgcm = AESGCM(key)
    return nonce + aesgcm.encrypt(None, plaintext, None)


def x__encrypt_data__mutmut_8(key: bytes, plaintext: bytes) -> bytes:
    nonce = secrets.token_bytes(12)
    aesgcm = AESGCM(key)
    return nonce + aesgcm.encrypt(nonce, None, None)


def x__encrypt_data__mutmut_9(key: bytes, plaintext: bytes) -> bytes:
    nonce = secrets.token_bytes(12)
    aesgcm = AESGCM(key)
    return nonce + aesgcm.encrypt(plaintext, None)


def x__encrypt_data__mutmut_10(key: bytes, plaintext: bytes) -> bytes:
    nonce = secrets.token_bytes(12)
    aesgcm = AESGCM(key)
    return nonce + aesgcm.encrypt(nonce, None)


def x__encrypt_data__mutmut_11(key: bytes, plaintext: bytes) -> bytes:
    nonce = secrets.token_bytes(12)
    aesgcm = AESGCM(key)
    return nonce + aesgcm.encrypt(nonce, plaintext, )

mutants_x__encrypt_data__mutmut['_mutmut_orig'] = x__encrypt_data__mutmut_orig # type: ignore # mutmut generated
mutants_x__encrypt_data__mutmut['x__encrypt_data__mutmut_1'] = x__encrypt_data__mutmut_1 # type: ignore # mutmut generated
mutants_x__encrypt_data__mutmut['x__encrypt_data__mutmut_2'] = x__encrypt_data__mutmut_2 # type: ignore # mutmut generated
mutants_x__encrypt_data__mutmut['x__encrypt_data__mutmut_3'] = x__encrypt_data__mutmut_3 # type: ignore # mutmut generated
mutants_x__encrypt_data__mutmut['x__encrypt_data__mutmut_4'] = x__encrypt_data__mutmut_4 # type: ignore # mutmut generated
mutants_x__encrypt_data__mutmut['x__encrypt_data__mutmut_5'] = x__encrypt_data__mutmut_5 # type: ignore # mutmut generated
mutants_x__encrypt_data__mutmut['x__encrypt_data__mutmut_6'] = x__encrypt_data__mutmut_6 # type: ignore # mutmut generated
mutants_x__encrypt_data__mutmut['x__encrypt_data__mutmut_7'] = x__encrypt_data__mutmut_7 # type: ignore # mutmut generated
mutants_x__encrypt_data__mutmut['x__encrypt_data__mutmut_8'] = x__encrypt_data__mutmut_8 # type: ignore # mutmut generated
mutants_x__encrypt_data__mutmut['x__encrypt_data__mutmut_9'] = x__encrypt_data__mutmut_9 # type: ignore # mutmut generated
mutants_x__encrypt_data__mutmut['x__encrypt_data__mutmut_10'] = x__encrypt_data__mutmut_10 # type: ignore # mutmut generated
mutants_x__encrypt_data__mutmut['x__encrypt_data__mutmut_11'] = x__encrypt_data__mutmut_11 # type: ignore # mutmut generated
mutants_x__decrypt_data__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__decrypt_data__mutmut)
def _decrypt_data(key: bytes, data: bytes) -> bytes:
    if len(data) < 13:  # noqa: PLR2004
        raise EncryptionError("Quota cache is too short to decrypt.")
    nonce, ciphertext = data[:12], data[12:]
    return AESGCM(key).decrypt(nonce, ciphertext, None)


def x__decrypt_data__mutmut_orig(key: bytes, data: bytes) -> bytes:
    if len(data) < 13:  # noqa: PLR2004
        raise EncryptionError("Quota cache is too short to decrypt.")
    nonce, ciphertext = data[:12], data[12:]
    return AESGCM(key).decrypt(nonce, ciphertext, None)


def x__decrypt_data__mutmut_1(key: bytes, data: bytes) -> bytes:
    if len(data) <= 13:  # noqa: PLR2004
        raise EncryptionError("Quota cache is too short to decrypt.")
    nonce, ciphertext = data[:12], data[12:]
    return AESGCM(key).decrypt(nonce, ciphertext, None)


def x__decrypt_data__mutmut_2(key: bytes, data: bytes) -> bytes:
    if len(data) < 14:  # noqa: PLR2004
        raise EncryptionError("Quota cache is too short to decrypt.")
    nonce, ciphertext = data[:12], data[12:]
    return AESGCM(key).decrypt(nonce, ciphertext, None)


def x__decrypt_data__mutmut_3(key: bytes, data: bytes) -> bytes:
    if len(data) < 13:  # noqa: PLR2004
        raise EncryptionError(None)
    nonce, ciphertext = data[:12], data[12:]
    return AESGCM(key).decrypt(nonce, ciphertext, None)


def x__decrypt_data__mutmut_4(key: bytes, data: bytes) -> bytes:
    if len(data) < 13:  # noqa: PLR2004
        raise EncryptionError("XXQuota cache is too short to decrypt.XX")
    nonce, ciphertext = data[:12], data[12:]
    return AESGCM(key).decrypt(nonce, ciphertext, None)


def x__decrypt_data__mutmut_5(key: bytes, data: bytes) -> bytes:
    if len(data) < 13:  # noqa: PLR2004
        raise EncryptionError("quota cache is too short to decrypt.")
    nonce, ciphertext = data[:12], data[12:]
    return AESGCM(key).decrypt(nonce, ciphertext, None)


def x__decrypt_data__mutmut_6(key: bytes, data: bytes) -> bytes:
    if len(data) < 13:  # noqa: PLR2004
        raise EncryptionError("QUOTA CACHE IS TOO SHORT TO DECRYPT.")
    nonce, ciphertext = data[:12], data[12:]
    return AESGCM(key).decrypt(nonce, ciphertext, None)


def x__decrypt_data__mutmut_7(key: bytes, data: bytes) -> bytes:
    if len(data) < 13:  # noqa: PLR2004
        raise EncryptionError("Quota cache is too short to decrypt.")
    nonce, ciphertext = None
    return AESGCM(key).decrypt(nonce, ciphertext, None)


def x__decrypt_data__mutmut_8(key: bytes, data: bytes) -> bytes:
    if len(data) < 13:  # noqa: PLR2004
        raise EncryptionError("Quota cache is too short to decrypt.")
    nonce, ciphertext = data[:13], data[12:]
    return AESGCM(key).decrypt(nonce, ciphertext, None)


def x__decrypt_data__mutmut_9(key: bytes, data: bytes) -> bytes:
    if len(data) < 13:  # noqa: PLR2004
        raise EncryptionError("Quota cache is too short to decrypt.")
    nonce, ciphertext = data[:12], data[13:]
    return AESGCM(key).decrypt(nonce, ciphertext, None)


def x__decrypt_data__mutmut_10(key: bytes, data: bytes) -> bytes:
    if len(data) < 13:  # noqa: PLR2004
        raise EncryptionError("Quota cache is too short to decrypt.")
    nonce, ciphertext = data[:12], data[12:]
    return AESGCM(key).decrypt(None, ciphertext, None)


def x__decrypt_data__mutmut_11(key: bytes, data: bytes) -> bytes:
    if len(data) < 13:  # noqa: PLR2004
        raise EncryptionError("Quota cache is too short to decrypt.")
    nonce, ciphertext = data[:12], data[12:]
    return AESGCM(key).decrypt(nonce, None, None)


def x__decrypt_data__mutmut_12(key: bytes, data: bytes) -> bytes:
    if len(data) < 13:  # noqa: PLR2004
        raise EncryptionError("Quota cache is too short to decrypt.")
    nonce, ciphertext = data[:12], data[12:]
    return AESGCM(key).decrypt(ciphertext, None)


def x__decrypt_data__mutmut_13(key: bytes, data: bytes) -> bytes:
    if len(data) < 13:  # noqa: PLR2004
        raise EncryptionError("Quota cache is too short to decrypt.")
    nonce, ciphertext = data[:12], data[12:]
    return AESGCM(key).decrypt(nonce, None)


def x__decrypt_data__mutmut_14(key: bytes, data: bytes) -> bytes:
    if len(data) < 13:  # noqa: PLR2004
        raise EncryptionError("Quota cache is too short to decrypt.")
    nonce, ciphertext = data[:12], data[12:]
    return AESGCM(key).decrypt(nonce, ciphertext, )


def x__decrypt_data__mutmut_15(key: bytes, data: bytes) -> bytes:
    if len(data) < 13:  # noqa: PLR2004
        raise EncryptionError("Quota cache is too short to decrypt.")
    nonce, ciphertext = data[:12], data[12:]
    return AESGCM(None).decrypt(nonce, ciphertext, None)

mutants_x__decrypt_data__mutmut['_mutmut_orig'] = x__decrypt_data__mutmut_orig # type: ignore # mutmut generated
mutants_x__decrypt_data__mutmut['x__decrypt_data__mutmut_1'] = x__decrypt_data__mutmut_1 # type: ignore # mutmut generated
mutants_x__decrypt_data__mutmut['x__decrypt_data__mutmut_2'] = x__decrypt_data__mutmut_2 # type: ignore # mutmut generated
mutants_x__decrypt_data__mutmut['x__decrypt_data__mutmut_3'] = x__decrypt_data__mutmut_3 # type: ignore # mutmut generated
mutants_x__decrypt_data__mutmut['x__decrypt_data__mutmut_4'] = x__decrypt_data__mutmut_4 # type: ignore # mutmut generated
mutants_x__decrypt_data__mutmut['x__decrypt_data__mutmut_5'] = x__decrypt_data__mutmut_5 # type: ignore # mutmut generated
mutants_x__decrypt_data__mutmut['x__decrypt_data__mutmut_6'] = x__decrypt_data__mutmut_6 # type: ignore # mutmut generated
mutants_x__decrypt_data__mutmut['x__decrypt_data__mutmut_7'] = x__decrypt_data__mutmut_7 # type: ignore # mutmut generated
mutants_x__decrypt_data__mutmut['x__decrypt_data__mutmut_8'] = x__decrypt_data__mutmut_8 # type: ignore # mutmut generated
mutants_x__decrypt_data__mutmut['x__decrypt_data__mutmut_9'] = x__decrypt_data__mutmut_9 # type: ignore # mutmut generated
mutants_x__decrypt_data__mutmut['x__decrypt_data__mutmut_10'] = x__decrypt_data__mutmut_10 # type: ignore # mutmut generated
mutants_x__decrypt_data__mutmut['x__decrypt_data__mutmut_11'] = x__decrypt_data__mutmut_11 # type: ignore # mutmut generated
mutants_x__decrypt_data__mutmut['x__decrypt_data__mutmut_12'] = x__decrypt_data__mutmut_12 # type: ignore # mutmut generated
mutants_x__decrypt_data__mutmut['x__decrypt_data__mutmut_13'] = x__decrypt_data__mutmut_13 # type: ignore # mutmut generated
mutants_x__decrypt_data__mutmut['x__decrypt_data__mutmut_14'] = x__decrypt_data__mutmut_14 # type: ignore # mutmut generated
mutants_x__decrypt_data__mutmut['x__decrypt_data__mutmut_15'] = x__decrypt_data__mutmut_15 # type: ignore # mutmut generated
mutants_x__payload__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__payload__mutmut)
def _payload(result: QuotaCheckResult) -> CachedQuota:
    return {
        "allowed": result["allowed"],
        "used": int(result["used"]),
        "limit": int(result["limit"]),
        "remaining": int(result["remaining"]),
        "stored_at": datetime.now(UTC).isoformat(),
    }


def x__payload__mutmut_orig(result: QuotaCheckResult) -> CachedQuota:
    return {
        "allowed": result["allowed"],
        "used": int(result["used"]),
        "limit": int(result["limit"]),
        "remaining": int(result["remaining"]),
        "stored_at": datetime.now(UTC).isoformat(),
    }


def x__payload__mutmut_1(result: QuotaCheckResult) -> CachedQuota:
    return {
        "XXallowedXX": result["allowed"],
        "used": int(result["used"]),
        "limit": int(result["limit"]),
        "remaining": int(result["remaining"]),
        "stored_at": datetime.now(UTC).isoformat(),
    }


def x__payload__mutmut_2(result: QuotaCheckResult) -> CachedQuota:
    return {
        "ALLOWED": result["allowed"],
        "used": int(result["used"]),
        "limit": int(result["limit"]),
        "remaining": int(result["remaining"]),
        "stored_at": datetime.now(UTC).isoformat(),
    }


def x__payload__mutmut_3(result: QuotaCheckResult) -> CachedQuota:
    return {
        "allowed": result["XXallowedXX"],
        "used": int(result["used"]),
        "limit": int(result["limit"]),
        "remaining": int(result["remaining"]),
        "stored_at": datetime.now(UTC).isoformat(),
    }


def x__payload__mutmut_4(result: QuotaCheckResult) -> CachedQuota:
    return {
        "allowed": result["ALLOWED"],
        "used": int(result["used"]),
        "limit": int(result["limit"]),
        "remaining": int(result["remaining"]),
        "stored_at": datetime.now(UTC).isoformat(),
    }


def x__payload__mutmut_5(result: QuotaCheckResult) -> CachedQuota:
    return {
        "allowed": result["allowed"],
        "XXusedXX": int(result["used"]),
        "limit": int(result["limit"]),
        "remaining": int(result["remaining"]),
        "stored_at": datetime.now(UTC).isoformat(),
    }


def x__payload__mutmut_6(result: QuotaCheckResult) -> CachedQuota:
    return {
        "allowed": result["allowed"],
        "USED": int(result["used"]),
        "limit": int(result["limit"]),
        "remaining": int(result["remaining"]),
        "stored_at": datetime.now(UTC).isoformat(),
    }


def x__payload__mutmut_7(result: QuotaCheckResult) -> CachedQuota:
    return {
        "allowed": result["allowed"],
        "used": int(None),
        "limit": int(result["limit"]),
        "remaining": int(result["remaining"]),
        "stored_at": datetime.now(UTC).isoformat(),
    }


def x__payload__mutmut_8(result: QuotaCheckResult) -> CachedQuota:
    return {
        "allowed": result["allowed"],
        "used": int(result["XXusedXX"]),
        "limit": int(result["limit"]),
        "remaining": int(result["remaining"]),
        "stored_at": datetime.now(UTC).isoformat(),
    }


def x__payload__mutmut_9(result: QuotaCheckResult) -> CachedQuota:
    return {
        "allowed": result["allowed"],
        "used": int(result["USED"]),
        "limit": int(result["limit"]),
        "remaining": int(result["remaining"]),
        "stored_at": datetime.now(UTC).isoformat(),
    }


def x__payload__mutmut_10(result: QuotaCheckResult) -> CachedQuota:
    return {
        "allowed": result["allowed"],
        "used": int(result["used"]),
        "XXlimitXX": int(result["limit"]),
        "remaining": int(result["remaining"]),
        "stored_at": datetime.now(UTC).isoformat(),
    }


def x__payload__mutmut_11(result: QuotaCheckResult) -> CachedQuota:
    return {
        "allowed": result["allowed"],
        "used": int(result["used"]),
        "LIMIT": int(result["limit"]),
        "remaining": int(result["remaining"]),
        "stored_at": datetime.now(UTC).isoformat(),
    }


def x__payload__mutmut_12(result: QuotaCheckResult) -> CachedQuota:
    return {
        "allowed": result["allowed"],
        "used": int(result["used"]),
        "limit": int(None),
        "remaining": int(result["remaining"]),
        "stored_at": datetime.now(UTC).isoformat(),
    }


def x__payload__mutmut_13(result: QuotaCheckResult) -> CachedQuota:
    return {
        "allowed": result["allowed"],
        "used": int(result["used"]),
        "limit": int(result["XXlimitXX"]),
        "remaining": int(result["remaining"]),
        "stored_at": datetime.now(UTC).isoformat(),
    }


def x__payload__mutmut_14(result: QuotaCheckResult) -> CachedQuota:
    return {
        "allowed": result["allowed"],
        "used": int(result["used"]),
        "limit": int(result["LIMIT"]),
        "remaining": int(result["remaining"]),
        "stored_at": datetime.now(UTC).isoformat(),
    }


def x__payload__mutmut_15(result: QuotaCheckResult) -> CachedQuota:
    return {
        "allowed": result["allowed"],
        "used": int(result["used"]),
        "limit": int(result["limit"]),
        "XXremainingXX": int(result["remaining"]),
        "stored_at": datetime.now(UTC).isoformat(),
    }


def x__payload__mutmut_16(result: QuotaCheckResult) -> CachedQuota:
    return {
        "allowed": result["allowed"],
        "used": int(result["used"]),
        "limit": int(result["limit"]),
        "REMAINING": int(result["remaining"]),
        "stored_at": datetime.now(UTC).isoformat(),
    }


def x__payload__mutmut_17(result: QuotaCheckResult) -> CachedQuota:
    return {
        "allowed": result["allowed"],
        "used": int(result["used"]),
        "limit": int(result["limit"]),
        "remaining": int(None),
        "stored_at": datetime.now(UTC).isoformat(),
    }


def x__payload__mutmut_18(result: QuotaCheckResult) -> CachedQuota:
    return {
        "allowed": result["allowed"],
        "used": int(result["used"]),
        "limit": int(result["limit"]),
        "remaining": int(result["XXremainingXX"]),
        "stored_at": datetime.now(UTC).isoformat(),
    }


def x__payload__mutmut_19(result: QuotaCheckResult) -> CachedQuota:
    return {
        "allowed": result["allowed"],
        "used": int(result["used"]),
        "limit": int(result["limit"]),
        "remaining": int(result["REMAINING"]),
        "stored_at": datetime.now(UTC).isoformat(),
    }


def x__payload__mutmut_20(result: QuotaCheckResult) -> CachedQuota:
    return {
        "allowed": result["allowed"],
        "used": int(result["used"]),
        "limit": int(result["limit"]),
        "remaining": int(result["remaining"]),
        "XXstored_atXX": datetime.now(UTC).isoformat(),
    }


def x__payload__mutmut_21(result: QuotaCheckResult) -> CachedQuota:
    return {
        "allowed": result["allowed"],
        "used": int(result["used"]),
        "limit": int(result["limit"]),
        "remaining": int(result["remaining"]),
        "STORED_AT": datetime.now(UTC).isoformat(),
    }


def x__payload__mutmut_22(result: QuotaCheckResult) -> CachedQuota:
    return {
        "allowed": result["allowed"],
        "used": int(result["used"]),
        "limit": int(result["limit"]),
        "remaining": int(result["remaining"]),
        "stored_at": datetime.now(None).isoformat(),
    }

mutants_x__payload__mutmut['_mutmut_orig'] = x__payload__mutmut_orig # type: ignore # mutmut generated
mutants_x__payload__mutmut['x__payload__mutmut_1'] = x__payload__mutmut_1 # type: ignore # mutmut generated
mutants_x__payload__mutmut['x__payload__mutmut_2'] = x__payload__mutmut_2 # type: ignore # mutmut generated
mutants_x__payload__mutmut['x__payload__mutmut_3'] = x__payload__mutmut_3 # type: ignore # mutmut generated
mutants_x__payload__mutmut['x__payload__mutmut_4'] = x__payload__mutmut_4 # type: ignore # mutmut generated
mutants_x__payload__mutmut['x__payload__mutmut_5'] = x__payload__mutmut_5 # type: ignore # mutmut generated
mutants_x__payload__mutmut['x__payload__mutmut_6'] = x__payload__mutmut_6 # type: ignore # mutmut generated
mutants_x__payload__mutmut['x__payload__mutmut_7'] = x__payload__mutmut_7 # type: ignore # mutmut generated
mutants_x__payload__mutmut['x__payload__mutmut_8'] = x__payload__mutmut_8 # type: ignore # mutmut generated
mutants_x__payload__mutmut['x__payload__mutmut_9'] = x__payload__mutmut_9 # type: ignore # mutmut generated
mutants_x__payload__mutmut['x__payload__mutmut_10'] = x__payload__mutmut_10 # type: ignore # mutmut generated
mutants_x__payload__mutmut['x__payload__mutmut_11'] = x__payload__mutmut_11 # type: ignore # mutmut generated
mutants_x__payload__mutmut['x__payload__mutmut_12'] = x__payload__mutmut_12 # type: ignore # mutmut generated
mutants_x__payload__mutmut['x__payload__mutmut_13'] = x__payload__mutmut_13 # type: ignore # mutmut generated
mutants_x__payload__mutmut['x__payload__mutmut_14'] = x__payload__mutmut_14 # type: ignore # mutmut generated
mutants_x__payload__mutmut['x__payload__mutmut_15'] = x__payload__mutmut_15 # type: ignore # mutmut generated
mutants_x__payload__mutmut['x__payload__mutmut_16'] = x__payload__mutmut_16 # type: ignore # mutmut generated
mutants_x__payload__mutmut['x__payload__mutmut_17'] = x__payload__mutmut_17 # type: ignore # mutmut generated
mutants_x__payload__mutmut['x__payload__mutmut_18'] = x__payload__mutmut_18 # type: ignore # mutmut generated
mutants_x__payload__mutmut['x__payload__mutmut_19'] = x__payload__mutmut_19 # type: ignore # mutmut generated
mutants_x__payload__mutmut['x__payload__mutmut_20'] = x__payload__mutmut_20 # type: ignore # mutmut generated
mutants_x__payload__mutmut['x__payload__mutmut_21'] = x__payload__mutmut_21 # type: ignore # mutmut generated
mutants_x__payload__mutmut['x__payload__mutmut_22'] = x__payload__mutmut_22 # type: ignore # mutmut generated
mutants_x_save_quota__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_save_quota__mutmut)
def save_quota(result: QuotaCheckResult) -> None:
    """Persist the last control-plane quota response (encrypted, 0o600)."""
    plaintext = json.dumps(_payload(result)).encode("utf-8")
    data = plaintext if is_encryption_disabled() else _encrypt_data(derive_key(), plaintext)
    QUOTA_CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    QUOTA_CACHE_PATH.write_bytes(data)
    QUOTA_CACHE_PATH.chmod(0o600)


def x_save_quota__mutmut_orig(result: QuotaCheckResult) -> None:
    """Persist the last control-plane quota response (encrypted, 0o600)."""
    plaintext = json.dumps(_payload(result)).encode("utf-8")
    data = plaintext if is_encryption_disabled() else _encrypt_data(derive_key(), plaintext)
    QUOTA_CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    QUOTA_CACHE_PATH.write_bytes(data)
    QUOTA_CACHE_PATH.chmod(0o600)


def x_save_quota__mutmut_1(result: QuotaCheckResult) -> None:
    """Persist the last control-plane quota response (encrypted, 0o600)."""
    plaintext = None
    data = plaintext if is_encryption_disabled() else _encrypt_data(derive_key(), plaintext)
    QUOTA_CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    QUOTA_CACHE_PATH.write_bytes(data)
    QUOTA_CACHE_PATH.chmod(0o600)


def x_save_quota__mutmut_2(result: QuotaCheckResult) -> None:
    """Persist the last control-plane quota response (encrypted, 0o600)."""
    plaintext = json.dumps(_payload(result)).encode(None)
    data = plaintext if is_encryption_disabled() else _encrypt_data(derive_key(), plaintext)
    QUOTA_CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    QUOTA_CACHE_PATH.write_bytes(data)
    QUOTA_CACHE_PATH.chmod(0o600)


def x_save_quota__mutmut_3(result: QuotaCheckResult) -> None:
    """Persist the last control-plane quota response (encrypted, 0o600)."""
    plaintext = json.dumps(None).encode("utf-8")
    data = plaintext if is_encryption_disabled() else _encrypt_data(derive_key(), plaintext)
    QUOTA_CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    QUOTA_CACHE_PATH.write_bytes(data)
    QUOTA_CACHE_PATH.chmod(0o600)


def x_save_quota__mutmut_4(result: QuotaCheckResult) -> None:
    """Persist the last control-plane quota response (encrypted, 0o600)."""
    plaintext = json.dumps(_payload(None)).encode("utf-8")
    data = plaintext if is_encryption_disabled() else _encrypt_data(derive_key(), plaintext)
    QUOTA_CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    QUOTA_CACHE_PATH.write_bytes(data)
    QUOTA_CACHE_PATH.chmod(0o600)


def x_save_quota__mutmut_5(result: QuotaCheckResult) -> None:
    """Persist the last control-plane quota response (encrypted, 0o600)."""
    plaintext = json.dumps(_payload(result)).encode("XXutf-8XX")
    data = plaintext if is_encryption_disabled() else _encrypt_data(derive_key(), plaintext)
    QUOTA_CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    QUOTA_CACHE_PATH.write_bytes(data)
    QUOTA_CACHE_PATH.chmod(0o600)


def x_save_quota__mutmut_6(result: QuotaCheckResult) -> None:
    """Persist the last control-plane quota response (encrypted, 0o600)."""
    plaintext = json.dumps(_payload(result)).encode("UTF-8")
    data = plaintext if is_encryption_disabled() else _encrypt_data(derive_key(), plaintext)
    QUOTA_CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    QUOTA_CACHE_PATH.write_bytes(data)
    QUOTA_CACHE_PATH.chmod(0o600)


def x_save_quota__mutmut_7(result: QuotaCheckResult) -> None:
    """Persist the last control-plane quota response (encrypted, 0o600)."""
    plaintext = json.dumps(_payload(result)).encode("utf-8")
    data = None
    QUOTA_CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    QUOTA_CACHE_PATH.write_bytes(data)
    QUOTA_CACHE_PATH.chmod(0o600)


def x_save_quota__mutmut_8(result: QuotaCheckResult) -> None:
    """Persist the last control-plane quota response (encrypted, 0o600)."""
    plaintext = json.dumps(_payload(result)).encode("utf-8")
    data = plaintext if is_encryption_disabled() else _encrypt_data(None, plaintext)
    QUOTA_CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    QUOTA_CACHE_PATH.write_bytes(data)
    QUOTA_CACHE_PATH.chmod(0o600)


def x_save_quota__mutmut_9(result: QuotaCheckResult) -> None:
    """Persist the last control-plane quota response (encrypted, 0o600)."""
    plaintext = json.dumps(_payload(result)).encode("utf-8")
    data = plaintext if is_encryption_disabled() else _encrypt_data(derive_key(), None)
    QUOTA_CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    QUOTA_CACHE_PATH.write_bytes(data)
    QUOTA_CACHE_PATH.chmod(0o600)


def x_save_quota__mutmut_10(result: QuotaCheckResult) -> None:
    """Persist the last control-plane quota response (encrypted, 0o600)."""
    plaintext = json.dumps(_payload(result)).encode("utf-8")
    data = plaintext if is_encryption_disabled() else _encrypt_data(plaintext)
    QUOTA_CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    QUOTA_CACHE_PATH.write_bytes(data)
    QUOTA_CACHE_PATH.chmod(0o600)


def x_save_quota__mutmut_11(result: QuotaCheckResult) -> None:
    """Persist the last control-plane quota response (encrypted, 0o600)."""
    plaintext = json.dumps(_payload(result)).encode("utf-8")
    data = plaintext if is_encryption_disabled() else _encrypt_data(derive_key(), )
    QUOTA_CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    QUOTA_CACHE_PATH.write_bytes(data)
    QUOTA_CACHE_PATH.chmod(0o600)


def x_save_quota__mutmut_12(result: QuotaCheckResult) -> None:
    """Persist the last control-plane quota response (encrypted, 0o600)."""
    plaintext = json.dumps(_payload(result)).encode("utf-8")
    data = plaintext if is_encryption_disabled() else _encrypt_data(derive_key(), plaintext)
    QUOTA_CACHE_PATH.parent.mkdir(parents=None, exist_ok=True)
    QUOTA_CACHE_PATH.write_bytes(data)
    QUOTA_CACHE_PATH.chmod(0o600)


def x_save_quota__mutmut_13(result: QuotaCheckResult) -> None:
    """Persist the last control-plane quota response (encrypted, 0o600)."""
    plaintext = json.dumps(_payload(result)).encode("utf-8")
    data = plaintext if is_encryption_disabled() else _encrypt_data(derive_key(), plaintext)
    QUOTA_CACHE_PATH.parent.mkdir(parents=True, exist_ok=None)
    QUOTA_CACHE_PATH.write_bytes(data)
    QUOTA_CACHE_PATH.chmod(0o600)


def x_save_quota__mutmut_14(result: QuotaCheckResult) -> None:
    """Persist the last control-plane quota response (encrypted, 0o600)."""
    plaintext = json.dumps(_payload(result)).encode("utf-8")
    data = plaintext if is_encryption_disabled() else _encrypt_data(derive_key(), plaintext)
    QUOTA_CACHE_PATH.parent.mkdir(exist_ok=True)
    QUOTA_CACHE_PATH.write_bytes(data)
    QUOTA_CACHE_PATH.chmod(0o600)


def x_save_quota__mutmut_15(result: QuotaCheckResult) -> None:
    """Persist the last control-plane quota response (encrypted, 0o600)."""
    plaintext = json.dumps(_payload(result)).encode("utf-8")
    data = plaintext if is_encryption_disabled() else _encrypt_data(derive_key(), plaintext)
    QUOTA_CACHE_PATH.parent.mkdir(parents=True, )
    QUOTA_CACHE_PATH.write_bytes(data)
    QUOTA_CACHE_PATH.chmod(0o600)


def x_save_quota__mutmut_16(result: QuotaCheckResult) -> None:
    """Persist the last control-plane quota response (encrypted, 0o600)."""
    plaintext = json.dumps(_payload(result)).encode("utf-8")
    data = plaintext if is_encryption_disabled() else _encrypt_data(derive_key(), plaintext)
    QUOTA_CACHE_PATH.parent.mkdir(parents=False, exist_ok=True)
    QUOTA_CACHE_PATH.write_bytes(data)
    QUOTA_CACHE_PATH.chmod(0o600)


def x_save_quota__mutmut_17(result: QuotaCheckResult) -> None:
    """Persist the last control-plane quota response (encrypted, 0o600)."""
    plaintext = json.dumps(_payload(result)).encode("utf-8")
    data = plaintext if is_encryption_disabled() else _encrypt_data(derive_key(), plaintext)
    QUOTA_CACHE_PATH.parent.mkdir(parents=True, exist_ok=False)
    QUOTA_CACHE_PATH.write_bytes(data)
    QUOTA_CACHE_PATH.chmod(0o600)


def x_save_quota__mutmut_18(result: QuotaCheckResult) -> None:
    """Persist the last control-plane quota response (encrypted, 0o600)."""
    plaintext = json.dumps(_payload(result)).encode("utf-8")
    data = plaintext if is_encryption_disabled() else _encrypt_data(derive_key(), plaintext)
    QUOTA_CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    QUOTA_CACHE_PATH.write_bytes(None)
    QUOTA_CACHE_PATH.chmod(0o600)


def x_save_quota__mutmut_19(result: QuotaCheckResult) -> None:
    """Persist the last control-plane quota response (encrypted, 0o600)."""
    plaintext = json.dumps(_payload(result)).encode("utf-8")
    data = plaintext if is_encryption_disabled() else _encrypt_data(derive_key(), plaintext)
    QUOTA_CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    QUOTA_CACHE_PATH.write_bytes(data)
    QUOTA_CACHE_PATH.chmod(None)


def x_save_quota__mutmut_20(result: QuotaCheckResult) -> None:
    """Persist the last control-plane quota response (encrypted, 0o600)."""
    plaintext = json.dumps(_payload(result)).encode("utf-8")
    data = plaintext if is_encryption_disabled() else _encrypt_data(derive_key(), plaintext)
    QUOTA_CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    QUOTA_CACHE_PATH.write_bytes(data)
    QUOTA_CACHE_PATH.chmod(385)

mutants_x_save_quota__mutmut['_mutmut_orig'] = x_save_quota__mutmut_orig # type: ignore # mutmut generated
mutants_x_save_quota__mutmut['x_save_quota__mutmut_1'] = x_save_quota__mutmut_1 # type: ignore # mutmut generated
mutants_x_save_quota__mutmut['x_save_quota__mutmut_2'] = x_save_quota__mutmut_2 # type: ignore # mutmut generated
mutants_x_save_quota__mutmut['x_save_quota__mutmut_3'] = x_save_quota__mutmut_3 # type: ignore # mutmut generated
mutants_x_save_quota__mutmut['x_save_quota__mutmut_4'] = x_save_quota__mutmut_4 # type: ignore # mutmut generated
mutants_x_save_quota__mutmut['x_save_quota__mutmut_5'] = x_save_quota__mutmut_5 # type: ignore # mutmut generated
mutants_x_save_quota__mutmut['x_save_quota__mutmut_6'] = x_save_quota__mutmut_6 # type: ignore # mutmut generated
mutants_x_save_quota__mutmut['x_save_quota__mutmut_7'] = x_save_quota__mutmut_7 # type: ignore # mutmut generated
mutants_x_save_quota__mutmut['x_save_quota__mutmut_8'] = x_save_quota__mutmut_8 # type: ignore # mutmut generated
mutants_x_save_quota__mutmut['x_save_quota__mutmut_9'] = x_save_quota__mutmut_9 # type: ignore # mutmut generated
mutants_x_save_quota__mutmut['x_save_quota__mutmut_10'] = x_save_quota__mutmut_10 # type: ignore # mutmut generated
mutants_x_save_quota__mutmut['x_save_quota__mutmut_11'] = x_save_quota__mutmut_11 # type: ignore # mutmut generated
mutants_x_save_quota__mutmut['x_save_quota__mutmut_12'] = x_save_quota__mutmut_12 # type: ignore # mutmut generated
mutants_x_save_quota__mutmut['x_save_quota__mutmut_13'] = x_save_quota__mutmut_13 # type: ignore # mutmut generated
mutants_x_save_quota__mutmut['x_save_quota__mutmut_14'] = x_save_quota__mutmut_14 # type: ignore # mutmut generated
mutants_x_save_quota__mutmut['x_save_quota__mutmut_15'] = x_save_quota__mutmut_15 # type: ignore # mutmut generated
mutants_x_save_quota__mutmut['x_save_quota__mutmut_16'] = x_save_quota__mutmut_16 # type: ignore # mutmut generated
mutants_x_save_quota__mutmut['x_save_quota__mutmut_17'] = x_save_quota__mutmut_17 # type: ignore # mutmut generated
mutants_x_save_quota__mutmut['x_save_quota__mutmut_18'] = x_save_quota__mutmut_18 # type: ignore # mutmut generated
mutants_x_save_quota__mutmut['x_save_quota__mutmut_19'] = x_save_quota__mutmut_19 # type: ignore # mutmut generated
mutants_x_save_quota__mutmut['x_save_quota__mutmut_20'] = x_save_quota__mutmut_20 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_load_quota__mutmut)
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


def x_load_quota__mutmut_orig() -> QuotaCheckResult | None:
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


def x_load_quota__mutmut_1() -> QuotaCheckResult | None:
    """Return the cached quota, or ``None`` when absent or unreadable.

    ``None`` means "quota unknown locally" (Option A neutral) — never a
    fabricated number.
    """
    if QUOTA_CACHE_PATH.exists():
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


def x_load_quota__mutmut_2() -> QuotaCheckResult | None:
    """Return the cached quota, or ``None`` when absent or unreadable.

    ``None`` means "quota unknown locally" (Option A neutral) — never a
    fabricated number.
    """
    if not QUOTA_CACHE_PATH.exists():
        return None
    try:
        data = None
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


def x_load_quota__mutmut_3() -> QuotaCheckResult | None:
    """Return the cached quota, or ``None`` when absent or unreadable.

    ``None`` means "quota unknown locally" (Option A neutral) — never a
    fabricated number.
    """
    if not QUOTA_CACHE_PATH.exists():
        return None
    try:
        data = QUOTA_CACHE_PATH.read_bytes()
        if is_encryption_disabled():
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


def x_load_quota__mutmut_4() -> QuotaCheckResult | None:
    """Return the cached quota, or ``None`` when absent or unreadable.

    ``None`` means "quota unknown locally" (Option A neutral) — never a
    fabricated number.
    """
    if not QUOTA_CACHE_PATH.exists():
        return None
    try:
        data = QUOTA_CACHE_PATH.read_bytes()
        if not is_encryption_disabled():
            data = None
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


def x_load_quota__mutmut_5() -> QuotaCheckResult | None:
    """Return the cached quota, or ``None`` when absent or unreadable.

    ``None`` means "quota unknown locally" (Option A neutral) — never a
    fabricated number.
    """
    if not QUOTA_CACHE_PATH.exists():
        return None
    try:
        data = QUOTA_CACHE_PATH.read_bytes()
        if not is_encryption_disabled():
            data = _decrypt_data(None, data)
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


def x_load_quota__mutmut_6() -> QuotaCheckResult | None:
    """Return the cached quota, or ``None`` when absent or unreadable.

    ``None`` means "quota unknown locally" (Option A neutral) — never a
    fabricated number.
    """
    if not QUOTA_CACHE_PATH.exists():
        return None
    try:
        data = QUOTA_CACHE_PATH.read_bytes()
        if not is_encryption_disabled():
            data = _decrypt_data(derive_key(), None)
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


def x_load_quota__mutmut_7() -> QuotaCheckResult | None:
    """Return the cached quota, or ``None`` when absent or unreadable.

    ``None`` means "quota unknown locally" (Option A neutral) — never a
    fabricated number.
    """
    if not QUOTA_CACHE_PATH.exists():
        return None
    try:
        data = QUOTA_CACHE_PATH.read_bytes()
        if not is_encryption_disabled():
            data = _decrypt_data(data)
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


def x_load_quota__mutmut_8() -> QuotaCheckResult | None:
    """Return the cached quota, or ``None`` when absent or unreadable.

    ``None`` means "quota unknown locally" (Option A neutral) — never a
    fabricated number.
    """
    if not QUOTA_CACHE_PATH.exists():
        return None
    try:
        data = QUOTA_CACHE_PATH.read_bytes()
        if not is_encryption_disabled():
            data = _decrypt_data(derive_key(), )
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


def x_load_quota__mutmut_9() -> QuotaCheckResult | None:
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
        payload = None
        return QuotaCheckResult(
            allowed=bool(payload["allowed"]),
            used=int(payload["used"]),
            limit=int(payload["limit"]),
            remaining=int(payload["remaining"]),
        )
    except (EncryptionError, KeyError, ValueError, json.JSONDecodeError) as exc:
        logger.warning("Could not read quota cache: %s", exc)
        return None


def x_load_quota__mutmut_10() -> QuotaCheckResult | None:
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
        payload = cast(None, json.loads(data.decode("utf-8")))
        return QuotaCheckResult(
            allowed=bool(payload["allowed"]),
            used=int(payload["used"]),
            limit=int(payload["limit"]),
            remaining=int(payload["remaining"]),
        )
    except (EncryptionError, KeyError, ValueError, json.JSONDecodeError) as exc:
        logger.warning("Could not read quota cache: %s", exc)
        return None


def x_load_quota__mutmut_11() -> QuotaCheckResult | None:
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
        payload = cast(CachedQuota, None)
        return QuotaCheckResult(
            allowed=bool(payload["allowed"]),
            used=int(payload["used"]),
            limit=int(payload["limit"]),
            remaining=int(payload["remaining"]),
        )
    except (EncryptionError, KeyError, ValueError, json.JSONDecodeError) as exc:
        logger.warning("Could not read quota cache: %s", exc)
        return None


def x_load_quota__mutmut_12() -> QuotaCheckResult | None:
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
        payload = cast(json.loads(data.decode("utf-8")))
        return QuotaCheckResult(
            allowed=bool(payload["allowed"]),
            used=int(payload["used"]),
            limit=int(payload["limit"]),
            remaining=int(payload["remaining"]),
        )
    except (EncryptionError, KeyError, ValueError, json.JSONDecodeError) as exc:
        logger.warning("Could not read quota cache: %s", exc)
        return None


def x_load_quota__mutmut_13() -> QuotaCheckResult | None:
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
        payload = cast(CachedQuota, )
        return QuotaCheckResult(
            allowed=bool(payload["allowed"]),
            used=int(payload["used"]),
            limit=int(payload["limit"]),
            remaining=int(payload["remaining"]),
        )
    except (EncryptionError, KeyError, ValueError, json.JSONDecodeError) as exc:
        logger.warning("Could not read quota cache: %s", exc)
        return None


def x_load_quota__mutmut_14() -> QuotaCheckResult | None:
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
        payload = cast(CachedQuota, json.loads(None))
        return QuotaCheckResult(
            allowed=bool(payload["allowed"]),
            used=int(payload["used"]),
            limit=int(payload["limit"]),
            remaining=int(payload["remaining"]),
        )
    except (EncryptionError, KeyError, ValueError, json.JSONDecodeError) as exc:
        logger.warning("Could not read quota cache: %s", exc)
        return None


def x_load_quota__mutmut_15() -> QuotaCheckResult | None:
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
        payload = cast(CachedQuota, json.loads(data.decode(None)))
        return QuotaCheckResult(
            allowed=bool(payload["allowed"]),
            used=int(payload["used"]),
            limit=int(payload["limit"]),
            remaining=int(payload["remaining"]),
        )
    except (EncryptionError, KeyError, ValueError, json.JSONDecodeError) as exc:
        logger.warning("Could not read quota cache: %s", exc)
        return None


def x_load_quota__mutmut_16() -> QuotaCheckResult | None:
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
        payload = cast(CachedQuota, json.loads(data.decode("XXutf-8XX")))
        return QuotaCheckResult(
            allowed=bool(payload["allowed"]),
            used=int(payload["used"]),
            limit=int(payload["limit"]),
            remaining=int(payload["remaining"]),
        )
    except (EncryptionError, KeyError, ValueError, json.JSONDecodeError) as exc:
        logger.warning("Could not read quota cache: %s", exc)
        return None


def x_load_quota__mutmut_17() -> QuotaCheckResult | None:
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
        payload = cast(CachedQuota, json.loads(data.decode("UTF-8")))
        return QuotaCheckResult(
            allowed=bool(payload["allowed"]),
            used=int(payload["used"]),
            limit=int(payload["limit"]),
            remaining=int(payload["remaining"]),
        )
    except (EncryptionError, KeyError, ValueError, json.JSONDecodeError) as exc:
        logger.warning("Could not read quota cache: %s", exc)
        return None


def x_load_quota__mutmut_18() -> QuotaCheckResult | None:
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
            allowed=None,
            used=int(payload["used"]),
            limit=int(payload["limit"]),
            remaining=int(payload["remaining"]),
        )
    except (EncryptionError, KeyError, ValueError, json.JSONDecodeError) as exc:
        logger.warning("Could not read quota cache: %s", exc)
        return None


def x_load_quota__mutmut_19() -> QuotaCheckResult | None:
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
            used=None,
            limit=int(payload["limit"]),
            remaining=int(payload["remaining"]),
        )
    except (EncryptionError, KeyError, ValueError, json.JSONDecodeError) as exc:
        logger.warning("Could not read quota cache: %s", exc)
        return None


def x_load_quota__mutmut_20() -> QuotaCheckResult | None:
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
            limit=None,
            remaining=int(payload["remaining"]),
        )
    except (EncryptionError, KeyError, ValueError, json.JSONDecodeError) as exc:
        logger.warning("Could not read quota cache: %s", exc)
        return None


def x_load_quota__mutmut_21() -> QuotaCheckResult | None:
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
            remaining=None,
        )
    except (EncryptionError, KeyError, ValueError, json.JSONDecodeError) as exc:
        logger.warning("Could not read quota cache: %s", exc)
        return None


def x_load_quota__mutmut_22() -> QuotaCheckResult | None:
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
            used=int(payload["used"]),
            limit=int(payload["limit"]),
            remaining=int(payload["remaining"]),
        )
    except (EncryptionError, KeyError, ValueError, json.JSONDecodeError) as exc:
        logger.warning("Could not read quota cache: %s", exc)
        return None


def x_load_quota__mutmut_23() -> QuotaCheckResult | None:
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
            limit=int(payload["limit"]),
            remaining=int(payload["remaining"]),
        )
    except (EncryptionError, KeyError, ValueError, json.JSONDecodeError) as exc:
        logger.warning("Could not read quota cache: %s", exc)
        return None


def x_load_quota__mutmut_24() -> QuotaCheckResult | None:
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
            remaining=int(payload["remaining"]),
        )
    except (EncryptionError, KeyError, ValueError, json.JSONDecodeError) as exc:
        logger.warning("Could not read quota cache: %s", exc)
        return None


def x_load_quota__mutmut_25() -> QuotaCheckResult | None:
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
            )
    except (EncryptionError, KeyError, ValueError, json.JSONDecodeError) as exc:
        logger.warning("Could not read quota cache: %s", exc)
        return None


def x_load_quota__mutmut_26() -> QuotaCheckResult | None:
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
            allowed=bool(None),
            used=int(payload["used"]),
            limit=int(payload["limit"]),
            remaining=int(payload["remaining"]),
        )
    except (EncryptionError, KeyError, ValueError, json.JSONDecodeError) as exc:
        logger.warning("Could not read quota cache: %s", exc)
        return None


def x_load_quota__mutmut_27() -> QuotaCheckResult | None:
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
            allowed=bool(payload["XXallowedXX"]),
            used=int(payload["used"]),
            limit=int(payload["limit"]),
            remaining=int(payload["remaining"]),
        )
    except (EncryptionError, KeyError, ValueError, json.JSONDecodeError) as exc:
        logger.warning("Could not read quota cache: %s", exc)
        return None


def x_load_quota__mutmut_28() -> QuotaCheckResult | None:
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
            allowed=bool(payload["ALLOWED"]),
            used=int(payload["used"]),
            limit=int(payload["limit"]),
            remaining=int(payload["remaining"]),
        )
    except (EncryptionError, KeyError, ValueError, json.JSONDecodeError) as exc:
        logger.warning("Could not read quota cache: %s", exc)
        return None


def x_load_quota__mutmut_29() -> QuotaCheckResult | None:
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
            used=int(None),
            limit=int(payload["limit"]),
            remaining=int(payload["remaining"]),
        )
    except (EncryptionError, KeyError, ValueError, json.JSONDecodeError) as exc:
        logger.warning("Could not read quota cache: %s", exc)
        return None


def x_load_quota__mutmut_30() -> QuotaCheckResult | None:
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
            used=int(payload["XXusedXX"]),
            limit=int(payload["limit"]),
            remaining=int(payload["remaining"]),
        )
    except (EncryptionError, KeyError, ValueError, json.JSONDecodeError) as exc:
        logger.warning("Could not read quota cache: %s", exc)
        return None


def x_load_quota__mutmut_31() -> QuotaCheckResult | None:
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
            used=int(payload["USED"]),
            limit=int(payload["limit"]),
            remaining=int(payload["remaining"]),
        )
    except (EncryptionError, KeyError, ValueError, json.JSONDecodeError) as exc:
        logger.warning("Could not read quota cache: %s", exc)
        return None


def x_load_quota__mutmut_32() -> QuotaCheckResult | None:
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
            limit=int(None),
            remaining=int(payload["remaining"]),
        )
    except (EncryptionError, KeyError, ValueError, json.JSONDecodeError) as exc:
        logger.warning("Could not read quota cache: %s", exc)
        return None


def x_load_quota__mutmut_33() -> QuotaCheckResult | None:
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
            limit=int(payload["XXlimitXX"]),
            remaining=int(payload["remaining"]),
        )
    except (EncryptionError, KeyError, ValueError, json.JSONDecodeError) as exc:
        logger.warning("Could not read quota cache: %s", exc)
        return None


def x_load_quota__mutmut_34() -> QuotaCheckResult | None:
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
            limit=int(payload["LIMIT"]),
            remaining=int(payload["remaining"]),
        )
    except (EncryptionError, KeyError, ValueError, json.JSONDecodeError) as exc:
        logger.warning("Could not read quota cache: %s", exc)
        return None


def x_load_quota__mutmut_35() -> QuotaCheckResult | None:
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
            remaining=int(None),
        )
    except (EncryptionError, KeyError, ValueError, json.JSONDecodeError) as exc:
        logger.warning("Could not read quota cache: %s", exc)
        return None


def x_load_quota__mutmut_36() -> QuotaCheckResult | None:
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
            remaining=int(payload["XXremainingXX"]),
        )
    except (EncryptionError, KeyError, ValueError, json.JSONDecodeError) as exc:
        logger.warning("Could not read quota cache: %s", exc)
        return None


def x_load_quota__mutmut_37() -> QuotaCheckResult | None:
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
            remaining=int(payload["REMAINING"]),
        )
    except (EncryptionError, KeyError, ValueError, json.JSONDecodeError) as exc:
        logger.warning("Could not read quota cache: %s", exc)
        return None


def x_load_quota__mutmut_38() -> QuotaCheckResult | None:
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
        logger.warning(None, exc)
        return None


def x_load_quota__mutmut_39() -> QuotaCheckResult | None:
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
        logger.warning("Could not read quota cache: %s", None)
        return None


def x_load_quota__mutmut_40() -> QuotaCheckResult | None:
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
        logger.warning(exc)
        return None


def x_load_quota__mutmut_41() -> QuotaCheckResult | None:
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
        logger.warning("Could not read quota cache: %s", )
        return None


def x_load_quota__mutmut_42() -> QuotaCheckResult | None:
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
        logger.warning("XXCould not read quota cache: %sXX", exc)
        return None


def x_load_quota__mutmut_43() -> QuotaCheckResult | None:
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
        logger.warning("could not read quota cache: %s", exc)
        return None


def x_load_quota__mutmut_44() -> QuotaCheckResult | None:
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
        logger.warning("COULD NOT READ QUOTA CACHE: %S", exc)
        return None

mutants_x_load_quota__mutmut['_mutmut_orig'] = x_load_quota__mutmut_orig # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_1'] = x_load_quota__mutmut_1 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_2'] = x_load_quota__mutmut_2 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_3'] = x_load_quota__mutmut_3 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_4'] = x_load_quota__mutmut_4 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_5'] = x_load_quota__mutmut_5 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_6'] = x_load_quota__mutmut_6 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_7'] = x_load_quota__mutmut_7 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_8'] = x_load_quota__mutmut_8 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_9'] = x_load_quota__mutmut_9 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_10'] = x_load_quota__mutmut_10 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_11'] = x_load_quota__mutmut_11 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_12'] = x_load_quota__mutmut_12 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_13'] = x_load_quota__mutmut_13 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_14'] = x_load_quota__mutmut_14 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_15'] = x_load_quota__mutmut_15 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_16'] = x_load_quota__mutmut_16 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_17'] = x_load_quota__mutmut_17 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_18'] = x_load_quota__mutmut_18 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_19'] = x_load_quota__mutmut_19 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_20'] = x_load_quota__mutmut_20 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_21'] = x_load_quota__mutmut_21 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_22'] = x_load_quota__mutmut_22 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_23'] = x_load_quota__mutmut_23 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_24'] = x_load_quota__mutmut_24 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_25'] = x_load_quota__mutmut_25 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_26'] = x_load_quota__mutmut_26 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_27'] = x_load_quota__mutmut_27 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_28'] = x_load_quota__mutmut_28 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_29'] = x_load_quota__mutmut_29 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_30'] = x_load_quota__mutmut_30 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_31'] = x_load_quota__mutmut_31 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_32'] = x_load_quota__mutmut_32 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_33'] = x_load_quota__mutmut_33 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_34'] = x_load_quota__mutmut_34 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_35'] = x_load_quota__mutmut_35 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_36'] = x_load_quota__mutmut_36 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_37'] = x_load_quota__mutmut_37 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_38'] = x_load_quota__mutmut_38 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_39'] = x_load_quota__mutmut_39 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_40'] = x_load_quota__mutmut_40 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_41'] = x_load_quota__mutmut_41 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_42'] = x_load_quota__mutmut_42 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_43'] = x_load_quota__mutmut_43 # type: ignore # mutmut generated
mutants_x_load_quota__mutmut['x_load_quota__mutmut_44'] = x_load_quota__mutmut_44 # type: ignore # mutmut generated
mutants_x_clear_quota__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_clear_quota__mutmut)
def clear_quota() -> None:
    """Remove the cached quota (used by tests and forced resync)."""
    QUOTA_CACHE_PATH.unlink(missing_ok=True)


def x_clear_quota__mutmut_orig() -> None:
    """Remove the cached quota (used by tests and forced resync)."""
    QUOTA_CACHE_PATH.unlink(missing_ok=True)


def x_clear_quota__mutmut_1() -> None:
    """Remove the cached quota (used by tests and forced resync)."""
    QUOTA_CACHE_PATH.unlink(missing_ok=None)


def x_clear_quota__mutmut_2() -> None:
    """Remove the cached quota (used by tests and forced resync)."""
    QUOTA_CACHE_PATH.unlink(missing_ok=False)

mutants_x_clear_quota__mutmut['_mutmut_orig'] = x_clear_quota__mutmut_orig # type: ignore # mutmut generated
mutants_x_clear_quota__mutmut['x_clear_quota__mutmut_1'] = x_clear_quota__mutmut_1 # type: ignore # mutmut generated
mutants_x_clear_quota__mutmut['x_clear_quota__mutmut_2'] = x_clear_quota__mutmut_2 # type: ignore # mutmut generated
