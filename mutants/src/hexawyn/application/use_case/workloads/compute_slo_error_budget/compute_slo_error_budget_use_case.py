from __future__ import annotations

from hexawyn.application.ports.driven.error_budget_port import ErrorBudgetPort
from hexawyn.application.use_case.workloads.compute_slo_error_budget.command import (
    ComputeSLOErrorBudgetCommand,
)
from hexawyn.application.use_case.workloads.compute_slo_error_budget.response import (
    ComputeSLOErrorBudgetResponse,
)
from hexawyn.domain.services.error_budget.slo_error_budget_engine import (
    SLOErrorBudgetBurnRateEngine,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁComputeSLOErrorBudgetUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut: MutantDict = {}  # type: ignore


class ComputeSLOErrorBudgetUseCase:
    @_mutmut_mutated(mutants_xǁComputeSLOErrorBudgetUseCaseǁ__init____mutmut)
    def __init__(self, error_budget_port: ErrorBudgetPort) -> None:
        self._port = error_budget_port
        self._engine = SLOErrorBudgetBurnRateEngine()
    def xǁComputeSLOErrorBudgetUseCaseǁ__init____mutmut_orig(self, error_budget_port: ErrorBudgetPort) -> None:
        self._port = error_budget_port
        self._engine = SLOErrorBudgetBurnRateEngine()
    def xǁComputeSLOErrorBudgetUseCaseǁ__init____mutmut_1(self, error_budget_port: ErrorBudgetPort) -> None:
        self._port = None
        self._engine = SLOErrorBudgetBurnRateEngine()
    def xǁComputeSLOErrorBudgetUseCaseǁ__init____mutmut_2(self, error_budget_port: ErrorBudgetPort) -> None:
        self._port = error_budget_port
        self._engine = None

    @_mutmut_mutated(mutants_xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut)
    def compute_slo_error_budget(
        self, command: ComputeSLOErrorBudgetCommand
    ) -> ComputeSLOErrorBudgetResponse:
        raw = self._port.fetch_success_rate(command.service_name, command.rolling_window_days)
        raw_dict: dict[str, object] = dict(raw)
        result = self._engine.compute(
            slo_target=command.slo_target,
            rolling_window_days=command.rolling_window_days,
            raw_success_rate=raw_dict,
        )
        return ComputeSLOErrorBudgetResponse(result=result)  # type: ignore

    def xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_orig(
        self, command: ComputeSLOErrorBudgetCommand
    ) -> ComputeSLOErrorBudgetResponse:
        raw = self._port.fetch_success_rate(command.service_name, command.rolling_window_days)
        raw_dict: dict[str, object] = dict(raw)
        result = self._engine.compute(
            slo_target=command.slo_target,
            rolling_window_days=command.rolling_window_days,
            raw_success_rate=raw_dict,
        )
        return ComputeSLOErrorBudgetResponse(result=result)  # type: ignore

    def xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_1(
        self, command: ComputeSLOErrorBudgetCommand
    ) -> ComputeSLOErrorBudgetResponse:
        raw = None
        raw_dict: dict[str, object] = dict(raw)
        result = self._engine.compute(
            slo_target=command.slo_target,
            rolling_window_days=command.rolling_window_days,
            raw_success_rate=raw_dict,
        )
        return ComputeSLOErrorBudgetResponse(result=result)  # type: ignore

    def xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_2(
        self, command: ComputeSLOErrorBudgetCommand
    ) -> ComputeSLOErrorBudgetResponse:
        raw = self._port.fetch_success_rate(None, command.rolling_window_days)
        raw_dict: dict[str, object] = dict(raw)
        result = self._engine.compute(
            slo_target=command.slo_target,
            rolling_window_days=command.rolling_window_days,
            raw_success_rate=raw_dict,
        )
        return ComputeSLOErrorBudgetResponse(result=result)  # type: ignore

    def xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_3(
        self, command: ComputeSLOErrorBudgetCommand
    ) -> ComputeSLOErrorBudgetResponse:
        raw = self._port.fetch_success_rate(command.service_name, None)
        raw_dict: dict[str, object] = dict(raw)
        result = self._engine.compute(
            slo_target=command.slo_target,
            rolling_window_days=command.rolling_window_days,
            raw_success_rate=raw_dict,
        )
        return ComputeSLOErrorBudgetResponse(result=result)  # type: ignore

    def xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_4(
        self, command: ComputeSLOErrorBudgetCommand
    ) -> ComputeSLOErrorBudgetResponse:
        raw = self._port.fetch_success_rate(command.rolling_window_days)
        raw_dict: dict[str, object] = dict(raw)
        result = self._engine.compute(
            slo_target=command.slo_target,
            rolling_window_days=command.rolling_window_days,
            raw_success_rate=raw_dict,
        )
        return ComputeSLOErrorBudgetResponse(result=result)  # type: ignore

    def xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_5(
        self, command: ComputeSLOErrorBudgetCommand
    ) -> ComputeSLOErrorBudgetResponse:
        raw = self._port.fetch_success_rate(command.service_name, )
        raw_dict: dict[str, object] = dict(raw)
        result = self._engine.compute(
            slo_target=command.slo_target,
            rolling_window_days=command.rolling_window_days,
            raw_success_rate=raw_dict,
        )
        return ComputeSLOErrorBudgetResponse(result=result)  # type: ignore

    def xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_6(
        self, command: ComputeSLOErrorBudgetCommand
    ) -> ComputeSLOErrorBudgetResponse:
        raw = self._port.fetch_success_rate(command.service_name, command.rolling_window_days)
        raw_dict: dict[str, object] = None
        result = self._engine.compute(
            slo_target=command.slo_target,
            rolling_window_days=command.rolling_window_days,
            raw_success_rate=raw_dict,
        )
        return ComputeSLOErrorBudgetResponse(result=result)  # type: ignore

    def xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_7(
        self, command: ComputeSLOErrorBudgetCommand
    ) -> ComputeSLOErrorBudgetResponse:
        raw = self._port.fetch_success_rate(command.service_name, command.rolling_window_days)
        raw_dict: dict[str, object] = dict(None)
        result = self._engine.compute(
            slo_target=command.slo_target,
            rolling_window_days=command.rolling_window_days,
            raw_success_rate=raw_dict,
        )
        return ComputeSLOErrorBudgetResponse(result=result)  # type: ignore

    def xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_8(
        self, command: ComputeSLOErrorBudgetCommand
    ) -> ComputeSLOErrorBudgetResponse:
        raw = self._port.fetch_success_rate(command.service_name, command.rolling_window_days)
        raw_dict: dict[str, object] = dict(raw)
        result = None
        return ComputeSLOErrorBudgetResponse(result=result)  # type: ignore

    def xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_9(
        self, command: ComputeSLOErrorBudgetCommand
    ) -> ComputeSLOErrorBudgetResponse:
        raw = self._port.fetch_success_rate(command.service_name, command.rolling_window_days)
        raw_dict: dict[str, object] = dict(raw)
        result = self._engine.compute(
            slo_target=None,
            rolling_window_days=command.rolling_window_days,
            raw_success_rate=raw_dict,
        )
        return ComputeSLOErrorBudgetResponse(result=result)  # type: ignore

    def xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_10(
        self, command: ComputeSLOErrorBudgetCommand
    ) -> ComputeSLOErrorBudgetResponse:
        raw = self._port.fetch_success_rate(command.service_name, command.rolling_window_days)
        raw_dict: dict[str, object] = dict(raw)
        result = self._engine.compute(
            slo_target=command.slo_target,
            rolling_window_days=None,
            raw_success_rate=raw_dict,
        )
        return ComputeSLOErrorBudgetResponse(result=result)  # type: ignore

    def xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_11(
        self, command: ComputeSLOErrorBudgetCommand
    ) -> ComputeSLOErrorBudgetResponse:
        raw = self._port.fetch_success_rate(command.service_name, command.rolling_window_days)
        raw_dict: dict[str, object] = dict(raw)
        result = self._engine.compute(
            slo_target=command.slo_target,
            rolling_window_days=command.rolling_window_days,
            raw_success_rate=None,
        )
        return ComputeSLOErrorBudgetResponse(result=result)  # type: ignore

    def xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_12(
        self, command: ComputeSLOErrorBudgetCommand
    ) -> ComputeSLOErrorBudgetResponse:
        raw = self._port.fetch_success_rate(command.service_name, command.rolling_window_days)
        raw_dict: dict[str, object] = dict(raw)
        result = self._engine.compute(
            rolling_window_days=command.rolling_window_days,
            raw_success_rate=raw_dict,
        )
        return ComputeSLOErrorBudgetResponse(result=result)  # type: ignore

    def xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_13(
        self, command: ComputeSLOErrorBudgetCommand
    ) -> ComputeSLOErrorBudgetResponse:
        raw = self._port.fetch_success_rate(command.service_name, command.rolling_window_days)
        raw_dict: dict[str, object] = dict(raw)
        result = self._engine.compute(
            slo_target=command.slo_target,
            raw_success_rate=raw_dict,
        )
        return ComputeSLOErrorBudgetResponse(result=result)  # type: ignore

    def xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_14(
        self, command: ComputeSLOErrorBudgetCommand
    ) -> ComputeSLOErrorBudgetResponse:
        raw = self._port.fetch_success_rate(command.service_name, command.rolling_window_days)
        raw_dict: dict[str, object] = dict(raw)
        result = self._engine.compute(
            slo_target=command.slo_target,
            rolling_window_days=command.rolling_window_days,
            )
        return ComputeSLOErrorBudgetResponse(result=result)  # type: ignore

    def xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_15(
        self, command: ComputeSLOErrorBudgetCommand
    ) -> ComputeSLOErrorBudgetResponse:
        raw = self._port.fetch_success_rate(command.service_name, command.rolling_window_days)
        raw_dict: dict[str, object] = dict(raw)
        result = self._engine.compute(
            slo_target=command.slo_target,
            rolling_window_days=command.rolling_window_days,
            raw_success_rate=raw_dict,
        )
        return ComputeSLOErrorBudgetResponse(result=None)  # type: ignore

mutants_xǁComputeSLOErrorBudgetUseCaseǁ__init____mutmut['_mutmut_orig'] = ComputeSLOErrorBudgetUseCase.xǁComputeSLOErrorBudgetUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁComputeSLOErrorBudgetUseCaseǁ__init____mutmut['xǁComputeSLOErrorBudgetUseCaseǁ__init____mutmut_1'] = ComputeSLOErrorBudgetUseCase.xǁComputeSLOErrorBudgetUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁComputeSLOErrorBudgetUseCaseǁ__init____mutmut['xǁComputeSLOErrorBudgetUseCaseǁ__init____mutmut_2'] = ComputeSLOErrorBudgetUseCase.xǁComputeSLOErrorBudgetUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut['_mutmut_orig'] = ComputeSLOErrorBudgetUseCase.xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_orig # type: ignore # mutmut generated
mutants_xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut['xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_1'] = ComputeSLOErrorBudgetUseCase.xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_1 # type: ignore # mutmut generated
mutants_xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut['xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_2'] = ComputeSLOErrorBudgetUseCase.xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_2 # type: ignore # mutmut generated
mutants_xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut['xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_3'] = ComputeSLOErrorBudgetUseCase.xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_3 # type: ignore # mutmut generated
mutants_xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut['xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_4'] = ComputeSLOErrorBudgetUseCase.xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_4 # type: ignore # mutmut generated
mutants_xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut['xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_5'] = ComputeSLOErrorBudgetUseCase.xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_5 # type: ignore # mutmut generated
mutants_xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut['xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_6'] = ComputeSLOErrorBudgetUseCase.xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_6 # type: ignore # mutmut generated
mutants_xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut['xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_7'] = ComputeSLOErrorBudgetUseCase.xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_7 # type: ignore # mutmut generated
mutants_xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut['xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_8'] = ComputeSLOErrorBudgetUseCase.xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_8 # type: ignore # mutmut generated
mutants_xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut['xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_9'] = ComputeSLOErrorBudgetUseCase.xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_9 # type: ignore # mutmut generated
mutants_xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut['xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_10'] = ComputeSLOErrorBudgetUseCase.xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_10 # type: ignore # mutmut generated
mutants_xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut['xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_11'] = ComputeSLOErrorBudgetUseCase.xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_11 # type: ignore # mutmut generated
mutants_xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut['xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_12'] = ComputeSLOErrorBudgetUseCase.xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_12 # type: ignore # mutmut generated
mutants_xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut['xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_13'] = ComputeSLOErrorBudgetUseCase.xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_13 # type: ignore # mutmut generated
mutants_xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut['xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_14'] = ComputeSLOErrorBudgetUseCase.xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_14 # type: ignore # mutmut generated
mutants_xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut['xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_15'] = ComputeSLOErrorBudgetUseCase.xǁComputeSLOErrorBudgetUseCaseǁcompute_slo_error_budget__mutmut_15 # type: ignore # mutmut generated
