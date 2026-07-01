from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.policy_list.policy_list_command import (
    PolicyListCommand,
)
from hexawyn.application.ports.driving.policy_list.policy_list_response import (
    PolicyListResponse,
)


class PolicyListServicePort(ABC):
    @abstractmethod
    def list_policies(self, command: PolicyListCommand) -> PolicyListResponse:
        """List all policies."""
