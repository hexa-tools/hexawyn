from __future__ import annotations

from hexawyn.application.ports.driving.plan_spike_provisioning.plan_spike_provisioning_command import (  # noqa: E501
    PlanSpikeProvisioningCommand,
)
from hexawyn.application.ports.driving.plan_spike_provisioning.plan_spike_provisioning_response import (  # noqa: E501
    PlanSpikeProvisioningResponse,
)
from hexawyn.application.ports.driving.plan_spike_provisioning.plan_spike_provisioning_service_port import (  # noqa: E501
    PlanSpikeProvisioningServicePort,
)


class PlanSpikeProvisioningUseCase:
    def __init__(self, service: PlanSpikeProvisioningServicePort) -> None:
        self._service = service

    def execute(self, command: PlanSpikeProvisioningCommand) -> PlanSpikeProvisioningResponse:
        return self._service.plan(command)
