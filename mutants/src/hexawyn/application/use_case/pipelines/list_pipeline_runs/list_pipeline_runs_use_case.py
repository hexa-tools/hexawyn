from hexawyn.application.ports.driven.tekton_port import TektonPort
from hexawyn.application.use_case.pipelines.list_pipeline_runs.command import (
    ListPipelineRunsCommand,
)
from hexawyn.application.use_case.pipelines.list_pipeline_runs.response import (
    ListPipelineRunsResponse,
)
from hexawyn.application.use_case.pipelines.list_pipeline_runs.sort_stats import (
    compute_stats,
    find_outliers,
    start_time_sort_key,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁListPipelineRunsUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁListPipelineRunsUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class ListPipelineRunsUseCase:
    """Fetches PipelineRuns, sorts, limits, computes stats and flags outliers."""

    @_mutmut_mutated(mutants_xǁListPipelineRunsUseCaseǁ__init____mutmut)
    def __init__(self, tekton_port: TektonPort) -> None:
        self._tekton = tekton_port

    def xǁListPipelineRunsUseCaseǁ__init____mutmut_orig(self, tekton_port: TektonPort) -> None:
        self._tekton = tekton_port

    def xǁListPipelineRunsUseCaseǁ__init____mutmut_1(self, tekton_port: TektonPort) -> None:
        self._tekton = None

    @_mutmut_mutated(mutants_xǁListPipelineRunsUseCaseǁexecute__mutmut)
    def execute(self, command: ListPipelineRunsCommand) -> ListPipelineRunsResponse:
        all_runs = self._tekton.list_pipeline_runs(
            service_name=command.service_name,
            namespace=command.namespace,  # type: ignore
        )
        sorted_runs = sorted(all_runs, key=start_time_sort_key, reverse=True)
        runs = sorted_runs[: command.limit]
        stats = compute_stats(runs)
        outliers = find_outliers(runs, stats.average_duration_seconds)
        note = f"Only {len(runs)} run(s) available." if len(runs) < command.limit else None
        return ListPipelineRunsResponse(
            runs=runs,
            stats=stats,
            outliers=outliers,
            note=note,
        )

    def xǁListPipelineRunsUseCaseǁexecute__mutmut_orig(self, command: ListPipelineRunsCommand) -> ListPipelineRunsResponse:
        all_runs = self._tekton.list_pipeline_runs(
            service_name=command.service_name,
            namespace=command.namespace,  # type: ignore
        )
        sorted_runs = sorted(all_runs, key=start_time_sort_key, reverse=True)
        runs = sorted_runs[: command.limit]
        stats = compute_stats(runs)
        outliers = find_outliers(runs, stats.average_duration_seconds)
        note = f"Only {len(runs)} run(s) available." if len(runs) < command.limit else None
        return ListPipelineRunsResponse(
            runs=runs,
            stats=stats,
            outliers=outliers,
            note=note,
        )

    def xǁListPipelineRunsUseCaseǁexecute__mutmut_1(self, command: ListPipelineRunsCommand) -> ListPipelineRunsResponse:
        all_runs = None
        sorted_runs = sorted(all_runs, key=start_time_sort_key, reverse=True)
        runs = sorted_runs[: command.limit]
        stats = compute_stats(runs)
        outliers = find_outliers(runs, stats.average_duration_seconds)
        note = f"Only {len(runs)} run(s) available." if len(runs) < command.limit else None
        return ListPipelineRunsResponse(
            runs=runs,
            stats=stats,
            outliers=outliers,
            note=note,
        )

    def xǁListPipelineRunsUseCaseǁexecute__mutmut_2(self, command: ListPipelineRunsCommand) -> ListPipelineRunsResponse:
        all_runs = self._tekton.list_pipeline_runs(
            service_name=None,
            namespace=command.namespace,  # type: ignore
        )
        sorted_runs = sorted(all_runs, key=start_time_sort_key, reverse=True)
        runs = sorted_runs[: command.limit]
        stats = compute_stats(runs)
        outliers = find_outliers(runs, stats.average_duration_seconds)
        note = f"Only {len(runs)} run(s) available." if len(runs) < command.limit else None
        return ListPipelineRunsResponse(
            runs=runs,
            stats=stats,
            outliers=outliers,
            note=note,
        )

    def xǁListPipelineRunsUseCaseǁexecute__mutmut_3(self, command: ListPipelineRunsCommand) -> ListPipelineRunsResponse:
        all_runs = self._tekton.list_pipeline_runs(
            service_name=command.service_name,
            namespace=None,  # type: ignore
        )
        sorted_runs = sorted(all_runs, key=start_time_sort_key, reverse=True)
        runs = sorted_runs[: command.limit]
        stats = compute_stats(runs)
        outliers = find_outliers(runs, stats.average_duration_seconds)
        note = f"Only {len(runs)} run(s) available." if len(runs) < command.limit else None
        return ListPipelineRunsResponse(
            runs=runs,
            stats=stats,
            outliers=outliers,
            note=note,
        )

    def xǁListPipelineRunsUseCaseǁexecute__mutmut_4(self, command: ListPipelineRunsCommand) -> ListPipelineRunsResponse:
        all_runs = self._tekton.list_pipeline_runs(
            namespace=command.namespace,  # type: ignore
        )
        sorted_runs = sorted(all_runs, key=start_time_sort_key, reverse=True)
        runs = sorted_runs[: command.limit]
        stats = compute_stats(runs)
        outliers = find_outliers(runs, stats.average_duration_seconds)
        note = f"Only {len(runs)} run(s) available." if len(runs) < command.limit else None
        return ListPipelineRunsResponse(
            runs=runs,
            stats=stats,
            outliers=outliers,
            note=note,
        )

    def xǁListPipelineRunsUseCaseǁexecute__mutmut_5(self, command: ListPipelineRunsCommand) -> ListPipelineRunsResponse:
        all_runs = self._tekton.list_pipeline_runs(
            service_name=command.service_name,
            )
        sorted_runs = sorted(all_runs, key=start_time_sort_key, reverse=True)
        runs = sorted_runs[: command.limit]
        stats = compute_stats(runs)
        outliers = find_outliers(runs, stats.average_duration_seconds)
        note = f"Only {len(runs)} run(s) available." if len(runs) < command.limit else None
        return ListPipelineRunsResponse(
            runs=runs,
            stats=stats,
            outliers=outliers,
            note=note,
        )

    def xǁListPipelineRunsUseCaseǁexecute__mutmut_6(self, command: ListPipelineRunsCommand) -> ListPipelineRunsResponse:
        all_runs = self._tekton.list_pipeline_runs(
            service_name=command.service_name,
            namespace=command.namespace,  # type: ignore
        )
        sorted_runs = None
        runs = sorted_runs[: command.limit]
        stats = compute_stats(runs)
        outliers = find_outliers(runs, stats.average_duration_seconds)
        note = f"Only {len(runs)} run(s) available." if len(runs) < command.limit else None
        return ListPipelineRunsResponse(
            runs=runs,
            stats=stats,
            outliers=outliers,
            note=note,
        )

    def xǁListPipelineRunsUseCaseǁexecute__mutmut_7(self, command: ListPipelineRunsCommand) -> ListPipelineRunsResponse:
        all_runs = self._tekton.list_pipeline_runs(
            service_name=command.service_name,
            namespace=command.namespace,  # type: ignore
        )
        sorted_runs = sorted(None, key=start_time_sort_key, reverse=True)
        runs = sorted_runs[: command.limit]
        stats = compute_stats(runs)
        outliers = find_outliers(runs, stats.average_duration_seconds)
        note = f"Only {len(runs)} run(s) available." if len(runs) < command.limit else None
        return ListPipelineRunsResponse(
            runs=runs,
            stats=stats,
            outliers=outliers,
            note=note,
        )

    def xǁListPipelineRunsUseCaseǁexecute__mutmut_8(self, command: ListPipelineRunsCommand) -> ListPipelineRunsResponse:
        all_runs = self._tekton.list_pipeline_runs(
            service_name=command.service_name,
            namespace=command.namespace,  # type: ignore
        )
        sorted_runs = sorted(all_runs, key=None, reverse=True)
        runs = sorted_runs[: command.limit]
        stats = compute_stats(runs)
        outliers = find_outliers(runs, stats.average_duration_seconds)
        note = f"Only {len(runs)} run(s) available." if len(runs) < command.limit else None
        return ListPipelineRunsResponse(
            runs=runs,
            stats=stats,
            outliers=outliers,
            note=note,
        )

    def xǁListPipelineRunsUseCaseǁexecute__mutmut_9(self, command: ListPipelineRunsCommand) -> ListPipelineRunsResponse:
        all_runs = self._tekton.list_pipeline_runs(
            service_name=command.service_name,
            namespace=command.namespace,  # type: ignore
        )
        sorted_runs = sorted(all_runs, key=start_time_sort_key, reverse=None)
        runs = sorted_runs[: command.limit]
        stats = compute_stats(runs)
        outliers = find_outliers(runs, stats.average_duration_seconds)
        note = f"Only {len(runs)} run(s) available." if len(runs) < command.limit else None
        return ListPipelineRunsResponse(
            runs=runs,
            stats=stats,
            outliers=outliers,
            note=note,
        )

    def xǁListPipelineRunsUseCaseǁexecute__mutmut_10(self, command: ListPipelineRunsCommand) -> ListPipelineRunsResponse:
        all_runs = self._tekton.list_pipeline_runs(
            service_name=command.service_name,
            namespace=command.namespace,  # type: ignore
        )
        sorted_runs = sorted(key=start_time_sort_key, reverse=True)
        runs = sorted_runs[: command.limit]
        stats = compute_stats(runs)
        outliers = find_outliers(runs, stats.average_duration_seconds)
        note = f"Only {len(runs)} run(s) available." if len(runs) < command.limit else None
        return ListPipelineRunsResponse(
            runs=runs,
            stats=stats,
            outliers=outliers,
            note=note,
        )

    def xǁListPipelineRunsUseCaseǁexecute__mutmut_11(self, command: ListPipelineRunsCommand) -> ListPipelineRunsResponse:
        all_runs = self._tekton.list_pipeline_runs(
            service_name=command.service_name,
            namespace=command.namespace,  # type: ignore
        )
        sorted_runs = sorted(all_runs, reverse=True)
        runs = sorted_runs[: command.limit]
        stats = compute_stats(runs)
        outliers = find_outliers(runs, stats.average_duration_seconds)
        note = f"Only {len(runs)} run(s) available." if len(runs) < command.limit else None
        return ListPipelineRunsResponse(
            runs=runs,
            stats=stats,
            outliers=outliers,
            note=note,
        )

    def xǁListPipelineRunsUseCaseǁexecute__mutmut_12(self, command: ListPipelineRunsCommand) -> ListPipelineRunsResponse:
        all_runs = self._tekton.list_pipeline_runs(
            service_name=command.service_name,
            namespace=command.namespace,  # type: ignore
        )
        sorted_runs = sorted(all_runs, key=start_time_sort_key, )
        runs = sorted_runs[: command.limit]
        stats = compute_stats(runs)
        outliers = find_outliers(runs, stats.average_duration_seconds)
        note = f"Only {len(runs)} run(s) available." if len(runs) < command.limit else None
        return ListPipelineRunsResponse(
            runs=runs,
            stats=stats,
            outliers=outliers,
            note=note,
        )

    def xǁListPipelineRunsUseCaseǁexecute__mutmut_13(self, command: ListPipelineRunsCommand) -> ListPipelineRunsResponse:
        all_runs = self._tekton.list_pipeline_runs(
            service_name=command.service_name,
            namespace=command.namespace,  # type: ignore
        )
        sorted_runs = sorted(all_runs, key=start_time_sort_key, reverse=False)
        runs = sorted_runs[: command.limit]
        stats = compute_stats(runs)
        outliers = find_outliers(runs, stats.average_duration_seconds)
        note = f"Only {len(runs)} run(s) available." if len(runs) < command.limit else None
        return ListPipelineRunsResponse(
            runs=runs,
            stats=stats,
            outliers=outliers,
            note=note,
        )

    def xǁListPipelineRunsUseCaseǁexecute__mutmut_14(self, command: ListPipelineRunsCommand) -> ListPipelineRunsResponse:
        all_runs = self._tekton.list_pipeline_runs(
            service_name=command.service_name,
            namespace=command.namespace,  # type: ignore
        )
        sorted_runs = sorted(all_runs, key=start_time_sort_key, reverse=True)
        runs = None
        stats = compute_stats(runs)
        outliers = find_outliers(runs, stats.average_duration_seconds)
        note = f"Only {len(runs)} run(s) available." if len(runs) < command.limit else None
        return ListPipelineRunsResponse(
            runs=runs,
            stats=stats,
            outliers=outliers,
            note=note,
        )

    def xǁListPipelineRunsUseCaseǁexecute__mutmut_15(self, command: ListPipelineRunsCommand) -> ListPipelineRunsResponse:
        all_runs = self._tekton.list_pipeline_runs(
            service_name=command.service_name,
            namespace=command.namespace,  # type: ignore
        )
        sorted_runs = sorted(all_runs, key=start_time_sort_key, reverse=True)
        runs = sorted_runs[: command.limit]
        stats = None
        outliers = find_outliers(runs, stats.average_duration_seconds)
        note = f"Only {len(runs)} run(s) available." if len(runs) < command.limit else None
        return ListPipelineRunsResponse(
            runs=runs,
            stats=stats,
            outliers=outliers,
            note=note,
        )

    def xǁListPipelineRunsUseCaseǁexecute__mutmut_16(self, command: ListPipelineRunsCommand) -> ListPipelineRunsResponse:
        all_runs = self._tekton.list_pipeline_runs(
            service_name=command.service_name,
            namespace=command.namespace,  # type: ignore
        )
        sorted_runs = sorted(all_runs, key=start_time_sort_key, reverse=True)
        runs = sorted_runs[: command.limit]
        stats = compute_stats(None)
        outliers = find_outliers(runs, stats.average_duration_seconds)
        note = f"Only {len(runs)} run(s) available." if len(runs) < command.limit else None
        return ListPipelineRunsResponse(
            runs=runs,
            stats=stats,
            outliers=outliers,
            note=note,
        )

    def xǁListPipelineRunsUseCaseǁexecute__mutmut_17(self, command: ListPipelineRunsCommand) -> ListPipelineRunsResponse:
        all_runs = self._tekton.list_pipeline_runs(
            service_name=command.service_name,
            namespace=command.namespace,  # type: ignore
        )
        sorted_runs = sorted(all_runs, key=start_time_sort_key, reverse=True)
        runs = sorted_runs[: command.limit]
        stats = compute_stats(runs)
        outliers = None
        note = f"Only {len(runs)} run(s) available." if len(runs) < command.limit else None
        return ListPipelineRunsResponse(
            runs=runs,
            stats=stats,
            outliers=outliers,
            note=note,
        )

    def xǁListPipelineRunsUseCaseǁexecute__mutmut_18(self, command: ListPipelineRunsCommand) -> ListPipelineRunsResponse:
        all_runs = self._tekton.list_pipeline_runs(
            service_name=command.service_name,
            namespace=command.namespace,  # type: ignore
        )
        sorted_runs = sorted(all_runs, key=start_time_sort_key, reverse=True)
        runs = sorted_runs[: command.limit]
        stats = compute_stats(runs)
        outliers = find_outliers(None, stats.average_duration_seconds)
        note = f"Only {len(runs)} run(s) available." if len(runs) < command.limit else None
        return ListPipelineRunsResponse(
            runs=runs,
            stats=stats,
            outliers=outliers,
            note=note,
        )

    def xǁListPipelineRunsUseCaseǁexecute__mutmut_19(self, command: ListPipelineRunsCommand) -> ListPipelineRunsResponse:
        all_runs = self._tekton.list_pipeline_runs(
            service_name=command.service_name,
            namespace=command.namespace,  # type: ignore
        )
        sorted_runs = sorted(all_runs, key=start_time_sort_key, reverse=True)
        runs = sorted_runs[: command.limit]
        stats = compute_stats(runs)
        outliers = find_outliers(runs, None)
        note = f"Only {len(runs)} run(s) available." if len(runs) < command.limit else None
        return ListPipelineRunsResponse(
            runs=runs,
            stats=stats,
            outliers=outliers,
            note=note,
        )

    def xǁListPipelineRunsUseCaseǁexecute__mutmut_20(self, command: ListPipelineRunsCommand) -> ListPipelineRunsResponse:
        all_runs = self._tekton.list_pipeline_runs(
            service_name=command.service_name,
            namespace=command.namespace,  # type: ignore
        )
        sorted_runs = sorted(all_runs, key=start_time_sort_key, reverse=True)
        runs = sorted_runs[: command.limit]
        stats = compute_stats(runs)
        outliers = find_outliers(stats.average_duration_seconds)
        note = f"Only {len(runs)} run(s) available." if len(runs) < command.limit else None
        return ListPipelineRunsResponse(
            runs=runs,
            stats=stats,
            outliers=outliers,
            note=note,
        )

    def xǁListPipelineRunsUseCaseǁexecute__mutmut_21(self, command: ListPipelineRunsCommand) -> ListPipelineRunsResponse:
        all_runs = self._tekton.list_pipeline_runs(
            service_name=command.service_name,
            namespace=command.namespace,  # type: ignore
        )
        sorted_runs = sorted(all_runs, key=start_time_sort_key, reverse=True)
        runs = sorted_runs[: command.limit]
        stats = compute_stats(runs)
        outliers = find_outliers(runs, )
        note = f"Only {len(runs)} run(s) available." if len(runs) < command.limit else None
        return ListPipelineRunsResponse(
            runs=runs,
            stats=stats,
            outliers=outliers,
            note=note,
        )

    def xǁListPipelineRunsUseCaseǁexecute__mutmut_22(self, command: ListPipelineRunsCommand) -> ListPipelineRunsResponse:
        all_runs = self._tekton.list_pipeline_runs(
            service_name=command.service_name,
            namespace=command.namespace,  # type: ignore
        )
        sorted_runs = sorted(all_runs, key=start_time_sort_key, reverse=True)
        runs = sorted_runs[: command.limit]
        stats = compute_stats(runs)
        outliers = find_outliers(runs, stats.average_duration_seconds)
        note = None
        return ListPipelineRunsResponse(
            runs=runs,
            stats=stats,
            outliers=outliers,
            note=note,
        )

    def xǁListPipelineRunsUseCaseǁexecute__mutmut_23(self, command: ListPipelineRunsCommand) -> ListPipelineRunsResponse:
        all_runs = self._tekton.list_pipeline_runs(
            service_name=command.service_name,
            namespace=command.namespace,  # type: ignore
        )
        sorted_runs = sorted(all_runs, key=start_time_sort_key, reverse=True)
        runs = sorted_runs[: command.limit]
        stats = compute_stats(runs)
        outliers = find_outliers(runs, stats.average_duration_seconds)
        note = f"Only {len(runs)} run(s) available." if len(runs) <= command.limit else None
        return ListPipelineRunsResponse(
            runs=runs,
            stats=stats,
            outliers=outliers,
            note=note,
        )

    def xǁListPipelineRunsUseCaseǁexecute__mutmut_24(self, command: ListPipelineRunsCommand) -> ListPipelineRunsResponse:
        all_runs = self._tekton.list_pipeline_runs(
            service_name=command.service_name,
            namespace=command.namespace,  # type: ignore
        )
        sorted_runs = sorted(all_runs, key=start_time_sort_key, reverse=True)
        runs = sorted_runs[: command.limit]
        stats = compute_stats(runs)
        outliers = find_outliers(runs, stats.average_duration_seconds)
        note = f"Only {len(runs)} run(s) available." if len(runs) < command.limit else None
        return ListPipelineRunsResponse(
            runs=None,
            stats=stats,
            outliers=outliers,
            note=note,
        )

    def xǁListPipelineRunsUseCaseǁexecute__mutmut_25(self, command: ListPipelineRunsCommand) -> ListPipelineRunsResponse:
        all_runs = self._tekton.list_pipeline_runs(
            service_name=command.service_name,
            namespace=command.namespace,  # type: ignore
        )
        sorted_runs = sorted(all_runs, key=start_time_sort_key, reverse=True)
        runs = sorted_runs[: command.limit]
        stats = compute_stats(runs)
        outliers = find_outliers(runs, stats.average_duration_seconds)
        note = f"Only {len(runs)} run(s) available." if len(runs) < command.limit else None
        return ListPipelineRunsResponse(
            runs=runs,
            stats=None,
            outliers=outliers,
            note=note,
        )

    def xǁListPipelineRunsUseCaseǁexecute__mutmut_26(self, command: ListPipelineRunsCommand) -> ListPipelineRunsResponse:
        all_runs = self._tekton.list_pipeline_runs(
            service_name=command.service_name,
            namespace=command.namespace,  # type: ignore
        )
        sorted_runs = sorted(all_runs, key=start_time_sort_key, reverse=True)
        runs = sorted_runs[: command.limit]
        stats = compute_stats(runs)
        outliers = find_outliers(runs, stats.average_duration_seconds)
        note = f"Only {len(runs)} run(s) available." if len(runs) < command.limit else None
        return ListPipelineRunsResponse(
            runs=runs,
            stats=stats,
            outliers=None,
            note=note,
        )

    def xǁListPipelineRunsUseCaseǁexecute__mutmut_27(self, command: ListPipelineRunsCommand) -> ListPipelineRunsResponse:
        all_runs = self._tekton.list_pipeline_runs(
            service_name=command.service_name,
            namespace=command.namespace,  # type: ignore
        )
        sorted_runs = sorted(all_runs, key=start_time_sort_key, reverse=True)
        runs = sorted_runs[: command.limit]
        stats = compute_stats(runs)
        outliers = find_outliers(runs, stats.average_duration_seconds)
        note = f"Only {len(runs)} run(s) available." if len(runs) < command.limit else None
        return ListPipelineRunsResponse(
            runs=runs,
            stats=stats,
            outliers=outliers,
            note=None,
        )

    def xǁListPipelineRunsUseCaseǁexecute__mutmut_28(self, command: ListPipelineRunsCommand) -> ListPipelineRunsResponse:
        all_runs = self._tekton.list_pipeline_runs(
            service_name=command.service_name,
            namespace=command.namespace,  # type: ignore
        )
        sorted_runs = sorted(all_runs, key=start_time_sort_key, reverse=True)
        runs = sorted_runs[: command.limit]
        stats = compute_stats(runs)
        outliers = find_outliers(runs, stats.average_duration_seconds)
        note = f"Only {len(runs)} run(s) available." if len(runs) < command.limit else None
        return ListPipelineRunsResponse(
            stats=stats,
            outliers=outliers,
            note=note,
        )

    def xǁListPipelineRunsUseCaseǁexecute__mutmut_29(self, command: ListPipelineRunsCommand) -> ListPipelineRunsResponse:
        all_runs = self._tekton.list_pipeline_runs(
            service_name=command.service_name,
            namespace=command.namespace,  # type: ignore
        )
        sorted_runs = sorted(all_runs, key=start_time_sort_key, reverse=True)
        runs = sorted_runs[: command.limit]
        stats = compute_stats(runs)
        outliers = find_outliers(runs, stats.average_duration_seconds)
        note = f"Only {len(runs)} run(s) available." if len(runs) < command.limit else None
        return ListPipelineRunsResponse(
            runs=runs,
            outliers=outliers,
            note=note,
        )

    def xǁListPipelineRunsUseCaseǁexecute__mutmut_30(self, command: ListPipelineRunsCommand) -> ListPipelineRunsResponse:
        all_runs = self._tekton.list_pipeline_runs(
            service_name=command.service_name,
            namespace=command.namespace,  # type: ignore
        )
        sorted_runs = sorted(all_runs, key=start_time_sort_key, reverse=True)
        runs = sorted_runs[: command.limit]
        stats = compute_stats(runs)
        outliers = find_outliers(runs, stats.average_duration_seconds)
        note = f"Only {len(runs)} run(s) available." if len(runs) < command.limit else None
        return ListPipelineRunsResponse(
            runs=runs,
            stats=stats,
            note=note,
        )

    def xǁListPipelineRunsUseCaseǁexecute__mutmut_31(self, command: ListPipelineRunsCommand) -> ListPipelineRunsResponse:
        all_runs = self._tekton.list_pipeline_runs(
            service_name=command.service_name,
            namespace=command.namespace,  # type: ignore
        )
        sorted_runs = sorted(all_runs, key=start_time_sort_key, reverse=True)
        runs = sorted_runs[: command.limit]
        stats = compute_stats(runs)
        outliers = find_outliers(runs, stats.average_duration_seconds)
        note = f"Only {len(runs)} run(s) available." if len(runs) < command.limit else None
        return ListPipelineRunsResponse(
            runs=runs,
            stats=stats,
            outliers=outliers,
            )

mutants_xǁListPipelineRunsUseCaseǁ__init____mutmut['_mutmut_orig'] = ListPipelineRunsUseCase.xǁListPipelineRunsUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁListPipelineRunsUseCaseǁ__init____mutmut['xǁListPipelineRunsUseCaseǁ__init____mutmut_1'] = ListPipelineRunsUseCase.xǁListPipelineRunsUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁListPipelineRunsUseCaseǁexecute__mutmut['_mutmut_orig'] = ListPipelineRunsUseCase.xǁListPipelineRunsUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁListPipelineRunsUseCaseǁexecute__mutmut['xǁListPipelineRunsUseCaseǁexecute__mutmut_1'] = ListPipelineRunsUseCase.xǁListPipelineRunsUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsUseCaseǁexecute__mutmut['xǁListPipelineRunsUseCaseǁexecute__mutmut_2'] = ListPipelineRunsUseCase.xǁListPipelineRunsUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsUseCaseǁexecute__mutmut['xǁListPipelineRunsUseCaseǁexecute__mutmut_3'] = ListPipelineRunsUseCase.xǁListPipelineRunsUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsUseCaseǁexecute__mutmut['xǁListPipelineRunsUseCaseǁexecute__mutmut_4'] = ListPipelineRunsUseCase.xǁListPipelineRunsUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsUseCaseǁexecute__mutmut['xǁListPipelineRunsUseCaseǁexecute__mutmut_5'] = ListPipelineRunsUseCase.xǁListPipelineRunsUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsUseCaseǁexecute__mutmut['xǁListPipelineRunsUseCaseǁexecute__mutmut_6'] = ListPipelineRunsUseCase.xǁListPipelineRunsUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsUseCaseǁexecute__mutmut['xǁListPipelineRunsUseCaseǁexecute__mutmut_7'] = ListPipelineRunsUseCase.xǁListPipelineRunsUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsUseCaseǁexecute__mutmut['xǁListPipelineRunsUseCaseǁexecute__mutmut_8'] = ListPipelineRunsUseCase.xǁListPipelineRunsUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsUseCaseǁexecute__mutmut['xǁListPipelineRunsUseCaseǁexecute__mutmut_9'] = ListPipelineRunsUseCase.xǁListPipelineRunsUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsUseCaseǁexecute__mutmut['xǁListPipelineRunsUseCaseǁexecute__mutmut_10'] = ListPipelineRunsUseCase.xǁListPipelineRunsUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsUseCaseǁexecute__mutmut['xǁListPipelineRunsUseCaseǁexecute__mutmut_11'] = ListPipelineRunsUseCase.xǁListPipelineRunsUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsUseCaseǁexecute__mutmut['xǁListPipelineRunsUseCaseǁexecute__mutmut_12'] = ListPipelineRunsUseCase.xǁListPipelineRunsUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsUseCaseǁexecute__mutmut['xǁListPipelineRunsUseCaseǁexecute__mutmut_13'] = ListPipelineRunsUseCase.xǁListPipelineRunsUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsUseCaseǁexecute__mutmut['xǁListPipelineRunsUseCaseǁexecute__mutmut_14'] = ListPipelineRunsUseCase.xǁListPipelineRunsUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsUseCaseǁexecute__mutmut['xǁListPipelineRunsUseCaseǁexecute__mutmut_15'] = ListPipelineRunsUseCase.xǁListPipelineRunsUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsUseCaseǁexecute__mutmut['xǁListPipelineRunsUseCaseǁexecute__mutmut_16'] = ListPipelineRunsUseCase.xǁListPipelineRunsUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsUseCaseǁexecute__mutmut['xǁListPipelineRunsUseCaseǁexecute__mutmut_17'] = ListPipelineRunsUseCase.xǁListPipelineRunsUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsUseCaseǁexecute__mutmut['xǁListPipelineRunsUseCaseǁexecute__mutmut_18'] = ListPipelineRunsUseCase.xǁListPipelineRunsUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsUseCaseǁexecute__mutmut['xǁListPipelineRunsUseCaseǁexecute__mutmut_19'] = ListPipelineRunsUseCase.xǁListPipelineRunsUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsUseCaseǁexecute__mutmut['xǁListPipelineRunsUseCaseǁexecute__mutmut_20'] = ListPipelineRunsUseCase.xǁListPipelineRunsUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsUseCaseǁexecute__mutmut['xǁListPipelineRunsUseCaseǁexecute__mutmut_21'] = ListPipelineRunsUseCase.xǁListPipelineRunsUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsUseCaseǁexecute__mutmut['xǁListPipelineRunsUseCaseǁexecute__mutmut_22'] = ListPipelineRunsUseCase.xǁListPipelineRunsUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsUseCaseǁexecute__mutmut['xǁListPipelineRunsUseCaseǁexecute__mutmut_23'] = ListPipelineRunsUseCase.xǁListPipelineRunsUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsUseCaseǁexecute__mutmut['xǁListPipelineRunsUseCaseǁexecute__mutmut_24'] = ListPipelineRunsUseCase.xǁListPipelineRunsUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsUseCaseǁexecute__mutmut['xǁListPipelineRunsUseCaseǁexecute__mutmut_25'] = ListPipelineRunsUseCase.xǁListPipelineRunsUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsUseCaseǁexecute__mutmut['xǁListPipelineRunsUseCaseǁexecute__mutmut_26'] = ListPipelineRunsUseCase.xǁListPipelineRunsUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsUseCaseǁexecute__mutmut['xǁListPipelineRunsUseCaseǁexecute__mutmut_27'] = ListPipelineRunsUseCase.xǁListPipelineRunsUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsUseCaseǁexecute__mutmut['xǁListPipelineRunsUseCaseǁexecute__mutmut_28'] = ListPipelineRunsUseCase.xǁListPipelineRunsUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsUseCaseǁexecute__mutmut['xǁListPipelineRunsUseCaseǁexecute__mutmut_29'] = ListPipelineRunsUseCase.xǁListPipelineRunsUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsUseCaseǁexecute__mutmut['xǁListPipelineRunsUseCaseǁexecute__mutmut_30'] = ListPipelineRunsUseCase.xǁListPipelineRunsUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁListPipelineRunsUseCaseǁexecute__mutmut['xǁListPipelineRunsUseCaseǁexecute__mutmut_31'] = ListPipelineRunsUseCase.xǁListPipelineRunsUseCaseǁexecute__mutmut_31 # type: ignore # mutmut generated
