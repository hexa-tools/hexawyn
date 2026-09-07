from dataclasses import dataclass

from hexawyn.domain.models.consolidation import ConsolidatedKnowledge


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class RunConsolidationResponse:
    consolidated: list[ConsolidatedKnowledge]
    groups_found: int = 0
