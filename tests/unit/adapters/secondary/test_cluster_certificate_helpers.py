from __future__ import annotations

import base64
from unittest.mock import Mock

from hexawyn.adapters.secondary.kubernetes_cluster_certificate_adapter import (
    KubernetesClusterCertificateAdapter,
    _extract_cert_pem,
    _get_annotations,
    _raise_on_rbac,
)
from hexawyn.application.ports.driven.cluster_certificate_health_port import (
    ClusterCertificateHealthPort,
)
from hexawyn.domain.errors import InsufficientPermissionsError


def _mk(**attrs: object) -> Mock:
    m = Mock()
    for k, v in attrs.items():
        setattr(m, k, v)
    return m


class TestKubernetesClusterCertificateAdapter:
    def test_implements_port(self) -> None:
        assert isinstance(KubernetesClusterCertificateAdapter(Mock()), ClusterCertificateHealthPort)


class TestExtractCertPem:
    def test_valid_cert(self) -> None:
        cert_pem = "-----BEGIN CERTIFICATE-----\nMIID...\n-----END CERTIFICATE-----"
        encoded = base64.b64encode(cert_pem.encode()).decode()
        secret = _mk(data={"tls.crt": encoded})
        result = _extract_cert_pem(secret)
        assert result == cert_pem

    def test_no_data_returns_empty(self) -> None:
        secret = _mk(data=None)
        assert _extract_cert_pem(secret) == ""

    def test_no_tls_crt_returns_empty(self) -> None:
        secret = _mk(data={"other": "value"})
        assert _extract_cert_pem(secret) == ""

    def test_data_not_dict_returns_empty(self) -> None:
        secret = _mk(data="bad")
        assert _extract_cert_pem(secret) == ""

    def test_invalid_base64_returns_empty(self) -> None:
        secret = _mk(data={"tls.crt": "not-base64!!!"})
        assert _extract_cert_pem(secret) == ""


class TestGetAnnotations:
    def test_returns_annotations(self) -> None:
        secret = _mk(metadata=_mk(annotations={"cert-manager.io/certificate-name": "my-cert"}))
        result = _get_annotations(secret)
        assert result == {"cert-manager.io/certificate-name": "my-cert"}

    def test_no_metadata_returns_empty(self) -> None:
        secret = _mk(metadata=None)
        assert _get_annotations(secret) == {}

    def test_no_annotations_returns_empty(self) -> None:
        secret = _mk(metadata=_mk(annotations=None))
        assert _get_annotations(secret) == {}

    def test_annotations_not_dict(self) -> None:
        secret = _mk(metadata=_mk(annotations="bad"))
        assert _get_annotations(secret) == {}


class TestRaiseOnRBAC:
    def test_forbidden_raises(self) -> None:
        import pytest

        exc = Exception("mock error")
        exc.status = 403  # type: ignore[attr-defined]
        with pytest.raises(InsufficientPermissionsError):
            _raise_on_rbac("default", exc)  # type: ignore[arg-type]

    def test_other_status_does_not_raise(self) -> None:
        exc = Exception("mock error")
        exc.status = 500  # type: ignore[attr-defined]
        _raise_on_rbac("default", exc)  # type: ignore[arg-type]
