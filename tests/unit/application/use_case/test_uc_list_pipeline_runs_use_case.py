"""Unit tests for ListPipelineRunsUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.list_pipeline_runs.list_pipeline_runs_service_port import (
    ListPipelineRunsServicePort,
)
from hexawyn.application.use_case.list_pipeline_runs.list_pipeline_runs_use_case import (
    ListPipelineRunsUseCase,
)


class TestListPipelineRunsUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=ListPipelineRunsServicePort)
        use_case = ListPipelineRunsUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.list_pipeline_runs.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=ListPipelineRunsServicePort)
        mock_service.list_pipeline_runs.side_effect = RuntimeError("test error")
        use_case = ListPipelineRunsUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
