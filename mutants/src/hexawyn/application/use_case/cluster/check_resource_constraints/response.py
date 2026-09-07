from dataclasses import dataclass

from hexawyn.domain.models.resource_constraint import ResourceConstraintReport


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class CheckResourceConstraintsResponse:
    report: ResourceConstraintReport | None = None
