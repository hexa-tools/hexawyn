from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.observability.redundant_calls.command import (
    RedundantCallsCommand,
)
from hexawyn.application.use_case.observability.redundant_calls.redundant_calls_use_case import (
    RedundantCallsUseCase,
)
from hexawyn.application.use_case.observability.redundant_calls.response import (
    RedundantCallsResponse,
)


class TestRedundantCallsUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.detect_redundant_calls.return_value = []
        use_case = RedundantCallsUseCase(port=port)
        result = use_case.execute(RedundantCallsCommand())
        assert isinstance(result, RedundantCallsResponse)

    def test_execute_empty_data(self) -> None:
        port = MagicMock()
        port.detect_redundant_calls.return_value = []
        use_case = RedundantCallsUseCase(port=port)
        result = use_case.execute(RedundantCallsCommand())
        assert isinstance(result, RedundantCallsResponse)
