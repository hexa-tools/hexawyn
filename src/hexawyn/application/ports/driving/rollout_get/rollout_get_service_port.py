from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.rollout_get.rollout_get_command import (
    RolloutGetCommand,
)
from hexawyn.application.ports.driving.rollout_get.rollout_get_response import (
    RolloutGetResponse,
)


class RolloutGetServicePort(ABC):
    @abstractmethod
    def get_rollout(self, command: RolloutGetCommand) -> RolloutGetResponse:
        """Get detailed status of a specific Rollout."""
