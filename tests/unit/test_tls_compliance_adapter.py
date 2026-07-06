"""RED → GREEN — TLSComplianceAdapter unit tests."""

from hexawyn.adapters.secondary.gitops.tls_compliance_adapter import TLSComplianceAdapter
from hexawyn.application.ports.driven.tls_compliance_port import TLSCompliancePort


class TestTLSComplianceAdapter:
    def test_implements_port(self) -> None:
        adapter = TLSComplianceAdapter()
        assert isinstance(adapter, TLSCompliancePort)

    def test_scan_services_returns_empty(self) -> None:
        adapter = TLSComplianceAdapter()
        result = adapter.scan_services()
        assert result == []
