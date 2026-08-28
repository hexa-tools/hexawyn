from __future__ import annotations

from hexawyn.application.ports.driven.cilium_port import CiliumPort
from hexawyn.application.use_case.cilium.cilium_segmentation_audit.command import (
    CiliumSegmentationAuditCommand,
)
from hexawyn.application.use_case.cilium.cilium_segmentation_audit.response import (
    CiliumPathFindingOutput,
    CiliumSegmentationAuditResponse,
)
from hexawyn.domain.models.cilium import CiliumPathFinding


class CiliumSegmentationAuditUseCase:
    def __init__(self, port: CiliumPort) -> None:
        self._port = port

    def execute(self, command: CiliumSegmentationAuditCommand) -> CiliumSegmentationAuditResponse:
        result = self._port.segmentation_audit()
        findings: list[CiliumPathFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumSegmentationAuditResponse(
            installed=result.installed,
            status=result.status,
            view=result.view,
            total_identities=result.total_identities,
            total_paths=result.total_paths,
            uncovered_paths=result.uncovered_paths,
            findings=findings,
            summary=result.summary,
            note=result.note,
        )

    @staticmethod
    def _to_finding(finding: CiliumPathFinding) -> CiliumPathFindingOutput:
        return {
            "source_id": finding.source_id,
            "destination_id": finding.destination_id,
            "source_labels": list(finding.source_labels),
            "destination_labels": list(finding.destination_labels),
            "severity": finding.severity,
            "note": finding.note,
        }
