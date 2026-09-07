from __future__ import annotations

from typing import Protocol

from hexawyn.application.ports.driven.budget_intelligence_port import (
    BudgetIntelligenceData,
    BudgetIntelligencePort,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class BudgetIntelligenceSource(Protocol):
    def fetch_budget_intelligence_data(self, period: str) -> BudgetIntelligenceData: ...
mutants_xǁBudgetIntelligenceAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁBudgetIntelligenceAdapterǁget_budget_intelligence_data__mutmut: MutantDict = {}  # type: ignore


class BudgetIntelligenceAdapter(BudgetIntelligencePort):
    @_mutmut_mutated(mutants_xǁBudgetIntelligenceAdapterǁ__init____mutmut)
    def __init__(self, source: BudgetIntelligenceSource) -> None:
        self._source = source
    def xǁBudgetIntelligenceAdapterǁ__init____mutmut_orig(self, source: BudgetIntelligenceSource) -> None:
        self._source = source
    def xǁBudgetIntelligenceAdapterǁ__init____mutmut_1(self, source: BudgetIntelligenceSource) -> None:
        self._source = None

    @_mutmut_mutated(mutants_xǁBudgetIntelligenceAdapterǁget_budget_intelligence_data__mutmut)
    def get_budget_intelligence_data(self, period: str) -> BudgetIntelligenceData:
        return self._source.fetch_budget_intelligence_data(period)

    def xǁBudgetIntelligenceAdapterǁget_budget_intelligence_data__mutmut_orig(self, period: str) -> BudgetIntelligenceData:
        return self._source.fetch_budget_intelligence_data(period)

    def xǁBudgetIntelligenceAdapterǁget_budget_intelligence_data__mutmut_1(self, period: str) -> BudgetIntelligenceData:
        return self._source.fetch_budget_intelligence_data(None)

mutants_xǁBudgetIntelligenceAdapterǁ__init____mutmut['_mutmut_orig'] = BudgetIntelligenceAdapter.xǁBudgetIntelligenceAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁBudgetIntelligenceAdapterǁ__init____mutmut['xǁBudgetIntelligenceAdapterǁ__init____mutmut_1'] = BudgetIntelligenceAdapter.xǁBudgetIntelligenceAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁBudgetIntelligenceAdapterǁget_budget_intelligence_data__mutmut['_mutmut_orig'] = BudgetIntelligenceAdapter.xǁBudgetIntelligenceAdapterǁget_budget_intelligence_data__mutmut_orig # type: ignore # mutmut generated
mutants_xǁBudgetIntelligenceAdapterǁget_budget_intelligence_data__mutmut['xǁBudgetIntelligenceAdapterǁget_budget_intelligence_data__mutmut_1'] = BudgetIntelligenceAdapter.xǁBudgetIntelligenceAdapterǁget_budget_intelligence_data__mutmut_1 # type: ignore # mutmut generated
