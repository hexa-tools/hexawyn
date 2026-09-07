from abc import ABC, abstractmethod

from hexawyn.domain.models.analyze_pod_logs import AnalyzePodLogsRequest, PodLogLine


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class PodLogsPort(ABC):
    @abstractmethod
    def fetch_logs(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]: ...
