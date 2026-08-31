from dataclasses import dataclass
from enum import Enum

UNLIMITED = -1  # sentinel: no limit

QUOTA_RESOURCES = [
    "investigations",
    "slack_alerts",
    "slack_channels",
    "clusters",
    "users",
    "billing_api",
]


class LicenseTier(Enum):
    """Plan label only — NO per-tier numeric limits live here.

    Tier -> limit is owned by the control plane (``/api/v1/quota``); the public
    client never hardcodes business figures.
    """

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
        if pct >= 90:  # noqa: PLR2004
            return QuotaState.CRITICAL
        if pct >= 80:  # noqa: PLR2004
            return QuotaState.WARNING
        return QuotaState.NORMAL


@dataclass
class UsageQuota:
    """Monthly investigation usage.

    The ``limit`` is streamed from the control plane (or its encrypted cache).
    When neither is available it defaults to ``UNLIMITED`` (= neutral / not
    locally constrained) because the public client never fabricates a number.
    """

    month: str
    count: int
    limit: int = UNLIMITED

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
    """Monthly Slack alert usage.

    Counted locally; the limit is ``UNLIMITED`` until the control plane exposes
    a real server-side slack quota (follow-up). No hardcoded figure here.
    """

    month: str
    count: int
    limit: int = UNLIMITED

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
