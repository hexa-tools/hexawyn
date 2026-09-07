from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cluster.hot_node_analysis.command import (
    HotNodeAnalysisCommand,
)
from hexawyn.application.use_case.cluster.hot_node_analysis.response import (
    HotNodeAnalysisResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class HotNodeAnalysisServicePort(ABC):
    @abstractmethod
    def analyze(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse: ...
