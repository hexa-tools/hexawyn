from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DetectNetworkSegmentationGapsCommand:
    namespaces: list[str] | None = None
