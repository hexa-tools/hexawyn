from hexawyn.application.ports.driven.hot_node_analysis_port import HotNodeAnalysisPort
from hexawyn.application.use_case.hot_node_analysis.command import HotNodeAnalysisCommand
from hexawyn.application.use_case.hot_node_analysis.response import HotNodeAnalysisResponse


class HotNodeAnalysisUseCase:
    def __init__(self, port: HotNodeAnalysisPort) -> None:
        self._port = port

    def execute(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        return HotNodeAnalysisResponse()
