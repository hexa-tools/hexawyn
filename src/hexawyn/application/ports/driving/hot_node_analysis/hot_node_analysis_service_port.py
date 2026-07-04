from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.hot_node_analysis.hot_node_analysis_command import (
    HotNodeAnalysisCommand,
)
from hexawyn.application.ports.driving.hot_node_analysis.hot_node_analysis_response import (
    HotNodeAnalysisResponse,
)


class HotNodeAnalysisServicePort(ABC):
    @abstractmethod
    def analyze(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse: ...
