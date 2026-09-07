from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.rollouts_port import RolloutsPort
from hexawyn.application.use_case.pipelines.analysis_runs_list.command import (
    AnalysisRunsListCommand,
)
from hexawyn.application.use_case.pipelines.analysis_runs_list.response import (
    AnalysisRunsListResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁAnalysisRunsListUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁAnalysisRunsListUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class AnalysisRunsListUseCase:
    @_mutmut_mutated(mutants_xǁAnalysisRunsListUseCaseǁ__init____mutmut)
    def __init__(self, rollouts_port: RolloutsPort) -> None:
        self._rollouts = rollouts_port
    def xǁAnalysisRunsListUseCaseǁ__init____mutmut_orig(self, rollouts_port: RolloutsPort) -> None:
        self._rollouts = rollouts_port
    def xǁAnalysisRunsListUseCaseǁ__init____mutmut_1(self, rollouts_port: RolloutsPort) -> None:
        self._rollouts = None

    @_mutmut_mutated(mutants_xǁAnalysisRunsListUseCaseǁexecute__mutmut)
    def execute(self, command: AnalysisRunsListCommand) -> AnalysisRunsListResponse:
        runs = self._rollouts.list_analysis_runs(
            namespace=command.namespace,
            rollout_name=command.rollout_name,
        )
        return AnalysisRunsListResponse(
            analysis_runs=[asdict(r) for r in runs],
        )

    def xǁAnalysisRunsListUseCaseǁexecute__mutmut_orig(self, command: AnalysisRunsListCommand) -> AnalysisRunsListResponse:
        runs = self._rollouts.list_analysis_runs(
            namespace=command.namespace,
            rollout_name=command.rollout_name,
        )
        return AnalysisRunsListResponse(
            analysis_runs=[asdict(r) for r in runs],
        )

    def xǁAnalysisRunsListUseCaseǁexecute__mutmut_1(self, command: AnalysisRunsListCommand) -> AnalysisRunsListResponse:
        runs = None
        return AnalysisRunsListResponse(
            analysis_runs=[asdict(r) for r in runs],
        )

    def xǁAnalysisRunsListUseCaseǁexecute__mutmut_2(self, command: AnalysisRunsListCommand) -> AnalysisRunsListResponse:
        runs = self._rollouts.list_analysis_runs(
            namespace=None,
            rollout_name=command.rollout_name,
        )
        return AnalysisRunsListResponse(
            analysis_runs=[asdict(r) for r in runs],
        )

    def xǁAnalysisRunsListUseCaseǁexecute__mutmut_3(self, command: AnalysisRunsListCommand) -> AnalysisRunsListResponse:
        runs = self._rollouts.list_analysis_runs(
            namespace=command.namespace,
            rollout_name=None,
        )
        return AnalysisRunsListResponse(
            analysis_runs=[asdict(r) for r in runs],
        )

    def xǁAnalysisRunsListUseCaseǁexecute__mutmut_4(self, command: AnalysisRunsListCommand) -> AnalysisRunsListResponse:
        runs = self._rollouts.list_analysis_runs(
            rollout_name=command.rollout_name,
        )
        return AnalysisRunsListResponse(
            analysis_runs=[asdict(r) for r in runs],
        )

    def xǁAnalysisRunsListUseCaseǁexecute__mutmut_5(self, command: AnalysisRunsListCommand) -> AnalysisRunsListResponse:
        runs = self._rollouts.list_analysis_runs(
            namespace=command.namespace,
            )
        return AnalysisRunsListResponse(
            analysis_runs=[asdict(r) for r in runs],
        )

    def xǁAnalysisRunsListUseCaseǁexecute__mutmut_6(self, command: AnalysisRunsListCommand) -> AnalysisRunsListResponse:
        runs = self._rollouts.list_analysis_runs(
            namespace=command.namespace,
            rollout_name=command.rollout_name,
        )
        return AnalysisRunsListResponse(
            analysis_runs=None,
        )

    def xǁAnalysisRunsListUseCaseǁexecute__mutmut_7(self, command: AnalysisRunsListCommand) -> AnalysisRunsListResponse:
        runs = self._rollouts.list_analysis_runs(
            namespace=command.namespace,
            rollout_name=command.rollout_name,
        )
        return AnalysisRunsListResponse(
            analysis_runs=[asdict(None) for r in runs],
        )

mutants_xǁAnalysisRunsListUseCaseǁ__init____mutmut['_mutmut_orig'] = AnalysisRunsListUseCase.xǁAnalysisRunsListUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁAnalysisRunsListUseCaseǁ__init____mutmut['xǁAnalysisRunsListUseCaseǁ__init____mutmut_1'] = AnalysisRunsListUseCase.xǁAnalysisRunsListUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁAnalysisRunsListUseCaseǁexecute__mutmut['_mutmut_orig'] = AnalysisRunsListUseCase.xǁAnalysisRunsListUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAnalysisRunsListUseCaseǁexecute__mutmut['xǁAnalysisRunsListUseCaseǁexecute__mutmut_1'] = AnalysisRunsListUseCase.xǁAnalysisRunsListUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAnalysisRunsListUseCaseǁexecute__mutmut['xǁAnalysisRunsListUseCaseǁexecute__mutmut_2'] = AnalysisRunsListUseCase.xǁAnalysisRunsListUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAnalysisRunsListUseCaseǁexecute__mutmut['xǁAnalysisRunsListUseCaseǁexecute__mutmut_3'] = AnalysisRunsListUseCase.xǁAnalysisRunsListUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAnalysisRunsListUseCaseǁexecute__mutmut['xǁAnalysisRunsListUseCaseǁexecute__mutmut_4'] = AnalysisRunsListUseCase.xǁAnalysisRunsListUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAnalysisRunsListUseCaseǁexecute__mutmut['xǁAnalysisRunsListUseCaseǁexecute__mutmut_5'] = AnalysisRunsListUseCase.xǁAnalysisRunsListUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAnalysisRunsListUseCaseǁexecute__mutmut['xǁAnalysisRunsListUseCaseǁexecute__mutmut_6'] = AnalysisRunsListUseCase.xǁAnalysisRunsListUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAnalysisRunsListUseCaseǁexecute__mutmut['xǁAnalysisRunsListUseCaseǁexecute__mutmut_7'] = AnalysisRunsListUseCase.xǁAnalysisRunsListUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
