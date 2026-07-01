from abc import ABC, abstractmethod

from hexawyn.domain.models.certificates import (
    AcmeChallenge,
    Certificate,
    CertificateIssuer,
    CertManagerDetectionResult,
)


class CertManagerPort(ABC):
    """Port for Cert-Manager operations — read-only. Never triggers renewal."""

    @abstractmethod
    def detect(self) -> CertManagerDetectionResult:
        """Detect Cert-Manager presence."""

    @abstractmethod
    def list_certificates(self, namespace: str | None = None) -> list[Certificate]:
        """List all certificates."""

    @abstractmethod
    def get_certificate(self, name: str, namespace: str) -> Certificate:
        """Get a specific certificate."""

    @abstractmethod
    def list_issuers(self, namespace: str | None = None) -> list[CertificateIssuer]:
        """List Issuers and ClusterIssuers."""

    @abstractmethod
    def get_issuer(self, name: str, namespace: str | None = None) -> CertificateIssuer:
        """Get a specific Issuer."""

    @abstractmethod
    def list_challenges(self, namespace: str | None = None) -> list[AcmeChallenge]:
        """List ACME challenges."""

    @abstractmethod
    def list_requests(self, namespace: str | None = None) -> list[Certificate]:
        """List CertificateRequests."""
