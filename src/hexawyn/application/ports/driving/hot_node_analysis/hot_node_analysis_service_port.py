from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cluster.hot_node_analysis.command import (
    HotNodeAnalysisCommand,
)
from hexawyn.application.use_case.cluster.hot_node_analysis.response import (
    HotNodeAnalysisResponse,
)


class HotNodeAnalysisServicePort(ABC):
    @abstractmethod
    def analyze(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse: ...
