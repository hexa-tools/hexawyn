from __future__ import annotations

import pytest
from hexawyn.adapters.secondary.gitops.cert_manager_detector import (
    CertManagerDetector,
)
from hexawyn.application.ports.driven.cert_manager_port import CertManagerPort
from hexawyn.domain.errors import ComponentNotInstalledError


class TestCertManagerDetector:
    def test_implements_port(self) -> None:
        detector = CertManagerDetector()
        assert isinstance(detector, CertManagerPort)

    def test_detect_returns_not_installed(self) -> None:
        detector = CertManagerDetector()
        result = detector.detect()
        assert result.installed is False
        assert result.total_certs == 0

    def test_list_certificates_raises(self) -> None:
        detector = CertManagerDetector()
        with pytest.raises(ComponentNotInstalledError):
            detector.list_certificates()

    def test_get_certificate_raises(self) -> None:
        detector = CertManagerDetector()
        with pytest.raises(ComponentNotInstalledError):
            detector.get_certificate(name="x", namespace="ns")

    def test_list_issuers_raises(self) -> None:
        detector = CertManagerDetector()
        with pytest.raises(ComponentNotInstalledError):
            detector.list_issuers()

    def test_get_issuer_raises(self) -> None:
        detector = CertManagerDetector()
        with pytest.raises(ComponentNotInstalledError):
            detector.get_issuer(name="x")

    def test_list_challenges_raises(self) -> None:
        detector = CertManagerDetector()
        with pytest.raises(ComponentNotInstalledError):
            detector.list_challenges()

    def test_list_requests_raises(self) -> None:
        detector = CertManagerDetector()
        with pytest.raises(ComponentNotInstalledError):
            detector.list_requests()
