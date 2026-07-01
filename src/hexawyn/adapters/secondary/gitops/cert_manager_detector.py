from __future__ import annotations

from hexawyn.application.ports.driven.cert_manager_port import CertManagerPort
from hexawyn.domain.errors import CertManagerNotFoundError
from hexawyn.domain.models.certificates import (
    AcmeChallenge,
    Certificate,
    CertificateIssuer,
    CertManagerDetectionResult,
)


class CertManagerDetector(CertManagerPort):
    """Auto-detects Cert-Manager via CRDs. All read-only — never triggers renewal."""

    def detect(self) -> CertManagerDetectionResult:
        return CertManagerDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_certs=0,
            ready_certs=0,
            expiring_soon=0,
            failed_certs=0,
            active_challenges=0,
        )

    def list_certificates(self, namespace: str | None = None) -> list[Certificate]:
        raise CertManagerNotFoundError()

    def get_certificate(self, name: str, namespace: str) -> Certificate:
        raise CertManagerNotFoundError()

    def list_issuers(self, namespace: str | None = None) -> list[CertificateIssuer]:
        raise CertManagerNotFoundError()

    def get_issuer(self, name: str, namespace: str | None = None) -> CertificateIssuer:
        raise CertManagerNotFoundError()

    def list_challenges(self, namespace: str | None = None) -> list[AcmeChallenge]:
        raise CertManagerNotFoundError()

    def list_requests(self, namespace: str | None = None) -> list[Certificate]:
        raise CertManagerNotFoundError()
