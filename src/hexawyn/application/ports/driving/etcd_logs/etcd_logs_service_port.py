from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.etcd_logs.etcd_logs_command import ETCDLogsCommand
from hexawyn.application.ports.driving.etcd_logs.etcd_logs_response import ETCDLogsResponse


class ETCDLogsServicePort(ABC):
    @abstractmethod
    def retrieve(self, command: ETCDLogsCommand) -> ETCDLogsResponse: ...
