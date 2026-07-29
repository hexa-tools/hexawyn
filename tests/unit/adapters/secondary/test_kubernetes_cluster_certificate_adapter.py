from __future__ import annotations

import base64
from unittest.mock import MagicMock, patch

import pytest
from hexawyn.adapters.secondary.kubernetes_cluster_certificate_adapter import (
    KubernetesClusterCertificateAdapter,
    _extract_cert_pem,
    _get_annotations,
    _is_auto_renewing,
    _raise_on_rbac,
)
from hexawyn.application.ports.driven.cluster_certificate_health_port import (
    ClusterCertificateHealthPort,
)
from hexawyn.domain.errors import AdapterTimeoutError, InsufficientPermissionsError


def _make_namespace(name: str) -> MagicMock:
    ns = MagicMock()
    ns.metadata.name = name
    return ns


def _make_secret(
    name: str,
    namespace: str,
    cert_b64: str = "",
    annotations: dict | None = None,
) -> MagicMock:
    secret = MagicMock()
    secret.metadata = MagicMock()
    secret.metadata.name = name
    secret.metadata.annotations = annotations or {}
    secret.type = "kubernetes.io/tls"
    secret.data = {"tls.crt": cert_b64} if cert_b64 else {}
    return secret


def _make_ingress(name: str, tls_entries: list[tuple[str, str]] | None = None) -> MagicMock:
    ingress = MagicMock()
    ingress.metadata = MagicMock()
    ingress.metadata.name = name
    ingress_spec = MagicMock()
    tls_list = []
    if tls_entries:
        for secret_name, host in tls_entries:
            tls_entry = MagicMock()
            tls_entry.secret_name = secret_name
            tls_entry.hosts = [host]
            tls_list.append(tls_entry)
    ingress_spec.tls = tls_list
    ingress.spec = ingress_spec
    return ingress


class TestKubernetesClusterCertificateAdapter:
    def test_implements_port(self) -> None:
        adapter = KubernetesClusterCertificateAdapter(MagicMock())
        assert isinstance(adapter, ClusterCertificateHealthPort)

    def test_list_namespaces(self) -> None:
        api = MagicMock()
        ns_list = MagicMock()
        ns_list.items = [
            _make_namespace("default"),
            _make_namespace("kube-system"),
        ]
        api.list_namespace.return_value = ns_list
        adapter = KubernetesClusterCertificateAdapter(api)

        result = adapter.list_namespaces()

        assert result == ["default", "kube-system"]
        api.list_namespace.assert_called_once_with(timeout_seconds=10)

    def test_list_namespaces_timeout_raises(self) -> None:
        api = MagicMock()
        api.list_namespace.side_effect = Exception("timeout")
        adapter = KubernetesClusterCertificateAdapter(api, timeout_seconds=5.0)

        with pytest.raises(AdapterTimeoutError):
            adapter.list_namespaces()

    def test_list_tls_secrets_filters_by_type(self) -> None:
        api = MagicMock()
        secret_list = MagicMock()
        tls_secret = _make_secret("my-tls", "ns1", cert_b64=base64.b64encode(b"fake-cert").decode())
        non_tls = MagicMock()
        non_tls.type = "Opaque"
        non_tls.metadata = MagicMock()
        non_tls.metadata.name = "other"
        secret_list.items = [tls_secret, non_tls]
        api.list_namespaced_secret.return_value = secret_list
        adapter = KubernetesClusterCertificateAdapter(api)

        result = adapter.list_tls_secrets(namespace="ns1")

        assert len(result) == 1  # noqa: PLR2004
        assert result[0]["secret_name"] == "my-tls"

    def test_list_tls_secrets_no_cert_pem_skipped(self) -> None:
        api = MagicMock()
        secret_list = MagicMock()
        secret = _make_secret("no-cert", "ns1", cert_b64="")
        secret_list.items = [secret]
        api.list_namespaced_secret.return_value = secret_list
        adapter = KubernetesClusterCertificateAdapter(api)

        result = adapter.list_tls_secrets(namespace="ns1")

        assert result == []

    def test_list_tls_secrets_cert_manager_managed(self) -> None:
        api = MagicMock()
        secret_list = MagicMock()
        secret = _make_secret(
            "my-tls",
            "ns1",
            cert_b64=base64.b64encode(b"fake-cert").decode(),
            annotations={"cert-manager.io/certificate-name": "my-cert"},
        )
        secret_list.items = [secret]
        api.list_namespaced_secret.return_value = secret_list
        adapter = KubernetesClusterCertificateAdapter(api)

        result = adapter.list_tls_secrets(namespace="ns1")

        assert result[0]["cert_manager_managed"] is True

    def test_list_tls_secrets_rbac_error(self) -> None:
        api = MagicMock()
        api_exc = Exception("forbidden")
        api_exc.status = 403
        api.list_namespaced_secret.side_effect = api_exc
        adapter = KubernetesClusterCertificateAdapter(api)

        with pytest.raises(InsufficientPermissionsError):
            adapter.list_tls_secrets(namespace="ns1")

    def test_list_ingresses(self) -> None:
        with patch("kubernetes.client.NetworkingV1Api") as mock_networking_cls:
            mock_networking = MagicMock()
            ingress_list = MagicMock()
            ingress_list.items = [_make_ingress("my-ingress", [("my-tls", "example.com")])]
            mock_networking.list_namespaced_ingress.return_value = ingress_list
            mock_networking_cls.return_value = mock_networking
            adapter = KubernetesClusterCertificateAdapter(MagicMock())

            result = adapter.list_ingresses(namespace="ns1")

        assert len(result) == 1  # noqa: PLR2004
        assert result[0]["ingress_name"] == "my-ingress"
        assert result[0]["secret_name"] == "my-tls"
        assert result[0]["host"] == "example.com"

    def test_list_ingresses_multiple_tls(self) -> None:
        with patch("kubernetes.client.NetworkingV1Api") as mock_networking_cls:
            mock_networking = MagicMock()
            ingress_list = MagicMock()
            ingress_list.items = [
                _make_ingress(
                    "multi-ingress",
                    [("cert-a", "a.com"), ("cert-b", "b.com")],
                )
            ]
            mock_networking.list_namespaced_ingress.return_value = ingress_list
            mock_networking_cls.return_value = mock_networking
            adapter = KubernetesClusterCertificateAdapter(MagicMock())

            result = adapter.list_ingresses(namespace="ns1")

        assert len(result) == 2  # noqa: PLR2004
        assert result[0]["secret_name"] == "cert-a"
        assert result[1]["secret_name"] == "cert-b"

    def test_list_ingresses_skips_no_secret(self) -> None:
        with patch("kubernetes.client.NetworkingV1Api") as mock_networking_cls:
            mock_networking = MagicMock()
            ingress_list = MagicMock()
            ingress = MagicMock()
            ingress.metadata = MagicMock()
            ingress.metadata.name = "ingress"
            ingress_spec = MagicMock()
            tls_entry = MagicMock()
            tls_entry.secret_name = ""
            tls_entry.hosts = ["example.com"]
            ingress_spec.tls = [tls_entry]
            ingress.spec = ingress_spec
            ingress_list.items = [ingress]
            mock_networking.list_namespaced_ingress.return_value = ingress_list
            mock_networking_cls.return_value = mock_networking
            adapter = KubernetesClusterCertificateAdapter(MagicMock())

            result = adapter.list_ingresses(namespace="ns1")

        assert result == []

    def test_list_ingresses_rbac_error(self) -> None:
        with patch("kubernetes.client.NetworkingV1Api") as mock_networking_cls:
            mock_networking = MagicMock()
            api_exc = Exception("forbidden")
            api_exc.status = 403
            mock_networking.list_namespaced_ingress.side_effect = api_exc
            mock_networking_cls.return_value = mock_networking
            adapter = KubernetesClusterCertificateAdapter(MagicMock())

            with pytest.raises(InsufficientPermissionsError):
                adapter.list_ingresses(namespace="ns1")


class TestExtractCertPem:
    def test_extract_valid_cert(self) -> None:
        secret = _make_secret("tls", "ns", cert_b64=base64.b64encode(b"cert-data").decode())

        result = _extract_cert_pem(secret)

        assert result == "cert-data"

    def test_extract_no_data(self) -> None:
        secret = _make_secret("tls", "ns", cert_b64="")

        result = _extract_cert_pem(secret)

        assert result == ""

    def test_extract_invalid_base64(self) -> None:
        secret = MagicMock()
        secret.data = {"tls.crt": "not-valid-base64!!!"}

        result = _extract_cert_pem(secret)

        assert result == ""


class TestGetAnnotations:
    def test_get_annotations(self) -> None:
        secret = MagicMock()
        secret.metadata = MagicMock()
        secret.metadata.annotations = {"key": "value"}

        result = _get_annotations(secret)

        assert result == {"key": "value"}

    def test_get_annotations_none_returns_empty(self) -> None:
        secret = MagicMock()
        secret.metadata = None

        result = _get_annotations(secret)

        assert result == {}


class TestIsAutoRenewing:
    def test_not_auto_renewing_no_cert_manager_annotation(self) -> None:
        secret = _make_secret("tls", "ns")

        result = _is_auto_renewing(secret, "ns")

        assert result is False

    def test_not_auto_renewing_ready_true(self) -> None:
        secret = _make_secret(
            "tls",
            "ns",
            annotations={"cert-manager.io/certificate-name": "my-cert"},
        )
        with patch("kubernetes.client.CustomObjectsApi") as mock_custom_cls:
            mock_custom = MagicMock()
            mock_custom.get_namespaced_custom_object.return_value = {
                "status": {"conditions": [{"type": "Ready", "status": "True"}]}
            }
            mock_custom_cls.return_value = mock_custom

            result = _is_auto_renewing(secret, "ns")

        assert result is False

    def test_is_auto_renewing_ready_false(self) -> None:
        secret = _make_secret(
            "tls",
            "ns",
            annotations={"cert-manager.io/certificate-name": "my-cert"},
        )
        with patch("kubernetes.client.CustomObjectsApi") as mock_custom_cls:
            mock_custom = MagicMock()
            mock_custom.get_namespaced_custom_object.return_value = {
                "status": {"conditions": [{"type": "Ready", "status": "False"}]}
            }
            mock_custom_cls.return_value = mock_custom

            result = _is_auto_renewing(secret, "ns")

        assert result is True

    def test_returns_false_on_exception(self) -> None:
        secret = _make_secret(
            "tls",
            "ns",
            annotations={"cert-manager.io/certificate-name": "my-cert"},
        )
        with patch("kubernetes.client.CustomObjectsApi") as mock_custom_cls:
            mock_custom_cls.side_effect = RuntimeError("boom")

            result = _is_auto_renewing(secret, "ns")

        assert result is False


class TestRaiseOnRBAC:
    def test_rbac_403_raises(self) -> None:
        exc = Exception("forbidden")
        exc.status = 403

        with pytest.raises(InsufficientPermissionsError):
            _raise_on_rbac("ns1", exc)

    def test_non_rbac_passes_through(self) -> None:
        exc = Exception("timeout")
        exc.status = 500

        _raise_on_rbac("ns1", exc)
