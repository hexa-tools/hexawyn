"""Unit tests for the detect_unintended_external_exposure MCP tool."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestDetectUnintendedExternalExposureTool:
    def test_tool_returns_findings_from_service(self) -> None:
        from hexawyn.mcp.tools.detect_unintended_external_exposure import (
            detect_unintended_external_exposure,
        )

        with patch("hexawyn.mcp.server.build_external_exposure_audit_adapter") as build_adapter:
            port = MagicMock()
            port.list_external_services.return_value = []
            build_adapter.return_value = port

            result = detect_unintended_external_exposure(
                allowlist=["api-gateway"],
                namespaces=["production"],
            )

        assert "findings" in result
        assert "excluded_exposures" in result
        assert "total_external_services_checked" in result
        assert "summary" in result
        assert "error" in result

    def test_tool_defaults_allowlist_and_namespaces_to_none(self) -> None:
        from hexawyn.mcp.tools.detect_unintended_external_exposure import (
            detect_unintended_external_exposure,
        )

        with patch("hexawyn.mcp.server.build_external_exposure_audit_adapter") as build_adapter:
            port = MagicMock()
            port.list_external_services.return_value = []
            build_adapter.return_value = port

            result = detect_unintended_external_exposure()

        assert result["error"] is None

    def test_tool_handles_exception_gracefully(self) -> None:
        from hexawyn.mcp.tools.detect_unintended_external_exposure import (
            detect_unintended_external_exposure,
        )

        with patch(
            "hexawyn.mcp.server.build_external_exposure_audit_adapter",
            side_effect=RuntimeError("K8s API unavailable"),
        ):
            result = detect_unintended_external_exposure()

        assert result["error"] is not None
        assert "K8s API unavailable" in str(result["error"])

    def test_register_calls_mcp_tool(self) -> None:
        from hexawyn.mcp.tools.detect_unintended_external_exposure import register

        mock_mcp = MagicMock()
        mock_tool_decorator = MagicMock()
        mock_mcp.tool.return_value = mock_tool_decorator

        register(mock_mcp)

        mock_mcp.tool.assert_called_once()
        mock_tool_decorator.assert_called_once()
