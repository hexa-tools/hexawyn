from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.policy_get.policy_get_command import (
    PolicyGetCommand,
)
from hexawyn.application.ports.driving.policy_get.policy_get_response import (
    PolicyGetResponse,
)


class PolicyGetServicePort(ABC):
    @abstractmethod
    def get_policy(self, command: PolicyGetCommand) -> PolicyGetResponse:
        """Get a specific policy detail."""
