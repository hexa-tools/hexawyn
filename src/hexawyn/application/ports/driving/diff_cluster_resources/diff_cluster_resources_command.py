from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DiffClusterResourcesCommand:
    source_context: str
    target_context: str
