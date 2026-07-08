"""RED → GREEN — Layers 3-6: driven port, driving ports, app service, use case."""

import inspect
from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driven.kustomize_patch_analysis_port import (
    BaseFieldRawData,
    KustomizePatchAnalysisPort,
    PatchFieldRawData,
)
from hexawyn.application.ports.driving.detect_kustomize_patch_conflicts.detect_kustomize_patch_conflicts_command import (
    DetectKustomizePatchConflictsCommand,
)
from hexawyn.application.ports.driving.detect_kustomize_patch_conflicts.detect_kustomize_patch_conflicts_response import (
    DetectKustomizePatchConflictsResponse,
)
from hexawyn.application.ports.driving.detect_kustomize_patch_conflicts.detect_kustomize_patch_conflicts_service_port import (
    DetectKustomizePatchConflictsServicePort,
)
from hexawyn.application.service.detect_kustomize_patch_conflicts_service import (
    DetectKustomizePatchConflictsService,
)
from hexawyn.application.use_case.detect_kustomize_patch_conflicts.detect_kustomize_patch_conflicts_use_case import (
    DetectKustomizePatchConflictsUseCase,
)
from hexawyn.domain.models.kustomize_patch_conflict import (
    KustomizePatchConflictReport,
)


class TestKustomizePatchAnalysisPort:
    def test_is_abstract(self) -> None:
        assert inspect.isabstract(KustomizePatchAnalysisPort)

    def test_concrete_impl_must_implement_methods(self) -> None:
        class Bad(KustomizePatchAnalysisPort):
            pass

        with pytest.raises(TypeError):
            Bad()  # type: ignore[abstract]


class TestDetectKustomizePatchConflictsCommand:
    def test_holds_overlay_path(self) -> None:
        cmd = DetectKustomizePatchConflictsCommand(overlay_path="overlays/production")
        assert cmd.overlay_path == "overlays/production"

    def test_is_frozen(self) -> None:
        cmd = DetectKustomizePatchConflictsCommand(overlay_path="test")
        with pytest.raises(Exception):
            cmd.overlay_path = "other"  # type: ignore[misc]


class TestDetectKustomizePatchConflictsResponse:
    def test_holds_result(self) -> None:
        inner = KustomizePatchConflictReport(
            overlay_path="overlays/prod",
            total_conflicts=2,
        )
        resp = DetectKustomizePatchConflictsResponse(result=inner)
        assert resp.result is inner


class TestDetectKustomizePatchConflictsService:
    def _mock_port(self) -> MagicMock:
        port = MagicMock(spec=KustomizePatchAnalysisPort)
        port.extract_patch_fields.return_value = []
        port.extract_base_fields.return_value = []
        return port

    def test_calls_port_with_overlay_path(self) -> None:
        port = self._mock_port()
        service = DetectKustomizePatchConflictsService(analysis_port=port)

        service.detect_conflicts(DetectKustomizePatchConflictsCommand(overlay_path="overlays/prod"))

        port.extract_patch_fields.assert_called_once_with("overlays/prod")
        port.extract_base_fields.assert_called_once_with("overlays/prod")

    def test_detects_conflict_from_patch_data(self) -> None:
        port = MagicMock(spec=KustomizePatchAnalysisPort)
        port.extract_patch_fields.return_value = [
            PatchFieldRawData(
                field_path="spec.replicas",
                resource="Deployment/payment-service",
                value="2",
                source_file="patches/a.yaml",
                patch_type="strategic_merge",
                order=0,
            ),
            PatchFieldRawData(
                field_path="spec.replicas",
                resource="Deployment/payment-service",
                value="5",
                source_file="patches/b.yaml",
                patch_type="strategic_merge",
                order=1,
            ),
        ]
        port.extract_base_fields.return_value = [
            BaseFieldRawData(
                field_path="spec.replicas",
                resource="Deployment/payment-service",
                value="1",
            ),
        ]
        service = DetectKustomizePatchConflictsService(analysis_port=port)

        response = service.detect_conflicts(
            DetectKustomizePatchConflictsCommand(overlay_path="test")
        )

        assert response.result.total_conflicts == 1
        assert response.result.patch_conflicts[0].effective_value == "5"

    def test_returns_response_with_result(self) -> None:
        port = self._mock_port()
        service = DetectKustomizePatchConflictsService(analysis_port=port)

        response = service.detect_conflicts(
            DetectKustomizePatchConflictsCommand(overlay_path="test")
        )

        assert isinstance(response, DetectKustomizePatchConflictsResponse)
        assert isinstance(response.result, KustomizePatchConflictReport)


class TestDetectKustomizePatchConflictsUseCase:
    def test_delegates_to_service(self) -> None:
        service = MagicMock(spec=DetectKustomizePatchConflictsServicePort)
        inner = KustomizePatchConflictReport(total_conflicts=1)
        service.detect_conflicts.return_value = DetectKustomizePatchConflictsResponse(result=inner)
        use_case = DetectKustomizePatchConflictsUseCase(service=service)

        result = use_case.execute(DetectKustomizePatchConflictsCommand(overlay_path="test"))

        service.detect_conflicts.assert_called_once()
        assert result.result is inner
