from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.workloads.rollouts_detect.command import (
    RolloutsDetectCommand,
)
from hexawyn.application.use_case.workloads.rollouts_detect.response import (
    RolloutsDetectResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class RolloutsDetectServicePort(ABC):
    @abstractmethod
    def detect(self, command: RolloutsDetectCommand) -> RolloutsDetectResponse: ...
