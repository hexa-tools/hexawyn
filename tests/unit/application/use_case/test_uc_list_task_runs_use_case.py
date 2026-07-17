"""Unit tests for ListTaskRunsUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.list_task_runs.list_task_runs_service_port import (
    ListTaskRunsServicePort,
)
from hexawyn.application.use_case.list_task_runs.list_task_runs_use_case import ListTaskRunsUseCase


class TestListTaskRunsUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=ListTaskRunsServicePort)
        use_case = ListTaskRunsUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.list_task_runs.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=ListTaskRunsServicePort)
        mock_service.list_task_runs.side_effect = RuntimeError("test error")
        use_case = ListTaskRunsUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
