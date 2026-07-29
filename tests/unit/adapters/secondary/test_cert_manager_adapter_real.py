"""Tests for the real CertManagerAdapter that queries K8s CRDs via VanillaAdapter."""

from __future__ import annotations

from unittest.mock import Mock

import pytest
from hexawyn.adapters.secondary.gitops.cert_manager_adapter import CertManagerAdapter
from hexawyn.domain.models.certificates import (
    Certificate,
    CertificateStatus,
    IssuerType,
)


def _mock_vanilla_with_crds(*item_lists: list[dict]) -> Mock:
    """Create a VanillaAdapter mock that returns the given CRD items.
    Uses side_effect to return successive item lists for each CRD API call.
    If more calls are made than items provided, returns empty list.
    """
    mock_vanilla = Mock()
    mock_crd = Mock()
    items_iter = iter(item_lists)

    def _list(*args, **kwargs):
        try:
            return {"items": next(items_iter)}
        except StopIteration:
            return {"items": []}

    def _get(*args, **kwargs):
        try:
            return next(items_iter)[0]
        except StopIteration:
            return {}

    mock_crd.list_namespaced_custom_object.side_effect = _list
    mock_crd.list_cluster_custom_object.side_effect = _list
    mock_crd.get_namespaced_custom_object.side_effect = _get
    mock_crd.get_cluster_custom_object.side_effect = _get

    mock_vanilla._crd_api_client.return_value = mock_crd
    return mock_vanilla


_CERT_ITEM = {
    "apiVersion": "cert-manager.io/v1",
    "kind": "Certificate",
    "metadata": {
        "name": "my-tls",
        "namespace": "default",
        "creationTimestamp": "2026-01-01T00:00:00Z",
    },
    "spec": {
        "dnsNames": ["app.example.com"],
        "issuerRef": {"name": "letsencrypt-prod", "kind": "ClusterIssuer"},
        "secretName": "my-tls-secret",
        "renewBefore": "720h0m0s",
    },
    "status": {
        "conditions": [
            {"type": "Ready", "status": "True", "reason": "Ready", "message": "OK"},
        ],
        "notBefore": "2026-01-01T00:00:00Z",
        "notAfter": "2027-01-01T00:00:00Z",
        "renewalTime": "2026-12-01T00:00:00Z",
    },
}

_ISSUER_ITEM = {
    "apiVersion": "cert-manager.io/v1",
    "kind": "ClusterIssuer",
    "metadata": {"name": "letsencrypt-prod", "creationTimestamp": "2026-01-01T00:00:00Z"},
    "spec": {
        "acme": {
            "server": "https://acme-v02.api.letsencrypt.org/directory",
            "email": "admin@example.com",
            "privateKeySecretRef": {"name": "letsencrypt-key"},
            "solvers": [{"http01": {"ingress": {"class": "nginx"}}}],
        },
    },
    "status": {
        "conditions": [
            {"type": "Ready", "status": "True", "reason": "ACMEAccountRegistered", "message": "OK"},
        ],
    },
}


class TestCertManagerAdapterDetect:
    def test_detect_installed(self) -> None:
        mock = _mock_vanilla_with_crds([_CERT_ITEM])
        adapter = CertManagerAdapter(mock)
        result = adapter.detect()

        assert result.installed is True
        assert result.total_certs == 1
        assert result.ready_certs == 1

    def test_detect_not_installed(self) -> None:
        # When CRD doesn't exist, K8s API raises ApiException
        mock_vanilla = Mock()
        mock_crd = Mock()
        from kubernetes.client import ApiException

        mock_crd.list_namespaced_custom_object.side_effect = ApiException(
            status=404, reason="Not Found"
        )
        mock_vanilla._crd_api_client.return_value = mock_crd

        adapter = CertManagerAdapter(mock_vanilla)
        result = adapter.detect()

        assert result.installed is False
        assert result.total_certs == 0


class TestCertManagerAdapterListCertificates:
    def test_list_all(self) -> None:
        mock = _mock_vanilla_with_crds([_CERT_ITEM])
        adapter = CertManagerAdapter(mock)
        certs = adapter.list_certificates()

        assert len(certs) == 1
        cert = certs[0]
        assert isinstance(cert, Certificate)
        assert cert.name == "my-tls"
        assert cert.namespace == "default"
        assert cert.status == CertificateStatus.READY
        assert cert.dns_names == ["app.example.com"]
        assert cert.issuer_name == "letsencrypt-prod"
        assert cert.issuer_type == IssuerType.LETS_ENCRYPT
        assert cert.not_before == "2026-01-01T00:00:00Z"
        assert cert.not_after == "2027-01-01T00:00:00Z"
        assert cert.days_until_expiry is not None and cert.days_until_expiry > 0
        assert cert.auto_renew is True

    def test_list_empty(self) -> None:
        mock = _mock_vanilla_with_crds([])
        adapter = CertManagerAdapter(mock)
        assert adapter.list_certificates() == []


class TestCertManagerAdapterGetCertificate:
    def test_get_found(self) -> None:
        mock = _mock_vanilla_with_crds([_CERT_ITEM])
        adapter = CertManagerAdapter(mock)
        cert = adapter.get_certificate("my-tls", "default")

        assert cert.name == "my-tls"
        assert cert.namespace == "default"

    def test_get_not_found(self) -> None:
        mock = _mock_vanilla_with_crds([{"metadata": {"name": "other", "namespace": "ns"}}])
        adapter = CertManagerAdapter(mock)
        with pytest.raises(Exception):
            adapter.get_certificate("nope", "ns")


class TestCertManagerAdapterIssuers:
    def test_list_cluster_issuers(self) -> None:
        # list_issuers calls list_cluster_custom_object twice: clusterissuers + issuers
        mock = _mock_vanilla_with_crds([_ISSUER_ITEM], [])
        adapter = CertManagerAdapter(mock)
        issuers = adapter.list_issuers()

        assert len(issuers) == 1
        iss = issuers[0]
        assert iss.name == "letsencrypt-prod"
        assert iss.kind == "ClusterIssuer"
        assert iss.ready is True
        assert iss.server == "https://acme-v02.api.letsencrypt.org/directory"

    def test_list_empty(self) -> None:
        mock = _mock_vanilla_with_crds([], [])
        adapter = CertManagerAdapter(mock)
        assert adapter.list_issuers() == []
