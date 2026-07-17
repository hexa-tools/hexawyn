"""Unit tests for CompareClusterHealthUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.compare_cluster_health.compare_cluster_health_service_port import (
    CompareClusterHealthServicePort,
)
from hexawyn.application.use_case.compare_cluster_health.compare_cluster_health_use_case import (
    CompareClusterHealthUseCase,
)


class TestCompareClusterHealthUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=CompareClusterHealthServicePort)
        use_case = CompareClusterHealthUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.compare.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=CompareClusterHealthServicePort)
        mock_service.compare.side_effect = RuntimeError("test error")
        use_case = CompareClusterHealthUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
