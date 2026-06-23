from datetime import UTC, datetime

from hexawyn.domain.errors import QuotaExceededError, SlackQuotaExceededError
from hexawyn.domain.models.quota import (
    LicenseTier,
    SlackQuota,
    UsageQuota,
    get_investigation_limit,
    get_slack_limit,
)
from hexawyn.domain.models.quota import (
    get_history_days as _tier_history_days,
)
from hexawyn.infrastructure.memory.duckdb_client import get_connection
from hexawyn.infrastructure.memory.quota_repository import QuotaRepository


def _get_current_month() -> str:
    return datetime.now(UTC).strftime("%Y-%m")


def _get_current_tier() -> LicenseTier:
    """
    Get current license tier from license_manager.
    Returns LicenseTier.FREE if no valid license found.
    Import is deferred to avoid circular dependency with license_manager.
    """
    try:
        from hexawyn.infrastructure.config.license_manager import get_license_tier

        return get_license_tier()
    except ImportError:
        return LicenseTier.FREE


def _get_current_investigation_quota() -> UsageQuota:
    conn = get_connection()
    repo = QuotaRepository(conn=conn)
    return repo.get_investigation_quota(month=_get_current_month())


def _get_current_slack_quota() -> SlackQuota:
    conn = get_connection()
    repo = QuotaRepository(conn=conn)
    return repo.get_slack_quota(month=_get_current_month())


def _increment_investigation() -> None:
    tier = _get_current_tier()
    limit = get_investigation_limit(tier)
    conn = get_connection()
    repo = QuotaRepository(conn=conn)
    repo.increment_investigation(
        month=_get_current_month(),
        tier=tier,
        limit=limit,
    )


def _increment_slack() -> None:
    tier = _get_current_tier()
    limit = get_slack_limit(tier)
    conn = get_connection()
    repo = QuotaRepository(conn=conn)
    repo.increment_slack(
        month=_get_current_month(),
        tier=tier,
        limit=limit,
    )


def check_quota() -> None:
    """
    Check investigation quota before starting LangGraph pipeline.
    Limits: Free=50 / Dev=200 / Startup=500 / Scale-up=unlimited / Enterprise=unlimited
    Raises QuotaExceededError if limit reached.
    Demo mode: caller must skip this.
    """
    quota = _get_current_investigation_quota()
    if quota.is_exceeded:
        raise QuotaExceededError(used=quota.count, limit=quota.limit)


def check_slack_quota() -> None:
    """
    Check Slack alert quota before sending.
    Limits: Free=5 / Dev=50 / Startup=unlimited / Scale-up=unlimited / Enterprise=unlimited
    Raises SlackQuotaExceededError if limit reached.
    """
    quota = _get_current_slack_quota()
    if quota.is_exceeded:
        raise SlackQuotaExceededError(used=quota.count, limit=quota.limit)


def increment_quota() -> None:
    """Increment investigation count after successful investigation.
    Demo mode: caller must skip."""
    _increment_investigation()


def increment_slack_quota() -> None:
    """Increment Slack alert count after sending."""
    _increment_slack()


def get_history_days() -> int:
    """
    DuckDB history window for VSS search.
    Free=7 / Dev=30 / Startup=90 / Scale-up=unlimited / Enterprise=unlimited
    """
    tier = _get_current_tier()
    return _tier_history_days(tier)


def get_quota_display() -> str:
    """
    Display string shown in CLI after each investigation.
    Examples:
      Free:     "[23/50 free investigations · 27 remaining]"
      Dev:      "[45/200 Dev investigations · 155 remaining]"
      Scale-up: "[⭐ Scale-up — unlimited investigations]"
    """
    tier = _get_current_tier()
    quota = _get_current_investigation_quota()

    tier_labels: dict[LicenseTier, str] = {
        LicenseTier.FREE: "free",
        LicenseTier.DEV: "Dev",
        LicenseTier.STARTUP: "Startup",
        LicenseTier.SCALE_UP: "Scale-up",
        LicenseTier.ENTERPRISE: "Enterprise",
    }
    label = tier_labels.get(tier, "free")

    if quota.is_unlimited:
        return f"[\u2b50 {label} \u2014 unlimited investigations]"

    warning = " \u26a0\ufe0f" if quota.remaining <= 5 else ""
    return (
        f"[{quota.count}/{quota.limit} {label} investigations"
        f" \u00b7 {quota.remaining} remaining{warning}]"
    )
