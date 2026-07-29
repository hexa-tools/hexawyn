from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DetectUnintendedExternalExposureCommand:
    namespaces: list[str] | None = None
    allowlist: list[str] | None = None
