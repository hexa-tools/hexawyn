from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

Severity = Literal["critical", "high", "medium"]
PSSLevel = Literal["Baseline", "Restricted"]
ViolationType = Literal[
    "privileged",
    "host_pid",
    "host_network",
    "host_ipc",
    "run_as_root",
    "allow_privilege_escalation",
    "dangerous_capability",
]
ContainerKind = Literal["init", "container", "ephemeral"]


@dataclass(frozen=True)
class ContainerSecurityContext:
    container_name: str
    container_kind: ContainerKind
    privileged: bool | None
    allow_privilege_escalation: bool | None
    run_as_non_root: bool | None
    added_capabilities: list[str]


@dataclass(frozen=True)
class PodSecuritySpec:
    pod_name: str
    namespace: str
    owner_kind: str | None
    pod_run_as_non_root: bool | None
    host_pid: bool
    host_network: bool
    host_ipc: bool
    containers: list[ContainerSecurityContext]


@dataclass(frozen=True)
class SecurityViolation:
    violation_type: ViolationType
    severity: Severity
    pss_level: PSSLevel
    container_name: str | None
    recommendation: str


@dataclass(frozen=True)
class PodSecurityFinding:
    pod_name: str
    namespace: str
    violations: list[SecurityViolation]
    note: str | None
    namespace_psa_enforce_level: str | None


@dataclass(frozen=True)
class PodSecurityAuditReport:
    findings: list[PodSecurityFinding]
    compliant_pod_count: int
    total_pods_checked: int
    summary: str
