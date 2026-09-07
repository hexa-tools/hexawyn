"""Unit tests for MCP tool: calico_segmentation_audit."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestCalicoSegmentationAuditTool:
    def test_returns_dict(self) -> None:
        from hexawyn.mcp.tools.calico_segmentation_audit import calico_segmentation_audit

        mock_response = MagicMock()
        mock_response.installed = True
        mock_response.not_installed_marker = None
        mock_response.view = "calico"
        mock_response.tiers = ["ns1", "ns2"]
        mock_response.edges = []
        mock_response.gap_count = 0
        mock_response.total_paths = 2
        mock_response.summary = "No unrestricted tier-to-tier paths out of 2."
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_calico_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.calico_segmentation_audit.CalicoSegmentationAuditUseCase",
                return_value=mock_uc,
            ),
        ):
            result = calico_segmentation_audit()

        assert isinstance(result, dict)
        assert result["installed"] is True
        assert result["view"] == "calico"
        assert result["total_paths"] == 2  # noqa: PLR2004
        assert result["error"] is None

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.calico_segmentation_audit import calico_segmentation_audit

        with patch(
            "hexawyn.mcp.server.build_calico_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = calico_segmentation_audit()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"
        assert result.get("installed") is False
        assert result.get("view") == "vanilla"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.calico_segmentation_audit")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))

    def test_edge_dict(self) -> None:
        from hexawyn.domain.models.calico import CalicoSegmentationEdge
        from hexawyn.mcp.tools.calico_segmentation_audit import _edge_dict

        edge = CalicoSegmentationEdge(
            source="ns1",
            destination="ns2",
            restricted=False,
            selectors=["app=='web'"],
            note="Allowed by default (no default-deny)",
        )
        result = _edge_dict(edge)

        assert result["source"] == "ns1"
        assert result["destination"] == "ns2"
        assert result["restricted"] is False
        assert result["selectors"] == ["app=='web'"]
