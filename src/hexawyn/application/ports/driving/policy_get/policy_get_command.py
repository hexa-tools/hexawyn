from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PolicyGetCommand:
    name: str
    namespace: str | None = None
