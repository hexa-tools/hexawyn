"""Unit tests for KedaScaledObjectGetUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.keda_scaledobject_get.keda_scaledobject_get_service_port import (
    KedaScaledObjectGetServicePort,
)
from hexawyn.application.use_case.keda_scaledobject_get.keda_scaledobject_get_use_case import (
    KedaScaledObjectGetUseCase,
)


class TestKedaScaledObjectGetUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=KedaScaledObjectGetServicePort)
        use_case = KedaScaledObjectGetUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.get_object.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=KedaScaledObjectGetServicePort)
        mock_service.get_object.side_effect = RuntimeError("test error")
        use_case = KedaScaledObjectGetUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
