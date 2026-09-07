from dataclasses import dataclass

from hexawyn.domain.models.zombie_detection import ZombieDetectionResult


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class DetectZombiesResponse:
    result: ZombieDetectionResult
