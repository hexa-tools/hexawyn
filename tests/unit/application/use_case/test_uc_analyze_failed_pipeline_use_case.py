"""Unit tests for AnalyzeFailedPipelineUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.analyze_failed_pipeline.analyze_failed_pipeline_service_port import (
    AnalyzeFailedPipelineServicePort,
)
from hexawyn.application.use_case.analyze_failed_pipeline.analyze_failed_pipeline_use_case import (
    AnalyzeFailedPipelineUseCase,
)


class TestAnalyzeFailedPipelineUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=AnalyzeFailedPipelineServicePort)
        use_case = AnalyzeFailedPipelineUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.analyze.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=AnalyzeFailedPipelineServicePort)
        mock_service.analyze.side_effect = RuntimeError("test error")
        use_case = AnalyzeFailedPipelineUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
