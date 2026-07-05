from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal, TypedDict


class SecurityViolationDict(TypedDict):
    violation_type: Literal[
        "privileged",
        "host_pid",
        "host_network",
        "host_ipc",
        "run_as_root",
        "allow_privilege_escalation",
        "dangerous_capability",
    ]
    severity: Literal["critical", "high", "medium"]
    pss_level: Literal["Baseline", "Restricted"]
    container_name: str | None
    recommendation: str


class PodSecurityFindingDict(TypedDict):
    pod_name: str
    namespace: str
    violations: list[SecurityViolationDict]
    note: str | None
    namespace_psa_enforce_level: str | None


@dataclass
class DetectPrivilegedPodsResponse:
    findings: list[PodSecurityFindingDict] = field(default_factory=list)
    compliant_pod_count: int = 0
    total_pods_checked: int = 0
    summary: str = ""
    error: str | None = None
