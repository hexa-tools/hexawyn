"""Unit tests for PolicyExplainDenialUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.policy_explain_denial.policy_explain_denial_service_port import (
    PolicyExplainDenialServicePort,
)
from hexawyn.application.use_case.policy_explain_denial.policy_explain_denial_use_case import (
    PolicyExplainDenialUseCase,
)


class TestPolicyExplainDenialUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=PolicyExplainDenialServicePort)
        use_case = PolicyExplainDenialUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.explain.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=PolicyExplainDenialServicePort)
        mock_service.explain.side_effect = RuntimeError("test error")
        use_case = PolicyExplainDenialUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
