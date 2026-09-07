from __future__ import annotations

from hexawyn.application.ports.driven.budget_projection_port import BudgetProjectionPort
from hexawyn.application.use_case.finops.project_budget.command import (
    ProjectBudgetCommand,
)
from hexawyn.application.use_case.finops.project_budget.response import (
    ProjectBudgetResponse,
)
from hexawyn.domain.services.budget_projection.budget_projection_service import (
    BudgetProjectionService,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁProjectBudgetUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁProjectBudgetUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class ProjectBudgetUseCase:
    @_mutmut_mutated(mutants_xǁProjectBudgetUseCaseǁ__init____mutmut)
    def __init__(self, budget_port: BudgetProjectionPort) -> None:
        self._port = budget_port
        self._engine = BudgetProjectionService()
    def xǁProjectBudgetUseCaseǁ__init____mutmut_orig(self, budget_port: BudgetProjectionPort) -> None:
        self._port = budget_port
        self._engine = BudgetProjectionService()
    def xǁProjectBudgetUseCaseǁ__init____mutmut_1(self, budget_port: BudgetProjectionPort) -> None:
        self._port = None
        self._engine = BudgetProjectionService()
    def xǁProjectBudgetUseCaseǁ__init____mutmut_2(self, budget_port: BudgetProjectionPort) -> None:
        self._port = budget_port
        self._engine = None

    @_mutmut_mutated(mutants_xǁProjectBudgetUseCaseǁexecute__mutmut)
    def execute(self, command: ProjectBudgetCommand) -> ProjectBudgetResponse:
        history = self._port.get_monthly_cost_history(command.history_months)
        result = self._engine.project(
            history=history,
            horizon_months=command.horizon_months,
            budget_threshold_usd=command.budget_threshold_usd,
            exclude_months=command.exclude_months,
        )
        return ProjectBudgetResponse(result=result)  # type: ignore

    def xǁProjectBudgetUseCaseǁexecute__mutmut_orig(self, command: ProjectBudgetCommand) -> ProjectBudgetResponse:
        history = self._port.get_monthly_cost_history(command.history_months)
        result = self._engine.project(
            history=history,
            horizon_months=command.horizon_months,
            budget_threshold_usd=command.budget_threshold_usd,
            exclude_months=command.exclude_months,
        )
        return ProjectBudgetResponse(result=result)  # type: ignore

    def xǁProjectBudgetUseCaseǁexecute__mutmut_1(self, command: ProjectBudgetCommand) -> ProjectBudgetResponse:
        history = None
        result = self._engine.project(
            history=history,
            horizon_months=command.horizon_months,
            budget_threshold_usd=command.budget_threshold_usd,
            exclude_months=command.exclude_months,
        )
        return ProjectBudgetResponse(result=result)  # type: ignore

    def xǁProjectBudgetUseCaseǁexecute__mutmut_2(self, command: ProjectBudgetCommand) -> ProjectBudgetResponse:
        history = self._port.get_monthly_cost_history(None)
        result = self._engine.project(
            history=history,
            horizon_months=command.horizon_months,
            budget_threshold_usd=command.budget_threshold_usd,
            exclude_months=command.exclude_months,
        )
        return ProjectBudgetResponse(result=result)  # type: ignore

    def xǁProjectBudgetUseCaseǁexecute__mutmut_3(self, command: ProjectBudgetCommand) -> ProjectBudgetResponse:
        history = self._port.get_monthly_cost_history(command.history_months)
        result = None
        return ProjectBudgetResponse(result=result)  # type: ignore

    def xǁProjectBudgetUseCaseǁexecute__mutmut_4(self, command: ProjectBudgetCommand) -> ProjectBudgetResponse:
        history = self._port.get_monthly_cost_history(command.history_months)
        result = self._engine.project(
            history=None,
            horizon_months=command.horizon_months,
            budget_threshold_usd=command.budget_threshold_usd,
            exclude_months=command.exclude_months,
        )
        return ProjectBudgetResponse(result=result)  # type: ignore

    def xǁProjectBudgetUseCaseǁexecute__mutmut_5(self, command: ProjectBudgetCommand) -> ProjectBudgetResponse:
        history = self._port.get_monthly_cost_history(command.history_months)
        result = self._engine.project(
            history=history,
            horizon_months=None,
            budget_threshold_usd=command.budget_threshold_usd,
            exclude_months=command.exclude_months,
        )
        return ProjectBudgetResponse(result=result)  # type: ignore

    def xǁProjectBudgetUseCaseǁexecute__mutmut_6(self, command: ProjectBudgetCommand) -> ProjectBudgetResponse:
        history = self._port.get_monthly_cost_history(command.history_months)
        result = self._engine.project(
            history=history,
            horizon_months=command.horizon_months,
            budget_threshold_usd=None,
            exclude_months=command.exclude_months,
        )
        return ProjectBudgetResponse(result=result)  # type: ignore

    def xǁProjectBudgetUseCaseǁexecute__mutmut_7(self, command: ProjectBudgetCommand) -> ProjectBudgetResponse:
        history = self._port.get_monthly_cost_history(command.history_months)
        result = self._engine.project(
            history=history,
            horizon_months=command.horizon_months,
            budget_threshold_usd=command.budget_threshold_usd,
            exclude_months=None,
        )
        return ProjectBudgetResponse(result=result)  # type: ignore

    def xǁProjectBudgetUseCaseǁexecute__mutmut_8(self, command: ProjectBudgetCommand) -> ProjectBudgetResponse:
        history = self._port.get_monthly_cost_history(command.history_months)
        result = self._engine.project(
            horizon_months=command.horizon_months,
            budget_threshold_usd=command.budget_threshold_usd,
            exclude_months=command.exclude_months,
        )
        return ProjectBudgetResponse(result=result)  # type: ignore

    def xǁProjectBudgetUseCaseǁexecute__mutmut_9(self, command: ProjectBudgetCommand) -> ProjectBudgetResponse:
        history = self._port.get_monthly_cost_history(command.history_months)
        result = self._engine.project(
            history=history,
            budget_threshold_usd=command.budget_threshold_usd,
            exclude_months=command.exclude_months,
        )
        return ProjectBudgetResponse(result=result)  # type: ignore

    def xǁProjectBudgetUseCaseǁexecute__mutmut_10(self, command: ProjectBudgetCommand) -> ProjectBudgetResponse:
        history = self._port.get_monthly_cost_history(command.history_months)
        result = self._engine.project(
            history=history,
            horizon_months=command.horizon_months,
            exclude_months=command.exclude_months,
        )
        return ProjectBudgetResponse(result=result)  # type: ignore

    def xǁProjectBudgetUseCaseǁexecute__mutmut_11(self, command: ProjectBudgetCommand) -> ProjectBudgetResponse:
        history = self._port.get_monthly_cost_history(command.history_months)
        result = self._engine.project(
            history=history,
            horizon_months=command.horizon_months,
            budget_threshold_usd=command.budget_threshold_usd,
            )
        return ProjectBudgetResponse(result=result)  # type: ignore

    def xǁProjectBudgetUseCaseǁexecute__mutmut_12(self, command: ProjectBudgetCommand) -> ProjectBudgetResponse:
        history = self._port.get_monthly_cost_history(command.history_months)
        result = self._engine.project(
            history=history,
            horizon_months=command.horizon_months,
            budget_threshold_usd=command.budget_threshold_usd,
            exclude_months=command.exclude_months,
        )
        return ProjectBudgetResponse(result=None)  # type: ignore

mutants_xǁProjectBudgetUseCaseǁ__init____mutmut['_mutmut_orig'] = ProjectBudgetUseCase.xǁProjectBudgetUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁProjectBudgetUseCaseǁ__init____mutmut['xǁProjectBudgetUseCaseǁ__init____mutmut_1'] = ProjectBudgetUseCase.xǁProjectBudgetUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁProjectBudgetUseCaseǁ__init____mutmut['xǁProjectBudgetUseCaseǁ__init____mutmut_2'] = ProjectBudgetUseCase.xǁProjectBudgetUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁProjectBudgetUseCaseǁexecute__mutmut['_mutmut_orig'] = ProjectBudgetUseCase.xǁProjectBudgetUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁProjectBudgetUseCaseǁexecute__mutmut['xǁProjectBudgetUseCaseǁexecute__mutmut_1'] = ProjectBudgetUseCase.xǁProjectBudgetUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁProjectBudgetUseCaseǁexecute__mutmut['xǁProjectBudgetUseCaseǁexecute__mutmut_2'] = ProjectBudgetUseCase.xǁProjectBudgetUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁProjectBudgetUseCaseǁexecute__mutmut['xǁProjectBudgetUseCaseǁexecute__mutmut_3'] = ProjectBudgetUseCase.xǁProjectBudgetUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁProjectBudgetUseCaseǁexecute__mutmut['xǁProjectBudgetUseCaseǁexecute__mutmut_4'] = ProjectBudgetUseCase.xǁProjectBudgetUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁProjectBudgetUseCaseǁexecute__mutmut['xǁProjectBudgetUseCaseǁexecute__mutmut_5'] = ProjectBudgetUseCase.xǁProjectBudgetUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁProjectBudgetUseCaseǁexecute__mutmut['xǁProjectBudgetUseCaseǁexecute__mutmut_6'] = ProjectBudgetUseCase.xǁProjectBudgetUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁProjectBudgetUseCaseǁexecute__mutmut['xǁProjectBudgetUseCaseǁexecute__mutmut_7'] = ProjectBudgetUseCase.xǁProjectBudgetUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁProjectBudgetUseCaseǁexecute__mutmut['xǁProjectBudgetUseCaseǁexecute__mutmut_8'] = ProjectBudgetUseCase.xǁProjectBudgetUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁProjectBudgetUseCaseǁexecute__mutmut['xǁProjectBudgetUseCaseǁexecute__mutmut_9'] = ProjectBudgetUseCase.xǁProjectBudgetUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁProjectBudgetUseCaseǁexecute__mutmut['xǁProjectBudgetUseCaseǁexecute__mutmut_10'] = ProjectBudgetUseCase.xǁProjectBudgetUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁProjectBudgetUseCaseǁexecute__mutmut['xǁProjectBudgetUseCaseǁexecute__mutmut_11'] = ProjectBudgetUseCase.xǁProjectBudgetUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁProjectBudgetUseCaseǁexecute__mutmut['xǁProjectBudgetUseCaseǁexecute__mutmut_12'] = ProjectBudgetUseCase.xǁProjectBudgetUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
