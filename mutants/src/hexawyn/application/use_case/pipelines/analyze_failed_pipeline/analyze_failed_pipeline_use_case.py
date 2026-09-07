from __future__ import annotations

from hexawyn.application.ports.driven.pipeline_run_logs_port import PipelineRunLogsPort
from hexawyn.application.ports.driven.tekton_port import TektonPort
from hexawyn.application.use_case.pipelines.analyze_failed_pipeline.command import (
    AnalyzeFailedPipelineCommand,
)
from hexawyn.application.use_case.pipelines.analyze_failed_pipeline.mapper import (
    to_response,
)
from hexawyn.application.use_case.pipelines.analyze_failed_pipeline.response import (
    AnalyzeFailedPipelineResponse,
)
from hexawyn.domain.models.pipeline_failure_analysis import (
    AnalyzeFailedPipelineRequest,
)
from hexawyn.domain.models.pipeline_run_logs import PipelineRunLogsRequest
from hexawyn.domain.services.failure_analysis.rca import analyze_pipeline_failure


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁAnalyzeFailedPipelineUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class AnalyzeFailedPipelineUseCase:
    @_mutmut_mutated(mutants_xǁAnalyzeFailedPipelineUseCaseǁ__init____mutmut)
    def __init__(
        self, tekton_port: TektonPort, pipeline_run_logs_port: PipelineRunLogsPort
    ) -> None:
        self._tekton = tekton_port
        self._logs_port = pipeline_run_logs_port
    def xǁAnalyzeFailedPipelineUseCaseǁ__init____mutmut_orig(
        self, tekton_port: TektonPort, pipeline_run_logs_port: PipelineRunLogsPort
    ) -> None:
        self._tekton = tekton_port
        self._logs_port = pipeline_run_logs_port
    def xǁAnalyzeFailedPipelineUseCaseǁ__init____mutmut_1(
        self, tekton_port: TektonPort, pipeline_run_logs_port: PipelineRunLogsPort
    ) -> None:
        self._tekton = None
        self._logs_port = pipeline_run_logs_port
    def xǁAnalyzeFailedPipelineUseCaseǁ__init____mutmut_2(
        self, tekton_port: TektonPort, pipeline_run_logs_port: PipelineRunLogsPort
    ) -> None:
        self._tekton = tekton_port
        self._logs_port = None

    @_mutmut_mutated(mutants_xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut)
    def execute(self, command: AnalyzeFailedPipelineCommand) -> AnalyzeFailedPipelineResponse:
        task_runs = self._tekton.list_task_runs(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        step_logs = self._logs_port.fetch_step_logs(
            PipelineRunLogsRequest(
                pipeline_run_name=command.pipeline_name,
                namespace=command.namespace,
            )
        )

        request = AnalyzeFailedPipelineRequest(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        result = analyze_pipeline_failure(request, task_runs, step_logs)
        return to_response(result)

    def xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_orig(self, command: AnalyzeFailedPipelineCommand) -> AnalyzeFailedPipelineResponse:
        task_runs = self._tekton.list_task_runs(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        step_logs = self._logs_port.fetch_step_logs(
            PipelineRunLogsRequest(
                pipeline_run_name=command.pipeline_name,
                namespace=command.namespace,
            )
        )

        request = AnalyzeFailedPipelineRequest(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        result = analyze_pipeline_failure(request, task_runs, step_logs)
        return to_response(result)

    def xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_1(self, command: AnalyzeFailedPipelineCommand) -> AnalyzeFailedPipelineResponse:
        task_runs = None
        step_logs = self._logs_port.fetch_step_logs(
            PipelineRunLogsRequest(
                pipeline_run_name=command.pipeline_name,
                namespace=command.namespace,
            )
        )

        request = AnalyzeFailedPipelineRequest(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        result = analyze_pipeline_failure(request, task_runs, step_logs)
        return to_response(result)

    def xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_2(self, command: AnalyzeFailedPipelineCommand) -> AnalyzeFailedPipelineResponse:
        task_runs = self._tekton.list_task_runs(
            pipeline_name=None, namespace=command.namespace
        )
        step_logs = self._logs_port.fetch_step_logs(
            PipelineRunLogsRequest(
                pipeline_run_name=command.pipeline_name,
                namespace=command.namespace,
            )
        )

        request = AnalyzeFailedPipelineRequest(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        result = analyze_pipeline_failure(request, task_runs, step_logs)
        return to_response(result)

    def xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_3(self, command: AnalyzeFailedPipelineCommand) -> AnalyzeFailedPipelineResponse:
        task_runs = self._tekton.list_task_runs(
            pipeline_name=command.pipeline_name, namespace=None
        )
        step_logs = self._logs_port.fetch_step_logs(
            PipelineRunLogsRequest(
                pipeline_run_name=command.pipeline_name,
                namespace=command.namespace,
            )
        )

        request = AnalyzeFailedPipelineRequest(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        result = analyze_pipeline_failure(request, task_runs, step_logs)
        return to_response(result)

    def xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_4(self, command: AnalyzeFailedPipelineCommand) -> AnalyzeFailedPipelineResponse:
        task_runs = self._tekton.list_task_runs(
            namespace=command.namespace
        )
        step_logs = self._logs_port.fetch_step_logs(
            PipelineRunLogsRequest(
                pipeline_run_name=command.pipeline_name,
                namespace=command.namespace,
            )
        )

        request = AnalyzeFailedPipelineRequest(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        result = analyze_pipeline_failure(request, task_runs, step_logs)
        return to_response(result)

    def xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_5(self, command: AnalyzeFailedPipelineCommand) -> AnalyzeFailedPipelineResponse:
        task_runs = self._tekton.list_task_runs(
            pipeline_name=command.pipeline_name, )
        step_logs = self._logs_port.fetch_step_logs(
            PipelineRunLogsRequest(
                pipeline_run_name=command.pipeline_name,
                namespace=command.namespace,
            )
        )

        request = AnalyzeFailedPipelineRequest(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        result = analyze_pipeline_failure(request, task_runs, step_logs)
        return to_response(result)

    def xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_6(self, command: AnalyzeFailedPipelineCommand) -> AnalyzeFailedPipelineResponse:
        task_runs = self._tekton.list_task_runs(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        step_logs = None

        request = AnalyzeFailedPipelineRequest(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        result = analyze_pipeline_failure(request, task_runs, step_logs)
        return to_response(result)

    def xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_7(self, command: AnalyzeFailedPipelineCommand) -> AnalyzeFailedPipelineResponse:
        task_runs = self._tekton.list_task_runs(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        step_logs = self._logs_port.fetch_step_logs(
            None
        )

        request = AnalyzeFailedPipelineRequest(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        result = analyze_pipeline_failure(request, task_runs, step_logs)
        return to_response(result)

    def xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_8(self, command: AnalyzeFailedPipelineCommand) -> AnalyzeFailedPipelineResponse:
        task_runs = self._tekton.list_task_runs(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        step_logs = self._logs_port.fetch_step_logs(
            PipelineRunLogsRequest(
                pipeline_run_name=None,
                namespace=command.namespace,
            )
        )

        request = AnalyzeFailedPipelineRequest(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        result = analyze_pipeline_failure(request, task_runs, step_logs)
        return to_response(result)

    def xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_9(self, command: AnalyzeFailedPipelineCommand) -> AnalyzeFailedPipelineResponse:
        task_runs = self._tekton.list_task_runs(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        step_logs = self._logs_port.fetch_step_logs(
            PipelineRunLogsRequest(
                pipeline_run_name=command.pipeline_name,
                namespace=None,
            )
        )

        request = AnalyzeFailedPipelineRequest(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        result = analyze_pipeline_failure(request, task_runs, step_logs)
        return to_response(result)

    def xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_10(self, command: AnalyzeFailedPipelineCommand) -> AnalyzeFailedPipelineResponse:
        task_runs = self._tekton.list_task_runs(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        step_logs = self._logs_port.fetch_step_logs(
            PipelineRunLogsRequest(
                namespace=command.namespace,
            )
        )

        request = AnalyzeFailedPipelineRequest(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        result = analyze_pipeline_failure(request, task_runs, step_logs)
        return to_response(result)

    def xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_11(self, command: AnalyzeFailedPipelineCommand) -> AnalyzeFailedPipelineResponse:
        task_runs = self._tekton.list_task_runs(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        step_logs = self._logs_port.fetch_step_logs(
            PipelineRunLogsRequest(
                pipeline_run_name=command.pipeline_name,
                )
        )

        request = AnalyzeFailedPipelineRequest(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        result = analyze_pipeline_failure(request, task_runs, step_logs)
        return to_response(result)

    def xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_12(self, command: AnalyzeFailedPipelineCommand) -> AnalyzeFailedPipelineResponse:
        task_runs = self._tekton.list_task_runs(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        step_logs = self._logs_port.fetch_step_logs(
            PipelineRunLogsRequest(
                pipeline_run_name=command.pipeline_name,
                namespace=command.namespace,
            )
        )

        request = None
        result = analyze_pipeline_failure(request, task_runs, step_logs)
        return to_response(result)

    def xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_13(self, command: AnalyzeFailedPipelineCommand) -> AnalyzeFailedPipelineResponse:
        task_runs = self._tekton.list_task_runs(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        step_logs = self._logs_port.fetch_step_logs(
            PipelineRunLogsRequest(
                pipeline_run_name=command.pipeline_name,
                namespace=command.namespace,
            )
        )

        request = AnalyzeFailedPipelineRequest(
            pipeline_name=None, namespace=command.namespace
        )
        result = analyze_pipeline_failure(request, task_runs, step_logs)
        return to_response(result)

    def xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_14(self, command: AnalyzeFailedPipelineCommand) -> AnalyzeFailedPipelineResponse:
        task_runs = self._tekton.list_task_runs(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        step_logs = self._logs_port.fetch_step_logs(
            PipelineRunLogsRequest(
                pipeline_run_name=command.pipeline_name,
                namespace=command.namespace,
            )
        )

        request = AnalyzeFailedPipelineRequest(
            pipeline_name=command.pipeline_name, namespace=None
        )
        result = analyze_pipeline_failure(request, task_runs, step_logs)
        return to_response(result)

    def xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_15(self, command: AnalyzeFailedPipelineCommand) -> AnalyzeFailedPipelineResponse:
        task_runs = self._tekton.list_task_runs(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        step_logs = self._logs_port.fetch_step_logs(
            PipelineRunLogsRequest(
                pipeline_run_name=command.pipeline_name,
                namespace=command.namespace,
            )
        )

        request = AnalyzeFailedPipelineRequest(
            namespace=command.namespace
        )
        result = analyze_pipeline_failure(request, task_runs, step_logs)
        return to_response(result)

    def xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_16(self, command: AnalyzeFailedPipelineCommand) -> AnalyzeFailedPipelineResponse:
        task_runs = self._tekton.list_task_runs(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        step_logs = self._logs_port.fetch_step_logs(
            PipelineRunLogsRequest(
                pipeline_run_name=command.pipeline_name,
                namespace=command.namespace,
            )
        )

        request = AnalyzeFailedPipelineRequest(
            pipeline_name=command.pipeline_name, )
        result = analyze_pipeline_failure(request, task_runs, step_logs)
        return to_response(result)

    def xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_17(self, command: AnalyzeFailedPipelineCommand) -> AnalyzeFailedPipelineResponse:
        task_runs = self._tekton.list_task_runs(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        step_logs = self._logs_port.fetch_step_logs(
            PipelineRunLogsRequest(
                pipeline_run_name=command.pipeline_name,
                namespace=command.namespace,
            )
        )

        request = AnalyzeFailedPipelineRequest(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        result = None
        return to_response(result)

    def xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_18(self, command: AnalyzeFailedPipelineCommand) -> AnalyzeFailedPipelineResponse:
        task_runs = self._tekton.list_task_runs(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        step_logs = self._logs_port.fetch_step_logs(
            PipelineRunLogsRequest(
                pipeline_run_name=command.pipeline_name,
                namespace=command.namespace,
            )
        )

        request = AnalyzeFailedPipelineRequest(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        result = analyze_pipeline_failure(None, task_runs, step_logs)
        return to_response(result)

    def xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_19(self, command: AnalyzeFailedPipelineCommand) -> AnalyzeFailedPipelineResponse:
        task_runs = self._tekton.list_task_runs(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        step_logs = self._logs_port.fetch_step_logs(
            PipelineRunLogsRequest(
                pipeline_run_name=command.pipeline_name,
                namespace=command.namespace,
            )
        )

        request = AnalyzeFailedPipelineRequest(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        result = analyze_pipeline_failure(request, None, step_logs)
        return to_response(result)

    def xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_20(self, command: AnalyzeFailedPipelineCommand) -> AnalyzeFailedPipelineResponse:
        task_runs = self._tekton.list_task_runs(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        step_logs = self._logs_port.fetch_step_logs(
            PipelineRunLogsRequest(
                pipeline_run_name=command.pipeline_name,
                namespace=command.namespace,
            )
        )

        request = AnalyzeFailedPipelineRequest(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        result = analyze_pipeline_failure(request, task_runs, None)
        return to_response(result)

    def xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_21(self, command: AnalyzeFailedPipelineCommand) -> AnalyzeFailedPipelineResponse:
        task_runs = self._tekton.list_task_runs(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        step_logs = self._logs_port.fetch_step_logs(
            PipelineRunLogsRequest(
                pipeline_run_name=command.pipeline_name,
                namespace=command.namespace,
            )
        )

        request = AnalyzeFailedPipelineRequest(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        result = analyze_pipeline_failure(task_runs, step_logs)
        return to_response(result)

    def xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_22(self, command: AnalyzeFailedPipelineCommand) -> AnalyzeFailedPipelineResponse:
        task_runs = self._tekton.list_task_runs(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        step_logs = self._logs_port.fetch_step_logs(
            PipelineRunLogsRequest(
                pipeline_run_name=command.pipeline_name,
                namespace=command.namespace,
            )
        )

        request = AnalyzeFailedPipelineRequest(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        result = analyze_pipeline_failure(request, step_logs)
        return to_response(result)

    def xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_23(self, command: AnalyzeFailedPipelineCommand) -> AnalyzeFailedPipelineResponse:
        task_runs = self._tekton.list_task_runs(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        step_logs = self._logs_port.fetch_step_logs(
            PipelineRunLogsRequest(
                pipeline_run_name=command.pipeline_name,
                namespace=command.namespace,
            )
        )

        request = AnalyzeFailedPipelineRequest(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        result = analyze_pipeline_failure(request, task_runs, )
        return to_response(result)

    def xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_24(self, command: AnalyzeFailedPipelineCommand) -> AnalyzeFailedPipelineResponse:
        task_runs = self._tekton.list_task_runs(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        step_logs = self._logs_port.fetch_step_logs(
            PipelineRunLogsRequest(
                pipeline_run_name=command.pipeline_name,
                namespace=command.namespace,
            )
        )

        request = AnalyzeFailedPipelineRequest(
            pipeline_name=command.pipeline_name, namespace=command.namespace
        )
        result = analyze_pipeline_failure(request, task_runs, step_logs)
        return to_response(None)

mutants_xǁAnalyzeFailedPipelineUseCaseǁ__init____mutmut['_mutmut_orig'] = AnalyzeFailedPipelineUseCase.xǁAnalyzeFailedPipelineUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁAnalyzeFailedPipelineUseCaseǁ__init____mutmut['xǁAnalyzeFailedPipelineUseCaseǁ__init____mutmut_1'] = AnalyzeFailedPipelineUseCase.xǁAnalyzeFailedPipelineUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁAnalyzeFailedPipelineUseCaseǁ__init____mutmut['xǁAnalyzeFailedPipelineUseCaseǁ__init____mutmut_2'] = AnalyzeFailedPipelineUseCase.xǁAnalyzeFailedPipelineUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut['_mutmut_orig'] = AnalyzeFailedPipelineUseCase.xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut['xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_1'] = AnalyzeFailedPipelineUseCase.xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut['xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_2'] = AnalyzeFailedPipelineUseCase.xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut['xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_3'] = AnalyzeFailedPipelineUseCase.xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut['xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_4'] = AnalyzeFailedPipelineUseCase.xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut['xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_5'] = AnalyzeFailedPipelineUseCase.xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut['xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_6'] = AnalyzeFailedPipelineUseCase.xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut['xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_7'] = AnalyzeFailedPipelineUseCase.xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut['xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_8'] = AnalyzeFailedPipelineUseCase.xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut['xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_9'] = AnalyzeFailedPipelineUseCase.xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut['xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_10'] = AnalyzeFailedPipelineUseCase.xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut['xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_11'] = AnalyzeFailedPipelineUseCase.xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut['xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_12'] = AnalyzeFailedPipelineUseCase.xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut['xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_13'] = AnalyzeFailedPipelineUseCase.xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut['xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_14'] = AnalyzeFailedPipelineUseCase.xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut['xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_15'] = AnalyzeFailedPipelineUseCase.xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut['xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_16'] = AnalyzeFailedPipelineUseCase.xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut['xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_17'] = AnalyzeFailedPipelineUseCase.xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut['xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_18'] = AnalyzeFailedPipelineUseCase.xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut['xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_19'] = AnalyzeFailedPipelineUseCase.xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut['xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_20'] = AnalyzeFailedPipelineUseCase.xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut['xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_21'] = AnalyzeFailedPipelineUseCase.xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut['xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_22'] = AnalyzeFailedPipelineUseCase.xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut['xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_23'] = AnalyzeFailedPipelineUseCase.xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut['xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_24'] = AnalyzeFailedPipelineUseCase.xǁAnalyzeFailedPipelineUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
