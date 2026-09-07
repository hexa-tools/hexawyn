from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.troubleshooting.watch_pod_logs.command import (
    WatchPodLogsCommand,
)
from hexawyn.application.use_case.troubleshooting.watch_pod_logs.response import (
    WatchPodLogsResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class WatchPodLogsServicePort(ABC):
    @abstractmethod
    def watch(self, command: WatchPodLogsCommand) -> WatchPodLogsResponse: ...
