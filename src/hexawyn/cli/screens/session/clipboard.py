"""Clipboard and export helpers for the session screen.

Platform-specific subprocess calls (pbcopy / wl-copy / xclip / open / xdg-open)
live here so the Textual screen stays focused on rendering and delegation and
the helpers stay unit-testable by mocking `platform` / `subprocess`.
"""

from __future__ import annotations

import platform
import subprocess
import tempfile

_COPIED = "✓ Copied to clipboard"
_SYSTEM_MISSING = "✗ Install xclip or wl-clipboard to enable copy"
_FAILED = "✗ Copy failed: {exc}"
_UNSUPPORTED = "✗ Copy not supported on {system}"

_MAC_COPY = ["pbcopy"]
_LINUX_COPY_TOOLS = (["wl-copy"], ["xclip", "-selection", "c"])


def copy_to_clipboard(text: str) -> str:
    """Copy ``text`` to the system clipboard and return a message string."""
    system = platform.system()
    try:
        if system == "Darwin":
            subprocess.run(_MAC_COPY, input=text.encode(), check=True)
            return _COPIED
        if system == "Linux":
            for cmd in _LINUX_COPY_TOOLS:
                try:
                    subprocess.run(cmd, input=text.encode(), check=True)
                    return _COPIED
                except (FileNotFoundError, subprocess.CalledProcessError):
                    continue
            return _SYSTEM_MISSING
        return _UNSUPPORTED.format(system=system)
    except Exception as exc:  # noqa: BLE001 - never surface a clipboard failure
        return _FAILED.format(exc=exc)


def write_export_file(text: str) -> str:
    """Write ``text`` to a temp file and return its path."""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".txt", delete=False, encoding="utf-8"
    ) as handle:  # noqa: E501
        handle.write(text)
        return str(handle.name)


def open_in_editor(path: str) -> None:
    """Open ``path`` in the platform default editor."""
    system = platform.system()
    if system == "Darwin":
        subprocess.Popen(["open", path])
    elif system == "Linux":
        subprocess.Popen(["xdg-open", path])
