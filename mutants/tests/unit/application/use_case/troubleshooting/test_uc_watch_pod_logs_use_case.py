from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.troubleshooting.watch_pod_logs.command import (
    WatchPodLogsCommand,
)
from hexawyn.application.use_case.troubleshooting.watch_pod_logs.response import (  # noqa: E501
    WatchPodLogsResponse,
)
from hexawyn.application.use_case.troubleshooting.watch_pod_logs.watch_pod_logs_use_case import (  # noqa: E501
    WatchPodLogsUseCase,
)


class TestWatchPodLogsUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.stream_logs.return_value = iter([])
        alert = MagicMock()

        use_case = WatchPodLogsUseCase(
            watch_port=port,
            alert_port=alert,
        )
        result = use_case.execute(WatchPodLogsCommand(pod_name="api", namespace="default"))

        assert isinstance(result, WatchPodLogsResponse)
