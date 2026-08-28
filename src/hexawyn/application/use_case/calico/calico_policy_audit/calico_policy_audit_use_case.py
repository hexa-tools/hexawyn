"""CalicoPolicyAuditUseCase — audit Calico L3/L4 (and L7) coverage gaps."""

from __future__ import annotations

from hexawyn.application.ports.driven.calico_port import CalicoPort
from hexawyn.application.use_case.calico.calico_policy_audit.command import (
    CalicoPolicyAuditCommand,
)
from hexawyn.application.use_case.calico.calico_policy_audit.response import (
    CalicoPolicyAuditResponse,
)
from hexawyn.domain.services.calico.policy_audit_service import (
    build_calico_policy_audit,
)


class CalicoPolicyAuditUseCase:
    """Orchestrates the Calico coverage audit — depends only on ``CalicoPort``."""

    def __init__(self, port: CalicoPort) -> None:
        self._port = port

    def execute(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                gap_count=0,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=list(result.findings),
            summary=result.summary,
            error=result.error,
        )
