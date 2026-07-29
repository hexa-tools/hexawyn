from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.governance.policy_get.command import (
    PolicyGetCommand,
)
from hexawyn.application.use_case.governance.policy_get.response import (
    PolicyGetResponse,
)


class PolicyGetServicePort(ABC):
    @abstractmethod
    def get_policy(self, command: PolicyGetCommand) -> PolicyGetResponse: ...
