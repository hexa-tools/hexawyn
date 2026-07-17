"""Unit tests for KedaScaledObjectTriggersUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.keda_scaledobject_triggers.keda_scaledobject_triggers_service_port import (
    KedaScaledObjectTriggersServicePort,
)
from hexawyn.application.use_case.keda_scaledobject_triggers.keda_scaledobject_triggers_use_case import (
    KedaScaledObjectTriggersUseCase,
)


class TestKedaScaledObjectTriggersUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=KedaScaledObjectTriggersServicePort)
        use_case = KedaScaledObjectTriggersUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.get_triggers.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=KedaScaledObjectTriggersServicePort)
        mock_service.get_triggers.side_effect = RuntimeError("test error")
        use_case = KedaScaledObjectTriggersUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
