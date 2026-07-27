from dataclasses import dataclass

from hexawyn.domain.models.machine_config_pool_health import (
    MachineConfigPoolHealthReport,
)


@dataclass
class CheckMachineConfigPoolStatusResponse:
    result: MachineConfigPoolHealthReport | None = None
    error: str | None = None
