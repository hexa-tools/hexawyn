"""Unit tests for SemanticLogSearchUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.semantic_log_search.semantic_log_search_service_port import (
    SemanticLogSearchServicePort,
)
from hexawyn.application.use_case.semantic_log_search.semantic_log_search_use_case import (
    SemanticLogSearchUseCase,
)


class TestSemanticLogSearchUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=SemanticLogSearchServicePort)
        use_case = SemanticLogSearchUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.search.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=SemanticLogSearchServicePort)
        mock_service.search.side_effect = RuntimeError("test error")
        use_case = SemanticLogSearchUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
