"""CalicoSegmentationAuditUseCase — Calico east-west segmentation matrix."""

from __future__ import annotations

from hexawyn.application.ports.driven.calico_port import CalicoPort
from hexawyn.application.use_case.calico.calico_segmentation_audit.command import (
    CalicoSegmentationAuditCommand,
)
from hexawyn.application.use_case.calico.calico_segmentation_audit.response import (
    CalicoSegmentationAuditResponse,
)
from hexawyn.domain.services.calico.segmentation_service import (
    build_calico_segmentation_audit,
)


class CalicoSegmentationAuditUseCase:
    """Orchestrates the Calico segmentation matrix — depends only on ``CalicoPort``."""

    def __init__(self, port: CalicoPort) -> None:
        self._port = port

    def execute(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )
