import click

from hexawyn.infrastructure.config.quota_manager import (
    _get_current_investigation_quota,
    _get_current_month,
    _get_current_slack_quota,
    get_history_days,
)


@click.command()
def quota() -> None:
    """Show your monthly usage quota."""
    inv_quota = _get_current_investigation_quota()
    slack_quota = _get_current_slack_quota()
    history = get_history_days()
    month = _get_current_month()

    click.echo(f"\nhexawyn Usage — {month}")
    click.echo("──────────────────────────────────")

    if inv_quota.is_unlimited:
        click.echo("Tier          : \u2b50 Pro")
        click.echo("Investigations: Unlimited")
        click.echo("Slack alerts  : Unlimited")
        click.echo("History       : 90 days")
    else:
        bar_inv = int((inv_quota.count / inv_quota.limit) * 20)
        bar_slack = int((slack_quota.count / slack_quota.limit) * 20)

        click.echo("Tier          : \U0001f1eb\U0001f1f7 Free")
        click.echo(
            f"Investigations: {inv_quota.count}/{inv_quota.limit} "
            f"[{chr(9608) * bar_inv}{chr(9617) * (20 - bar_inv)}] "
            f"\u00b7 {inv_quota.remaining} remaining"
        )
        click.echo(
            f"Slack alerts  : {slack_quota.count}/{slack_quota.limit} "
            f"[{chr(9608) * bar_slack}{chr(9617) * (20 - bar_slack)}] "
            f"\u00b7 {slack_quota.remaining} remaining"
        )
        click.echo(f"History       : {history} days")
        click.echo("Reset         : 1st of next month")

        if inv_quota.is_exceeded or slack_quota.is_exceeded:
            click.echo("\n\u274c Quota exceeded!")
            click.echo("Upgrade to Pro: https://hexawyn.com/pro")
        elif inv_quota.remaining <= 5:
            click.echo("\n\u26a0\ufe0f  Running low on investigations!")
            click.echo("Upgrade to Pro: https://hexawyn.com/pro")
