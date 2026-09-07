from abc import ABC, abstractmethod
from collections.abc import Iterator

from hexawyn.domain.models.analyze_pod_logs import PodLogLine
from hexawyn.domain.models.watch_pod_logs import WatchPodLogsRequest


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class PodLogWatchPort(ABC):
    @abstractmethod
    def watch(self, request: WatchPodLogsRequest) -> Iterator[PodLogLine]: ...

    @abstractmethod
    def pod_exists(self, pod_name: str, namespace: str) -> bool: ...
