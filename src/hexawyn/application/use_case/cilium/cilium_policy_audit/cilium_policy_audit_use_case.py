from __future__ import annotations

from hexawyn.application.ports.driven.cilium_port import CiliumPort
from hexawyn.application.use_case.cilium.cilium_policy_audit.command import (
    CiliumPolicyAuditCommand,
)
from hexawyn.application.use_case.cilium.cilium_policy_audit.response import (
    CiliumAuditFindingOutput,
    CiliumPolicyAuditResponse,
)
from hexawyn.domain.models.cilium import CiliumAuditFinding


class CiliumPolicyAuditUseCase:
    def __init__(self, port: CiliumPort) -> None:
        self._port = port

    def execute(self, command: CiliumPolicyAuditCommand) -> CiliumPolicyAuditResponse:
        result = self._port.audit_policies()
        findings: list[CiliumAuditFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumPolicyAuditResponse(
            installed=result.installed,
            status=result.status,
            view=result.view,
            total_workloads=result.total_workloads,
            uncovered_count=result.uncovered_count,
            findings=findings,
            summary=result.summary,
            note=result.note,
        )

    @staticmethod
    def _to_finding(finding: CiliumAuditFinding) -> CiliumAuditFindingOutput:
        return {
            "namespace": finding.namespace,
            "workload": finding.workload,
            "coverage": finding.coverage,
            "ingress_restricted": finding.ingress_restricted,
            "egress_restricted": finding.egress_restricted,
            "l7_restricted": finding.l7_restricted,
            "risk": finding.risk,
            "note": finding.note,
        }
