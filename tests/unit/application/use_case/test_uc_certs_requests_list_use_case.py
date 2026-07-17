"""Unit tests for CertsRequestsListUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.certs_requests_list.certs_requests_list_service_port import (
    CertsRequestsListServicePort,
)
from hexawyn.application.use_case.certs_requests_list.certs_requests_list_use_case import (
    CertsRequestsListUseCase,
)


class TestCertsRequestsListUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=CertsRequestsListServicePort)
        use_case = CertsRequestsListUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.list_requests.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=CertsRequestsListServicePort)
        mock_service.list_requests.side_effect = RuntimeError("test error")
        use_case = CertsRequestsListUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
