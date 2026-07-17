"""Unit tests for CertsIssuersListUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.certs_issuers_list.certs_issuers_list_service_port import (
    CertsIssuersListServicePort,
)
from hexawyn.application.use_case.certs_issuers_list.certs_issuers_list_use_case import (
    CertsIssuersListUseCase,
)


class TestCertsIssuersListUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=CertsIssuersListServicePort)
        use_case = CertsIssuersListUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.list_issuers.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=CertsIssuersListServicePort)
        mock_service.list_issuers.side_effect = RuntimeError("test error")
        use_case = CertsIssuersListUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
