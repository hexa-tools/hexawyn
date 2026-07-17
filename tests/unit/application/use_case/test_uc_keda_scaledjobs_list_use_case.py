"""Unit tests for KedaScaledJobsListUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.keda_scaledjobs_list.keda_scaledjobs_list_service_port import (
    KedaScaledJobsListServicePort,
)
from hexawyn.application.use_case.keda_scaledjobs_list.keda_scaledjobs_list_use_case import (
    KedaScaledJobsListUseCase,
)


class TestKedaScaledJobsListUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=KedaScaledJobsListServicePort)
        use_case = KedaScaledJobsListUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.list_jobs.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=KedaScaledJobsListServicePort)
        mock_service.list_jobs.side_effect = RuntimeError("test error")
        use_case = KedaScaledJobsListUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
