"""RED → GREEN — MCP tool: audit_tls_compliance."""

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.tls_compliance_port import (
    TLSCompliancePort,
    TLSServiceRawData,
)
from hexawyn.domain.errors import ClusterUnreachableError


class TestAuditTLSComplianceTool:
    def test_delegates_and_returns_dict(self) -> None:
        mock_port = MagicMock(spec=TLSCompliancePort)
        mock_port.scan_services.return_value = [
            TLSServiceRawData(
                service_name="payment-service",
                namespace="production",
                tls_configured=False,
                cert_expiry_days=0,
                cert_issuer="",
                is_self_signed=False,
                proxy_tls_termination=False,
            ),
        ]

        with patch(
            "hexawyn.mcp.server.build_tls_compliance_adapter",
            return_value=mock_port,
        ):
            from hexawyn.mcp.tools.audit_tls_compliance import audit_tls_compliance

            result = audit_tls_compliance()

        assert result["all_compliant"] is False
        assert result["services"][0]["severity"] == "high_risk"
        assert result["error"] is None

    def test_handles_exception_gracefully(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_tls_compliance_adapter",
            side_effect=ClusterUnreachableError("down"),
        ):
            from hexawyn.mcp.tools.audit_tls_compliance import audit_tls_compliance

            result = audit_tls_compliance()

        assert result["all_compliant"] is False
        assert "down" in result["error"]

    def test_has_register_function(self) -> None:
        from hexawyn.mcp.tools.audit_tls_compliance import register

        assert callable(register)
