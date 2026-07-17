"""Unit tests for GetPipelineRunStatusUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.get_pipeline_run_status.get_pipeline_run_status_service_port import (
    GetPipelineRunStatusServicePort,
)
from hexawyn.application.use_case.get_pipeline_run_status.get_pipeline_run_status_use_case import (
    GetPipelineRunStatusUseCase,
)


class TestGetPipelineRunStatusUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=GetPipelineRunStatusServicePort)
        use_case = GetPipelineRunStatusUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.get_pipeline_run_status.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=GetPipelineRunStatusServicePort)
        mock_service.get_pipeline_run_status.side_effect = RuntimeError("test error")
        use_case = GetPipelineRunStatusUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
