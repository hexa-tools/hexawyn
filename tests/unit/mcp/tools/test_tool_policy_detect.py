"""Unit tests for MCP tool: policy_detect."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestPolicyDetectTool:
    def test_policy_detect_returns_dict(self) -> None:
        from hexawyn.mcp.tools.policy_detect import policy_detect

        mock_response = MagicMock()
        mock_response.engine = "kyverno"
        mock_response.version = "1.0"
        mock_response.namespace = "kyverno"
        mock_response.total_policies = 5
        mock_response.enforce_policies = 3
        mock_response.audit_policies = 2
        mock_response.total_violations = 1
        mock_response.high_severity = 0
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_policy_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.policy_detect.PolicyDetectUseCase",
                return_value=mock_uc,
            ),
        ):
            result = policy_detect()

        assert isinstance(result, dict)
        assert result["engine"] == "kyverno"

    def test_policy_detect_handles_error(self) -> None:
        from hexawyn.mcp.tools.policy_detect import policy_detect

        with patch(
            "hexawyn.mcp.server.build_policy_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = policy_detect()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.policy_detect")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
