from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.rollouts_list.rollouts_list_command import (
    RolloutsListCommand,
)
from hexawyn.application.ports.driving.rollouts_list.rollouts_list_response import (
    RolloutsListResponse,
)


class RolloutsListServicePort(ABC):
    @abstractmethod
    def list_rollouts(self, command: RolloutsListCommand) -> RolloutsListResponse:
        """List all Rollouts."""
