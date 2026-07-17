"""Unit tests for ProjectBudgetUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.project_budget.project_budget_service_port import (
    ProjectBudgetServicePort,
)
from hexawyn.application.use_case.project_budget.project_budget_use_case import ProjectBudgetUseCase


class TestProjectBudgetUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=ProjectBudgetServicePort)
        use_case = ProjectBudgetUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.project.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=ProjectBudgetServicePort)
        mock_service.project.side_effect = RuntimeError("test error")
        use_case = ProjectBudgetUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
