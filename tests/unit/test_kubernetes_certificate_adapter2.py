from __future__ import annotations

from hexawyn.adapters.secondary.gitops.kubernetes_certificate_adapter import (
    KubernetesCertificateAdapter,
)
from hexawyn.application.ports.driven.certificate_investigation_port import (
    CertificateInvestigationPort,
)
from hexawyn.domain.models.tls_certificate_diagnosis import (
    TLSCertificateDiagnosticRequest,
)


class TestKubernetesCertificateAdapter:
    def test_implements_port(self) -> None:
        assert isinstance(KubernetesCertificateAdapter(), CertificateInvestigationPort)

    def test_fetch_pem_returns_none(self) -> None:
        r = KubernetesCertificateAdapter().fetch_certificate_pem(
            TLSCertificateDiagnosticRequest(ingress_name="x", namespace="ns")
        )
        assert r is None

    def test_fetch_hostname_returns_ingress_name(self) -> None:
        r = KubernetesCertificateAdapter().fetch_ingress_hostname(
            TLSCertificateDiagnosticRequest(ingress_name="payment-service", namespace="ns")
        )
        assert r == "payment-service"
