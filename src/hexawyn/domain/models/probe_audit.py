from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class MissingProbe:
    deployment_name: str
    namespace: str
    missing: list[str]
    severity: str
    exposed_port: int
    readiness_suggestion: str
    liveness_suggestion: str
    has_service: bool
    workload_type: str
    is_exposed_externally: bool


@dataclass
class ProbeAuditResult:
    total_without_probes: int = 0
    critical: int = 0
    warning: int = 0
    informational: int = 0
    missing_probes: list[MissingProbe] = field(default_factory=list)
    misconfigured_probes: list[MissingProbe] = field(default_factory=list)
