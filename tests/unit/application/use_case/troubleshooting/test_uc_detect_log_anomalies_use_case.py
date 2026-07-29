from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.troubleshooting.detect_log_anomalies.command import (
    DetectLogAnomaliesCommand,
)
from hexawyn.application.use_case.troubleshooting.detect_log_anomalies.detect_log_anomalies_use_case import (  # noqa: E501
    DetectLogAnomaliesUseCase,
)
from hexawyn.application.use_case.troubleshooting.detect_log_anomalies.response import (  # noqa: E501
    DetectLogAnomaliesResponse,
)


class TestDetectLogAnomaliesUseCase:
    def test_execute_returns_response_with_empty_logs(self) -> None:
        port = MagicMock()
        port.fetch_logs.return_value = []

        use_case = DetectLogAnomaliesUseCase(port=port)
        result = use_case.execute(DetectLogAnomaliesCommand(pod_name="api", namespace="default"))

        assert isinstance(result, DetectLogAnomaliesResponse)

    def test_execute_calls_port(self) -> None:
        port = MagicMock()
        port.fetch_logs.return_value = []

        use_case = DetectLogAnomaliesUseCase(port=port)
        use_case.execute(
            DetectLogAnomaliesCommand(
                pod_name="api",
                namespace="prod",
                time_window_minutes=120,
                zscore_threshold=2.5,
            )
        )

        assert port.fetch_logs.call_count == 1
