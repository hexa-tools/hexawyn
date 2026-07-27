from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.governance.policy_list.command import (
    PolicyListCommand,
)
from hexawyn.application.use_case.governance.policy_list.response import (
    PolicyListResponse,
)


class PolicyListServicePort(ABC):
    @abstractmethod
    def list_policies(self, command: PolicyListCommand) -> PolicyListResponse: ...
