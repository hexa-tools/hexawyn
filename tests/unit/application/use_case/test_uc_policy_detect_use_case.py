"""Unit tests for PolicyDetectUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.policy_detect.policy_detect_service_port import (
    PolicyDetectServicePort,
)
from hexawyn.application.use_case.policy_detect.policy_detect_use_case import PolicyDetectUseCase


class TestPolicyDetectUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=PolicyDetectServicePort)
        use_case = PolicyDetectUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.detect.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=PolicyDetectServicePort)
        mock_service.detect.side_effect = RuntimeError("test error")
        use_case = PolicyDetectUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
