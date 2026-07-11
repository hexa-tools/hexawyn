from __future__ import annotations

from dataclasses import dataclass

from hexawyn.domain.models.spike_provisioning import SpikeProvisioningReport


@dataclass
class PlanSpikeProvisioningResponse:
    result: SpikeProvisioningReport
