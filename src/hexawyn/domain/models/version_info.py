from __future__ import annotations

from dataclasses import dataclass

UpdateStatus = str


@dataclass(frozen=True)
class VersionCheckResult:
    """Result of comparing the installed hexa version against the latest release."""

    current_version: str
    latest_version: str
    status: UpdateStatus
    error: str | None = None
