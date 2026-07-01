from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.live_topology_mapper.live_topology_mapper_command import (
    LiveTopologyMapperCommand,
)
from hexawyn.application.ports.driving.live_topology_mapper.live_topology_mapper_response import (
    LiveTopologyMapperResponse,
)


class LiveTopologyMapperServicePort(ABC):
    @abstractmethod
    def map_topology(self, command: LiveTopologyMapperCommand) -> LiveTopologyMapperResponse: ...
