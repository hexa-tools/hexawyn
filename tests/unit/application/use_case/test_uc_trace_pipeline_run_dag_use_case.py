"""Unit tests for TracePipelineRunDAGUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.trace_pipeline_run_dag.trace_pipeline_run_dag_service_port import (
    TracePipelineRunDAGServicePort,
)
from hexawyn.application.use_case.trace_pipeline_run_dag.trace_pipeline_run_dag_use_case import (
    TracePipelineRunDAGUseCase,
)


class TestTracePipelineRunDAGUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=TracePipelineRunDAGServicePort)
        use_case = TracePipelineRunDAGUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.trace_pipeline_run_dag.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=TracePipelineRunDAGServicePort)
        mock_service.trace_pipeline_run_dag.side_effect = RuntimeError("test error")
        use_case = TracePipelineRunDAGUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
