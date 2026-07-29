from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal, TypedDict

ComplianceCategory = Literal["tls", "rbac", "pod_security", "image_scanning", "secret_rotation"]
ComplianceStatus = Literal["compliant", "non_compliant", "exempt", "policy_not_defined"]
PostureTrend = Literal["improving", "degrading", "stable"]


class WorkloadComplianceRaw(TypedDict):
    workload: str
    namespace: str
    category: str
    compliant: bool
    exempt: bool
    detail: str


@dataclass(frozen=True)
class WorkloadCompliance:
    workload: str
    namespace: str
    category: str
    status: str
    remediation_priority: int
    detail: str


@dataclass(frozen=True)
class CategoryScore:
    category: str
    total: int
    compliant: int
    non_compliant: int
    exempt: int
    score_pct: float
    policy_defined: bool
    non_compliant_workloads: list[WorkloadCompliance]


@dataclass
class SecurityPostureReport:
    overall_score_pct: float
    categories: list[CategoryScore] = field(default_factory=list)
    remediation_order: list[WorkloadCompliance] = field(default_factory=list)
    trend: str = "stable"
    previous_score_pct: float | None = None
    partial: bool = False
    warning: str = ""
