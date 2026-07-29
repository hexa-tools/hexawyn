"""RED → GREEN — Layer 1: TLS Compliance domain models."""

from hexawyn.domain.models.tls_compliance import TLSComplianceReport, TLSServiceStatus


class TestTLSServiceStatus:
    def test_is_frozen(self) -> None:
        import pytest

        s = TLSServiceStatus(
            service_name="svc",
            namespace="prod",
            tls_configured=True,
            cert_expiry_days=30,
            days_remaining=30,
            severity="warning",
            cert_issuer="LE",
            is_self_signed=False,
            proxy_tls_termination=False,
        )
        with pytest.raises(Exception):
            s.severity = "critical"  # type: ignore[misc]


class TestTLSComplianceReport:
    def test_defaults(self) -> None:
        r = TLSComplianceReport()
        assert r.all_compliant is True
        assert r.total_issues == 0

    def test_with_issues(self) -> None:
        r = TLSComplianceReport(all_compliant=False, total_issues=3)
        assert r.total_issues == 3  # noqa: PLR2004
