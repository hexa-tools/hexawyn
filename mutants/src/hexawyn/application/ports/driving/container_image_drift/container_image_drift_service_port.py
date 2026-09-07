from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.security.detect_container_image_drift.command import (
    DetectContainerImageDriftCommand,
)
from hexawyn.application.use_case.security.detect_container_image_drift.response import (
    DetectContainerImageDriftResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ContainerImageDriftServicePort(ABC):
    @abstractmethod
    def detect_image_drift(
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse: ...
