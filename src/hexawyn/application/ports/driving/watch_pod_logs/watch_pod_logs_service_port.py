from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.watch_pod_logs.watch_pod_logs_command import (
    WatchPodLogsCommand,
)
from hexawyn.application.ports.driving.watch_pod_logs.watch_pod_logs_response import (
    WatchPodLogsResponse,
)


class WatchPodLogsServicePort(ABC):
    @abstractmethod
    def watch(self, command: WatchPodLogsCommand) -> WatchPodLogsResponse: ...
