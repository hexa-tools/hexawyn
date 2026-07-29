"""Additional tests for fleet_health_adapter uncovered helpers."""

from __future__ import annotations

from datetime import UTC, datetime, timedelta
from unittest.mock import Mock, patch

from hexawyn.adapters.secondary.fleet_health_adapter import (
    _get_cert_counts,
    _get_resource_utilization,
)


class TestGetResourceUtilization:
    def test_no_prometheus_url(self) -> None:
        cpu, mem = _get_resource_utilization("ctx", "")
        assert cpu is None
        assert mem is None

    def test_returns_cpu_and_mem(self) -> None:
        import requests

        mock_resp = Mock()
        mock_resp.raise_for_status.return_value = None
        mock_resp.json.return_value = {"data": {"result": [{"value": [1700000000, "0.65"]}]}}

        with patch.object(requests, "get", return_value=mock_resp):
            cpu, mem = _get_resource_utilization("ctx", "http://prom:9090")
            assert cpu == 0.65  # noqa: PLR2004
            assert mem == 0.65  # noqa: PLR2004

    def test_empty_result(self) -> None:
        import requests

        mock_resp = Mock()
        mock_resp.raise_for_status.return_value = None
        mock_resp.json.return_value = {"data": {"result": []}}

        with patch.object(requests, "get", return_value=mock_resp):
            cpu, mem = _get_resource_utilization("ctx", "http://prom:9090")
            assert cpu is None
            assert mem is None

    def test_handles_exception(self) -> None:
        import requests

        with patch.object(requests, "get", side_effect=Exception("boom")):
            cpu, mem = _get_resource_utilization("ctx", "http://prom:9090")
            assert cpu is None
            assert mem is None


class TestGetCertCounts:
    def test_no_certs(self) -> None:
        api = Mock()
        api.list_secret_for_all_namespaces.return_value = Mock()
        with patch(
            "hexawyn.adapters.secondary.fleet_health_adapter._items",
            return_value=[],
        ):
            critical, warning = _get_cert_counts(api)
            assert critical == 0
            assert warning == 0

    def test_non_tls_secrets_skipped(self) -> None:
        api = Mock()
        api.list_secret_for_all_namespaces.return_value = Mock()
        secret = Mock()
        secret.type = "Opaque"
        with patch(
            "hexawyn.adapters.secondary.fleet_health_adapter._items",
            return_value=[secret],
        ):
            critical, warning = _get_cert_counts(api)
            assert critical == 0
            assert warning == 0

    def test_secret_without_data_skipped(self) -> None:
        api = Mock()
        api.list_secret_for_all_namespaces.return_value = Mock()
        secret = Mock()
        secret.type = "kubernetes.io/tls"
        secret.data = {}
        with patch(
            "hexawyn.adapters.secondary.fleet_health_adapter._items",
            return_value=[secret],
        ):
            critical, warning = _get_cert_counts(api)
            assert critical == 0
            assert warning == 0

    def test_expiring_critical_and_warning(self) -> None:
        import base64

        from cryptography import x509
        from cryptography.hazmat.primitives import hashes, serialization
        from cryptography.hazmat.primitives.asymmetric import rsa
        from cryptography.x509.oid import NameOID

        key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        subject = issuer = x509.Name(
            [
                x509.NameAttribute(NameOID.COMMON_NAME, "test.local"),
            ]
        )

        critical_date = datetime.now(UTC) + timedelta(days=3)
        warning_date = datetime.now(UTC) + timedelta(days=14)

        def _make_cert(not_after: datetime) -> bytes:
            cert = (
                x509.CertificateBuilder()
                .subject_name(subject)
                .issuer_name(issuer)
                .public_key(key.public_key())
                .serial_number(x509.random_serial_number())
                .not_valid_before(datetime.now(UTC))
                .not_valid_after(not_after)
                .add_extension(
                    x509.SubjectAlternativeName([x509.DNSName("test.local")]),
                    critical=False,
                )
                .sign(key, hashes.SHA256())
            )
            return cert.public_bytes(serialization.Encoding.PEM)

        critical_pem = _make_cert(critical_date)
        warning_pem = _make_cert(warning_date)

        critical_secret = Mock()
        critical_secret.type = "kubernetes.io/tls"
        critical_secret.data = {"tls.crt": base64.b64encode(critical_pem).decode()}

        warning_secret = Mock()
        warning_secret.type = "kubernetes.io/tls"
        warning_secret.data = {"tls.crt": base64.b64encode(warning_pem).decode()}

        api = Mock()
        api.list_secret_for_all_namespaces.return_value = Mock()
        with patch(
            "hexawyn.adapters.secondary.fleet_health_adapter._items",
            return_value=[critical_secret, warning_secret],
        ):
            critical, warning = _get_cert_counts(api)
            assert critical == 1
            assert warning == 1

    def test_exception_returns_zeros(self) -> None:
        api = Mock()
        api.list_secret_for_all_namespaces.side_effect = Exception("boom")
        critical, warning = _get_cert_counts(api)
        assert critical == 0
        assert warning == 0
