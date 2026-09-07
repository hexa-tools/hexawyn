from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cluster.plan_spike_provisioning.command import (
    PlanSpikeProvisioningCommand,
)
from hexawyn.application.use_case.cluster.plan_spike_provisioning.response import (
    PlanSpikeProvisioningResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class PlanSpikeProvisioningServicePort(ABC):
    @abstractmethod
    def plan(self, command: PlanSpikeProvisioningCommand) -> PlanSpikeProvisioningResponse: ...
