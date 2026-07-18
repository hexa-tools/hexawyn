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


def shortcut_to_cron(expression: str) -> str | None:
    """Convert a time shortcut like ``6h`` to a cron expression.

    Returns the expression unchanged if it already looks like a cron string
    (contains spaces), or the shortcut mapping if known, or None.
    """
    stripped = expression.strip()
    if " " in stripped:
        return stripped
    return _CRON_SHORTCUTS.get(stripped)


def cron_to_minutes(cron_expr: str) -> int:
    """Convert a cron expression to its approximate interval in minutes.

    Returns 0 for expressions not in the shortcut mapping.
    """
    return _CRON_TO_MINUTES.get(cron_expr.strip(), 0)
