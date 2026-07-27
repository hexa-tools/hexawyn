from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.observability.etcd_logs.command import (
    ETCDLogsCommand,
)
from hexawyn.application.use_case.observability.etcd_logs.response import (
    ETCDLogsResponse,
)


class ETCDLogsServicePort(ABC):
    @abstractmethod
    def retrieve(self, command: ETCDLogsCommand) -> ETCDLogsResponse: ...
