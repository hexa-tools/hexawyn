from dataclasses import dataclass

from hexawyn.domain.models.prediction_roi import PredictionRoiReport


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class ComputePredictionRoiResponse:
    result: PredictionRoiReport
