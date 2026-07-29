from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.observability.deployment_latency.command import (
    DeploymentLatencyCommand,
)
from hexawyn.application.use_case.observability.deployment_latency.response import (
    DeploymentLatencyResponse,
)


class DeploymentLatencyServicePort(ABC):
    @abstractmethod
    def compare(self, command: DeploymentLatencyCommand) -> DeploymentLatencyResponse: ...
