"""hexa update / hexa update-check / hexa version — manage hexawyn updates."""

from __future__ import annotations

import subprocess

import click

from hexawyn.application.service.version_check_service import check_for_update
from hexawyn.cli.commands.uninstall_command import _detect_installer
from hexawyn.cli.presentation.feedback import fail, ok, spinner, success
from hexawyn.domain.models.constants import VERSION
from hexawyn.infrastructure.adapters.secondary.pypi.pypi_version_adapter import (
    DEFAULT_PYPI_INDEX_URL,
    PyPIVersionAdapter,
    _resolve_index_url,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_resolve_install_index__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_resolve_install_index__mutmut)
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


def x_resolve_install_index__mutmut_orig() -> dict[str, list[str]]:
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


def x_resolve_install_index__mutmut_1() -> dict[str, list[str]]:
    """Build pip index arguments from the resolved source index.

    When running against TestPyPI (dev), pip needs the TestPyPI index for the
    package itself plus the real PyPI index for dependencies. The production
    index needs no extra arguments.
    """
    index_url = None
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


def x_resolve_install_index__mutmut_2() -> dict[str, list[str]]:
    """Build pip index arguments from the resolved source index.

    When running against TestPyPI (dev), pip needs the TestPyPI index for the
    package itself plus the real PyPI index for dependencies. The production
    index needs no extra arguments.
    """
    index_url = _resolve_index_url()
    if index_url != DEFAULT_PYPI_INDEX_URL:
        return {"index_args": []}
    return {
        "index_args": [
            "--index-url",
            f"{index_url}/simple/",
            "--extra-index-url",
            f"{DEFAULT_PYPI_INDEX_URL}/simple/",
        ]
    }


def x_resolve_install_index__mutmut_3() -> dict[str, list[str]]:
    """Build pip index arguments from the resolved source index.

    When running against TestPyPI (dev), pip needs the TestPyPI index for the
    package itself plus the real PyPI index for dependencies. The production
    index needs no extra arguments.
    """
    index_url = _resolve_index_url()
    if index_url == DEFAULT_PYPI_INDEX_URL:
        return {"XXindex_argsXX": []}
    return {
        "index_args": [
            "--index-url",
            f"{index_url}/simple/",
            "--extra-index-url",
            f"{DEFAULT_PYPI_INDEX_URL}/simple/",
        ]
    }


def x_resolve_install_index__mutmut_4() -> dict[str, list[str]]:
    """Build pip index arguments from the resolved source index.

    When running against TestPyPI (dev), pip needs the TestPyPI index for the
    package itself plus the real PyPI index for dependencies. The production
    index needs no extra arguments.
    """
    index_url = _resolve_index_url()
    if index_url == DEFAULT_PYPI_INDEX_URL:
        return {"INDEX_ARGS": []}
    return {
        "index_args": [
            "--index-url",
            f"{index_url}/simple/",
            "--extra-index-url",
            f"{DEFAULT_PYPI_INDEX_URL}/simple/",
        ]
    }


def x_resolve_install_index__mutmut_5() -> dict[str, list[str]]:
    """Build pip index arguments from the resolved source index.

    When running against TestPyPI (dev), pip needs the TestPyPI index for the
    package itself plus the real PyPI index for dependencies. The production
    index needs no extra arguments.
    """
    index_url = _resolve_index_url()
    if index_url == DEFAULT_PYPI_INDEX_URL:
        return {"index_args": []}
    return {
        "XXindex_argsXX": [
            "--index-url",
            f"{index_url}/simple/",
            "--extra-index-url",
            f"{DEFAULT_PYPI_INDEX_URL}/simple/",
        ]
    }


def x_resolve_install_index__mutmut_6() -> dict[str, list[str]]:
    """Build pip index arguments from the resolved source index.

    When running against TestPyPI (dev), pip needs the TestPyPI index for the
    package itself plus the real PyPI index for dependencies. The production
    index needs no extra arguments.
    """
    index_url = _resolve_index_url()
    if index_url == DEFAULT_PYPI_INDEX_URL:
        return {"index_args": []}
    return {
        "INDEX_ARGS": [
            "--index-url",
            f"{index_url}/simple/",
            "--extra-index-url",
            f"{DEFAULT_PYPI_INDEX_URL}/simple/",
        ]
    }


def x_resolve_install_index__mutmut_7() -> dict[str, list[str]]:
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
            "XX--index-urlXX",
            f"{index_url}/simple/",
            "--extra-index-url",
            f"{DEFAULT_PYPI_INDEX_URL}/simple/",
        ]
    }


def x_resolve_install_index__mutmut_8() -> dict[str, list[str]]:
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
            "--INDEX-URL",
            f"{index_url}/simple/",
            "--extra-index-url",
            f"{DEFAULT_PYPI_INDEX_URL}/simple/",
        ]
    }


def x_resolve_install_index__mutmut_9() -> dict[str, list[str]]:
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
            "XX--extra-index-urlXX",
            f"{DEFAULT_PYPI_INDEX_URL}/simple/",
        ]
    }


def x_resolve_install_index__mutmut_10() -> dict[str, list[str]]:
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
            "--EXTRA-INDEX-URL",
            f"{DEFAULT_PYPI_INDEX_URL}/simple/",
        ]
    }

mutants_x_resolve_install_index__mutmut['_mutmut_orig'] = x_resolve_install_index__mutmut_orig # type: ignore # mutmut generated
mutants_x_resolve_install_index__mutmut['x_resolve_install_index__mutmut_1'] = x_resolve_install_index__mutmut_1 # type: ignore # mutmut generated
mutants_x_resolve_install_index__mutmut['x_resolve_install_index__mutmut_2'] = x_resolve_install_index__mutmut_2 # type: ignore # mutmut generated
mutants_x_resolve_install_index__mutmut['x_resolve_install_index__mutmut_3'] = x_resolve_install_index__mutmut_3 # type: ignore # mutmut generated
mutants_x_resolve_install_index__mutmut['x_resolve_install_index__mutmut_4'] = x_resolve_install_index__mutmut_4 # type: ignore # mutmut generated
mutants_x_resolve_install_index__mutmut['x_resolve_install_index__mutmut_5'] = x_resolve_install_index__mutmut_5 # type: ignore # mutmut generated
mutants_x_resolve_install_index__mutmut['x_resolve_install_index__mutmut_6'] = x_resolve_install_index__mutmut_6 # type: ignore # mutmut generated
mutants_x_resolve_install_index__mutmut['x_resolve_install_index__mutmut_7'] = x_resolve_install_index__mutmut_7 # type: ignore # mutmut generated
mutants_x_resolve_install_index__mutmut['x_resolve_install_index__mutmut_8'] = x_resolve_install_index__mutmut_8 # type: ignore # mutmut generated
mutants_x_resolve_install_index__mutmut['x_resolve_install_index__mutmut_9'] = x_resolve_install_index__mutmut_9 # type: ignore # mutmut generated
mutants_x_resolve_install_index__mutmut['x_resolve_install_index__mutmut_10'] = x_resolve_install_index__mutmut_10 # type: ignore # mutmut generated


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
mutants_x__build_install_command__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__build_install_command__mutmut)
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


def x__build_install_command__mutmut_orig(installer: str, index_args: list[str]) -> list[str]:
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


def x__build_install_command__mutmut_1(installer: str, index_args: list[str]) -> list[str]:
    """Assemble the pip/pipx command to install the latest hexawyn.

    ``pip`` accepts index flags directly; ``pipx`` does not, so they are
    forwarded through ``--pip-args`` (which pipx passes through to pip).
    """
    if installer != "pipx":
        command = ["pipx", "install", "--force"]
        if index_args:
            command.append("--pip-args")
            command.append(" ".join(index_args))
        command.append("hexawyn")
        return command
    return ["pip", "install", "--upgrade", "--force-reinstall", *index_args, "hexawyn"]


def x__build_install_command__mutmut_2(installer: str, index_args: list[str]) -> list[str]:
    """Assemble the pip/pipx command to install the latest hexawyn.

    ``pip`` accepts index flags directly; ``pipx`` does not, so they are
    forwarded through ``--pip-args`` (which pipx passes through to pip).
    """
    if installer == "XXpipxXX":
        command = ["pipx", "install", "--force"]
        if index_args:
            command.append("--pip-args")
            command.append(" ".join(index_args))
        command.append("hexawyn")
        return command
    return ["pip", "install", "--upgrade", "--force-reinstall", *index_args, "hexawyn"]


def x__build_install_command__mutmut_3(installer: str, index_args: list[str]) -> list[str]:
    """Assemble the pip/pipx command to install the latest hexawyn.

    ``pip`` accepts index flags directly; ``pipx`` does not, so they are
    forwarded through ``--pip-args`` (which pipx passes through to pip).
    """
    if installer == "PIPX":
        command = ["pipx", "install", "--force"]
        if index_args:
            command.append("--pip-args")
            command.append(" ".join(index_args))
        command.append("hexawyn")
        return command
    return ["pip", "install", "--upgrade", "--force-reinstall", *index_args, "hexawyn"]


def x__build_install_command__mutmut_4(installer: str, index_args: list[str]) -> list[str]:
    """Assemble the pip/pipx command to install the latest hexawyn.

    ``pip`` accepts index flags directly; ``pipx`` does not, so they are
    forwarded through ``--pip-args`` (which pipx passes through to pip).
    """
    if installer == "pipx":
        command = None
        if index_args:
            command.append("--pip-args")
            command.append(" ".join(index_args))
        command.append("hexawyn")
        return command
    return ["pip", "install", "--upgrade", "--force-reinstall", *index_args, "hexawyn"]


def x__build_install_command__mutmut_5(installer: str, index_args: list[str]) -> list[str]:
    """Assemble the pip/pipx command to install the latest hexawyn.

    ``pip`` accepts index flags directly; ``pipx`` does not, so they are
    forwarded through ``--pip-args`` (which pipx passes through to pip).
    """
    if installer == "pipx":
        command = ["XXpipxXX", "install", "--force"]
        if index_args:
            command.append("--pip-args")
            command.append(" ".join(index_args))
        command.append("hexawyn")
        return command
    return ["pip", "install", "--upgrade", "--force-reinstall", *index_args, "hexawyn"]


def x__build_install_command__mutmut_6(installer: str, index_args: list[str]) -> list[str]:
    """Assemble the pip/pipx command to install the latest hexawyn.

    ``pip`` accepts index flags directly; ``pipx`` does not, so they are
    forwarded through ``--pip-args`` (which pipx passes through to pip).
    """
    if installer == "pipx":
        command = ["PIPX", "install", "--force"]
        if index_args:
            command.append("--pip-args")
            command.append(" ".join(index_args))
        command.append("hexawyn")
        return command
    return ["pip", "install", "--upgrade", "--force-reinstall", *index_args, "hexawyn"]


def x__build_install_command__mutmut_7(installer: str, index_args: list[str]) -> list[str]:
    """Assemble the pip/pipx command to install the latest hexawyn.

    ``pip`` accepts index flags directly; ``pipx`` does not, so they are
    forwarded through ``--pip-args`` (which pipx passes through to pip).
    """
    if installer == "pipx":
        command = ["pipx", "XXinstallXX", "--force"]
        if index_args:
            command.append("--pip-args")
            command.append(" ".join(index_args))
        command.append("hexawyn")
        return command
    return ["pip", "install", "--upgrade", "--force-reinstall", *index_args, "hexawyn"]


def x__build_install_command__mutmut_8(installer: str, index_args: list[str]) -> list[str]:
    """Assemble the pip/pipx command to install the latest hexawyn.

    ``pip`` accepts index flags directly; ``pipx`` does not, so they are
    forwarded through ``--pip-args`` (which pipx passes through to pip).
    """
    if installer == "pipx":
        command = ["pipx", "INSTALL", "--force"]
        if index_args:
            command.append("--pip-args")
            command.append(" ".join(index_args))
        command.append("hexawyn")
        return command
    return ["pip", "install", "--upgrade", "--force-reinstall", *index_args, "hexawyn"]


def x__build_install_command__mutmut_9(installer: str, index_args: list[str]) -> list[str]:
    """Assemble the pip/pipx command to install the latest hexawyn.

    ``pip`` accepts index flags directly; ``pipx`` does not, so they are
    forwarded through ``--pip-args`` (which pipx passes through to pip).
    """
    if installer == "pipx":
        command = ["pipx", "install", "XX--forceXX"]
        if index_args:
            command.append("--pip-args")
            command.append(" ".join(index_args))
        command.append("hexawyn")
        return command
    return ["pip", "install", "--upgrade", "--force-reinstall", *index_args, "hexawyn"]


def x__build_install_command__mutmut_10(installer: str, index_args: list[str]) -> list[str]:
    """Assemble the pip/pipx command to install the latest hexawyn.

    ``pip`` accepts index flags directly; ``pipx`` does not, so they are
    forwarded through ``--pip-args`` (which pipx passes through to pip).
    """
    if installer == "pipx":
        command = ["pipx", "install", "--FORCE"]
        if index_args:
            command.append("--pip-args")
            command.append(" ".join(index_args))
        command.append("hexawyn")
        return command
    return ["pip", "install", "--upgrade", "--force-reinstall", *index_args, "hexawyn"]


def x__build_install_command__mutmut_11(installer: str, index_args: list[str]) -> list[str]:
    """Assemble the pip/pipx command to install the latest hexawyn.

    ``pip`` accepts index flags directly; ``pipx`` does not, so they are
    forwarded through ``--pip-args`` (which pipx passes through to pip).
    """
    if installer == "pipx":
        command = ["pipx", "install", "--force"]
        if index_args:
            command.append(None)
            command.append(" ".join(index_args))
        command.append("hexawyn")
        return command
    return ["pip", "install", "--upgrade", "--force-reinstall", *index_args, "hexawyn"]


def x__build_install_command__mutmut_12(installer: str, index_args: list[str]) -> list[str]:
    """Assemble the pip/pipx command to install the latest hexawyn.

    ``pip`` accepts index flags directly; ``pipx`` does not, so they are
    forwarded through ``--pip-args`` (which pipx passes through to pip).
    """
    if installer == "pipx":
        command = ["pipx", "install", "--force"]
        if index_args:
            command.append("XX--pip-argsXX")
            command.append(" ".join(index_args))
        command.append("hexawyn")
        return command
    return ["pip", "install", "--upgrade", "--force-reinstall", *index_args, "hexawyn"]


def x__build_install_command__mutmut_13(installer: str, index_args: list[str]) -> list[str]:
    """Assemble the pip/pipx command to install the latest hexawyn.

    ``pip`` accepts index flags directly; ``pipx`` does not, so they are
    forwarded through ``--pip-args`` (which pipx passes through to pip).
    """
    if installer == "pipx":
        command = ["pipx", "install", "--force"]
        if index_args:
            command.append("--PIP-ARGS")
            command.append(" ".join(index_args))
        command.append("hexawyn")
        return command
    return ["pip", "install", "--upgrade", "--force-reinstall", *index_args, "hexawyn"]


def x__build_install_command__mutmut_14(installer: str, index_args: list[str]) -> list[str]:
    """Assemble the pip/pipx command to install the latest hexawyn.

    ``pip`` accepts index flags directly; ``pipx`` does not, so they are
    forwarded through ``--pip-args`` (which pipx passes through to pip).
    """
    if installer == "pipx":
        command = ["pipx", "install", "--force"]
        if index_args:
            command.append("--pip-args")
            command.append(None)
        command.append("hexawyn")
        return command
    return ["pip", "install", "--upgrade", "--force-reinstall", *index_args, "hexawyn"]


def x__build_install_command__mutmut_15(installer: str, index_args: list[str]) -> list[str]:
    """Assemble the pip/pipx command to install the latest hexawyn.

    ``pip`` accepts index flags directly; ``pipx`` does not, so they are
    forwarded through ``--pip-args`` (which pipx passes through to pip).
    """
    if installer == "pipx":
        command = ["pipx", "install", "--force"]
        if index_args:
            command.append("--pip-args")
            command.append(" ".join(None))
        command.append("hexawyn")
        return command
    return ["pip", "install", "--upgrade", "--force-reinstall", *index_args, "hexawyn"]


def x__build_install_command__mutmut_16(installer: str, index_args: list[str]) -> list[str]:
    """Assemble the pip/pipx command to install the latest hexawyn.

    ``pip`` accepts index flags directly; ``pipx`` does not, so they are
    forwarded through ``--pip-args`` (which pipx passes through to pip).
    """
    if installer == "pipx":
        command = ["pipx", "install", "--force"]
        if index_args:
            command.append("--pip-args")
            command.append("XX XX".join(index_args))
        command.append("hexawyn")
        return command
    return ["pip", "install", "--upgrade", "--force-reinstall", *index_args, "hexawyn"]


def x__build_install_command__mutmut_17(installer: str, index_args: list[str]) -> list[str]:
    """Assemble the pip/pipx command to install the latest hexawyn.

    ``pip`` accepts index flags directly; ``pipx`` does not, so they are
    forwarded through ``--pip-args`` (which pipx passes through to pip).
    """
    if installer == "pipx":
        command = ["pipx", "install", "--force"]
        if index_args:
            command.append("--pip-args")
            command.append(" ".join(index_args))
        command.append(None)
        return command
    return ["pip", "install", "--upgrade", "--force-reinstall", *index_args, "hexawyn"]


def x__build_install_command__mutmut_18(installer: str, index_args: list[str]) -> list[str]:
    """Assemble the pip/pipx command to install the latest hexawyn.

    ``pip`` accepts index flags directly; ``pipx`` does not, so they are
    forwarded through ``--pip-args`` (which pipx passes through to pip).
    """
    if installer == "pipx":
        command = ["pipx", "install", "--force"]
        if index_args:
            command.append("--pip-args")
            command.append(" ".join(index_args))
        command.append("XXhexawynXX")
        return command
    return ["pip", "install", "--upgrade", "--force-reinstall", *index_args, "hexawyn"]


def x__build_install_command__mutmut_19(installer: str, index_args: list[str]) -> list[str]:
    """Assemble the pip/pipx command to install the latest hexawyn.

    ``pip`` accepts index flags directly; ``pipx`` does not, so they are
    forwarded through ``--pip-args`` (which pipx passes through to pip).
    """
    if installer == "pipx":
        command = ["pipx", "install", "--force"]
        if index_args:
            command.append("--pip-args")
            command.append(" ".join(index_args))
        command.append("HEXAWYN")
        return command
    return ["pip", "install", "--upgrade", "--force-reinstall", *index_args, "hexawyn"]


def x__build_install_command__mutmut_20(installer: str, index_args: list[str]) -> list[str]:
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
    return ["XXpipXX", "install", "--upgrade", "--force-reinstall", *index_args, "hexawyn"]


def x__build_install_command__mutmut_21(installer: str, index_args: list[str]) -> list[str]:
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
    return ["PIP", "install", "--upgrade", "--force-reinstall", *index_args, "hexawyn"]


def x__build_install_command__mutmut_22(installer: str, index_args: list[str]) -> list[str]:
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
    return ["pip", "XXinstallXX", "--upgrade", "--force-reinstall", *index_args, "hexawyn"]


def x__build_install_command__mutmut_23(installer: str, index_args: list[str]) -> list[str]:
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
    return ["pip", "INSTALL", "--upgrade", "--force-reinstall", *index_args, "hexawyn"]


def x__build_install_command__mutmut_24(installer: str, index_args: list[str]) -> list[str]:
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
    return ["pip", "install", "XX--upgradeXX", "--force-reinstall", *index_args, "hexawyn"]


def x__build_install_command__mutmut_25(installer: str, index_args: list[str]) -> list[str]:
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
    return ["pip", "install", "--UPGRADE", "--force-reinstall", *index_args, "hexawyn"]


def x__build_install_command__mutmut_26(installer: str, index_args: list[str]) -> list[str]:
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
    return ["pip", "install", "--upgrade", "XX--force-reinstallXX", *index_args, "hexawyn"]


def x__build_install_command__mutmut_27(installer: str, index_args: list[str]) -> list[str]:
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
    return ["pip", "install", "--upgrade", "--FORCE-REINSTALL", *index_args, "hexawyn"]


def x__build_install_command__mutmut_28(installer: str, index_args: list[str]) -> list[str]:
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
    return ["pip", "install", "--upgrade", "--force-reinstall", *index_args, "XXhexawynXX"]


def x__build_install_command__mutmut_29(installer: str, index_args: list[str]) -> list[str]:
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
    return ["pip", "install", "--upgrade", "--force-reinstall", *index_args, "HEXAWYN"]

mutants_x__build_install_command__mutmut['_mutmut_orig'] = x__build_install_command__mutmut_orig # type: ignore # mutmut generated
mutants_x__build_install_command__mutmut['x__build_install_command__mutmut_1'] = x__build_install_command__mutmut_1 # type: ignore # mutmut generated
mutants_x__build_install_command__mutmut['x__build_install_command__mutmut_2'] = x__build_install_command__mutmut_2 # type: ignore # mutmut generated
mutants_x__build_install_command__mutmut['x__build_install_command__mutmut_3'] = x__build_install_command__mutmut_3 # type: ignore # mutmut generated
mutants_x__build_install_command__mutmut['x__build_install_command__mutmut_4'] = x__build_install_command__mutmut_4 # type: ignore # mutmut generated
mutants_x__build_install_command__mutmut['x__build_install_command__mutmut_5'] = x__build_install_command__mutmut_5 # type: ignore # mutmut generated
mutants_x__build_install_command__mutmut['x__build_install_command__mutmut_6'] = x__build_install_command__mutmut_6 # type: ignore # mutmut generated
mutants_x__build_install_command__mutmut['x__build_install_command__mutmut_7'] = x__build_install_command__mutmut_7 # type: ignore # mutmut generated
mutants_x__build_install_command__mutmut['x__build_install_command__mutmut_8'] = x__build_install_command__mutmut_8 # type: ignore # mutmut generated
mutants_x__build_install_command__mutmut['x__build_install_command__mutmut_9'] = x__build_install_command__mutmut_9 # type: ignore # mutmut generated
mutants_x__build_install_command__mutmut['x__build_install_command__mutmut_10'] = x__build_install_command__mutmut_10 # type: ignore # mutmut generated
mutants_x__build_install_command__mutmut['x__build_install_command__mutmut_11'] = x__build_install_command__mutmut_11 # type: ignore # mutmut generated
mutants_x__build_install_command__mutmut['x__build_install_command__mutmut_12'] = x__build_install_command__mutmut_12 # type: ignore # mutmut generated
mutants_x__build_install_command__mutmut['x__build_install_command__mutmut_13'] = x__build_install_command__mutmut_13 # type: ignore # mutmut generated
mutants_x__build_install_command__mutmut['x__build_install_command__mutmut_14'] = x__build_install_command__mutmut_14 # type: ignore # mutmut generated
mutants_x__build_install_command__mutmut['x__build_install_command__mutmut_15'] = x__build_install_command__mutmut_15 # type: ignore # mutmut generated
mutants_x__build_install_command__mutmut['x__build_install_command__mutmut_16'] = x__build_install_command__mutmut_16 # type: ignore # mutmut generated
mutants_x__build_install_command__mutmut['x__build_install_command__mutmut_17'] = x__build_install_command__mutmut_17 # type: ignore # mutmut generated
mutants_x__build_install_command__mutmut['x__build_install_command__mutmut_18'] = x__build_install_command__mutmut_18 # type: ignore # mutmut generated
mutants_x__build_install_command__mutmut['x__build_install_command__mutmut_19'] = x__build_install_command__mutmut_19 # type: ignore # mutmut generated
mutants_x__build_install_command__mutmut['x__build_install_command__mutmut_20'] = x__build_install_command__mutmut_20 # type: ignore # mutmut generated
mutants_x__build_install_command__mutmut['x__build_install_command__mutmut_21'] = x__build_install_command__mutmut_21 # type: ignore # mutmut generated
mutants_x__build_install_command__mutmut['x__build_install_command__mutmut_22'] = x__build_install_command__mutmut_22 # type: ignore # mutmut generated
mutants_x__build_install_command__mutmut['x__build_install_command__mutmut_23'] = x__build_install_command__mutmut_23 # type: ignore # mutmut generated
mutants_x__build_install_command__mutmut['x__build_install_command__mutmut_24'] = x__build_install_command__mutmut_24 # type: ignore # mutmut generated
mutants_x__build_install_command__mutmut['x__build_install_command__mutmut_25'] = x__build_install_command__mutmut_25 # type: ignore # mutmut generated
mutants_x__build_install_command__mutmut['x__build_install_command__mutmut_26'] = x__build_install_command__mutmut_26 # type: ignore # mutmut generated
mutants_x__build_install_command__mutmut['x__build_install_command__mutmut_27'] = x__build_install_command__mutmut_27 # type: ignore # mutmut generated
mutants_x__build_install_command__mutmut['x__build_install_command__mutmut_28'] = x__build_install_command__mutmut_28 # type: ignore # mutmut generated
mutants_x__build_install_command__mutmut['x__build_install_command__mutmut_29'] = x__build_install_command__mutmut_29 # type: ignore # mutmut generated
