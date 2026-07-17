import click

from hexawyn.application.ports.driving.get_quota_usage.get_quota_usage_command import (
    GetQuotaUsageCommand,
)
from hexawyn.application.service.get_quota_usage_service import GetQuotaUsageService
from hexawyn.application.use_case.get_quota_usage.get_quota_usage_use_case import (
    GetQuotaUsageUseCase,
)
from hexawyn.domain.models.quota import QuotaState

TIER_LABELS: dict[str, str] = {
    "starter": "\U0001f1eb\U0001f1f7 Starter ($1/month)",
    "team": "\U0001f680 Team ($99/month)",
    "scale_up": "\U0001f680 Scale-up ($199/month)",
}

RESOURCE_LABELS: dict[str, str] = {
    "investigations": "Investigations",
    "slack_alerts": "Slack alerts  ",
}

TIER_EXCEEDED_URL = "https://hexawyn.com/pricing"

BAR_WIDTH = 20
FILL_CHAR = chr(9608)
EMPTY_CHAR = chr(9617)


def _state_color(state: QuotaState) -> str:
    return {
        QuotaState.NORMAL: "",
        QuotaState.WARNING: "\u26a0\ufe0f ",
        QuotaState.CRITICAL: "\U0001f534 ",
        QuotaState.EXHAUSTED: "\u274c ",
        QuotaState.UNLIMITED: "",
        QuotaState.LOCKED: "\U0001f512 ",
    }.get(state, "")


def _render_bar(used: int, limit: int | None, state: QuotaState) -> str:
    if state in (QuotaState.UNLIMITED,):
        return "\u221e Illimit\u00e9"
    if state == QuotaState.LOCKED:
        return ""
    if limit is None or limit <= 0:
        return ""
    pct = min(100.0, (used / limit) * 100)
    filled = int((pct / 100.0) * BAR_WIDTH)
    return f"[{FILL_CHAR * filled}{EMPTY_CHAR * (BAR_WIDTH - filled)}]"


def _render_line(
    label: str,
    used: int,
    limit: int | None,
    state: QuotaState,
) -> str:
    color = _state_color(state)
    bar = _render_bar(used, limit, state)

    if state == QuotaState.UNLIMITED:
        extra = "\u221e Illimit\u00e9"
    elif state == QuotaState.LOCKED:
        extra = "\U0001f512 Unavailable"
    else:
        remaining = (limit or 0) - used
        extra = f"{used}/{limit}  {bar}  {remaining} remaining"

    return f"{label}: {color}{extra}"


def _get_tier_label() -> str:
    try:
        from hexawyn.infrastructure.config.license_manager import get_license_tier

        tier = get_license_tier()
        return TIER_LABELS.get(tier.value, TIER_LABELS["starter"])
    except ImportError:
        return TIER_LABELS["starter"]


@click.command()
def quota() -> None:
    """Show your monthly usage quota per resource with progress bars."""
    from hexawyn.adapters.secondary.pricing_plan_adapter import PricingPlanAdapter
    from hexawyn.adapters.secondary.usage_meter_adapter import UsageMeterAdapter

    plan_adapter = PricingPlanAdapter()
    meter_adapter = UsageMeterAdapter()

    from hexawyn.infrastructure.config.quota_manager import (
        _get_current_investigation_quota,
        _get_current_month,
        _get_current_slack_quota,
    )

    inv_quota = _get_current_investigation_quota()
    slack_quota = _get_current_slack_quota()
    month = _get_current_month()

    meter_adapter.set_usage("investigations", inv_quota.count)
    meter_adapter.set_usage("slack_alerts", slack_quota.count)

    service = GetQuotaUsageService(
        plan_port=plan_adapter,
        usage_meter=meter_adapter,
    )
    use_case = GetQuotaUsageUseCase(service=service)
    response = use_case.execute(GetQuotaUsageCommand())

    tier_label = _get_tier_label()

    click.echo(f"\nhexawyn Usage \u2014 {month}")
    click.echo("\u2500" * 52)
    click.echo(f"Tier          : {tier_label}")

    any_exhausted = False
    any_critical = False

    for quota_usage in response.quotas:
        label = RESOURCE_LABELS.get(quota_usage.resource, quota_usage.resource)

        if quota_usage.state == QuotaState.EXHAUSTED:
            any_exhausted = True
        if quota_usage.state == QuotaState.CRITICAL:
            any_critical = True

        click.echo(
            _render_line(
                label=label,
                used=quota_usage.used,
                limit=quota_usage.limit,
                state=quota_usage.state,
            )
        )

    from hexawyn.infrastructure.config.quota_manager import get_history_days

    history_days = get_history_days()
    if history_days == -1:
        click.echo("History       : \u221e Unlimited")
    else:
        click.echo(f"History       : {history_days} days")

    click.echo("Reset         : 1st of next month")

    if any_exhausted:
        click.echo(f"\n\u274c Quota exceeded! Upgrade: {TIER_EXCEEDED_URL}")
    elif any_critical:
        click.echo(f"\n\U0001f534 Running low on quota! Upgrade: {TIER_EXCEEDED_URL}")
