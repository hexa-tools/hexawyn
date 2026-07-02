from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.deployment_latency.deployment_latency_command import (
    DeploymentLatencyCommand,
)
from hexawyn.application.ports.driving.deployment_latency.deployment_latency_response import (
    DeploymentLatencyResponse,
)


class DeploymentLatencyServicePort(ABC):
    @abstractmethod
    def compare(self, command: DeploymentLatencyCommand) -> DeploymentLatencyResponse: ...
