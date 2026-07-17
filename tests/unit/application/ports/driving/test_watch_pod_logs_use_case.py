from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.watch_pod_logs.watch_pod_logs_command import (
    WatchPodLogsCommand,
)
from hexawyn.application.ports.driving.watch_pod_logs.watch_pod_logs_response import (
    WatchPodLogsResponse,
)
from hexawyn.application.ports.driving.watch_pod_logs.watch_pod_logs_service_port import (
    WatchPodLogsServicePort,
)
from hexawyn.application.use_case.watch_pod_logs.watch_pod_logs_use_case import (
    WatchPodLogsUseCase,
)


class TestWatchPodLogsUseCase:
    def test_execute_delegates_to_service(self) -> None:
        service = MagicMock(spec=WatchPodLogsServicePort)
        expected = WatchPodLogsResponse(pod_name="payment-service-7f9b")
        service.watch.return_value = expected
        use_case = WatchPodLogsUseCase(service=service)
        command = WatchPodLogsCommand(pod_name="payment-service-7f9b", namespace="prod")

        result = use_case.execute(command)

        service.watch.assert_called_once_with(command)
        assert result is expected
