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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x__detect_installer__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__detect_installer__mutmut)
def _detect_installer() -> str:
    """Return ``pipx`` when the CLI runs from a pipx-managed venv, else ``pip``."""
    if shutil.which("pipx"):
        executable = str(sys.executable)
        if ".local/share/pipx" in executable or "pipx/venvs" in executable:
            return _PIPX_MARKER
    return "pip"


def x__detect_installer__mutmut_orig() -> str:
    """Return ``pipx`` when the CLI runs from a pipx-managed venv, else ``pip``."""
    if shutil.which("pipx"):
        executable = str(sys.executable)
        if ".local/share/pipx" in executable or "pipx/venvs" in executable:
            return _PIPX_MARKER
    return "pip"


def x__detect_installer__mutmut_1() -> str:
    """Return ``pipx`` when the CLI runs from a pipx-managed venv, else ``pip``."""
    if shutil.which(None):
        executable = str(sys.executable)
        if ".local/share/pipx" in executable or "pipx/venvs" in executable:
            return _PIPX_MARKER
    return "pip"


def x__detect_installer__mutmut_2() -> str:
    """Return ``pipx`` when the CLI runs from a pipx-managed venv, else ``pip``."""
    if shutil.which("XXpipxXX"):
        executable = str(sys.executable)
        if ".local/share/pipx" in executable or "pipx/venvs" in executable:
            return _PIPX_MARKER
    return "pip"


def x__detect_installer__mutmut_3() -> str:
    """Return ``pipx`` when the CLI runs from a pipx-managed venv, else ``pip``."""
    if shutil.which("PIPX"):
        executable = str(sys.executable)
        if ".local/share/pipx" in executable or "pipx/venvs" in executable:
            return _PIPX_MARKER
    return "pip"


def x__detect_installer__mutmut_4() -> str:
    """Return ``pipx`` when the CLI runs from a pipx-managed venv, else ``pip``."""
    if shutil.which("pipx"):
        executable = None
        if ".local/share/pipx" in executable or "pipx/venvs" in executable:
            return _PIPX_MARKER
    return "pip"


def x__detect_installer__mutmut_5() -> str:
    """Return ``pipx`` when the CLI runs from a pipx-managed venv, else ``pip``."""
    if shutil.which("pipx"):
        executable = str(None)
        if ".local/share/pipx" in executable or "pipx/venvs" in executable:
            return _PIPX_MARKER
    return "pip"


def x__detect_installer__mutmut_6() -> str:
    """Return ``pipx`` when the CLI runs from a pipx-managed venv, else ``pip``."""
    if shutil.which("pipx"):
        executable = str(sys.executable)
        if ".local/share/pipx" in executable and "pipx/venvs" in executable:
            return _PIPX_MARKER
    return "pip"


def x__detect_installer__mutmut_7() -> str:
    """Return ``pipx`` when the CLI runs from a pipx-managed venv, else ``pip``."""
    if shutil.which("pipx"):
        executable = str(sys.executable)
        if "XX.local/share/pipxXX" in executable or "pipx/venvs" in executable:
            return _PIPX_MARKER
    return "pip"


def x__detect_installer__mutmut_8() -> str:
    """Return ``pipx`` when the CLI runs from a pipx-managed venv, else ``pip``."""
    if shutil.which("pipx"):
        executable = str(sys.executable)
        if ".LOCAL/SHARE/PIPX" in executable or "pipx/venvs" in executable:
            return _PIPX_MARKER
    return "pip"


def x__detect_installer__mutmut_9() -> str:
    """Return ``pipx`` when the CLI runs from a pipx-managed venv, else ``pip``."""
    if shutil.which("pipx"):
        executable = str(sys.executable)
        if ".local/share/pipx" not in executable or "pipx/venvs" in executable:
            return _PIPX_MARKER
    return "pip"


def x__detect_installer__mutmut_10() -> str:
    """Return ``pipx`` when the CLI runs from a pipx-managed venv, else ``pip``."""
    if shutil.which("pipx"):
        executable = str(sys.executable)
        if ".local/share/pipx" in executable or "XXpipx/venvsXX" in executable:
            return _PIPX_MARKER
    return "pip"


def x__detect_installer__mutmut_11() -> str:
    """Return ``pipx`` when the CLI runs from a pipx-managed venv, else ``pip``."""
    if shutil.which("pipx"):
        executable = str(sys.executable)
        if ".local/share/pipx" in executable or "PIPX/VENVS" in executable:
            return _PIPX_MARKER
    return "pip"


def x__detect_installer__mutmut_12() -> str:
    """Return ``pipx`` when the CLI runs from a pipx-managed venv, else ``pip``."""
    if shutil.which("pipx"):
        executable = str(sys.executable)
        if ".local/share/pipx" in executable or "pipx/venvs" not in executable:
            return _PIPX_MARKER
    return "pip"


def x__detect_installer__mutmut_13() -> str:
    """Return ``pipx`` when the CLI runs from a pipx-managed venv, else ``pip``."""
    if shutil.which("pipx"):
        executable = str(sys.executable)
        if ".local/share/pipx" in executable or "pipx/venvs" in executable:
            return _PIPX_MARKER
    return "XXpipXX"


def x__detect_installer__mutmut_14() -> str:
    """Return ``pipx`` when the CLI runs from a pipx-managed venv, else ``pip``."""
    if shutil.which("pipx"):
        executable = str(sys.executable)
        if ".local/share/pipx" in executable or "pipx/venvs" in executable:
            return _PIPX_MARKER
    return "PIP"

mutants_x__detect_installer__mutmut['_mutmut_orig'] = x__detect_installer__mutmut_orig # type: ignore # mutmut generated
mutants_x__detect_installer__mutmut['x__detect_installer__mutmut_1'] = x__detect_installer__mutmut_1 # type: ignore # mutmut generated
mutants_x__detect_installer__mutmut['x__detect_installer__mutmut_2'] = x__detect_installer__mutmut_2 # type: ignore # mutmut generated
mutants_x__detect_installer__mutmut['x__detect_installer__mutmut_3'] = x__detect_installer__mutmut_3 # type: ignore # mutmut generated
mutants_x__detect_installer__mutmut['x__detect_installer__mutmut_4'] = x__detect_installer__mutmut_4 # type: ignore # mutmut generated
mutants_x__detect_installer__mutmut['x__detect_installer__mutmut_5'] = x__detect_installer__mutmut_5 # type: ignore # mutmut generated
mutants_x__detect_installer__mutmut['x__detect_installer__mutmut_6'] = x__detect_installer__mutmut_6 # type: ignore # mutmut generated
mutants_x__detect_installer__mutmut['x__detect_installer__mutmut_7'] = x__detect_installer__mutmut_7 # type: ignore # mutmut generated
mutants_x__detect_installer__mutmut['x__detect_installer__mutmut_8'] = x__detect_installer__mutmut_8 # type: ignore # mutmut generated
mutants_x__detect_installer__mutmut['x__detect_installer__mutmut_9'] = x__detect_installer__mutmut_9 # type: ignore # mutmut generated
mutants_x__detect_installer__mutmut['x__detect_installer__mutmut_10'] = x__detect_installer__mutmut_10 # type: ignore # mutmut generated
mutants_x__detect_installer__mutmut['x__detect_installer__mutmut_11'] = x__detect_installer__mutmut_11 # type: ignore # mutmut generated
mutants_x__detect_installer__mutmut['x__detect_installer__mutmut_12'] = x__detect_installer__mutmut_12 # type: ignore # mutmut generated
mutants_x__detect_installer__mutmut['x__detect_installer__mutmut_13'] = x__detect_installer__mutmut_13 # type: ignore # mutmut generated
mutants_x__detect_installer__mutmut['x__detect_installer__mutmut_14'] = x__detect_installer__mutmut_14 # type: ignore # mutmut generated


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
