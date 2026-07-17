"""Unit tests for CertsGetUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.certs_get.certs_get_service_port import CertsGetServicePort
from hexawyn.application.use_case.certs_get.certs_get_use_case import CertsGetUseCase


class TestCertsGetUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=CertsGetServicePort)
        use_case = CertsGetUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.get_cert.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=CertsGetServicePort)
        mock_service.get_cert.side_effect = RuntimeError("test error")
        use_case = CertsGetUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
