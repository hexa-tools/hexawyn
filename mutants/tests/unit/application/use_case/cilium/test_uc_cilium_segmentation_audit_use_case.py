from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.cilium.cilium_segmentation_audit.cilium_segmentation_audit_use_case import (  # noqa: E501
    CiliumSegmentationAuditUseCase,
)
from hexawyn.application.use_case.cilium.cilium_segmentation_audit.command import (
    CiliumSegmentationAuditCommand,
)
from hexawyn.application.use_case.cilium.cilium_segmentation_audit.response import (
    CiliumSegmentationAuditResponse,
)
from hexawyn.domain.models.cilium import (
    CiliumPathFinding,
    CiliumSegmentationAuditResult,
)


class TestCiliumSegmentationAuditUseCase:
    def test_execute_returns_findings(self) -> None:
        result = CiliumSegmentationAuditResult(
            installed=True,
            status="gaps_found",
            view="cilium",
            total_identities=2,
            total_paths=2,
            uncovered_paths=1,
            findings=[
                CiliumPathFinding(
                    source_id="100",
                    destination_id="200",
                    source_labels=("app=web",),
                    destination_labels=("app=db",),
                    severity="high",
                    note="unrestricted",
                )
            ],
            summary="1 unrestricted path(s) out of 2",
            note=None,
        )
        port = MagicMock()
        port.segmentation_audit.return_value = result

        response = CiliumSegmentationAuditUseCase(port=port).execute(
            CiliumSegmentationAuditCommand()
        )

        assert isinstance(response, CiliumSegmentationAuditResponse)
        assert response.status == "gaps_found"
        assert response.view == "cilium"
        assert response.findings == [
            {
                "source_id": "100",
                "destination_id": "200",
                "source_labels": ["app=web"],
                "destination_labels": ["app=db"],
                "severity": "high",
                "note": "unrestricted",
            }
        ]

    def test_execute_not_installed_vanilla_view(self) -> None:
        result = CiliumSegmentationAuditResult(
            installed=False,
            status="not_installed",
            view="vanilla",
            total_identities=0,
            total_paths=0,
            uncovered_paths=0,
            findings=[],
            summary="Cilium is not installed; vanilla NetworkPolicy view is out of scope",
            note="Cilium is not installed in this cluster",
        )
        port = MagicMock()
        port.segmentation_audit.return_value = result

        response = CiliumSegmentationAuditUseCase(port=port).execute(
            CiliumSegmentationAuditCommand()
        )

        assert response.installed is False
        assert response.view == "vanilla"
        assert response.findings == []
