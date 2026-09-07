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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_header__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_header__mutmut)
def header() -> None:
    """Render the hexawyn logo banner with the current version on stdout."""
    console = Console()
    console.print("\n".join(line.format(version=VERSION) for line in _LOGO_BANNER))
    console.print()


def x_header__mutmut_orig() -> None:
    """Render the hexawyn logo banner with the current version on stdout."""
    console = Console()
    console.print("\n".join(line.format(version=VERSION) for line in _LOGO_BANNER))
    console.print()


def x_header__mutmut_1() -> None:
    """Render the hexawyn logo banner with the current version on stdout."""
    console = None
    console.print("\n".join(line.format(version=VERSION) for line in _LOGO_BANNER))
    console.print()


def x_header__mutmut_2() -> None:
    """Render the hexawyn logo banner with the current version on stdout."""
    console = Console()
    console.print(None)
    console.print()


def x_header__mutmut_3() -> None:
    """Render the hexawyn logo banner with the current version on stdout."""
    console = Console()
    console.print("\n".join(None))
    console.print()


def x_header__mutmut_4() -> None:
    """Render the hexawyn logo banner with the current version on stdout."""
    console = Console()
    console.print("XX\nXX".join(line.format(version=VERSION) for line in _LOGO_BANNER))
    console.print()


def x_header__mutmut_5() -> None:
    """Render the hexawyn logo banner with the current version on stdout."""
    console = Console()
    console.print("\n".join(line.format(version=None) for line in _LOGO_BANNER))
    console.print()

mutants_x_header__mutmut['_mutmut_orig'] = x_header__mutmut_orig # type: ignore # mutmut generated
mutants_x_header__mutmut['x_header__mutmut_1'] = x_header__mutmut_1 # type: ignore # mutmut generated
mutants_x_header__mutmut['x_header__mutmut_2'] = x_header__mutmut_2 # type: ignore # mutmut generated
mutants_x_header__mutmut['x_header__mutmut_3'] = x_header__mutmut_3 # type: ignore # mutmut generated
mutants_x_header__mutmut['x_header__mutmut_4'] = x_header__mutmut_4 # type: ignore # mutmut generated
mutants_x_header__mutmut['x_header__mutmut_5'] = x_header__mutmut_5 # type: ignore # mutmut generated
mutants_x_step__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_step__mutmut)
def step(message: str) -> None:
    """Render an in-progress spinner line on stderr (non-blocking)."""
    _SPINNER_CONSOLE.print(f"  ⏳ {message}...", highlight=False)


def x_step__mutmut_orig(message: str) -> None:
    """Render an in-progress spinner line on stderr (non-blocking)."""
    _SPINNER_CONSOLE.print(f"  ⏳ {message}...", highlight=False)


def x_step__mutmut_1(message: str) -> None:
    """Render an in-progress spinner line on stderr (non-blocking)."""
    _SPINNER_CONSOLE.print(None, highlight=False)


def x_step__mutmut_2(message: str) -> None:
    """Render an in-progress spinner line on stderr (non-blocking)."""
    _SPINNER_CONSOLE.print(f"  ⏳ {message}...", highlight=None)


def x_step__mutmut_3(message: str) -> None:
    """Render an in-progress spinner line on stderr (non-blocking)."""
    _SPINNER_CONSOLE.print(highlight=False)


def x_step__mutmut_4(message: str) -> None:
    """Render an in-progress spinner line on stderr (non-blocking)."""
    _SPINNER_CONSOLE.print(f"  ⏳ {message}...", )


def x_step__mutmut_5(message: str) -> None:
    """Render an in-progress spinner line on stderr (non-blocking)."""
    _SPINNER_CONSOLE.print(f"  ⏳ {message}...", highlight=True)

mutants_x_step__mutmut['_mutmut_orig'] = x_step__mutmut_orig # type: ignore # mutmut generated
mutants_x_step__mutmut['x_step__mutmut_1'] = x_step__mutmut_1 # type: ignore # mutmut generated
mutants_x_step__mutmut['x_step__mutmut_2'] = x_step__mutmut_2 # type: ignore # mutmut generated
mutants_x_step__mutmut['x_step__mutmut_3'] = x_step__mutmut_3 # type: ignore # mutmut generated
mutants_x_step__mutmut['x_step__mutmut_4'] = x_step__mutmut_4 # type: ignore # mutmut generated
mutants_x_step__mutmut['x_step__mutmut_5'] = x_step__mutmut_5 # type: ignore # mutmut generated
mutants_x_ok__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_ok__mutmut)
def ok(message: str) -> None:
    """Render a completed step with a checkmark on stdout."""
    click.echo(f"  ✅ {message}")


def x_ok__mutmut_orig(message: str) -> None:
    """Render a completed step with a checkmark on stdout."""
    click.echo(f"  ✅ {message}")


def x_ok__mutmut_1(message: str) -> None:
    """Render a completed step with a checkmark on stdout."""
    click.echo(None)

mutants_x_ok__mutmut['_mutmut_orig'] = x_ok__mutmut_orig # type: ignore # mutmut generated
mutants_x_ok__mutmut['x_ok__mutmut_1'] = x_ok__mutmut_1 # type: ignore # mutmut generated
mutants_x_success__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_success__mutmut)
def success(message: str) -> None:
    """Render a final success line with a celebration on stdout."""
    click.echo(f"  🎉 {message}")


def x_success__mutmut_orig(message: str) -> None:
    """Render a final success line with a celebration on stdout."""
    click.echo(f"  🎉 {message}")


def x_success__mutmut_1(message: str) -> None:
    """Render a final success line with a celebration on stdout."""
    click.echo(None)

mutants_x_success__mutmut['_mutmut_orig'] = x_success__mutmut_orig # type: ignore # mutmut generated
mutants_x_success__mutmut['x_success__mutmut_1'] = x_success__mutmut_1 # type: ignore # mutmut generated
mutants_x_fail__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_fail__mutmut)
def fail(message: str) -> None:
    """Render a failure line with a cross on stderr."""
    click.echo(f"  ❌ {message}", err=True)


def x_fail__mutmut_orig(message: str) -> None:
    """Render a failure line with a cross on stderr."""
    click.echo(f"  ❌ {message}", err=True)


def x_fail__mutmut_1(message: str) -> None:
    """Render a failure line with a cross on stderr."""
    click.echo(None, err=True)


def x_fail__mutmut_2(message: str) -> None:
    """Render a failure line with a cross on stderr."""
    click.echo(f"  ❌ {message}", err=None)


def x_fail__mutmut_3(message: str) -> None:
    """Render a failure line with a cross on stderr."""
    click.echo(err=True)


def x_fail__mutmut_4(message: str) -> None:
    """Render a failure line with a cross on stderr."""
    click.echo(f"  ❌ {message}", )


def x_fail__mutmut_5(message: str) -> None:
    """Render a failure line with a cross on stderr."""
    click.echo(f"  ❌ {message}", err=False)

mutants_x_fail__mutmut['_mutmut_orig'] = x_fail__mutmut_orig # type: ignore # mutmut generated
mutants_x_fail__mutmut['x_fail__mutmut_1'] = x_fail__mutmut_1 # type: ignore # mutmut generated
mutants_x_fail__mutmut['x_fail__mutmut_2'] = x_fail__mutmut_2 # type: ignore # mutmut generated
mutants_x_fail__mutmut['x_fail__mutmut_3'] = x_fail__mutmut_3 # type: ignore # mutmut generated
mutants_x_fail__mutmut['x_fail__mutmut_4'] = x_fail__mutmut_4 # type: ignore # mutmut generated
mutants_x_fail__mutmut['x_fail__mutmut_5'] = x_fail__mutmut_5 # type: ignore # mutmut generated
mutants_x_spinner__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_spinner__mutmut)
def spinner(message: str) -> Status:
    """Start an animated rich spinner on stderr.

    Usage:
        with spinner("Checking for updates"):
            ...work...
    """
    return _SPINNER_CONSOLE.status(f"⏳ {message}...", spinner="dots")


def x_spinner__mutmut_orig(message: str) -> Status:
    """Start an animated rich spinner on stderr.

    Usage:
        with spinner("Checking for updates"):
            ...work...
    """
    return _SPINNER_CONSOLE.status(f"⏳ {message}...", spinner="dots")


def x_spinner__mutmut_1(message: str) -> Status:
    """Start an animated rich spinner on stderr.

    Usage:
        with spinner("Checking for updates"):
            ...work...
    """
    return _SPINNER_CONSOLE.status(None, spinner="dots")


def x_spinner__mutmut_2(message: str) -> Status:
    """Start an animated rich spinner on stderr.

    Usage:
        with spinner("Checking for updates"):
            ...work...
    """
    return _SPINNER_CONSOLE.status(f"⏳ {message}...", spinner=None)


def x_spinner__mutmut_3(message: str) -> Status:
    """Start an animated rich spinner on stderr.

    Usage:
        with spinner("Checking for updates"):
            ...work...
    """
    return _SPINNER_CONSOLE.status(spinner="dots")


def x_spinner__mutmut_4(message: str) -> Status:
    """Start an animated rich spinner on stderr.

    Usage:
        with spinner("Checking for updates"):
            ...work...
    """
    return _SPINNER_CONSOLE.status(f"⏳ {message}...", )


def x_spinner__mutmut_5(message: str) -> Status:
    """Start an animated rich spinner on stderr.

    Usage:
        with spinner("Checking for updates"):
            ...work...
    """
    return _SPINNER_CONSOLE.status(f"⏳ {message}...", spinner="XXdotsXX")


def x_spinner__mutmut_6(message: str) -> Status:
    """Start an animated rich spinner on stderr.

    Usage:
        with spinner("Checking for updates"):
            ...work...
    """
    return _SPINNER_CONSOLE.status(f"⏳ {message}...", spinner="DOTS")

mutants_x_spinner__mutmut['_mutmut_orig'] = x_spinner__mutmut_orig # type: ignore # mutmut generated
mutants_x_spinner__mutmut['x_spinner__mutmut_1'] = x_spinner__mutmut_1 # type: ignore # mutmut generated
mutants_x_spinner__mutmut['x_spinner__mutmut_2'] = x_spinner__mutmut_2 # type: ignore # mutmut generated
mutants_x_spinner__mutmut['x_spinner__mutmut_3'] = x_spinner__mutmut_3 # type: ignore # mutmut generated
mutants_x_spinner__mutmut['x_spinner__mutmut_4'] = x_spinner__mutmut_4 # type: ignore # mutmut generated
mutants_x_spinner__mutmut['x_spinner__mutmut_5'] = x_spinner__mutmut_5 # type: ignore # mutmut generated
mutants_x_spinner__mutmut['x_spinner__mutmut_6'] = x_spinner__mutmut_6 # type: ignore # mutmut generated
