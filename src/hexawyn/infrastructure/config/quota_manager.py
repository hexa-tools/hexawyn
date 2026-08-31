from datetime import UTC, datetime

from hexawyn.application.ports.driven.quota_port import QuotaStorePort
from hexawyn.domain.errors import QuotaExceededError, SlackQuotaExceededError
from hexawyn.domain.models.quota import (
    UNLIMITED,
    LicenseTier,
    SlackQuota,
    UsageQuota,
)
from hexawyn.infrastructure.config import quota_cache

_store: QuotaStorePort | None = None


def _get_store() -> QuotaStorePort:
    """Lazily initialize the quota store (defaults to DuckDB-backed QuotaRepository)."""
    global _store
    if _store is None:
        from hexawyn.infrastructure.memory.duckdb_client import get_connection
        from hexawyn.infrastructure.memory.quota_repository import QuotaRepository

        _store = QuotaRepository(conn=get_connection())
    return _store


def inject_quota_store(store: QuotaStorePort) -> None:
    """Inject a custom QuotaStorePort implementation (for testing)."""
    global _store
    _store = store


def _get_current_month() -> str:
    return datetime.now(UTC).strftime("%Y-%m")


def _get_current_tier() -> LicenseTier:
    """
    Get current license tier from license_manager.
    Returns LicenseTier.STARTER if no valid license found.
    Import is deferred to avoid circular dependency with license_manager.
    """
    try:
        from hexawyn.infrastructure.config.license_manager import get_license_tier

        return get_license_tier()
    except ImportError:
        return LicenseTier.STARTER


def _local_investigation_limit() -> int:
    """Investigation limit from the encrypted CP cache, else neutral (UNLIMITED)."""
    cached = quota_cache.load_quota()
    if cached is not None:
        return int(cached["limit"])
    return UNLIMITED


def _get_current_investigation_quota() -> UsageQuota:
    return _get_store().get_investigation_quota(month=_get_current_month())


def _get_current_slack_quota() -> SlackQuota:
    return _get_store().get_slack_quota(month=_get_current_month())


def _increment_investigation() -> None:
    tier = _get_current_tier()
    limit = _local_investigation_limit()
    _get_store().increment_investigation(
        month=_get_current_month(),
        tier=tier,
        limit=limit,
    )


def _increment_slack() -> None:
    # (ii) Slack is counted-but-unlimited locally; real limit is a CP follow-up.
    tier = _get_current_tier()
    _get_store().increment_slack(
        month=_get_current_month(),
        tier=tier,
        limit=UNLIMITED,
    )


def check_quota() -> None:
    """Check investigation quota before starting LangGraph pipeline.

    The limit is streamed from the control plane (or its cache). When unknown
    (neutral), the quota is not locally constrained and this does not block —
    the control plane re-enforces on the next sync. Demo mode: caller must
    skip this.
    """
    quota = _get_current_investigation_quota()
    if quota.is_exceeded:
        raise QuotaExceededError(used=quota.count, limit=quota.limit)


def check_slack_quota() -> None:
    """Check Slack alert quota before sending.

    Slack is counted-but-unlimited locally until the control plane exposes a
    real limit, so this does not block on a fabricated number.
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

    Neutral by design: no hardcoded tiered figure. When the control plane does
    not supply a retention window, the client does not fabricate one — it keeps
    the full window (unlimited).
    """
    return UNLIMITED


def get_quota_display() -> str:
    """
    Display string shown in CLI after each investigation.

    When the quota is neutral (UNKNOWN / unlimited locally) this reports the
    plan label without fabricating a numeric usage figure.
    """
    tier = _get_current_tier()
    quota = _get_current_investigation_quota()

    tier_labels: dict[LicenseTier, str] = {
        LicenseTier.STARTER: "Starter",
        LicenseTier.TEAM: "Team",
        LicenseTier.SCALE_UP: "Scale-up",
    }
    label = tier_labels.get(tier, "Starter")

    if quota.is_unlimited:
        return f"[\u2b50 {label} \u2014 unlimited investigations]"

    warning = " \u26a0\ufe0f" if quota.remaining <= 5 else ""  # noqa: PLR2004
    return (
        f"[{quota.count}/{quota.limit} {label} investigations"
        f" \u00b7 {quota.remaining} remaining{warning}]"
    )
