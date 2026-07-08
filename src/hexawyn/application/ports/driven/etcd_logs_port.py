from abc import ABC, abstractmethod

from hexawyn.domain.models.etcd_logs import ETCDLogLine, ETCDLogsRequest


class ETCDLogsPort(ABC):
    @abstractmethod
    def fetch_logs(self, request: ETCDLogsRequest) -> list[ETCDLogLine]: ...
