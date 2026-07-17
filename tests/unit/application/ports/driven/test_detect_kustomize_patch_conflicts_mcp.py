"""RED → GREEN — MCP tool: detect_kustomize_patch_conflicts."""

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.kustomize_patch_analysis_port import (
    KustomizePatchAnalysisPort,
    PatchFieldRawData,
)
from hexawyn.domain.errors import KustomizeNotFoundError


class TestDetectKustomizePatchConflictsTool:
    def test_delegates_and_returns_dict(self) -> None:
        mock_port = MagicMock(spec=KustomizePatchAnalysisPort)
        mock_port.extract_patch_fields.return_value = [
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
        mock_port.extract_base_fields.return_value = []

        with patch(
            "hexawyn.mcp.server.build_kustomize_patch_analysis_adapter",
            return_value=mock_port,
        ):
            from hexawyn.mcp.tools.detect_kustomize_patch_conflicts import (
                detect_kustomize_patch_conflicts,
            )

            result = detect_kustomize_patch_conflicts(overlay_path="overlays/production")

        assert result["total_conflicts"] == 1
        assert result["patch_conflicts"][0]["effective_value"] == "5"
        assert result["error"] is None

    def test_handles_exception_gracefully(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_kustomize_patch_analysis_adapter",
            side_effect=KustomizeNotFoundError(),
        ):
            from hexawyn.mcp.tools.detect_kustomize_patch_conflicts import (
                detect_kustomize_patch_conflicts,
            )

            result = detect_kustomize_patch_conflicts(overlay_path="test")

        assert result["total_conflicts"] == 0
        assert "kustomize" in result["error"].lower()

    def test_has_register_function(self) -> None:
        from hexawyn.mcp.tools.detect_kustomize_patch_conflicts import register

        assert callable(register)
