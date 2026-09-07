"""RED → GREEN — TLS Compliance domain logic."""

from hexawyn.domain.services.tls_compliance.tls_compliance_engine import (
    TLSComplianceEngine,
    _as_bool,
    _as_int,
)


def _service(  # noqa: PLR0913
    service_name: str = "payment-service",
    namespace: str = "production",
    tls_configured: bool = True,
    cert_expiry_days: int = 180,
    cert_issuer: str = "Let's Encrypt",
    is_self_signed: bool = False,
    proxy_tls_termination: bool = False,
) -> dict[str, object]:
    return {
        "service_name": service_name,
        "namespace": namespace,
        "tls_configured": tls_configured,
        "cert_expiry_days": cert_expiry_days,
        "cert_issuer": cert_issuer,
        "is_self_signed": is_self_signed,
        "proxy_tls_termination": proxy_tls_termination,
    }


class TestTLSDetection:
    def test_expired_cert_critical(self) -> None:
        engine = TLSComplianceEngine()
        services = [_service(cert_expiry_days=-3)]

        result = engine.compute(services)

        assert result.services[0].severity == "critical"
        assert result.services[0].days_remaining == 0

    def test_expiring_soon_warning(self) -> None:
        engine = TLSComplianceEngine()
        services = [_service(cert_expiry_days=7)]

        result = engine.compute(services)

        assert result.services[0].severity == "warning"
        assert result.services[0].days_remaining == 7  # noqa: PLR2004

    def test_no_tls_high_risk(self) -> None:
        engine = TLSComplianceEngine()
        services = [_service(tls_configured=False)]

        result = engine.compute(services)

        assert result.services[0].severity == "high_risk"
        assert result.services[0].tls_configured is False

    def test_all_compliant_clean_report(self) -> None:
        engine = TLSComplianceEngine()
        services = [
            _service(cert_expiry_days=180),
            _service(service_name="auth-service", cert_expiry_days=365),
        ]

        result = engine.compute(services)

        assert result.all_compliant is True
        assert result.total_issues == 0

    def test_mixed_statuses_ranked_by_severity(self) -> None:
        engine = TLSComplianceEngine()
        services = [
            _service(service_name="valid-svc", cert_expiry_days=180),
            _service(service_name="expired-svc", cert_expiry_days=-3),
            _service(service_name="no-tls-svc", tls_configured=False),
            _service(service_name="soon-svc", cert_expiry_days=5),
        ]

        result = engine.compute(services)

        assert result.services[0].severity == "critical"
        assert result.services[1].severity == "high_risk"
        assert result.total_issues == 3  # noqa: PLR2004


class TestEdgeCases:
    def test_self_signed_flagged_separately(self) -> None:
        engine = TLSComplianceEngine()
        services = [_service(cert_expiry_days=60, is_self_signed=True)]

        result = engine.compute(services)

        assert result.services[0].is_self_signed is True

    def test_wildcard_cert_each_service_checked(self) -> None:
        engine = TLSComplianceEngine()
        services = [
            _service(service_name="api-v1"),
            _service(service_name="api-v2", cert_expiry_days=-1),
        ]

        result = engine.compute(services)

        assert len(result.services) == 2  # noqa: PLR2004
        assert result.services[0].severity == "critical"

    def test_proxy_tls_termination_detected(self) -> None:
        engine = TLSComplianceEngine()
        services = [
            _service(tls_configured=False, proxy_tls_termination=True),
        ]

        result = engine.compute(services)

        assert result.services[0].proxy_tls_termination is True

    def test_empty_services_returns_clean(self) -> None:
        engine = TLSComplianceEngine()

        result = engine.compute([])

        assert result.all_compliant is True
        assert result.total_issues == 0

    def test_expiring_soon_30_day_threshold(self) -> None:
        engine = TLSComplianceEngine()
        services = [
            _service(cert_expiry_days=30),
            _service(service_name="safe", cert_expiry_days=31),
        ]

        result = engine.compute(services)

        assert result.all_compliant is False
        assert result.services[0].severity == "warning"


class TestHelperFunctions:
    def test_as_int_none_returns_zero(self) -> None:
        assert _as_int(None) == 0

    def test_as_int_list_returns_zero(self) -> None:
        assert _as_int([1, 2]) == 0

    def test_as_bool_none_false(self) -> None:
        assert _as_bool(None) is False

    def test_as_bool_non_empty_string_true(self) -> None:
        assert _as_bool("yes") is True
