from hexawyn.application.ports.driven.tekton_port import TektonPort
from hexawyn.application.use_case.pipelines.list_task_runs.command import (
    ListTaskRunsCommand,
)
from hexawyn.application.use_case.pipelines.list_task_runs.response import (
    ListTaskRunsResponse,
)
from hexawyn.application.use_case.pipelines.list_task_runs.sort_task_runs import (
    sort_by_start_time_desc,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁListTaskRunsUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁListTaskRunsUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class ListTaskRunsUseCase:
    """Lists TaskRuns for a pipeline, sorted by start time descending."""

    @_mutmut_mutated(mutants_xǁListTaskRunsUseCaseǁ__init____mutmut)
    def __init__(self, tekton_port: TektonPort) -> None:
        self._tekton = tekton_port

    def xǁListTaskRunsUseCaseǁ__init____mutmut_orig(self, tekton_port: TektonPort) -> None:
        self._tekton = tekton_port

    def xǁListTaskRunsUseCaseǁ__init____mutmut_1(self, tekton_port: TektonPort) -> None:
        self._tekton = None

    @_mutmut_mutated(mutants_xǁListTaskRunsUseCaseǁexecute__mutmut)
    def execute(self, command: ListTaskRunsCommand) -> ListTaskRunsResponse:
        task_runs = self._tekton.list_task_runs(
            pipeline_name=command.pipeline_name,
            namespace=command.namespace,  # type: ignore
        )
        sorted_runs = sort_by_start_time_desc(task_runs)
        return ListTaskRunsResponse(task_runs=sorted_runs)

    def xǁListTaskRunsUseCaseǁexecute__mutmut_orig(self, command: ListTaskRunsCommand) -> ListTaskRunsResponse:
        task_runs = self._tekton.list_task_runs(
            pipeline_name=command.pipeline_name,
            namespace=command.namespace,  # type: ignore
        )
        sorted_runs = sort_by_start_time_desc(task_runs)
        return ListTaskRunsResponse(task_runs=sorted_runs)

    def xǁListTaskRunsUseCaseǁexecute__mutmut_1(self, command: ListTaskRunsCommand) -> ListTaskRunsResponse:
        task_runs = None
        sorted_runs = sort_by_start_time_desc(task_runs)
        return ListTaskRunsResponse(task_runs=sorted_runs)

    def xǁListTaskRunsUseCaseǁexecute__mutmut_2(self, command: ListTaskRunsCommand) -> ListTaskRunsResponse:
        task_runs = self._tekton.list_task_runs(
            pipeline_name=None,
            namespace=command.namespace,  # type: ignore
        )
        sorted_runs = sort_by_start_time_desc(task_runs)
        return ListTaskRunsResponse(task_runs=sorted_runs)

    def xǁListTaskRunsUseCaseǁexecute__mutmut_3(self, command: ListTaskRunsCommand) -> ListTaskRunsResponse:
        task_runs = self._tekton.list_task_runs(
            pipeline_name=command.pipeline_name,
            namespace=None,  # type: ignore
        )
        sorted_runs = sort_by_start_time_desc(task_runs)
        return ListTaskRunsResponse(task_runs=sorted_runs)

    def xǁListTaskRunsUseCaseǁexecute__mutmut_4(self, command: ListTaskRunsCommand) -> ListTaskRunsResponse:
        task_runs = self._tekton.list_task_runs(
            namespace=command.namespace,  # type: ignore
        )
        sorted_runs = sort_by_start_time_desc(task_runs)
        return ListTaskRunsResponse(task_runs=sorted_runs)

    def xǁListTaskRunsUseCaseǁexecute__mutmut_5(self, command: ListTaskRunsCommand) -> ListTaskRunsResponse:
        task_runs = self._tekton.list_task_runs(
            pipeline_name=command.pipeline_name,
            )
        sorted_runs = sort_by_start_time_desc(task_runs)
        return ListTaskRunsResponse(task_runs=sorted_runs)

    def xǁListTaskRunsUseCaseǁexecute__mutmut_6(self, command: ListTaskRunsCommand) -> ListTaskRunsResponse:
        task_runs = self._tekton.list_task_runs(
            pipeline_name=command.pipeline_name,
            namespace=command.namespace,  # type: ignore
        )
        sorted_runs = None
        return ListTaskRunsResponse(task_runs=sorted_runs)

    def xǁListTaskRunsUseCaseǁexecute__mutmut_7(self, command: ListTaskRunsCommand) -> ListTaskRunsResponse:
        task_runs = self._tekton.list_task_runs(
            pipeline_name=command.pipeline_name,
            namespace=command.namespace,  # type: ignore
        )
        sorted_runs = sort_by_start_time_desc(None)
        return ListTaskRunsResponse(task_runs=sorted_runs)

    def xǁListTaskRunsUseCaseǁexecute__mutmut_8(self, command: ListTaskRunsCommand) -> ListTaskRunsResponse:
        task_runs = self._tekton.list_task_runs(
            pipeline_name=command.pipeline_name,
            namespace=command.namespace,  # type: ignore
        )
        sorted_runs = sort_by_start_time_desc(task_runs)
        return ListTaskRunsResponse(task_runs=None)

mutants_xǁListTaskRunsUseCaseǁ__init____mutmut['_mutmut_orig'] = ListTaskRunsUseCase.xǁListTaskRunsUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁListTaskRunsUseCaseǁ__init____mutmut['xǁListTaskRunsUseCaseǁ__init____mutmut_1'] = ListTaskRunsUseCase.xǁListTaskRunsUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁListTaskRunsUseCaseǁexecute__mutmut['_mutmut_orig'] = ListTaskRunsUseCase.xǁListTaskRunsUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁListTaskRunsUseCaseǁexecute__mutmut['xǁListTaskRunsUseCaseǁexecute__mutmut_1'] = ListTaskRunsUseCase.xǁListTaskRunsUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁListTaskRunsUseCaseǁexecute__mutmut['xǁListTaskRunsUseCaseǁexecute__mutmut_2'] = ListTaskRunsUseCase.xǁListTaskRunsUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁListTaskRunsUseCaseǁexecute__mutmut['xǁListTaskRunsUseCaseǁexecute__mutmut_3'] = ListTaskRunsUseCase.xǁListTaskRunsUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁListTaskRunsUseCaseǁexecute__mutmut['xǁListTaskRunsUseCaseǁexecute__mutmut_4'] = ListTaskRunsUseCase.xǁListTaskRunsUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁListTaskRunsUseCaseǁexecute__mutmut['xǁListTaskRunsUseCaseǁexecute__mutmut_5'] = ListTaskRunsUseCase.xǁListTaskRunsUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁListTaskRunsUseCaseǁexecute__mutmut['xǁListTaskRunsUseCaseǁexecute__mutmut_6'] = ListTaskRunsUseCase.xǁListTaskRunsUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁListTaskRunsUseCaseǁexecute__mutmut['xǁListTaskRunsUseCaseǁexecute__mutmut_7'] = ListTaskRunsUseCase.xǁListTaskRunsUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁListTaskRunsUseCaseǁexecute__mutmut['xǁListTaskRunsUseCaseǁexecute__mutmut_8'] = ListTaskRunsUseCase.xǁListTaskRunsUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
