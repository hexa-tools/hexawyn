"""hexa update / hexa update-check / hexa version — manage hexawyn updates."""

from __future__ import annotations

import subprocess

import click

from hexawyn.adapters.secondary.pypi.pypi_version_adapter import (
    DEFAULT_PYPI_INDEX_URL,
    PyPIVersionAdapter,
    _resolve_index_url,
)
from hexawyn.application.service.version_check_service import check_for_update
from hexawyn.cli.commands.uninstall_command import _detect_installer
from hexawyn.cli.presentation.feedback import fail, ok, spinner, success
from hexawyn.domain.models.constants import VERSION


def resolve_install_index() -> dict[str, list[str]]:
    """Build pip index arguments from the resolved source index.

    When running against TestPyPI (dev), pip needs the TestPyPI index for the
    package itself plus the real PyPI index for dependencies. The production
    index needs no extra arguments.
    """
    index_url = _resolve_index_url()
    if index_url == DEFAULT_PYPI_INDEX_URL:
        return {"index_args": []}
    return {
        "index_args": [
            "--index-url",
            f"{index_url}/simple/",
            "--extra-index-url",
            f"{DEFAULT_PYPI_INDEX_URL}/simple/",
        ]
    }


@click.command()
def version() -> None:
    """Show the installed hexawyn version."""
    click.echo(f"hexawyn {VERSION}")


@click.command()
def update_check() -> None:
    """Check for a newer release and print the upgrade command (no install)."""
    with spinner("Checking for updates on PyPI"):
        result = check_for_update(VERSION, PyPIVersionAdapter())

    if result.status == "update_available":
        installer = _detect_installer()
        index_args = resolve_install_index()["index_args"]
        command = _build_install_command(installer, index_args)
        click.echo(f"  ⚠️  Update available: {result.current_version} → {result.latest_version}")
        click.echo(f"  ⏩ Run: {' '.join(command)}")
        return

    if result.status == "up_to_date":
        ok(f"hexawyn {result.current_version} is up to date")
        success("Nothing to do — enjoy your day!")
        return

    fail(f"Could not check for updates: {result.error}")


@click.command()
def update() -> None:
    """Check for a newer release and install it (with confirmation)."""
    installer = _detect_installer()
    index_args = resolve_install_index()["index_args"]

    with spinner("Checking for updates on PyPI"):
        result = check_for_update(VERSION, PyPIVersionAdapter())

    if result.status == "update_available":
        command = _build_install_command(installer, index_args)
        click.echo(f"  ⚠️  Update available: {result.current_version} → {result.latest_version}")
        click.echo(f"  ⏩ Run: {' '.join(command)}")

        if not click.confirm(f"Install {result.latest_version} now?", default=False):
            click.echo("  ✋ Skipped — you can run the command above manually.")
            return

        with spinner(f"Updating hexawyn to {result.latest_version} via {installer}"):
            try:
                proc = subprocess.run(command, check=False)
            except FileNotFoundError as exc:
                fail(f"{installer} not found — could not run update: {exc}")
                raise click.exceptions.Exit(code=1) from exc

        if proc.returncode != 0:
            fail(f"Update failed with exit code {proc.returncode}")
            raise click.exceptions.Exit(code=proc.returncode)

        ok(f"hexawyn updated to {result.latest_version}")
        return

    if result.status == "up_to_date":
        ok(f"hexawyn {result.current_version} is up to date")
        success("Nothing to do — enjoy your day!")
        return

    fail(f"Could not check for updates: {result.error}")


def _build_install_command(installer: str, index_args: list[str]) -> list[str]:
    """Assemble the pip/pipx command to install the latest hexawyn.

    ``pip`` accepts index flags directly; ``pipx`` does not, so they are
    forwarded through ``--pip-args`` (which pipx passes through to pip).
    """
    if installer == "pipx":
        command = ["pipx", "install", "--force"]
        if index_args:
            command.append("--pip-args")
            command.append(" ".join(index_args))
        command.append("hexawyn")
        return command
    return ["pip", "install", "--upgrade", "--force-reinstall", *index_args, "hexawyn"]
