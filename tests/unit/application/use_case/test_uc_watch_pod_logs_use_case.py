"""Unit tests for WatchPodLogsUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.watch_pod_logs.watch_pod_logs_service_port import (
    WatchPodLogsServicePort,
)
from hexawyn.application.use_case.watch_pod_logs.watch_pod_logs_use_case import WatchPodLogsUseCase


class TestWatchPodLogsUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=WatchPodLogsServicePort)
        use_case = WatchPodLogsUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.watch.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=WatchPodLogsServicePort)
        mock_service.watch.side_effect = RuntimeError("test error")
        use_case = WatchPodLogsUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
