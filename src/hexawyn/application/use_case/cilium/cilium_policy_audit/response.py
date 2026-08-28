from __future__ import annotations

from dataclasses import dataclass
from typing import TypedDict


class CiliumAuditFindingOutput(TypedDict):
    namespace: str
    workload: str
    coverage: str
    ingress_restricted: bool
    egress_restricted: bool
    l7_restricted: bool
    risk: str
    note: str | None


@dataclass
class CiliumPolicyAuditResponse:
    installed: bool = False
    status: str = "not_installed"
    view: str = "vanilla"
    total_workloads: int = 0
    uncovered_count: int = 0
    findings: list[CiliumAuditFindingOutput] | None = None
    summary: str = ""
    note: str | None = None
    error: str | None = None
