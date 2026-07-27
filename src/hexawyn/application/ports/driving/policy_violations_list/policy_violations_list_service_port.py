from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.governance.policy_violations_list.command import (
    PolicyViolationsListCommand,
)
from hexawyn.application.use_case.governance.policy_violations_list.response import (
    PolicyViolationsListResponse,
)


class PolicyViolationsListServicePort(ABC):
    @abstractmethod
    def list_violations(
        self, command: PolicyViolationsListCommand
    ) -> PolicyViolationsListResponse: ...
