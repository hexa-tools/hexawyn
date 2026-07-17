"""Unit tests for DiffClusterResourcesUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.diff_cluster_resources.diff_cluster_resources_service_port import (
    DiffClusterResourcesServicePort,
)
from hexawyn.application.use_case.diff_cluster_resources.diff_cluster_resources_use_case import (
    DiffClusterResourcesUseCase,
)


class TestDiffClusterResourcesUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=DiffClusterResourcesServicePort)
        use_case = DiffClusterResourcesUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.diff.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=DiffClusterResourcesServicePort)
        mock_service.diff.side_effect = RuntimeError("test error")
        use_case = DiffClusterResourcesUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
