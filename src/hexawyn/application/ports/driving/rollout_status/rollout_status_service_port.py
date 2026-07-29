from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.workloads.rollout_status.command import (
    RolloutStatusCommand,
)
from hexawyn.application.use_case.workloads.rollout_status.response import (
    RolloutStatusResponse,
)


class RolloutStatusServicePort(ABC):
    @abstractmethod
    def get_status(self, command: RolloutStatusCommand) -> RolloutStatusResponse: ...
