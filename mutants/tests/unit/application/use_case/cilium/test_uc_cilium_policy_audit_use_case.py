from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.cilium.cilium_policy_audit.cilium_policy_audit_use_case import (
    CiliumPolicyAuditUseCase,
)
from hexawyn.application.use_case.cilium.cilium_policy_audit.command import (
    CiliumPolicyAuditCommand,
)
from hexawyn.application.use_case.cilium.cilium_policy_audit.response import (
    CiliumPolicyAuditResponse,
)
from hexawyn.domain.models.cilium import CiliumAuditFinding, CiliumPolicyAuditResult


class TestCiliumPolicyAuditUseCase:
    def test_execute_returns_findings(self) -> None:
        result = CiliumPolicyAuditResult(
            installed=True,
            status="gaps_found",
            view="cilium",
            total_workloads=2,
            uncovered_count=1,
            findings=[
                CiliumAuditFinding(
                    namespace="payments",
                    workload="web-0",
                    coverage="no_policy",
                    ingress_restricted=False,
                    egress_restricted=False,
                    l7_restricted=False,
                    risk="critical",
                    note="No Cilium network policy selects this workload",
                )
            ],
            summary="1 workload(s) with a coverage gap out of 2",
            note=None,
        )
        port = MagicMock()
        port.audit_policies.return_value = result

        response = CiliumPolicyAuditUseCase(port=port).execute(CiliumPolicyAuditCommand())

        assert isinstance(response, CiliumPolicyAuditResponse)
        assert response.status == "gaps_found"
        assert response.view == "cilium"
        assert response.findings == [
            {
                "namespace": "payments",
                "workload": "web-0",
                "coverage": "no_policy",
                "ingress_restricted": False,
                "egress_restricted": False,
                "l7_restricted": False,
                "risk": "critical",
                "note": "No Cilium network policy selects this workload",
            }
        ]

    def test_execute_not_installed_vanilla_view(self) -> None:
        result = CiliumPolicyAuditResult(
            installed=False,
            status="not_installed",
            view="vanilla",
            total_workloads=0,
            uncovered_count=0,
            findings=[],
            summary="Cilium is not installed; vanilla NetworkPolicy view is out of scope",
            note="Cilium is not installed in this cluster",
        )
        port = MagicMock()
        port.audit_policies.return_value = result

        response = CiliumPolicyAuditUseCase(port=port).execute(CiliumPolicyAuditCommand())

        assert response.installed is False
        assert response.view == "vanilla"
        assert response.findings == []
