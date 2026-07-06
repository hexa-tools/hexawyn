from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DetectUnintendedExternalExposureCommand:
    allowlist: list[str] | None = None
    namespaces: list[str] | None = None
