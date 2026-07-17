from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.semantic_log_search.semantic_log_search_command import (
    SemanticLogSearchCommand,
)
from hexawyn.application.ports.driving.semantic_log_search.semantic_log_search_response import (
    SemanticLogSearchResponse,
)
from hexawyn.application.ports.driving.semantic_log_search.semantic_log_search_service_port import (
    SemanticLogSearchServicePort,
)
from hexawyn.application.use_case.semantic_log_search.semantic_log_search_use_case import (
    SemanticLogSearchUseCase,
)


class TestSemanticLogSearchUseCase:
    def test_execute_delegates_to_service(self) -> None:
        service = MagicMock(spec=SemanticLogSearchServicePort)
        expected = SemanticLogSearchResponse(pattern="connection refused")
        service.search.return_value = expected
        use_case = SemanticLogSearchUseCase(service=service)
        command = SemanticLogSearchCommand(pattern="connection refused")

        result = use_case.execute(command)

        service.search.assert_called_once_with(command)
        assert result is expected
