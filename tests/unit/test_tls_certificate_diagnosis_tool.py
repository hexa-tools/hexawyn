from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.certificate_investigation_port import (
    CertificateInvestigationPort,
)


class TestTLSCertificateDiagnosisTool:
    def test_returns_diagnosis(self) -> None:
        from hexawyn.mcp.tools.tls_certificate_diagnosis import (
            tls_certificate_diagnosis,
        )

        with patch("hexawyn.mcp.server.build_certificate_investigation_adapter") as m:
            a = MagicMock(spec=CertificateInvestigationPort)
            a.fetch_certificate_pem.return_value = None
            a.fetch_ingress_hostname.return_value = "payment.example.com"
            m.return_value = a
            r = tls_certificate_diagnosis(ingress_name="payment-service", namespace="production")
        assert r["error"] is None
        assert r["status"] == "error"

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.tls_certificate_diagnosis import (
            tls_certificate_diagnosis,
        )

        with patch(
            "hexawyn.mcp.server.build_certificate_investigation_adapter",
            side_effect=RuntimeError("boom"),
        ):
            r = tls_certificate_diagnosis(ingress_name="x", namespace="ns")
        assert r["error"] == "boom"


class TestBuildCertificateInvestigationAdapter:
    def test_returns_port(self) -> None:
        from hexawyn.application.ports.driven.certificate_investigation_port import (
            CertificateInvestigationPort,
        )
        from hexawyn.mcp.server import build_certificate_investigation_adapter

        assert isinstance(build_certificate_investigation_adapter(), CertificateInvestigationPort)


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.tls_certificate_diagnosis")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
