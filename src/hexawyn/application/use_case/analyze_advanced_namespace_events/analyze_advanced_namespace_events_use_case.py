from __future__ import annotations

from hexawyn.application.use_case.analyze_advanced_namespace_events.command import (
    AnalyzeAdvancedNamespaceEventsCommand,
)
from hexawyn.application.use_case.analyze_advanced_namespace_events.response import (
    AnalyzeAdvancedNamespaceEventsResponse,
)


class AnalyzeAdvancedNamespaceEventsUseCase:
    def __init__(self) -> None:
        pass

    def execute(
        self, command: AnalyzeAdvancedNamespaceEventsCommand
    ) -> AnalyzeAdvancedNamespaceEventsResponse:
        return AnalyzeAdvancedNamespaceEventsResponse()
