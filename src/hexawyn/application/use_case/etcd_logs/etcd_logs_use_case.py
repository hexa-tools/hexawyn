from __future__ import annotations

from hexawyn.application.ports.driving.etcd_logs.etcd_logs_command import ETCDLogsCommand
from hexawyn.application.ports.driving.etcd_logs.etcd_logs_response import ETCDLogsResponse
from hexawyn.application.ports.driving.etcd_logs.etcd_logs_service_port import ETCDLogsServicePort


class ETCDLogsUseCase:
    def __init__(self, service: ETCDLogsServicePort) -> None:
        self._svc = service

    def execute(self, cmd: ETCDLogsCommand) -> ETCDLogsResponse:
        return self._svc.retrieve(cmd)
