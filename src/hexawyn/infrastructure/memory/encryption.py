import atexit
import os
import secrets
from pathlib import Path

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from hexawyn.domain.errors import EncryptionError

HEXAWYN_DIR = Path.home() / ".hexawyn"
ENCRYPTED_DB_PATH = HEXAWYN_DIR / "memory.duckdb.enc"
DB_PATH = HEXAWYN_DIR / "memory.duckdb"
KEY_SALT_PATH = HEXAWYN_DIR / ".keysalt"

_salt_cache: bytes | None = None
_db_prepared: bool = False
_atexit_registered: bool = False


def _reset_salt() -> None:
    """Reset the salt cache for test isolation."""
    global _salt_cache
    _salt_cache = None


def _reset_prepare_db_state() -> None:
    """Reset the prepared state for test isolation."""
    global _db_prepared, _atexit_registered
    _db_prepared = False
    _atexit_registered = False


def _get_or_create_salt() -> bytes:
    global _salt_cache
    if _salt_cache is not None:
        return _salt_cache
    if KEY_SALT_PATH.exists():
        _salt_cache = KEY_SALT_PATH.read_bytes()
        return _salt_cache
    salt = secrets.token_bytes(32)
    KEY_SALT_PATH.parent.mkdir(parents=True, exist_ok=True)
    KEY_SALT_PATH.write_bytes(salt)
    KEY_SALT_PATH.chmod(0o600)
    _salt_cache = salt
    return salt


def derive_key(kubeconfig_content: bytes) -> bytes:
    salt = _get_or_create_salt()
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=32,
        salt=salt,
        iterations=600_000,
    )
    return kdf.derive(kubeconfig_content)


def is_encryption_disabled() -> bool:
    return os.environ.get("HEXAWYN_DISABLE_ENCRYPTION", "").lower() == "true"


def _encrypt_data(key: bytes, plaintext: bytes) -> bytes:
    nonce = secrets.token_bytes(12)
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(nonce, plaintext, None)
    return nonce + ciphertext


def _decrypt_data(key: bytes, data: bytes) -> bytes:
    if len(data) < 13:  # noqa: PLR2004
        raise EncryptionError(
            "Encrypted data is too short to contain nonce and ciphertext.",
            context={"data_length": str(len(data))},
        )
    nonce = data[:12]
    ciphertext = data[12:]
    try:
        aesgcm = AESGCM(key)
        return aesgcm.decrypt(nonce, ciphertext, None)
    except Exception as e:
        raise EncryptionError(
            "Failed to decrypt database. Wrong kubeconfig, corrupted file, "
            "or encryption key mismatch.",
            context={"error": str(e)},
        ) from e


def _encrypt_file(key: bytes, plain_path: Path, enc_path: Path) -> None:
    if not plain_path.exists():
        return
    plaintext = plain_path.read_bytes()
    encrypted = _encrypt_data(key, plaintext)
    enc_path.write_bytes(encrypted)
    enc_path.chmod(0o600)


def _decrypt_file(key: bytes, enc_path: Path, output_path: Path) -> None:
    if not enc_path.exists():
        return
    data = enc_path.read_bytes()
    plaintext = _decrypt_data(key, data)
    output_path.write_bytes(plaintext)
    output_path.chmod(0o600)


def _encrypt_db_on_exit(key: bytes) -> None:
    if DB_PATH.exists():
        _encrypt_file(key, DB_PATH, ENCRYPTED_DB_PATH)
        DB_PATH.unlink(missing_ok=True)


def prepare_db(key: bytes) -> None:
    global _db_prepared, _atexit_registered
    if _db_prepared:
        return

    HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

    if ENCRYPTED_DB_PATH.exists():
        _decrypt_file(key, ENCRYPTED_DB_PATH, DB_PATH)

    if not _atexit_registered:
        atexit.register(_encrypt_db_on_exit, key)
        _atexit_registered = True

    _db_prepared = True
