from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.cert_manager.tls_certificate_diagnosis.command import (
    TLSCertificateDiagnosisCommand,
)
from hexawyn.application.use_case.cert_manager.tls_certificate_diagnosis.response import (
    TLSCertificateDiagnosisResponse,
)
from hexawyn.application.use_case.cert_manager.tls_certificate_diagnosis.tls_certificate_diagnosis_use_case import (  # noqa: E501
    TLSCertificateDiagnosisUseCase,
)


class TestTLSCertificateDiagnosisUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.fetch_certificate_pem.return_value = ""
        port.fetch_ingress_hostname.return_value = ""

        use_case = TLSCertificateDiagnosisUseCase(port=port)
        result = use_case.execute(
            TLSCertificateDiagnosisCommand(ingress_name="api-tls", namespace="default")
        )

        assert isinstance(result, TLSCertificateDiagnosisResponse)
