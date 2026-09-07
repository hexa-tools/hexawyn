from hexawyn.application.ports.driven.pipeline_baseline_port import PipelineBaselinePort
from hexawyn.application.use_case.pipelines.pipeline_performance_baseline.command import (
    PipelinePerformanceBaselineCommand,
)
from hexawyn.application.use_case.pipelines.pipeline_performance_baseline.response import (
    PipelinePerformanceBaselineResponse,
)
from hexawyn.domain.services.pipeline_baseline.cicd_performance_baseline_service import (
    compute_baseline,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁPipelinePerformanceBaselineUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class PipelinePerformanceBaselineUseCase:
    @_mutmut_mutated(mutants_xǁPipelinePerformanceBaselineUseCaseǁ__init____mutmut)
    def __init__(self, port: PipelineBaselinePort) -> None:
        self._port = port
    def xǁPipelinePerformanceBaselineUseCaseǁ__init____mutmut_orig(self, port: PipelineBaselinePort) -> None:
        self._port = port
    def xǁPipelinePerformanceBaselineUseCaseǁ__init____mutmut_1(self, port: PipelineBaselinePort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut)
    def execute(
        self, command: PipelinePerformanceBaselineCommand
    ) -> PipelinePerformanceBaselineResponse:
        try:
            pipeline_runs = self._port.list_pipeline_runs(
                command.pipeline_name,
                command.namespace,
                command.limit,
            )
            all_task_runs = []
            for run in pipeline_runs:
                try:
                    task_runs = self._port.list_task_runs_for_pipeline(
                        command.namespace,
                        run["name"],
                    )
                    all_task_runs.extend(task_runs)
                except Exception:
                    continue

            result = compute_baseline(
                command.pipeline_name,
                command.limit,  # type: ignore
                all_task_runs,
            )
            return PipelinePerformanceBaselineResponse.from_result(result)
        except Exception as exc:
            return PipelinePerformanceBaselineResponse(
                pipeline=command.pipeline_name,
                error=str(exc),
            )

    def xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_orig(
        self, command: PipelinePerformanceBaselineCommand
    ) -> PipelinePerformanceBaselineResponse:
        try:
            pipeline_runs = self._port.list_pipeline_runs(
                command.pipeline_name,
                command.namespace,
                command.limit,
            )
            all_task_runs = []
            for run in pipeline_runs:
                try:
                    task_runs = self._port.list_task_runs_for_pipeline(
                        command.namespace,
                        run["name"],
                    )
                    all_task_runs.extend(task_runs)
                except Exception:
                    continue

            result = compute_baseline(
                command.pipeline_name,
                command.limit,  # type: ignore
                all_task_runs,
            )
            return PipelinePerformanceBaselineResponse.from_result(result)
        except Exception as exc:
            return PipelinePerformanceBaselineResponse(
                pipeline=command.pipeline_name,
                error=str(exc),
            )

    def xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_1(
        self, command: PipelinePerformanceBaselineCommand
    ) -> PipelinePerformanceBaselineResponse:
        try:
            pipeline_runs = None
            all_task_runs = []
            for run in pipeline_runs:
                try:
                    task_runs = self._port.list_task_runs_for_pipeline(
                        command.namespace,
                        run["name"],
                    )
                    all_task_runs.extend(task_runs)
                except Exception:
                    continue

            result = compute_baseline(
                command.pipeline_name,
                command.limit,  # type: ignore
                all_task_runs,
            )
            return PipelinePerformanceBaselineResponse.from_result(result)
        except Exception as exc:
            return PipelinePerformanceBaselineResponse(
                pipeline=command.pipeline_name,
                error=str(exc),
            )

    def xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_2(
        self, command: PipelinePerformanceBaselineCommand
    ) -> PipelinePerformanceBaselineResponse:
        try:
            pipeline_runs = self._port.list_pipeline_runs(
                None,
                command.namespace,
                command.limit,
            )
            all_task_runs = []
            for run in pipeline_runs:
                try:
                    task_runs = self._port.list_task_runs_for_pipeline(
                        command.namespace,
                        run["name"],
                    )
                    all_task_runs.extend(task_runs)
                except Exception:
                    continue

            result = compute_baseline(
                command.pipeline_name,
                command.limit,  # type: ignore
                all_task_runs,
            )
            return PipelinePerformanceBaselineResponse.from_result(result)
        except Exception as exc:
            return PipelinePerformanceBaselineResponse(
                pipeline=command.pipeline_name,
                error=str(exc),
            )

    def xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_3(
        self, command: PipelinePerformanceBaselineCommand
    ) -> PipelinePerformanceBaselineResponse:
        try:
            pipeline_runs = self._port.list_pipeline_runs(
                command.pipeline_name,
                None,
                command.limit,
            )
            all_task_runs = []
            for run in pipeline_runs:
                try:
                    task_runs = self._port.list_task_runs_for_pipeline(
                        command.namespace,
                        run["name"],
                    )
                    all_task_runs.extend(task_runs)
                except Exception:
                    continue

            result = compute_baseline(
                command.pipeline_name,
                command.limit,  # type: ignore
                all_task_runs,
            )
            return PipelinePerformanceBaselineResponse.from_result(result)
        except Exception as exc:
            return PipelinePerformanceBaselineResponse(
                pipeline=command.pipeline_name,
                error=str(exc),
            )

    def xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_4(
        self, command: PipelinePerformanceBaselineCommand
    ) -> PipelinePerformanceBaselineResponse:
        try:
            pipeline_runs = self._port.list_pipeline_runs(
                command.pipeline_name,
                command.namespace,
                None,
            )
            all_task_runs = []
            for run in pipeline_runs:
                try:
                    task_runs = self._port.list_task_runs_for_pipeline(
                        command.namespace,
                        run["name"],
                    )
                    all_task_runs.extend(task_runs)
                except Exception:
                    continue

            result = compute_baseline(
                command.pipeline_name,
                command.limit,  # type: ignore
                all_task_runs,
            )
            return PipelinePerformanceBaselineResponse.from_result(result)
        except Exception as exc:
            return PipelinePerformanceBaselineResponse(
                pipeline=command.pipeline_name,
                error=str(exc),
            )

    def xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_5(
        self, command: PipelinePerformanceBaselineCommand
    ) -> PipelinePerformanceBaselineResponse:
        try:
            pipeline_runs = self._port.list_pipeline_runs(
                command.namespace,
                command.limit,
            )
            all_task_runs = []
            for run in pipeline_runs:
                try:
                    task_runs = self._port.list_task_runs_for_pipeline(
                        command.namespace,
                        run["name"],
                    )
                    all_task_runs.extend(task_runs)
                except Exception:
                    continue

            result = compute_baseline(
                command.pipeline_name,
                command.limit,  # type: ignore
                all_task_runs,
            )
            return PipelinePerformanceBaselineResponse.from_result(result)
        except Exception as exc:
            return PipelinePerformanceBaselineResponse(
                pipeline=command.pipeline_name,
                error=str(exc),
            )

    def xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_6(
        self, command: PipelinePerformanceBaselineCommand
    ) -> PipelinePerformanceBaselineResponse:
        try:
            pipeline_runs = self._port.list_pipeline_runs(
                command.pipeline_name,
                command.limit,
            )
            all_task_runs = []
            for run in pipeline_runs:
                try:
                    task_runs = self._port.list_task_runs_for_pipeline(
                        command.namespace,
                        run["name"],
                    )
                    all_task_runs.extend(task_runs)
                except Exception:
                    continue

            result = compute_baseline(
                command.pipeline_name,
                command.limit,  # type: ignore
                all_task_runs,
            )
            return PipelinePerformanceBaselineResponse.from_result(result)
        except Exception as exc:
            return PipelinePerformanceBaselineResponse(
                pipeline=command.pipeline_name,
                error=str(exc),
            )

    def xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_7(
        self, command: PipelinePerformanceBaselineCommand
    ) -> PipelinePerformanceBaselineResponse:
        try:
            pipeline_runs = self._port.list_pipeline_runs(
                command.pipeline_name,
                command.namespace,
                )
            all_task_runs = []
            for run in pipeline_runs:
                try:
                    task_runs = self._port.list_task_runs_for_pipeline(
                        command.namespace,
                        run["name"],
                    )
                    all_task_runs.extend(task_runs)
                except Exception:
                    continue

            result = compute_baseline(
                command.pipeline_name,
                command.limit,  # type: ignore
                all_task_runs,
            )
            return PipelinePerformanceBaselineResponse.from_result(result)
        except Exception as exc:
            return PipelinePerformanceBaselineResponse(
                pipeline=command.pipeline_name,
                error=str(exc),
            )

    def xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_8(
        self, command: PipelinePerformanceBaselineCommand
    ) -> PipelinePerformanceBaselineResponse:
        try:
            pipeline_runs = self._port.list_pipeline_runs(
                command.pipeline_name,
                command.namespace,
                command.limit,
            )
            all_task_runs = None
            for run in pipeline_runs:
                try:
                    task_runs = self._port.list_task_runs_for_pipeline(
                        command.namespace,
                        run["name"],
                    )
                    all_task_runs.extend(task_runs)
                except Exception:
                    continue

            result = compute_baseline(
                command.pipeline_name,
                command.limit,  # type: ignore
                all_task_runs,
            )
            return PipelinePerformanceBaselineResponse.from_result(result)
        except Exception as exc:
            return PipelinePerformanceBaselineResponse(
                pipeline=command.pipeline_name,
                error=str(exc),
            )

    def xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_9(
        self, command: PipelinePerformanceBaselineCommand
    ) -> PipelinePerformanceBaselineResponse:
        try:
            pipeline_runs = self._port.list_pipeline_runs(
                command.pipeline_name,
                command.namespace,
                command.limit,
            )
            all_task_runs = []
            for run in pipeline_runs:
                try:
                    task_runs = None
                    all_task_runs.extend(task_runs)
                except Exception:
                    continue

            result = compute_baseline(
                command.pipeline_name,
                command.limit,  # type: ignore
                all_task_runs,
            )
            return PipelinePerformanceBaselineResponse.from_result(result)
        except Exception as exc:
            return PipelinePerformanceBaselineResponse(
                pipeline=command.pipeline_name,
                error=str(exc),
            )

    def xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_10(
        self, command: PipelinePerformanceBaselineCommand
    ) -> PipelinePerformanceBaselineResponse:
        try:
            pipeline_runs = self._port.list_pipeline_runs(
                command.pipeline_name,
                command.namespace,
                command.limit,
            )
            all_task_runs = []
            for run in pipeline_runs:
                try:
                    task_runs = self._port.list_task_runs_for_pipeline(
                        None,
                        run["name"],
                    )
                    all_task_runs.extend(task_runs)
                except Exception:
                    continue

            result = compute_baseline(
                command.pipeline_name,
                command.limit,  # type: ignore
                all_task_runs,
            )
            return PipelinePerformanceBaselineResponse.from_result(result)
        except Exception as exc:
            return PipelinePerformanceBaselineResponse(
                pipeline=command.pipeline_name,
                error=str(exc),
            )

    def xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_11(
        self, command: PipelinePerformanceBaselineCommand
    ) -> PipelinePerformanceBaselineResponse:
        try:
            pipeline_runs = self._port.list_pipeline_runs(
                command.pipeline_name,
                command.namespace,
                command.limit,
            )
            all_task_runs = []
            for run in pipeline_runs:
                try:
                    task_runs = self._port.list_task_runs_for_pipeline(
                        command.namespace,
                        None,
                    )
                    all_task_runs.extend(task_runs)
                except Exception:
                    continue

            result = compute_baseline(
                command.pipeline_name,
                command.limit,  # type: ignore
                all_task_runs,
            )
            return PipelinePerformanceBaselineResponse.from_result(result)
        except Exception as exc:
            return PipelinePerformanceBaselineResponse(
                pipeline=command.pipeline_name,
                error=str(exc),
            )

    def xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_12(
        self, command: PipelinePerformanceBaselineCommand
    ) -> PipelinePerformanceBaselineResponse:
        try:
            pipeline_runs = self._port.list_pipeline_runs(
                command.pipeline_name,
                command.namespace,
                command.limit,
            )
            all_task_runs = []
            for run in pipeline_runs:
                try:
                    task_runs = self._port.list_task_runs_for_pipeline(
                        run["name"],
                    )
                    all_task_runs.extend(task_runs)
                except Exception:
                    continue

            result = compute_baseline(
                command.pipeline_name,
                command.limit,  # type: ignore
                all_task_runs,
            )
            return PipelinePerformanceBaselineResponse.from_result(result)
        except Exception as exc:
            return PipelinePerformanceBaselineResponse(
                pipeline=command.pipeline_name,
                error=str(exc),
            )

    def xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_13(
        self, command: PipelinePerformanceBaselineCommand
    ) -> PipelinePerformanceBaselineResponse:
        try:
            pipeline_runs = self._port.list_pipeline_runs(
                command.pipeline_name,
                command.namespace,
                command.limit,
            )
            all_task_runs = []
            for run in pipeline_runs:
                try:
                    task_runs = self._port.list_task_runs_for_pipeline(
                        command.namespace,
                        )
                    all_task_runs.extend(task_runs)
                except Exception:
                    continue

            result = compute_baseline(
                command.pipeline_name,
                command.limit,  # type: ignore
                all_task_runs,
            )
            return PipelinePerformanceBaselineResponse.from_result(result)
        except Exception as exc:
            return PipelinePerformanceBaselineResponse(
                pipeline=command.pipeline_name,
                error=str(exc),
            )

    def xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_14(
        self, command: PipelinePerformanceBaselineCommand
    ) -> PipelinePerformanceBaselineResponse:
        try:
            pipeline_runs = self._port.list_pipeline_runs(
                command.pipeline_name,
                command.namespace,
                command.limit,
            )
            all_task_runs = []
            for run in pipeline_runs:
                try:
                    task_runs = self._port.list_task_runs_for_pipeline(
                        command.namespace,
                        run["XXnameXX"],
                    )
                    all_task_runs.extend(task_runs)
                except Exception:
                    continue

            result = compute_baseline(
                command.pipeline_name,
                command.limit,  # type: ignore
                all_task_runs,
            )
            return PipelinePerformanceBaselineResponse.from_result(result)
        except Exception as exc:
            return PipelinePerformanceBaselineResponse(
                pipeline=command.pipeline_name,
                error=str(exc),
            )

    def xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_15(
        self, command: PipelinePerformanceBaselineCommand
    ) -> PipelinePerformanceBaselineResponse:
        try:
            pipeline_runs = self._port.list_pipeline_runs(
                command.pipeline_name,
                command.namespace,
                command.limit,
            )
            all_task_runs = []
            for run in pipeline_runs:
                try:
                    task_runs = self._port.list_task_runs_for_pipeline(
                        command.namespace,
                        run["NAME"],
                    )
                    all_task_runs.extend(task_runs)
                except Exception:
                    continue

            result = compute_baseline(
                command.pipeline_name,
                command.limit,  # type: ignore
                all_task_runs,
            )
            return PipelinePerformanceBaselineResponse.from_result(result)
        except Exception as exc:
            return PipelinePerformanceBaselineResponse(
                pipeline=command.pipeline_name,
                error=str(exc),
            )

    def xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_16(
        self, command: PipelinePerformanceBaselineCommand
    ) -> PipelinePerformanceBaselineResponse:
        try:
            pipeline_runs = self._port.list_pipeline_runs(
                command.pipeline_name,
                command.namespace,
                command.limit,
            )
            all_task_runs = []
            for run in pipeline_runs:
                try:
                    task_runs = self._port.list_task_runs_for_pipeline(
                        command.namespace,
                        run["name"],
                    )
                    all_task_runs.extend(None)
                except Exception:
                    continue

            result = compute_baseline(
                command.pipeline_name,
                command.limit,  # type: ignore
                all_task_runs,
            )
            return PipelinePerformanceBaselineResponse.from_result(result)
        except Exception as exc:
            return PipelinePerformanceBaselineResponse(
                pipeline=command.pipeline_name,
                error=str(exc),
            )

    def xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_17(
        self, command: PipelinePerformanceBaselineCommand
    ) -> PipelinePerformanceBaselineResponse:
        try:
            pipeline_runs = self._port.list_pipeline_runs(
                command.pipeline_name,
                command.namespace,
                command.limit,
            )
            all_task_runs = []
            for run in pipeline_runs:
                try:
                    task_runs = self._port.list_task_runs_for_pipeline(
                        command.namespace,
                        run["name"],
                    )
                    all_task_runs.extend(task_runs)
                except Exception:
                    break

            result = compute_baseline(
                command.pipeline_name,
                command.limit,  # type: ignore
                all_task_runs,
            )
            return PipelinePerformanceBaselineResponse.from_result(result)
        except Exception as exc:
            return PipelinePerformanceBaselineResponse(
                pipeline=command.pipeline_name,
                error=str(exc),
            )

    def xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_18(
        self, command: PipelinePerformanceBaselineCommand
    ) -> PipelinePerformanceBaselineResponse:
        try:
            pipeline_runs = self._port.list_pipeline_runs(
                command.pipeline_name,
                command.namespace,
                command.limit,
            )
            all_task_runs = []
            for run in pipeline_runs:
                try:
                    task_runs = self._port.list_task_runs_for_pipeline(
                        command.namespace,
                        run["name"],
                    )
                    all_task_runs.extend(task_runs)
                except Exception:
                    continue

            result = None
            return PipelinePerformanceBaselineResponse.from_result(result)
        except Exception as exc:
            return PipelinePerformanceBaselineResponse(
                pipeline=command.pipeline_name,
                error=str(exc),
            )

    def xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_19(
        self, command: PipelinePerformanceBaselineCommand
    ) -> PipelinePerformanceBaselineResponse:
        try:
            pipeline_runs = self._port.list_pipeline_runs(
                command.pipeline_name,
                command.namespace,
                command.limit,
            )
            all_task_runs = []
            for run in pipeline_runs:
                try:
                    task_runs = self._port.list_task_runs_for_pipeline(
                        command.namespace,
                        run["name"],
                    )
                    all_task_runs.extend(task_runs)
                except Exception:
                    continue

            result = compute_baseline(
                None,
                command.limit,  # type: ignore
                all_task_runs,
            )
            return PipelinePerformanceBaselineResponse.from_result(result)
        except Exception as exc:
            return PipelinePerformanceBaselineResponse(
                pipeline=command.pipeline_name,
                error=str(exc),
            )

    def xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_20(
        self, command: PipelinePerformanceBaselineCommand
    ) -> PipelinePerformanceBaselineResponse:
        try:
            pipeline_runs = self._port.list_pipeline_runs(
                command.pipeline_name,
                command.namespace,
                command.limit,
            )
            all_task_runs = []
            for run in pipeline_runs:
                try:
                    task_runs = self._port.list_task_runs_for_pipeline(
                        command.namespace,
                        run["name"],
                    )
                    all_task_runs.extend(task_runs)
                except Exception:
                    continue

            result = compute_baseline(
                command.pipeline_name,
                None,  # type: ignore
                all_task_runs,
            )
            return PipelinePerformanceBaselineResponse.from_result(result)
        except Exception as exc:
            return PipelinePerformanceBaselineResponse(
                pipeline=command.pipeline_name,
                error=str(exc),
            )

    def xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_21(
        self, command: PipelinePerformanceBaselineCommand
    ) -> PipelinePerformanceBaselineResponse:
        try:
            pipeline_runs = self._port.list_pipeline_runs(
                command.pipeline_name,
                command.namespace,
                command.limit,
            )
            all_task_runs = []
            for run in pipeline_runs:
                try:
                    task_runs = self._port.list_task_runs_for_pipeline(
                        command.namespace,
                        run["name"],
                    )
                    all_task_runs.extend(task_runs)
                except Exception:
                    continue

            result = compute_baseline(
                command.pipeline_name,
                command.limit,  # type: ignore
                None,
            )
            return PipelinePerformanceBaselineResponse.from_result(result)
        except Exception as exc:
            return PipelinePerformanceBaselineResponse(
                pipeline=command.pipeline_name,
                error=str(exc),
            )

    def xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_22(
        self, command: PipelinePerformanceBaselineCommand
    ) -> PipelinePerformanceBaselineResponse:
        try:
            pipeline_runs = self._port.list_pipeline_runs(
                command.pipeline_name,
                command.namespace,
                command.limit,
            )
            all_task_runs = []
            for run in pipeline_runs:
                try:
                    task_runs = self._port.list_task_runs_for_pipeline(
                        command.namespace,
                        run["name"],
                    )
                    all_task_runs.extend(task_runs)
                except Exception:
                    continue

            result = compute_baseline(
                command.limit,  # type: ignore
                all_task_runs,
            )
            return PipelinePerformanceBaselineResponse.from_result(result)
        except Exception as exc:
            return PipelinePerformanceBaselineResponse(
                pipeline=command.pipeline_name,
                error=str(exc),
            )

    def xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_23(
        self, command: PipelinePerformanceBaselineCommand
    ) -> PipelinePerformanceBaselineResponse:
        try:
            pipeline_runs = self._port.list_pipeline_runs(
                command.pipeline_name,
                command.namespace,
                command.limit,
            )
            all_task_runs = []
            for run in pipeline_runs:
                try:
                    task_runs = self._port.list_task_runs_for_pipeline(
                        command.namespace,
                        run["name"],
                    )
                    all_task_runs.extend(task_runs)
                except Exception:
                    continue

            result = compute_baseline(
                command.pipeline_name,
                all_task_runs,
            )
            return PipelinePerformanceBaselineResponse.from_result(result)
        except Exception as exc:
            return PipelinePerformanceBaselineResponse(
                pipeline=command.pipeline_name,
                error=str(exc),
            )

    def xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_24(
        self, command: PipelinePerformanceBaselineCommand
    ) -> PipelinePerformanceBaselineResponse:
        try:
            pipeline_runs = self._port.list_pipeline_runs(
                command.pipeline_name,
                command.namespace,
                command.limit,
            )
            all_task_runs = []
            for run in pipeline_runs:
                try:
                    task_runs = self._port.list_task_runs_for_pipeline(
                        command.namespace,
                        run["name"],
                    )
                    all_task_runs.extend(task_runs)
                except Exception:
                    continue

            result = compute_baseline(
                command.pipeline_name,
                command.limit,  # type: ignore
                )
            return PipelinePerformanceBaselineResponse.from_result(result)
        except Exception as exc:
            return PipelinePerformanceBaselineResponse(
                pipeline=command.pipeline_name,
                error=str(exc),
            )

    def xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_25(
        self, command: PipelinePerformanceBaselineCommand
    ) -> PipelinePerformanceBaselineResponse:
        try:
            pipeline_runs = self._port.list_pipeline_runs(
                command.pipeline_name,
                command.namespace,
                command.limit,
            )
            all_task_runs = []
            for run in pipeline_runs:
                try:
                    task_runs = self._port.list_task_runs_for_pipeline(
                        command.namespace,
                        run["name"],
                    )
                    all_task_runs.extend(task_runs)
                except Exception:
                    continue

            result = compute_baseline(
                command.pipeline_name,
                command.limit,  # type: ignore
                all_task_runs,
            )
            return PipelinePerformanceBaselineResponse.from_result(None)
        except Exception as exc:
            return PipelinePerformanceBaselineResponse(
                pipeline=command.pipeline_name,
                error=str(exc),
            )

    def xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_26(
        self, command: PipelinePerformanceBaselineCommand
    ) -> PipelinePerformanceBaselineResponse:
        try:
            pipeline_runs = self._port.list_pipeline_runs(
                command.pipeline_name,
                command.namespace,
                command.limit,
            )
            all_task_runs = []
            for run in pipeline_runs:
                try:
                    task_runs = self._port.list_task_runs_for_pipeline(
                        command.namespace,
                        run["name"],
                    )
                    all_task_runs.extend(task_runs)
                except Exception:
                    continue

            result = compute_baseline(
                command.pipeline_name,
                command.limit,  # type: ignore
                all_task_runs,
            )
            return PipelinePerformanceBaselineResponse.from_result(result)
        except Exception as exc:
            return PipelinePerformanceBaselineResponse(
                pipeline=None,
                error=str(exc),
            )

    def xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_27(
        self, command: PipelinePerformanceBaselineCommand
    ) -> PipelinePerformanceBaselineResponse:
        try:
            pipeline_runs = self._port.list_pipeline_runs(
                command.pipeline_name,
                command.namespace,
                command.limit,
            )
            all_task_runs = []
            for run in pipeline_runs:
                try:
                    task_runs = self._port.list_task_runs_for_pipeline(
                        command.namespace,
                        run["name"],
                    )
                    all_task_runs.extend(task_runs)
                except Exception:
                    continue

            result = compute_baseline(
                command.pipeline_name,
                command.limit,  # type: ignore
                all_task_runs,
            )
            return PipelinePerformanceBaselineResponse.from_result(result)
        except Exception as exc:
            return PipelinePerformanceBaselineResponse(
                pipeline=command.pipeline_name,
                error=None,
            )

    def xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_28(
        self, command: PipelinePerformanceBaselineCommand
    ) -> PipelinePerformanceBaselineResponse:
        try:
            pipeline_runs = self._port.list_pipeline_runs(
                command.pipeline_name,
                command.namespace,
                command.limit,
            )
            all_task_runs = []
            for run in pipeline_runs:
                try:
                    task_runs = self._port.list_task_runs_for_pipeline(
                        command.namespace,
                        run["name"],
                    )
                    all_task_runs.extend(task_runs)
                except Exception:
                    continue

            result = compute_baseline(
                command.pipeline_name,
                command.limit,  # type: ignore
                all_task_runs,
            )
            return PipelinePerformanceBaselineResponse.from_result(result)
        except Exception as exc:
            return PipelinePerformanceBaselineResponse(
                error=str(exc),
            )

    def xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_29(
        self, command: PipelinePerformanceBaselineCommand
    ) -> PipelinePerformanceBaselineResponse:
        try:
            pipeline_runs = self._port.list_pipeline_runs(
                command.pipeline_name,
                command.namespace,
                command.limit,
            )
            all_task_runs = []
            for run in pipeline_runs:
                try:
                    task_runs = self._port.list_task_runs_for_pipeline(
                        command.namespace,
                        run["name"],
                    )
                    all_task_runs.extend(task_runs)
                except Exception:
                    continue

            result = compute_baseline(
                command.pipeline_name,
                command.limit,  # type: ignore
                all_task_runs,
            )
            return PipelinePerformanceBaselineResponse.from_result(result)
        except Exception as exc:
            return PipelinePerformanceBaselineResponse(
                pipeline=command.pipeline_name,
                )

    def xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_30(
        self, command: PipelinePerformanceBaselineCommand
    ) -> PipelinePerformanceBaselineResponse:
        try:
            pipeline_runs = self._port.list_pipeline_runs(
                command.pipeline_name,
                command.namespace,
                command.limit,
            )
            all_task_runs = []
            for run in pipeline_runs:
                try:
                    task_runs = self._port.list_task_runs_for_pipeline(
                        command.namespace,
                        run["name"],
                    )
                    all_task_runs.extend(task_runs)
                except Exception:
                    continue

            result = compute_baseline(
                command.pipeline_name,
                command.limit,  # type: ignore
                all_task_runs,
            )
            return PipelinePerformanceBaselineResponse.from_result(result)
        except Exception as exc:
            return PipelinePerformanceBaselineResponse(
                pipeline=command.pipeline_name,
                error=str(None),
            )

mutants_xǁPipelinePerformanceBaselineUseCaseǁ__init____mutmut['_mutmut_orig'] = PipelinePerformanceBaselineUseCase.xǁPipelinePerformanceBaselineUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁPipelinePerformanceBaselineUseCaseǁ__init____mutmut['xǁPipelinePerformanceBaselineUseCaseǁ__init____mutmut_1'] = PipelinePerformanceBaselineUseCase.xǁPipelinePerformanceBaselineUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut['_mutmut_orig'] = PipelinePerformanceBaselineUseCase.xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut['xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_1'] = PipelinePerformanceBaselineUseCase.xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut['xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_2'] = PipelinePerformanceBaselineUseCase.xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut['xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_3'] = PipelinePerformanceBaselineUseCase.xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut['xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_4'] = PipelinePerformanceBaselineUseCase.xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut['xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_5'] = PipelinePerformanceBaselineUseCase.xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut['xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_6'] = PipelinePerformanceBaselineUseCase.xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut['xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_7'] = PipelinePerformanceBaselineUseCase.xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut['xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_8'] = PipelinePerformanceBaselineUseCase.xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut['xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_9'] = PipelinePerformanceBaselineUseCase.xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut['xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_10'] = PipelinePerformanceBaselineUseCase.xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut['xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_11'] = PipelinePerformanceBaselineUseCase.xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut['xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_12'] = PipelinePerformanceBaselineUseCase.xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut['xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_13'] = PipelinePerformanceBaselineUseCase.xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut['xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_14'] = PipelinePerformanceBaselineUseCase.xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut['xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_15'] = PipelinePerformanceBaselineUseCase.xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut['xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_16'] = PipelinePerformanceBaselineUseCase.xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut['xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_17'] = PipelinePerformanceBaselineUseCase.xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut['xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_18'] = PipelinePerformanceBaselineUseCase.xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut['xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_19'] = PipelinePerformanceBaselineUseCase.xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut['xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_20'] = PipelinePerformanceBaselineUseCase.xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut['xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_21'] = PipelinePerformanceBaselineUseCase.xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut['xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_22'] = PipelinePerformanceBaselineUseCase.xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut['xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_23'] = PipelinePerformanceBaselineUseCase.xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut['xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_24'] = PipelinePerformanceBaselineUseCase.xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut['xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_25'] = PipelinePerformanceBaselineUseCase.xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut['xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_26'] = PipelinePerformanceBaselineUseCase.xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut['xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_27'] = PipelinePerformanceBaselineUseCase.xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut['xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_28'] = PipelinePerformanceBaselineUseCase.xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut['xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_29'] = PipelinePerformanceBaselineUseCase.xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut['xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_30'] = PipelinePerformanceBaselineUseCase.xǁPipelinePerformanceBaselineUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
