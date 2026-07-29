from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cluster.plan_spike_provisioning.command import (
    PlanSpikeProvisioningCommand,
)
from hexawyn.application.use_case.cluster.plan_spike_provisioning.response import (
    PlanSpikeProvisioningResponse,
)


class PlanSpikeProvisioningServicePort(ABC):
    @abstractmethod
    def plan(self, command: PlanSpikeProvisioningCommand) -> PlanSpikeProvisioningResponse: ...
