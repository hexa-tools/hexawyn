from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.policy_violations_list.policy_violations_list_command import (
    PolicyViolationsListCommand,
)
from hexawyn.application.ports.driving.policy_violations_list.policy_violations_list_response import (
    PolicyViolationsListResponse,
)


class PolicyViolationsListServicePort(ABC):
    @abstractmethod
    def list_violations(self, command: PolicyViolationsListCommand) -> PolicyViolationsListResponse:
        """List current policy violations."""
