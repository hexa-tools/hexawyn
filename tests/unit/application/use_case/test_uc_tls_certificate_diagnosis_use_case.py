"""Unit tests for TLSCertificateDiagnosisUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.tls_certificate_diagnosis.tls_certificate_diagnosis_service_port import (
    TLSCertificateDiagnosisServicePort,
)
from hexawyn.application.use_case.tls_certificate_diagnosis.tls_certificate_diagnosis_use_case import (
    TLSCertificateDiagnosisUseCase,
)


class TestTLSCertificateDiagnosisUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=TLSCertificateDiagnosisServicePort)
        use_case = TLSCertificateDiagnosisUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.diagnose.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=TLSCertificateDiagnosisServicePort)
        mock_service.diagnose.side_effect = RuntimeError("test error")
        use_case = TLSCertificateDiagnosisUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
