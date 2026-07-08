from __future__ import annotations

from dataclasses import dataclass


@dataclass
class PolicyGetResponse:
    name: str = ""
    namespace: str | None = None
    engine: str = "unknown"
    kind: str = ""
    action: str = "unknown"
    description: str | None = None
    rules_count: int = 0
    violations_count: int = 0
    ready: bool = False
    error: str | None = None
