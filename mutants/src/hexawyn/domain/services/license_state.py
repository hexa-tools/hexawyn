from dataclasses import dataclass
from datetime import UTC, datetime
from math import ceil

from hexawyn.domain.models.license import LicenseClaims


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class LicenseState:
    state: str
    plan: str
    days_remaining: int
    expiry_date: str
mutants_x_compute_license_state__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compute_license_state__mutmut)
def compute_license_state(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_orig(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_1(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = None
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_2(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = None

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_3(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(None)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_4(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = None
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_5(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(None, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_6(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=None)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_7(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_8(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, )
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_9(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = None
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_10(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(None)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_11(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = None
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_12(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt + now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_13(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = None
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_14(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime(None)
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_15(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("XX%d %b %YXX")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_16(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_17(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%D %B %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_18(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = None

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_19(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(None, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_20(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, None)

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_21(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_22(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, )

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_23(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(1, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_24(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(None))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_25(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining * 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_26(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86401))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_27(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining < 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_28(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 1:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_29(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state=None,
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_30(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=None,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_31(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=None,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_32(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=None,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_33(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_34(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_35(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_36(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_37(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="XXexpiredXX",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_38(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="EXPIRED",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_39(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=1,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_40(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining < 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_41(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 / 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_42(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 8 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_43(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86401:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_44(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state=None,
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_45(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=None,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_46(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=None,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_47(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=None,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_48(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_49(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_50(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_51(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_52(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="XXwarningXX",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_53(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="WARNING",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_54(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state=None, plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_55(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=None, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_56(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=None, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_57(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=None
    )


def x_compute_license_state__mutmut_58(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_59(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_60(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_61(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, )


def x_compute_license_state__mutmut_62(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="XXactiveXX", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )


def x_compute_license_state__mutmut_63(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    seconds_remaining = (expiry_dt - now).total_seconds()
    expiry_date = expiry_dt.strftime("%d %b %Y")
    days_remaining = max(0, ceil(seconds_remaining / 86400))

    if seconds_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=0,
            expiry_date=expiry_date,
        )
    if seconds_remaining <= 7 * 86400:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="ACTIVE", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )

mutants_x_compute_license_state__mutmut['_mutmut_orig'] = x_compute_license_state__mutmut_orig # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_1'] = x_compute_license_state__mutmut_1 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_2'] = x_compute_license_state__mutmut_2 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_3'] = x_compute_license_state__mutmut_3 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_4'] = x_compute_license_state__mutmut_4 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_5'] = x_compute_license_state__mutmut_5 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_6'] = x_compute_license_state__mutmut_6 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_7'] = x_compute_license_state__mutmut_7 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_8'] = x_compute_license_state__mutmut_8 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_9'] = x_compute_license_state__mutmut_9 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_10'] = x_compute_license_state__mutmut_10 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_11'] = x_compute_license_state__mutmut_11 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_12'] = x_compute_license_state__mutmut_12 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_13'] = x_compute_license_state__mutmut_13 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_14'] = x_compute_license_state__mutmut_14 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_15'] = x_compute_license_state__mutmut_15 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_16'] = x_compute_license_state__mutmut_16 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_17'] = x_compute_license_state__mutmut_17 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_18'] = x_compute_license_state__mutmut_18 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_19'] = x_compute_license_state__mutmut_19 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_20'] = x_compute_license_state__mutmut_20 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_21'] = x_compute_license_state__mutmut_21 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_22'] = x_compute_license_state__mutmut_22 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_23'] = x_compute_license_state__mutmut_23 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_24'] = x_compute_license_state__mutmut_24 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_25'] = x_compute_license_state__mutmut_25 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_26'] = x_compute_license_state__mutmut_26 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_27'] = x_compute_license_state__mutmut_27 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_28'] = x_compute_license_state__mutmut_28 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_29'] = x_compute_license_state__mutmut_29 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_30'] = x_compute_license_state__mutmut_30 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_31'] = x_compute_license_state__mutmut_31 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_32'] = x_compute_license_state__mutmut_32 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_33'] = x_compute_license_state__mutmut_33 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_34'] = x_compute_license_state__mutmut_34 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_35'] = x_compute_license_state__mutmut_35 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_36'] = x_compute_license_state__mutmut_36 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_37'] = x_compute_license_state__mutmut_37 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_38'] = x_compute_license_state__mutmut_38 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_39'] = x_compute_license_state__mutmut_39 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_40'] = x_compute_license_state__mutmut_40 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_41'] = x_compute_license_state__mutmut_41 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_42'] = x_compute_license_state__mutmut_42 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_43'] = x_compute_license_state__mutmut_43 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_44'] = x_compute_license_state__mutmut_44 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_45'] = x_compute_license_state__mutmut_45 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_46'] = x_compute_license_state__mutmut_46 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_47'] = x_compute_license_state__mutmut_47 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_48'] = x_compute_license_state__mutmut_48 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_49'] = x_compute_license_state__mutmut_49 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_50'] = x_compute_license_state__mutmut_50 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_51'] = x_compute_license_state__mutmut_51 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_52'] = x_compute_license_state__mutmut_52 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_53'] = x_compute_license_state__mutmut_53 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_54'] = x_compute_license_state__mutmut_54 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_55'] = x_compute_license_state__mutmut_55 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_56'] = x_compute_license_state__mutmut_56 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_57'] = x_compute_license_state__mutmut_57 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_58'] = x_compute_license_state__mutmut_58 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_59'] = x_compute_license_state__mutmut_59 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_60'] = x_compute_license_state__mutmut_60 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_61'] = x_compute_license_state__mutmut_61 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_62'] = x_compute_license_state__mutmut_62 # type: ignore # mutmut generated
mutants_x_compute_license_state__mutmut['x_compute_license_state__mutmut_63'] = x_compute_license_state__mutmut_63 # type: ignore # mutmut generated
