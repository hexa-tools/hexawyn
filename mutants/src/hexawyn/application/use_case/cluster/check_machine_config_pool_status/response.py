from dataclasses import dataclass

from hexawyn.domain.models.machine_config_pool_health import (
    MachineConfigPoolHealthReport,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class CheckMachineConfigPoolStatusResponse:
    result: MachineConfigPoolHealthReport | None = None
    error: str | None = None
