from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.observability.error_attribution.command import (
    ErrorAttributionCommand,
)
from hexawyn.application.use_case.observability.error_attribution.error_attribution_use_case import (  # noqa: E501
    ErrorAttributionUseCase,
)
from hexawyn.application.use_case.observability.error_attribution.response import (
    ErrorAttributionResponse,
)


class TestErrorAttributionUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.get_error_attribution.return_value = []
        use_case = ErrorAttributionUseCase(port=port)
        result = use_case.execute(ErrorAttributionCommand())
        assert isinstance(result, ErrorAttributionResponse)

    def test_execute_empty_data(self) -> None:
        port = MagicMock()
        port.get_error_attribution.return_value = []
        use_case = ErrorAttributionUseCase(port=port)
        result = use_case.execute(ErrorAttributionCommand())
        assert isinstance(result, ErrorAttributionResponse)
