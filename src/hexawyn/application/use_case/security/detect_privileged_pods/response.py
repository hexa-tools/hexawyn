from __future__ import annotations

from dataclasses import dataclass
from typing import TypedDict


class SecurityViolationDict(TypedDict):
    violation_type: str
    severity: str
    pss_level: str
    container_name: str
    recommendation: str


class PodSecurityFindingDict(TypedDict):
    pod_name: str
    namespace: str
    violations: list[SecurityViolationDict]
    note: str
    namespace_psa_enforce_level: str | None


@dataclass
class DetectPrivilegedPodsResponse:
    findings: list[PodSecurityFindingDict] | None = None
    compliant_pod_count: int = 0
    total_pods_checked: int = 0
    summary: str = ""
    error: str | None = None
