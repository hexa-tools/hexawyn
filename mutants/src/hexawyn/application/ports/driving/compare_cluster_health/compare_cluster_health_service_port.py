from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cluster.compare_cluster_health.command import (
    CompareClusterHealthCommand,
)
from hexawyn.application.use_case.cluster.compare_cluster_health.response import (
    CompareClusterHealthResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class CompareClusterHealthServicePort(ABC):
    @abstractmethod
    def compare(self, command: CompareClusterHealthCommand) -> CompareClusterHealthResponse: ...
