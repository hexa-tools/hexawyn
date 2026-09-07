from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class AuditSecretRotationCommand:
    rotation_threshold_days: int = 90
