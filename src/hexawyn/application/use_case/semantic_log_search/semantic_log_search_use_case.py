from __future__ import annotations

from hexawyn.application.ports.driving.semantic_log_search.semantic_log_search_command import (
    SemanticLogSearchCommand,
)
from hexawyn.application.ports.driving.semantic_log_search.semantic_log_search_response import (
    SemanticLogSearchResponse,
)
from hexawyn.application.ports.driving.semantic_log_search.semantic_log_search_service_port import (
    SemanticLogSearchServicePort,
)


class SemanticLogSearchUseCase:
    def __init__(self, service: SemanticLogSearchServicePort) -> None:
        self._svc = service

    def execute(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
        return self._svc.search(command)
