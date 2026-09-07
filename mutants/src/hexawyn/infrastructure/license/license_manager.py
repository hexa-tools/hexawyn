import os
import time
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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x__read_license_key__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__read_license_key__mutmut)
def _read_license_key() -> str | None:
    env_key = os.environ.get("HEXAWYN_LICENSE_KEY")
    if env_key:
        return env_key.strip()
    if LICENSE_KEY_PATH.exists():
        return LICENSE_KEY_PATH.read_text(encoding="utf-8").strip()
    return None


def x__read_license_key__mutmut_orig() -> str | None:
    env_key = os.environ.get("HEXAWYN_LICENSE_KEY")
    if env_key:
        return env_key.strip()
    if LICENSE_KEY_PATH.exists():
        return LICENSE_KEY_PATH.read_text(encoding="utf-8").strip()
    return None


def x__read_license_key__mutmut_1() -> str | None:
    env_key = None
    if env_key:
        return env_key.strip()
    if LICENSE_KEY_PATH.exists():
        return LICENSE_KEY_PATH.read_text(encoding="utf-8").strip()
    return None


def x__read_license_key__mutmut_2() -> str | None:
    env_key = os.environ.get(None)
    if env_key:
        return env_key.strip()
    if LICENSE_KEY_PATH.exists():
        return LICENSE_KEY_PATH.read_text(encoding="utf-8").strip()
    return None


def x__read_license_key__mutmut_3() -> str | None:
    env_key = os.environ.get("XXHEXAWYN_LICENSE_KEYXX")
    if env_key:
        return env_key.strip()
    if LICENSE_KEY_PATH.exists():
        return LICENSE_KEY_PATH.read_text(encoding="utf-8").strip()
    return None


def x__read_license_key__mutmut_4() -> str | None:
    env_key = os.environ.get("hexawyn_license_key")
    if env_key:
        return env_key.strip()
    if LICENSE_KEY_PATH.exists():
        return LICENSE_KEY_PATH.read_text(encoding="utf-8").strip()
    return None


def x__read_license_key__mutmut_5() -> str | None:
    env_key = os.environ.get("HEXAWYN_LICENSE_KEY")
    if env_key:
        return env_key.strip()
    if LICENSE_KEY_PATH.exists():
        return LICENSE_KEY_PATH.read_text(encoding=None).strip()
    return None


def x__read_license_key__mutmut_6() -> str | None:
    env_key = os.environ.get("HEXAWYN_LICENSE_KEY")
    if env_key:
        return env_key.strip()
    if LICENSE_KEY_PATH.exists():
        return LICENSE_KEY_PATH.read_text(encoding="XXutf-8XX").strip()
    return None


def x__read_license_key__mutmut_7() -> str | None:
    env_key = os.environ.get("HEXAWYN_LICENSE_KEY")
    if env_key:
        return env_key.strip()
    if LICENSE_KEY_PATH.exists():
        return LICENSE_KEY_PATH.read_text(encoding="UTF-8").strip()
    return None

mutants_x__read_license_key__mutmut['_mutmut_orig'] = x__read_license_key__mutmut_orig # type: ignore # mutmut generated
mutants_x__read_license_key__mutmut['x__read_license_key__mutmut_1'] = x__read_license_key__mutmut_1 # type: ignore # mutmut generated
mutants_x__read_license_key__mutmut['x__read_license_key__mutmut_2'] = x__read_license_key__mutmut_2 # type: ignore # mutmut generated
mutants_x__read_license_key__mutmut['x__read_license_key__mutmut_3'] = x__read_license_key__mutmut_3 # type: ignore # mutmut generated
mutants_x__read_license_key__mutmut['x__read_license_key__mutmut_4'] = x__read_license_key__mutmut_4 # type: ignore # mutmut generated
mutants_x__read_license_key__mutmut['x__read_license_key__mutmut_5'] = x__read_license_key__mutmut_5 # type: ignore # mutmut generated
mutants_x__read_license_key__mutmut['x__read_license_key__mutmut_6'] = x__read_license_key__mutmut_6 # type: ignore # mutmut generated
mutants_x__read_license_key__mutmut['x__read_license_key__mutmut_7'] = x__read_license_key__mutmut_7 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_verify_license__mutmut)
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_orig() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_1() -> LicenseClaims:
    """
    Verify the license JWT at CLI startup.
    Returns LicenseClaims.free() if no license is present or token is invalid.
    Raises LicenseExpiredError only if token is valid but expired.
    """
    token = None
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_2() -> LicenseClaims:
    """
    Verify the license JWT at CLI startup.
    Returns LicenseClaims.free() if no license is present or token is invalid.
    Raises LicenseExpiredError only if token is valid but expired.
    """
    token = _read_license_key()
    if token:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_3() -> LicenseClaims:
    """
    Verify the license JWT at CLI startup.
    Returns LicenseClaims.free() if no license is present or token is invalid.
    Raises LicenseExpiredError only if token is valid but expired.
    """
    token = _read_license_key()
    if not token:
        return LicenseClaims.free()

    try:
        payload = None
    except jwt.ExpiredSignatureError:
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")
    except (jwt.InvalidTokenError, InvalidKeyError):
        try:
            payload = jwt.decode(token, options={"verify_signature": False})
        except jwt.InvalidTokenError:
            return LicenseClaims.free()

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_4() -> LicenseClaims:
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
            None,
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_5() -> LicenseClaims:
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
            None,
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_6() -> LicenseClaims:
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
            algorithms=None,
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_7() -> LicenseClaims:
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
            options=None,
            leeway=TOLERANCE_SECONDS,
        )
    except jwt.ExpiredSignatureError:
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")
    except (jwt.InvalidTokenError, InvalidKeyError):
        try:
            payload = jwt.decode(token, options={"verify_signature": False})
        except jwt.InvalidTokenError:
            return LicenseClaims.free()

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_8() -> LicenseClaims:
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
            leeway=None,
        )
    except jwt.ExpiredSignatureError:
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")
    except (jwt.InvalidTokenError, InvalidKeyError):
        try:
            payload = jwt.decode(token, options={"verify_signature": False})
        except jwt.InvalidTokenError:
            return LicenseClaims.free()

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_9() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_10() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_11() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_12() -> LicenseClaims:
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
            leeway=TOLERANCE_SECONDS,
        )
    except jwt.ExpiredSignatureError:
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")
    except (jwt.InvalidTokenError, InvalidKeyError):
        try:
            payload = jwt.decode(token, options={"verify_signature": False})
        except jwt.InvalidTokenError:
            return LicenseClaims.free()

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_13() -> LicenseClaims:
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
            )
    except jwt.ExpiredSignatureError:
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")
    except (jwt.InvalidTokenError, InvalidKeyError):
        try:
            payload = jwt.decode(token, options={"verify_signature": False})
        except jwt.InvalidTokenError:
            return LicenseClaims.free()

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_14() -> LicenseClaims:
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
            algorithms=["XXRS256XX"],
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_15() -> LicenseClaims:
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
            algorithms=["rs256"],
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_16() -> LicenseClaims:
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
            options={"XXrequireXX": ["exp", "sub", "plan"]},
            leeway=TOLERANCE_SECONDS,
        )
    except jwt.ExpiredSignatureError:
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")
    except (jwt.InvalidTokenError, InvalidKeyError):
        try:
            payload = jwt.decode(token, options={"verify_signature": False})
        except jwt.InvalidTokenError:
            return LicenseClaims.free()

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_17() -> LicenseClaims:
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
            options={"REQUIRE": ["exp", "sub", "plan"]},
            leeway=TOLERANCE_SECONDS,
        )
    except jwt.ExpiredSignatureError:
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")
    except (jwt.InvalidTokenError, InvalidKeyError):
        try:
            payload = jwt.decode(token, options={"verify_signature": False})
        except jwt.InvalidTokenError:
            return LicenseClaims.free()

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_18() -> LicenseClaims:
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
            options={"require": ["XXexpXX", "sub", "plan"]},
            leeway=TOLERANCE_SECONDS,
        )
    except jwt.ExpiredSignatureError:
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")
    except (jwt.InvalidTokenError, InvalidKeyError):
        try:
            payload = jwt.decode(token, options={"verify_signature": False})
        except jwt.InvalidTokenError:
            return LicenseClaims.free()

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_19() -> LicenseClaims:
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
            options={"require": ["EXP", "sub", "plan"]},
            leeway=TOLERANCE_SECONDS,
        )
    except jwt.ExpiredSignatureError:
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")
    except (jwt.InvalidTokenError, InvalidKeyError):
        try:
            payload = jwt.decode(token, options={"verify_signature": False})
        except jwt.InvalidTokenError:
            return LicenseClaims.free()

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_20() -> LicenseClaims:
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
            options={"require": ["exp", "XXsubXX", "plan"]},
            leeway=TOLERANCE_SECONDS,
        )
    except jwt.ExpiredSignatureError:
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")
    except (jwt.InvalidTokenError, InvalidKeyError):
        try:
            payload = jwt.decode(token, options={"verify_signature": False})
        except jwt.InvalidTokenError:
            return LicenseClaims.free()

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_21() -> LicenseClaims:
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
            options={"require": ["exp", "SUB", "plan"]},
            leeway=TOLERANCE_SECONDS,
        )
    except jwt.ExpiredSignatureError:
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")
    except (jwt.InvalidTokenError, InvalidKeyError):
        try:
            payload = jwt.decode(token, options={"verify_signature": False})
        except jwt.InvalidTokenError:
            return LicenseClaims.free()

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_22() -> LicenseClaims:
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
            options={"require": ["exp", "sub", "XXplanXX"]},
            leeway=TOLERANCE_SECONDS,
        )
    except jwt.ExpiredSignatureError:
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")
    except (jwt.InvalidTokenError, InvalidKeyError):
        try:
            payload = jwt.decode(token, options={"verify_signature": False})
        except jwt.InvalidTokenError:
            return LicenseClaims.free()

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_23() -> LicenseClaims:
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
            options={"require": ["exp", "sub", "PLAN"]},
            leeway=TOLERANCE_SECONDS,
        )
    except jwt.ExpiredSignatureError:
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")
    except (jwt.InvalidTokenError, InvalidKeyError):
        try:
            payload = jwt.decode(token, options={"verify_signature": False})
        except jwt.InvalidTokenError:
            return LicenseClaims.free()

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_24() -> LicenseClaims:
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
        raise LicenseExpiredError(None)
    except (jwt.InvalidTokenError, InvalidKeyError):
        try:
            payload = jwt.decode(token, options={"verify_signature": False})
        except jwt.InvalidTokenError:
            return LicenseClaims.free()

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_25() -> LicenseClaims:
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
        raise LicenseExpiredError("XXYour license has expired. Renew at https://hexawyn.com/pricingXX")
    except (jwt.InvalidTokenError, InvalidKeyError):
        try:
            payload = jwt.decode(token, options={"verify_signature": False})
        except jwt.InvalidTokenError:
            return LicenseClaims.free()

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_26() -> LicenseClaims:
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
        raise LicenseExpiredError("your license has expired. renew at https://hexawyn.com/pricing")
    except (jwt.InvalidTokenError, InvalidKeyError):
        try:
            payload = jwt.decode(token, options={"verify_signature": False})
        except jwt.InvalidTokenError:
            return LicenseClaims.free()

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_27() -> LicenseClaims:
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
        raise LicenseExpiredError("YOUR LICENSE HAS EXPIRED. RENEW AT HTTPS://HEXAWYN.COM/PRICING")
    except (jwt.InvalidTokenError, InvalidKeyError):
        try:
            payload = jwt.decode(token, options={"verify_signature": False})
        except jwt.InvalidTokenError:
            return LicenseClaims.free()

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_28() -> LicenseClaims:
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
            payload = None
        except jwt.InvalidTokenError:
            return LicenseClaims.free()

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_29() -> LicenseClaims:
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
            payload = jwt.decode(None, options={"verify_signature": False})
        except jwt.InvalidTokenError:
            return LicenseClaims.free()

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_30() -> LicenseClaims:
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
            payload = jwt.decode(token, options=None)
        except jwt.InvalidTokenError:
            return LicenseClaims.free()

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_31() -> LicenseClaims:
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
            payload = jwt.decode(options={"verify_signature": False})
        except jwt.InvalidTokenError:
            return LicenseClaims.free()

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_32() -> LicenseClaims:
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
            payload = jwt.decode(token, )
        except jwt.InvalidTokenError:
            return LicenseClaims.free()

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_33() -> LicenseClaims:
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
            payload = jwt.decode(token, options={"XXverify_signatureXX": False})
        except jwt.InvalidTokenError:
            return LicenseClaims.free()

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_34() -> LicenseClaims:
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
            payload = jwt.decode(token, options={"VERIFY_SIGNATURE": False})
        except jwt.InvalidTokenError:
            return LicenseClaims.free()

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_35() -> LicenseClaims:
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
            payload = jwt.decode(token, options={"verify_signature": True})
        except jwt.InvalidTokenError:
            return LicenseClaims.free()

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_36() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(None) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_37() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["XXexpXX"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_38() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["EXP"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_39() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) < int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_40() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(None):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_41() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError(None)

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


def x_verify_license__mutmut_42() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("XXYour license has expired. Renew at https://hexawyn.com/pricingXX")

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


def x_verify_license__mutmut_43() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("your license has expired. renew at https://hexawyn.com/pricing")

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


def x_verify_license__mutmut_44() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("YOUR LICENSE HAS EXPIRED. RENEW AT HTTPS://HEXAWYN.COM/PRICING")

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


def x_verify_license__mutmut_45() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=None,
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_46() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=None,
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_47() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=None,
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_48() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=None,
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_49() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=None,
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_50() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=None,
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_51() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=None,
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_52() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=None,
        iat=payload["iat"],
    )


def x_verify_license__mutmut_53() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=None,
    )


def x_verify_license__mutmut_54() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_55() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_56() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_57() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_58() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_59() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_60() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_61() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        iat=payload["iat"],
    )


def x_verify_license__mutmut_62() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        )


def x_verify_license__mutmut_63() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["XXsubXX"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_64() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["SUB"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_65() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["XXplanXX"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_66() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["PLAN"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_67() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get(None, 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_68() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", None),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_69() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get(1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_70() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", ),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_71() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("XXclusters_maxXX", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_72() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("CLUSTERS_MAX", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_73() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 2),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_74() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get(None, 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_75() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", None),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_76() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get(1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_77() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", ),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_78() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("XXusers_maxXX", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_79() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("USERS_MAX", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_80() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 2),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_81() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get(None, 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_82() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", None),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_83() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get(50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_84() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", ),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_85() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("XXinvestigations_monthlyXX", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_86() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("INVESTIGATIONS_MONTHLY", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_87() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 51),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_88() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get(None, 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_89() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", None),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_90() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get(7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_91() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", ),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_92() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("XXhistory_daysXX", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_93() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("HISTORY_DAYS", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_94() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 8),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_95() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get(None, ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_96() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", None),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_97() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get(["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_98() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_99() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("XXprovidersXX", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_100() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("PROVIDERS", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_101() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["XXvanillaXX"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_102() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["VANILLA"]),
        exp=payload["exp"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_103() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["XXexpXX"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_104() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["EXP"],
        iat=payload["iat"],
    )


def x_verify_license__mutmut_105() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["XXiatXX"],
    )


def x_verify_license__mutmut_106() -> LicenseClaims:
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

    # The fallback decode (used when the public key is a placeholder) does not
    # raise on an expired ``exp`` — enforce it here so an expired token drops
    # back to the free tier instead of keeping a paid quota.
    if int(payload["exp"]) <= int(time.time()):
        raise LicenseExpiredError("Your license has expired. Renew at https://hexawyn.com/pricing")

    return LicenseClaims(
        sub=payload["sub"],
        plan=payload["plan"],
        clusters_max=payload.get("clusters_max", 1),
        users_max=payload.get("users_max", 1),
        investigations_monthly=payload.get("investigations_monthly", 50),
        history_days=payload.get("history_days", 7),
        providers=payload.get("providers", ["vanilla"]),
        exp=payload["exp"],
        iat=payload["IAT"],
    )

mutants_x_verify_license__mutmut['_mutmut_orig'] = x_verify_license__mutmut_orig # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_1'] = x_verify_license__mutmut_1 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_2'] = x_verify_license__mutmut_2 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_3'] = x_verify_license__mutmut_3 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_4'] = x_verify_license__mutmut_4 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_5'] = x_verify_license__mutmut_5 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_6'] = x_verify_license__mutmut_6 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_7'] = x_verify_license__mutmut_7 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_8'] = x_verify_license__mutmut_8 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_9'] = x_verify_license__mutmut_9 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_10'] = x_verify_license__mutmut_10 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_11'] = x_verify_license__mutmut_11 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_12'] = x_verify_license__mutmut_12 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_13'] = x_verify_license__mutmut_13 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_14'] = x_verify_license__mutmut_14 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_15'] = x_verify_license__mutmut_15 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_16'] = x_verify_license__mutmut_16 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_17'] = x_verify_license__mutmut_17 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_18'] = x_verify_license__mutmut_18 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_19'] = x_verify_license__mutmut_19 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_20'] = x_verify_license__mutmut_20 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_21'] = x_verify_license__mutmut_21 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_22'] = x_verify_license__mutmut_22 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_23'] = x_verify_license__mutmut_23 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_24'] = x_verify_license__mutmut_24 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_25'] = x_verify_license__mutmut_25 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_26'] = x_verify_license__mutmut_26 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_27'] = x_verify_license__mutmut_27 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_28'] = x_verify_license__mutmut_28 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_29'] = x_verify_license__mutmut_29 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_30'] = x_verify_license__mutmut_30 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_31'] = x_verify_license__mutmut_31 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_32'] = x_verify_license__mutmut_32 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_33'] = x_verify_license__mutmut_33 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_34'] = x_verify_license__mutmut_34 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_35'] = x_verify_license__mutmut_35 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_36'] = x_verify_license__mutmut_36 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_37'] = x_verify_license__mutmut_37 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_38'] = x_verify_license__mutmut_38 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_39'] = x_verify_license__mutmut_39 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_40'] = x_verify_license__mutmut_40 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_41'] = x_verify_license__mutmut_41 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_42'] = x_verify_license__mutmut_42 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_43'] = x_verify_license__mutmut_43 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_44'] = x_verify_license__mutmut_44 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_45'] = x_verify_license__mutmut_45 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_46'] = x_verify_license__mutmut_46 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_47'] = x_verify_license__mutmut_47 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_48'] = x_verify_license__mutmut_48 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_49'] = x_verify_license__mutmut_49 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_50'] = x_verify_license__mutmut_50 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_51'] = x_verify_license__mutmut_51 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_52'] = x_verify_license__mutmut_52 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_53'] = x_verify_license__mutmut_53 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_54'] = x_verify_license__mutmut_54 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_55'] = x_verify_license__mutmut_55 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_56'] = x_verify_license__mutmut_56 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_57'] = x_verify_license__mutmut_57 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_58'] = x_verify_license__mutmut_58 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_59'] = x_verify_license__mutmut_59 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_60'] = x_verify_license__mutmut_60 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_61'] = x_verify_license__mutmut_61 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_62'] = x_verify_license__mutmut_62 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_63'] = x_verify_license__mutmut_63 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_64'] = x_verify_license__mutmut_64 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_65'] = x_verify_license__mutmut_65 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_66'] = x_verify_license__mutmut_66 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_67'] = x_verify_license__mutmut_67 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_68'] = x_verify_license__mutmut_68 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_69'] = x_verify_license__mutmut_69 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_70'] = x_verify_license__mutmut_70 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_71'] = x_verify_license__mutmut_71 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_72'] = x_verify_license__mutmut_72 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_73'] = x_verify_license__mutmut_73 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_74'] = x_verify_license__mutmut_74 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_75'] = x_verify_license__mutmut_75 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_76'] = x_verify_license__mutmut_76 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_77'] = x_verify_license__mutmut_77 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_78'] = x_verify_license__mutmut_78 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_79'] = x_verify_license__mutmut_79 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_80'] = x_verify_license__mutmut_80 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_81'] = x_verify_license__mutmut_81 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_82'] = x_verify_license__mutmut_82 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_83'] = x_verify_license__mutmut_83 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_84'] = x_verify_license__mutmut_84 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_85'] = x_verify_license__mutmut_85 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_86'] = x_verify_license__mutmut_86 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_87'] = x_verify_license__mutmut_87 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_88'] = x_verify_license__mutmut_88 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_89'] = x_verify_license__mutmut_89 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_90'] = x_verify_license__mutmut_90 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_91'] = x_verify_license__mutmut_91 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_92'] = x_verify_license__mutmut_92 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_93'] = x_verify_license__mutmut_93 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_94'] = x_verify_license__mutmut_94 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_95'] = x_verify_license__mutmut_95 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_96'] = x_verify_license__mutmut_96 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_97'] = x_verify_license__mutmut_97 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_98'] = x_verify_license__mutmut_98 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_99'] = x_verify_license__mutmut_99 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_100'] = x_verify_license__mutmut_100 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_101'] = x_verify_license__mutmut_101 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_102'] = x_verify_license__mutmut_102 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_103'] = x_verify_license__mutmut_103 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_104'] = x_verify_license__mutmut_104 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_105'] = x_verify_license__mutmut_105 # type: ignore # mutmut generated
mutants_x_verify_license__mutmut['x_verify_license__mutmut_106'] = x_verify_license__mutmut_106 # type: ignore # mutmut generated
mutants_x_has_provider_access__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_has_provider_access__mutmut)
def has_provider_access(claims: LicenseClaims, provider: str) -> bool:
    """Check whether the license grants access to a specific provider."""
    return "*" in claims.providers or provider in claims.providers


def x_has_provider_access__mutmut_orig(claims: LicenseClaims, provider: str) -> bool:
    """Check whether the license grants access to a specific provider."""
    return "*" in claims.providers or provider in claims.providers


def x_has_provider_access__mutmut_1(claims: LicenseClaims, provider: str) -> bool:
    """Check whether the license grants access to a specific provider."""
    return "*" in claims.providers and provider in claims.providers


def x_has_provider_access__mutmut_2(claims: LicenseClaims, provider: str) -> bool:
    """Check whether the license grants access to a specific provider."""
    return "XX*XX" in claims.providers or provider in claims.providers


def x_has_provider_access__mutmut_3(claims: LicenseClaims, provider: str) -> bool:
    """Check whether the license grants access to a specific provider."""
    return "*" not in claims.providers or provider in claims.providers


def x_has_provider_access__mutmut_4(claims: LicenseClaims, provider: str) -> bool:
    """Check whether the license grants access to a specific provider."""
    return "*" in claims.providers or provider not in claims.providers

mutants_x_has_provider_access__mutmut['_mutmut_orig'] = x_has_provider_access__mutmut_orig # type: ignore # mutmut generated
mutants_x_has_provider_access__mutmut['x_has_provider_access__mutmut_1'] = x_has_provider_access__mutmut_1 # type: ignore # mutmut generated
mutants_x_has_provider_access__mutmut['x_has_provider_access__mutmut_2'] = x_has_provider_access__mutmut_2 # type: ignore # mutmut generated
mutants_x_has_provider_access__mutmut['x_has_provider_access__mutmut_3'] = x_has_provider_access__mutmut_3 # type: ignore # mutmut generated
mutants_x_has_provider_access__mutmut['x_has_provider_access__mutmut_4'] = x_has_provider_access__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_license_tier__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_license_tier__mutmut)
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


def x_get_license_tier__mutmut_orig() -> LicenseTier:
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


def x_get_license_tier__mutmut_1() -> LicenseTier:
    """Return the current LicenseTier from the license or STARTER fallback."""
    try:
        claims = None
    except LicenseExpiredError:
        return LicenseTier.STARTER

    tier_map: dict[str, LicenseTier] = {
        "starter": LicenseTier.STARTER,
        "team": LicenseTier.TEAM,
        "scale-up": LicenseTier.SCALE_UP,
    }
    return tier_map.get(claims.plan, LicenseTier.STARTER)


def x_get_license_tier__mutmut_2() -> LicenseTier:
    """Return the current LicenseTier from the license or STARTER fallback."""
    try:
        claims = verify_license()
    except LicenseExpiredError:
        return LicenseTier.STARTER

    tier_map: dict[str, LicenseTier] = None
    return tier_map.get(claims.plan, LicenseTier.STARTER)


def x_get_license_tier__mutmut_3() -> LicenseTier:
    """Return the current LicenseTier from the license or STARTER fallback."""
    try:
        claims = verify_license()
    except LicenseExpiredError:
        return LicenseTier.STARTER

    tier_map: dict[str, LicenseTier] = {
        "XXstarterXX": LicenseTier.STARTER,
        "team": LicenseTier.TEAM,
        "scale-up": LicenseTier.SCALE_UP,
    }
    return tier_map.get(claims.plan, LicenseTier.STARTER)


def x_get_license_tier__mutmut_4() -> LicenseTier:
    """Return the current LicenseTier from the license or STARTER fallback."""
    try:
        claims = verify_license()
    except LicenseExpiredError:
        return LicenseTier.STARTER

    tier_map: dict[str, LicenseTier] = {
        "STARTER": LicenseTier.STARTER,
        "team": LicenseTier.TEAM,
        "scale-up": LicenseTier.SCALE_UP,
    }
    return tier_map.get(claims.plan, LicenseTier.STARTER)


def x_get_license_tier__mutmut_5() -> LicenseTier:
    """Return the current LicenseTier from the license or STARTER fallback."""
    try:
        claims = verify_license()
    except LicenseExpiredError:
        return LicenseTier.STARTER

    tier_map: dict[str, LicenseTier] = {
        "starter": LicenseTier.STARTER,
        "XXteamXX": LicenseTier.TEAM,
        "scale-up": LicenseTier.SCALE_UP,
    }
    return tier_map.get(claims.plan, LicenseTier.STARTER)


def x_get_license_tier__mutmut_6() -> LicenseTier:
    """Return the current LicenseTier from the license or STARTER fallback."""
    try:
        claims = verify_license()
    except LicenseExpiredError:
        return LicenseTier.STARTER

    tier_map: dict[str, LicenseTier] = {
        "starter": LicenseTier.STARTER,
        "TEAM": LicenseTier.TEAM,
        "scale-up": LicenseTier.SCALE_UP,
    }
    return tier_map.get(claims.plan, LicenseTier.STARTER)


def x_get_license_tier__mutmut_7() -> LicenseTier:
    """Return the current LicenseTier from the license or STARTER fallback."""
    try:
        claims = verify_license()
    except LicenseExpiredError:
        return LicenseTier.STARTER

    tier_map: dict[str, LicenseTier] = {
        "starter": LicenseTier.STARTER,
        "team": LicenseTier.TEAM,
        "XXscale-upXX": LicenseTier.SCALE_UP,
    }
    return tier_map.get(claims.plan, LicenseTier.STARTER)


def x_get_license_tier__mutmut_8() -> LicenseTier:
    """Return the current LicenseTier from the license or STARTER fallback."""
    try:
        claims = verify_license()
    except LicenseExpiredError:
        return LicenseTier.STARTER

    tier_map: dict[str, LicenseTier] = {
        "starter": LicenseTier.STARTER,
        "team": LicenseTier.TEAM,
        "SCALE-UP": LicenseTier.SCALE_UP,
    }
    return tier_map.get(claims.plan, LicenseTier.STARTER)


def x_get_license_tier__mutmut_9() -> LicenseTier:
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
    return tier_map.get(None, LicenseTier.STARTER)


def x_get_license_tier__mutmut_10() -> LicenseTier:
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
    return tier_map.get(claims.plan, None)


def x_get_license_tier__mutmut_11() -> LicenseTier:
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
    return tier_map.get(LicenseTier.STARTER)


def x_get_license_tier__mutmut_12() -> LicenseTier:
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
    return tier_map.get(claims.plan, )

mutants_x_get_license_tier__mutmut['_mutmut_orig'] = x_get_license_tier__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_license_tier__mutmut['x_get_license_tier__mutmut_1'] = x_get_license_tier__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_license_tier__mutmut['x_get_license_tier__mutmut_2'] = x_get_license_tier__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_license_tier__mutmut['x_get_license_tier__mutmut_3'] = x_get_license_tier__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_license_tier__mutmut['x_get_license_tier__mutmut_4'] = x_get_license_tier__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_license_tier__mutmut['x_get_license_tier__mutmut_5'] = x_get_license_tier__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_license_tier__mutmut['x_get_license_tier__mutmut_6'] = x_get_license_tier__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_license_tier__mutmut['x_get_license_tier__mutmut_7'] = x_get_license_tier__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_license_tier__mutmut['x_get_license_tier__mutmut_8'] = x_get_license_tier__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_license_tier__mutmut['x_get_license_tier__mutmut_9'] = x_get_license_tier__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_license_tier__mutmut['x_get_license_tier__mutmut_10'] = x_get_license_tier__mutmut_10 # type: ignore # mutmut generated
mutants_x_get_license_tier__mutmut['x_get_license_tier__mutmut_11'] = x_get_license_tier__mutmut_11 # type: ignore # mutmut generated
mutants_x_get_license_tier__mutmut['x_get_license_tier__mutmut_12'] = x_get_license_tier__mutmut_12 # type: ignore # mutmut generated
mutants_x_activate_license__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_activate_license__mutmut)
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


def x_activate_license__mutmut_orig(key: str) -> LicenseClaims:
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


def x_activate_license__mutmut_1(key: str) -> LicenseClaims:
    """
    Validate and persist a license JWT.
    Raises LicenseInvalidError if the token cannot be verified.
    """
    key = None
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


def x_activate_license__mutmut_2(key: str) -> LicenseClaims:
    """
    Validate and persist a license JWT.
    Raises LicenseInvalidError if the token cannot be verified.
    """
    key = key.strip()
    try:
        jwt.decode(None, PUBLIC_KEY_PEM, algorithms=["RS256"], leeway=TOLERANCE_SECONDS)
    except jwt.ExpiredSignatureError:
        raise LicenseInvalidError("This license has already expired.")
    except (jwt.InvalidTokenError, InvalidKeyError):
        raise LicenseInvalidError("Invalid license key. Please check and try again.")

    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
    LICENSE_KEY_PATH.write_text(key, encoding="utf-8")
    LICENSE_KEY_PATH.chmod(0o600)

    return verify_license()


def x_activate_license__mutmut_3(key: str) -> LicenseClaims:
    """
    Validate and persist a license JWT.
    Raises LicenseInvalidError if the token cannot be verified.
    """
    key = key.strip()
    try:
        jwt.decode(key, None, algorithms=["RS256"], leeway=TOLERANCE_SECONDS)
    except jwt.ExpiredSignatureError:
        raise LicenseInvalidError("This license has already expired.")
    except (jwt.InvalidTokenError, InvalidKeyError):
        raise LicenseInvalidError("Invalid license key. Please check and try again.")

    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
    LICENSE_KEY_PATH.write_text(key, encoding="utf-8")
    LICENSE_KEY_PATH.chmod(0o600)

    return verify_license()


def x_activate_license__mutmut_4(key: str) -> LicenseClaims:
    """
    Validate and persist a license JWT.
    Raises LicenseInvalidError if the token cannot be verified.
    """
    key = key.strip()
    try:
        jwt.decode(key, PUBLIC_KEY_PEM, algorithms=None, leeway=TOLERANCE_SECONDS)
    except jwt.ExpiredSignatureError:
        raise LicenseInvalidError("This license has already expired.")
    except (jwt.InvalidTokenError, InvalidKeyError):
        raise LicenseInvalidError("Invalid license key. Please check and try again.")

    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
    LICENSE_KEY_PATH.write_text(key, encoding="utf-8")
    LICENSE_KEY_PATH.chmod(0o600)

    return verify_license()


def x_activate_license__mutmut_5(key: str) -> LicenseClaims:
    """
    Validate and persist a license JWT.
    Raises LicenseInvalidError if the token cannot be verified.
    """
    key = key.strip()
    try:
        jwt.decode(key, PUBLIC_KEY_PEM, algorithms=["RS256"], leeway=None)
    except jwt.ExpiredSignatureError:
        raise LicenseInvalidError("This license has already expired.")
    except (jwt.InvalidTokenError, InvalidKeyError):
        raise LicenseInvalidError("Invalid license key. Please check and try again.")

    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
    LICENSE_KEY_PATH.write_text(key, encoding="utf-8")
    LICENSE_KEY_PATH.chmod(0o600)

    return verify_license()


def x_activate_license__mutmut_6(key: str) -> LicenseClaims:
    """
    Validate and persist a license JWT.
    Raises LicenseInvalidError if the token cannot be verified.
    """
    key = key.strip()
    try:
        jwt.decode(PUBLIC_KEY_PEM, algorithms=["RS256"], leeway=TOLERANCE_SECONDS)
    except jwt.ExpiredSignatureError:
        raise LicenseInvalidError("This license has already expired.")
    except (jwt.InvalidTokenError, InvalidKeyError):
        raise LicenseInvalidError("Invalid license key. Please check and try again.")

    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
    LICENSE_KEY_PATH.write_text(key, encoding="utf-8")
    LICENSE_KEY_PATH.chmod(0o600)

    return verify_license()


def x_activate_license__mutmut_7(key: str) -> LicenseClaims:
    """
    Validate and persist a license JWT.
    Raises LicenseInvalidError if the token cannot be verified.
    """
    key = key.strip()
    try:
        jwt.decode(key, algorithms=["RS256"], leeway=TOLERANCE_SECONDS)
    except jwt.ExpiredSignatureError:
        raise LicenseInvalidError("This license has already expired.")
    except (jwt.InvalidTokenError, InvalidKeyError):
        raise LicenseInvalidError("Invalid license key. Please check and try again.")

    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
    LICENSE_KEY_PATH.write_text(key, encoding="utf-8")
    LICENSE_KEY_PATH.chmod(0o600)

    return verify_license()


def x_activate_license__mutmut_8(key: str) -> LicenseClaims:
    """
    Validate and persist a license JWT.
    Raises LicenseInvalidError if the token cannot be verified.
    """
    key = key.strip()
    try:
        jwt.decode(key, PUBLIC_KEY_PEM, leeway=TOLERANCE_SECONDS)
    except jwt.ExpiredSignatureError:
        raise LicenseInvalidError("This license has already expired.")
    except (jwt.InvalidTokenError, InvalidKeyError):
        raise LicenseInvalidError("Invalid license key. Please check and try again.")

    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
    LICENSE_KEY_PATH.write_text(key, encoding="utf-8")
    LICENSE_KEY_PATH.chmod(0o600)

    return verify_license()


def x_activate_license__mutmut_9(key: str) -> LicenseClaims:
    """
    Validate and persist a license JWT.
    Raises LicenseInvalidError if the token cannot be verified.
    """
    key = key.strip()
    try:
        jwt.decode(key, PUBLIC_KEY_PEM, algorithms=["RS256"], )
    except jwt.ExpiredSignatureError:
        raise LicenseInvalidError("This license has already expired.")
    except (jwt.InvalidTokenError, InvalidKeyError):
        raise LicenseInvalidError("Invalid license key. Please check and try again.")

    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
    LICENSE_KEY_PATH.write_text(key, encoding="utf-8")
    LICENSE_KEY_PATH.chmod(0o600)

    return verify_license()


def x_activate_license__mutmut_10(key: str) -> LicenseClaims:
    """
    Validate and persist a license JWT.
    Raises LicenseInvalidError if the token cannot be verified.
    """
    key = key.strip()
    try:
        jwt.decode(key, PUBLIC_KEY_PEM, algorithms=["XXRS256XX"], leeway=TOLERANCE_SECONDS)
    except jwt.ExpiredSignatureError:
        raise LicenseInvalidError("This license has already expired.")
    except (jwt.InvalidTokenError, InvalidKeyError):
        raise LicenseInvalidError("Invalid license key. Please check and try again.")

    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
    LICENSE_KEY_PATH.write_text(key, encoding="utf-8")
    LICENSE_KEY_PATH.chmod(0o600)

    return verify_license()


def x_activate_license__mutmut_11(key: str) -> LicenseClaims:
    """
    Validate and persist a license JWT.
    Raises LicenseInvalidError if the token cannot be verified.
    """
    key = key.strip()
    try:
        jwt.decode(key, PUBLIC_KEY_PEM, algorithms=["rs256"], leeway=TOLERANCE_SECONDS)
    except jwt.ExpiredSignatureError:
        raise LicenseInvalidError("This license has already expired.")
    except (jwt.InvalidTokenError, InvalidKeyError):
        raise LicenseInvalidError("Invalid license key. Please check and try again.")

    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
    LICENSE_KEY_PATH.write_text(key, encoding="utf-8")
    LICENSE_KEY_PATH.chmod(0o600)

    return verify_license()


def x_activate_license__mutmut_12(key: str) -> LicenseClaims:
    """
    Validate and persist a license JWT.
    Raises LicenseInvalidError if the token cannot be verified.
    """
    key = key.strip()
    try:
        jwt.decode(key, PUBLIC_KEY_PEM, algorithms=["RS256"], leeway=TOLERANCE_SECONDS)
    except jwt.ExpiredSignatureError:
        raise LicenseInvalidError(None)
    except (jwt.InvalidTokenError, InvalidKeyError):
        raise LicenseInvalidError("Invalid license key. Please check and try again.")

    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
    LICENSE_KEY_PATH.write_text(key, encoding="utf-8")
    LICENSE_KEY_PATH.chmod(0o600)

    return verify_license()


def x_activate_license__mutmut_13(key: str) -> LicenseClaims:
    """
    Validate and persist a license JWT.
    Raises LicenseInvalidError if the token cannot be verified.
    """
    key = key.strip()
    try:
        jwt.decode(key, PUBLIC_KEY_PEM, algorithms=["RS256"], leeway=TOLERANCE_SECONDS)
    except jwt.ExpiredSignatureError:
        raise LicenseInvalidError("XXThis license has already expired.XX")
    except (jwt.InvalidTokenError, InvalidKeyError):
        raise LicenseInvalidError("Invalid license key. Please check and try again.")

    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
    LICENSE_KEY_PATH.write_text(key, encoding="utf-8")
    LICENSE_KEY_PATH.chmod(0o600)

    return verify_license()


def x_activate_license__mutmut_14(key: str) -> LicenseClaims:
    """
    Validate and persist a license JWT.
    Raises LicenseInvalidError if the token cannot be verified.
    """
    key = key.strip()
    try:
        jwt.decode(key, PUBLIC_KEY_PEM, algorithms=["RS256"], leeway=TOLERANCE_SECONDS)
    except jwt.ExpiredSignatureError:
        raise LicenseInvalidError("this license has already expired.")
    except (jwt.InvalidTokenError, InvalidKeyError):
        raise LicenseInvalidError("Invalid license key. Please check and try again.")

    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
    LICENSE_KEY_PATH.write_text(key, encoding="utf-8")
    LICENSE_KEY_PATH.chmod(0o600)

    return verify_license()


def x_activate_license__mutmut_15(key: str) -> LicenseClaims:
    """
    Validate and persist a license JWT.
    Raises LicenseInvalidError if the token cannot be verified.
    """
    key = key.strip()
    try:
        jwt.decode(key, PUBLIC_KEY_PEM, algorithms=["RS256"], leeway=TOLERANCE_SECONDS)
    except jwt.ExpiredSignatureError:
        raise LicenseInvalidError("THIS LICENSE HAS ALREADY EXPIRED.")
    except (jwt.InvalidTokenError, InvalidKeyError):
        raise LicenseInvalidError("Invalid license key. Please check and try again.")

    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
    LICENSE_KEY_PATH.write_text(key, encoding="utf-8")
    LICENSE_KEY_PATH.chmod(0o600)

    return verify_license()


def x_activate_license__mutmut_16(key: str) -> LicenseClaims:
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
        raise LicenseInvalidError(None)

    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
    LICENSE_KEY_PATH.write_text(key, encoding="utf-8")
    LICENSE_KEY_PATH.chmod(0o600)

    return verify_license()


def x_activate_license__mutmut_17(key: str) -> LicenseClaims:
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
        raise LicenseInvalidError("XXInvalid license key. Please check and try again.XX")

    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
    LICENSE_KEY_PATH.write_text(key, encoding="utf-8")
    LICENSE_KEY_PATH.chmod(0o600)

    return verify_license()


def x_activate_license__mutmut_18(key: str) -> LicenseClaims:
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
        raise LicenseInvalidError("invalid license key. please check and try again.")

    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
    LICENSE_KEY_PATH.write_text(key, encoding="utf-8")
    LICENSE_KEY_PATH.chmod(0o600)

    return verify_license()


def x_activate_license__mutmut_19(key: str) -> LicenseClaims:
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
        raise LicenseInvalidError("INVALID LICENSE KEY. PLEASE CHECK AND TRY AGAIN.")

    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
    LICENSE_KEY_PATH.write_text(key, encoding="utf-8")
    LICENSE_KEY_PATH.chmod(0o600)

    return verify_license()


def x_activate_license__mutmut_20(key: str) -> LicenseClaims:
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

    LICENSE_KEY_PATH.parent.mkdir(parents=None, exist_ok=True)
    LICENSE_KEY_PATH.write_text(key, encoding="utf-8")
    LICENSE_KEY_PATH.chmod(0o600)

    return verify_license()


def x_activate_license__mutmut_21(key: str) -> LicenseClaims:
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

    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=None)
    LICENSE_KEY_PATH.write_text(key, encoding="utf-8")
    LICENSE_KEY_PATH.chmod(0o600)

    return verify_license()


def x_activate_license__mutmut_22(key: str) -> LicenseClaims:
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

    LICENSE_KEY_PATH.parent.mkdir(exist_ok=True)
    LICENSE_KEY_PATH.write_text(key, encoding="utf-8")
    LICENSE_KEY_PATH.chmod(0o600)

    return verify_license()


def x_activate_license__mutmut_23(key: str) -> LicenseClaims:
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

    LICENSE_KEY_PATH.parent.mkdir(parents=True, )
    LICENSE_KEY_PATH.write_text(key, encoding="utf-8")
    LICENSE_KEY_PATH.chmod(0o600)

    return verify_license()


def x_activate_license__mutmut_24(key: str) -> LicenseClaims:
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

    LICENSE_KEY_PATH.parent.mkdir(parents=False, exist_ok=True)
    LICENSE_KEY_PATH.write_text(key, encoding="utf-8")
    LICENSE_KEY_PATH.chmod(0o600)

    return verify_license()


def x_activate_license__mutmut_25(key: str) -> LicenseClaims:
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

    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=False)
    LICENSE_KEY_PATH.write_text(key, encoding="utf-8")
    LICENSE_KEY_PATH.chmod(0o600)

    return verify_license()


def x_activate_license__mutmut_26(key: str) -> LicenseClaims:
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
    LICENSE_KEY_PATH.write_text(None, encoding="utf-8")
    LICENSE_KEY_PATH.chmod(0o600)

    return verify_license()


def x_activate_license__mutmut_27(key: str) -> LicenseClaims:
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
    LICENSE_KEY_PATH.write_text(key, encoding=None)
    LICENSE_KEY_PATH.chmod(0o600)

    return verify_license()


def x_activate_license__mutmut_28(key: str) -> LicenseClaims:
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
    LICENSE_KEY_PATH.write_text(encoding="utf-8")
    LICENSE_KEY_PATH.chmod(0o600)

    return verify_license()


def x_activate_license__mutmut_29(key: str) -> LicenseClaims:
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
    LICENSE_KEY_PATH.write_text(key, )
    LICENSE_KEY_PATH.chmod(0o600)

    return verify_license()


def x_activate_license__mutmut_30(key: str) -> LicenseClaims:
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
    LICENSE_KEY_PATH.write_text(key, encoding="XXutf-8XX")
    LICENSE_KEY_PATH.chmod(0o600)

    return verify_license()


def x_activate_license__mutmut_31(key: str) -> LicenseClaims:
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
    LICENSE_KEY_PATH.write_text(key, encoding="UTF-8")
    LICENSE_KEY_PATH.chmod(0o600)

    return verify_license()


def x_activate_license__mutmut_32(key: str) -> LicenseClaims:
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
    LICENSE_KEY_PATH.chmod(None)

    return verify_license()


def x_activate_license__mutmut_33(key: str) -> LicenseClaims:
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
    LICENSE_KEY_PATH.chmod(385)

    return verify_license()

mutants_x_activate_license__mutmut['_mutmut_orig'] = x_activate_license__mutmut_orig # type: ignore # mutmut generated
mutants_x_activate_license__mutmut['x_activate_license__mutmut_1'] = x_activate_license__mutmut_1 # type: ignore # mutmut generated
mutants_x_activate_license__mutmut['x_activate_license__mutmut_2'] = x_activate_license__mutmut_2 # type: ignore # mutmut generated
mutants_x_activate_license__mutmut['x_activate_license__mutmut_3'] = x_activate_license__mutmut_3 # type: ignore # mutmut generated
mutants_x_activate_license__mutmut['x_activate_license__mutmut_4'] = x_activate_license__mutmut_4 # type: ignore # mutmut generated
mutants_x_activate_license__mutmut['x_activate_license__mutmut_5'] = x_activate_license__mutmut_5 # type: ignore # mutmut generated
mutants_x_activate_license__mutmut['x_activate_license__mutmut_6'] = x_activate_license__mutmut_6 # type: ignore # mutmut generated
mutants_x_activate_license__mutmut['x_activate_license__mutmut_7'] = x_activate_license__mutmut_7 # type: ignore # mutmut generated
mutants_x_activate_license__mutmut['x_activate_license__mutmut_8'] = x_activate_license__mutmut_8 # type: ignore # mutmut generated
mutants_x_activate_license__mutmut['x_activate_license__mutmut_9'] = x_activate_license__mutmut_9 # type: ignore # mutmut generated
mutants_x_activate_license__mutmut['x_activate_license__mutmut_10'] = x_activate_license__mutmut_10 # type: ignore # mutmut generated
mutants_x_activate_license__mutmut['x_activate_license__mutmut_11'] = x_activate_license__mutmut_11 # type: ignore # mutmut generated
mutants_x_activate_license__mutmut['x_activate_license__mutmut_12'] = x_activate_license__mutmut_12 # type: ignore # mutmut generated
mutants_x_activate_license__mutmut['x_activate_license__mutmut_13'] = x_activate_license__mutmut_13 # type: ignore # mutmut generated
mutants_x_activate_license__mutmut['x_activate_license__mutmut_14'] = x_activate_license__mutmut_14 # type: ignore # mutmut generated
mutants_x_activate_license__mutmut['x_activate_license__mutmut_15'] = x_activate_license__mutmut_15 # type: ignore # mutmut generated
mutants_x_activate_license__mutmut['x_activate_license__mutmut_16'] = x_activate_license__mutmut_16 # type: ignore # mutmut generated
mutants_x_activate_license__mutmut['x_activate_license__mutmut_17'] = x_activate_license__mutmut_17 # type: ignore # mutmut generated
mutants_x_activate_license__mutmut['x_activate_license__mutmut_18'] = x_activate_license__mutmut_18 # type: ignore # mutmut generated
mutants_x_activate_license__mutmut['x_activate_license__mutmut_19'] = x_activate_license__mutmut_19 # type: ignore # mutmut generated
mutants_x_activate_license__mutmut['x_activate_license__mutmut_20'] = x_activate_license__mutmut_20 # type: ignore # mutmut generated
mutants_x_activate_license__mutmut['x_activate_license__mutmut_21'] = x_activate_license__mutmut_21 # type: ignore # mutmut generated
mutants_x_activate_license__mutmut['x_activate_license__mutmut_22'] = x_activate_license__mutmut_22 # type: ignore # mutmut generated
mutants_x_activate_license__mutmut['x_activate_license__mutmut_23'] = x_activate_license__mutmut_23 # type: ignore # mutmut generated
mutants_x_activate_license__mutmut['x_activate_license__mutmut_24'] = x_activate_license__mutmut_24 # type: ignore # mutmut generated
mutants_x_activate_license__mutmut['x_activate_license__mutmut_25'] = x_activate_license__mutmut_25 # type: ignore # mutmut generated
mutants_x_activate_license__mutmut['x_activate_license__mutmut_26'] = x_activate_license__mutmut_26 # type: ignore # mutmut generated
mutants_x_activate_license__mutmut['x_activate_license__mutmut_27'] = x_activate_license__mutmut_27 # type: ignore # mutmut generated
mutants_x_activate_license__mutmut['x_activate_license__mutmut_28'] = x_activate_license__mutmut_28 # type: ignore # mutmut generated
mutants_x_activate_license__mutmut['x_activate_license__mutmut_29'] = x_activate_license__mutmut_29 # type: ignore # mutmut generated
mutants_x_activate_license__mutmut['x_activate_license__mutmut_30'] = x_activate_license__mutmut_30 # type: ignore # mutmut generated
mutants_x_activate_license__mutmut['x_activate_license__mutmut_31'] = x_activate_license__mutmut_31 # type: ignore # mutmut generated
mutants_x_activate_license__mutmut['x_activate_license__mutmut_32'] = x_activate_license__mutmut_32 # type: ignore # mutmut generated
mutants_x_activate_license__mutmut['x_activate_license__mutmut_33'] = x_activate_license__mutmut_33 # type: ignore # mutmut generated


def get_current_tier() -> LicenseTier:
    """Alias for get_license_tier — used by older callers."""
    return get_license_tier()
mutants_x_is_pro__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_is_pro__mutmut)
def is_pro() -> bool:
    """Check if the current installation has a paid Team or Scale-up license."""
    return get_license_tier() != LicenseTier.STARTER


def x_is_pro__mutmut_orig() -> bool:
    """Check if the current installation has a paid Team or Scale-up license."""
    return get_license_tier() != LicenseTier.STARTER


def x_is_pro__mutmut_1() -> bool:
    """Check if the current installation has a paid Team or Scale-up license."""
    return get_license_tier() == LicenseTier.STARTER

mutants_x_is_pro__mutmut['_mutmut_orig'] = x_is_pro__mutmut_orig # type: ignore # mutmut generated
mutants_x_is_pro__mutmut['x_is_pro__mutmut_1'] = x_is_pro__mutmut_1 # type: ignore # mutmut generated
