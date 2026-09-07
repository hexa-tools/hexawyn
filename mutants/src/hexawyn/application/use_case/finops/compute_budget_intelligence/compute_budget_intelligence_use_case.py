from __future__ import annotations

from hexawyn.application.ports.driven.budget_intelligence_port import BudgetIntelligencePort
from hexawyn.application.use_case.finops.compute_budget_intelligence.command import (  # noqa: E501
    ComputeBudgetIntelligenceCommand,
)
from hexawyn.application.use_case.finops.compute_budget_intelligence.response import (  # noqa: E501
    ComputeBudgetIntelligenceResponse,
)
from hexawyn.domain.services.budget_intelligence.budget_intelligence_service import (
    compute_budget_intelligence,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁComputeBudgetIntelligenceUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁComputeBudgetIntelligenceUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class ComputeBudgetIntelligenceUseCase:
    @_mutmut_mutated(mutants_xǁComputeBudgetIntelligenceUseCaseǁ__init____mutmut)
    def __init__(self, budget_intelligence_port: BudgetIntelligencePort) -> None:
        self._port = budget_intelligence_port
    def xǁComputeBudgetIntelligenceUseCaseǁ__init____mutmut_orig(self, budget_intelligence_port: BudgetIntelligencePort) -> None:
        self._port = budget_intelligence_port
    def xǁComputeBudgetIntelligenceUseCaseǁ__init____mutmut_1(self, budget_intelligence_port: BudgetIntelligencePort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁComputeBudgetIntelligenceUseCaseǁexecute__mutmut)
    def execute(
        self, command: ComputeBudgetIntelligenceCommand
    ) -> ComputeBudgetIntelligenceResponse:
        data = self._port.get_budget_intelligence_data(command.period)
        result = compute_budget_intelligence(data, period=command.period)
        return ComputeBudgetIntelligenceResponse(result=result)

    def xǁComputeBudgetIntelligenceUseCaseǁexecute__mutmut_orig(
        self, command: ComputeBudgetIntelligenceCommand
    ) -> ComputeBudgetIntelligenceResponse:
        data = self._port.get_budget_intelligence_data(command.period)
        result = compute_budget_intelligence(data, period=command.period)
        return ComputeBudgetIntelligenceResponse(result=result)

    def xǁComputeBudgetIntelligenceUseCaseǁexecute__mutmut_1(
        self, command: ComputeBudgetIntelligenceCommand
    ) -> ComputeBudgetIntelligenceResponse:
        data = None
        result = compute_budget_intelligence(data, period=command.period)
        return ComputeBudgetIntelligenceResponse(result=result)

    def xǁComputeBudgetIntelligenceUseCaseǁexecute__mutmut_2(
        self, command: ComputeBudgetIntelligenceCommand
    ) -> ComputeBudgetIntelligenceResponse:
        data = self._port.get_budget_intelligence_data(None)
        result = compute_budget_intelligence(data, period=command.period)
        return ComputeBudgetIntelligenceResponse(result=result)

    def xǁComputeBudgetIntelligenceUseCaseǁexecute__mutmut_3(
        self, command: ComputeBudgetIntelligenceCommand
    ) -> ComputeBudgetIntelligenceResponse:
        data = self._port.get_budget_intelligence_data(command.period)
        result = None
        return ComputeBudgetIntelligenceResponse(result=result)

    def xǁComputeBudgetIntelligenceUseCaseǁexecute__mutmut_4(
        self, command: ComputeBudgetIntelligenceCommand
    ) -> ComputeBudgetIntelligenceResponse:
        data = self._port.get_budget_intelligence_data(command.period)
        result = compute_budget_intelligence(None, period=command.period)
        return ComputeBudgetIntelligenceResponse(result=result)

    def xǁComputeBudgetIntelligenceUseCaseǁexecute__mutmut_5(
        self, command: ComputeBudgetIntelligenceCommand
    ) -> ComputeBudgetIntelligenceResponse:
        data = self._port.get_budget_intelligence_data(command.period)
        result = compute_budget_intelligence(data, period=None)
        return ComputeBudgetIntelligenceResponse(result=result)

    def xǁComputeBudgetIntelligenceUseCaseǁexecute__mutmut_6(
        self, command: ComputeBudgetIntelligenceCommand
    ) -> ComputeBudgetIntelligenceResponse:
        data = self._port.get_budget_intelligence_data(command.period)
        result = compute_budget_intelligence(period=command.period)
        return ComputeBudgetIntelligenceResponse(result=result)

    def xǁComputeBudgetIntelligenceUseCaseǁexecute__mutmut_7(
        self, command: ComputeBudgetIntelligenceCommand
    ) -> ComputeBudgetIntelligenceResponse:
        data = self._port.get_budget_intelligence_data(command.period)
        result = compute_budget_intelligence(data, )
        return ComputeBudgetIntelligenceResponse(result=result)

    def xǁComputeBudgetIntelligenceUseCaseǁexecute__mutmut_8(
        self, command: ComputeBudgetIntelligenceCommand
    ) -> ComputeBudgetIntelligenceResponse:
        data = self._port.get_budget_intelligence_data(command.period)
        result = compute_budget_intelligence(data, period=command.period)
        return ComputeBudgetIntelligenceResponse(result=None)

mutants_xǁComputeBudgetIntelligenceUseCaseǁ__init____mutmut['_mutmut_orig'] = ComputeBudgetIntelligenceUseCase.xǁComputeBudgetIntelligenceUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁComputeBudgetIntelligenceUseCaseǁ__init____mutmut['xǁComputeBudgetIntelligenceUseCaseǁ__init____mutmut_1'] = ComputeBudgetIntelligenceUseCase.xǁComputeBudgetIntelligenceUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁComputeBudgetIntelligenceUseCaseǁexecute__mutmut['_mutmut_orig'] = ComputeBudgetIntelligenceUseCase.xǁComputeBudgetIntelligenceUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁComputeBudgetIntelligenceUseCaseǁexecute__mutmut['xǁComputeBudgetIntelligenceUseCaseǁexecute__mutmut_1'] = ComputeBudgetIntelligenceUseCase.xǁComputeBudgetIntelligenceUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁComputeBudgetIntelligenceUseCaseǁexecute__mutmut['xǁComputeBudgetIntelligenceUseCaseǁexecute__mutmut_2'] = ComputeBudgetIntelligenceUseCase.xǁComputeBudgetIntelligenceUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁComputeBudgetIntelligenceUseCaseǁexecute__mutmut['xǁComputeBudgetIntelligenceUseCaseǁexecute__mutmut_3'] = ComputeBudgetIntelligenceUseCase.xǁComputeBudgetIntelligenceUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁComputeBudgetIntelligenceUseCaseǁexecute__mutmut['xǁComputeBudgetIntelligenceUseCaseǁexecute__mutmut_4'] = ComputeBudgetIntelligenceUseCase.xǁComputeBudgetIntelligenceUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁComputeBudgetIntelligenceUseCaseǁexecute__mutmut['xǁComputeBudgetIntelligenceUseCaseǁexecute__mutmut_5'] = ComputeBudgetIntelligenceUseCase.xǁComputeBudgetIntelligenceUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁComputeBudgetIntelligenceUseCaseǁexecute__mutmut['xǁComputeBudgetIntelligenceUseCaseǁexecute__mutmut_6'] = ComputeBudgetIntelligenceUseCase.xǁComputeBudgetIntelligenceUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁComputeBudgetIntelligenceUseCaseǁexecute__mutmut['xǁComputeBudgetIntelligenceUseCaseǁexecute__mutmut_7'] = ComputeBudgetIntelligenceUseCase.xǁComputeBudgetIntelligenceUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁComputeBudgetIntelligenceUseCaseǁexecute__mutmut['xǁComputeBudgetIntelligenceUseCaseǁexecute__mutmut_8'] = ComputeBudgetIntelligenceUseCase.xǁComputeBudgetIntelligenceUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
