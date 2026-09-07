from abc import ABC, abstractmethod

from hexawyn.application.use_case.troubleshooting.detect_pod_anomalies.command import (
    DetectPodAnomaliesCommand,
)
from hexawyn.application.use_case.troubleshooting.detect_pod_anomalies.response import (
    DetectPodAnomaliesResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class DetectPodAnomaliesServicePort(ABC):
    @abstractmethod
    def detect(self, command: DetectPodAnomaliesCommand) -> DetectPodAnomaliesResponse: ...
