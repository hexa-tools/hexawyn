from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DiffHelmValuesCommand:
    release: str
    source_namespace: str
    target_namespace: str
    source_env: str = "staging"
    target_env: str = "production"
