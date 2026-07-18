from dataclasses import dataclass
from enum import Enum

UNLIMITED = -1  # sentinel: no limit


class LicenseTier(Enum):
    STARTER = "starter"
    TEAM = "team"
    SCALE_UP = "scale_up"


class QuotaState(Enum):
    NORMAL = "normal"
    WARNING = "warning"
    CRITICAL = "critical"
    EXHAUSTED = "exhausted"
    UNLIMITED = "unlimited"
    LOCKED = "locked"


@dataclass(frozen=True)
class QuotaUsage:
    resource: str
    used: int
    limit: int | None
    state: QuotaState
    available_from_tier: str | None = None

    @property
    def percentage(self) -> float | None:
        if self.limit is None or self.limit <= 0:
            return None
        return min(100.0, (self.used / self.limit) * 100)

    @property
    def should_render_bar(self) -> bool:
        return self.state not in (QuotaState.UNLIMITED, QuotaState.LOCKED)

    @staticmethod
    def compute_state(used: int, limit: int | None) -> QuotaState:
        if limit is None or limit == UNLIMITED:
            return QuotaState.UNLIMITED
        if limit <= 0:
            return QuotaState.LOCKED
        if used >= limit:
            return QuotaState.EXHAUSTED
        pct = (used / limit) * 100
        if pct >= 90:
            return QuotaState.CRITICAL
        if pct >= 80:
            return QuotaState.WARNING
        return QuotaState.NORMAL


# ── Investigation limits ───────────────────────────────────
_INVESTIGATION_LIMITS: dict[LicenseTier, int] = {
    LicenseTier.STARTER: 200,
    LicenseTier.TEAM: 500,
    LicenseTier.SCALE_UP: UNLIMITED,
}

# ── Slack alert limits ─────────────────────────────────────
_SLACK_LIMITS: dict[LicenseTier, int] = {
    LicenseTier.STARTER: 50,
    LicenseTier.TEAM: UNLIMITED,
    LicenseTier.SCALE_UP: UNLIMITED,
}

# ── DuckDB history days ────────────────────────────────────
_HISTORY_DAYS: dict[LicenseTier, int] = {
    LicenseTier.STARTER: 30,
    LicenseTier.TEAM: 90,
    LicenseTier.SCALE_UP: UNLIMITED,
}

# ── Cluster limits ─────────────────────────────────────────
_CLUSTER_LIMITS: dict[LicenseTier, int] = {
    LicenseTier.STARTER: 1,
    LicenseTier.TEAM: 3,
    LicenseTier.SCALE_UP: UNLIMITED,
}

# ── User limits ────────────────────────────────────────────
_USER_LIMITS: dict[LicenseTier, int] = {
    LicenseTier.STARTER: 1,
    LicenseTier.TEAM: 5,
    LicenseTier.SCALE_UP: 20,
}

# ── Slack channel limits ───────────────────────────────────
_SLACK_CHANNEL_LIMITS: dict[LicenseTier, int] = {
    LicenseTier.STARTER: 1,
    LicenseTier.TEAM: 3,
    LicenseTier.SCALE_UP: UNLIMITED,
}

# ── Billing API call limits (cost tracking) ────────────────
_BILLING_API_LIMITS: dict[LicenseTier, int] = {
    LicenseTier.STARTER: 2,
    LicenseTier.TEAM: UNLIMITED,
    LicenseTier.SCALE_UP: UNLIMITED,
}


def get_investigation_limit(tier: LicenseTier) -> int:
    return _INVESTIGATION_LIMITS[tier]


def get_slack_limit(tier: LicenseTier) -> int:
    return _SLACK_LIMITS[tier]


def get_history_days(tier: LicenseTier) -> int:
    return _HISTORY_DAYS[tier]


def get_cluster_limit(tier: LicenseTier) -> int:
    return _CLUSTER_LIMITS[tier]


def get_user_limit(tier: LicenseTier) -> int:
    return _USER_LIMITS[tier]


def get_slack_channel_limit(tier: LicenseTier) -> int:
    return _SLACK_CHANNEL_LIMITS[tier]


def get_billing_api_limit(tier: LicenseTier) -> int:
    return _BILLING_API_LIMITS[tier]


# ── Backward-compatible constants ──────────────────────────
STARTER_MONTHLY_LIMIT = get_investigation_limit(LicenseTier.STARTER)
STARTER_SLACK_LIMIT = get_slack_limit(LicenseTier.STARTER)
STARTER_HISTORY_DAYS = get_history_days(LicenseTier.STARTER)
FREE_MONTHLY_LIMIT = STARTER_MONTHLY_LIMIT  # backward compat
FREE_SLACK_LIMIT = STARTER_SLACK_LIMIT  # backward compat
FREE_HISTORY_DAYS = STARTER_HISTORY_DAYS  # backward compat
PRO_HISTORY_DAYS = 90  # kept for backward compat (Team/Scale-up)


@dataclass
class UsageQuota:
    """
    Monthly investigation usage.
    Limit depends on license tier:
    Starter=50 / Team=500 / Scale-up=unlimited
    """

    month: str
    count: int
    limit: int = STARTER_MONTHLY_LIMIT

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
    Starter=5 / Team=unlimited / Scale-up=unlimited
    """

    month: str
    count: int
    limit: int = STARTER_SLACK_LIMIT

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
