from hexawyn.application.ports.driven.pod_log_watch_port import PodLogWatchPort
from hexawyn.application.use_case.watch_pod_logs.command import WatchPodLogsCommand
from hexawyn.application.use_case.watch_pod_logs.response import WatchPodLogsResponse


class WatchPodLogsUseCase:
    def __init__(self, pod_log_watch_port: PodLogWatchPort) -> None:
        self._port = pod_log_watch_port

    def execute(self, command: WatchPodLogsCommand) -> WatchPodLogsResponse:
        return WatchPodLogsResponse()
