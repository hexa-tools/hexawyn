"""hexa uninstall — remove the hexawyn package from the environment.

Detects whether hexawyn was installed via pipx (isolated application) or a
classic pip venv, then runs the matching uninstall command.
"""

from __future__ import annotations

import shutil
import subprocess
import sys

import click

from hexawyn.cli.presentation.feedback import fail, ok, spinner

_PACKAGE_NAME = "hexawyn"
_PIPX_MARKER = "pipx"


def _detect_installer() -> str:
    """Return ``pipx`` when the CLI runs from a pipx-managed venv, else ``pip``."""
    if shutil.which("pipx"):
        executable = str(sys.executable)
        if ".local/share/pipx" in executable or "pipx/venvs" in executable:
            return _PIPX_MARKER
    return "pip"


@click.command()
def uninstall() -> None:
    """Uninstall hexawyn from the current environment."""
    installer = _detect_installer()

    if installer == _PIPX_MARKER:
        command = ["pipx", "uninstall", _PACKAGE_NAME]
    else:
        command = ["pip", "uninstall", "-y", _PACKAGE_NAME]

    with spinner(f"Uninstalling {_PACKAGE_NAME} via {installer}"):
        try:
            result = subprocess.run(command, check=False)
        except FileNotFoundError as exc:
            fail(f"{installer} not found — could not run uninstall: {exc}")
            raise click.exceptions.Exit(code=1) from exc

    if result.returncode != 0:
        fail(f"Uninstall failed with exit code {result.returncode}")
        raise click.exceptions.Exit(code=result.returncode)

    ok(f"{_PACKAGE_NAME} has been removed via {installer}")
