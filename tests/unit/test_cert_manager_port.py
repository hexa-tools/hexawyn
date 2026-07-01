from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.cert_manager_port import CertManagerPort


class TestCertManagerPort:
    def test_is_abstract(self) -> None:
        assert issubclass(CertManagerPort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            CertManagerPort()  # type: ignore[abstract]

    def test_has_methods(self) -> None:
        for name in [
            "detect",
            "list_certificates",
            "get_certificate",
            "list_issuers",
            "get_issuer",
            "list_challenges",
            "list_requests",
        ]:
            method = getattr(CertManagerPort, name)
            assert getattr(method, "__isabstractmethod__", False)
