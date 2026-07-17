"""Unit tests for KedaScaledObjectsListUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.keda_scaledobjects_list.keda_scaledobjects_list_service_port import (
    KedaScaledObjectsListServicePort,
)
from hexawyn.application.use_case.keda_scaledobjects_list.keda_scaledobjects_list_use_case import (
    KedaScaledObjectsListUseCase,
)


class TestKedaScaledObjectsListUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=KedaScaledObjectsListServicePort)
        use_case = KedaScaledObjectsListUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.list_objects.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=KedaScaledObjectsListServicePort)
        mock_service.list_objects.side_effect = RuntimeError("test error")
        use_case = KedaScaledObjectsListUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
