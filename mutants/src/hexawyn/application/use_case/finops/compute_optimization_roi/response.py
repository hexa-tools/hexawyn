from dataclasses import dataclass

from hexawyn.domain.models.optimization_roi import OptimizationRoiReport


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class ComputeOptimizationRoiResponse:
    result: OptimizationRoiReport
