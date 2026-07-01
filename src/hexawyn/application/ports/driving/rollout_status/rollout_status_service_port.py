from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.rollout_status.rollout_status_command import (
    RolloutStatusCommand,
)
from hexawyn.application.ports.driving.rollout_status.rollout_status_response import (
    RolloutStatusResponse,
)


class RolloutStatusServicePort(ABC):
    @abstractmethod
    def get_status(self, command: RolloutStatusCommand) -> RolloutStatusResponse:
        """Get real-time status of a Rollout with canary weight."""
