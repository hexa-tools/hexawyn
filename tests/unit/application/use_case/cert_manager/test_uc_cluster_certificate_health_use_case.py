from __future__ import annotations

from datetime import UTC, datetime, timedelta
from unittest.mock import MagicMock

from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID
from hexawyn.application.use_case.cert_manager.cluster_certificate_health.cluster_certificate_health_use_case import (  # noqa: E501
    ClusterCertificateHealthUseCase,
    _build_ingress_map,
    _is_wildcard,
)
from hexawyn.application.use_case.cert_manager.cluster_certificate_health.command import (
    ClusterCertificateHealthCommand,
)
from hexawyn.application.use_case.cert_manager.cluster_certificate_health.response import (
    ClusterCertificateHealthResponse,
)
from hexawyn.domain.models.certificate import ClusterCertificateReport


def _make_valid_cert_pem(
    common_name: str = "example.com",
    days_valid: int = 200,
) -> str:
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    subject = issuer = x509.Name(
        [
            x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
            x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "California"),
            x509.NameAttribute(NameOID.LOCALITY_NAME, "San Francisco"),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Test Org"),
            x509.NameAttribute(NameOID.COMMON_NAME, common_name),
        ]
    )
    now = datetime.now(UTC)
    cert = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(now)
        .not_valid_after(now + timedelta(days=days_valid))
        .add_extension(
            x509.SubjectAlternativeName([x509.DNSName(common_name)]),
            critical=False,
        )
        .sign(key, hashes.SHA256())
    )
    return cert.public_bytes(serialization.Encoding.PEM).decode("utf-8")


VALID_PEM = _make_valid_cert_pem()


class TestClusterCertificateHealthUseCase:
    def test_execute_returns_cluster_certificate_health_response(self) -> None:
        port = MagicMock()
        port.list_namespaces.return_value = ["default"]
        port.list_tls_secrets.return_value = []
        port.list_ingresses.return_value = []

        use_case = ClusterCertificateHealthUseCase(port=port)
        result = use_case.check_cluster_certificate_health(
            ClusterCertificateHealthCommand(warning_days=30, critical_days=7)
        )

        assert isinstance(result, ClusterCertificateHealthResponse)
        assert isinstance(result.report, ClusterCertificateReport)
        assert result.error is None

    def test_execute_with_no_tls_secrets_returns_empty_report(self) -> None:
        port = MagicMock()
        port.list_namespaces.return_value = ["default"]
        port.list_tls_secrets.return_value = []
        port.list_ingresses.return_value = []

        use_case = ClusterCertificateHealthUseCase(port=port)
        result = use_case.check_cluster_certificate_health(
            ClusterCertificateHealthCommand(warning_days=30, critical_days=7)
        )

        assert result.report is not None
        assert result.report.total_scanned == 0  # noqa: PLR2004

    def test_execute_skips_namespace_on_permission_error(self) -> None:
        from hexawyn.domain.errors import InsufficientPermissionsError

        port = MagicMock()
        port.list_namespaces.return_value = ["default", "restricted"]
        port.list_tls_secrets.side_effect = [
            [],
            InsufficientPermissionsError(
                "Forbidden", context={"resource": "secrets", "namespace": "restricted"}
            ),
        ]
        port.list_ingresses.return_value = []

        use_case = ClusterCertificateHealthUseCase(port=port)
        result = use_case.check_cluster_certificate_health(
            ClusterCertificateHealthCommand(warning_days=30, critical_days=7)
        )

        assert result.report is not None
        assert "restricted" in result.report.skipped_namespaces

    def test_execute_with_valid_tls_secret(self) -> None:
        port = MagicMock()
        port.list_namespaces.return_value = ["default"]
        port.list_tls_secrets.return_value = [
            {
                "secret_name": "my-tls",
                "namespace": "default",
                "cert_pem": VALID_PEM,
                "cert_manager_managed": True,
                "cert_manager_auto_renewing": True,
            },
        ]
        port.list_ingresses.return_value = []

        use_case = ClusterCertificateHealthUseCase(port=port)
        result = use_case.check_cluster_certificate_health(
            ClusterCertificateHealthCommand(warning_days=30, critical_days=7)
        )

        assert result.report is not None
        assert result.report.total_scanned == 1  # noqa: PLR2004
        assert len(result.report.healthy) == 1  # noqa: PLR2004
        assert result.report.healthy[0].secret_name == "my-tls"
        assert result.report.healthy[0].is_orphan is True

    def test_execute_with_tls_secret_and_ingress(self) -> None:
        port = MagicMock()
        port.list_namespaces.return_value = ["default"]
        port.list_tls_secrets.return_value = [
            {
                "secret_name": "my-tls",
                "namespace": "default",
                "cert_pem": VALID_PEM,
                "cert_manager_managed": True,
                "cert_manager_auto_renewing": True,
            },
        ]
        port.list_ingresses.return_value = [
            {
                "ingress_name": "my-ingress",
                "namespace": "default",
                "secret_name": "my-tls",
                "host": "example.com",
            },
        ]

        use_case = ClusterCertificateHealthUseCase(port=port)
        result = use_case.check_cluster_certificate_health(
            ClusterCertificateHealthCommand(warning_days=30, critical_days=7)
        )

        assert result.report is not None
        assert result.report.total_scanned == 1  # noqa: PLR2004
        assert result.report.healthy[0].is_orphan is False
        assert result.report.healthy[0].ingress_refs == ["my-ingress"]

    def test_execute_skips_invalid_cert_pem(self) -> None:
        port = MagicMock()
        port.list_namespaces.return_value = ["default"]
        port.list_tls_secrets.return_value = [
            {
                "secret_name": "invalid-tls",
                "namespace": "default",
                "cert_pem": "NOT_A_VALID_CERTIFICATE",
                "cert_manager_managed": False,
                "cert_manager_auto_renewing": False,
            },
            {
                "secret_name": "valid-tls",
                "namespace": "default",
                "cert_pem": VALID_PEM,
                "cert_manager_managed": True,
                "cert_manager_auto_renewing": True,
            },
        ]
        port.list_ingresses.return_value = []

        use_case = ClusterCertificateHealthUseCase(port=port)
        result = use_case.check_cluster_certificate_health(
            ClusterCertificateHealthCommand(warning_days=30, critical_days=7)
        )

        assert result.report is not None
        assert result.report.total_scanned == 1  # noqa: PLR2004
        assert result.report.healthy[0].secret_name == "valid-tls"

    def test_execute_with_multiple_namespaces(self) -> None:
        port = MagicMock()
        port.list_namespaces.return_value = ["default", "kube-system"]
        port.list_tls_secrets.side_effect = [
            [
                {
                    "secret_name": "app-tls",
                    "namespace": "default",
                    "cert_pem": VALID_PEM,
                    "cert_manager_managed": True,
                    "cert_manager_auto_renewing": True,
                },
            ],
            [
                {
                    "secret_name": "sys-tls",
                    "namespace": "kube-system",
                    "cert_pem": VALID_PEM,
                    "cert_manager_managed": False,
                    "cert_manager_auto_renewing": False,
                },
            ],
        ]
        port.list_ingresses.return_value = []

        use_case = ClusterCertificateHealthUseCase(port=port)
        result = use_case.check_cluster_certificate_health(
            ClusterCertificateHealthCommand(warning_days=30, critical_days=7)
        )

        assert result.report is not None
        assert result.report.total_scanned == 2  # noqa: PLR2004
        namespaces = {e.namespace for e in result.report.healthy}
        assert namespaces == {"default", "kube-system"}

    def test_cluster_name_defaults_to_default(self) -> None:
        port = MagicMock()
        port.list_namespaces.return_value = []
        port.list_tls_secrets.return_value = []
        port.list_ingresses.return_value = []

        use_case = ClusterCertificateHealthUseCase(port=port)
        result = use_case.check_cluster_certificate_health(ClusterCertificateHealthCommand())

        assert result.report is not None
        assert result.report.cluster_name == "default"

    def test_cluster_name_custom(self) -> None:
        port = MagicMock()
        port.list_namespaces.return_value = []
        port.list_tls_secrets.return_value = []
        port.list_ingresses.return_value = []

        use_case = ClusterCertificateHealthUseCase(port=port, cluster_name="prod-eu")
        result = use_case.check_cluster_certificate_health(ClusterCertificateHealthCommand())

        assert result.report is not None
        assert result.report.cluster_name == "prod-eu"

    def test_execute_wildcard_cert(self) -> None:
        wildcard_pem = _make_valid_cert_pem(common_name="*.example.com")
        port = MagicMock()
        port.list_namespaces.return_value = ["default"]
        port.list_tls_secrets.return_value = [
            {
                "secret_name": "wildcard-tls",
                "namespace": "default",
                "cert_pem": wildcard_pem,
                "cert_manager_managed": True,
                "cert_manager_auto_renewing": False,
            },
        ]
        port.list_ingresses.return_value = []

        use_case = ClusterCertificateHealthUseCase(port=port)
        result = use_case.check_cluster_certificate_health(
            ClusterCertificateHealthCommand(warning_days=30, critical_days=7)
        )

        assert result.report is not None
        assert result.report.total_scanned == 1  # noqa: PLR2004
        assert result.report.healthy[0].is_wildcard is True


class TestBuildIngressMap:
    def test_empty_ingresses_returns_empty_dict(self) -> None:
        assert _build_ingress_map([]) == {}

    def test_single_ingress(self) -> None:
        ingresses = [
            {
                "ingress_name": "my-ingress",
                "namespace": "default",
                "secret_name": "my-tls",
                "host": "example.com",
            },
        ]
        assert _build_ingress_map(ingresses) == {"my-tls": ["my-ingress"]}

    def test_multiple_ingresses_same_secret(self) -> None:
        ingresses = [
            {
                "ingress_name": "ingress-a",
                "namespace": "default",
                "secret_name": "shared-tls",
                "host": "a.example.com",
            },
            {
                "ingress_name": "ingress-b",
                "namespace": "default",
                "secret_name": "shared-tls",
                "host": "b.example.com",
            },
        ]
        assert _build_ingress_map(ingresses) == {"shared-tls": ["ingress-a", "ingress-b"]}

    def test_multiple_secrets(self) -> None:
        ingresses = [
            {
                "ingress_name": "ingress-a",
                "namespace": "default",
                "secret_name": "tls-a",
                "host": "a.example.com",
            },
            {
                "ingress_name": "ingress-b",
                "namespace": "default",
                "secret_name": "tls-b",
                "host": "b.example.com",
            },
        ]
        assert _build_ingress_map(ingresses) == {
            "tls-a": ["ingress-a"],
            "tls-b": ["ingress-b"],
        }

    def test_execute_cert_without_san_or_basic_constraints(self) -> None:
        key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        subject = issuer = x509.Name(
            [
                x509.NameAttribute(NameOID.COMMON_NAME, "no-ext.example.com"),
            ]
        )
        now = datetime.now(UTC)
        cert = (
            x509.CertificateBuilder()
            .subject_name(subject)
            .issuer_name(issuer)
            .public_key(key.public_key())
            .serial_number(x509.random_serial_number())
            .not_valid_before(now)
            .not_valid_after(now + timedelta(days=200))
            .sign(key, hashes.SHA256())
        )
        pem = cert.public_bytes(serialization.Encoding.PEM).decode("utf-8")

        port = MagicMock()
        port.list_namespaces.return_value = ["default"]
        port.list_tls_secrets.return_value = [
            {
                "secret_name": "no-ext-tls",
                "namespace": "default",
                "cert_pem": pem,
                "cert_manager_managed": False,
                "cert_manager_auto_renewing": False,
            },
        ]
        port.list_ingresses.return_value = []

        use_case = ClusterCertificateHealthUseCase(port=port)
        result = use_case.check_cluster_certificate_health(
            ClusterCertificateHealthCommand(warning_days=30, critical_days=7)
        )

        assert result.report is not None
        assert result.report.total_scanned == 1  # noqa: PLR2004
        assert result.report.healthy[0].info.san_list == []
        assert result.report.healthy[0].info.is_ca is False

    def test_execute_cert_with_basic_constraints_ca(self) -> None:
        key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        subject = issuer = x509.Name(
            [
                x509.NameAttribute(NameOID.COMMON_NAME, "ca-cert.example.com"),
            ]
        )
        now = datetime.now(UTC)
        cert = (
            x509.CertificateBuilder()
            .subject_name(subject)
            .issuer_name(issuer)
            .public_key(key.public_key())
            .serial_number(x509.random_serial_number())
            .not_valid_before(now)
            .not_valid_after(now + timedelta(days=200))
            .add_extension(
                x509.BasicConstraints(ca=True, path_length=None),
                critical=True,
            )
            .sign(key, hashes.SHA256())
        )
        pem = cert.public_bytes(serialization.Encoding.PEM).decode("utf-8")

        port = MagicMock()
        port.list_namespaces.return_value = ["default"]
        port.list_tls_secrets.return_value = [
            {
                "secret_name": "ca-tls",
                "namespace": "default",
                "cert_pem": pem,
                "cert_manager_managed": False,
                "cert_manager_auto_renewing": False,
            },
        ]
        port.list_ingresses.return_value = []

        use_case = ClusterCertificateHealthUseCase(port=port)
        result = use_case.check_cluster_certificate_health(
            ClusterCertificateHealthCommand(warning_days=30, critical_days=7)
        )

        assert result.report is not None
        assert result.report.total_scanned == 1  # noqa: PLR2004
        assert result.report.healthy[0].info.is_ca is True


class TestIsWildcard:
    def test_wildcard_cn_returns_true(self) -> None:
        assert _is_wildcard("*.example.com", []) is True

    def test_wildcard_in_san_returns_true(self) -> None:
        assert _is_wildcard("example.com", ["*.example.com"]) is True

    def test_no_wildcard_returns_false(self) -> None:
        assert _is_wildcard("example.com", ["www.example.com"]) is False

    def test_empty_cn_and_san_returns_false(self) -> None:
        assert _is_wildcard("", []) is False
