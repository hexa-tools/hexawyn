"""Unit tests for CheckClusterOperatorHealthUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.check_cluster_operator_health.check_cluster_operator_health_service_port import (
    CheckClusterOperatorHealthServicePort,
)
from hexawyn.application.use_case.check_cluster_operator_health.check_cluster_operator_health_use_case import (
    CheckClusterOperatorHealthUseCase,
)


class TestCheckClusterOperatorHealthUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=CheckClusterOperatorHealthServicePort)
        use_case = CheckClusterOperatorHealthUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.check.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=CheckClusterOperatorHealthServicePort)
        mock_service.check.side_effect = RuntimeError("test error")
        use_case = CheckClusterOperatorHealthUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
