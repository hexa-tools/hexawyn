from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.workloads.rollout_get.command import (
    RolloutGetCommand,
)
from hexawyn.application.use_case.workloads.rollout_get.response import (
    RolloutGetResponse,
)


class RolloutGetServicePort(ABC):
    @abstractmethod
    def get_rollout(self, command: RolloutGetCommand) -> RolloutGetResponse: ...
