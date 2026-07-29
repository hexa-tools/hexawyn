from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.observability.latency_diagnostic.command import (
    LatencyDiagnosticCommand,
)
from hexawyn.application.use_case.observability.latency_diagnostic.latency_diagnostic_use_case import (  # noqa: E501
    LatencyDiagnosticUseCase,
)
from hexawyn.application.use_case.observability.latency_diagnostic.response import (
    LatencyDiagnosticResponse,
)


class TestLatencyDiagnosticUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.get_latency_data.return_value = []
        use_case = LatencyDiagnosticUseCase(port=port)
        result = use_case.execute(LatencyDiagnosticCommand(service_name="api-gateway"))
        assert isinstance(result, LatencyDiagnosticResponse)

    def test_execute_empty_data(self) -> None:
        port = MagicMock()
        port.get_latency_data.return_value = []
        use_case = LatencyDiagnosticUseCase(port=port)
        result = use_case.execute(LatencyDiagnosticCommand(service_name="api-gateway"))
        assert isinstance(result, LatencyDiagnosticResponse)
