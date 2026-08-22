"""Emoji-based step feedback for the hexa CLI.

Thin wrappers around rich Status and click echo so every command renders
consistent, cheerful progress feedback without duplicating spinner logic.
"""

from __future__ import annotations

import click
from rich.console import Console
from rich.status import Status

from hexawyn.cli.presentation.constants import _LOGO_BANNER
from hexawyn.domain.models.constants import VERSION

_SPINNER_CONSOLE = Console(stderr=True)


def header() -> None:
    """Render the hexawyn logo banner with the current version on stdout."""
    console = Console()
    console.print("\n".join(line.format(version=VERSION) for line in _LOGO_BANNER))
    console.print()


def step(message: str) -> None:
    """Render an in-progress spinner line on stderr (non-blocking)."""
    _SPINNER_CONSOLE.print(f"  ⏳ {message}...", highlight=False)


def ok(message: str) -> None:
    """Render a completed step with a checkmark on stdout."""
    click.echo(f"  ✅ {message}")


def success(message: str) -> None:
    """Render a final success line with a celebration on stdout."""
    click.echo(f"  🎉 {message}")


def fail(message: str) -> None:
    """Render a failure line with a cross on stderr."""
    click.echo(f"  ❌ {message}", err=True)


def spinner(message: str) -> Status:
    """Start an animated rich spinner on stderr.

    Usage:
        with spinner("Checking for updates"):
            ...work...
    """
    return _SPINNER_CONSOLE.status(f"⏳ {message}...", spinner="dots")
