"""Unit tests for ErrorAttributionUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.error_attribution.error_attribution_service_port import (
    ErrorAttributionServicePort,
)
from hexawyn.application.use_case.error_attribution.error_attribution_use_case import (
    ErrorAttributionUseCase,
)


class TestErrorAttributionUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=ErrorAttributionServicePort)
        use_case = ErrorAttributionUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.attribute.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=ErrorAttributionServicePort)
        mock_service.attribute.side_effect = RuntimeError("test error")
        use_case = ErrorAttributionUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
