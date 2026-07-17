"""Unit tests for PipelineForServiceUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.pipeline_for_service.pipeline_for_service_service_port import (
    PipelineForServiceServicePort,
)
from hexawyn.application.use_case.pipeline_for_service.pipeline_for_service_use_case import (
    PipelineForServiceUseCase,
)


class TestPipelineForServiceUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=PipelineForServiceServicePort)
        use_case = PipelineForServiceUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.find.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=PipelineForServiceServicePort)
        mock_service.find.side_effect = RuntimeError("test error")
        use_case = PipelineForServiceUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
