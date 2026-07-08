from dataclasses import dataclass
from enum import Enum

UNLIMITED = -1  # sentinel: no limit


class LicenseTier(Enum):
    FREE = "free"
    DEV = "dev"
    STARTUP = "startup"
    SCALE_UP = "scale_up"
    ENTERPRISE = "enterprise"


# ── Investigation limits ───────────────────────────────────
_INVESTIGATION_LIMITS: dict[LicenseTier, int] = {
    LicenseTier.FREE: 50,
    LicenseTier.DEV: 200,
    LicenseTier.STARTUP: 500,
    LicenseTier.SCALE_UP: UNLIMITED,
    LicenseTier.ENTERPRISE: UNLIMITED,
}

# ── Slack alert limits ─────────────────────────────────────
_SLACK_LIMITS: dict[LicenseTier, int] = {
    LicenseTier.FREE: 5,
    LicenseTier.DEV: 50,
    LicenseTier.STARTUP: UNLIMITED,
    LicenseTier.SCALE_UP: UNLIMITED,
    LicenseTier.ENTERPRISE: UNLIMITED,
}

# ── DuckDB history days ────────────────────────────────────
_HISTORY_DAYS: dict[LicenseTier, int] = {
    LicenseTier.FREE: 7,
    LicenseTier.DEV: 30,
    LicenseTier.STARTUP: 90,
    LicenseTier.SCALE_UP: UNLIMITED,
    LicenseTier.ENTERPRISE: UNLIMITED,
}


def get_investigation_limit(tier: LicenseTier) -> int:
    return _INVESTIGATION_LIMITS[tier]


def get_slack_limit(tier: LicenseTier) -> int:
    return _SLACK_LIMITS[tier]


def get_history_days(tier: LicenseTier) -> int:
    return _HISTORY_DAYS[tier]


# ── Backward-compatible constants ──────────────────────────
FREE_MONTHLY_LIMIT = get_investigation_limit(LicenseTier.FREE)
FREE_SLACK_LIMIT = get_slack_limit(LicenseTier.FREE)
FREE_HISTORY_DAYS = get_history_days(LicenseTier.FREE)
PRO_HISTORY_DAYS = 90  # kept for backward compat (Startup/Scale-up/Enterprise)


@dataclass
class UsageQuota:
    """
    Monthly investigation usage.
    Limit depends on license tier:
    Free=50 / Dev=200 / Startup=500 / Scale-up=unlimited / Enterprise=unlimited
    """

    month: str
    count: int
    limit: int = FREE_MONTHLY_LIMIT

    @property
    def remaining(self) -> int:
        if self.limit == UNLIMITED:
            return UNLIMITED
        return max(0, self.limit - self.count)

    @property
    def is_exceeded(self) -> bool:
        if self.limit == UNLIMITED:
            return False
        return self.count >= self.limit

    @property
    def is_unlimited(self) -> bool:
        return self.limit == UNLIMITED


@dataclass
class SlackQuota:
    """
    Monthly Slack alert usage.
    Limit depends on license tier:
    Free=5 / Dev=50 / Startup=unlimited / Scale-up=unlimited / Enterprise=unlimited
    """

    month: str
    count: int
    limit: int = FREE_SLACK_LIMIT

    @property
    def remaining(self) -> int:
        if self.limit == UNLIMITED:
            return UNLIMITED
        return max(0, self.limit - self.count)

    @property
    def is_exceeded(self) -> bool:
        if self.limit == UNLIMITED:
            return False
        return self.count >= self.limit

    @property
    def is_unlimited(self) -> bool:
        return self.limit == UNLIMITED
