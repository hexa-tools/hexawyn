from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.security.detect_missing_probes.command import (
    DetectMissingProbesCommand,
)
from hexawyn.application.use_case.security.detect_missing_probes.response import (
    DetectMissingProbesResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class DetectMissingProbesServicePort(ABC):
    @abstractmethod
    def detect_missing_probes(
        self, command: DetectMissingProbesCommand
    ) -> DetectMissingProbesResponse: ...
