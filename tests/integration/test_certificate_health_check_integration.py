"""Integration tests: certificate_health_check — TLS certificate health analyzer.

Uses real certificate generation (cryptography) wired with fake K8s clients.
No real cluster needed.
"""

from __future__ import annotations

import base64
import datetime
from unittest.mock import MagicMock, patch

from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID
from hexawyn.application.ports.driving.check_cluster_certificate_health.check_cluster_certificate_health_command import (
    CheckClusterCertificateHealthCommand,
)

_TEST_NAMESPACE = "hexawyn-test"


def _generate_cert(
    subject_cn: str,
    not_before: datetime.datetime,
    not_after: datetime.datetime,
) -> str:
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    subject = issuer = x509.Name(
        [
            x509.NameAttribute(NameOID.COMMON_NAME, subject_cn),
        ]
    )
    cert = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(private_key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(not_before)
        .not_valid_after(not_after)
        .sign(private_key, hashes.SHA256())
    )
    pem = cert.public_bytes(serialization.Encoding.PEM)
    return base64.b64encode(pem).decode("utf-8")


def _fake_secret(
    name: str,
    namespace: str,
    cert_pem_b64: str,
    cert_manager_annotations: dict[str, str] | None = None,
) -> object:
    secret = MagicMock()
    secret.type = "kubernetes.io/tls"
    secret.metadata.name = name
    secret.metadata.namespace = namespace
    secret.metadata.annotations = cert_manager_annotations or {}
    secret.data = {"tls.crt": cert_pem_b64}
    return secret


def _fake_k8s_api(
    secrets: list[object],
    namespaces: list[str] | None = None,
) -> object:
    api = MagicMock()
    ns_items = []
    for ns in namespaces or [_TEST_NAMESPACE]:
        ns_mock = MagicMock()
        ns_mock.metadata.name = ns
        ns_items.append(ns_mock)
    ns_list = MagicMock()
    ns_list.items = ns_items
    api.list_namespace.return_value = ns_list
    secret_list = MagicMock()
    secret_list.items = secrets
    api.list_namespaced_secret.return_value = secret_list
    return api


def _fake_networking_api(ingresses: list[object] | None = None) -> MagicMock:
    api = MagicMock()
    ingress_list = MagicMock()
    ingress_list.items = ingresses or []
    api.list_namespaced_ingress.return_value = ingress_list
    return api


def _fake_ingress(
    name: str,
    namespace: str,
    secret_name: str,
    host: str = "example.com",
) -> object:
    ingress = MagicMock()
    ingress.metadata.name = name
    ingress.metadata.namespace = namespace
    tls_entry = MagicMock()
    tls_entry.secret_name = secret_name
    tls_entry.hosts = [host]
    ingress.spec.tls = [tls_entry]
    return ingress


def _execute_check(
    secrets: list[object],
    warning_days: int = 30,
    critical_days: int = 7,
    ingresses: list[object] | None = None,
    namespaces: list[str] | None = None,
) -> object:
    from hexawyn.adapters.secondary.kubernetes_cluster_certificate_adapter import (
        KubernetesClusterCertificateAdapter,
    )
    from hexawyn.application.service.cluster_certificate_health_service import (
        ClusterCertificateHealthService,
    )
    from hexawyn.application.use_case.check_cluster_certificate_health.check_cluster_certificate_health_use_case import (
        CheckClusterCertificateHealthUseCase,
    )

    api = _fake_k8s_api(secrets, namespaces)
    adapter = KubernetesClusterCertificateAdapter(api=api, timeout_seconds=10.0)
    service = ClusterCertificateHealthService(port=adapter, cluster_name="test-cluster")
    use_case = CheckClusterCertificateHealthUseCase(service=service)

    net_api = _fake_networking_api(ingresses)
    with patch("kubernetes.client.NetworkingV1Api", return_value=net_api):
        return use_case.execute(
            CheckClusterCertificateHealthCommand(
                warning_days=warning_days,
                critical_days=critical_days,
                timeout_seconds=10.0,
            )
        )


class TestCertificateHealthCheckIntegration:
    def test_expired_certificate_detected_as_expired(self) -> None:
        now = datetime.datetime.now(datetime.UTC)
        expired_cert = _generate_cert(
            "expired.example.com",
            not_before=now - datetime.timedelta(days=400),
            not_after=now - datetime.timedelta(days=10),
        )
        secret = _fake_secret("expired-tls", _TEST_NAMESPACE, expired_cert)

        response = _execute_check([secret])

        report = response.report
        assert len(report.expired) == 1
        entry = report.expired[0]
        assert entry.secret_name == "expired-tls"
        assert entry.days_remaining < 0

    def test_expiring_soon_certificate_detected_as_warning(self) -> None:
        now = datetime.datetime.now(datetime.UTC)
        expiring_cert = _generate_cert(
            "almost-expired.example.com",
            not_before=now - datetime.timedelta(days=360),
            not_after=now + datetime.timedelta(days=5),
        )
        secret = _fake_secret("almost-expired-tls", _TEST_NAMESPACE, expiring_cert)

        response = _execute_check([secret], warning_days=30, critical_days=3)

        report = response.report
        assert len(report.warning) == 1
        entry = report.warning[0]
        assert entry.secret_name == "almost-expired-tls"
        assert 0 <= entry.days_remaining <= 5

    def test_orphaned_certificate_detected(self) -> None:
        now = datetime.datetime.now(datetime.UTC)
        valid_cert = _generate_cert(
            "orphan.example.com",
            not_before=now - datetime.timedelta(days=30),
            not_after=now + datetime.timedelta(days=300),
        )
        secret = _fake_secret("orphan-tls", _TEST_NAMESPACE, valid_cert)

        response = _execute_check([secret])

        report = response.report
        assert len(report.healthy) == 1
        entry = report.healthy[0]
        assert entry.is_orphan is True

    def test_healthy_certificate_with_ingress_reference(self) -> None:
        now = datetime.datetime.now(datetime.UTC)
        valid_cert = _generate_cert(
            "healthy.example.com",
            not_before=now - datetime.timedelta(days=30),
            not_after=now + datetime.timedelta(days=300),
        )
        secret = _fake_secret("healthy-tls", _TEST_NAMESPACE, valid_cert)
        ingress = _fake_ingress("healthy-ingress", _TEST_NAMESPACE, "healthy-tls")

        response = _execute_check([secret], ingresses=[ingress])

        report = response.report
        assert len(report.healthy) == 1
        entry = report.healthy[0]
        assert entry.secret_name == "healthy-tls"
        assert entry.days_remaining >= 0

    def test_mixed_certificates_all_categories(self) -> None:
        now = datetime.datetime.now(datetime.UTC)
        expired_cert = _generate_cert(
            "expired.com",
            not_before=now - datetime.timedelta(days=400),
            not_after=now - datetime.timedelta(days=1),
        )
        warning_cert = _generate_cert(
            "warning.com",
            not_before=now - datetime.timedelta(days=350),
            not_after=now + datetime.timedelta(days=10),
        )
        healthy_cert = _generate_cert(
            "healthy.com",
            not_before=now - datetime.timedelta(days=30),
            not_after=now + datetime.timedelta(days=300),
        )
        secrets = [
            _fake_secret("expired-tls", _TEST_NAMESPACE, expired_cert),
            _fake_secret("warning-tls", _TEST_NAMESPACE, warning_cert),
            _fake_secret("healthy-tls", _TEST_NAMESPACE, healthy_cert),
        ]

        response = _execute_check(secrets)

        report = response.report
        assert len(report.expired) == 1
        assert len(report.warning) == 1
        assert len(report.healthy) == 1
        assert report.total_scanned == 3

    def test_custom_thresholds_respected(self) -> None:
        now = datetime.datetime.now(datetime.UTC)
        cert_15_days = _generate_cert(
            "threshold-test.example.com",
            not_before=now - datetime.timedelta(days=30),
            not_after=now + datetime.timedelta(days=15),
        )
        secret = _fake_secret("threshold-tls", _TEST_NAMESPACE, cert_15_days)

        response = _execute_check([secret], warning_days=20, critical_days=5)

        report = response.report
        assert len(report.critical) == 0
        assert len(report.warning) == 1

    def test_no_secrets_returns_empty_report(self) -> None:
        response = _execute_check([])

        report = response.report
        assert report.total_scanned == 0
        assert len(report.expired) == 0
