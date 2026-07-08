from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RolloutsListCommand:
    namespace: str | None = None
