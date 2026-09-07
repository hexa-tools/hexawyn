import atexit
import logging
import os
import secrets
from datetime import UTC, datetime
from pathlib import Path

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from hexawyn.domain.errors import EncryptionError
from hexawyn.infrastructure.config.machine_id import get_machine_id

logger = logging.getLogger(__name__)

HEXAWYN_DIR = Path.home() / ".hexawyn"
ENCRYPTED_DB_PATH = HEXAWYN_DIR / "memory.duckdb.enc"
DB_PATH = HEXAWYN_DIR / "memory.duckdb"
KEY_SALT_PATH = HEXAWYN_DIR / ".keysalt"

_salt_cache: bytes | None = None
_db_prepared: bool = False
_atexit_registered: bool = False


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x__reset_salt__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__reset_salt__mutmut)
def _reset_salt() -> None:
    """Reset the salt cache for test isolation."""
    global _salt_cache
    _salt_cache = None


def x__reset_salt__mutmut_orig() -> None:
    """Reset the salt cache for test isolation."""
    global _salt_cache
    _salt_cache = None


def x__reset_salt__mutmut_1() -> None:
    """Reset the salt cache for test isolation."""
    global _salt_cache
    _salt_cache = ""

mutants_x__reset_salt__mutmut['_mutmut_orig'] = x__reset_salt__mutmut_orig # type: ignore # mutmut generated
mutants_x__reset_salt__mutmut['x__reset_salt__mutmut_1'] = x__reset_salt__mutmut_1 # type: ignore # mutmut generated
mutants_x__reset_prepare_db_state__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__reset_prepare_db_state__mutmut)
def _reset_prepare_db_state() -> None:
    """Reset the prepared state for test isolation."""
    global _db_prepared, _atexit_registered
    _db_prepared = False
    _atexit_registered = False


def x__reset_prepare_db_state__mutmut_orig() -> None:
    """Reset the prepared state for test isolation."""
    global _db_prepared, _atexit_registered
    _db_prepared = False
    _atexit_registered = False


def x__reset_prepare_db_state__mutmut_1() -> None:
    """Reset the prepared state for test isolation."""
    global _db_prepared, _atexit_registered
    _db_prepared = None
    _atexit_registered = False


def x__reset_prepare_db_state__mutmut_2() -> None:
    """Reset the prepared state for test isolation."""
    global _db_prepared, _atexit_registered
    _db_prepared = True
    _atexit_registered = False


def x__reset_prepare_db_state__mutmut_3() -> None:
    """Reset the prepared state for test isolation."""
    global _db_prepared, _atexit_registered
    _db_prepared = False
    _atexit_registered = None


def x__reset_prepare_db_state__mutmut_4() -> None:
    """Reset the prepared state for test isolation."""
    global _db_prepared, _atexit_registered
    _db_prepared = False
    _atexit_registered = True

mutants_x__reset_prepare_db_state__mutmut['_mutmut_orig'] = x__reset_prepare_db_state__mutmut_orig # type: ignore # mutmut generated
mutants_x__reset_prepare_db_state__mutmut['x__reset_prepare_db_state__mutmut_1'] = x__reset_prepare_db_state__mutmut_1 # type: ignore # mutmut generated
mutants_x__reset_prepare_db_state__mutmut['x__reset_prepare_db_state__mutmut_2'] = x__reset_prepare_db_state__mutmut_2 # type: ignore # mutmut generated
mutants_x__reset_prepare_db_state__mutmut['x__reset_prepare_db_state__mutmut_3'] = x__reset_prepare_db_state__mutmut_3 # type: ignore # mutmut generated
mutants_x__reset_prepare_db_state__mutmut['x__reset_prepare_db_state__mutmut_4'] = x__reset_prepare_db_state__mutmut_4 # type: ignore # mutmut generated
mutants_x__get_or_create_salt__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__get_or_create_salt__mutmut)
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


def x__get_or_create_salt__mutmut_orig() -> bytes:
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


def x__get_or_create_salt__mutmut_1() -> bytes:
    global _salt_cache
    if _salt_cache is None:
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


def x__get_or_create_salt__mutmut_2() -> bytes:
    global _salt_cache
    if _salt_cache is not None:
        return _salt_cache
    if KEY_SALT_PATH.exists():
        _salt_cache = None
        return _salt_cache
    salt = secrets.token_bytes(32)
    KEY_SALT_PATH.parent.mkdir(parents=True, exist_ok=True)
    KEY_SALT_PATH.write_bytes(salt)
    KEY_SALT_PATH.chmod(0o600)
    _salt_cache = salt
    return salt


def x__get_or_create_salt__mutmut_3() -> bytes:
    global _salt_cache
    if _salt_cache is not None:
        return _salt_cache
    if KEY_SALT_PATH.exists():
        _salt_cache = KEY_SALT_PATH.read_bytes()
        return _salt_cache
    salt = None
    KEY_SALT_PATH.parent.mkdir(parents=True, exist_ok=True)
    KEY_SALT_PATH.write_bytes(salt)
    KEY_SALT_PATH.chmod(0o600)
    _salt_cache = salt
    return salt


def x__get_or_create_salt__mutmut_4() -> bytes:
    global _salt_cache
    if _salt_cache is not None:
        return _salt_cache
    if KEY_SALT_PATH.exists():
        _salt_cache = KEY_SALT_PATH.read_bytes()
        return _salt_cache
    salt = secrets.token_bytes(None)
    KEY_SALT_PATH.parent.mkdir(parents=True, exist_ok=True)
    KEY_SALT_PATH.write_bytes(salt)
    KEY_SALT_PATH.chmod(0o600)
    _salt_cache = salt
    return salt


def x__get_or_create_salt__mutmut_5() -> bytes:
    global _salt_cache
    if _salt_cache is not None:
        return _salt_cache
    if KEY_SALT_PATH.exists():
        _salt_cache = KEY_SALT_PATH.read_bytes()
        return _salt_cache
    salt = secrets.token_bytes(33)
    KEY_SALT_PATH.parent.mkdir(parents=True, exist_ok=True)
    KEY_SALT_PATH.write_bytes(salt)
    KEY_SALT_PATH.chmod(0o600)
    _salt_cache = salt
    return salt


def x__get_or_create_salt__mutmut_6() -> bytes:
    global _salt_cache
    if _salt_cache is not None:
        return _salt_cache
    if KEY_SALT_PATH.exists():
        _salt_cache = KEY_SALT_PATH.read_bytes()
        return _salt_cache
    salt = secrets.token_bytes(32)
    KEY_SALT_PATH.parent.mkdir(parents=None, exist_ok=True)
    KEY_SALT_PATH.write_bytes(salt)
    KEY_SALT_PATH.chmod(0o600)
    _salt_cache = salt
    return salt


def x__get_or_create_salt__mutmut_7() -> bytes:
    global _salt_cache
    if _salt_cache is not None:
        return _salt_cache
    if KEY_SALT_PATH.exists():
        _salt_cache = KEY_SALT_PATH.read_bytes()
        return _salt_cache
    salt = secrets.token_bytes(32)
    KEY_SALT_PATH.parent.mkdir(parents=True, exist_ok=None)
    KEY_SALT_PATH.write_bytes(salt)
    KEY_SALT_PATH.chmod(0o600)
    _salt_cache = salt
    return salt


def x__get_or_create_salt__mutmut_8() -> bytes:
    global _salt_cache
    if _salt_cache is not None:
        return _salt_cache
    if KEY_SALT_PATH.exists():
        _salt_cache = KEY_SALT_PATH.read_bytes()
        return _salt_cache
    salt = secrets.token_bytes(32)
    KEY_SALT_PATH.parent.mkdir(exist_ok=True)
    KEY_SALT_PATH.write_bytes(salt)
    KEY_SALT_PATH.chmod(0o600)
    _salt_cache = salt
    return salt


def x__get_or_create_salt__mutmut_9() -> bytes:
    global _salt_cache
    if _salt_cache is not None:
        return _salt_cache
    if KEY_SALT_PATH.exists():
        _salt_cache = KEY_SALT_PATH.read_bytes()
        return _salt_cache
    salt = secrets.token_bytes(32)
    KEY_SALT_PATH.parent.mkdir(parents=True, )
    KEY_SALT_PATH.write_bytes(salt)
    KEY_SALT_PATH.chmod(0o600)
    _salt_cache = salt
    return salt


def x__get_or_create_salt__mutmut_10() -> bytes:
    global _salt_cache
    if _salt_cache is not None:
        return _salt_cache
    if KEY_SALT_PATH.exists():
        _salt_cache = KEY_SALT_PATH.read_bytes()
        return _salt_cache
    salt = secrets.token_bytes(32)
    KEY_SALT_PATH.parent.mkdir(parents=False, exist_ok=True)
    KEY_SALT_PATH.write_bytes(salt)
    KEY_SALT_PATH.chmod(0o600)
    _salt_cache = salt
    return salt


def x__get_or_create_salt__mutmut_11() -> bytes:
    global _salt_cache
    if _salt_cache is not None:
        return _salt_cache
    if KEY_SALT_PATH.exists():
        _salt_cache = KEY_SALT_PATH.read_bytes()
        return _salt_cache
    salt = secrets.token_bytes(32)
    KEY_SALT_PATH.parent.mkdir(parents=True, exist_ok=False)
    KEY_SALT_PATH.write_bytes(salt)
    KEY_SALT_PATH.chmod(0o600)
    _salt_cache = salt
    return salt


def x__get_or_create_salt__mutmut_12() -> bytes:
    global _salt_cache
    if _salt_cache is not None:
        return _salt_cache
    if KEY_SALT_PATH.exists():
        _salt_cache = KEY_SALT_PATH.read_bytes()
        return _salt_cache
    salt = secrets.token_bytes(32)
    KEY_SALT_PATH.parent.mkdir(parents=True, exist_ok=True)
    KEY_SALT_PATH.write_bytes(None)
    KEY_SALT_PATH.chmod(0o600)
    _salt_cache = salt
    return salt


def x__get_or_create_salt__mutmut_13() -> bytes:
    global _salt_cache
    if _salt_cache is not None:
        return _salt_cache
    if KEY_SALT_PATH.exists():
        _salt_cache = KEY_SALT_PATH.read_bytes()
        return _salt_cache
    salt = secrets.token_bytes(32)
    KEY_SALT_PATH.parent.mkdir(parents=True, exist_ok=True)
    KEY_SALT_PATH.write_bytes(salt)
    KEY_SALT_PATH.chmod(None)
    _salt_cache = salt
    return salt


def x__get_or_create_salt__mutmut_14() -> bytes:
    global _salt_cache
    if _salt_cache is not None:
        return _salt_cache
    if KEY_SALT_PATH.exists():
        _salt_cache = KEY_SALT_PATH.read_bytes()
        return _salt_cache
    salt = secrets.token_bytes(32)
    KEY_SALT_PATH.parent.mkdir(parents=True, exist_ok=True)
    KEY_SALT_PATH.write_bytes(salt)
    KEY_SALT_PATH.chmod(385)
    _salt_cache = salt
    return salt


def x__get_or_create_salt__mutmut_15() -> bytes:
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
    _salt_cache = None
    return salt

mutants_x__get_or_create_salt__mutmut['_mutmut_orig'] = x__get_or_create_salt__mutmut_orig # type: ignore # mutmut generated
mutants_x__get_or_create_salt__mutmut['x__get_or_create_salt__mutmut_1'] = x__get_or_create_salt__mutmut_1 # type: ignore # mutmut generated
mutants_x__get_or_create_salt__mutmut['x__get_or_create_salt__mutmut_2'] = x__get_or_create_salt__mutmut_2 # type: ignore # mutmut generated
mutants_x__get_or_create_salt__mutmut['x__get_or_create_salt__mutmut_3'] = x__get_or_create_salt__mutmut_3 # type: ignore # mutmut generated
mutants_x__get_or_create_salt__mutmut['x__get_or_create_salt__mutmut_4'] = x__get_or_create_salt__mutmut_4 # type: ignore # mutmut generated
mutants_x__get_or_create_salt__mutmut['x__get_or_create_salt__mutmut_5'] = x__get_or_create_salt__mutmut_5 # type: ignore # mutmut generated
mutants_x__get_or_create_salt__mutmut['x__get_or_create_salt__mutmut_6'] = x__get_or_create_salt__mutmut_6 # type: ignore # mutmut generated
mutants_x__get_or_create_salt__mutmut['x__get_or_create_salt__mutmut_7'] = x__get_or_create_salt__mutmut_7 # type: ignore # mutmut generated
mutants_x__get_or_create_salt__mutmut['x__get_or_create_salt__mutmut_8'] = x__get_or_create_salt__mutmut_8 # type: ignore # mutmut generated
mutants_x__get_or_create_salt__mutmut['x__get_or_create_salt__mutmut_9'] = x__get_or_create_salt__mutmut_9 # type: ignore # mutmut generated
mutants_x__get_or_create_salt__mutmut['x__get_or_create_salt__mutmut_10'] = x__get_or_create_salt__mutmut_10 # type: ignore # mutmut generated
mutants_x__get_or_create_salt__mutmut['x__get_or_create_salt__mutmut_11'] = x__get_or_create_salt__mutmut_11 # type: ignore # mutmut generated
mutants_x__get_or_create_salt__mutmut['x__get_or_create_salt__mutmut_12'] = x__get_or_create_salt__mutmut_12 # type: ignore # mutmut generated
mutants_x__get_or_create_salt__mutmut['x__get_or_create_salt__mutmut_13'] = x__get_or_create_salt__mutmut_13 # type: ignore # mutmut generated
mutants_x__get_or_create_salt__mutmut['x__get_or_create_salt__mutmut_14'] = x__get_or_create_salt__mutmut_14 # type: ignore # mutmut generated
mutants_x__get_or_create_salt__mutmut['x__get_or_create_salt__mutmut_15'] = x__get_or_create_salt__mutmut_15 # type: ignore # mutmut generated
mutants_x_derive_key__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_derive_key__mutmut)
def derive_key() -> bytes:
    """Derive the AES-256-GCM key from the installation's machine identity.

    The key is bound to the machine (via ``get_machine_id``) and a stored
    random salt. It does NOT depend on the kubeconfig, so switching contexts,
    clusters, or ``$KUBECONFIG`` never invalidates the encryption key.
    """
    salt = _get_or_create_salt()
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=32,
        salt=salt,
        iterations=600_000,
    )
    return kdf.derive(get_machine_id().encode("utf-8"))


def x_derive_key__mutmut_orig() -> bytes:
    """Derive the AES-256-GCM key from the installation's machine identity.

    The key is bound to the machine (via ``get_machine_id``) and a stored
    random salt. It does NOT depend on the kubeconfig, so switching contexts,
    clusters, or ``$KUBECONFIG`` never invalidates the encryption key.
    """
    salt = _get_or_create_salt()
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=32,
        salt=salt,
        iterations=600_000,
    )
    return kdf.derive(get_machine_id().encode("utf-8"))


def x_derive_key__mutmut_1() -> bytes:
    """Derive the AES-256-GCM key from the installation's machine identity.

    The key is bound to the machine (via ``get_machine_id``) and a stored
    random salt. It does NOT depend on the kubeconfig, so switching contexts,
    clusters, or ``$KUBECONFIG`` never invalidates the encryption key.
    """
    salt = None
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=32,
        salt=salt,
        iterations=600_000,
    )
    return kdf.derive(get_machine_id().encode("utf-8"))


def x_derive_key__mutmut_2() -> bytes:
    """Derive the AES-256-GCM key from the installation's machine identity.

    The key is bound to the machine (via ``get_machine_id``) and a stored
    random salt. It does NOT depend on the kubeconfig, so switching contexts,
    clusters, or ``$KUBECONFIG`` never invalidates the encryption key.
    """
    salt = _get_or_create_salt()
    kdf = None
    return kdf.derive(get_machine_id().encode("utf-8"))


def x_derive_key__mutmut_3() -> bytes:
    """Derive the AES-256-GCM key from the installation's machine identity.

    The key is bound to the machine (via ``get_machine_id``) and a stored
    random salt. It does NOT depend on the kubeconfig, so switching contexts,
    clusters, or ``$KUBECONFIG`` never invalidates the encryption key.
    """
    salt = _get_or_create_salt()
    kdf = PBKDF2HMAC(
        algorithm=None,
        length=32,
        salt=salt,
        iterations=600_000,
    )
    return kdf.derive(get_machine_id().encode("utf-8"))


def x_derive_key__mutmut_4() -> bytes:
    """Derive the AES-256-GCM key from the installation's machine identity.

    The key is bound to the machine (via ``get_machine_id``) and a stored
    random salt. It does NOT depend on the kubeconfig, so switching contexts,
    clusters, or ``$KUBECONFIG`` never invalidates the encryption key.
    """
    salt = _get_or_create_salt()
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=None,
        salt=salt,
        iterations=600_000,
    )
    return kdf.derive(get_machine_id().encode("utf-8"))


def x_derive_key__mutmut_5() -> bytes:
    """Derive the AES-256-GCM key from the installation's machine identity.

    The key is bound to the machine (via ``get_machine_id``) and a stored
    random salt. It does NOT depend on the kubeconfig, so switching contexts,
    clusters, or ``$KUBECONFIG`` never invalidates the encryption key.
    """
    salt = _get_or_create_salt()
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=32,
        salt=None,
        iterations=600_000,
    )
    return kdf.derive(get_machine_id().encode("utf-8"))


def x_derive_key__mutmut_6() -> bytes:
    """Derive the AES-256-GCM key from the installation's machine identity.

    The key is bound to the machine (via ``get_machine_id``) and a stored
    random salt. It does NOT depend on the kubeconfig, so switching contexts,
    clusters, or ``$KUBECONFIG`` never invalidates the encryption key.
    """
    salt = _get_or_create_salt()
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=32,
        salt=salt,
        iterations=None,
    )
    return kdf.derive(get_machine_id().encode("utf-8"))


def x_derive_key__mutmut_7() -> bytes:
    """Derive the AES-256-GCM key from the installation's machine identity.

    The key is bound to the machine (via ``get_machine_id``) and a stored
    random salt. It does NOT depend on the kubeconfig, so switching contexts,
    clusters, or ``$KUBECONFIG`` never invalidates the encryption key.
    """
    salt = _get_or_create_salt()
    kdf = PBKDF2HMAC(
        length=32,
        salt=salt,
        iterations=600_000,
    )
    return kdf.derive(get_machine_id().encode("utf-8"))


def x_derive_key__mutmut_8() -> bytes:
    """Derive the AES-256-GCM key from the installation's machine identity.

    The key is bound to the machine (via ``get_machine_id``) and a stored
    random salt. It does NOT depend on the kubeconfig, so switching contexts,
    clusters, or ``$KUBECONFIG`` never invalidates the encryption key.
    """
    salt = _get_or_create_salt()
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        salt=salt,
        iterations=600_000,
    )
    return kdf.derive(get_machine_id().encode("utf-8"))


def x_derive_key__mutmut_9() -> bytes:
    """Derive the AES-256-GCM key from the installation's machine identity.

    The key is bound to the machine (via ``get_machine_id``) and a stored
    random salt. It does NOT depend on the kubeconfig, so switching contexts,
    clusters, or ``$KUBECONFIG`` never invalidates the encryption key.
    """
    salt = _get_or_create_salt()
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=32,
        iterations=600_000,
    )
    return kdf.derive(get_machine_id().encode("utf-8"))


def x_derive_key__mutmut_10() -> bytes:
    """Derive the AES-256-GCM key from the installation's machine identity.

    The key is bound to the machine (via ``get_machine_id``) and a stored
    random salt. It does NOT depend on the kubeconfig, so switching contexts,
    clusters, or ``$KUBECONFIG`` never invalidates the encryption key.
    """
    salt = _get_or_create_salt()
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=32,
        salt=salt,
        )
    return kdf.derive(get_machine_id().encode("utf-8"))


def x_derive_key__mutmut_11() -> bytes:
    """Derive the AES-256-GCM key from the installation's machine identity.

    The key is bound to the machine (via ``get_machine_id``) and a stored
    random salt. It does NOT depend on the kubeconfig, so switching contexts,
    clusters, or ``$KUBECONFIG`` never invalidates the encryption key.
    """
    salt = _get_or_create_salt()
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=33,
        salt=salt,
        iterations=600_000,
    )
    return kdf.derive(get_machine_id().encode("utf-8"))


def x_derive_key__mutmut_12() -> bytes:
    """Derive the AES-256-GCM key from the installation's machine identity.

    The key is bound to the machine (via ``get_machine_id``) and a stored
    random salt. It does NOT depend on the kubeconfig, so switching contexts,
    clusters, or ``$KUBECONFIG`` never invalidates the encryption key.
    """
    salt = _get_or_create_salt()
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=32,
        salt=salt,
        iterations=600001,
    )
    return kdf.derive(get_machine_id().encode("utf-8"))


def x_derive_key__mutmut_13() -> bytes:
    """Derive the AES-256-GCM key from the installation's machine identity.

    The key is bound to the machine (via ``get_machine_id``) and a stored
    random salt. It does NOT depend on the kubeconfig, so switching contexts,
    clusters, or ``$KUBECONFIG`` never invalidates the encryption key.
    """
    salt = _get_or_create_salt()
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=32,
        salt=salt,
        iterations=600_000,
    )
    return kdf.derive(None)


def x_derive_key__mutmut_14() -> bytes:
    """Derive the AES-256-GCM key from the installation's machine identity.

    The key is bound to the machine (via ``get_machine_id``) and a stored
    random salt. It does NOT depend on the kubeconfig, so switching contexts,
    clusters, or ``$KUBECONFIG`` never invalidates the encryption key.
    """
    salt = _get_or_create_salt()
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=32,
        salt=salt,
        iterations=600_000,
    )
    return kdf.derive(get_machine_id().encode(None))


def x_derive_key__mutmut_15() -> bytes:
    """Derive the AES-256-GCM key from the installation's machine identity.

    The key is bound to the machine (via ``get_machine_id``) and a stored
    random salt. It does NOT depend on the kubeconfig, so switching contexts,
    clusters, or ``$KUBECONFIG`` never invalidates the encryption key.
    """
    salt = _get_or_create_salt()
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=32,
        salt=salt,
        iterations=600_000,
    )
    return kdf.derive(get_machine_id().encode("XXutf-8XX"))


def x_derive_key__mutmut_16() -> bytes:
    """Derive the AES-256-GCM key from the installation's machine identity.

    The key is bound to the machine (via ``get_machine_id``) and a stored
    random salt. It does NOT depend on the kubeconfig, so switching contexts,
    clusters, or ``$KUBECONFIG`` never invalidates the encryption key.
    """
    salt = _get_or_create_salt()
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=32,
        salt=salt,
        iterations=600_000,
    )
    return kdf.derive(get_machine_id().encode("UTF-8"))

mutants_x_derive_key__mutmut['_mutmut_orig'] = x_derive_key__mutmut_orig # type: ignore # mutmut generated
mutants_x_derive_key__mutmut['x_derive_key__mutmut_1'] = x_derive_key__mutmut_1 # type: ignore # mutmut generated
mutants_x_derive_key__mutmut['x_derive_key__mutmut_2'] = x_derive_key__mutmut_2 # type: ignore # mutmut generated
mutants_x_derive_key__mutmut['x_derive_key__mutmut_3'] = x_derive_key__mutmut_3 # type: ignore # mutmut generated
mutants_x_derive_key__mutmut['x_derive_key__mutmut_4'] = x_derive_key__mutmut_4 # type: ignore # mutmut generated
mutants_x_derive_key__mutmut['x_derive_key__mutmut_5'] = x_derive_key__mutmut_5 # type: ignore # mutmut generated
mutants_x_derive_key__mutmut['x_derive_key__mutmut_6'] = x_derive_key__mutmut_6 # type: ignore # mutmut generated
mutants_x_derive_key__mutmut['x_derive_key__mutmut_7'] = x_derive_key__mutmut_7 # type: ignore # mutmut generated
mutants_x_derive_key__mutmut['x_derive_key__mutmut_8'] = x_derive_key__mutmut_8 # type: ignore # mutmut generated
mutants_x_derive_key__mutmut['x_derive_key__mutmut_9'] = x_derive_key__mutmut_9 # type: ignore # mutmut generated
mutants_x_derive_key__mutmut['x_derive_key__mutmut_10'] = x_derive_key__mutmut_10 # type: ignore # mutmut generated
mutants_x_derive_key__mutmut['x_derive_key__mutmut_11'] = x_derive_key__mutmut_11 # type: ignore # mutmut generated
mutants_x_derive_key__mutmut['x_derive_key__mutmut_12'] = x_derive_key__mutmut_12 # type: ignore # mutmut generated
mutants_x_derive_key__mutmut['x_derive_key__mutmut_13'] = x_derive_key__mutmut_13 # type: ignore # mutmut generated
mutants_x_derive_key__mutmut['x_derive_key__mutmut_14'] = x_derive_key__mutmut_14 # type: ignore # mutmut generated
mutants_x_derive_key__mutmut['x_derive_key__mutmut_15'] = x_derive_key__mutmut_15 # type: ignore # mutmut generated
mutants_x_derive_key__mutmut['x_derive_key__mutmut_16'] = x_derive_key__mutmut_16 # type: ignore # mutmut generated
mutants_x_is_encryption_disabled__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_is_encryption_disabled__mutmut)
def is_encryption_disabled() -> bool:
    return os.environ.get("HEXAWYN_DISABLE_ENCRYPTION", "").lower() == "true"


def x_is_encryption_disabled__mutmut_orig() -> bool:
    return os.environ.get("HEXAWYN_DISABLE_ENCRYPTION", "").lower() == "true"


def x_is_encryption_disabled__mutmut_1() -> bool:
    return os.environ.get("HEXAWYN_DISABLE_ENCRYPTION", "").upper() == "true"


def x_is_encryption_disabled__mutmut_2() -> bool:
    return os.environ.get(None, "").lower() == "true"


def x_is_encryption_disabled__mutmut_3() -> bool:
    return os.environ.get("HEXAWYN_DISABLE_ENCRYPTION", None).lower() == "true"


def x_is_encryption_disabled__mutmut_4() -> bool:
    return os.environ.get("").lower() == "true"


def x_is_encryption_disabled__mutmut_5() -> bool:
    return os.environ.get("HEXAWYN_DISABLE_ENCRYPTION", ).lower() == "true"


def x_is_encryption_disabled__mutmut_6() -> bool:
    return os.environ.get("XXHEXAWYN_DISABLE_ENCRYPTIONXX", "").lower() == "true"


def x_is_encryption_disabled__mutmut_7() -> bool:
    return os.environ.get("hexawyn_disable_encryption", "").lower() == "true"


def x_is_encryption_disabled__mutmut_8() -> bool:
    return os.environ.get("HEXAWYN_DISABLE_ENCRYPTION", "XXXX").lower() == "true"


def x_is_encryption_disabled__mutmut_9() -> bool:
    return os.environ.get("HEXAWYN_DISABLE_ENCRYPTION", "").lower() != "true"


def x_is_encryption_disabled__mutmut_10() -> bool:
    return os.environ.get("HEXAWYN_DISABLE_ENCRYPTION", "").lower() == "XXtrueXX"


def x_is_encryption_disabled__mutmut_11() -> bool:
    return os.environ.get("HEXAWYN_DISABLE_ENCRYPTION", "").lower() == "TRUE"

mutants_x_is_encryption_disabled__mutmut['_mutmut_orig'] = x_is_encryption_disabled__mutmut_orig # type: ignore # mutmut generated
mutants_x_is_encryption_disabled__mutmut['x_is_encryption_disabled__mutmut_1'] = x_is_encryption_disabled__mutmut_1 # type: ignore # mutmut generated
mutants_x_is_encryption_disabled__mutmut['x_is_encryption_disabled__mutmut_2'] = x_is_encryption_disabled__mutmut_2 # type: ignore # mutmut generated
mutants_x_is_encryption_disabled__mutmut['x_is_encryption_disabled__mutmut_3'] = x_is_encryption_disabled__mutmut_3 # type: ignore # mutmut generated
mutants_x_is_encryption_disabled__mutmut['x_is_encryption_disabled__mutmut_4'] = x_is_encryption_disabled__mutmut_4 # type: ignore # mutmut generated
mutants_x_is_encryption_disabled__mutmut['x_is_encryption_disabled__mutmut_5'] = x_is_encryption_disabled__mutmut_5 # type: ignore # mutmut generated
mutants_x_is_encryption_disabled__mutmut['x_is_encryption_disabled__mutmut_6'] = x_is_encryption_disabled__mutmut_6 # type: ignore # mutmut generated
mutants_x_is_encryption_disabled__mutmut['x_is_encryption_disabled__mutmut_7'] = x_is_encryption_disabled__mutmut_7 # type: ignore # mutmut generated
mutants_x_is_encryption_disabled__mutmut['x_is_encryption_disabled__mutmut_8'] = x_is_encryption_disabled__mutmut_8 # type: ignore # mutmut generated
mutants_x_is_encryption_disabled__mutmut['x_is_encryption_disabled__mutmut_9'] = x_is_encryption_disabled__mutmut_9 # type: ignore # mutmut generated
mutants_x_is_encryption_disabled__mutmut['x_is_encryption_disabled__mutmut_10'] = x_is_encryption_disabled__mutmut_10 # type: ignore # mutmut generated
mutants_x_is_encryption_disabled__mutmut['x_is_encryption_disabled__mutmut_11'] = x_is_encryption_disabled__mutmut_11 # type: ignore # mutmut generated
mutants_x__encrypt_data__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__encrypt_data__mutmut)
def _encrypt_data(key: bytes, plaintext: bytes) -> bytes:
    nonce = secrets.token_bytes(12)
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(nonce, plaintext, None)
    return nonce + ciphertext


def x__encrypt_data__mutmut_orig(key: bytes, plaintext: bytes) -> bytes:
    nonce = secrets.token_bytes(12)
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(nonce, plaintext, None)
    return nonce + ciphertext


def x__encrypt_data__mutmut_1(key: bytes, plaintext: bytes) -> bytes:
    nonce = None
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(nonce, plaintext, None)
    return nonce + ciphertext


def x__encrypt_data__mutmut_2(key: bytes, plaintext: bytes) -> bytes:
    nonce = secrets.token_bytes(None)
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(nonce, plaintext, None)
    return nonce + ciphertext


def x__encrypt_data__mutmut_3(key: bytes, plaintext: bytes) -> bytes:
    nonce = secrets.token_bytes(13)
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(nonce, plaintext, None)
    return nonce + ciphertext


def x__encrypt_data__mutmut_4(key: bytes, plaintext: bytes) -> bytes:
    nonce = secrets.token_bytes(12)
    aesgcm = None
    ciphertext = aesgcm.encrypt(nonce, plaintext, None)
    return nonce + ciphertext


def x__encrypt_data__mutmut_5(key: bytes, plaintext: bytes) -> bytes:
    nonce = secrets.token_bytes(12)
    aesgcm = AESGCM(None)
    ciphertext = aesgcm.encrypt(nonce, plaintext, None)
    return nonce + ciphertext


def x__encrypt_data__mutmut_6(key: bytes, plaintext: bytes) -> bytes:
    nonce = secrets.token_bytes(12)
    aesgcm = AESGCM(key)
    ciphertext = None
    return nonce + ciphertext


def x__encrypt_data__mutmut_7(key: bytes, plaintext: bytes) -> bytes:
    nonce = secrets.token_bytes(12)
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(None, plaintext, None)
    return nonce + ciphertext


def x__encrypt_data__mutmut_8(key: bytes, plaintext: bytes) -> bytes:
    nonce = secrets.token_bytes(12)
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(nonce, None, None)
    return nonce + ciphertext


def x__encrypt_data__mutmut_9(key: bytes, plaintext: bytes) -> bytes:
    nonce = secrets.token_bytes(12)
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(plaintext, None)
    return nonce + ciphertext


def x__encrypt_data__mutmut_10(key: bytes, plaintext: bytes) -> bytes:
    nonce = secrets.token_bytes(12)
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(nonce, None)
    return nonce + ciphertext


def x__encrypt_data__mutmut_11(key: bytes, plaintext: bytes) -> bytes:
    nonce = secrets.token_bytes(12)
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(nonce, plaintext, )
    return nonce + ciphertext


def x__encrypt_data__mutmut_12(key: bytes, plaintext: bytes) -> bytes:
    nonce = secrets.token_bytes(12)
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(nonce, plaintext, None)
    return nonce - ciphertext

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
mutants_x__encrypt_data__mutmut['x__encrypt_data__mutmut_12'] = x__encrypt_data__mutmut_12 # type: ignore # mutmut generated
mutants_x__decrypt_data__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__decrypt_data__mutmut)
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


def x__decrypt_data__mutmut_orig(key: bytes, data: bytes) -> bytes:
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


def x__decrypt_data__mutmut_1(key: bytes, data: bytes) -> bytes:
    if len(data) <= 13:  # noqa: PLR2004
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


def x__decrypt_data__mutmut_2(key: bytes, data: bytes) -> bytes:
    if len(data) < 14:  # noqa: PLR2004
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


def x__decrypt_data__mutmut_3(key: bytes, data: bytes) -> bytes:
    if len(data) < 13:  # noqa: PLR2004
        raise EncryptionError(
            None,
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


def x__decrypt_data__mutmut_4(key: bytes, data: bytes) -> bytes:
    if len(data) < 13:  # noqa: PLR2004
        raise EncryptionError(
            "Encrypted data is too short to contain nonce and ciphertext.",
            context=None,
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


def x__decrypt_data__mutmut_5(key: bytes, data: bytes) -> bytes:
    if len(data) < 13:  # noqa: PLR2004
        raise EncryptionError(
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


def x__decrypt_data__mutmut_6(key: bytes, data: bytes) -> bytes:
    if len(data) < 13:  # noqa: PLR2004
        raise EncryptionError(
            "Encrypted data is too short to contain nonce and ciphertext.",
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


def x__decrypt_data__mutmut_7(key: bytes, data: bytes) -> bytes:
    if len(data) < 13:  # noqa: PLR2004
        raise EncryptionError(
            "XXEncrypted data is too short to contain nonce and ciphertext.XX",
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


def x__decrypt_data__mutmut_8(key: bytes, data: bytes) -> bytes:
    if len(data) < 13:  # noqa: PLR2004
        raise EncryptionError(
            "encrypted data is too short to contain nonce and ciphertext.",
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


def x__decrypt_data__mutmut_9(key: bytes, data: bytes) -> bytes:
    if len(data) < 13:  # noqa: PLR2004
        raise EncryptionError(
            "ENCRYPTED DATA IS TOO SHORT TO CONTAIN NONCE AND CIPHERTEXT.",
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


def x__decrypt_data__mutmut_10(key: bytes, data: bytes) -> bytes:
    if len(data) < 13:  # noqa: PLR2004
        raise EncryptionError(
            "Encrypted data is too short to contain nonce and ciphertext.",
            context={"XXdata_lengthXX": str(len(data))},
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


def x__decrypt_data__mutmut_11(key: bytes, data: bytes) -> bytes:
    if len(data) < 13:  # noqa: PLR2004
        raise EncryptionError(
            "Encrypted data is too short to contain nonce and ciphertext.",
            context={"DATA_LENGTH": str(len(data))},
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


def x__decrypt_data__mutmut_12(key: bytes, data: bytes) -> bytes:
    if len(data) < 13:  # noqa: PLR2004
        raise EncryptionError(
            "Encrypted data is too short to contain nonce and ciphertext.",
            context={"data_length": str(None)},
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


def x__decrypt_data__mutmut_13(key: bytes, data: bytes) -> bytes:
    if len(data) < 13:  # noqa: PLR2004
        raise EncryptionError(
            "Encrypted data is too short to contain nonce and ciphertext.",
            context={"data_length": str(len(data))},
        )
    nonce = None
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


def x__decrypt_data__mutmut_14(key: bytes, data: bytes) -> bytes:
    if len(data) < 13:  # noqa: PLR2004
        raise EncryptionError(
            "Encrypted data is too short to contain nonce and ciphertext.",
            context={"data_length": str(len(data))},
        )
    nonce = data[:13]
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


def x__decrypt_data__mutmut_15(key: bytes, data: bytes) -> bytes:
    if len(data) < 13:  # noqa: PLR2004
        raise EncryptionError(
            "Encrypted data is too short to contain nonce and ciphertext.",
            context={"data_length": str(len(data))},
        )
    nonce = data[:12]
    ciphertext = None
    try:
        aesgcm = AESGCM(key)
        return aesgcm.decrypt(nonce, ciphertext, None)
    except Exception as e:
        raise EncryptionError(
            "Failed to decrypt database. Wrong kubeconfig, corrupted file, "
            "or encryption key mismatch.",
            context={"error": str(e)},
        ) from e


def x__decrypt_data__mutmut_16(key: bytes, data: bytes) -> bytes:
    if len(data) < 13:  # noqa: PLR2004
        raise EncryptionError(
            "Encrypted data is too short to contain nonce and ciphertext.",
            context={"data_length": str(len(data))},
        )
    nonce = data[:12]
    ciphertext = data[13:]
    try:
        aesgcm = AESGCM(key)
        return aesgcm.decrypt(nonce, ciphertext, None)
    except Exception as e:
        raise EncryptionError(
            "Failed to decrypt database. Wrong kubeconfig, corrupted file, "
            "or encryption key mismatch.",
            context={"error": str(e)},
        ) from e


def x__decrypt_data__mutmut_17(key: bytes, data: bytes) -> bytes:
    if len(data) < 13:  # noqa: PLR2004
        raise EncryptionError(
            "Encrypted data is too short to contain nonce and ciphertext.",
            context={"data_length": str(len(data))},
        )
    nonce = data[:12]
    ciphertext = data[12:]
    try:
        aesgcm = None
        return aesgcm.decrypt(nonce, ciphertext, None)
    except Exception as e:
        raise EncryptionError(
            "Failed to decrypt database. Wrong kubeconfig, corrupted file, "
            "or encryption key mismatch.",
            context={"error": str(e)},
        ) from e


def x__decrypt_data__mutmut_18(key: bytes, data: bytes) -> bytes:
    if len(data) < 13:  # noqa: PLR2004
        raise EncryptionError(
            "Encrypted data is too short to contain nonce and ciphertext.",
            context={"data_length": str(len(data))},
        )
    nonce = data[:12]
    ciphertext = data[12:]
    try:
        aesgcm = AESGCM(None)
        return aesgcm.decrypt(nonce, ciphertext, None)
    except Exception as e:
        raise EncryptionError(
            "Failed to decrypt database. Wrong kubeconfig, corrupted file, "
            "or encryption key mismatch.",
            context={"error": str(e)},
        ) from e


def x__decrypt_data__mutmut_19(key: bytes, data: bytes) -> bytes:
    if len(data) < 13:  # noqa: PLR2004
        raise EncryptionError(
            "Encrypted data is too short to contain nonce and ciphertext.",
            context={"data_length": str(len(data))},
        )
    nonce = data[:12]
    ciphertext = data[12:]
    try:
        aesgcm = AESGCM(key)
        return aesgcm.decrypt(None, ciphertext, None)
    except Exception as e:
        raise EncryptionError(
            "Failed to decrypt database. Wrong kubeconfig, corrupted file, "
            "or encryption key mismatch.",
            context={"error": str(e)},
        ) from e


def x__decrypt_data__mutmut_20(key: bytes, data: bytes) -> bytes:
    if len(data) < 13:  # noqa: PLR2004
        raise EncryptionError(
            "Encrypted data is too short to contain nonce and ciphertext.",
            context={"data_length": str(len(data))},
        )
    nonce = data[:12]
    ciphertext = data[12:]
    try:
        aesgcm = AESGCM(key)
        return aesgcm.decrypt(nonce, None, None)
    except Exception as e:
        raise EncryptionError(
            "Failed to decrypt database. Wrong kubeconfig, corrupted file, "
            "or encryption key mismatch.",
            context={"error": str(e)},
        ) from e


def x__decrypt_data__mutmut_21(key: bytes, data: bytes) -> bytes:
    if len(data) < 13:  # noqa: PLR2004
        raise EncryptionError(
            "Encrypted data is too short to contain nonce and ciphertext.",
            context={"data_length": str(len(data))},
        )
    nonce = data[:12]
    ciphertext = data[12:]
    try:
        aesgcm = AESGCM(key)
        return aesgcm.decrypt(ciphertext, None)
    except Exception as e:
        raise EncryptionError(
            "Failed to decrypt database. Wrong kubeconfig, corrupted file, "
            "or encryption key mismatch.",
            context={"error": str(e)},
        ) from e


def x__decrypt_data__mutmut_22(key: bytes, data: bytes) -> bytes:
    if len(data) < 13:  # noqa: PLR2004
        raise EncryptionError(
            "Encrypted data is too short to contain nonce and ciphertext.",
            context={"data_length": str(len(data))},
        )
    nonce = data[:12]
    ciphertext = data[12:]
    try:
        aesgcm = AESGCM(key)
        return aesgcm.decrypt(nonce, None)
    except Exception as e:
        raise EncryptionError(
            "Failed to decrypt database. Wrong kubeconfig, corrupted file, "
            "or encryption key mismatch.",
            context={"error": str(e)},
        ) from e


def x__decrypt_data__mutmut_23(key: bytes, data: bytes) -> bytes:
    if len(data) < 13:  # noqa: PLR2004
        raise EncryptionError(
            "Encrypted data is too short to contain nonce and ciphertext.",
            context={"data_length": str(len(data))},
        )
    nonce = data[:12]
    ciphertext = data[12:]
    try:
        aesgcm = AESGCM(key)
        return aesgcm.decrypt(nonce, ciphertext, )
    except Exception as e:
        raise EncryptionError(
            "Failed to decrypt database. Wrong kubeconfig, corrupted file, "
            "or encryption key mismatch.",
            context={"error": str(e)},
        ) from e


def x__decrypt_data__mutmut_24(key: bytes, data: bytes) -> bytes:
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
            None,
            context={"error": str(e)},
        ) from e


def x__decrypt_data__mutmut_25(key: bytes, data: bytes) -> bytes:
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
            context=None,
        ) from e


def x__decrypt_data__mutmut_26(key: bytes, data: bytes) -> bytes:
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
            context={"error": str(e)},
        ) from e


def x__decrypt_data__mutmut_27(key: bytes, data: bytes) -> bytes:
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
            ) from e


def x__decrypt_data__mutmut_28(key: bytes, data: bytes) -> bytes:
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
            "XXFailed to decrypt database. Wrong kubeconfig, corrupted file, XX"
            "or encryption key mismatch.",
            context={"error": str(e)},
        ) from e


def x__decrypt_data__mutmut_29(key: bytes, data: bytes) -> bytes:
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
            "failed to decrypt database. wrong kubeconfig, corrupted file, "
            "or encryption key mismatch.",
            context={"error": str(e)},
        ) from e


def x__decrypt_data__mutmut_30(key: bytes, data: bytes) -> bytes:
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
            "FAILED TO DECRYPT DATABASE. WRONG KUBECONFIG, CORRUPTED FILE, "
            "or encryption key mismatch.",
            context={"error": str(e)},
        ) from e


def x__decrypt_data__mutmut_31(key: bytes, data: bytes) -> bytes:
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
            "XXor encryption key mismatch.XX",
            context={"error": str(e)},
        ) from e


def x__decrypt_data__mutmut_32(key: bytes, data: bytes) -> bytes:
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
            "OR ENCRYPTION KEY MISMATCH.",
            context={"error": str(e)},
        ) from e


def x__decrypt_data__mutmut_33(key: bytes, data: bytes) -> bytes:
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
            context={"XXerrorXX": str(e)},
        ) from e


def x__decrypt_data__mutmut_34(key: bytes, data: bytes) -> bytes:
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
            context={"ERROR": str(e)},
        ) from e


def x__decrypt_data__mutmut_35(key: bytes, data: bytes) -> bytes:
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
            context={"error": str(None)},
        ) from e

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
mutants_x__decrypt_data__mutmut['x__decrypt_data__mutmut_16'] = x__decrypt_data__mutmut_16 # type: ignore # mutmut generated
mutants_x__decrypt_data__mutmut['x__decrypt_data__mutmut_17'] = x__decrypt_data__mutmut_17 # type: ignore # mutmut generated
mutants_x__decrypt_data__mutmut['x__decrypt_data__mutmut_18'] = x__decrypt_data__mutmut_18 # type: ignore # mutmut generated
mutants_x__decrypt_data__mutmut['x__decrypt_data__mutmut_19'] = x__decrypt_data__mutmut_19 # type: ignore # mutmut generated
mutants_x__decrypt_data__mutmut['x__decrypt_data__mutmut_20'] = x__decrypt_data__mutmut_20 # type: ignore # mutmut generated
mutants_x__decrypt_data__mutmut['x__decrypt_data__mutmut_21'] = x__decrypt_data__mutmut_21 # type: ignore # mutmut generated
mutants_x__decrypt_data__mutmut['x__decrypt_data__mutmut_22'] = x__decrypt_data__mutmut_22 # type: ignore # mutmut generated
mutants_x__decrypt_data__mutmut['x__decrypt_data__mutmut_23'] = x__decrypt_data__mutmut_23 # type: ignore # mutmut generated
mutants_x__decrypt_data__mutmut['x__decrypt_data__mutmut_24'] = x__decrypt_data__mutmut_24 # type: ignore # mutmut generated
mutants_x__decrypt_data__mutmut['x__decrypt_data__mutmut_25'] = x__decrypt_data__mutmut_25 # type: ignore # mutmut generated
mutants_x__decrypt_data__mutmut['x__decrypt_data__mutmut_26'] = x__decrypt_data__mutmut_26 # type: ignore # mutmut generated
mutants_x__decrypt_data__mutmut['x__decrypt_data__mutmut_27'] = x__decrypt_data__mutmut_27 # type: ignore # mutmut generated
mutants_x__decrypt_data__mutmut['x__decrypt_data__mutmut_28'] = x__decrypt_data__mutmut_28 # type: ignore # mutmut generated
mutants_x__decrypt_data__mutmut['x__decrypt_data__mutmut_29'] = x__decrypt_data__mutmut_29 # type: ignore # mutmut generated
mutants_x__decrypt_data__mutmut['x__decrypt_data__mutmut_30'] = x__decrypt_data__mutmut_30 # type: ignore # mutmut generated
mutants_x__decrypt_data__mutmut['x__decrypt_data__mutmut_31'] = x__decrypt_data__mutmut_31 # type: ignore # mutmut generated
mutants_x__decrypt_data__mutmut['x__decrypt_data__mutmut_32'] = x__decrypt_data__mutmut_32 # type: ignore # mutmut generated
mutants_x__decrypt_data__mutmut['x__decrypt_data__mutmut_33'] = x__decrypt_data__mutmut_33 # type: ignore # mutmut generated
mutants_x__decrypt_data__mutmut['x__decrypt_data__mutmut_34'] = x__decrypt_data__mutmut_34 # type: ignore # mutmut generated
mutants_x__decrypt_data__mutmut['x__decrypt_data__mutmut_35'] = x__decrypt_data__mutmut_35 # type: ignore # mutmut generated
mutants_x__encrypt_file__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__encrypt_file__mutmut)
def _encrypt_file(key: bytes, plain_path: Path, enc_path: Path) -> None:
    if not plain_path.exists():
        return
    plaintext = plain_path.read_bytes()
    encrypted = _encrypt_data(key, plaintext)
    enc_path.write_bytes(encrypted)
    enc_path.chmod(0o600)


def x__encrypt_file__mutmut_orig(key: bytes, plain_path: Path, enc_path: Path) -> None:
    if not plain_path.exists():
        return
    plaintext = plain_path.read_bytes()
    encrypted = _encrypt_data(key, plaintext)
    enc_path.write_bytes(encrypted)
    enc_path.chmod(0o600)


def x__encrypt_file__mutmut_1(key: bytes, plain_path: Path, enc_path: Path) -> None:
    if plain_path.exists():
        return
    plaintext = plain_path.read_bytes()
    encrypted = _encrypt_data(key, plaintext)
    enc_path.write_bytes(encrypted)
    enc_path.chmod(0o600)


def x__encrypt_file__mutmut_2(key: bytes, plain_path: Path, enc_path: Path) -> None:
    if not plain_path.exists():
        return
    plaintext = None
    encrypted = _encrypt_data(key, plaintext)
    enc_path.write_bytes(encrypted)
    enc_path.chmod(0o600)


def x__encrypt_file__mutmut_3(key: bytes, plain_path: Path, enc_path: Path) -> None:
    if not plain_path.exists():
        return
    plaintext = plain_path.read_bytes()
    encrypted = None
    enc_path.write_bytes(encrypted)
    enc_path.chmod(0o600)


def x__encrypt_file__mutmut_4(key: bytes, plain_path: Path, enc_path: Path) -> None:
    if not plain_path.exists():
        return
    plaintext = plain_path.read_bytes()
    encrypted = _encrypt_data(None, plaintext)
    enc_path.write_bytes(encrypted)
    enc_path.chmod(0o600)


def x__encrypt_file__mutmut_5(key: bytes, plain_path: Path, enc_path: Path) -> None:
    if not plain_path.exists():
        return
    plaintext = plain_path.read_bytes()
    encrypted = _encrypt_data(key, None)
    enc_path.write_bytes(encrypted)
    enc_path.chmod(0o600)


def x__encrypt_file__mutmut_6(key: bytes, plain_path: Path, enc_path: Path) -> None:
    if not plain_path.exists():
        return
    plaintext = plain_path.read_bytes()
    encrypted = _encrypt_data(plaintext)
    enc_path.write_bytes(encrypted)
    enc_path.chmod(0o600)


def x__encrypt_file__mutmut_7(key: bytes, plain_path: Path, enc_path: Path) -> None:
    if not plain_path.exists():
        return
    plaintext = plain_path.read_bytes()
    encrypted = _encrypt_data(key, )
    enc_path.write_bytes(encrypted)
    enc_path.chmod(0o600)


def x__encrypt_file__mutmut_8(key: bytes, plain_path: Path, enc_path: Path) -> None:
    if not plain_path.exists():
        return
    plaintext = plain_path.read_bytes()
    encrypted = _encrypt_data(key, plaintext)
    enc_path.write_bytes(None)
    enc_path.chmod(0o600)


def x__encrypt_file__mutmut_9(key: bytes, plain_path: Path, enc_path: Path) -> None:
    if not plain_path.exists():
        return
    plaintext = plain_path.read_bytes()
    encrypted = _encrypt_data(key, plaintext)
    enc_path.write_bytes(encrypted)
    enc_path.chmod(None)


def x__encrypt_file__mutmut_10(key: bytes, plain_path: Path, enc_path: Path) -> None:
    if not plain_path.exists():
        return
    plaintext = plain_path.read_bytes()
    encrypted = _encrypt_data(key, plaintext)
    enc_path.write_bytes(encrypted)
    enc_path.chmod(385)

mutants_x__encrypt_file__mutmut['_mutmut_orig'] = x__encrypt_file__mutmut_orig # type: ignore # mutmut generated
mutants_x__encrypt_file__mutmut['x__encrypt_file__mutmut_1'] = x__encrypt_file__mutmut_1 # type: ignore # mutmut generated
mutants_x__encrypt_file__mutmut['x__encrypt_file__mutmut_2'] = x__encrypt_file__mutmut_2 # type: ignore # mutmut generated
mutants_x__encrypt_file__mutmut['x__encrypt_file__mutmut_3'] = x__encrypt_file__mutmut_3 # type: ignore # mutmut generated
mutants_x__encrypt_file__mutmut['x__encrypt_file__mutmut_4'] = x__encrypt_file__mutmut_4 # type: ignore # mutmut generated
mutants_x__encrypt_file__mutmut['x__encrypt_file__mutmut_5'] = x__encrypt_file__mutmut_5 # type: ignore # mutmut generated
mutants_x__encrypt_file__mutmut['x__encrypt_file__mutmut_6'] = x__encrypt_file__mutmut_6 # type: ignore # mutmut generated
mutants_x__encrypt_file__mutmut['x__encrypt_file__mutmut_7'] = x__encrypt_file__mutmut_7 # type: ignore # mutmut generated
mutants_x__encrypt_file__mutmut['x__encrypt_file__mutmut_8'] = x__encrypt_file__mutmut_8 # type: ignore # mutmut generated
mutants_x__encrypt_file__mutmut['x__encrypt_file__mutmut_9'] = x__encrypt_file__mutmut_9 # type: ignore # mutmut generated
mutants_x__encrypt_file__mutmut['x__encrypt_file__mutmut_10'] = x__encrypt_file__mutmut_10 # type: ignore # mutmut generated
mutants_x__decrypt_file__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__decrypt_file__mutmut)
def _decrypt_file(key: bytes, enc_path: Path, output_path: Path) -> None:
    if not enc_path.exists():
        return
    data = enc_path.read_bytes()
    plaintext = _decrypt_data(key, data)
    output_path.write_bytes(plaintext)
    output_path.chmod(0o600)


def x__decrypt_file__mutmut_orig(key: bytes, enc_path: Path, output_path: Path) -> None:
    if not enc_path.exists():
        return
    data = enc_path.read_bytes()
    plaintext = _decrypt_data(key, data)
    output_path.write_bytes(plaintext)
    output_path.chmod(0o600)


def x__decrypt_file__mutmut_1(key: bytes, enc_path: Path, output_path: Path) -> None:
    if enc_path.exists():
        return
    data = enc_path.read_bytes()
    plaintext = _decrypt_data(key, data)
    output_path.write_bytes(plaintext)
    output_path.chmod(0o600)


def x__decrypt_file__mutmut_2(key: bytes, enc_path: Path, output_path: Path) -> None:
    if not enc_path.exists():
        return
    data = None
    plaintext = _decrypt_data(key, data)
    output_path.write_bytes(plaintext)
    output_path.chmod(0o600)


def x__decrypt_file__mutmut_3(key: bytes, enc_path: Path, output_path: Path) -> None:
    if not enc_path.exists():
        return
    data = enc_path.read_bytes()
    plaintext = None
    output_path.write_bytes(plaintext)
    output_path.chmod(0o600)


def x__decrypt_file__mutmut_4(key: bytes, enc_path: Path, output_path: Path) -> None:
    if not enc_path.exists():
        return
    data = enc_path.read_bytes()
    plaintext = _decrypt_data(None, data)
    output_path.write_bytes(plaintext)
    output_path.chmod(0o600)


def x__decrypt_file__mutmut_5(key: bytes, enc_path: Path, output_path: Path) -> None:
    if not enc_path.exists():
        return
    data = enc_path.read_bytes()
    plaintext = _decrypt_data(key, None)
    output_path.write_bytes(plaintext)
    output_path.chmod(0o600)


def x__decrypt_file__mutmut_6(key: bytes, enc_path: Path, output_path: Path) -> None:
    if not enc_path.exists():
        return
    data = enc_path.read_bytes()
    plaintext = _decrypt_data(data)
    output_path.write_bytes(plaintext)
    output_path.chmod(0o600)


def x__decrypt_file__mutmut_7(key: bytes, enc_path: Path, output_path: Path) -> None:
    if not enc_path.exists():
        return
    data = enc_path.read_bytes()
    plaintext = _decrypt_data(key, )
    output_path.write_bytes(plaintext)
    output_path.chmod(0o600)


def x__decrypt_file__mutmut_8(key: bytes, enc_path: Path, output_path: Path) -> None:
    if not enc_path.exists():
        return
    data = enc_path.read_bytes()
    plaintext = _decrypt_data(key, data)
    output_path.write_bytes(None)
    output_path.chmod(0o600)


def x__decrypt_file__mutmut_9(key: bytes, enc_path: Path, output_path: Path) -> None:
    if not enc_path.exists():
        return
    data = enc_path.read_bytes()
    plaintext = _decrypt_data(key, data)
    output_path.write_bytes(plaintext)
    output_path.chmod(None)


def x__decrypt_file__mutmut_10(key: bytes, enc_path: Path, output_path: Path) -> None:
    if not enc_path.exists():
        return
    data = enc_path.read_bytes()
    plaintext = _decrypt_data(key, data)
    output_path.write_bytes(plaintext)
    output_path.chmod(385)

mutants_x__decrypt_file__mutmut['_mutmut_orig'] = x__decrypt_file__mutmut_orig # type: ignore # mutmut generated
mutants_x__decrypt_file__mutmut['x__decrypt_file__mutmut_1'] = x__decrypt_file__mutmut_1 # type: ignore # mutmut generated
mutants_x__decrypt_file__mutmut['x__decrypt_file__mutmut_2'] = x__decrypt_file__mutmut_2 # type: ignore # mutmut generated
mutants_x__decrypt_file__mutmut['x__decrypt_file__mutmut_3'] = x__decrypt_file__mutmut_3 # type: ignore # mutmut generated
mutants_x__decrypt_file__mutmut['x__decrypt_file__mutmut_4'] = x__decrypt_file__mutmut_4 # type: ignore # mutmut generated
mutants_x__decrypt_file__mutmut['x__decrypt_file__mutmut_5'] = x__decrypt_file__mutmut_5 # type: ignore # mutmut generated
mutants_x__decrypt_file__mutmut['x__decrypt_file__mutmut_6'] = x__decrypt_file__mutmut_6 # type: ignore # mutmut generated
mutants_x__decrypt_file__mutmut['x__decrypt_file__mutmut_7'] = x__decrypt_file__mutmut_7 # type: ignore # mutmut generated
mutants_x__decrypt_file__mutmut['x__decrypt_file__mutmut_8'] = x__decrypt_file__mutmut_8 # type: ignore # mutmut generated
mutants_x__decrypt_file__mutmut['x__decrypt_file__mutmut_9'] = x__decrypt_file__mutmut_9 # type: ignore # mutmut generated
mutants_x__decrypt_file__mutmut['x__decrypt_file__mutmut_10'] = x__decrypt_file__mutmut_10 # type: ignore # mutmut generated
mutants_x__encrypt_db_on_exit__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__encrypt_db_on_exit__mutmut)
def _encrypt_db_on_exit(key: bytes) -> None:
    if DB_PATH.exists():
        _encrypt_file(key, DB_PATH, ENCRYPTED_DB_PATH)
        DB_PATH.unlink(missing_ok=True)


def x__encrypt_db_on_exit__mutmut_orig(key: bytes) -> None:
    if DB_PATH.exists():
        _encrypt_file(key, DB_PATH, ENCRYPTED_DB_PATH)
        DB_PATH.unlink(missing_ok=True)


def x__encrypt_db_on_exit__mutmut_1(key: bytes) -> None:
    if DB_PATH.exists():
        _encrypt_file(None, DB_PATH, ENCRYPTED_DB_PATH)
        DB_PATH.unlink(missing_ok=True)


def x__encrypt_db_on_exit__mutmut_2(key: bytes) -> None:
    if DB_PATH.exists():
        _encrypt_file(key, None, ENCRYPTED_DB_PATH)
        DB_PATH.unlink(missing_ok=True)


def x__encrypt_db_on_exit__mutmut_3(key: bytes) -> None:
    if DB_PATH.exists():
        _encrypt_file(key, DB_PATH, None)
        DB_PATH.unlink(missing_ok=True)


def x__encrypt_db_on_exit__mutmut_4(key: bytes) -> None:
    if DB_PATH.exists():
        _encrypt_file(DB_PATH, ENCRYPTED_DB_PATH)
        DB_PATH.unlink(missing_ok=True)


def x__encrypt_db_on_exit__mutmut_5(key: bytes) -> None:
    if DB_PATH.exists():
        _encrypt_file(key, ENCRYPTED_DB_PATH)
        DB_PATH.unlink(missing_ok=True)


def x__encrypt_db_on_exit__mutmut_6(key: bytes) -> None:
    if DB_PATH.exists():
        _encrypt_file(key, DB_PATH, )
        DB_PATH.unlink(missing_ok=True)


def x__encrypt_db_on_exit__mutmut_7(key: bytes) -> None:
    if DB_PATH.exists():
        _encrypt_file(key, DB_PATH, ENCRYPTED_DB_PATH)
        DB_PATH.unlink(missing_ok=None)


def x__encrypt_db_on_exit__mutmut_8(key: bytes) -> None:
    if DB_PATH.exists():
        _encrypt_file(key, DB_PATH, ENCRYPTED_DB_PATH)
        DB_PATH.unlink(missing_ok=False)

mutants_x__encrypt_db_on_exit__mutmut['_mutmut_orig'] = x__encrypt_db_on_exit__mutmut_orig # type: ignore # mutmut generated
mutants_x__encrypt_db_on_exit__mutmut['x__encrypt_db_on_exit__mutmut_1'] = x__encrypt_db_on_exit__mutmut_1 # type: ignore # mutmut generated
mutants_x__encrypt_db_on_exit__mutmut['x__encrypt_db_on_exit__mutmut_2'] = x__encrypt_db_on_exit__mutmut_2 # type: ignore # mutmut generated
mutants_x__encrypt_db_on_exit__mutmut['x__encrypt_db_on_exit__mutmut_3'] = x__encrypt_db_on_exit__mutmut_3 # type: ignore # mutmut generated
mutants_x__encrypt_db_on_exit__mutmut['x__encrypt_db_on_exit__mutmut_4'] = x__encrypt_db_on_exit__mutmut_4 # type: ignore # mutmut generated
mutants_x__encrypt_db_on_exit__mutmut['x__encrypt_db_on_exit__mutmut_5'] = x__encrypt_db_on_exit__mutmut_5 # type: ignore # mutmut generated
mutants_x__encrypt_db_on_exit__mutmut['x__encrypt_db_on_exit__mutmut_6'] = x__encrypt_db_on_exit__mutmut_6 # type: ignore # mutmut generated
mutants_x__encrypt_db_on_exit__mutmut['x__encrypt_db_on_exit__mutmut_7'] = x__encrypt_db_on_exit__mutmut_7 # type: ignore # mutmut generated
mutants_x__encrypt_db_on_exit__mutmut['x__encrypt_db_on_exit__mutmut_8'] = x__encrypt_db_on_exit__mutmut_8 # type: ignore # mutmut generated
mutants_x__quarantine_orphaned_enc__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__quarantine_orphaned_enc__mutmut)
def _quarantine_orphaned_enc() -> None:
    """Rename an undecryptable .enc aside instead of deleting it.

    The quarantine suffix preserves the file for auditing should the key
    ever be recovered, while letting a fresh database be created.
    """
    if not ENCRYPTED_DB_PATH.exists():
        return
    ts = datetime.now(UTC).strftime("%Y%m%d-%H%M%S")
    orphan_path = ENCRYPTED_DB_PATH.with_name(f"{ENCRYPTED_DB_PATH.name}.orphan-{ts}")
    try:
        ENCRYPTED_DB_PATH.rename(orphan_path)
        logger.warning(
            "Detected an orphaned encrypted database (key mismatch). Quarantined "
            "it to %s and will start with a fresh database.",
            orphan_path,
        )
    except OSError:
        logger.warning("Could not quarantine orphaned encrypted database at %s", ENCRYPTED_DB_PATH)


def x__quarantine_orphaned_enc__mutmut_orig() -> None:
    """Rename an undecryptable .enc aside instead of deleting it.

    The quarantine suffix preserves the file for auditing should the key
    ever be recovered, while letting a fresh database be created.
    """
    if not ENCRYPTED_DB_PATH.exists():
        return
    ts = datetime.now(UTC).strftime("%Y%m%d-%H%M%S")
    orphan_path = ENCRYPTED_DB_PATH.with_name(f"{ENCRYPTED_DB_PATH.name}.orphan-{ts}")
    try:
        ENCRYPTED_DB_PATH.rename(orphan_path)
        logger.warning(
            "Detected an orphaned encrypted database (key mismatch). Quarantined "
            "it to %s and will start with a fresh database.",
            orphan_path,
        )
    except OSError:
        logger.warning("Could not quarantine orphaned encrypted database at %s", ENCRYPTED_DB_PATH)


def x__quarantine_orphaned_enc__mutmut_1() -> None:
    """Rename an undecryptable .enc aside instead of deleting it.

    The quarantine suffix preserves the file for auditing should the key
    ever be recovered, while letting a fresh database be created.
    """
    if ENCRYPTED_DB_PATH.exists():
        return
    ts = datetime.now(UTC).strftime("%Y%m%d-%H%M%S")
    orphan_path = ENCRYPTED_DB_PATH.with_name(f"{ENCRYPTED_DB_PATH.name}.orphan-{ts}")
    try:
        ENCRYPTED_DB_PATH.rename(orphan_path)
        logger.warning(
            "Detected an orphaned encrypted database (key mismatch). Quarantined "
            "it to %s and will start with a fresh database.",
            orphan_path,
        )
    except OSError:
        logger.warning("Could not quarantine orphaned encrypted database at %s", ENCRYPTED_DB_PATH)


def x__quarantine_orphaned_enc__mutmut_2() -> None:
    """Rename an undecryptable .enc aside instead of deleting it.

    The quarantine suffix preserves the file for auditing should the key
    ever be recovered, while letting a fresh database be created.
    """
    if not ENCRYPTED_DB_PATH.exists():
        return
    ts = None
    orphan_path = ENCRYPTED_DB_PATH.with_name(f"{ENCRYPTED_DB_PATH.name}.orphan-{ts}")
    try:
        ENCRYPTED_DB_PATH.rename(orphan_path)
        logger.warning(
            "Detected an orphaned encrypted database (key mismatch). Quarantined "
            "it to %s and will start with a fresh database.",
            orphan_path,
        )
    except OSError:
        logger.warning("Could not quarantine orphaned encrypted database at %s", ENCRYPTED_DB_PATH)


def x__quarantine_orphaned_enc__mutmut_3() -> None:
    """Rename an undecryptable .enc aside instead of deleting it.

    The quarantine suffix preserves the file for auditing should the key
    ever be recovered, while letting a fresh database be created.
    """
    if not ENCRYPTED_DB_PATH.exists():
        return
    ts = datetime.now(UTC).strftime(None)
    orphan_path = ENCRYPTED_DB_PATH.with_name(f"{ENCRYPTED_DB_PATH.name}.orphan-{ts}")
    try:
        ENCRYPTED_DB_PATH.rename(orphan_path)
        logger.warning(
            "Detected an orphaned encrypted database (key mismatch). Quarantined "
            "it to %s and will start with a fresh database.",
            orphan_path,
        )
    except OSError:
        logger.warning("Could not quarantine orphaned encrypted database at %s", ENCRYPTED_DB_PATH)


def x__quarantine_orphaned_enc__mutmut_4() -> None:
    """Rename an undecryptable .enc aside instead of deleting it.

    The quarantine suffix preserves the file for auditing should the key
    ever be recovered, while letting a fresh database be created.
    """
    if not ENCRYPTED_DB_PATH.exists():
        return
    ts = datetime.now(None).strftime("%Y%m%d-%H%M%S")
    orphan_path = ENCRYPTED_DB_PATH.with_name(f"{ENCRYPTED_DB_PATH.name}.orphan-{ts}")
    try:
        ENCRYPTED_DB_PATH.rename(orphan_path)
        logger.warning(
            "Detected an orphaned encrypted database (key mismatch). Quarantined "
            "it to %s and will start with a fresh database.",
            orphan_path,
        )
    except OSError:
        logger.warning("Could not quarantine orphaned encrypted database at %s", ENCRYPTED_DB_PATH)


def x__quarantine_orphaned_enc__mutmut_5() -> None:
    """Rename an undecryptable .enc aside instead of deleting it.

    The quarantine suffix preserves the file for auditing should the key
    ever be recovered, while letting a fresh database be created.
    """
    if not ENCRYPTED_DB_PATH.exists():
        return
    ts = datetime.now(UTC).strftime("XX%Y%m%d-%H%M%SXX")
    orphan_path = ENCRYPTED_DB_PATH.with_name(f"{ENCRYPTED_DB_PATH.name}.orphan-{ts}")
    try:
        ENCRYPTED_DB_PATH.rename(orphan_path)
        logger.warning(
            "Detected an orphaned encrypted database (key mismatch). Quarantined "
            "it to %s and will start with a fresh database.",
            orphan_path,
        )
    except OSError:
        logger.warning("Could not quarantine orphaned encrypted database at %s", ENCRYPTED_DB_PATH)


def x__quarantine_orphaned_enc__mutmut_6() -> None:
    """Rename an undecryptable .enc aside instead of deleting it.

    The quarantine suffix preserves the file for auditing should the key
    ever be recovered, while letting a fresh database be created.
    """
    if not ENCRYPTED_DB_PATH.exists():
        return
    ts = datetime.now(UTC).strftime("%y%m%d-%h%m%s")
    orphan_path = ENCRYPTED_DB_PATH.with_name(f"{ENCRYPTED_DB_PATH.name}.orphan-{ts}")
    try:
        ENCRYPTED_DB_PATH.rename(orphan_path)
        logger.warning(
            "Detected an orphaned encrypted database (key mismatch). Quarantined "
            "it to %s and will start with a fresh database.",
            orphan_path,
        )
    except OSError:
        logger.warning("Could not quarantine orphaned encrypted database at %s", ENCRYPTED_DB_PATH)


def x__quarantine_orphaned_enc__mutmut_7() -> None:
    """Rename an undecryptable .enc aside instead of deleting it.

    The quarantine suffix preserves the file for auditing should the key
    ever be recovered, while letting a fresh database be created.
    """
    if not ENCRYPTED_DB_PATH.exists():
        return
    ts = datetime.now(UTC).strftime("%Y%M%D-%H%M%S")
    orphan_path = ENCRYPTED_DB_PATH.with_name(f"{ENCRYPTED_DB_PATH.name}.orphan-{ts}")
    try:
        ENCRYPTED_DB_PATH.rename(orphan_path)
        logger.warning(
            "Detected an orphaned encrypted database (key mismatch). Quarantined "
            "it to %s and will start with a fresh database.",
            orphan_path,
        )
    except OSError:
        logger.warning("Could not quarantine orphaned encrypted database at %s", ENCRYPTED_DB_PATH)


def x__quarantine_orphaned_enc__mutmut_8() -> None:
    """Rename an undecryptable .enc aside instead of deleting it.

    The quarantine suffix preserves the file for auditing should the key
    ever be recovered, while letting a fresh database be created.
    """
    if not ENCRYPTED_DB_PATH.exists():
        return
    ts = datetime.now(UTC).strftime("%Y%m%d-%H%M%S")
    orphan_path = None
    try:
        ENCRYPTED_DB_PATH.rename(orphan_path)
        logger.warning(
            "Detected an orphaned encrypted database (key mismatch). Quarantined "
            "it to %s and will start with a fresh database.",
            orphan_path,
        )
    except OSError:
        logger.warning("Could not quarantine orphaned encrypted database at %s", ENCRYPTED_DB_PATH)


def x__quarantine_orphaned_enc__mutmut_9() -> None:
    """Rename an undecryptable .enc aside instead of deleting it.

    The quarantine suffix preserves the file for auditing should the key
    ever be recovered, while letting a fresh database be created.
    """
    if not ENCRYPTED_DB_PATH.exists():
        return
    ts = datetime.now(UTC).strftime("%Y%m%d-%H%M%S")
    orphan_path = ENCRYPTED_DB_PATH.with_name(None)
    try:
        ENCRYPTED_DB_PATH.rename(orphan_path)
        logger.warning(
            "Detected an orphaned encrypted database (key mismatch). Quarantined "
            "it to %s and will start with a fresh database.",
            orphan_path,
        )
    except OSError:
        logger.warning("Could not quarantine orphaned encrypted database at %s", ENCRYPTED_DB_PATH)


def x__quarantine_orphaned_enc__mutmut_10() -> None:
    """Rename an undecryptable .enc aside instead of deleting it.

    The quarantine suffix preserves the file for auditing should the key
    ever be recovered, while letting a fresh database be created.
    """
    if not ENCRYPTED_DB_PATH.exists():
        return
    ts = datetime.now(UTC).strftime("%Y%m%d-%H%M%S")
    orphan_path = ENCRYPTED_DB_PATH.with_name(f"{ENCRYPTED_DB_PATH.name}.orphan-{ts}")
    try:
        ENCRYPTED_DB_PATH.rename(None)
        logger.warning(
            "Detected an orphaned encrypted database (key mismatch). Quarantined "
            "it to %s and will start with a fresh database.",
            orphan_path,
        )
    except OSError:
        logger.warning("Could not quarantine orphaned encrypted database at %s", ENCRYPTED_DB_PATH)


def x__quarantine_orphaned_enc__mutmut_11() -> None:
    """Rename an undecryptable .enc aside instead of deleting it.

    The quarantine suffix preserves the file for auditing should the key
    ever be recovered, while letting a fresh database be created.
    """
    if not ENCRYPTED_DB_PATH.exists():
        return
    ts = datetime.now(UTC).strftime("%Y%m%d-%H%M%S")
    orphan_path = ENCRYPTED_DB_PATH.with_name(f"{ENCRYPTED_DB_PATH.name}.orphan-{ts}")
    try:
        ENCRYPTED_DB_PATH.rename(orphan_path)
        logger.warning(
            None,
            orphan_path,
        )
    except OSError:
        logger.warning("Could not quarantine orphaned encrypted database at %s", ENCRYPTED_DB_PATH)


def x__quarantine_orphaned_enc__mutmut_12() -> None:
    """Rename an undecryptable .enc aside instead of deleting it.

    The quarantine suffix preserves the file for auditing should the key
    ever be recovered, while letting a fresh database be created.
    """
    if not ENCRYPTED_DB_PATH.exists():
        return
    ts = datetime.now(UTC).strftime("%Y%m%d-%H%M%S")
    orphan_path = ENCRYPTED_DB_PATH.with_name(f"{ENCRYPTED_DB_PATH.name}.orphan-{ts}")
    try:
        ENCRYPTED_DB_PATH.rename(orphan_path)
        logger.warning(
            "Detected an orphaned encrypted database (key mismatch). Quarantined "
            "it to %s and will start with a fresh database.",
            None,
        )
    except OSError:
        logger.warning("Could not quarantine orphaned encrypted database at %s", ENCRYPTED_DB_PATH)


def x__quarantine_orphaned_enc__mutmut_13() -> None:
    """Rename an undecryptable .enc aside instead of deleting it.

    The quarantine suffix preserves the file for auditing should the key
    ever be recovered, while letting a fresh database be created.
    """
    if not ENCRYPTED_DB_PATH.exists():
        return
    ts = datetime.now(UTC).strftime("%Y%m%d-%H%M%S")
    orphan_path = ENCRYPTED_DB_PATH.with_name(f"{ENCRYPTED_DB_PATH.name}.orphan-{ts}")
    try:
        ENCRYPTED_DB_PATH.rename(orphan_path)
        logger.warning(
            orphan_path,
        )
    except OSError:
        logger.warning("Could not quarantine orphaned encrypted database at %s", ENCRYPTED_DB_PATH)


def x__quarantine_orphaned_enc__mutmut_14() -> None:
    """Rename an undecryptable .enc aside instead of deleting it.

    The quarantine suffix preserves the file for auditing should the key
    ever be recovered, while letting a fresh database be created.
    """
    if not ENCRYPTED_DB_PATH.exists():
        return
    ts = datetime.now(UTC).strftime("%Y%m%d-%H%M%S")
    orphan_path = ENCRYPTED_DB_PATH.with_name(f"{ENCRYPTED_DB_PATH.name}.orphan-{ts}")
    try:
        ENCRYPTED_DB_PATH.rename(orphan_path)
        logger.warning(
            "Detected an orphaned encrypted database (key mismatch). Quarantined "
            "it to %s and will start with a fresh database.",
            )
    except OSError:
        logger.warning("Could not quarantine orphaned encrypted database at %s", ENCRYPTED_DB_PATH)


def x__quarantine_orphaned_enc__mutmut_15() -> None:
    """Rename an undecryptable .enc aside instead of deleting it.

    The quarantine suffix preserves the file for auditing should the key
    ever be recovered, while letting a fresh database be created.
    """
    if not ENCRYPTED_DB_PATH.exists():
        return
    ts = datetime.now(UTC).strftime("%Y%m%d-%H%M%S")
    orphan_path = ENCRYPTED_DB_PATH.with_name(f"{ENCRYPTED_DB_PATH.name}.orphan-{ts}")
    try:
        ENCRYPTED_DB_PATH.rename(orphan_path)
        logger.warning(
            "XXDetected an orphaned encrypted database (key mismatch). Quarantined XX"
            "it to %s and will start with a fresh database.",
            orphan_path,
        )
    except OSError:
        logger.warning("Could not quarantine orphaned encrypted database at %s", ENCRYPTED_DB_PATH)


def x__quarantine_orphaned_enc__mutmut_16() -> None:
    """Rename an undecryptable .enc aside instead of deleting it.

    The quarantine suffix preserves the file for auditing should the key
    ever be recovered, while letting a fresh database be created.
    """
    if not ENCRYPTED_DB_PATH.exists():
        return
    ts = datetime.now(UTC).strftime("%Y%m%d-%H%M%S")
    orphan_path = ENCRYPTED_DB_PATH.with_name(f"{ENCRYPTED_DB_PATH.name}.orphan-{ts}")
    try:
        ENCRYPTED_DB_PATH.rename(orphan_path)
        logger.warning(
            "detected an orphaned encrypted database (key mismatch). quarantined "
            "it to %s and will start with a fresh database.",
            orphan_path,
        )
    except OSError:
        logger.warning("Could not quarantine orphaned encrypted database at %s", ENCRYPTED_DB_PATH)


def x__quarantine_orphaned_enc__mutmut_17() -> None:
    """Rename an undecryptable .enc aside instead of deleting it.

    The quarantine suffix preserves the file for auditing should the key
    ever be recovered, while letting a fresh database be created.
    """
    if not ENCRYPTED_DB_PATH.exists():
        return
    ts = datetime.now(UTC).strftime("%Y%m%d-%H%M%S")
    orphan_path = ENCRYPTED_DB_PATH.with_name(f"{ENCRYPTED_DB_PATH.name}.orphan-{ts}")
    try:
        ENCRYPTED_DB_PATH.rename(orphan_path)
        logger.warning(
            "DETECTED AN ORPHANED ENCRYPTED DATABASE (KEY MISMATCH). QUARANTINED "
            "it to %s and will start with a fresh database.",
            orphan_path,
        )
    except OSError:
        logger.warning("Could not quarantine orphaned encrypted database at %s", ENCRYPTED_DB_PATH)


def x__quarantine_orphaned_enc__mutmut_18() -> None:
    """Rename an undecryptable .enc aside instead of deleting it.

    The quarantine suffix preserves the file for auditing should the key
    ever be recovered, while letting a fresh database be created.
    """
    if not ENCRYPTED_DB_PATH.exists():
        return
    ts = datetime.now(UTC).strftime("%Y%m%d-%H%M%S")
    orphan_path = ENCRYPTED_DB_PATH.with_name(f"{ENCRYPTED_DB_PATH.name}.orphan-{ts}")
    try:
        ENCRYPTED_DB_PATH.rename(orphan_path)
        logger.warning(
            "Detected an orphaned encrypted database (key mismatch). Quarantined "
            "XXit to %s and will start with a fresh database.XX",
            orphan_path,
        )
    except OSError:
        logger.warning("Could not quarantine orphaned encrypted database at %s", ENCRYPTED_DB_PATH)


def x__quarantine_orphaned_enc__mutmut_19() -> None:
    """Rename an undecryptable .enc aside instead of deleting it.

    The quarantine suffix preserves the file for auditing should the key
    ever be recovered, while letting a fresh database be created.
    """
    if not ENCRYPTED_DB_PATH.exists():
        return
    ts = datetime.now(UTC).strftime("%Y%m%d-%H%M%S")
    orphan_path = ENCRYPTED_DB_PATH.with_name(f"{ENCRYPTED_DB_PATH.name}.orphan-{ts}")
    try:
        ENCRYPTED_DB_PATH.rename(orphan_path)
        logger.warning(
            "Detected an orphaned encrypted database (key mismatch). Quarantined "
            "IT TO %S AND WILL START WITH A FRESH DATABASE.",
            orphan_path,
        )
    except OSError:
        logger.warning("Could not quarantine orphaned encrypted database at %s", ENCRYPTED_DB_PATH)


def x__quarantine_orphaned_enc__mutmut_20() -> None:
    """Rename an undecryptable .enc aside instead of deleting it.

    The quarantine suffix preserves the file for auditing should the key
    ever be recovered, while letting a fresh database be created.
    """
    if not ENCRYPTED_DB_PATH.exists():
        return
    ts = datetime.now(UTC).strftime("%Y%m%d-%H%M%S")
    orphan_path = ENCRYPTED_DB_PATH.with_name(f"{ENCRYPTED_DB_PATH.name}.orphan-{ts}")
    try:
        ENCRYPTED_DB_PATH.rename(orphan_path)
        logger.warning(
            "Detected an orphaned encrypted database (key mismatch). Quarantined "
            "it to %s and will start with a fresh database.",
            orphan_path,
        )
    except OSError:
        logger.warning(None, ENCRYPTED_DB_PATH)


def x__quarantine_orphaned_enc__mutmut_21() -> None:
    """Rename an undecryptable .enc aside instead of deleting it.

    The quarantine suffix preserves the file for auditing should the key
    ever be recovered, while letting a fresh database be created.
    """
    if not ENCRYPTED_DB_PATH.exists():
        return
    ts = datetime.now(UTC).strftime("%Y%m%d-%H%M%S")
    orphan_path = ENCRYPTED_DB_PATH.with_name(f"{ENCRYPTED_DB_PATH.name}.orphan-{ts}")
    try:
        ENCRYPTED_DB_PATH.rename(orphan_path)
        logger.warning(
            "Detected an orphaned encrypted database (key mismatch). Quarantined "
            "it to %s and will start with a fresh database.",
            orphan_path,
        )
    except OSError:
        logger.warning("Could not quarantine orphaned encrypted database at %s", None)


def x__quarantine_orphaned_enc__mutmut_22() -> None:
    """Rename an undecryptable .enc aside instead of deleting it.

    The quarantine suffix preserves the file for auditing should the key
    ever be recovered, while letting a fresh database be created.
    """
    if not ENCRYPTED_DB_PATH.exists():
        return
    ts = datetime.now(UTC).strftime("%Y%m%d-%H%M%S")
    orphan_path = ENCRYPTED_DB_PATH.with_name(f"{ENCRYPTED_DB_PATH.name}.orphan-{ts}")
    try:
        ENCRYPTED_DB_PATH.rename(orphan_path)
        logger.warning(
            "Detected an orphaned encrypted database (key mismatch). Quarantined "
            "it to %s and will start with a fresh database.",
            orphan_path,
        )
    except OSError:
        logger.warning(ENCRYPTED_DB_PATH)


def x__quarantine_orphaned_enc__mutmut_23() -> None:
    """Rename an undecryptable .enc aside instead of deleting it.

    The quarantine suffix preserves the file for auditing should the key
    ever be recovered, while letting a fresh database be created.
    """
    if not ENCRYPTED_DB_PATH.exists():
        return
    ts = datetime.now(UTC).strftime("%Y%m%d-%H%M%S")
    orphan_path = ENCRYPTED_DB_PATH.with_name(f"{ENCRYPTED_DB_PATH.name}.orphan-{ts}")
    try:
        ENCRYPTED_DB_PATH.rename(orphan_path)
        logger.warning(
            "Detected an orphaned encrypted database (key mismatch). Quarantined "
            "it to %s and will start with a fresh database.",
            orphan_path,
        )
    except OSError:
        logger.warning("Could not quarantine orphaned encrypted database at %s", )


def x__quarantine_orphaned_enc__mutmut_24() -> None:
    """Rename an undecryptable .enc aside instead of deleting it.

    The quarantine suffix preserves the file for auditing should the key
    ever be recovered, while letting a fresh database be created.
    """
    if not ENCRYPTED_DB_PATH.exists():
        return
    ts = datetime.now(UTC).strftime("%Y%m%d-%H%M%S")
    orphan_path = ENCRYPTED_DB_PATH.with_name(f"{ENCRYPTED_DB_PATH.name}.orphan-{ts}")
    try:
        ENCRYPTED_DB_PATH.rename(orphan_path)
        logger.warning(
            "Detected an orphaned encrypted database (key mismatch). Quarantined "
            "it to %s and will start with a fresh database.",
            orphan_path,
        )
    except OSError:
        logger.warning("XXCould not quarantine orphaned encrypted database at %sXX", ENCRYPTED_DB_PATH)


def x__quarantine_orphaned_enc__mutmut_25() -> None:
    """Rename an undecryptable .enc aside instead of deleting it.

    The quarantine suffix preserves the file for auditing should the key
    ever be recovered, while letting a fresh database be created.
    """
    if not ENCRYPTED_DB_PATH.exists():
        return
    ts = datetime.now(UTC).strftime("%Y%m%d-%H%M%S")
    orphan_path = ENCRYPTED_DB_PATH.with_name(f"{ENCRYPTED_DB_PATH.name}.orphan-{ts}")
    try:
        ENCRYPTED_DB_PATH.rename(orphan_path)
        logger.warning(
            "Detected an orphaned encrypted database (key mismatch). Quarantined "
            "it to %s and will start with a fresh database.",
            orphan_path,
        )
    except OSError:
        logger.warning("could not quarantine orphaned encrypted database at %s", ENCRYPTED_DB_PATH)


def x__quarantine_orphaned_enc__mutmut_26() -> None:
    """Rename an undecryptable .enc aside instead of deleting it.

    The quarantine suffix preserves the file for auditing should the key
    ever be recovered, while letting a fresh database be created.
    """
    if not ENCRYPTED_DB_PATH.exists():
        return
    ts = datetime.now(UTC).strftime("%Y%m%d-%H%M%S")
    orphan_path = ENCRYPTED_DB_PATH.with_name(f"{ENCRYPTED_DB_PATH.name}.orphan-{ts}")
    try:
        ENCRYPTED_DB_PATH.rename(orphan_path)
        logger.warning(
            "Detected an orphaned encrypted database (key mismatch). Quarantined "
            "it to %s and will start with a fresh database.",
            orphan_path,
        )
    except OSError:
        logger.warning("COULD NOT QUARANTINE ORPHANED ENCRYPTED DATABASE AT %S", ENCRYPTED_DB_PATH)

mutants_x__quarantine_orphaned_enc__mutmut['_mutmut_orig'] = x__quarantine_orphaned_enc__mutmut_orig # type: ignore # mutmut generated
mutants_x__quarantine_orphaned_enc__mutmut['x__quarantine_orphaned_enc__mutmut_1'] = x__quarantine_orphaned_enc__mutmut_1 # type: ignore # mutmut generated
mutants_x__quarantine_orphaned_enc__mutmut['x__quarantine_orphaned_enc__mutmut_2'] = x__quarantine_orphaned_enc__mutmut_2 # type: ignore # mutmut generated
mutants_x__quarantine_orphaned_enc__mutmut['x__quarantine_orphaned_enc__mutmut_3'] = x__quarantine_orphaned_enc__mutmut_3 # type: ignore # mutmut generated
mutants_x__quarantine_orphaned_enc__mutmut['x__quarantine_orphaned_enc__mutmut_4'] = x__quarantine_orphaned_enc__mutmut_4 # type: ignore # mutmut generated
mutants_x__quarantine_orphaned_enc__mutmut['x__quarantine_orphaned_enc__mutmut_5'] = x__quarantine_orphaned_enc__mutmut_5 # type: ignore # mutmut generated
mutants_x__quarantine_orphaned_enc__mutmut['x__quarantine_orphaned_enc__mutmut_6'] = x__quarantine_orphaned_enc__mutmut_6 # type: ignore # mutmut generated
mutants_x__quarantine_orphaned_enc__mutmut['x__quarantine_orphaned_enc__mutmut_7'] = x__quarantine_orphaned_enc__mutmut_7 # type: ignore # mutmut generated
mutants_x__quarantine_orphaned_enc__mutmut['x__quarantine_orphaned_enc__mutmut_8'] = x__quarantine_orphaned_enc__mutmut_8 # type: ignore # mutmut generated
mutants_x__quarantine_orphaned_enc__mutmut['x__quarantine_orphaned_enc__mutmut_9'] = x__quarantine_orphaned_enc__mutmut_9 # type: ignore # mutmut generated
mutants_x__quarantine_orphaned_enc__mutmut['x__quarantine_orphaned_enc__mutmut_10'] = x__quarantine_orphaned_enc__mutmut_10 # type: ignore # mutmut generated
mutants_x__quarantine_orphaned_enc__mutmut['x__quarantine_orphaned_enc__mutmut_11'] = x__quarantine_orphaned_enc__mutmut_11 # type: ignore # mutmut generated
mutants_x__quarantine_orphaned_enc__mutmut['x__quarantine_orphaned_enc__mutmut_12'] = x__quarantine_orphaned_enc__mutmut_12 # type: ignore # mutmut generated
mutants_x__quarantine_orphaned_enc__mutmut['x__quarantine_orphaned_enc__mutmut_13'] = x__quarantine_orphaned_enc__mutmut_13 # type: ignore # mutmut generated
mutants_x__quarantine_orphaned_enc__mutmut['x__quarantine_orphaned_enc__mutmut_14'] = x__quarantine_orphaned_enc__mutmut_14 # type: ignore # mutmut generated
mutants_x__quarantine_orphaned_enc__mutmut['x__quarantine_orphaned_enc__mutmut_15'] = x__quarantine_orphaned_enc__mutmut_15 # type: ignore # mutmut generated
mutants_x__quarantine_orphaned_enc__mutmut['x__quarantine_orphaned_enc__mutmut_16'] = x__quarantine_orphaned_enc__mutmut_16 # type: ignore # mutmut generated
mutants_x__quarantine_orphaned_enc__mutmut['x__quarantine_orphaned_enc__mutmut_17'] = x__quarantine_orphaned_enc__mutmut_17 # type: ignore # mutmut generated
mutants_x__quarantine_orphaned_enc__mutmut['x__quarantine_orphaned_enc__mutmut_18'] = x__quarantine_orphaned_enc__mutmut_18 # type: ignore # mutmut generated
mutants_x__quarantine_orphaned_enc__mutmut['x__quarantine_orphaned_enc__mutmut_19'] = x__quarantine_orphaned_enc__mutmut_19 # type: ignore # mutmut generated
mutants_x__quarantine_orphaned_enc__mutmut['x__quarantine_orphaned_enc__mutmut_20'] = x__quarantine_orphaned_enc__mutmut_20 # type: ignore # mutmut generated
mutants_x__quarantine_orphaned_enc__mutmut['x__quarantine_orphaned_enc__mutmut_21'] = x__quarantine_orphaned_enc__mutmut_21 # type: ignore # mutmut generated
mutants_x__quarantine_orphaned_enc__mutmut['x__quarantine_orphaned_enc__mutmut_22'] = x__quarantine_orphaned_enc__mutmut_22 # type: ignore # mutmut generated
mutants_x__quarantine_orphaned_enc__mutmut['x__quarantine_orphaned_enc__mutmut_23'] = x__quarantine_orphaned_enc__mutmut_23 # type: ignore # mutmut generated
mutants_x__quarantine_orphaned_enc__mutmut['x__quarantine_orphaned_enc__mutmut_24'] = x__quarantine_orphaned_enc__mutmut_24 # type: ignore # mutmut generated
mutants_x__quarantine_orphaned_enc__mutmut['x__quarantine_orphaned_enc__mutmut_25'] = x__quarantine_orphaned_enc__mutmut_25 # type: ignore # mutmut generated
mutants_x__quarantine_orphaned_enc__mutmut['x__quarantine_orphaned_enc__mutmut_26'] = x__quarantine_orphaned_enc__mutmut_26 # type: ignore # mutmut generated
mutants_x_prepare_db__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_prepare_db__mutmut)
def prepare_db(key: bytes) -> None:
    global _db_prepared, _atexit_registered
    if _db_prepared:
        return

    HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

    if ENCRYPTED_DB_PATH.exists():
        try:
            _decrypt_file(key, ENCRYPTED_DB_PATH, DB_PATH)
        except EncryptionError:
            _quarantine_orphaned_enc()

    if not _atexit_registered:
        atexit.register(_encrypt_db_on_exit, key)
        _atexit_registered = True

    _db_prepared = True


def x_prepare_db__mutmut_orig(key: bytes) -> None:
    global _db_prepared, _atexit_registered
    if _db_prepared:
        return

    HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

    if ENCRYPTED_DB_PATH.exists():
        try:
            _decrypt_file(key, ENCRYPTED_DB_PATH, DB_PATH)
        except EncryptionError:
            _quarantine_orphaned_enc()

    if not _atexit_registered:
        atexit.register(_encrypt_db_on_exit, key)
        _atexit_registered = True

    _db_prepared = True


def x_prepare_db__mutmut_1(key: bytes) -> None:
    global _db_prepared, _atexit_registered
    if _db_prepared:
        return

    HEXAWYN_DIR.mkdir(parents=None, exist_ok=True)

    if ENCRYPTED_DB_PATH.exists():
        try:
            _decrypt_file(key, ENCRYPTED_DB_PATH, DB_PATH)
        except EncryptionError:
            _quarantine_orphaned_enc()

    if not _atexit_registered:
        atexit.register(_encrypt_db_on_exit, key)
        _atexit_registered = True

    _db_prepared = True


def x_prepare_db__mutmut_2(key: bytes) -> None:
    global _db_prepared, _atexit_registered
    if _db_prepared:
        return

    HEXAWYN_DIR.mkdir(parents=True, exist_ok=None)

    if ENCRYPTED_DB_PATH.exists():
        try:
            _decrypt_file(key, ENCRYPTED_DB_PATH, DB_PATH)
        except EncryptionError:
            _quarantine_orphaned_enc()

    if not _atexit_registered:
        atexit.register(_encrypt_db_on_exit, key)
        _atexit_registered = True

    _db_prepared = True


def x_prepare_db__mutmut_3(key: bytes) -> None:
    global _db_prepared, _atexit_registered
    if _db_prepared:
        return

    HEXAWYN_DIR.mkdir(exist_ok=True)

    if ENCRYPTED_DB_PATH.exists():
        try:
            _decrypt_file(key, ENCRYPTED_DB_PATH, DB_PATH)
        except EncryptionError:
            _quarantine_orphaned_enc()

    if not _atexit_registered:
        atexit.register(_encrypt_db_on_exit, key)
        _atexit_registered = True

    _db_prepared = True


def x_prepare_db__mutmut_4(key: bytes) -> None:
    global _db_prepared, _atexit_registered
    if _db_prepared:
        return

    HEXAWYN_DIR.mkdir(parents=True, )

    if ENCRYPTED_DB_PATH.exists():
        try:
            _decrypt_file(key, ENCRYPTED_DB_PATH, DB_PATH)
        except EncryptionError:
            _quarantine_orphaned_enc()

    if not _atexit_registered:
        atexit.register(_encrypt_db_on_exit, key)
        _atexit_registered = True

    _db_prepared = True


def x_prepare_db__mutmut_5(key: bytes) -> None:
    global _db_prepared, _atexit_registered
    if _db_prepared:
        return

    HEXAWYN_DIR.mkdir(parents=False, exist_ok=True)

    if ENCRYPTED_DB_PATH.exists():
        try:
            _decrypt_file(key, ENCRYPTED_DB_PATH, DB_PATH)
        except EncryptionError:
            _quarantine_orphaned_enc()

    if not _atexit_registered:
        atexit.register(_encrypt_db_on_exit, key)
        _atexit_registered = True

    _db_prepared = True


def x_prepare_db__mutmut_6(key: bytes) -> None:
    global _db_prepared, _atexit_registered
    if _db_prepared:
        return

    HEXAWYN_DIR.mkdir(parents=True, exist_ok=False)

    if ENCRYPTED_DB_PATH.exists():
        try:
            _decrypt_file(key, ENCRYPTED_DB_PATH, DB_PATH)
        except EncryptionError:
            _quarantine_orphaned_enc()

    if not _atexit_registered:
        atexit.register(_encrypt_db_on_exit, key)
        _atexit_registered = True

    _db_prepared = True


def x_prepare_db__mutmut_7(key: bytes) -> None:
    global _db_prepared, _atexit_registered
    if _db_prepared:
        return

    HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

    if ENCRYPTED_DB_PATH.exists():
        try:
            _decrypt_file(None, ENCRYPTED_DB_PATH, DB_PATH)
        except EncryptionError:
            _quarantine_orphaned_enc()

    if not _atexit_registered:
        atexit.register(_encrypt_db_on_exit, key)
        _atexit_registered = True

    _db_prepared = True


def x_prepare_db__mutmut_8(key: bytes) -> None:
    global _db_prepared, _atexit_registered
    if _db_prepared:
        return

    HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

    if ENCRYPTED_DB_PATH.exists():
        try:
            _decrypt_file(key, None, DB_PATH)
        except EncryptionError:
            _quarantine_orphaned_enc()

    if not _atexit_registered:
        atexit.register(_encrypt_db_on_exit, key)
        _atexit_registered = True

    _db_prepared = True


def x_prepare_db__mutmut_9(key: bytes) -> None:
    global _db_prepared, _atexit_registered
    if _db_prepared:
        return

    HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

    if ENCRYPTED_DB_PATH.exists():
        try:
            _decrypt_file(key, ENCRYPTED_DB_PATH, None)
        except EncryptionError:
            _quarantine_orphaned_enc()

    if not _atexit_registered:
        atexit.register(_encrypt_db_on_exit, key)
        _atexit_registered = True

    _db_prepared = True


def x_prepare_db__mutmut_10(key: bytes) -> None:
    global _db_prepared, _atexit_registered
    if _db_prepared:
        return

    HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

    if ENCRYPTED_DB_PATH.exists():
        try:
            _decrypt_file(ENCRYPTED_DB_PATH, DB_PATH)
        except EncryptionError:
            _quarantine_orphaned_enc()

    if not _atexit_registered:
        atexit.register(_encrypt_db_on_exit, key)
        _atexit_registered = True

    _db_prepared = True


def x_prepare_db__mutmut_11(key: bytes) -> None:
    global _db_prepared, _atexit_registered
    if _db_prepared:
        return

    HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

    if ENCRYPTED_DB_PATH.exists():
        try:
            _decrypt_file(key, DB_PATH)
        except EncryptionError:
            _quarantine_orphaned_enc()

    if not _atexit_registered:
        atexit.register(_encrypt_db_on_exit, key)
        _atexit_registered = True

    _db_prepared = True


def x_prepare_db__mutmut_12(key: bytes) -> None:
    global _db_prepared, _atexit_registered
    if _db_prepared:
        return

    HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

    if ENCRYPTED_DB_PATH.exists():
        try:
            _decrypt_file(key, ENCRYPTED_DB_PATH, )
        except EncryptionError:
            _quarantine_orphaned_enc()

    if not _atexit_registered:
        atexit.register(_encrypt_db_on_exit, key)
        _atexit_registered = True

    _db_prepared = True


def x_prepare_db__mutmut_13(key: bytes) -> None:
    global _db_prepared, _atexit_registered
    if _db_prepared:
        return

    HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

    if ENCRYPTED_DB_PATH.exists():
        try:
            _decrypt_file(key, ENCRYPTED_DB_PATH, DB_PATH)
        except EncryptionError:
            _quarantine_orphaned_enc()

    if _atexit_registered:
        atexit.register(_encrypt_db_on_exit, key)
        _atexit_registered = True

    _db_prepared = True


def x_prepare_db__mutmut_14(key: bytes) -> None:
    global _db_prepared, _atexit_registered
    if _db_prepared:
        return

    HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

    if ENCRYPTED_DB_PATH.exists():
        try:
            _decrypt_file(key, ENCRYPTED_DB_PATH, DB_PATH)
        except EncryptionError:
            _quarantine_orphaned_enc()

    if not _atexit_registered:
        atexit.register(None, key)
        _atexit_registered = True

    _db_prepared = True


def x_prepare_db__mutmut_15(key: bytes) -> None:
    global _db_prepared, _atexit_registered
    if _db_prepared:
        return

    HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

    if ENCRYPTED_DB_PATH.exists():
        try:
            _decrypt_file(key, ENCRYPTED_DB_PATH, DB_PATH)
        except EncryptionError:
            _quarantine_orphaned_enc()

    if not _atexit_registered:
        atexit.register(_encrypt_db_on_exit, None)
        _atexit_registered = True

    _db_prepared = True


def x_prepare_db__mutmut_16(key: bytes) -> None:
    global _db_prepared, _atexit_registered
    if _db_prepared:
        return

    HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

    if ENCRYPTED_DB_PATH.exists():
        try:
            _decrypt_file(key, ENCRYPTED_DB_PATH, DB_PATH)
        except EncryptionError:
            _quarantine_orphaned_enc()

    if not _atexit_registered:
        atexit.register(key)
        _atexit_registered = True

    _db_prepared = True


def x_prepare_db__mutmut_17(key: bytes) -> None:
    global _db_prepared, _atexit_registered
    if _db_prepared:
        return

    HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

    if ENCRYPTED_DB_PATH.exists():
        try:
            _decrypt_file(key, ENCRYPTED_DB_PATH, DB_PATH)
        except EncryptionError:
            _quarantine_orphaned_enc()

    if not _atexit_registered:
        atexit.register(_encrypt_db_on_exit, )
        _atexit_registered = True

    _db_prepared = True


def x_prepare_db__mutmut_18(key: bytes) -> None:
    global _db_prepared, _atexit_registered
    if _db_prepared:
        return

    HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

    if ENCRYPTED_DB_PATH.exists():
        try:
            _decrypt_file(key, ENCRYPTED_DB_PATH, DB_PATH)
        except EncryptionError:
            _quarantine_orphaned_enc()

    if not _atexit_registered:
        atexit.register(_encrypt_db_on_exit, key)
        _atexit_registered = None

    _db_prepared = True


def x_prepare_db__mutmut_19(key: bytes) -> None:
    global _db_prepared, _atexit_registered
    if _db_prepared:
        return

    HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

    if ENCRYPTED_DB_PATH.exists():
        try:
            _decrypt_file(key, ENCRYPTED_DB_PATH, DB_PATH)
        except EncryptionError:
            _quarantine_orphaned_enc()

    if not _atexit_registered:
        atexit.register(_encrypt_db_on_exit, key)
        _atexit_registered = False

    _db_prepared = True


def x_prepare_db__mutmut_20(key: bytes) -> None:
    global _db_prepared, _atexit_registered
    if _db_prepared:
        return

    HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

    if ENCRYPTED_DB_PATH.exists():
        try:
            _decrypt_file(key, ENCRYPTED_DB_PATH, DB_PATH)
        except EncryptionError:
            _quarantine_orphaned_enc()

    if not _atexit_registered:
        atexit.register(_encrypt_db_on_exit, key)
        _atexit_registered = True

    _db_prepared = None


def x_prepare_db__mutmut_21(key: bytes) -> None:
    global _db_prepared, _atexit_registered
    if _db_prepared:
        return

    HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

    if ENCRYPTED_DB_PATH.exists():
        try:
            _decrypt_file(key, ENCRYPTED_DB_PATH, DB_PATH)
        except EncryptionError:
            _quarantine_orphaned_enc()

    if not _atexit_registered:
        atexit.register(_encrypt_db_on_exit, key)
        _atexit_registered = True

    _db_prepared = False

mutants_x_prepare_db__mutmut['_mutmut_orig'] = x_prepare_db__mutmut_orig # type: ignore # mutmut generated
mutants_x_prepare_db__mutmut['x_prepare_db__mutmut_1'] = x_prepare_db__mutmut_1 # type: ignore # mutmut generated
mutants_x_prepare_db__mutmut['x_prepare_db__mutmut_2'] = x_prepare_db__mutmut_2 # type: ignore # mutmut generated
mutants_x_prepare_db__mutmut['x_prepare_db__mutmut_3'] = x_prepare_db__mutmut_3 # type: ignore # mutmut generated
mutants_x_prepare_db__mutmut['x_prepare_db__mutmut_4'] = x_prepare_db__mutmut_4 # type: ignore # mutmut generated
mutants_x_prepare_db__mutmut['x_prepare_db__mutmut_5'] = x_prepare_db__mutmut_5 # type: ignore # mutmut generated
mutants_x_prepare_db__mutmut['x_prepare_db__mutmut_6'] = x_prepare_db__mutmut_6 # type: ignore # mutmut generated
mutants_x_prepare_db__mutmut['x_prepare_db__mutmut_7'] = x_prepare_db__mutmut_7 # type: ignore # mutmut generated
mutants_x_prepare_db__mutmut['x_prepare_db__mutmut_8'] = x_prepare_db__mutmut_8 # type: ignore # mutmut generated
mutants_x_prepare_db__mutmut['x_prepare_db__mutmut_9'] = x_prepare_db__mutmut_9 # type: ignore # mutmut generated
mutants_x_prepare_db__mutmut['x_prepare_db__mutmut_10'] = x_prepare_db__mutmut_10 # type: ignore # mutmut generated
mutants_x_prepare_db__mutmut['x_prepare_db__mutmut_11'] = x_prepare_db__mutmut_11 # type: ignore # mutmut generated
mutants_x_prepare_db__mutmut['x_prepare_db__mutmut_12'] = x_prepare_db__mutmut_12 # type: ignore # mutmut generated
mutants_x_prepare_db__mutmut['x_prepare_db__mutmut_13'] = x_prepare_db__mutmut_13 # type: ignore # mutmut generated
mutants_x_prepare_db__mutmut['x_prepare_db__mutmut_14'] = x_prepare_db__mutmut_14 # type: ignore # mutmut generated
mutants_x_prepare_db__mutmut['x_prepare_db__mutmut_15'] = x_prepare_db__mutmut_15 # type: ignore # mutmut generated
mutants_x_prepare_db__mutmut['x_prepare_db__mutmut_16'] = x_prepare_db__mutmut_16 # type: ignore # mutmut generated
mutants_x_prepare_db__mutmut['x_prepare_db__mutmut_17'] = x_prepare_db__mutmut_17 # type: ignore # mutmut generated
mutants_x_prepare_db__mutmut['x_prepare_db__mutmut_18'] = x_prepare_db__mutmut_18 # type: ignore # mutmut generated
mutants_x_prepare_db__mutmut['x_prepare_db__mutmut_19'] = x_prepare_db__mutmut_19 # type: ignore # mutmut generated
mutants_x_prepare_db__mutmut['x_prepare_db__mutmut_20'] = x_prepare_db__mutmut_20 # type: ignore # mutmut generated
mutants_x_prepare_db__mutmut['x_prepare_db__mutmut_21'] = x_prepare_db__mutmut_21 # type: ignore # mutmut generated
