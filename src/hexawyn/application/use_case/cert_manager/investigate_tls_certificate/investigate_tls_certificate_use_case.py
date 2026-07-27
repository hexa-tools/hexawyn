from __future__ import annotations

from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.use_case.cert_manager.investigate_tls_certificate.command import (
    InvestigateTLSCertificateCommand,
)
from hexawyn.application.use_case.cert_manager.investigate_tls_certificate.response import (
    InvestigateTLSCertificateResponse,
)


class InvestigateTLSCertificateUseCase:
    def __init__(self, k8s_port: K8sPort) -> None:
        self._k8s = k8s_port

    def execute(
        self,
        command: InvestigateTLSCertificateCommand,
    ) -> InvestigateTLSCertificateResponse:
        return InvestigateTLSCertificateResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            certificate_found=False,
            status="NotChecked",
        )
