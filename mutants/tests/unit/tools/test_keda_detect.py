from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestKedaDetectMCPTool:
    def test_returns_dict_on_success(self) -> None:
        from hexawyn.mcp.tools.keda_detect import keda_detect

        detection_result = MagicMock()
        detection_result.installed = True
        detection_result.version = "2.10"
        detection_result.namespace = "keda"
        detection_result.total_scaledobjects = 5
        detection_result.ready_scaledobjects = 4
        detection_result.error_scaledobjects = 1
        detection_result.scaled_to_zero_count = 2
        detection_result.total_scaledjobs = 0
        detection_result.managed_namespaces = ["default"]

        mock_port = MagicMock()
        mock_port.detect.return_value = detection_result

        with patch(
            "hexawyn.mcp.server.build_keda_adapter",
            return_value=mock_port,
        ):
            result = keda_detect()

        assert isinstance(result, dict)
        assert result["error"] is None
        assert result["installed"] is True
        assert result["total_scaledobjects"] == 5  # noqa: PLR2004

    def test_returns_error_on_exception(self) -> None:
        from hexawyn.mcp.tools.keda_detect import keda_detect

        with patch(
            "hexawyn.mcp.server.build_keda_adapter",
            side_effect=RuntimeError("keda CRD not found"),
        ):
            result = keda_detect()

        assert isinstance(result, dict)
        assert "keda CRD not found" in str(result["error"])
