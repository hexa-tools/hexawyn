"""Unit tests for ListPipelineRunsInNamespaceUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.list_pipeline_runs_in_namespace.list_pipeline_runs_in_namespace_service_port import (
    ListPipelineRunsInNamespaceServicePort,
)
from hexawyn.application.use_case.list_pipeline_runs_in_namespace.list_pipeline_runs_in_namespace_use_case import (
    ListPipelineRunsInNamespaceUseCase,
)


class TestListPipelineRunsInNamespaceUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=ListPipelineRunsInNamespaceServicePort)
        use_case = ListPipelineRunsInNamespaceUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.list_pipeline_runs_in_namespace.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=ListPipelineRunsInNamespaceServicePort)
        mock_service.list_pipeline_runs_in_namespace.side_effect = RuntimeError("test error")
        use_case = ListPipelineRunsInNamespaceUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
