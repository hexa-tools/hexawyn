from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.cert_manager.investigate_tls_certificate.command import (
    InvestigateTLSCertificateCommand,
)
from hexawyn.application.use_case.cert_manager.investigate_tls_certificate.investigate_tls_certificate_use_case import (  # noqa: E501
    InvestigateTLSCertificateUseCase,
)
from hexawyn.application.use_case.cert_manager.investigate_tls_certificate.response import (
    InvestigateTLSCertificateResponse,
)


class TestInvestigateTLSCertificateUseCase:
    def test_execute_returns_response(self) -> None:
        k8s = MagicMock()

        use_case = InvestigateTLSCertificateUseCase(k8s_port=k8s)
        result = use_case.execute(
            InvestigateTLSCertificateCommand(
                ingress_name="api-tls",
                namespace="default",
            )
        )

        assert isinstance(result, InvestigateTLSCertificateResponse)
        assert result.ingress_name == "api-tls"

    def test_execute_not_found(self) -> None:
        k8s = MagicMock()

        use_case = InvestigateTLSCertificateUseCase(k8s_port=k8s)
        result = use_case.execute(
            InvestigateTLSCertificateCommand(
                ingress_name="nonexistent",
                namespace="default",
            )
        )

        assert result.certificate_found is False
