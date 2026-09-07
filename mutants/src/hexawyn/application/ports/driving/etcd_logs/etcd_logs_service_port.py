from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.observability.etcd_logs.command import (
    ETCDLogsCommand,
)
from hexawyn.application.use_case.observability.etcd_logs.response import (
    ETCDLogsResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ETCDLogsServicePort(ABC):
    @abstractmethod
    def retrieve(self, command: ETCDLogsCommand) -> ETCDLogsResponse: ...
