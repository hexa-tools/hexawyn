"""Unit tests for PipelineRunLogsUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.pipeline_run_logs.pipeline_run_logs_service_port import (
    PipelineRunLogsServicePort,
)
from hexawyn.application.use_case.pipeline_run_logs.pipeline_run_logs_use_case import (
    PipelineRunLogsUseCase,
)


class TestPipelineRunLogsUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=PipelineRunLogsServicePort)
        use_case = PipelineRunLogsUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.get_logs.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=PipelineRunLogsServicePort)
        mock_service.get_logs.side_effect = RuntimeError("test error")
        use_case = PipelineRunLogsUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
