import click

from hexawyn.application.use_case.get_quota_usage.command import (
    GetQuotaUsageCommand,
)
from hexawyn.application.use_case.get_quota_usage.get_quota_usage_use_case import (
    GetQuotaUsageUseCase,
)
from hexawyn.cli.presentation.quota_renderer import (
    BAR_WIDTH,
    EMPTY_CHAR,
    FILL_CHAR,
    QUOTA_RESOURCE_LABELS,
    QUOTA_STATE_ICONS,
    UPGRADE_URL,
    compute_bar_fill,
)
from hexawyn.domain.models.quota import QuotaState

TIER_LABELS: dict[str, str] = {
    "starter": "\U0001f1eb\U0001f1f7 Starter ($1/month)",
    "team": "\U0001f680 Team ($99/month)",
    "scale_up": "\U0001f680 Scale-up ($199/month)",
}

_BAR_COLORS: dict[str, str] = {
    "normal": "green",
    "warning": "yellow",
    "critical": "red",
    "exhausted": "red",
}


def _render_bar(used: int, limit: int | None, state: QuotaState) -> str:
    if state in (QuotaState.UNLIMITED,):
        return "\u221e Illimit\u00e9"
    if state == QuotaState.LOCKED:
        return ""
    if limit is None or limit <= 0:
        return ""
    filled, _ = compute_bar_fill(used, limit, BAR_WIDTH)
    color = _BAR_COLORS.get(state.value, _BAR_COLORS["normal"])
    empty_part = EMPTY_CHAR * (BAR_WIDTH - filled)
    return f"{click.style(FILL_CHAR * filled, fg=color)}{empty_part}"


def _render_line(
    label: str,
    used: int,
    limit: int | None,
    state: QuotaState,
) -> str:
    icon = QUOTA_STATE_ICONS.get(state, "")
    bar = _render_bar(used, limit, state)

    if state == QuotaState.UNLIMITED:
        extra = "\u221e Illimit\u00e9"
    elif state == QuotaState.LOCKED:
        extra = "\U0001f512 Unavailable"
    else:
        remaining = (limit or 0) - used
        extra = f"{used}/{limit}  {bar}  {remaining} remaining"

    return f"{label}: {icon}{extra}"


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

    use_case = GetQuotaUsageUseCase(plan_port=plan_adapter, usage_meter=meter_adapter)
    response = use_case.execute(GetQuotaUsageCommand())

    tier_label = _get_tier_label()

    click.echo(f"\nhexawyn Usage \u2014 {month}")
    click.echo("\u2500" * 52)
    click.echo(f"Tier          : {tier_label}")

    any_exhausted = False
    any_above_normal = False

    for quota_usage in response.quotas:
        if quota_usage.state == QuotaState.UNLIMITED:
            continue
        label = QUOTA_RESOURCE_LABELS.get(quota_usage.resource, quota_usage.resource)

        if quota_usage.state == QuotaState.EXHAUSTED:
            any_exhausted = True
        if quota_usage.state in (QuotaState.WARNING, QuotaState.CRITICAL):
            any_above_normal = True

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
        click.echo(f"\n\u274c Quota exceeded! Upgrade: {UPGRADE_URL}")
    elif any_above_normal:
        click.echo(f"\n\U0001f680 Running low on quota! Upgrade: {UPGRADE_URL}")
