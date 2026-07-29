from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.governance.policy_explain_denial.command import (
    PolicyExplainDenialCommand,
)
from hexawyn.application.use_case.governance.policy_explain_denial.policy_explain_denial_use_case import (  # noqa: E501
    PolicyExplainDenialUseCase,
)
from hexawyn.application.use_case.governance.policy_explain_denial.response import (
    PolicyExplainDenialResponse,
)


class TestPolicyExplainDenialUseCase:
    def test_execute_returns_response(self) -> None:
        explanation = MagicMock()
        explanation.policy_name = "restrictive"
        explanation.rule_name = "validate-images"
        explanation.raw_message = "denied"
        explanation.human_explanation = "Image not allowed"
        explanation.fix_suggestion = "Use approved image"

        port = MagicMock()
        port.explain_denial.return_value = explanation

        use_case = PolicyExplainDenialUseCase(policy_port=port)
        result = use_case.execute(
            PolicyExplainDenialCommand(
                name="restrictive",
                namespace="default",
                resource_kind="Deployment",
                resource_name="nginx",
            )
        )

        assert isinstance(result, PolicyExplainDenialResponse)
        assert result.policy_name == "restrictive"
