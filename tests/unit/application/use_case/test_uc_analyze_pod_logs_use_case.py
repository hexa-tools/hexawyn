"""Unit tests for AnalyzePodLogsUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.analyze_pod_logs.analyze_pod_logs_service_port import (
    AnalyzePodLogsServicePort,
)
from hexawyn.application.use_case.analyze_pod_logs.analyze_pod_logs_use_case import (
    AnalyzePodLogsUseCase,
)


class TestAnalyzePodLogsUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=AnalyzePodLogsServicePort)
        use_case = AnalyzePodLogsUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.analyze.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=AnalyzePodLogsServicePort)
        mock_service.analyze.side_effect = RuntimeError("test error")
        use_case = AnalyzePodLogsUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
