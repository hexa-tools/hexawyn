from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.observability.deployment_latency.command import (
    DeploymentLatencyCommand,
)
from hexawyn.application.use_case.observability.deployment_latency.response import (
    DeploymentLatencyResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class DeploymentLatencyServicePort(ABC):
    @abstractmethod
    def compare(self, command: DeploymentLatencyCommand) -> DeploymentLatencyResponse: ...
