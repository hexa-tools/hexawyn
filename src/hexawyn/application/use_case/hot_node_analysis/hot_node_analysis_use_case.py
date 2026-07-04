from __future__ import annotations

from hexawyn.application.ports.driving.hot_node_analysis.hot_node_analysis_command import (
    HotNodeAnalysisCommand,
)
from hexawyn.application.ports.driving.hot_node_analysis.hot_node_analysis_response import (
    HotNodeAnalysisResponse,
)
from hexawyn.application.ports.driving.hot_node_analysis.hot_node_analysis_service_port import (
    HotNodeAnalysisServicePort,
)


class HotNodeAnalysisUseCase:
    def __init__(self, service: HotNodeAnalysisServicePort) -> None:
        self._svc = service

    def execute(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        return self._svc.analyze(command)
