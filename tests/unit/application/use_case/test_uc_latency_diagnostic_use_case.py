"""Unit tests for LatencyDiagnosticUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.latency_diagnostic.latency_diagnostic_service_port import (
    LatencyDiagnosticServicePort,
)
from hexawyn.application.use_case.latency_diagnostic.latency_diagnostic_use_case import (
    LatencyDiagnosticUseCase,
)


class TestLatencyDiagnosticUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=LatencyDiagnosticServicePort)
        use_case = LatencyDiagnosticUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.diagnose.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=LatencyDiagnosticServicePort)
        mock_service.diagnose.side_effect = RuntimeError("test error")
        use_case = LatencyDiagnosticUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
