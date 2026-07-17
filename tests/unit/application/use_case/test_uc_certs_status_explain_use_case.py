"""Unit tests for CertsStatusExplainUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.certs_status_explain.certs_status_explain_service_port import (
    CertsStatusExplainServicePort,
)
from hexawyn.application.use_case.certs_status_explain.certs_status_explain_use_case import (
    CertsStatusExplainUseCase,
)


class TestCertsStatusExplainUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=CertsStatusExplainServicePort)
        use_case = CertsStatusExplainUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.explain.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=CertsStatusExplainServicePort)
        mock_service.explain.side_effect = RuntimeError("test error")
        use_case = CertsStatusExplainUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
