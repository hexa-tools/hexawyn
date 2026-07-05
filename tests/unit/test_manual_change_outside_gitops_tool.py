from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestManualChangeOutsideGitOpsDetectionTool:
    def test_returns_report(self) -> None:
        from hexawyn.mcp.tools.manual_change_outside_gitops_detection import (
            detect_manual_changes_outside_gitops,
        )

        with patch("hexawyn.mcp.server.build_audit_log_adapter") as build_audit:
            audit_port = MagicMock()
            audit_port.list_live_config_resources.return_value = []
            audit_port.fetch_audit_log_events.return_value = {
                "available": False,
                "events": [],
                "earliest_timestamp": None,
            }
            build_audit.return_value = audit_port

            result = detect_manual_changes_outside_gitops(namespace="production")

        assert result["error"] is None
        assert result["manual_changes"] == []

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.manual_change_outside_gitops_detection import (
            detect_manual_changes_outside_gitops,
        )

        with patch(
            "hexawyn.mcp.server.build_audit_log_adapter",
            side_effect=RuntimeError("cluster unreachable"),
        ):
            result = detect_manual_changes_outside_gitops(namespace="production")

        assert "cluster unreachable" in result["error"]


class TestBuildAuditLogAdapterFactory:
    def test_build_audit_log_adapter_returns_gitops_drift_audit_port(self) -> None:
        from hexawyn.application.ports.driven.gitops_drift_audit_port import GitOpsDriftAuditPort
        from hexawyn.mcp.server import build_audit_log_adapter

        result = build_audit_log_adapter()

        assert isinstance(result, GitOpsDriftAuditPort)


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.manual_change_outside_gitops_detection")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
