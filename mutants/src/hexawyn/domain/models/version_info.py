from __future__ import annotations

from dataclasses import dataclass

UpdateStatus = str


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class VersionCheckResult:
    """Result of comparing the installed hexa version against the latest release."""

    current_version: str
    latest_version: str
    status: UpdateStatus
    error: str | None = None
