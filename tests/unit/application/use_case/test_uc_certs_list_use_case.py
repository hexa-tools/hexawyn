"""Unit tests for CertsListUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.certs_list.certs_list_service_port import (
    CertsListServicePort,
)
from hexawyn.application.use_case.certs_list.certs_list_use_case import CertsListUseCase


class TestCertsListUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=CertsListServicePort)
        use_case = CertsListUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.list_certs.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=CertsListServicePort)
        mock_service.list_certs.side_effect = RuntimeError("test error")
        use_case = CertsListUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
