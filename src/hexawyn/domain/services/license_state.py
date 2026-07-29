from dataclasses import dataclass
from datetime import UTC, datetime

from hexawyn.domain.models.license import LicenseClaims


@dataclass(frozen=True)
class LicenseState:
    state: str
    plan: str
    days_remaining: int
    expiry_date: str


def compute_license_state(claims: LicenseClaims) -> LicenseState:
    exp_timestamp = claims.exp
    if isinstance(exp_timestamp, str):
        exp_timestamp = int(exp_timestamp)

    expiry_dt = datetime.fromtimestamp(exp_timestamp, tz=UTC)
    now = datetime.now(UTC)
    days_remaining = (expiry_dt - now).days
    expiry_date = expiry_dt.strftime("%d %b %Y")

    if days_remaining <= 0:
        return LicenseState(
            state="expired",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    if days_remaining <= 7:  # noqa: PLR2004
        return LicenseState(
            state="warning",
            plan=claims.plan,
            days_remaining=days_remaining,
            expiry_date=expiry_date,
        )
    return LicenseState(
        state="active", plan=claims.plan, days_remaining=days_remaining, expiry_date=expiry_date
    )
