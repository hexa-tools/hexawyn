"""Unit tests for CheckResourceConstraintsUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.check_resource_constraints.check_resource_constraints_service_port import (
    CheckResourceConstraintsServicePort,
)
from hexawyn.application.use_case.check_resource_constraints.check_resource_constraints_use_case import (
    CheckResourceConstraintsUseCase,
)


class TestCheckResourceConstraintsUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=CheckResourceConstraintsServicePort)
        use_case = CheckResourceConstraintsUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.check_resource_constraints.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=CheckResourceConstraintsServicePort)
        mock_service.check_resource_constraints.side_effect = RuntimeError("test error")
        use_case = CheckResourceConstraintsUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
