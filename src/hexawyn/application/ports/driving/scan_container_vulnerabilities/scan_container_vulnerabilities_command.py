from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ScanContainerVulnerabilitiesCommand:
    namespaces: list[str] | None = None
