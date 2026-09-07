import base64
import json
import logging
import os
from pathlib import Path

import httpx

from hexawyn.domain.models.license import LicenseClaims
from hexawyn.domain.services.license_state import LicenseState, compute_license_state

LICENSE_KEY_PATH = Path.home() / ".hexawyn" / "license.key"
HEXA_CLOUD_URL = os.environ.get("HEXAWYN_CLOUD_ENDPOINT", "https://api.hexawyn.com")
REFRESH_INTERVAL_SECONDS = 6 * 3600

logger = logging.getLogger(__name__)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_read_license_state__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_read_license_state__mutmut)
def read_license_state() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_orig() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_1() -> LicenseState:
    token = None
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_2() -> LicenseState:
    token = _read_license_key()
    if token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_3() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state=None, plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_4() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan=None, days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_5() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=None, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_6() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date=None)

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_7() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_8() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_9() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_10() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, )

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_11() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="XXmissingXX", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_12() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="MISSING", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_13() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="XXunknownXX", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_14() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="UNKNOWN", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_15() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=1, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_16() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="XXXX")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_17() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = None
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_18() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(None)
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_19() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split("XX.XX")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_20() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) <= 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_21() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 3:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_22() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state=None, plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_23() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan=None, days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_24() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=None, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_25() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date=None)

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_26() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_27() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_28() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_29() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, )

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_30() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="XXinvalidXX", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_31() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="INVALID", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_32() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="XXunknownXX", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_33() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="UNKNOWN", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_34() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=1, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_35() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="XXXX")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_36() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = None
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_37() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[2]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_38() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = None
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_39() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 + len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_40() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 5 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_41() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) / 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_42() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 5
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_43() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding == 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_44() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 5:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_45() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload = "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_46() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload -= "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_47() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" / padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_48() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "XX=XX" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_49() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = None

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_50() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(None)

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_51() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(None).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_52() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = None
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_53() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get(None, 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_54() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", None)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_55() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get(0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_56() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", )
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_57() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("XXexpXX", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_58() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("EXP", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_59() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 1)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_60() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 or "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_61() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value != 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_62() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 1 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_63() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "XXplanXX" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_64() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "PLAN" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_65() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" not in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_66() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state=None,
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_67() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=None,
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_68() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=None,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_69() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date=None,
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_70() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_71() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_72() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_73() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_74() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="XXactiveXX",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_75() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="ACTIVE",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_76() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(None),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_77() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get(None, "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_78() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", None)),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_79() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_80() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", )),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_81() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("XXplanXX", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_82() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("PLAN", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_83() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "XXstarterXX")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_84() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "STARTER")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_85() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=1,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_86() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="XXunknownXX",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_87() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="UNKNOWN",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_88() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = None

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_89() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=None,
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_90() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=None,
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_91() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=None,
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_92() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=None,
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_93() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=None,
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_94() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=None,
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_95() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=None,
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_96() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=None,
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_97() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=None,
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_98() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_99() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_100() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_101() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_102() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_103() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_104() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_105() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_106() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_107() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get(None, ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_108() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", None),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_109() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get(""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_110() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_111() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("XXsubXX", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_112() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("SUB", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_113() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", "XXXX"),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_114() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get(None, "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_115() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", None),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_116() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_117() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", ),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_118() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("XXplanXX", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_119() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("PLAN", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_120() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "XXstarterXX"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_121() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "STARTER"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_122() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get(None, 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_123() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", None),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_124() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get(1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_125() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", ),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_126() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("XXclusters_maxXX", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_127() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("CLUSTERS_MAX", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_128() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 2),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_129() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get(None, 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_130() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", None),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_131() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get(1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_132() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", ),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_133() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("XXusers_maxXX", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_134() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("USERS_MAX", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_135() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 2),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_136() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get(None, 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_137() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", None),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_138() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get(50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_139() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", ),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_140() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("XXinvestigations_monthlyXX", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_141() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("INVESTIGATIONS_MONTHLY", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_142() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 51),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_143() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get(None, 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_144() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", None),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_145() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get(7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_146() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", ),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_147() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("XXhistory_daysXX", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_148() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("HISTORY_DAYS", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_149() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 8),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_150() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get(None, ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_151() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", None),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_152() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get(["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_153() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_154() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("XXprovidersXX", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_155() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("PROVIDERS", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_156() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["XXvanillaXX"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_157() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["VANILLA"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_158() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(None),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_159() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(None),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_160() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get(None, 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_161() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", None)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_162() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get(0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_163() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", )),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_164() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("XXiatXX", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_165() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("IAT", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_166() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 1)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_167() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(None)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_168() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state=None, plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_169() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan=None, days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_170() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=None, expiry_date="")


def x_read_license_state__mutmut_171() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date=None)


def x_read_license_state__mutmut_172() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_173() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_174() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", expiry_date="")


def x_read_license_state__mutmut_175() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, )


def x_read_license_state__mutmut_176() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="XXinvalidXX", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_177() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="INVALID", plan="unknown", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_178() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="XXunknownXX", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_179() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="UNKNOWN", days_remaining=0, expiry_date="")


def x_read_license_state__mutmut_180() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=1, expiry_date="")


def x_read_license_state__mutmut_181() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:  # noqa: PLR2004
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:  # noqa: PLR2004
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="XXXX")

mutants_x_read_license_state__mutmut['_mutmut_orig'] = x_read_license_state__mutmut_orig # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_1'] = x_read_license_state__mutmut_1 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_2'] = x_read_license_state__mutmut_2 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_3'] = x_read_license_state__mutmut_3 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_4'] = x_read_license_state__mutmut_4 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_5'] = x_read_license_state__mutmut_5 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_6'] = x_read_license_state__mutmut_6 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_7'] = x_read_license_state__mutmut_7 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_8'] = x_read_license_state__mutmut_8 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_9'] = x_read_license_state__mutmut_9 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_10'] = x_read_license_state__mutmut_10 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_11'] = x_read_license_state__mutmut_11 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_12'] = x_read_license_state__mutmut_12 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_13'] = x_read_license_state__mutmut_13 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_14'] = x_read_license_state__mutmut_14 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_15'] = x_read_license_state__mutmut_15 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_16'] = x_read_license_state__mutmut_16 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_17'] = x_read_license_state__mutmut_17 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_18'] = x_read_license_state__mutmut_18 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_19'] = x_read_license_state__mutmut_19 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_20'] = x_read_license_state__mutmut_20 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_21'] = x_read_license_state__mutmut_21 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_22'] = x_read_license_state__mutmut_22 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_23'] = x_read_license_state__mutmut_23 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_24'] = x_read_license_state__mutmut_24 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_25'] = x_read_license_state__mutmut_25 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_26'] = x_read_license_state__mutmut_26 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_27'] = x_read_license_state__mutmut_27 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_28'] = x_read_license_state__mutmut_28 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_29'] = x_read_license_state__mutmut_29 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_30'] = x_read_license_state__mutmut_30 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_31'] = x_read_license_state__mutmut_31 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_32'] = x_read_license_state__mutmut_32 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_33'] = x_read_license_state__mutmut_33 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_34'] = x_read_license_state__mutmut_34 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_35'] = x_read_license_state__mutmut_35 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_36'] = x_read_license_state__mutmut_36 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_37'] = x_read_license_state__mutmut_37 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_38'] = x_read_license_state__mutmut_38 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_39'] = x_read_license_state__mutmut_39 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_40'] = x_read_license_state__mutmut_40 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_41'] = x_read_license_state__mutmut_41 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_42'] = x_read_license_state__mutmut_42 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_43'] = x_read_license_state__mutmut_43 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_44'] = x_read_license_state__mutmut_44 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_45'] = x_read_license_state__mutmut_45 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_46'] = x_read_license_state__mutmut_46 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_47'] = x_read_license_state__mutmut_47 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_48'] = x_read_license_state__mutmut_48 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_49'] = x_read_license_state__mutmut_49 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_50'] = x_read_license_state__mutmut_50 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_51'] = x_read_license_state__mutmut_51 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_52'] = x_read_license_state__mutmut_52 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_53'] = x_read_license_state__mutmut_53 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_54'] = x_read_license_state__mutmut_54 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_55'] = x_read_license_state__mutmut_55 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_56'] = x_read_license_state__mutmut_56 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_57'] = x_read_license_state__mutmut_57 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_58'] = x_read_license_state__mutmut_58 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_59'] = x_read_license_state__mutmut_59 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_60'] = x_read_license_state__mutmut_60 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_61'] = x_read_license_state__mutmut_61 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_62'] = x_read_license_state__mutmut_62 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_63'] = x_read_license_state__mutmut_63 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_64'] = x_read_license_state__mutmut_64 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_65'] = x_read_license_state__mutmut_65 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_66'] = x_read_license_state__mutmut_66 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_67'] = x_read_license_state__mutmut_67 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_68'] = x_read_license_state__mutmut_68 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_69'] = x_read_license_state__mutmut_69 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_70'] = x_read_license_state__mutmut_70 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_71'] = x_read_license_state__mutmut_71 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_72'] = x_read_license_state__mutmut_72 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_73'] = x_read_license_state__mutmut_73 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_74'] = x_read_license_state__mutmut_74 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_75'] = x_read_license_state__mutmut_75 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_76'] = x_read_license_state__mutmut_76 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_77'] = x_read_license_state__mutmut_77 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_78'] = x_read_license_state__mutmut_78 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_79'] = x_read_license_state__mutmut_79 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_80'] = x_read_license_state__mutmut_80 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_81'] = x_read_license_state__mutmut_81 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_82'] = x_read_license_state__mutmut_82 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_83'] = x_read_license_state__mutmut_83 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_84'] = x_read_license_state__mutmut_84 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_85'] = x_read_license_state__mutmut_85 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_86'] = x_read_license_state__mutmut_86 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_87'] = x_read_license_state__mutmut_87 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_88'] = x_read_license_state__mutmut_88 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_89'] = x_read_license_state__mutmut_89 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_90'] = x_read_license_state__mutmut_90 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_91'] = x_read_license_state__mutmut_91 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_92'] = x_read_license_state__mutmut_92 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_93'] = x_read_license_state__mutmut_93 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_94'] = x_read_license_state__mutmut_94 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_95'] = x_read_license_state__mutmut_95 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_96'] = x_read_license_state__mutmut_96 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_97'] = x_read_license_state__mutmut_97 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_98'] = x_read_license_state__mutmut_98 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_99'] = x_read_license_state__mutmut_99 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_100'] = x_read_license_state__mutmut_100 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_101'] = x_read_license_state__mutmut_101 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_102'] = x_read_license_state__mutmut_102 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_103'] = x_read_license_state__mutmut_103 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_104'] = x_read_license_state__mutmut_104 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_105'] = x_read_license_state__mutmut_105 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_106'] = x_read_license_state__mutmut_106 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_107'] = x_read_license_state__mutmut_107 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_108'] = x_read_license_state__mutmut_108 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_109'] = x_read_license_state__mutmut_109 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_110'] = x_read_license_state__mutmut_110 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_111'] = x_read_license_state__mutmut_111 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_112'] = x_read_license_state__mutmut_112 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_113'] = x_read_license_state__mutmut_113 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_114'] = x_read_license_state__mutmut_114 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_115'] = x_read_license_state__mutmut_115 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_116'] = x_read_license_state__mutmut_116 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_117'] = x_read_license_state__mutmut_117 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_118'] = x_read_license_state__mutmut_118 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_119'] = x_read_license_state__mutmut_119 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_120'] = x_read_license_state__mutmut_120 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_121'] = x_read_license_state__mutmut_121 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_122'] = x_read_license_state__mutmut_122 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_123'] = x_read_license_state__mutmut_123 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_124'] = x_read_license_state__mutmut_124 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_125'] = x_read_license_state__mutmut_125 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_126'] = x_read_license_state__mutmut_126 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_127'] = x_read_license_state__mutmut_127 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_128'] = x_read_license_state__mutmut_128 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_129'] = x_read_license_state__mutmut_129 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_130'] = x_read_license_state__mutmut_130 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_131'] = x_read_license_state__mutmut_131 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_132'] = x_read_license_state__mutmut_132 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_133'] = x_read_license_state__mutmut_133 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_134'] = x_read_license_state__mutmut_134 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_135'] = x_read_license_state__mutmut_135 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_136'] = x_read_license_state__mutmut_136 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_137'] = x_read_license_state__mutmut_137 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_138'] = x_read_license_state__mutmut_138 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_139'] = x_read_license_state__mutmut_139 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_140'] = x_read_license_state__mutmut_140 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_141'] = x_read_license_state__mutmut_141 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_142'] = x_read_license_state__mutmut_142 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_143'] = x_read_license_state__mutmut_143 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_144'] = x_read_license_state__mutmut_144 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_145'] = x_read_license_state__mutmut_145 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_146'] = x_read_license_state__mutmut_146 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_147'] = x_read_license_state__mutmut_147 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_148'] = x_read_license_state__mutmut_148 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_149'] = x_read_license_state__mutmut_149 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_150'] = x_read_license_state__mutmut_150 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_151'] = x_read_license_state__mutmut_151 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_152'] = x_read_license_state__mutmut_152 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_153'] = x_read_license_state__mutmut_153 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_154'] = x_read_license_state__mutmut_154 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_155'] = x_read_license_state__mutmut_155 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_156'] = x_read_license_state__mutmut_156 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_157'] = x_read_license_state__mutmut_157 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_158'] = x_read_license_state__mutmut_158 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_159'] = x_read_license_state__mutmut_159 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_160'] = x_read_license_state__mutmut_160 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_161'] = x_read_license_state__mutmut_161 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_162'] = x_read_license_state__mutmut_162 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_163'] = x_read_license_state__mutmut_163 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_164'] = x_read_license_state__mutmut_164 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_165'] = x_read_license_state__mutmut_165 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_166'] = x_read_license_state__mutmut_166 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_167'] = x_read_license_state__mutmut_167 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_168'] = x_read_license_state__mutmut_168 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_169'] = x_read_license_state__mutmut_169 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_170'] = x_read_license_state__mutmut_170 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_171'] = x_read_license_state__mutmut_171 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_172'] = x_read_license_state__mutmut_172 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_173'] = x_read_license_state__mutmut_173 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_174'] = x_read_license_state__mutmut_174 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_175'] = x_read_license_state__mutmut_175 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_176'] = x_read_license_state__mutmut_176 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_177'] = x_read_license_state__mutmut_177 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_178'] = x_read_license_state__mutmut_178 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_179'] = x_read_license_state__mutmut_179 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_180'] = x_read_license_state__mutmut_180 # type: ignore # mutmut generated
mutants_x_read_license_state__mutmut['x_read_license_state__mutmut_181'] = x_read_license_state__mutmut_181 # type: ignore # mutmut generated
mutants_x__read_license_key__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__read_license_key__mutmut)
def _read_license_key() -> str | None:
    try:
        env_key = os.environ.get("HEXAWYN_LICENSE_KEY")
        if env_key:
            return env_key.strip()
        if LICENSE_KEY_PATH.exists():
            return LICENSE_KEY_PATH.read_text(encoding="utf-8").strip()
        return None
    except Exception:
        return None


def x__read_license_key__mutmut_orig() -> str | None:
    try:
        env_key = os.environ.get("HEXAWYN_LICENSE_KEY")
        if env_key:
            return env_key.strip()
        if LICENSE_KEY_PATH.exists():
            return LICENSE_KEY_PATH.read_text(encoding="utf-8").strip()
        return None
    except Exception:
        return None


def x__read_license_key__mutmut_1() -> str | None:
    try:
        env_key = None
        if env_key:
            return env_key.strip()
        if LICENSE_KEY_PATH.exists():
            return LICENSE_KEY_PATH.read_text(encoding="utf-8").strip()
        return None
    except Exception:
        return None


def x__read_license_key__mutmut_2() -> str | None:
    try:
        env_key = os.environ.get(None)
        if env_key:
            return env_key.strip()
        if LICENSE_KEY_PATH.exists():
            return LICENSE_KEY_PATH.read_text(encoding="utf-8").strip()
        return None
    except Exception:
        return None


def x__read_license_key__mutmut_3() -> str | None:
    try:
        env_key = os.environ.get("XXHEXAWYN_LICENSE_KEYXX")
        if env_key:
            return env_key.strip()
        if LICENSE_KEY_PATH.exists():
            return LICENSE_KEY_PATH.read_text(encoding="utf-8").strip()
        return None
    except Exception:
        return None


def x__read_license_key__mutmut_4() -> str | None:
    try:
        env_key = os.environ.get("hexawyn_license_key")
        if env_key:
            return env_key.strip()
        if LICENSE_KEY_PATH.exists():
            return LICENSE_KEY_PATH.read_text(encoding="utf-8").strip()
        return None
    except Exception:
        return None


def x__read_license_key__mutmut_5() -> str | None:
    try:
        env_key = os.environ.get("HEXAWYN_LICENSE_KEY")
        if env_key:
            return env_key.strip()
        if LICENSE_KEY_PATH.exists():
            return LICENSE_KEY_PATH.read_text(encoding=None).strip()
        return None
    except Exception:
        return None


def x__read_license_key__mutmut_6() -> str | None:
    try:
        env_key = os.environ.get("HEXAWYN_LICENSE_KEY")
        if env_key:
            return env_key.strip()
        if LICENSE_KEY_PATH.exists():
            return LICENSE_KEY_PATH.read_text(encoding="XXutf-8XX").strip()
        return None
    except Exception:
        return None


def x__read_license_key__mutmut_7() -> str | None:
    try:
        env_key = os.environ.get("HEXAWYN_LICENSE_KEY")
        if env_key:
            return env_key.strip()
        if LICENSE_KEY_PATH.exists():
            return LICENSE_KEY_PATH.read_text(encoding="UTF-8").strip()
        return None
    except Exception:
        return None

mutants_x__read_license_key__mutmut['_mutmut_orig'] = x__read_license_key__mutmut_orig # type: ignore # mutmut generated
mutants_x__read_license_key__mutmut['x__read_license_key__mutmut_1'] = x__read_license_key__mutmut_1 # type: ignore # mutmut generated
mutants_x__read_license_key__mutmut['x__read_license_key__mutmut_2'] = x__read_license_key__mutmut_2 # type: ignore # mutmut generated
mutants_x__read_license_key__mutmut['x__read_license_key__mutmut_3'] = x__read_license_key__mutmut_3 # type: ignore # mutmut generated
mutants_x__read_license_key__mutmut['x__read_license_key__mutmut_4'] = x__read_license_key__mutmut_4 # type: ignore # mutmut generated
mutants_x__read_license_key__mutmut['x__read_license_key__mutmut_5'] = x__read_license_key__mutmut_5 # type: ignore # mutmut generated
mutants_x__read_license_key__mutmut['x__read_license_key__mutmut_6'] = x__read_license_key__mutmut_6 # type: ignore # mutmut generated
mutants_x__read_license_key__mutmut['x__read_license_key__mutmut_7'] = x__read_license_key__mutmut_7 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_refresh_license__mutmut)
def refresh_license() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get("hexawyn_token")
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )
            if resp.status_code == 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get("token", "")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_orig() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get("hexawyn_token")
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )
            if resp.status_code == 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get("token", "")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_1() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = None
        token = config.get("hexawyn_token")
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )
            if resp.status_code == 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get("token", "")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_2() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = None
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )
            if resp.status_code == 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get("token", "")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_3() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get(None)
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )
            if resp.status_code == 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get("token", "")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_4() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get("XXhexawyn_tokenXX")
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )
            if resp.status_code == 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get("token", "")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_5() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get("HEXAWYN_TOKEN")
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )
            if resp.status_code == 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get("token", "")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_6() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get("hexawyn_token")
        if token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )
            if resp.status_code == 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get("token", "")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_7() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get("hexawyn_token")
        if not token:
            return True

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )
            if resp.status_code == 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get("token", "")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_8() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get("hexawyn_token")
        if not token:
            return False

        machine_id = None
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )
            if resp.status_code == 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get("token", "")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_9() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get("hexawyn_token")
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=None) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )
            if resp.status_code == 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get("token", "")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_10() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get("hexawyn_token")
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=11.0) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )
            if resp.status_code == 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get("token", "")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_11() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get("hexawyn_token")
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = None
            if resp.status_code == 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get("token", "")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_12() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get("hexawyn_token")
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                None,
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )
            if resp.status_code == 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get("token", "")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_13() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get("hexawyn_token")
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                json=None,
            )
            if resp.status_code == 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get("token", "")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_14() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get("hexawyn_token")
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )
            if resp.status_code == 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get("token", "")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_15() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get("hexawyn_token")
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                )
            if resp.status_code == 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get("token", "")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_16() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get("hexawyn_token")
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                json={
                    "XXapi_keyXX": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )
            if resp.status_code == 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get("token", "")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_17() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get("hexawyn_token")
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                json={
                    "API_KEY": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )
            if resp.status_code == 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get("token", "")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_18() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get("hexawyn_token")
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                json={
                    "api_key": token,
                    "XXmachine_idXX": machine_id,
                    "client_version": "1.0.0",
                },
            )
            if resp.status_code == 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get("token", "")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_19() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get("hexawyn_token")
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                json={
                    "api_key": token,
                    "MACHINE_ID": machine_id,
                    "client_version": "1.0.0",
                },
            )
            if resp.status_code == 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get("token", "")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_20() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get("hexawyn_token")
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "XXclient_versionXX": "1.0.0",
                },
            )
            if resp.status_code == 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get("token", "")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_21() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get("hexawyn_token")
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "CLIENT_VERSION": "1.0.0",
                },
            )
            if resp.status_code == 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get("token", "")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_22() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get("hexawyn_token")
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "XX1.0.0XX",
                },
            )
            if resp.status_code == 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get("token", "")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_23() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get("hexawyn_token")
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )
            if resp.status_code != 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get("token", "")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_24() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get("hexawyn_token")
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )
            if resp.status_code == 201:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get("token", "")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_25() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get("hexawyn_token")
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )
            if resp.status_code == 200:  # noqa: PLR2004
                data = None
                jwt_token = data.get("token", "")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_26() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get("hexawyn_token")
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )
            if resp.status_code == 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = None
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_27() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get("hexawyn_token")
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )
            if resp.status_code == 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get(None, "")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_28() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get("hexawyn_token")
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )
            if resp.status_code == 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get("token", None)
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_29() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get("hexawyn_token")
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )
            if resp.status_code == 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get("")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_30() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get("hexawyn_token")
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )
            if resp.status_code == 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get("token", )
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_31() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get("hexawyn_token")
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )
            if resp.status_code == 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get("XXtokenXX", "")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_32() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get("hexawyn_token")
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )
            if resp.status_code == 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get("TOKEN", "")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_33() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get("hexawyn_token")
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )
            if resp.status_code == 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get("token", "XXXX")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_34() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get("hexawyn_token")
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )
            if resp.status_code == 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get("token", "")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=None, exist_ok=True)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_35() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get("hexawyn_token")
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )
            if resp.status_code == 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get("token", "")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=None)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_36() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get("hexawyn_token")
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )
            if resp.status_code == 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get("token", "")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(exist_ok=True)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_37() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get("hexawyn_token")
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )
            if resp.status_code == 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get("token", "")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, )
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_38() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get("hexawyn_token")
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )
            if resp.status_code == 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get("token", "")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=False, exist_ok=True)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_39() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get("hexawyn_token")
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )
            if resp.status_code == 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get("token", "")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=False)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_40() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get("hexawyn_token")
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )
            if resp.status_code == 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get("token", "")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
                    LICENSE_KEY_PATH.write_text(None)
                    return True
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_41() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get("hexawyn_token")
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )
            if resp.status_code == 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get("token", "")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return False
        return False
    except Exception:
        return False


def x_refresh_license__mutmut_42() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get("hexawyn_token")
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )
            if resp.status_code == 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get("token", "")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return True
    except Exception:
        return False


def x_refresh_license__mutmut_43() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config  # hexa-lazy-import
        from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

        config = load_config()
        token = config.get("hexawyn_token")
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )
            if resp.status_code == 200:  # noqa: PLR2004
                data = resp.json()
                jwt_token = data.get("token", "")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return True

mutants_x_refresh_license__mutmut['_mutmut_orig'] = x_refresh_license__mutmut_orig # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_1'] = x_refresh_license__mutmut_1 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_2'] = x_refresh_license__mutmut_2 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_3'] = x_refresh_license__mutmut_3 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_4'] = x_refresh_license__mutmut_4 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_5'] = x_refresh_license__mutmut_5 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_6'] = x_refresh_license__mutmut_6 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_7'] = x_refresh_license__mutmut_7 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_8'] = x_refresh_license__mutmut_8 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_9'] = x_refresh_license__mutmut_9 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_10'] = x_refresh_license__mutmut_10 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_11'] = x_refresh_license__mutmut_11 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_12'] = x_refresh_license__mutmut_12 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_13'] = x_refresh_license__mutmut_13 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_14'] = x_refresh_license__mutmut_14 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_15'] = x_refresh_license__mutmut_15 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_16'] = x_refresh_license__mutmut_16 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_17'] = x_refresh_license__mutmut_17 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_18'] = x_refresh_license__mutmut_18 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_19'] = x_refresh_license__mutmut_19 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_20'] = x_refresh_license__mutmut_20 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_21'] = x_refresh_license__mutmut_21 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_22'] = x_refresh_license__mutmut_22 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_23'] = x_refresh_license__mutmut_23 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_24'] = x_refresh_license__mutmut_24 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_25'] = x_refresh_license__mutmut_25 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_26'] = x_refresh_license__mutmut_26 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_27'] = x_refresh_license__mutmut_27 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_28'] = x_refresh_license__mutmut_28 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_29'] = x_refresh_license__mutmut_29 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_30'] = x_refresh_license__mutmut_30 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_31'] = x_refresh_license__mutmut_31 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_32'] = x_refresh_license__mutmut_32 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_33'] = x_refresh_license__mutmut_33 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_34'] = x_refresh_license__mutmut_34 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_35'] = x_refresh_license__mutmut_35 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_36'] = x_refresh_license__mutmut_36 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_37'] = x_refresh_license__mutmut_37 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_38'] = x_refresh_license__mutmut_38 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_39'] = x_refresh_license__mutmut_39 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_40'] = x_refresh_license__mutmut_40 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_41'] = x_refresh_license__mutmut_41 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_42'] = x_refresh_license__mutmut_42 # type: ignore # mutmut generated
mutants_x_refresh_license__mutmut['x_refresh_license__mutmut_43'] = x_refresh_license__mutmut_43 # type: ignore # mutmut generated
