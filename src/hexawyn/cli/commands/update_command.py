"""hexa update / hexa version — check for and report hexawyn updates."""

from __future__ import annotations

import click

from hexawyn.adapters.secondary.pypi.pypi_version_adapter import PyPIVersionAdapter
from hexawyn.application.service.version_check_service import check_for_update
from hexawyn.cli.presentation.feedback import fail, ok, spinner, success
from hexawyn.domain.models.constants import VERSION


@click.command()
def version() -> None:
    """Show the installed hexawyn version."""
    click.echo(f"hexawyn {VERSION}")


@click.command()
def update() -> None:
    """Check for a newer hexawyn release on PyPI."""
    with spinner("Checking for updates on PyPI"):
        result = check_for_update(VERSION, PyPIVersionAdapter())

    if result.status == "update_available":
        click.echo(f"  ⚠️  Update available: {result.current_version} → {result.latest_version}")
        click.echo("  ⏩ Run: pip install --upgrade hexawyn")
        click.echo("  📦   (or: pipx upgrade hexawyn if installed via pipx)")
        return

    if result.status == "up_to_date":
        ok(f"hexawyn {result.current_version} is up to date")
        success("Nothing to do — enjoy your day!")
        return

    fail(f"Could not check for updates: {result.error}")
