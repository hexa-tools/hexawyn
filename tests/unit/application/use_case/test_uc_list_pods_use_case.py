"""Unit tests for ListPodsUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.list_pods.list_pods_service_port import ListPodsServicePort
from hexawyn.application.use_case.list_pods.list_pods_use_case import ListPodsUseCase


class TestListPodsUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=ListPodsServicePort)
        use_case = ListPodsUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.list_pods.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=ListPodsServicePort)
        mock_service.list_pods.side_effect = RuntimeError("test error")
        use_case = ListPodsUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
