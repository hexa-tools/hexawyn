from __future__ import annotations

import re

_CRON_SHORTCUTS: dict[str, str] = {
    "15m": "*/15 * * * *",
    "30m": "*/30 * * * *",
    "1h": "0 * * * *",
    "6h": "0 */6 * * *",
    "12h": "0 */12 * * *",
    "24h": "0 0 * * *",
}
_CRON_TO_MINUTES: dict[str, int] = {
    "*/15 * * * *": 15,
    "*/30 * * * *": 30,
    "0 * * * *": 60,
    "0 */6 * * *": 360,
    "0 */12 * * *": 720,
    "0 0 * * *": 1440,
}
_CRON_PATTERN = re.compile(r"^(\*|\d+)(\s+(\*|\d+)(\s+(\*|\d+)(\s+(\*|\d+)(\s+(\*|\d+))?)?)?)?$")


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_shortcut_to_cron__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_shortcut_to_cron__mutmut)
def shortcut_to_cron(expression: str) -> str | None:
    """Convert a time shortcut like ``6h`` to a cron expression.

    Returns the expression unchanged if it already looks like a cron string
    (contains spaces), or the shortcut mapping if known, or None.
    """
    stripped = expression.strip()
    if " " in stripped:
        return stripped
    return _CRON_SHORTCUTS.get(stripped)


def x_shortcut_to_cron__mutmut_orig(expression: str) -> str | None:
    """Convert a time shortcut like ``6h`` to a cron expression.

    Returns the expression unchanged if it already looks like a cron string
    (contains spaces), or the shortcut mapping if known, or None.
    """
    stripped = expression.strip()
    if " " in stripped:
        return stripped
    return _CRON_SHORTCUTS.get(stripped)


def x_shortcut_to_cron__mutmut_1(expression: str) -> str | None:
    """Convert a time shortcut like ``6h`` to a cron expression.

    Returns the expression unchanged if it already looks like a cron string
    (contains spaces), or the shortcut mapping if known, or None.
    """
    stripped = None
    if " " in stripped:
        return stripped
    return _CRON_SHORTCUTS.get(stripped)


def x_shortcut_to_cron__mutmut_2(expression: str) -> str | None:
    """Convert a time shortcut like ``6h`` to a cron expression.

    Returns the expression unchanged if it already looks like a cron string
    (contains spaces), or the shortcut mapping if known, or None.
    """
    stripped = expression.strip()
    if "XX XX" in stripped:
        return stripped
    return _CRON_SHORTCUTS.get(stripped)


def x_shortcut_to_cron__mutmut_3(expression: str) -> str | None:
    """Convert a time shortcut like ``6h`` to a cron expression.

    Returns the expression unchanged if it already looks like a cron string
    (contains spaces), or the shortcut mapping if known, or None.
    """
    stripped = expression.strip()
    if " " not in stripped:
        return stripped
    return _CRON_SHORTCUTS.get(stripped)


def x_shortcut_to_cron__mutmut_4(expression: str) -> str | None:
    """Convert a time shortcut like ``6h`` to a cron expression.

    Returns the expression unchanged if it already looks like a cron string
    (contains spaces), or the shortcut mapping if known, or None.
    """
    stripped = expression.strip()
    if " " in stripped:
        return stripped
    return _CRON_SHORTCUTS.get(None)

mutants_x_shortcut_to_cron__mutmut['_mutmut_orig'] = x_shortcut_to_cron__mutmut_orig # type: ignore # mutmut generated
mutants_x_shortcut_to_cron__mutmut['x_shortcut_to_cron__mutmut_1'] = x_shortcut_to_cron__mutmut_1 # type: ignore # mutmut generated
mutants_x_shortcut_to_cron__mutmut['x_shortcut_to_cron__mutmut_2'] = x_shortcut_to_cron__mutmut_2 # type: ignore # mutmut generated
mutants_x_shortcut_to_cron__mutmut['x_shortcut_to_cron__mutmut_3'] = x_shortcut_to_cron__mutmut_3 # type: ignore # mutmut generated
mutants_x_shortcut_to_cron__mutmut['x_shortcut_to_cron__mutmut_4'] = x_shortcut_to_cron__mutmut_4 # type: ignore # mutmut generated
mutants_x_cron_to_minutes__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_cron_to_minutes__mutmut)
def cron_to_minutes(cron_expr: str) -> int:
    """Convert a cron expression to its approximate interval in minutes.

    Returns 0 for expressions not in the shortcut mapping.
    """
    return _CRON_TO_MINUTES.get(cron_expr.strip(), 0)


def x_cron_to_minutes__mutmut_orig(cron_expr: str) -> int:
    """Convert a cron expression to its approximate interval in minutes.

    Returns 0 for expressions not in the shortcut mapping.
    """
    return _CRON_TO_MINUTES.get(cron_expr.strip(), 0)


def x_cron_to_minutes__mutmut_1(cron_expr: str) -> int:
    """Convert a cron expression to its approximate interval in minutes.

    Returns 0 for expressions not in the shortcut mapping.
    """
    return _CRON_TO_MINUTES.get(None, 0)


def x_cron_to_minutes__mutmut_2(cron_expr: str) -> int:
    """Convert a cron expression to its approximate interval in minutes.

    Returns 0 for expressions not in the shortcut mapping.
    """
    return _CRON_TO_MINUTES.get(cron_expr.strip(), None)


def x_cron_to_minutes__mutmut_3(cron_expr: str) -> int:
    """Convert a cron expression to its approximate interval in minutes.

    Returns 0 for expressions not in the shortcut mapping.
    """
    return _CRON_TO_MINUTES.get(0)


def x_cron_to_minutes__mutmut_4(cron_expr: str) -> int:
    """Convert a cron expression to its approximate interval in minutes.

    Returns 0 for expressions not in the shortcut mapping.
    """
    return _CRON_TO_MINUTES.get(cron_expr.strip(), )


def x_cron_to_minutes__mutmut_5(cron_expr: str) -> int:
    """Convert a cron expression to its approximate interval in minutes.

    Returns 0 for expressions not in the shortcut mapping.
    """
    return _CRON_TO_MINUTES.get(cron_expr.strip(), 1)

mutants_x_cron_to_minutes__mutmut['_mutmut_orig'] = x_cron_to_minutes__mutmut_orig # type: ignore # mutmut generated
mutants_x_cron_to_minutes__mutmut['x_cron_to_minutes__mutmut_1'] = x_cron_to_minutes__mutmut_1 # type: ignore # mutmut generated
mutants_x_cron_to_minutes__mutmut['x_cron_to_minutes__mutmut_2'] = x_cron_to_minutes__mutmut_2 # type: ignore # mutmut generated
mutants_x_cron_to_minutes__mutmut['x_cron_to_minutes__mutmut_3'] = x_cron_to_minutes__mutmut_3 # type: ignore # mutmut generated
mutants_x_cron_to_minutes__mutmut['x_cron_to_minutes__mutmut_4'] = x_cron_to_minutes__mutmut_4 # type: ignore # mutmut generated
mutants_x_cron_to_minutes__mutmut['x_cron_to_minutes__mutmut_5'] = x_cron_to_minutes__mutmut_5 # type: ignore # mutmut generated
