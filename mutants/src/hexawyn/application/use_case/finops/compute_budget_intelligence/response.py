from dataclasses import dataclass

from hexawyn.domain.models.budget_intelligence import BudgetIntelligenceReport


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class ComputeBudgetIntelligenceResponse:
    result: BudgetIntelligenceReport
