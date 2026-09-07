from __future__ import annotations

from hexawyn.application.ports.driven.pipeline_tracer_port import PipelineTracerPort
from hexawyn.application.use_case.pipelines.trace_pipeline_run_dag.command import (
    TracePipelineRunDagCommand,
)
from hexawyn.application.use_case.pipelines.trace_pipeline_run_dag.response import (
    TracePipelineRunDagResponse,
)
from hexawyn.domain.services.pipeline_dag.pipeline_dag_tracer_service import (
    PipelineDAGTracerService,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁTracePipelineRunDagUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut: MutantDict = {}  # type: ignore


class TracePipelineRunDagUseCase:
    @_mutmut_mutated(mutants_xǁTracePipelineRunDagUseCaseǁ__init____mutmut)
    def __init__(self, port: PipelineTracerPort) -> None:
        self._port = port
    def xǁTracePipelineRunDagUseCaseǁ__init____mutmut_orig(self, port: PipelineTracerPort) -> None:
        self._port = port
    def xǁTracePipelineRunDagUseCaseǁ__init____mutmut_1(self, port: PipelineTracerPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut)
    def trace_pipeline_run_dag(
        self, command: TracePipelineRunDagCommand
    ) -> TracePipelineRunDagResponse:
        pipeline = self._port.get_pipeline_run(command.namespace, command.pipeline_run_name)
        task_runs = self._port.list_task_runs_for_pipeline(
            command.namespace, command.pipeline_run_name
        )
        dag = PipelineDAGTracerService.build_dag(
            pipeline_run_name=command.pipeline_run_name,
            namespace=command.namespace,
            pipeline_status=pipeline["status"],
            task_runs=task_runs,
        )
        return TracePipelineRunDagResponse(dag=dag)  # type: ignore

    def xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_orig(
        self, command: TracePipelineRunDagCommand
    ) -> TracePipelineRunDagResponse:
        pipeline = self._port.get_pipeline_run(command.namespace, command.pipeline_run_name)
        task_runs = self._port.list_task_runs_for_pipeline(
            command.namespace, command.pipeline_run_name
        )
        dag = PipelineDAGTracerService.build_dag(
            pipeline_run_name=command.pipeline_run_name,
            namespace=command.namespace,
            pipeline_status=pipeline["status"],
            task_runs=task_runs,
        )
        return TracePipelineRunDagResponse(dag=dag)  # type: ignore

    def xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_1(
        self, command: TracePipelineRunDagCommand
    ) -> TracePipelineRunDagResponse:
        pipeline = None
        task_runs = self._port.list_task_runs_for_pipeline(
            command.namespace, command.pipeline_run_name
        )
        dag = PipelineDAGTracerService.build_dag(
            pipeline_run_name=command.pipeline_run_name,
            namespace=command.namespace,
            pipeline_status=pipeline["status"],
            task_runs=task_runs,
        )
        return TracePipelineRunDagResponse(dag=dag)  # type: ignore

    def xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_2(
        self, command: TracePipelineRunDagCommand
    ) -> TracePipelineRunDagResponse:
        pipeline = self._port.get_pipeline_run(None, command.pipeline_run_name)
        task_runs = self._port.list_task_runs_for_pipeline(
            command.namespace, command.pipeline_run_name
        )
        dag = PipelineDAGTracerService.build_dag(
            pipeline_run_name=command.pipeline_run_name,
            namespace=command.namespace,
            pipeline_status=pipeline["status"],
            task_runs=task_runs,
        )
        return TracePipelineRunDagResponse(dag=dag)  # type: ignore

    def xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_3(
        self, command: TracePipelineRunDagCommand
    ) -> TracePipelineRunDagResponse:
        pipeline = self._port.get_pipeline_run(command.namespace, None)
        task_runs = self._port.list_task_runs_for_pipeline(
            command.namespace, command.pipeline_run_name
        )
        dag = PipelineDAGTracerService.build_dag(
            pipeline_run_name=command.pipeline_run_name,
            namespace=command.namespace,
            pipeline_status=pipeline["status"],
            task_runs=task_runs,
        )
        return TracePipelineRunDagResponse(dag=dag)  # type: ignore

    def xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_4(
        self, command: TracePipelineRunDagCommand
    ) -> TracePipelineRunDagResponse:
        pipeline = self._port.get_pipeline_run(command.pipeline_run_name)
        task_runs = self._port.list_task_runs_for_pipeline(
            command.namespace, command.pipeline_run_name
        )
        dag = PipelineDAGTracerService.build_dag(
            pipeline_run_name=command.pipeline_run_name,
            namespace=command.namespace,
            pipeline_status=pipeline["status"],
            task_runs=task_runs,
        )
        return TracePipelineRunDagResponse(dag=dag)  # type: ignore

    def xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_5(
        self, command: TracePipelineRunDagCommand
    ) -> TracePipelineRunDagResponse:
        pipeline = self._port.get_pipeline_run(command.namespace, )
        task_runs = self._port.list_task_runs_for_pipeline(
            command.namespace, command.pipeline_run_name
        )
        dag = PipelineDAGTracerService.build_dag(
            pipeline_run_name=command.pipeline_run_name,
            namespace=command.namespace,
            pipeline_status=pipeline["status"],
            task_runs=task_runs,
        )
        return TracePipelineRunDagResponse(dag=dag)  # type: ignore

    def xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_6(
        self, command: TracePipelineRunDagCommand
    ) -> TracePipelineRunDagResponse:
        pipeline = self._port.get_pipeline_run(command.namespace, command.pipeline_run_name)
        task_runs = None
        dag = PipelineDAGTracerService.build_dag(
            pipeline_run_name=command.pipeline_run_name,
            namespace=command.namespace,
            pipeline_status=pipeline["status"],
            task_runs=task_runs,
        )
        return TracePipelineRunDagResponse(dag=dag)  # type: ignore

    def xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_7(
        self, command: TracePipelineRunDagCommand
    ) -> TracePipelineRunDagResponse:
        pipeline = self._port.get_pipeline_run(command.namespace, command.pipeline_run_name)
        task_runs = self._port.list_task_runs_for_pipeline(
            None, command.pipeline_run_name
        )
        dag = PipelineDAGTracerService.build_dag(
            pipeline_run_name=command.pipeline_run_name,
            namespace=command.namespace,
            pipeline_status=pipeline["status"],
            task_runs=task_runs,
        )
        return TracePipelineRunDagResponse(dag=dag)  # type: ignore

    def xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_8(
        self, command: TracePipelineRunDagCommand
    ) -> TracePipelineRunDagResponse:
        pipeline = self._port.get_pipeline_run(command.namespace, command.pipeline_run_name)
        task_runs = self._port.list_task_runs_for_pipeline(
            command.namespace, None
        )
        dag = PipelineDAGTracerService.build_dag(
            pipeline_run_name=command.pipeline_run_name,
            namespace=command.namespace,
            pipeline_status=pipeline["status"],
            task_runs=task_runs,
        )
        return TracePipelineRunDagResponse(dag=dag)  # type: ignore

    def xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_9(
        self, command: TracePipelineRunDagCommand
    ) -> TracePipelineRunDagResponse:
        pipeline = self._port.get_pipeline_run(command.namespace, command.pipeline_run_name)
        task_runs = self._port.list_task_runs_for_pipeline(
            command.pipeline_run_name
        )
        dag = PipelineDAGTracerService.build_dag(
            pipeline_run_name=command.pipeline_run_name,
            namespace=command.namespace,
            pipeline_status=pipeline["status"],
            task_runs=task_runs,
        )
        return TracePipelineRunDagResponse(dag=dag)  # type: ignore

    def xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_10(
        self, command: TracePipelineRunDagCommand
    ) -> TracePipelineRunDagResponse:
        pipeline = self._port.get_pipeline_run(command.namespace, command.pipeline_run_name)
        task_runs = self._port.list_task_runs_for_pipeline(
            command.namespace, )
        dag = PipelineDAGTracerService.build_dag(
            pipeline_run_name=command.pipeline_run_name,
            namespace=command.namespace,
            pipeline_status=pipeline["status"],
            task_runs=task_runs,
        )
        return TracePipelineRunDagResponse(dag=dag)  # type: ignore

    def xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_11(
        self, command: TracePipelineRunDagCommand
    ) -> TracePipelineRunDagResponse:
        pipeline = self._port.get_pipeline_run(command.namespace, command.pipeline_run_name)
        task_runs = self._port.list_task_runs_for_pipeline(
            command.namespace, command.pipeline_run_name
        )
        dag = None
        return TracePipelineRunDagResponse(dag=dag)  # type: ignore

    def xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_12(
        self, command: TracePipelineRunDagCommand
    ) -> TracePipelineRunDagResponse:
        pipeline = self._port.get_pipeline_run(command.namespace, command.pipeline_run_name)
        task_runs = self._port.list_task_runs_for_pipeline(
            command.namespace, command.pipeline_run_name
        )
        dag = PipelineDAGTracerService.build_dag(
            pipeline_run_name=None,
            namespace=command.namespace,
            pipeline_status=pipeline["status"],
            task_runs=task_runs,
        )
        return TracePipelineRunDagResponse(dag=dag)  # type: ignore

    def xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_13(
        self, command: TracePipelineRunDagCommand
    ) -> TracePipelineRunDagResponse:
        pipeline = self._port.get_pipeline_run(command.namespace, command.pipeline_run_name)
        task_runs = self._port.list_task_runs_for_pipeline(
            command.namespace, command.pipeline_run_name
        )
        dag = PipelineDAGTracerService.build_dag(
            pipeline_run_name=command.pipeline_run_name,
            namespace=None,
            pipeline_status=pipeline["status"],
            task_runs=task_runs,
        )
        return TracePipelineRunDagResponse(dag=dag)  # type: ignore

    def xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_14(
        self, command: TracePipelineRunDagCommand
    ) -> TracePipelineRunDagResponse:
        pipeline = self._port.get_pipeline_run(command.namespace, command.pipeline_run_name)
        task_runs = self._port.list_task_runs_for_pipeline(
            command.namespace, command.pipeline_run_name
        )
        dag = PipelineDAGTracerService.build_dag(
            pipeline_run_name=command.pipeline_run_name,
            namespace=command.namespace,
            pipeline_status=None,
            task_runs=task_runs,
        )
        return TracePipelineRunDagResponse(dag=dag)  # type: ignore

    def xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_15(
        self, command: TracePipelineRunDagCommand
    ) -> TracePipelineRunDagResponse:
        pipeline = self._port.get_pipeline_run(command.namespace, command.pipeline_run_name)
        task_runs = self._port.list_task_runs_for_pipeline(
            command.namespace, command.pipeline_run_name
        )
        dag = PipelineDAGTracerService.build_dag(
            pipeline_run_name=command.pipeline_run_name,
            namespace=command.namespace,
            pipeline_status=pipeline["status"],
            task_runs=None,
        )
        return TracePipelineRunDagResponse(dag=dag)  # type: ignore

    def xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_16(
        self, command: TracePipelineRunDagCommand
    ) -> TracePipelineRunDagResponse:
        pipeline = self._port.get_pipeline_run(command.namespace, command.pipeline_run_name)
        task_runs = self._port.list_task_runs_for_pipeline(
            command.namespace, command.pipeline_run_name
        )
        dag = PipelineDAGTracerService.build_dag(
            namespace=command.namespace,
            pipeline_status=pipeline["status"],
            task_runs=task_runs,
        )
        return TracePipelineRunDagResponse(dag=dag)  # type: ignore

    def xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_17(
        self, command: TracePipelineRunDagCommand
    ) -> TracePipelineRunDagResponse:
        pipeline = self._port.get_pipeline_run(command.namespace, command.pipeline_run_name)
        task_runs = self._port.list_task_runs_for_pipeline(
            command.namespace, command.pipeline_run_name
        )
        dag = PipelineDAGTracerService.build_dag(
            pipeline_run_name=command.pipeline_run_name,
            pipeline_status=pipeline["status"],
            task_runs=task_runs,
        )
        return TracePipelineRunDagResponse(dag=dag)  # type: ignore

    def xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_18(
        self, command: TracePipelineRunDagCommand
    ) -> TracePipelineRunDagResponse:
        pipeline = self._port.get_pipeline_run(command.namespace, command.pipeline_run_name)
        task_runs = self._port.list_task_runs_for_pipeline(
            command.namespace, command.pipeline_run_name
        )
        dag = PipelineDAGTracerService.build_dag(
            pipeline_run_name=command.pipeline_run_name,
            namespace=command.namespace,
            task_runs=task_runs,
        )
        return TracePipelineRunDagResponse(dag=dag)  # type: ignore

    def xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_19(
        self, command: TracePipelineRunDagCommand
    ) -> TracePipelineRunDagResponse:
        pipeline = self._port.get_pipeline_run(command.namespace, command.pipeline_run_name)
        task_runs = self._port.list_task_runs_for_pipeline(
            command.namespace, command.pipeline_run_name
        )
        dag = PipelineDAGTracerService.build_dag(
            pipeline_run_name=command.pipeline_run_name,
            namespace=command.namespace,
            pipeline_status=pipeline["status"],
            )
        return TracePipelineRunDagResponse(dag=dag)  # type: ignore

    def xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_20(
        self, command: TracePipelineRunDagCommand
    ) -> TracePipelineRunDagResponse:
        pipeline = self._port.get_pipeline_run(command.namespace, command.pipeline_run_name)
        task_runs = self._port.list_task_runs_for_pipeline(
            command.namespace, command.pipeline_run_name
        )
        dag = PipelineDAGTracerService.build_dag(
            pipeline_run_name=command.pipeline_run_name,
            namespace=command.namespace,
            pipeline_status=pipeline["XXstatusXX"],
            task_runs=task_runs,
        )
        return TracePipelineRunDagResponse(dag=dag)  # type: ignore

    def xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_21(
        self, command: TracePipelineRunDagCommand
    ) -> TracePipelineRunDagResponse:
        pipeline = self._port.get_pipeline_run(command.namespace, command.pipeline_run_name)
        task_runs = self._port.list_task_runs_for_pipeline(
            command.namespace, command.pipeline_run_name
        )
        dag = PipelineDAGTracerService.build_dag(
            pipeline_run_name=command.pipeline_run_name,
            namespace=command.namespace,
            pipeline_status=pipeline["STATUS"],
            task_runs=task_runs,
        )
        return TracePipelineRunDagResponse(dag=dag)  # type: ignore

    def xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_22(
        self, command: TracePipelineRunDagCommand
    ) -> TracePipelineRunDagResponse:
        pipeline = self._port.get_pipeline_run(command.namespace, command.pipeline_run_name)
        task_runs = self._port.list_task_runs_for_pipeline(
            command.namespace, command.pipeline_run_name
        )
        dag = PipelineDAGTracerService.build_dag(
            pipeline_run_name=command.pipeline_run_name,
            namespace=command.namespace,
            pipeline_status=pipeline["status"],
            task_runs=task_runs,
        )
        return TracePipelineRunDagResponse(dag=None)  # type: ignore

mutants_xǁTracePipelineRunDagUseCaseǁ__init____mutmut['_mutmut_orig'] = TracePipelineRunDagUseCase.xǁTracePipelineRunDagUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁTracePipelineRunDagUseCaseǁ__init____mutmut['xǁTracePipelineRunDagUseCaseǁ__init____mutmut_1'] = TracePipelineRunDagUseCase.xǁTracePipelineRunDagUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut['_mutmut_orig'] = TracePipelineRunDagUseCase.xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut['xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_1'] = TracePipelineRunDagUseCase.xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut['xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_2'] = TracePipelineRunDagUseCase.xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut['xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_3'] = TracePipelineRunDagUseCase.xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut['xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_4'] = TracePipelineRunDagUseCase.xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut['xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_5'] = TracePipelineRunDagUseCase.xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut['xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_6'] = TracePipelineRunDagUseCase.xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut['xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_7'] = TracePipelineRunDagUseCase.xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut['xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_8'] = TracePipelineRunDagUseCase.xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_8 # type: ignore # mutmut generated
mutants_xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut['xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_9'] = TracePipelineRunDagUseCase.xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_9 # type: ignore # mutmut generated
mutants_xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut['xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_10'] = TracePipelineRunDagUseCase.xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_10 # type: ignore # mutmut generated
mutants_xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut['xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_11'] = TracePipelineRunDagUseCase.xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_11 # type: ignore # mutmut generated
mutants_xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut['xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_12'] = TracePipelineRunDagUseCase.xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_12 # type: ignore # mutmut generated
mutants_xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut['xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_13'] = TracePipelineRunDagUseCase.xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_13 # type: ignore # mutmut generated
mutants_xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut['xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_14'] = TracePipelineRunDagUseCase.xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_14 # type: ignore # mutmut generated
mutants_xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut['xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_15'] = TracePipelineRunDagUseCase.xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_15 # type: ignore # mutmut generated
mutants_xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut['xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_16'] = TracePipelineRunDagUseCase.xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_16 # type: ignore # mutmut generated
mutants_xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut['xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_17'] = TracePipelineRunDagUseCase.xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_17 # type: ignore # mutmut generated
mutants_xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut['xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_18'] = TracePipelineRunDagUseCase.xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_18 # type: ignore # mutmut generated
mutants_xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut['xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_19'] = TracePipelineRunDagUseCase.xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_19 # type: ignore # mutmut generated
mutants_xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut['xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_20'] = TracePipelineRunDagUseCase.xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_20 # type: ignore # mutmut generated
mutants_xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut['xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_21'] = TracePipelineRunDagUseCase.xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_21 # type: ignore # mutmut generated
mutants_xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut['xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_22'] = TracePipelineRunDagUseCase.xǁTracePipelineRunDagUseCaseǁtrace_pipeline_run_dag__mutmut_22 # type: ignore # mutmut generated
