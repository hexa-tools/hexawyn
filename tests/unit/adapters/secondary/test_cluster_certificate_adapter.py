from __future__ import annotations

from unittest.mock import Mock

import pytest
from hexawyn.adapters.secondary.kubernetes_cluster_certificate_adapter import (
    _extract_cert_pem,
    _get_annotations,
    _raise_on_rbac,
)
from hexawyn.domain.errors import InsufficientPermissionsError


class TestExtractCertPem:
    def test_empty_data(self) -> None:
        secret = Mock()
        type(secret).data = None
        assert _extract_cert_pem(secret) == ""

    def test_no_tls_key(self) -> None:
        secret = Mock(data={})
        assert _extract_cert_pem(secret) == ""

    def test_invalid_base64(self) -> None:
        secret = Mock(data={"tls.crt": "!!!invalid!!!"})
        assert _extract_cert_pem(secret) == ""

    def test_valid(self) -> None:
        import base64

        pem = "-----BEGIN CERTIFICATE-----\nMIIBxTCCAU0=\n-----END CERTIFICATE-----"
        b64 = base64.b64encode(pem.encode()).decode()
        secret = Mock(data={"tls.crt": b64})
        result = _extract_cert_pem(secret)
        assert "BEGIN CERTIFICATE" in result


class TestGetAnnotations:
    def test_empty(self) -> None:
        secret = Mock(metadata=None)
        assert _get_annotations(secret) == {}

    def test_with_annotations(self) -> None:
        secret = Mock(metadata=Mock(annotations={"key": "val"}))
        assert _get_annotations(secret) == {"key": "val"}

    def test_not_dict(self) -> None:
        secret = Mock(metadata=Mock(annotations="bad"))
        assert _get_annotations(secret) == {}


class K8sError(Exception):
    def __init__(self, status: int) -> None:
        self.status = status


class TestRaiseOnRbac:
    def test_forbidden(self) -> None:
        with pytest.raises(InsufficientPermissionsError):
            _raise_on_rbac("ns", K8sError(403))

    def test_other_does_not_raise(self) -> None:
        _raise_on_rbac("ns", K8sError(500))
