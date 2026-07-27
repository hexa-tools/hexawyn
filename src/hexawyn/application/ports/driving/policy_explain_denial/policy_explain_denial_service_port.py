from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.governance.policy_explain_denial.command import (
    PolicyExplainDenialCommand,
)
from hexawyn.application.use_case.governance.policy_explain_denial.response import (
    PolicyExplainDenialResponse,
)


class PolicyExplainDenialServicePort(ABC):
    @abstractmethod
    def explain(self, command: PolicyExplainDenialCommand) -> PolicyExplainDenialResponse: ...
