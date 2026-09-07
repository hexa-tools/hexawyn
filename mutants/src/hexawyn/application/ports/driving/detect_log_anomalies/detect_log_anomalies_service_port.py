from abc import ABC, abstractmethod

from hexawyn.application.use_case.troubleshooting.detect_log_anomalies.command import (
    DetectLogAnomaliesCommand,
)
from hexawyn.application.use_case.troubleshooting.detect_log_anomalies.response import (
    DetectLogAnomaliesResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class DetectLogAnomaliesServicePort(ABC):
    @abstractmethod
    def detect(self, command: DetectLogAnomaliesCommand) -> DetectLogAnomaliesResponse: ...
