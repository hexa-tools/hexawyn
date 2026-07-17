"""Unit tests for ETCDLogsUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.etcd_logs.etcd_logs_service_port import ETCDLogsServicePort
from hexawyn.application.use_case.etcd_logs.etcd_logs_use_case import ETCDLogsUseCase


class TestETCDLogsUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=ETCDLogsServicePort)
        use_case = ETCDLogsUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.retrieve.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=ETCDLogsServicePort)
        mock_service.retrieve.side_effect = RuntimeError("test error")
        use_case = ETCDLogsUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
