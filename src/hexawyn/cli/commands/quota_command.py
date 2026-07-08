import click

from hexawyn.domain.models.quota import UNLIMITED, LicenseTier
from hexawyn.infrastructure.config.license_manager import get_license_tier
from hexawyn.infrastructure.config.quota_manager import (
    _get_current_investigation_quota,
    _get_current_month,
    _get_current_slack_quota,
    get_history_days,
)

TIER_LABELS: dict[LicenseTier, str] = {
    LicenseTier.FREE: "\U0001f1eb\U0001f1f7 Free",
    LicenseTier.DEV: "\U0001f4bb Dev ($19/month)",
    LicenseTier.STARTUP: "\U0001f680 Startup ($99/month)",
    LicenseTier.SCALE_UP: "\U0001f680 Scale-up ($199/month)",
    LicenseTier.ENTERPRISE: "\U0001f3e2 Enterprise",
}

TIER_EXCEEDED_URL = "https://hexawyn.com/pricing"

BAR_WIDTH = 20
FILL_CHAR = chr(9608)
EMPTY_CHAR = chr(9617)


def _bar(count: int, limit: int) -> str:
    filled = int((count / limit) * BAR_WIDTH)
    return f"[{FILL_CHAR * filled}{EMPTY_CHAR * (BAR_WIDTH - filled)}]"


@click.command()
def quota() -> None:
    """Show your monthly usage quota with tier-specific limits."""
    tier = get_license_tier()
    inv_quota = _get_current_investigation_quota()
    slack_quota = _get_current_slack_quota()
    history = get_history_days()
    month = _get_current_month()

    label = TIER_LABELS.get(tier, "\U0001f1eb\U0001f1f7 Free")

    click.echo(f"\nhexawyn Usage \u2014 {month}")
    click.echo("\u2500" * 38)
    click.echo(f"Tier          : {label}")

    if inv_quota.is_unlimited:
        click.echo("Investigations: Unlimited")
    else:
        click.echo(
            f"Investigations: {inv_quota.count}/{inv_quota.limit} "
            f"{_bar(inv_quota.count, inv_quota.limit)} "
            f"\u00b7 {inv_quota.remaining} remaining"
        )

    if slack_quota.is_unlimited:
        click.echo("Slack alerts  : Unlimited")
    else:
        click.echo(
            f"Slack alerts  : {slack_quota.count}/{slack_quota.limit} "
            f"{_bar(slack_quota.count, slack_quota.limit)} "
            f"\u00b7 {slack_quota.remaining} remaining"
        )

    if history == UNLIMITED:
        click.echo("History       : Unlimited")
    else:
        click.echo(f"History       : {history} days")

    click.echo("Reset         : 1st of next month")

    if inv_quota.is_exceeded or slack_quota.is_exceeded:
        click.echo(f"\n\u274c Quota exceeded! Upgrade: {TIER_EXCEEDED_URL}")
    elif not inv_quota.is_unlimited and inv_quota.remaining <= 5:
        click.echo(f"\n\u26a0\ufe0f  Running low! Upgrade: {TIER_EXCEEDED_URL}")
