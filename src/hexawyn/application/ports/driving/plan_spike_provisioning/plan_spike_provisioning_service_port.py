from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.plan_spike_provisioning.plan_spike_provisioning_command import (  # noqa: E501
    PlanSpikeProvisioningCommand,
)
from hexawyn.application.ports.driving.plan_spike_provisioning.plan_spike_provisioning_response import (  # noqa: E501
    PlanSpikeProvisioningResponse,
)


class PlanSpikeProvisioningServicePort(ABC):
    @abstractmethod
    def plan(self, command: PlanSpikeProvisioningCommand) -> PlanSpikeProvisioningResponse: ...
