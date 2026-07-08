from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.policy_explain_denial.policy_explain_denial_command import (
    PolicyExplainDenialCommand,
)
from hexawyn.application.ports.driving.policy_explain_denial.policy_explain_denial_response import (
    PolicyExplainDenialResponse,
)


class PolicyExplainDenialServicePort(ABC):
    @abstractmethod
    def explain(self, command: PolicyExplainDenialCommand) -> PolicyExplainDenialResponse:
        """Explain why a resource was denied."""
