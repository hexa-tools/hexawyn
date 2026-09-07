from abc import ABC, abstractmethod

from hexawyn.domain.models.etcd_logs import ETCDLogLine, ETCDLogsRequest


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ETCDLogsPort(ABC):
    @abstractmethod
    def fetch_logs(self, request: ETCDLogsRequest) -> list[ETCDLogLine]: ...
