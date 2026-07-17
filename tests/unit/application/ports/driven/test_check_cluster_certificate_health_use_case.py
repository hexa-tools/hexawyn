"""Unit tests for check_cluster_certificate_health use case — domain + wiring."""

from __future__ import annotations

from datetime import UTC, datetime, timedelta
from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driven.cluster_certificate_health_port import (
    ClusterCertificateHealthPort,
    IngressRef,
    TlsSecretData,
)
from hexawyn.application.ports.driving.check_cluster_certificate_health.check_cluster_certificate_health_command import (
    CheckClusterCertificateHealthCommand,
)
from hexawyn.application.ports.driving.check_cluster_certificate_health.check_cluster_certificate_health_response import (
    CheckClusterCertificateHealthResponse,
)
from hexawyn.application.ports.driving.check_cluster_certificate_health.check_cluster_certificate_health_service_port import (
    CheckClusterCertificateHealthServicePort,
)
from hexawyn.application.service.cluster_certificate_health_service import (
    ClusterCertificateHealthService,
    _build_ingress_map,
    _is_wildcard,
)
from hexawyn.application.use_case.check_cluster_certificate_health.check_cluster_certificate_health_use_case import (
    CheckClusterCertificateHealthUseCase,
)
from hexawyn.domain.errors import InsufficientPermissionsError
from hexawyn.domain.models.certificate import (
    CertificateEntry,
    CertificateStatus,
    ClusterCertificateReport,
)

# ── Test PEM fixtures ──────────────────────────────────────────────────────


def _make_self_signed_pem(days_until_expiry: int) -> str:
    """Generate a minimal self-signed PEM for testing.

    Negative days_until_expiry produces an already-expired certificate
    by shifting both not_valid_before and not_valid_after into the past.
    """
    from cryptography import x509
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import rsa
    from cryptography.x509.oid import NameOID

    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    subject = issuer = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "test.example.com")])
    now = datetime.now(UTC)

    if days_until_expiry < 0:
        not_before = now - timedelta(days=abs(days_until_expiry) + 30)
        not_after = now - timedelta(days=abs(days_until_expiry))
    else:
        not_before = now - timedelta(days=1)
        not_after = now + timedelta(days=days_until_expiry)

    cert = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(not_before)
        .not_valid_after(not_after)
        .sign(key, hashes.SHA256())
    )
    return cert.public_bytes(serialization.Encoding.PEM).decode("utf-8")


def _make_wildcard_pem(days_until_expiry: int) -> str:
    """Generate a wildcard certificate PEM for testing."""
    from cryptography import x509
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import rsa
    from cryptography.x509.oid import NameOID

    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    subject = issuer = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "*.example.com")])
    now = datetime.now(UTC)
    cert = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(now - timedelta(days=1))
        .not_valid_after(now + timedelta(days=days_until_expiry))
        .sign(key, hashes.SHA256())
    )
    return cert.public_bytes(serialization.Encoding.PEM).decode("utf-8")


def _make_pem_with_san(days_until_expiry: int, san_hosts: list[str]) -> str:
    """Generate a PEM with a SubjectAlternativeName extension."""
    from cryptography import x509
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import rsa
    from cryptography.x509.oid import NameOID

    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    subject = issuer = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, san_hosts[0])])
    now = datetime.now(UTC)
    cert = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(now - timedelta(days=1))
        .not_valid_after(now + timedelta(days=days_until_expiry))
        .add_extension(
            x509.SubjectAlternativeName([x509.DNSName(h) for h in san_hosts]),
            critical=False,
        )
        .sign(key, hashes.SHA256())
    )
    return cert.public_bytes(serialization.Encoding.PEM).decode("utf-8")


def _make_ca_pem(days_until_expiry: int) -> str:
    """Generate a self-signed CA certificate with BasicConstraints (is_ca=True)."""
    from cryptography import x509
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import rsa
    from cryptography.x509.oid import NameOID

    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    subject = issuer = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "My Root CA")])
    now = datetime.now(UTC)
    cert = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(now - timedelta(days=1))
        .not_valid_after(now + timedelta(days=days_until_expiry))
        .add_extension(x509.BasicConstraints(ca=True, path_length=None), critical=True)
        .sign(key, hashes.SHA256())
    )
    return cert.public_bytes(serialization.Encoding.PEM).decode("utf-8")


# ── K8s exception helper ──────────────────────────────────────────────────


class _K8sApiException(Exception):  # noqa: N818
    """Fake K8s ApiException with a status code attribute."""

    def __init__(self, status: int) -> None:
        super().__init__(str(status))
        self.status = status


# ── Port stub ──────────────────────────────────────────────────────────────


class _StubPort(ClusterCertificateHealthPort):
    def __init__(
        self,
        namespaces: list[str],
        secrets_by_ns: dict[str, list[TlsSecretData]],
        ingresses_by_ns: dict[str, list[IngressRef]],
        rbac_blocked: set[str] | None = None,
    ) -> None:
        self._namespaces = namespaces
        self._secrets_by_ns = secrets_by_ns
        self._ingresses_by_ns = ingresses_by_ns
        self._rbac_blocked = rbac_blocked or set()

    def list_namespaces(self) -> list[str]:
        return self._namespaces

    def list_tls_secrets(self, namespace: str) -> list[TlsSecretData]:
        if namespace in self._rbac_blocked:
            raise InsufficientPermissionsError(
                f"RBAC denied for namespace {namespace!r}", context={}
            )
        return self._secrets_by_ns.get(namespace, [])

    def list_ingresses(self, namespace: str) -> list[IngressRef]:
        if namespace in self._rbac_blocked:
            raise InsufficientPermissionsError(
                f"RBAC denied for namespace {namespace!r}", context={}
            )
        return self._ingresses_by_ns.get(namespace, [])


def _secret(
    name: str,
    namespace: str,
    cert_pem: str,
    cert_manager: bool = False,
    auto_renewing: bool = False,
) -> TlsSecretData:
    return TlsSecretData(
        secret_name=name,
        namespace=namespace,
        cert_pem=cert_pem,
        cert_manager_managed=cert_manager,
        cert_manager_auto_renewing=auto_renewing,
    )


def _ingress(name: str, namespace: str, secret_name: str, host: str = "example.com") -> IngressRef:
    return IngressRef(
        ingress_name=name,
        namespace=namespace,
        secret_name=secret_name,
        host=host,
    )


# ── Command / Response dataclasses ────────────────────────────────────────


class TestCheckClusterCertificateHealthCommand:
    def test_defaults(self) -> None:
        cmd = CheckClusterCertificateHealthCommand()
        assert cmd.warning_days == 30
        assert cmd.critical_days == 7
        assert cmd.timeout_seconds == 10.0

    def test_custom_thresholds(self) -> None:
        cmd = CheckClusterCertificateHealthCommand(warning_days=60, critical_days=14)
        assert cmd.warning_days == 60
        assert cmd.critical_days == 14

    def test_is_frozen(self) -> None:
        cmd = CheckClusterCertificateHealthCommand()
        with pytest.raises(Exception):
            cmd.warning_days = 99  # type: ignore[misc]


class TestCheckClusterCertificateHealthResponse:
    def test_wraps_report(self) -> None:
        report = ClusterCertificateReport(cluster_name="prod")
        resp = CheckClusterCertificateHealthResponse(report=report)
        assert resp.report.cluster_name == "prod"


# ── Service port ABC ──────────────────────────────────────────────────────


class TestCheckClusterCertificateHealthServicePort:
    def test_cannot_instantiate_abstract(self) -> None:
        with pytest.raises(TypeError):
            CheckClusterCertificateHealthServicePort()  # type: ignore[abstract]


# ── Domain models ─────────────────────────────────────────────────────────


class TestCertificateEntry:
    def test_minimal_construction(self) -> None:
        from hexawyn.domain.models.certificate import CertificateInfo

        info = CertificateInfo(subject_cn="api.example.com", issuer_cn="CA")
        entry = CertificateEntry(
            secret_name="api-tls",
            namespace="production",
            info=info,
            status=CertificateStatus.HEALTHY,
            days_remaining=90,
        )
        assert entry.secret_name == "api-tls"
        assert entry.namespace == "production"
        assert entry.is_orphan is True
        assert entry.cert_manager_managed is False
        assert entry.cert_manager_auto_renewing is False
        assert entry.is_wildcard is False
        assert entry.ingress_refs == []

    def test_with_ingress_refs(self) -> None:
        from hexawyn.domain.models.certificate import CertificateInfo

        info = CertificateInfo(subject_cn="payment.example.com", issuer_cn="CA")
        entry = CertificateEntry(
            secret_name="payment-tls",
            namespace="production",
            info=info,
            status=CertificateStatus.WARNING,
            days_remaining=15,
            ingress_refs=["payment-service", "checkout-service"],
            is_orphan=False,
        )
        assert len(entry.ingress_refs) == 2
        assert entry.is_orphan is False


class TestClusterCertificateReport:
    def test_empty_report(self) -> None:
        report = ClusterCertificateReport(cluster_name="prod")
        assert report.critical == []
        assert report.warning == []
        assert report.healthy == []
        assert report.expired == []
        assert report.skipped_namespaces == []
        assert report.total_scanned == 0

    def test_cluster_name_preserved(self) -> None:
        report = ClusterCertificateReport(cluster_name="prod-eu")
        assert report.cluster_name == "prod-eu"


# ── Use case wiring ───────────────────────────────────────────────────────


class _StubServicePort(CheckClusterCertificateHealthServicePort):
    def __init__(self, response: CheckClusterCertificateHealthResponse) -> None:
        self._response = response

    def check_cluster_certificate_health(
        self, command: CheckClusterCertificateHealthCommand
    ) -> CheckClusterCertificateHealthResponse:
        return self._response


class TestCheckClusterCertificateHealthUseCase:
    def test_delegates_to_service(self) -> None:
        report = ClusterCertificateReport(cluster_name="prod")
        expected = CheckClusterCertificateHealthResponse(report=report)
        use_case = CheckClusterCertificateHealthUseCase(service=_StubServicePort(expected))
        result = use_case.execute(CheckClusterCertificateHealthCommand())
        assert result is expected

    def test_passes_command_to_service(self) -> None:
        report = ClusterCertificateReport(cluster_name="prod")
        captured: list[CheckClusterCertificateHealthCommand] = []

        class _CapturingPort(CheckClusterCertificateHealthServicePort):
            def check_cluster_certificate_health(
                self, cmd: CheckClusterCertificateHealthCommand
            ) -> CheckClusterCertificateHealthResponse:
                captured.append(cmd)
                return CheckClusterCertificateHealthResponse(report=report)

        use_case = CheckClusterCertificateHealthUseCase(service=_CapturingPort())
        cmd = CheckClusterCertificateHealthCommand(warning_days=45)
        use_case.execute(cmd)
        assert captured[0].warning_days == 45


# ── Helper functions ──────────────────────────────────────────────────────


class TestBuildIngressMap:
    def test_single_ingress_single_secret(self) -> None:
        ingresses = [_ingress("payment-ingress", "production", "payment-tls")]
        result = _build_ingress_map(ingresses)
        assert result == {"payment-tls": ["payment-ingress"]}

    def test_multiple_ingresses_same_secret(self) -> None:
        ingresses = [
            _ingress("payment-ingress", "production", "payment-tls"),
            _ingress("checkout-ingress", "production", "payment-tls"),
        ]
        result = _build_ingress_map(ingresses)
        assert sorted(result["payment-tls"]) == ["checkout-ingress", "payment-ingress"]

    def test_empty_ingress_list(self) -> None:
        assert _build_ingress_map([]) == {}

    def test_multiple_secrets(self) -> None:
        ingresses = [
            _ingress("payment-ingress", "production", "payment-tls"),
            _ingress("auth-ingress", "production", "auth-tls"),
        ]
        result = _build_ingress_map(ingresses)
        assert "payment-tls" in result
        assert "auth-tls" in result


class TestIsWildcard:
    def test_wildcard_cn(self) -> None:
        assert _is_wildcard("*.example.com", []) is True

    def test_regular_cn(self) -> None:
        assert _is_wildcard("api.example.com", []) is False

    def test_wildcard_in_san(self) -> None:
        assert _is_wildcard("api.example.com", ["*.example.com"]) is True

    def test_no_wildcard(self) -> None:
        assert _is_wildcard("api.example.com", ["api.example.com"]) is False


# ── Application service — all acceptance scenarios ─────────────────────────


class TestClusterCertificateHealthService:
    def test_three_certs_one_critical_one_warning_one_healthy(self) -> None:
        """3 certs: 5d → critical, 15d → warning, 45d → healthy."""
        pem_5d = _make_self_signed_pem(5)
        pem_15d = _make_self_signed_pem(15)
        pem_45d = _make_self_signed_pem(45)

        port = _StubPort(
            namespaces=["production"],
            secrets_by_ns={
                "production": [
                    _secret("critical-tls", "production", pem_5d),
                    _secret("warning-tls", "production", pem_15d),
                    _secret("healthy-tls", "production", pem_45d),
                ]
            },
            ingresses_by_ns={"production": []},
        )
        svc = ClusterCertificateHealthService(port=port, cluster_name="prod")
        resp = svc.check_cluster_certificate_health(CheckClusterCertificateHealthCommand())
        report = resp.report

        assert len(report.critical) == 1
        assert len(report.warning) == 1
        assert len(report.healthy) == 1
        assert len(report.expired) == 0
        assert report.total_scanned == 3
        assert report.critical[0].secret_name == "critical-tls"
        assert report.warning[0].secret_name == "warning-tls"
        assert report.healthy[0].secret_name == "healthy-tls"

    def test_no_tls_secrets_returns_empty_report(self) -> None:
        """No TLS secrets → all sections empty, helpful message via total_scanned=0."""
        port = _StubPort(
            namespaces=["production", "monitoring"],
            secrets_by_ns={"production": [], "monitoring": []},
            ingresses_by_ns={"production": [], "monitoring": []},
        )
        svc = ClusterCertificateHealthService(port=port, cluster_name="prod")
        resp = svc.check_cluster_certificate_health(CheckClusterCertificateHealthCommand())
        report = resp.report

        assert report.total_scanned == 0
        assert report.critical == []
        assert report.warning == []
        assert report.healthy == []
        assert report.expired == []

    def test_all_certs_healthy(self) -> None:
        """All certs > 30 days → only healthy section populated."""
        port = _StubPort(
            namespaces=["default"],
            secrets_by_ns={
                "default": [
                    _secret("cert-a", "default", _make_self_signed_pem(60)),
                    _secret("cert-b", "default", _make_self_signed_pem(90)),
                ]
            },
            ingresses_by_ns={"default": []},
        )
        svc = ClusterCertificateHealthService(port=port, cluster_name="prod")
        resp = svc.check_cluster_certificate_health(CheckClusterCertificateHealthCommand())
        report = resp.report

        assert len(report.healthy) == 2
        assert report.critical == []
        assert report.warning == []
        assert report.expired == []

    def test_cert_referenced_by_ingress_impacted_service_listed(self) -> None:
        """payment-tls referenced by payment-service → ingress_refs correct."""
        port = _StubPort(
            namespaces=["production"],
            secrets_by_ns={
                "production": [_secret("payment-tls", "production", _make_self_signed_pem(45))]
            },
            ingresses_by_ns={
                "production": [
                    _ingress("payment-service", "production", "payment-tls", "payment.example.com")
                ]
            },
        )
        svc = ClusterCertificateHealthService(port=port, cluster_name="prod")
        resp = svc.check_cluster_certificate_health(CheckClusterCertificateHealthCommand())
        entry = resp.report.healthy[0]

        assert "payment-service" in entry.ingress_refs
        assert entry.is_orphan is False

    def test_expired_cert_shown_with_negative_days_and_expired_status(self) -> None:
        """Expired cert → status=expired, days_remaining < 0."""
        pem_expired = _make_self_signed_pem(-10)
        port = _StubPort(
            namespaces=["production"],
            secrets_by_ns={"production": [_secret("expired-tls", "production", pem_expired)]},
            ingresses_by_ns={"production": []},
        )
        svc = ClusterCertificateHealthService(port=port, cluster_name="prod")
        resp = svc.check_cluster_certificate_health(CheckClusterCertificateHealthCommand())
        report = resp.report

        assert len(report.expired) == 1
        assert report.expired[0].status == CertificateStatus.EXPIRED
        assert report.expired[0].days_remaining < 0

    def test_rbac_namespace_skipped_with_warning(self) -> None:
        """RBAC block on namespace → skipped_namespaces populated."""
        port = _StubPort(
            namespaces=["production", "restricted"],
            secrets_by_ns={
                "production": [_secret("cert-a", "production", _make_self_signed_pem(60))]
            },
            ingresses_by_ns={"production": []},
            rbac_blocked={"restricted"},
        )
        svc = ClusterCertificateHealthService(port=port, cluster_name="prod")
        resp = svc.check_cluster_certificate_health(CheckClusterCertificateHealthCommand())
        report = resp.report

        assert "restricted" in report.skipped_namespaces
        assert report.total_scanned == 1

    def test_same_secret_referenced_by_multiple_ingresses(self) -> None:
        """Same TLS secret referenced by multiple ingresses → all listed."""
        port = _StubPort(
            namespaces=["production"],
            secrets_by_ns={
                "production": [_secret("payment-tls", "production", _make_self_signed_pem(45))]
            },
            ingresses_by_ns={
                "production": [
                    _ingress("payment-service", "production", "payment-tls"),
                    _ingress("checkout-service", "production", "payment-tls"),
                ]
            },
        )
        svc = ClusterCertificateHealthService(port=port, cluster_name="prod")
        resp = svc.check_cluster_certificate_health(CheckClusterCertificateHealthCommand())
        entry = resp.report.healthy[0]

        assert len(entry.ingress_refs) == 2
        assert "payment-service" in entry.ingress_refs
        assert "checkout-service" in entry.ingress_refs
        assert entry.is_orphan is False

    def test_orphan_secret_not_referenced_by_any_ingress(self) -> None:
        """Secret with no ingress reference → is_orphan=True."""
        port = _StubPort(
            namespaces=["production"],
            secrets_by_ns={
                "production": [_secret("orphan-tls", "production", _make_self_signed_pem(60))]
            },
            ingresses_by_ns={"production": []},
        )
        svc = ClusterCertificateHealthService(port=port, cluster_name="prod")
        resp = svc.check_cluster_certificate_health(CheckClusterCertificateHealthCommand())

        assert resp.report.healthy[0].is_orphan is True

    def test_cert_manager_auto_renewing_flagged(self) -> None:
        """cert-manager managed cert with auto_renewing=True → flagged correctly."""
        port = _StubPort(
            namespaces=["production"],
            secrets_by_ns={
                "production": [
                    _secret(
                        "managed-tls",
                        "production",
                        _make_self_signed_pem(5),
                        cert_manager=True,
                        auto_renewing=True,
                    )
                ]
            },
            ingresses_by_ns={"production": []},
        )
        svc = ClusterCertificateHealthService(port=port, cluster_name="prod")
        resp = svc.check_cluster_certificate_health(CheckClusterCertificateHealthCommand())
        entry = resp.report.critical[0]

        assert entry.cert_manager_managed is True
        assert entry.cert_manager_auto_renewing is True

    def test_wildcard_cert_detection(self) -> None:
        """Wildcard cert CN=*.example.com → is_wildcard=True."""
        port = _StubPort(
            namespaces=["production"],
            secrets_by_ns={
                "production": [_secret("wildcard-tls", "production", _make_wildcard_pem(60))]
            },
            ingresses_by_ns={"production": []},
        )
        svc = ClusterCertificateHealthService(port=port, cluster_name="prod")
        resp = svc.check_cluster_certificate_health(CheckClusterCertificateHealthCommand())

        assert resp.report.healthy[0].is_wildcard is True

    def test_custom_thresholds_respected(self) -> None:
        """Custom warning=60d, critical=14d — cert at 20d → critical."""
        pem_20d = _make_self_signed_pem(20)
        port = _StubPort(
            namespaces=["production"],
            secrets_by_ns={"production": [_secret("cert-a", "production", pem_20d)]},
            ingresses_by_ns={"production": []},
        )
        svc = ClusterCertificateHealthService(port=port, cluster_name="prod")
        cmd = CheckClusterCertificateHealthCommand(warning_days=60, critical_days=14)
        resp = svc.check_cluster_certificate_health(cmd)

        assert len(resp.report.warning) == 1

    def test_multiple_namespaces_aggregated(self) -> None:
        """Certs from multiple namespaces aggregated in one report."""
        port = _StubPort(
            namespaces=["production", "monitoring"],
            secrets_by_ns={
                "production": [_secret("prod-tls", "production", _make_self_signed_pem(60))],
                "monitoring": [_secret("grafana-tls", "monitoring", _make_self_signed_pem(5))],
            },
            ingresses_by_ns={"production": [], "monitoring": []},
        )
        svc = ClusterCertificateHealthService(port=port, cluster_name="prod")
        resp = svc.check_cluster_certificate_health(CheckClusterCertificateHealthCommand())
        report = resp.report

        assert report.total_scanned == 2
        assert len(report.healthy) == 1
        assert len(report.critical) == 1

    def test_cluster_name_in_report(self) -> None:
        port = _StubPort(namespaces=[], secrets_by_ns={}, ingresses_by_ns={})
        svc = ClusterCertificateHealthService(port=port, cluster_name="prod-eu")
        resp = svc.check_cluster_certificate_health(CheckClusterCertificateHealthCommand())
        assert resp.report.cluster_name == "prod-eu"

    def test_report_sorted_by_days_remaining_ascending(self) -> None:
        """Critical section sorted: most urgent first."""
        port = _StubPort(
            namespaces=["production"],
            secrets_by_ns={
                "production": [
                    _secret("cert-6d", "production", _make_self_signed_pem(6)),
                    _secret("cert-2d", "production", _make_self_signed_pem(2)),
                    _secret("cert-4d", "production", _make_self_signed_pem(4)),
                ]
            },
            ingresses_by_ns={"production": []},
        )
        svc = ClusterCertificateHealthService(port=port, cluster_name="prod")
        resp = svc.check_cluster_certificate_health(CheckClusterCertificateHealthCommand())
        days = [e.days_remaining for e in resp.report.critical]
        assert days == sorted(days)

    def test_invalid_cert_pem_skipped_gracefully(self) -> None:
        """Secret with invalid PEM is skipped without crashing."""
        port = _StubPort(
            namespaces=["production"],
            secrets_by_ns={
                "production": [
                    _secret("bad-tls", "production", "not-valid-pem"),
                    _secret("good-tls", "production", _make_self_signed_pem(60)),
                ]
            },
            ingresses_by_ns={"production": []},
        )
        svc = ClusterCertificateHealthService(port=port, cluster_name="prod")
        resp = svc.check_cluster_certificate_health(CheckClusterCertificateHealthCommand())
        assert resp.report.total_scanned == 1


# ── MCP tool ──────────────────────────────────────────────────────────────


class TestCheckClusterCertificateHealthMCPTool:
    def test_tool_returns_expected_keys(self) -> None:
        from unittest.mock import patch

        from hexawyn.mcp.tools.check_cluster_certificate_health import (
            check_cluster_certificate_health,
        )

        fake_report = ClusterCertificateReport(
            cluster_name="prod",
            critical=[],
            warning=[],
            healthy=[],
            expired=[],
            skipped_namespaces=[],
            total_scanned=0,
        )
        fake_resp = CheckClusterCertificateHealthResponse(report=fake_report)

        with patch(
            "hexawyn.mcp.tools.check_cluster_certificate_health.CheckClusterCertificateHealthUseCase"
        ) as mock_uc_cls:
            mock_uc_cls.return_value.execute.return_value = fake_resp
            with patch(
                "hexawyn.mcp.tools.check_cluster_certificate_health._build_adapter",
                return_value=MagicMock(spec=ClusterCertificateHealthPort),
            ):
                result = check_cluster_certificate_health()

        assert "cluster_name" in result
        assert "critical" in result
        assert "warning" in result
        assert "healthy" in result
        assert "expired" in result
        assert "skipped_namespaces" in result
        assert "total_scanned" in result
        assert "scanned_at" in result
        assert result["error"] is None

    def test_tool_serializes_cert_entries(self) -> None:
        """Covers _serialize_entry when the report contains actual certificate entries."""
        from unittest.mock import patch

        from hexawyn.domain.models.certificate import CertificateInfo
        from hexawyn.mcp.tools.check_cluster_certificate_health import (
            check_cluster_certificate_health,
        )

        info = CertificateInfo(
            subject_cn="api.example.com",
            issuer_cn="CA",
            not_after=datetime(2027, 1, 1, tzinfo=UTC),
            days_remaining=180,
        )
        entry = CertificateEntry(
            secret_name="api-tls",
            namespace="production",
            info=info,
            status=CertificateStatus.HEALTHY,
            days_remaining=180,
            ingress_refs=["api-ingress"],
            is_orphan=False,
        )
        fake_report = ClusterCertificateReport(
            cluster_name="prod",
            healthy=[entry],
            total_scanned=1,
        )
        fake_resp = CheckClusterCertificateHealthResponse(report=fake_report)

        with patch(
            "hexawyn.mcp.tools.check_cluster_certificate_health.CheckClusterCertificateHealthUseCase"
        ) as mock_uc_cls:
            mock_uc_cls.return_value.execute.return_value = fake_resp
            with patch(
                "hexawyn.mcp.tools.check_cluster_certificate_health._build_adapter",
                return_value=MagicMock(spec=ClusterCertificateHealthPort),
            ):
                result = check_cluster_certificate_health()

        healthy = result["healthy"]
        assert isinstance(healthy, list)
        assert len(healthy) == 1
        serialized = healthy[0]
        assert isinstance(serialized, dict)
        assert serialized["secret_name"] == "api-tls"
        assert serialized["status"] == "healthy"
        assert serialized["days_remaining"] == 180
        assert serialized["ingress_refs"] == ["api-ingress"]
        assert serialized["is_orphan"] is False

    def test_tool_error_returns_error_key(self) -> None:
        from unittest.mock import patch

        from hexawyn.mcp.tools.check_cluster_certificate_health import (
            check_cluster_certificate_health,
        )

        with patch(
            "hexawyn.mcp.tools.check_cluster_certificate_health._build_adapter",
            side_effect=RuntimeError("no kubeconfig"),
        ):
            result = check_cluster_certificate_health()

        assert result["error"] == "no kubeconfig"
        assert result["cluster_name"] is None
        assert result["total_scanned"] == 0


# ── _parse_pem_to_cert_info direct tests ──────────────────────────────────


class TestParsePemToCertInfo:
    def test_cert_with_san_extension_populates_san_list(self) -> None:
        """Covers the SAN try-block (lines 63-67) in _parse_pem_to_cert_info."""
        from hexawyn.application.service.cluster_certificate_health_service import (
            _parse_pem_to_cert_info,
        )

        pem = _make_pem_with_san(60, ["api.example.com", "www.example.com"])
        info = _parse_pem_to_cert_info(pem)
        assert len(info.san_list) == 2
        assert "api.example.com" in info.san_list
        assert "www.example.com" in info.san_list

    def test_cert_without_san_returns_empty_san_list(self) -> None:
        """Cert without SAN extension → empty san_list (except branch)."""
        from hexawyn.application.service.cluster_certificate_health_service import (
            _parse_pem_to_cert_info,
        )

        pem = _make_self_signed_pem(60)
        info = _parse_pem_to_cert_info(pem)
        assert info.san_list == []

    def test_cert_days_remaining_computed_correctly(self) -> None:
        from hexawyn.application.service.cluster_certificate_health_service import (
            _parse_pem_to_cert_info,
        )

        pem = _make_self_signed_pem(30)
        info = _parse_pem_to_cert_info(pem)
        assert 28 <= info.days_remaining <= 31

    def test_cert_subject_cn_extracted(self) -> None:
        from hexawyn.application.service.cluster_certificate_health_service import (
            _parse_pem_to_cert_info,
        )

        pem = _make_self_signed_pem(60)
        info = _parse_pem_to_cert_info(pem)
        assert info.subject_cn == "test.example.com"

    def test_ca_cert_is_ca_flag_set(self) -> None:
        """CA cert with BasicConstraints → is_ca=True (covers lines 81-82)."""
        from hexawyn.application.service.cluster_certificate_health_service import (
            _parse_pem_to_cert_info,
        )

        pem = _make_ca_pem(365)
        info = _parse_pem_to_cert_info(pem)
        assert info.is_ca is True

    def test_regular_cert_is_ca_false(self) -> None:
        """Regular cert without BasicConstraints → is_ca=False (except branch)."""
        from hexawyn.application.service.cluster_certificate_health_service import (
            _parse_pem_to_cert_info,
        )

        pem = _make_self_signed_pem(60)
        info = _parse_pem_to_cert_info(pem)
        assert info.is_ca is False


# ── _build_adapter coverage ───────────────────────────────────────────────


class TestBuildAdapter:
    def test_build_adapter_returns_certificate_adapter(self) -> None:
        """Covers _build_adapter body by patching the imported classes inside the function."""
        from unittest.mock import MagicMock, patch

        from hexawyn.mcp.tools.check_cluster_certificate_health import _build_adapter

        fake_api = MagicMock()
        mock_adapter = MagicMock()

        with (
            patch(
                "hexawyn.adapters.secondary.kubernetes_cluster_certificate_adapter.KubernetesClusterCertificateAdapter",
                return_value=mock_adapter,
            ),
            patch("hexawyn.mcp.server._k8s_api", fake_api),
        ):
            result = _build_adapter()

        assert result is not None


# ── KubernetesClusterCertificateAdapter helpers ───────────────────────────


class TestKubernetesAdapterHelpers:
    def test_extract_cert_pem_valid_base64(self) -> None:
        import base64

        from hexawyn.adapters.secondary.kubernetes_cluster_certificate_adapter import (
            _extract_cert_pem,
        )

        pem_bytes = _make_self_signed_pem(60).encode("utf-8")
        b64 = base64.b64encode(pem_bytes).decode("utf-8")
        secret = MagicMock()
        secret.data = {"tls.crt": b64}
        result = _extract_cert_pem(secret)
        assert result.startswith("-----BEGIN CERTIFICATE-----")

    def test_extract_cert_pem_missing_key(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_cluster_certificate_adapter import (
            _extract_cert_pem,
        )

        secret = MagicMock()
        secret.data = {}
        assert _extract_cert_pem(secret) == ""

    def test_extract_cert_pem_invalid_base64(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_cluster_certificate_adapter import (
            _extract_cert_pem,
        )

        secret = MagicMock()
        secret.data = {"tls.crt": "not!!valid!!base64"}
        assert _extract_cert_pem(secret) == ""

    def test_extract_cert_pem_no_data_attr(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_cluster_certificate_adapter import (
            _extract_cert_pem,
        )

        secret = MagicMock()
        secret.data = None
        assert _extract_cert_pem(secret) == ""

    def test_get_annotations_returns_dict(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_cluster_certificate_adapter import (
            _get_annotations,
        )

        secret = MagicMock()
        secret.metadata.annotations = {"cert-manager.io/certificate-name": "my-cert"}
        result = _get_annotations(secret)
        assert result["cert-manager.io/certificate-name"] == "my-cert"

    def test_get_annotations_none_returns_empty(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_cluster_certificate_adapter import (
            _get_annotations,
        )

        secret = MagicMock()
        secret.metadata.annotations = None
        assert _get_annotations(secret) == {}

    def test_raise_on_rbac_403_raises_insufficient_permissions(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_cluster_certificate_adapter import (
            _raise_on_rbac,
        )

        with pytest.raises(InsufficientPermissionsError):
            _raise_on_rbac("restricted", _K8sApiException(403))

    def test_raise_on_rbac_non_403_does_not_raise(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_cluster_certificate_adapter import (
            _raise_on_rbac,
        )

        _raise_on_rbac("default", _K8sApiException(500))

    def test_list_namespaces_happy_path(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_cluster_certificate_adapter import (
            KubernetesClusterCertificateAdapter,
        )

        ns_a = MagicMock()
        ns_a.metadata.name = "production"
        ns_b = MagicMock()
        ns_b.metadata.name = "monitoring"
        api = MagicMock()
        api.list_namespace.return_value = MagicMock(items=[ns_a, ns_b])

        adapter = KubernetesClusterCertificateAdapter(api=api)
        result = adapter.list_namespaces()
        assert result == ["production", "monitoring"]

    def test_list_namespaces_api_error_raises(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_cluster_certificate_adapter import (
            KubernetesClusterCertificateAdapter,
        )
        from hexawyn.domain.errors import AdapterTimeoutError

        api = MagicMock()
        api.list_namespace.side_effect = RuntimeError("connection refused")
        adapter = KubernetesClusterCertificateAdapter(api=api)

        with pytest.raises(AdapterTimeoutError):
            adapter.list_namespaces()

    def test_list_tls_secrets_skips_non_tls(self) -> None:
        import base64

        from hexawyn.adapters.secondary.kubernetes_cluster_certificate_adapter import (
            KubernetesClusterCertificateAdapter,
        )

        pem = _make_self_signed_pem(60).encode("utf-8")
        b64 = base64.b64encode(pem).decode("utf-8")

        tls_secret = MagicMock()
        tls_secret.type = "kubernetes.io/tls"
        tls_secret.data = {"tls.crt": b64}
        tls_secret.metadata.name = "my-tls"
        tls_secret.metadata.annotations = None

        opaque_secret = MagicMock()
        opaque_secret.type = "Opaque"

        api = MagicMock()
        api.list_namespaced_secret.return_value = MagicMock(items=[tls_secret, opaque_secret])

        adapter = KubernetesClusterCertificateAdapter(api=api)
        result = adapter.list_tls_secrets("production")
        assert len(result) == 1
        assert result[0]["secret_name"] == "my-tls"

    def test_list_tls_secrets_rbac_403_raises(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_cluster_certificate_adapter import (
            KubernetesClusterCertificateAdapter,
        )

        api = MagicMock()
        api.list_namespaced_secret.side_effect = _K8sApiException(403)

        adapter = KubernetesClusterCertificateAdapter(api=api)
        with pytest.raises(InsufficientPermissionsError):
            adapter.list_tls_secrets("restricted")

    def test_list_tls_secrets_no_cert_data_skipped(self) -> None:
        """TLS secret with missing tls.crt data is skipped."""
        from hexawyn.adapters.secondary.kubernetes_cluster_certificate_adapter import (
            KubernetesClusterCertificateAdapter,
        )

        secret = MagicMock()
        secret.type = "kubernetes.io/tls"
        secret.data = {}
        api = MagicMock()
        api.list_namespaced_secret.return_value = MagicMock(items=[secret])

        adapter = KubernetesClusterCertificateAdapter(api=api)
        result = adapter.list_tls_secrets("production")
        assert result == []

    def test_list_ingresses_happy_path(self) -> None:
        from unittest.mock import patch

        from hexawyn.adapters.secondary.kubernetes_cluster_certificate_adapter import (
            KubernetesClusterCertificateAdapter,
        )

        tls_rule = MagicMock()
        tls_rule.secret_name = "payment-tls"
        tls_rule.hosts = ["payment.example.com"]

        ingress = MagicMock()
        ingress.metadata.name = "payment-ingress"
        ingress.spec.tls = [tls_rule]

        mock_networking = MagicMock()
        mock_networking.list_namespaced_ingress.return_value = MagicMock(items=[ingress])

        adapter = KubernetesClusterCertificateAdapter(api=MagicMock())
        with patch("kubernetes.client.NetworkingV1Api", return_value=mock_networking):
            result = adapter.list_ingresses("production")

        assert len(result) == 1
        assert result[0]["ingress_name"] == "payment-ingress"
        assert result[0]["secret_name"] == "payment-tls"
        assert result[0]["host"] == "payment.example.com"

    def test_list_ingresses_rbac_403_raises(self) -> None:
        from unittest.mock import patch

        from hexawyn.adapters.secondary.kubernetes_cluster_certificate_adapter import (
            KubernetesClusterCertificateAdapter,
        )

        mock_networking = MagicMock()
        mock_networking.list_namespaced_ingress.side_effect = _K8sApiException(403)

        adapter = KubernetesClusterCertificateAdapter(api=MagicMock())
        with patch("kubernetes.client.NetworkingV1Api", return_value=mock_networking):
            with pytest.raises(InsufficientPermissionsError):
                adapter.list_ingresses("restricted")

    def test_list_ingresses_no_tls_entries(self) -> None:
        from unittest.mock import patch

        from hexawyn.adapters.secondary.kubernetes_cluster_certificate_adapter import (
            KubernetesClusterCertificateAdapter,
        )

        ingress = MagicMock()
        ingress.metadata.name = "http-only-ingress"
        ingress.spec.tls = []

        mock_networking = MagicMock()
        mock_networking.list_namespaced_ingress.return_value = MagicMock(items=[ingress])

        adapter = KubernetesClusterCertificateAdapter(api=MagicMock())
        with patch("kubernetes.client.NetworkingV1Api", return_value=mock_networking):
            result = adapter.list_ingresses("production")

        assert result == []

    def test_is_auto_renewing_returns_false_on_error(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_cluster_certificate_adapter import (
            _is_auto_renewing,
        )

        secret = MagicMock()
        secret.metadata.annotations = None
        assert _is_auto_renewing(secret, "production") is False

    def test_is_auto_renewing_no_cert_manager_annotation(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_cluster_certificate_adapter import (
            _is_auto_renewing,
        )

        secret = MagicMock()
        secret.metadata.annotations = {}
        assert _is_auto_renewing(secret, "production") is False

    def test_list_tls_secrets_cert_manager_managed(self) -> None:
        """Secret with cert-manager annotation is marked as cert_manager_managed=True."""
        import base64

        from hexawyn.adapters.secondary.kubernetes_cluster_certificate_adapter import (
            KubernetesClusterCertificateAdapter,
        )

        pem = _make_self_signed_pem(60).encode("utf-8")
        b64 = base64.b64encode(pem).decode("utf-8")

        secret = MagicMock()
        secret.type = "kubernetes.io/tls"
        secret.data = {"tls.crt": b64}
        secret.metadata.name = "managed-cert"
        secret.metadata.annotations = {"cert-manager.io/certificate-name": "my-cert"}

        api = MagicMock()
        api.list_namespaced_secret.return_value = MagicMock(items=[secret])

        adapter = KubernetesClusterCertificateAdapter(api=api)
        from unittest.mock import patch

        with patch(
            "hexawyn.adapters.secondary.kubernetes_cluster_certificate_adapter._is_auto_renewing",
            return_value=False,
        ):
            result = adapter.list_tls_secrets("production")

        assert result[0]["cert_manager_managed"] is True

    def test_list_tls_secrets_non_403_error_reraises(self) -> None:
        """Non-RBAC exception from list_namespaced_secret is re-raised (line 43)."""
        from hexawyn.adapters.secondary.kubernetes_cluster_certificate_adapter import (
            KubernetesClusterCertificateAdapter,
        )

        api = MagicMock()
        api.list_namespaced_secret.side_effect = RuntimeError("connection timeout")
        adapter = KubernetesClusterCertificateAdapter(api=api)

        with pytest.raises(RuntimeError, match="connection timeout"):
            adapter.list_tls_secrets("production")

    def test_list_ingresses_non_403_error_reraises(self) -> None:
        """Non-RBAC exception from list_namespaced_ingress is re-raised (line 78)."""
        from unittest.mock import patch

        from hexawyn.adapters.secondary.kubernetes_cluster_certificate_adapter import (
            KubernetesClusterCertificateAdapter,
        )

        mock_networking = MagicMock()
        mock_networking.list_namespaced_ingress.side_effect = RuntimeError("connection timeout")

        adapter = KubernetesClusterCertificateAdapter(api=MagicMock())
        with patch("kubernetes.client.NetworkingV1Api", return_value=mock_networking):
            with pytest.raises(RuntimeError, match="connection timeout"):
                adapter.list_ingresses("production")

    def test_is_auto_renewing_cert_not_ready_returns_true(self) -> None:
        """cert-manager Certificate CR with Ready=False means renewal in progress."""
        from unittest.mock import patch

        from hexawyn.adapters.secondary.kubernetes_cluster_certificate_adapter import (
            _is_auto_renewing,
        )

        secret = MagicMock()
        secret.metadata.annotations = {"cert-manager.io/certificate-name": "my-cert"}

        cert_obj = {
            "status": {
                "conditions": [{"type": "Ready", "status": "False"}],
            }
        }
        mock_custom_api = MagicMock()
        mock_custom_api.get_namespaced_custom_object.return_value = cert_obj

        with patch("kubernetes.client.CustomObjectsApi", return_value=mock_custom_api):
            result = _is_auto_renewing(secret, "production")

        assert result is True

    def test_is_auto_renewing_cert_ready_returns_false(self) -> None:
        """cert-manager Certificate CR with Ready=True → not renewing."""
        from unittest.mock import patch

        from hexawyn.adapters.secondary.kubernetes_cluster_certificate_adapter import (
            _is_auto_renewing,
        )

        secret = MagicMock()
        secret.metadata.annotations = {"cert-manager.io/certificate-name": "my-cert"}

        cert_obj = {
            "status": {
                "conditions": [{"type": "Ready", "status": "True"}],
            }
        }
        mock_custom_api = MagicMock()
        mock_custom_api.get_namespaced_custom_object.return_value = cert_obj

        with patch("kubernetes.client.CustomObjectsApi", return_value=mock_custom_api):
            result = _is_auto_renewing(secret, "production")

        assert result is False

    def test_is_auto_renewing_no_ready_condition_returns_false(self) -> None:
        """cert-manager CR conditions without a 'Ready' entry → not renewing."""
        from unittest.mock import patch

        from hexawyn.adapters.secondary.kubernetes_cluster_certificate_adapter import (
            _is_auto_renewing,
        )

        secret = MagicMock()
        secret.metadata.annotations = {"cert-manager.io/certificate-name": "my-cert"}

        cert_obj = {
            "status": {
                "conditions": [{"type": "Issuing", "status": "True"}],
            }
        }
        mock_custom_api = MagicMock()
        mock_custom_api.get_namespaced_custom_object.return_value = cert_obj

        with patch("kubernetes.client.CustomObjectsApi", return_value=mock_custom_api):
            result = _is_auto_renewing(secret, "production")

        assert result is False

    def test_is_auto_renewing_api_error_returns_false(self) -> None:
        """cert-manager CustomObjects API call failure is swallowed → returns False (lines 145-146)."""
        from unittest.mock import patch

        from hexawyn.adapters.secondary.kubernetes_cluster_certificate_adapter import (
            _is_auto_renewing,
        )

        secret = MagicMock()
        secret.metadata.annotations = {"cert-manager.io/certificate-name": "my-cert"}

        mock_custom_api = MagicMock()
        mock_custom_api.get_namespaced_custom_object.side_effect = RuntimeError("CRD not installed")

        with patch("kubernetes.client.CustomObjectsApi", return_value=mock_custom_api):
            result = _is_auto_renewing(secret, "production")

        assert result is False
