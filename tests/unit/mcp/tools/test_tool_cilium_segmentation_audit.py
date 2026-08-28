"""Unit tests for MCP tool: cilium_segmentation_audit."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestCiliumSegmentationAuditTool:
    def test_cilium_segmentation_audit_returns_dict(self) -> None:
        from hexawyn.mcp.tools.cilium_segmentation_audit import (
            cilium_segmentation_audit,
        )

        mock_finding = MagicMock()
        mock_finding.source_id = "100"
        mock_response = MagicMock()
        mock_response.installed = True
        mock_response.status = "gaps_found"
        mock_response.view = "cilium"
        mock_response.total_identities = 2
        mock_response.total_paths = 2
        mock_response.uncovered_paths = 1
        mock_response.findings = [mock_finding]
        mock_response.summary = "1 unrestricted path(s) out of 2"
        mock_response.note = None
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_cilium_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.cilium_segmentation_audit.CiliumSegmentationAuditUseCase",
                return_value=mock_uc,
            ),
        ):
            result = cilium_segmentation_audit()

        assert isinstance(result, dict)
        assert result["installed"] is True
        assert result["status"] == "gaps_found"
        assert result["view"] == "cilium"
        assert result["error"] is None

    def test_cilium_segmentation_audit_error_returns_unknown(self) -> None:
        from hexawyn.mcp.tools.cilium_segmentation_audit import (
            cilium_segmentation_audit,
        )

        with patch(
            "hexawyn.mcp.server.build_cilium_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = cilium_segmentation_audit()

        assert isinstance(result, dict)
        assert result["installed"] is False
        assert result["status"] == "unknown"
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.cilium_segmentation_audit")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
