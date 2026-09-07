"""Unit tests for MCP tool: calico_policy_audit."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestCalicoPolicyAuditTool:
    def test_returns_dict(self) -> None:
        from hexawyn.mcp.tools.calico_policy_audit import calico_policy_audit

        mock_response = MagicMock()
        mock_response.installed = True
        mock_response.not_installed_marker = None
        mock_response.degraded_to_vanilla = False
        mock_response.total_namespaces_checked = 1
        mock_response.gap_count = 1
        mock_response.findings = []
        mock_response.summary = "1 namespace(s) have Calico L3/L4 coverage gaps out of 1."
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_calico_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.calico_policy_audit.CalicoPolicyAuditUseCase",
                return_value=mock_uc,
            ),
        ):
            result = calico_policy_audit()

        assert isinstance(result, dict)
        assert result["installed"] is True
        assert result["gap_count"] == 1  # noqa: PLR2004
        assert result["error"] is None

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.calico_policy_audit import calico_policy_audit

        with patch(
            "hexawyn.mcp.server.build_calico_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = calico_policy_audit()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"
        assert result.get("installed") is False

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.calico_policy_audit")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))

    def test_gap_dict(self) -> None:
        from hexawyn.domain.models.calico import CalicoCoverageGap
        from hexawyn.mcp.tools.calico_policy_audit import _gap_dict

        gap = CalicoCoverageGap(
            namespace="ns1",
            workload_count=3,
            policy_count=0,
            issue="no_policy",
            network_status="open",
            risk_level="critical",
            selectors=[],
            note="No Calico policy restricts 3 workload(s) in namespace 'ns1'",
        )
        result = _gap_dict(gap)

        assert result["namespace"] == "ns1"
        assert result["issue"] == "no_policy"
        assert result["risk_level"] == "critical"
        assert result["workload_count"] == 3  # noqa: PLR2004
