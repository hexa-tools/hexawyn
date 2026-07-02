from abc import ABC, abstractmethod

from hexawyn.domain.models.analyze_pod_logs import AnalyzePodLogsRequest, PodLogLine


class PodLogsPort(ABC):
    @abstractmethod
    def fetch_logs(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]: ...
