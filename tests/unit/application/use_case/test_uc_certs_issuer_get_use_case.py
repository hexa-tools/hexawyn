"""Unit tests for CertsIssuerGetUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.certs_issuer_get.certs_issuer_get_service_port import (
    CertsIssuerGetServicePort,
)
from hexawyn.application.use_case.certs_issuer_get.certs_issuer_get_use_case import (
    CertsIssuerGetUseCase,
)


class TestCertsIssuerGetUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=CertsIssuerGetServicePort)
        use_case = CertsIssuerGetUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.get_issuer.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=CertsIssuerGetServicePort)
        mock_service.get_issuer.side_effect = RuntimeError("test error")
        use_case = CertsIssuerGetUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
