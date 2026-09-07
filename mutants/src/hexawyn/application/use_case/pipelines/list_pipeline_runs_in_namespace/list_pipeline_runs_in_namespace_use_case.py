from hexawyn.application.ports.driven.tekton_port import TektonPort
from hexawyn.application.use_case.pipelines.list_pipeline_runs_in_namespace.command import (
    ListPipelineRunsInNamespaceCommand,
)
from hexawyn.application.use_case.pipelines.list_pipeline_runs_in_namespace.response import (
    ListPipelineRunsInNamespaceResponse,
)
from hexawyn.application.use_case.pipelines.list_pipeline_runs_in_namespace.sort_stuck import (
    find_stuck_runs,
    sort_by_status_then_time,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁListPipelineRunsInNamespaceUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut: MutantDict = {}  # type: ignore


class ListPipelineRunsInNamespaceUseCase:
    """Fetches all PipelineRuns in a namespace, sorts (Failed first), detects stuck runs."""

    @_mutmut_mutated(mutants_xǁListPipelineRunsInNamespaceUseCaseǁ__init____mutmut)
    def __init__(self, tekton_port: TektonPort) -> None:
        self._tekton = tekton_port

    def xǁListPipelineRunsInNamespaceUseCaseǁ__init____mutmut_orig(self, tekton_port: TektonPort) -> None:
        self._tekton = tekton_port

    def xǁListPipelineRunsInNamespaceUseCaseǁ__init____mutmut_1(self, tekton_port: TektonPort) -> None:
        self._tekton = None

    @_mutmut_mutated(mutants_xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut)
    def list_pipeline_runs_in_namespace(
        self, command: ListPipelineRunsInNamespaceCommand
    ) -> ListPipelineRunsInNamespaceResponse:
        all_runs = self._tekton.list_pipeline_runs_in_namespace(
            namespace=command.namespace,
            limit=command.limit,
        )
        runs = sort_by_status_then_time(all_runs)[: command.limit]
        stuck_runs = find_stuck_runs(runs)
        note = f"No PipelineRuns found in namespace '{command.namespace}'." if not runs else None
        return ListPipelineRunsInNamespaceResponse(
            runs=runs,
            stuck_runs=stuck_runs,
            note=note,
        )

    def xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_orig(
        self, command: ListPipelineRunsInNamespaceCommand
    ) -> ListPipelineRunsInNamespaceResponse:
        all_runs = self._tekton.list_pipeline_runs_in_namespace(
            namespace=command.namespace,
            limit=command.limit,
        )
        runs = sort_by_status_then_time(all_runs)[: command.limit]
        stuck_runs = find_stuck_runs(runs)
        note = f"No PipelineRuns found in namespace '{command.namespace}'." if not runs else None
        return ListPipelineRunsInNamespaceResponse(
            runs=runs,
            stuck_runs=stuck_runs,
            note=note,
        )

    def xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_1(
        self, command: ListPipelineRunsInNamespaceCommand
    ) -> ListPipelineRunsInNamespaceResponse:
        all_runs = None
        runs = sort_by_status_then_time(all_runs)[: command.limit]
        stuck_runs = find_stuck_runs(runs)
        note = f"No PipelineRuns found in namespace '{command.namespace}'." if not runs else None
        return ListPipelineRunsInNamespaceResponse(
            runs=runs,
            stuck_runs=stuck_runs,
            note=note,
        )

    def xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_2(
        self, command: ListPipelineRunsInNamespaceCommand
    ) -> ListPipelineRunsInNamespaceResponse:
        all_runs = self._tekton.list_pipeline_runs_in_namespace(
            namespace=None,
            limit=command.limit,
        )
        runs = sort_by_status_then_time(all_runs)[: command.limit]
        stuck_runs = find_stuck_runs(runs)
        note = f"No PipelineRuns found in namespace '{command.namespace}'." if not runs else None
        return ListPipelineRunsInNamespaceResponse(
            runs=runs,
            stuck_runs=stuck_runs,
            note=note,
        )

    def xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_3(
        self, command: ListPipelineRunsInNamespaceCommand
    ) -> ListPipelineRunsInNamespaceResponse:
        all_runs = self._tekton.list_pipeline_runs_in_namespace(
            namespace=command.namespace,
            limit=None,
        )
        runs = sort_by_status_then_time(all_runs)[: command.limit]
        stuck_runs = find_stuck_runs(runs)
        note = f"No PipelineRuns found in namespace '{command.namespace}'." if not runs else None
        return ListPipelineRunsInNamespaceResponse(
            runs=runs,
            stuck_runs=stuck_runs,
            note=note,
        )

    def xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_4(
        self, command: ListPipelineRunsInNamespaceCommand
    ) -> ListPipelineRunsInNamespaceResponse:
        all_runs = self._tekton.list_pipeline_runs_in_namespace(
            limit=command.limit,
        )
        runs = sort_by_status_then_time(all_runs)[: command.limit]
        stuck_runs = find_stuck_runs(runs)
        note = f"No PipelineRuns found in namespace '{command.namespace}'." if not runs else None
        return ListPipelineRunsInNamespaceResponse(
            runs=runs,
            stuck_runs=stuck_runs,
            note=note,
        )

    def xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_5(
        self, command: ListPipelineRunsInNamespaceCommand
    ) -> ListPipelineRunsInNamespaceResponse:
        all_runs = self._tekton.list_pipeline_runs_in_namespace(
            namespace=command.namespace,
            )
        runs = sort_by_status_then_time(all_runs)[: command.limit]
        stuck_runs = find_stuck_runs(runs)
        note = f"No PipelineRuns found in namespace '{command.namespace}'." if not runs else None
        return ListPipelineRunsInNamespaceResponse(
            runs=runs,
            stuck_runs=stuck_runs,
            note=note,
        )

    def xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_6(
        self, command: ListPipelineRunsInNamespaceCommand
    ) -> ListPipelineRunsInNamespaceResponse:
        all_runs = self._tekton.list_pipeline_runs_in_namespace(
            namespace=command.namespace,
            limit=command.limit,
        )
        runs = None
        stuck_runs = find_stuck_runs(runs)
        note = f"No PipelineRuns found in namespace '{command.namespace}'." if not runs else None
        return ListPipelineRunsInNamespaceResponse(
            runs=runs,
            stuck_runs=stuck_runs,
            note=note,
        )

    def xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_7(
        self, command: ListPipelineRunsInNamespaceCommand
    ) -> ListPipelineRunsInNamespaceResponse:
        all_runs = self._tekton.list_pipeline_runs_in_namespace(
            namespace=command.namespace,
            limit=command.limit,
        )
        runs = sort_by_status_then_time(None)[: command.limit]
        stuck_runs = find_stuck_runs(runs)
        note = f"No PipelineRuns found in namespace '{command.namespace}'." if not runs else None
        return ListPipelineRunsInNamespaceResponse(
            runs=runs,
            stuck_runs=stuck_runs,
            note=note,
        )

    def xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_8(
        self, command: ListPipelineRunsInNamespaceCommand
    ) -> ListPipelineRunsInNamespaceResponse:
        all_runs = self._tekton.list_pipeline_runs_in_namespace(
            namespace=command.namespace,
            limit=command.limit,
        )
        runs = sort_by_status_then_time(all_runs)[: command.limit]
        stuck_runs = None
        note = f"No PipelineRuns found in namespace '{command.namespace}'." if not runs else None
        return ListPipelineRunsInNamespaceResponse(
            runs=runs,
            stuck_runs=stuck_runs,
            note=note,
        )

    def xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_9(
        self, command: ListPipelineRunsInNamespaceCommand
    ) -> ListPipelineRunsInNamespaceResponse:
        all_runs = self._tekton.list_pipeline_runs_in_namespace(
            namespace=command.namespace,
            limit=command.limit,
        )
        runs = sort_by_status_then_time(all_runs)[: command.limit]
        stuck_runs = find_stuck_runs(None)
        note = f"No PipelineRuns found in namespace '{command.namespace}'." if not runs else None
        return ListPipelineRunsInNamespaceResponse(
            runs=runs,
            stuck_runs=stuck_runs,
            note=note,
        )

    def xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_10(
        self, command: ListPipelineRunsInNamespaceCommand
    ) -> ListPipelineRunsInNamespaceResponse:
        all_runs = self._tekton.list_pipeline_runs_in_namespace(
            namespace=command.namespace,
            limit=command.limit,
        )
        runs = sort_by_status_then_time(all_runs)[: command.limit]
        stuck_runs = find_stuck_runs(runs)
        note = None
        return ListPipelineRunsInNamespaceResponse(
            runs=runs,
            stuck_runs=stuck_runs,
            note=note,
        )

    def xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_11(
        self, command: ListPipelineRunsInNamespaceCommand
    ) -> ListPipelineRunsInNamespaceResponse:
        all_runs = self._tekton.list_pipeline_runs_in_namespace(
            namespace=command.namespace,
            limit=command.limit,
        )
        runs = sort_by_status_then_time(all_runs)[: command.limit]
        stuck_runs = find_stuck_runs(runs)
        note = f"No PipelineRuns found in namespace '{command.namespace}'." if runs else None
        return ListPipelineRunsInNamespaceResponse(
            runs=runs,
            stuck_runs=stuck_runs,
            note=note,
        )

    def xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_12(
        self, command: ListPipelineRunsInNamespaceCommand
    ) -> ListPipelineRunsInNamespaceResponse:
        all_runs = self._tekton.list_pipeline_runs_in_namespace(
            namespace=command.namespace,
            limit=command.limit,
        )
        runs = sort_by_status_then_time(all_runs)[: command.limit]
        stuck_runs = find_stuck_runs(runs)
        note = f"No PipelineRuns found in namespace '{command.namespace}'." if not runs else None
        return ListPipelineRunsInNamespaceResponse(
            runs=None,
            stuck_runs=stuck_runs,
            note=note,
        )

    def xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_13(
        self, command: ListPipelineRunsInNamespaceCommand
    ) -> ListPipelineRunsInNamespaceResponse:
        all_runs = self._tekton.list_pipeline_runs_in_namespace(
            namespace=command.namespace,
            limit=command.limit,
        )
        runs = sort_by_status_then_time(all_runs)[: command.limit]
        stuck_runs = find_stuck_runs(runs)
        note = f"No PipelineRuns found in namespace '{command.namespace}'." if not runs else None
        return ListPipelineRunsInNamespaceResponse(
            runs=runs,
            stuck_runs=None,
            note=note,
        )

    def xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_14(
        self, command: ListPipelineRunsInNamespaceCommand
    ) -> ListPipelineRunsInNamespaceResponse:
        all_runs = self._tekton.list_pipeline_runs_in_namespace(
            namespace=command.namespace,
            limit=command.limit,
        )
        runs = sort_by_status_then_time(all_runs)[: command.limit]
        stuck_runs = find_stuck_runs(runs)
        note = f"No PipelineRuns found in namespace '{command.namespace}'." if not runs else None
        return ListPipelineRunsInNamespaceResponse(
            runs=runs,
            stuck_runs=stuck_runs,
            note=None,
        )

    def xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_15(
        self, command: ListPipelineRunsInNamespaceCommand
    ) -> ListPipelineRunsInNamespaceResponse:
        all_runs = self._tekton.list_pipeline_runs_in_namespace(
            namespace=command.namespace,
            limit=command.limit,
        )
        runs = sort_by_status_then_time(all_runs)[: command.limit]
        stuck_runs = find_stuck_runs(runs)
        note = f"No PipelineRuns found in namespace '{command.namespace}'." if not runs else None
        return ListPipelineRunsInNamespaceResponse(
            stuck_runs=stuck_runs,
            note=note,
        )

    def xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_16(
        self, command: ListPipelineRunsInNamespaceCommand
    ) -> ListPipelineRunsInNamespaceResponse:
        all_runs = self._tekton.list_pipeline_runs_in_namespace(
            namespace=command.namespace,
            limit=command.limit,
        )
        runs = sort_by_status_then_time(all_runs)[: command.limit]
        stuck_runs = find_stuck_runs(runs)
        note = f"No PipelineRuns found in namespace '{command.namespace}'." if not runs else None
        return ListPipelineRunsInNamespaceResponse(
            runs=runs,
            note=note,
        )

    def xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_17(
        self, command: ListPipelineRunsInNamespaceCommand
    ) -> ListPipelineRunsInNamespaceResponse:
        all_runs = self._tekton.list_pipeline_runs_in_namespace(
            namespace=command.namespace,
            limit=command.limit,
        )
        runs = sort_by_status_then_time(all_runs)[: command.limit]
        stuck_runs = find_stuck_runs(runs)
        note = f"No PipelineRuns found in namespace '{command.namespace}'." if not runs else None
        return ListPipelineRunsInNamespaceResponse(
            runs=runs,
            stuck_runs=stuck_runs,
            )

mutants_xǁListPipelineRunsInNamespaceUseCaseǁ__init____mutmut['_mutmut_orig'] = ListPipelineRunsInNamespaceUseCase.xǁListPipelineRunsInNamespaceUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁListPipelineRunsInNamespaceUseCaseǁ__init____mutmut['xǁListPipelineRunsInNamespaceUseCaseǁ__init____mutmut_1'] = ListPipelineRunsInNamespaceUseCase.xǁListPipelineRunsInNamespaceUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut['_mutmut_orig'] = ListPipelineRunsInNamespaceUseCase.xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_orig # type: ignore # mutmut generated
mutants_xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut['xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_1'] = ListPipelineRunsInNamespaceUseCase.xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_1 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut['xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_2'] = ListPipelineRunsInNamespaceUseCase.xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_2 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut['xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_3'] = ListPipelineRunsInNamespaceUseCase.xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_3 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut['xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_4'] = ListPipelineRunsInNamespaceUseCase.xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_4 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut['xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_5'] = ListPipelineRunsInNamespaceUseCase.xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_5 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut['xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_6'] = ListPipelineRunsInNamespaceUseCase.xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_6 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut['xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_7'] = ListPipelineRunsInNamespaceUseCase.xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_7 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut['xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_8'] = ListPipelineRunsInNamespaceUseCase.xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_8 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut['xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_9'] = ListPipelineRunsInNamespaceUseCase.xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_9 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut['xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_10'] = ListPipelineRunsInNamespaceUseCase.xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_10 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut['xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_11'] = ListPipelineRunsInNamespaceUseCase.xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_11 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut['xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_12'] = ListPipelineRunsInNamespaceUseCase.xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_12 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut['xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_13'] = ListPipelineRunsInNamespaceUseCase.xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_13 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut['xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_14'] = ListPipelineRunsInNamespaceUseCase.xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_14 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut['xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_15'] = ListPipelineRunsInNamespaceUseCase.xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_15 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut['xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_16'] = ListPipelineRunsInNamespaceUseCase.xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_16 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut['xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_17'] = ListPipelineRunsInNamespaceUseCase.xǁListPipelineRunsInNamespaceUseCaseǁlist_pipeline_runs_in_namespace__mutmut_17 # type: ignore # mutmut generated
