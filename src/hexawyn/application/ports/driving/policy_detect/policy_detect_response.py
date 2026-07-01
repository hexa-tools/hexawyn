from __future__ import annotations

from dataclasses import dataclass


@dataclass
class PolicyDetectResponse:
    engine: str = "unknown"
    version: str | None = None
    namespace: str | None = None
    total_policies: int = 0
    enforce_policies: int = 0
    audit_policies: int = 0
    total_violations: int = 0
    high_severity: int = 0
    error: str | None = None
