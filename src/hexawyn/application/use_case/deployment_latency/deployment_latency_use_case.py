from __future__ import annotations

from hexawyn.application.ports.driving.deployment_latency.deployment_latency_command import (
    DeploymentLatencyCommand,
)
from hexawyn.application.ports.driving.deployment_latency.deployment_latency_response import (
    DeploymentLatencyResponse,
)
from hexawyn.application.ports.driving.deployment_latency.deployment_latency_service_port import (
    DeploymentLatencyServicePort,
)


class DeploymentLatencyUseCase:
    def __init__(self, service: DeploymentLatencyServicePort) -> None:
        self._svc = service

    def execute(self, cmd: DeploymentLatencyCommand) -> DeploymentLatencyResponse:
        return self._svc.compare(cmd)
