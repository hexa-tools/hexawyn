from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.security_audit_port import SecurityAuditPort
from hexawyn.domain.models.admin_endpoint_audit import FailedAdminCall


class TestAdminEndpointAuditTool:
    def test_returns_flagged_callers(self) -> None:
        from hexawyn.mcp.tools.admin_endpoint_audit import admin_endpoint_audit

        with patch("hexawyn.mcp.server.build_security_audit_adapter") as m:
            a = MagicMock(spec=SecurityAuditPort)
            calls = []
            for i in range(52):
                calls.append(
                    FailedAdminCall(
                        timestamp=f"T{i}",
                        caller_ip="185.220.101.5",
                        caller_service="unknown",
                        endpoint="/admin/users",
                    )
                )
            for i in range(3):
                calls.append(
                    FailedAdminCall(
                        timestamp=f"T{i}",
                        caller_ip="10.0.1.45",
                        caller_service="monitoring-service",
                        endpoint="/admin/metrics",
                    )
                )
            a.fetch_failed_admin_calls.return_value = calls
            a.fetch_total_requests.return_value = 520
            m.return_value = a
            r = admin_endpoint_audit()
        assert r["error"] is None
        assert r["total_403s"] == 55
        assert len(r["flagged_callers"]) == 1

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.admin_endpoint_audit import admin_endpoint_audit

        with patch(
            "hexawyn.mcp.server.build_security_audit_adapter", side_effect=RuntimeError("boom")
        ):
            r = admin_endpoint_audit()
        assert r["error"] == "boom"
