"""Unit tests for AnalysisRunsListUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.analysis_runs_list.analysis_runs_list_service_port import (
    AnalysisRunsListServicePort,
)
from hexawyn.application.use_case.analysis_runs_list.analysis_runs_list_use_case import (
    AnalysisRunsListUseCase,
)


class TestAnalysisRunsListUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=AnalysisRunsListServicePort)
        use_case = AnalysisRunsListUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.list_analysis_runs.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=AnalysisRunsListServicePort)
        mock_service.list_analysis_runs.side_effect = RuntimeError("test error")
        use_case = AnalysisRunsListUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
