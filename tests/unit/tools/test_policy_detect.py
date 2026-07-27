from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestPolicyDetectMCPTool:
    def test_returns_dict_with_error_none_on_success(self) -> None:
        from hexawyn.mcp.tools.policy_detect import policy_detect

        detection_result = MagicMock()
        detection_result.engine = MagicMock()
        detection_result.engine.value = "kyverno"
        detection_result.version = "v1.11.0"
        detection_result.namespace = "kyverno"
        detection_result.total_policies = 15
        detection_result.enforce_policies = 10
        detection_result.audit_policies = 5
        detection_result.total_violations = 3
        detection_result.high_severity = 1

        mock_port = MagicMock()
        mock_port.detect_engine.return_value = detection_result

        with patch(
            "hexawyn.mcp.server.build_policy_adapter",
            return_value=mock_port,
        ):
            result = policy_detect()

        assert isinstance(result, dict)
        assert result["error"] is None
        assert result["engine"] == "kyverno"
        assert result["total_policies"] == 15  # noqa: PLR2004

    def test_returns_error_on_exception(self) -> None:
        from hexawyn.mcp.tools.policy_detect import policy_detect

        with patch(
            "hexawyn.mcp.server.build_policy_adapter",
            side_effect=RuntimeError("no policy engine found"),
        ):
            result = policy_detect()

        assert isinstance(result, dict)
        assert "no policy engine found" in str(result["error"])
