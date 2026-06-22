from datetime import UTC, datetime

from hexawyn.domain.errors import QuotaExceededError, SlackQuotaExceededError
from hexawyn.domain.models.quota import (
    FREE_HISTORY_DAYS,
    FREE_MONTHLY_LIMIT,
    FREE_SLACK_LIMIT,
    PRO_HISTORY_DAYS,
    SlackQuota,
    UsageQuota,
)
from hexawyn.infrastructure.config.license_manager import is_pro
from hexawyn.infrastructure.memory.duckdb_client import get_connection
from hexawyn.infrastructure.memory.quota_repository import QuotaRepository


def _get_current_month() -> str:
    return datetime.now(UTC).strftime("%Y-%m")


def _get_current_investigation_quota() -> UsageQuota:
    conn = get_connection()
    repo = QuotaRepository(conn=conn)
    return repo.get_investigation_quota(month=_get_current_month())


def _get_current_slack_quota() -> SlackQuota:
    conn = get_connection()
    repo = QuotaRepository(conn=conn)
    return repo.get_slack_quota(month=_get_current_month())


def _increment_investigation() -> None:
    conn = get_connection()
    repo = QuotaRepository(conn=conn)
    repo.increment_investigation(month=_get_current_month(), limit=FREE_MONTHLY_LIMIT)


def _increment_slack() -> None:
    conn = get_connection()
    repo = QuotaRepository(conn=conn)
    repo.increment_slack(month=_get_current_month(), limit=FREE_SLACK_LIMIT)


def check_quota() -> None:
    """
    Check if the user has remaining investigations this month.

    Called by: LangGraph parse_intent node (BEFORE any tool call).
    Demo mode: caller must skip this — demo never counts against quota.

    Raises:
        QuotaExceededError: if Free tier limit of 50 investigations/month is reached.
    Does nothing if Pro tier (unlimited).
    """
    quota = _get_current_investigation_quota()
    if quota.is_exceeded:
        raise QuotaExceededError(used=quota.count, limit=quota.limit)


def check_slack_quota() -> None:
    """
    Check if the user has remaining Slack alerts this month.

    Called by: Slack alert adapter (BEFORE sending a Slack message).
    Free tier: 5 Slack alerts/month.
    Pro tier: unlimited.

    Raises:
        SlackQuotaExceededError: if Free tier Slack limit is reached.
    """
    quota = _get_current_slack_quota()
    if quota.is_exceeded:
        raise SlackQuotaExceededError(used=quota.count, limit=quota.limit)


def increment_quota() -> None:
    """
    Increment investigation count after a successful investigation.

    Called by: LangGraph store_memory node (AFTER successful investigation).
    Demo mode: caller must skip this — demo never counts against quota.
    """
    _increment_investigation()


def increment_slack_quota() -> None:
    """
    Increment Slack alert count after a Slack alert is sent.

    Called by: Slack alert adapter (AFTER successfully sending alert).
    """
    _increment_slack()


def get_history_days() -> int:
    """
    Returns the number of days of DuckDB history available for VSS search.

    Free tier → 7 days  (users see recent incidents only)
    Pro tier  → 90 days (full history available)

    Called by: duckdb_client.search_similar() to set the timestamp filter.
    """
    return PRO_HISTORY_DAYS if is_pro() else FREE_HISTORY_DAYS


def get_quota_display() -> str:
    """
    Returns a human-readable quota status for CLI display.
    Shown after every investigation response in the chat view.

    Examples:
        Free:     "[23/50 free investigations · 27 remaining]"
        Low:      "[46/50 free investigations · ⚠️ 4 remaining]"
        Pro:      "[⭐ Pro — unlimited investigations]"
    """
    quota = _get_current_investigation_quota()

    if quota.is_unlimited:
        return "[\u2b50 Pro \u2014 unlimited investigations]"

    warning = " \u26a0\ufe0f" if quota.remaining <= 5 else ""
    return (
        f"[{quota.count}/{quota.limit} free investigations"
        f" \u00b7 {quota.remaining} remaining{warning}]"
    )
