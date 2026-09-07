from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.networking.detect_unintended_external_exposure.command import (
    DetectUnintendedExternalExposureCommand,
)
from hexawyn.application.use_case.networking.detect_unintended_external_exposure.response import (
    DetectUnintendedExternalExposureResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class DetectUnintendedExternalExposureServicePort(ABC):
    @abstractmethod
    def detect_unintended_exposure(
        self, command: DetectUnintendedExternalExposureCommand
    ) -> DetectUnintendedExternalExposureResponse: ...
