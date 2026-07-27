from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.observability.analyze_pod_logs.analyze_pod_logs_use_case import (
    AnalyzePodLogsUseCase,
)
from hexawyn.application.use_case.observability.analyze_pod_logs.command import (
    AnalyzePodLogsCommand,
)
from hexawyn.application.use_case.observability.analyze_pod_logs.response import (
    AnalyzePodLogsResponse,
)


class TestAnalyzePodLogsUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.fetch_logs.return_value = []
        use_case = AnalyzePodLogsUseCase(port=port)
        result = use_case.execute(AnalyzePodLogsCommand(pod_name="api", namespace="default"))
        assert isinstance(result, AnalyzePodLogsResponse)

    def test_execute_empty_data(self) -> None:
        port = MagicMock()
        port.fetch_logs.return_value = []
        use_case = AnalyzePodLogsUseCase(port=port)
        result = use_case.execute(AnalyzePodLogsCommand(pod_name="api", namespace="default"))
        assert isinstance(result, AnalyzePodLogsResponse)
