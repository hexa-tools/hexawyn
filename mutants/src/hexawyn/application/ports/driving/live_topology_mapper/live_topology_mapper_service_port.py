from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cluster.live_topology_mapper.command import (
    LiveTopologyMapperCommand,
)
from hexawyn.application.use_case.cluster.live_topology_mapper.response import (
    LiveTopologyMapperResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class LiveTopologyMapperServicePort(ABC):
    @abstractmethod
    def map_topology(self, command: LiveTopologyMapperCommand) -> LiveTopologyMapperResponse: ...
