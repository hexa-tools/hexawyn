from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.governance.policy_detect.command import (
    PolicyDetectCommand,
)
from hexawyn.application.use_case.governance.policy_detect.policy_detect_use_case import (
    PolicyDetectUseCase,
)
from hexawyn.application.use_case.governance.policy_detect.response import (
    PolicyDetectResponse,
)


class TestPolicyDetectUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.detect_policy_engine.return_value = {}

        use_case = PolicyDetectUseCase(policy_port=port)
        result = use_case.execute(PolicyDetectCommand())

        assert isinstance(result, PolicyDetectResponse)
