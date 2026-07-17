"""Unit tests for AnalyzeIncidentCostUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.analyze_incident_cost.analyze_incident_cost_service_port import (
    AnalyzeIncidentCostServicePort,
)
from hexawyn.application.use_case.analyze_incident_cost.analyze_incident_cost_use_case import (
    AnalyzeIncidentCostUseCase,
)


class TestAnalyzeIncidentCostUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=AnalyzeIncidentCostServicePort)
        use_case = AnalyzeIncidentCostUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.analyze.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=AnalyzeIncidentCostServicePort)
        mock_service.analyze.side_effect = RuntimeError("test error")
        use_case = AnalyzeIncidentCostUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
