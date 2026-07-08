from __future__ import annotations

from hexawyn.application.ports.driving.watch_pod_logs.watch_pod_logs_command import (
    WatchPodLogsCommand,
)
from hexawyn.application.ports.driving.watch_pod_logs.watch_pod_logs_response import (
    WatchPodLogsResponse,
)
from hexawyn.application.ports.driving.watch_pod_logs.watch_pod_logs_service_port import (
    WatchPodLogsServicePort,
)


class WatchPodLogsUseCase:
    def __init__(self, service: WatchPodLogsServicePort) -> None:
        self._svc = service

    def execute(self, command: WatchPodLogsCommand) -> WatchPodLogsResponse:
        return self._svc.watch(command)
