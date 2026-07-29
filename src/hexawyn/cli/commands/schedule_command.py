"""CLI commands: hexawyn schedule — create, list, manage scheduled checks."""

from __future__ import annotations

import json

import click

from hexawyn.domain.models.schedule import CronCheck
from hexawyn.domain.services.schedule.cron_shortcut import cron_to_minutes, shortcut_to_cron
from hexawyn.infrastructure.config.schedule_registry import build_registry


@click.group()
def schedule() -> None:
    """Manage scheduled recurring audits (cron-based)."""


@schedule.command()
@click.option("--name", required=True, help="Unique check name")
@click.option("--use-case", "use_case", required=True, help="Use case / tool to run")
@click.option("--every", default=None, help="Shortcut: 15m, 30m, 1h, 6h, 12h, 24h")
@click.option("--cron", default=None, help="Full cron expression (takes precedence over --every)")
@click.option("--namespace", default=None, help="Namespace filter")
@click.option(
    "--notify",
    "notify_policy",
    default="on_change",
    type=click.Choice(["always", "on_change", "on_failure"]),
)
@click.option(
    "--alert", "destinations_str", default="slack", help="Alert destinations (comma-separated)"
)
def create(  # noqa: PLR0913
    name: str,
    use_case: str,
    every: str | None,
    cron: str | None,
    namespace: str | None,
    notify_policy: str,
    destinations_str: str,
) -> None:
    """Create a new scheduled check."""
    cron_expr = cron or shortcut_to_cron(every or "24h")
    if cron_expr is None:
        click.echo(
            f"❌ Invalid schedule: '{every or cron}'. Use --every 6h or --cron '0 */6 * * *'.",
            err=True,
        )
        return

    params: dict[str, str] = {}
    if namespace:
        params["namespace"] = namespace

    check = CronCheck(
        name=name,
        schedule=cron_expr,
        use_case=use_case,
        params=params,
        notify_policy=notify_policy,
        destinations=[d.strip() for d in destinations_str.split(",")],
    )

    from hexawyn.infrastructure.config.schedule_source import YamlScheduleSource

    source = YamlScheduleSource()
    existing = source.load_checks()
    existing = [c for c in existing if c.name != name]
    existing.append(check)
    source.save_checks(existing)

    click.echo(f"✅ Check '{name}' created — runs {use_case} on {cron_expr}")
    click.echo(f"   Notify: {notify_policy} → {destinations_str}")


@schedule.command()
def list() -> None:
    """List all scheduled checks."""
    from hexawyn.infrastructure.config.schedule_source import YamlScheduleSource

    source = YamlScheduleSource()
    checks = source.load_checks()

    if not checks:
        click.echo(
            "No scheduled checks. Create one with: hexawyn schedule create --name X --use-case Y --every 6h"  # noqa: E501
        )
        return

    click.echo(f"{'NAME':<30} {'SCHEDULE':<20} {'USE_CASE':<25} {'ENABLED':<8} {'NOTIFY':<12}")
    click.echo("-" * 95)
    for check in checks:
        enabled = "✅" if check.enabled else "❌"
        click.echo(
            f"{check.name:<30} {check.schedule:<20} {check.use_case:<25} {enabled:<8} {check.notify_policy:<12}"  # noqa: E501
        )


@schedule.command()
@click.argument("name")
def get(name: str) -> None:
    """Show details of a scheduled check."""
    from hexawyn.infrastructure.config.schedule_source import YamlScheduleSource

    source = YamlScheduleSource()
    for check in source.load_checks():
        if check.name == name:
            click.echo(f"Name:       {check.name}")
            click.echo(f"Use case:   {check.use_case}")
            click.echo(f"Schedule:   {check.schedule}")
            click.echo(f"Params:     {json.dumps(check.params)}")
            click.echo(f"Enabled:    {check.enabled}")
            click.echo(f"Notify:     {check.notify_policy}")
            click.echo(f"Alerts:     {', '.join(check.destinations)}")
            click.echo(f"Timeout:    {check.timeout_seconds}s")
            return
    click.echo(f"❌ Check '{name}' not found.", err=True)


@schedule.command()
@click.argument("name")
@click.option("--limit", default=10, help="Number of results to show")
def history(name: str, limit: int) -> None:
    """Show execution history for a check."""
    from hexawyn.domain.services.schedule.duckdb_schedule_store import DuckDBScheduleStore
    from hexawyn.infrastructure.memory.duckdb_client import get_connection

    store = DuckDBScheduleStore(connection=get_connection())
    results = store.history(name, limit=limit)

    if not results:
        click.echo(f"No history for '{name}'. Run it first with: hexawyn schedule run {name}")
        return

    for result in results:
        icon = "🔔" if result.changed else "✅"
        click.echo(
            f"{icon} [{result.phase}] {result.started_at.isoformat()[:19]} — {result.summary}"
        )


@schedule.command()
def status() -> None:
    """Show scheduler overview."""
    from hexawyn.infrastructure.config.schedule_source import YamlScheduleSource

    source = YamlScheduleSource()
    checks = source.load_checks()
    enabled = [c for c in checks if c.enabled]

    click.echo(f"Total checks:     {len(checks)}")
    click.echo(f"Enabled:          {len(enabled)}")
    click.echo(f"Disabled:         {len(checks) - len(enabled)}")


@schedule.command()
@click.argument("name")
def enable(name: str) -> None:
    """Enable a scheduled check."""
    _toggle(name, enabled=True)


@schedule.command()
@click.argument("name")
def disable(name: str) -> None:
    """Disable a scheduled check (without deleting it)."""
    _toggle(name, enabled=False)


def _toggle(name: str, enabled: bool) -> None:
    from hexawyn.infrastructure.config.schedule_source import YamlScheduleSource

    source = YamlScheduleSource()
    checks = source.load_checks()
    found = False
    for check in checks:
        if check.name == name:
            check.enabled = enabled
            found = True
            break
    if not found:
        click.echo(f"❌ Check '{name}' not found.", err=True)
        return
    source.save_checks(checks)
    state = "enabled" if enabled else "disabled"
    click.echo(f"✅ Check '{name}' {state}.")


@schedule.command()
@click.argument("name")
def delete(name: str) -> None:
    """Delete a scheduled check."""
    from hexawyn.infrastructure.config.schedule_source import YamlScheduleSource

    source = YamlScheduleSource()
    checks = [c for c in source.load_checks() if c.name != name]
    source.save_checks(checks)

    from hexawyn.domain.services.schedule.duckdb_schedule_store import DuckDBScheduleStore
    from hexawyn.infrastructure.memory.duckdb_client import get_connection

    DuckDBScheduleStore(connection=get_connection()).delete_check(name)

    click.echo(f"✅ Check '{name}' deleted.")


@schedule.command()
@click.argument("name")
def run(name: str) -> None:
    """Run a scheduled check immediately (outside cron)."""
    from hexawyn.domain.services.schedule.alert_history import AlertHistoryDecorator
    from hexawyn.domain.services.schedule.check_runner import CheckRunnerUseCase
    from hexawyn.domain.services.schedule.duckdb_schedule_store import DuckDBScheduleStore
    from hexawyn.infrastructure.config.schedule_source import YamlScheduleSource
    from hexawyn.infrastructure.memory.duckdb_client import get_connection

    source = YamlScheduleSource()
    check = None
    for c in source.load_checks():
        if c.name == name:
            check = c
            break
    if check is None:
        click.echo(f"❌ Check '{name}' not found.", err=True)
        return

    conn = get_connection()
    store = DuckDBScheduleStore(connection=conn)

    from hexawyn.adapters.secondary.slack.slack_alert_adapter import SlackAlertAdapter

    alert_port = AlertHistoryDecorator(SlackAlertAdapter(), connection=conn)

    runner = CheckRunnerUseCase(
        store=store,
        alert_port=alert_port,
        use_case_registry=build_registry(),
    )

    result = runner.execute(check)
    icon = "🔔" if result.changed else "✅"
    click.echo(f"{icon} [{result.phase}] {result.summary}")
    if result.error_message:
        click.echo(f"   Error: {result.error_message}")


@schedule.command()
@click.option("--dry-run", is_flag=True, help="Show next runs without starting")
def start(dry_run: bool) -> None:  # noqa: C901
    """Start the scheduler (long-running, native Python loop)."""
    import os
    import time
    from datetime import UTC, datetime

    if os.environ.get("HEXAWYN_SCHEDULER_ENABLED", "false").lower() != "true":
        click.echo(
            "⚠️  HEXAWYN_SCHEDULER_ENABLED=false. Set to 'true' to start the scheduler.", err=True
        )
        return

    from hexawyn.domain.services.schedule.check_runner import CheckRunnerUseCase
    from hexawyn.domain.services.schedule.duckdb_schedule_store import DuckDBScheduleStore
    from hexawyn.infrastructure.config.schedule_source import YamlScheduleSource
    from hexawyn.infrastructure.memory.duckdb_client import get_connection

    source = YamlScheduleSource()
    checks = [c for c in source.load_checks() if c.enabled]

    if not checks:
        click.echo("No enabled checks. Create one first.")
        return

    if dry_run:
        click.echo("Dry-run — checks that would be executed:")
        for check in checks:
            interval = cron_to_minutes(check.schedule)
            click.echo(f"  {check.name}: every ~{interval}min → {check.use_case}")
        return

    store = DuckDBScheduleStore(connection=get_connection())
    from hexawyn.adapters.secondary.slack.slack_alert_adapter import SlackAlertAdapter
    from hexawyn.domain.services.schedule.alert_history import AlertHistoryDecorator

    alert_port = AlertHistoryDecorator(SlackAlertAdapter(), connection=get_connection())

    runner = CheckRunnerUseCase(
        store=store,
        alert_port=alert_port,
        use_case_registry=build_registry(),
    )

    last_run: dict[str, datetime] = {c.name: datetime.now(UTC) for c in checks}
    click.echo(
        f"Scheduler started — {len(checks)} checks, polling every 60s. Press Ctrl+C to stop."
    )
    click.echo(f"{'CHECK':<25} {'INTERVAL':<10} {'NEXT RUN':<20}")
    for check in checks:
        interval = cron_to_minutes(check.schedule)
        click.echo(f"{check.name:<25} ~{interval}min     in ~{interval}min")

    try:
        while True:
            now = datetime.now(UTC)
            for check in checks:
                interval = cron_to_minutes(check.schedule)
                if interval <= 0:
                    continue
                elapsed = (now - last_run[check.name]).total_seconds() / 60
                if elapsed >= interval:
                    result = runner.execute(check)
                    last_run[check.name] = now
                    icon = "🔔" if result.changed else "✅"
                    click.echo(f"{icon} [{now.strftime('%H:%M:%S')}] {check.name}: {result.phase}")
            time.sleep(60)
    except KeyboardInterrupt:
        click.echo("\nScheduler stopped.")
