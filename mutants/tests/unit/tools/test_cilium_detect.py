from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestCiliumDetectMCPTool:
    def test_returns_dict_on_success(self) -> None:
        from hexawyn.mcp.tools.cilium_detect import cilium_detect

        detection_result = MagicMock()
        detection_result.installed = True
        detection_result.status = "installed"
        detection_result.version = "v1.16.3"
        detection_result.mode = "tunnel"
        detection_result.namespace = "kube-system"
        detection_result.total_agents = 3
        detection_result.ready_agents = 3
        detection_result.degraded_summary = None
        detection_result.agents = []
        detection_result.note = None

        mock_port = MagicMock()
        mock_port.detect.return_value = detection_result

        with patch(
            "hexawyn.mcp.server.build_cilium_adapter",
            return_value=mock_port,
        ):
            result = cilium_detect()

        assert isinstance(result, dict)
        assert result["error"] is None
        assert result["installed"] is True
        assert result["mode"] == "tunnel"

    def test_returns_error_on_exception(self) -> None:
        from hexawyn.mcp.tools.cilium_detect import cilium_detect

        with patch(
            "hexawyn.mcp.server.build_cilium_adapter",
            side_effect=RuntimeError("cilium CRD not found"),
        ):
            result = cilium_detect()

        assert isinstance(result, dict)
        assert "cilium CRD not found" in str(result["error"])
