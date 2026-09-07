from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cluster.global_health_check.command import (
    GlobalHealthCheckCommand,
)
from hexawyn.application.use_case.cluster.global_health_check.response import (
    GlobalHealthCheckResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class GlobalHealthCheckServicePort(ABC):
    @abstractmethod
    def global_health_check(
        self, command: GlobalHealthCheckCommand
    ) -> GlobalHealthCheckResponse: ...
