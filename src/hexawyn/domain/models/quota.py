from dataclasses import dataclass

# ── Constants ─────────────────────────────────────────────
FREE_MONTHLY_LIMIT = 50  # investigations/month on Free tier
FREE_SLACK_LIMIT = 5  # Slack alerts/month on Free tier
FREE_HISTORY_DAYS = 7  # days of DuckDB history on Free tier
PRO_HISTORY_DAYS = 90  # days of DuckDB history on Pro tier
UNLIMITED = -1  # sentinel value for Pro tier (no limit)


@dataclass
class UsageQuota:
    """
    Tracks monthly investigation usage for a hexawyn installation.
    Free tier: 50 investigations/month.
    Pro tier: unlimited (limit=-1).

    Used by:
    - quota_manager.check_quota() → raises QuotaExceededError if exceeded
    - quota_manager.get_quota_display() → shows [23/50 · 27 remaining] in CLI
    """

    month: str  # "2026-06" — YYYY-MM format
    count: int  # number of investigations used this month
    limit: int = FREE_MONTHLY_LIMIT  # 50 Free / -1 Pro

    @property
    def remaining(self) -> int:
        """Remaining investigations this month. Returns UNLIMITED (-1) for Pro."""
        if self.limit == UNLIMITED:
            return UNLIMITED
        return max(0, self.limit - self.count)

    @property
    def is_exceeded(self) -> bool:
        """True if the user has reached their monthly limit."""
        if self.limit == UNLIMITED:
            return False
        return self.count >= self.limit

    @property
    def is_unlimited(self) -> bool:
        """True for Pro tier (limit=-1)."""
        return self.limit == UNLIMITED


@dataclass
class SlackQuota:
    """
    Tracks monthly Slack alert usage for a hexawyn installation.
    Free tier: 5 Slack alerts/month.
    Pro tier: unlimited (limit=-1).

    Used by:
    - quota_manager.check_slack_quota() → raises SlackQuotaExceededError
    - Slack alert adapter → checks before sending
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
