from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.compliance_audit_port import ComplianceAuditPort
from hexawyn.domain.models.sensitive_data_audit import AccessMatch


class TestSensitiveDataAuditTool:
    def test_returns_flagged(self) -> None:
        from hexawyn.mcp.tools.sensitive_data_audit import sensitive_data_audit

        with patch("hexawyn.mcp.server.build_compliance_audit_adapter") as m:
            a = MagicMock(spec=ComplianceAuditPort)
            a.fetch_access_matches.return_value = [
                AccessMatch(
                    timestamp="T1",
                    caller_ip="192.168.1.45",
                    caller_service="user-service",
                    method="GET",
                    url="/user/123/ssn",
                    status_code=200,
                ),
                AccessMatch(
                    timestamp="T2",
                    caller_ip="203.0.113.5",
                    caller_service="unknown",
                    method="GET",
                    url="/user/456/ssn",
                    status_code=200,
                ),
            ]
            m.return_value = a
            r = sensitive_data_audit(pattern="/user/*/ssn", allowlist="user-service")
        assert r["error"] is None
        assert r["total_matches"] == 2
        assert len(r["flagged"]) == 1

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.sensitive_data_audit import sensitive_data_audit

        with patch(
            "hexawyn.mcp.server.build_compliance_audit_adapter",
            side_effect=RuntimeError("boom"),
        ):
            r = sensitive_data_audit(pattern="/x")
        assert r["error"] == "boom"


class TestBuildComplianceAuditAdapter:
    def test_returns_port(self) -> None:
        from hexawyn.application.ports.driven.compliance_audit_port import (
            ComplianceAuditPort,
        )
        from hexawyn.mcp.server import build_compliance_audit_adapter

        assert isinstance(build_compliance_audit_adapter(), ComplianceAuditPort)


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.sensitive_data_audit")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
