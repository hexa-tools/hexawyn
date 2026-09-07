from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.pipeline_run_logs_port import PipelineRunLogsPort
from hexawyn.application.use_case.pipelines.pipeline_run_logs.command import (
    PipelineRunLogsCommand,
)
from hexawyn.application.use_case.pipelines.pipeline_run_logs.response import (
    PipelineRunLogsResponse,
)
from hexawyn.domain.models.pipeline_run_logs import PipelineRunLogsRequest, PipelineRunLogsResult


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁPipelineRunLogsUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁPipelineRunLogsUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class PipelineRunLogsUseCase:
    @_mutmut_mutated(mutants_xǁPipelineRunLogsUseCaseǁ__init____mutmut)
    def __init__(self, port: PipelineRunLogsPort) -> None:
        self._port = port
    def xǁPipelineRunLogsUseCaseǁ__init____mutmut_orig(self, port: PipelineRunLogsPort) -> None:
        self._port = port
    def xǁPipelineRunLogsUseCaseǁ__init____mutmut_1(self, port: PipelineRunLogsPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁPipelineRunLogsUseCaseǁexecute__mutmut)
    def execute(self, command: PipelineRunLogsCommand) -> PipelineRunLogsResponse:
        req = PipelineRunLogsRequest(
            pipeline_run_name=command.pipeline_run_name, namespace=command.namespace
        )
        steps = self._port.fetch_step_logs(req)
        r = PipelineRunLogsResult.compute(request=req, steps=steps)
        return PipelineRunLogsResponse(
            pipeline_run_name=r.pipeline_run_name,
            namespace=r.namespace,
            pipeline_run_found=r.pipeline_run_found,
            is_still_running=r.is_still_running,
            failed_step_count=r.failed_step_count,
            total_step_count=r.total_step_count,
            steps=[asdict(s) for s in r.steps],
        )

    def xǁPipelineRunLogsUseCaseǁexecute__mutmut_orig(self, command: PipelineRunLogsCommand) -> PipelineRunLogsResponse:
        req = PipelineRunLogsRequest(
            pipeline_run_name=command.pipeline_run_name, namespace=command.namespace
        )
        steps = self._port.fetch_step_logs(req)
        r = PipelineRunLogsResult.compute(request=req, steps=steps)
        return PipelineRunLogsResponse(
            pipeline_run_name=r.pipeline_run_name,
            namespace=r.namespace,
            pipeline_run_found=r.pipeline_run_found,
            is_still_running=r.is_still_running,
            failed_step_count=r.failed_step_count,
            total_step_count=r.total_step_count,
            steps=[asdict(s) for s in r.steps],
        )

    def xǁPipelineRunLogsUseCaseǁexecute__mutmut_1(self, command: PipelineRunLogsCommand) -> PipelineRunLogsResponse:
        req = None
        steps = self._port.fetch_step_logs(req)
        r = PipelineRunLogsResult.compute(request=req, steps=steps)
        return PipelineRunLogsResponse(
            pipeline_run_name=r.pipeline_run_name,
            namespace=r.namespace,
            pipeline_run_found=r.pipeline_run_found,
            is_still_running=r.is_still_running,
            failed_step_count=r.failed_step_count,
            total_step_count=r.total_step_count,
            steps=[asdict(s) for s in r.steps],
        )

    def xǁPipelineRunLogsUseCaseǁexecute__mutmut_2(self, command: PipelineRunLogsCommand) -> PipelineRunLogsResponse:
        req = PipelineRunLogsRequest(
            pipeline_run_name=None, namespace=command.namespace
        )
        steps = self._port.fetch_step_logs(req)
        r = PipelineRunLogsResult.compute(request=req, steps=steps)
        return PipelineRunLogsResponse(
            pipeline_run_name=r.pipeline_run_name,
            namespace=r.namespace,
            pipeline_run_found=r.pipeline_run_found,
            is_still_running=r.is_still_running,
            failed_step_count=r.failed_step_count,
            total_step_count=r.total_step_count,
            steps=[asdict(s) for s in r.steps],
        )

    def xǁPipelineRunLogsUseCaseǁexecute__mutmut_3(self, command: PipelineRunLogsCommand) -> PipelineRunLogsResponse:
        req = PipelineRunLogsRequest(
            pipeline_run_name=command.pipeline_run_name, namespace=None
        )
        steps = self._port.fetch_step_logs(req)
        r = PipelineRunLogsResult.compute(request=req, steps=steps)
        return PipelineRunLogsResponse(
            pipeline_run_name=r.pipeline_run_name,
            namespace=r.namespace,
            pipeline_run_found=r.pipeline_run_found,
            is_still_running=r.is_still_running,
            failed_step_count=r.failed_step_count,
            total_step_count=r.total_step_count,
            steps=[asdict(s) for s in r.steps],
        )

    def xǁPipelineRunLogsUseCaseǁexecute__mutmut_4(self, command: PipelineRunLogsCommand) -> PipelineRunLogsResponse:
        req = PipelineRunLogsRequest(
            namespace=command.namespace
        )
        steps = self._port.fetch_step_logs(req)
        r = PipelineRunLogsResult.compute(request=req, steps=steps)
        return PipelineRunLogsResponse(
            pipeline_run_name=r.pipeline_run_name,
            namespace=r.namespace,
            pipeline_run_found=r.pipeline_run_found,
            is_still_running=r.is_still_running,
            failed_step_count=r.failed_step_count,
            total_step_count=r.total_step_count,
            steps=[asdict(s) for s in r.steps],
        )

    def xǁPipelineRunLogsUseCaseǁexecute__mutmut_5(self, command: PipelineRunLogsCommand) -> PipelineRunLogsResponse:
        req = PipelineRunLogsRequest(
            pipeline_run_name=command.pipeline_run_name, )
        steps = self._port.fetch_step_logs(req)
        r = PipelineRunLogsResult.compute(request=req, steps=steps)
        return PipelineRunLogsResponse(
            pipeline_run_name=r.pipeline_run_name,
            namespace=r.namespace,
            pipeline_run_found=r.pipeline_run_found,
            is_still_running=r.is_still_running,
            failed_step_count=r.failed_step_count,
            total_step_count=r.total_step_count,
            steps=[asdict(s) for s in r.steps],
        )

    def xǁPipelineRunLogsUseCaseǁexecute__mutmut_6(self, command: PipelineRunLogsCommand) -> PipelineRunLogsResponse:
        req = PipelineRunLogsRequest(
            pipeline_run_name=command.pipeline_run_name, namespace=command.namespace
        )
        steps = None
        r = PipelineRunLogsResult.compute(request=req, steps=steps)
        return PipelineRunLogsResponse(
            pipeline_run_name=r.pipeline_run_name,
            namespace=r.namespace,
            pipeline_run_found=r.pipeline_run_found,
            is_still_running=r.is_still_running,
            failed_step_count=r.failed_step_count,
            total_step_count=r.total_step_count,
            steps=[asdict(s) for s in r.steps],
        )

    def xǁPipelineRunLogsUseCaseǁexecute__mutmut_7(self, command: PipelineRunLogsCommand) -> PipelineRunLogsResponse:
        req = PipelineRunLogsRequest(
            pipeline_run_name=command.pipeline_run_name, namespace=command.namespace
        )
        steps = self._port.fetch_step_logs(None)
        r = PipelineRunLogsResult.compute(request=req, steps=steps)
        return PipelineRunLogsResponse(
            pipeline_run_name=r.pipeline_run_name,
            namespace=r.namespace,
            pipeline_run_found=r.pipeline_run_found,
            is_still_running=r.is_still_running,
            failed_step_count=r.failed_step_count,
            total_step_count=r.total_step_count,
            steps=[asdict(s) for s in r.steps],
        )

    def xǁPipelineRunLogsUseCaseǁexecute__mutmut_8(self, command: PipelineRunLogsCommand) -> PipelineRunLogsResponse:
        req = PipelineRunLogsRequest(
            pipeline_run_name=command.pipeline_run_name, namespace=command.namespace
        )
        steps = self._port.fetch_step_logs(req)
        r = None
        return PipelineRunLogsResponse(
            pipeline_run_name=r.pipeline_run_name,
            namespace=r.namespace,
            pipeline_run_found=r.pipeline_run_found,
            is_still_running=r.is_still_running,
            failed_step_count=r.failed_step_count,
            total_step_count=r.total_step_count,
            steps=[asdict(s) for s in r.steps],
        )

    def xǁPipelineRunLogsUseCaseǁexecute__mutmut_9(self, command: PipelineRunLogsCommand) -> PipelineRunLogsResponse:
        req = PipelineRunLogsRequest(
            pipeline_run_name=command.pipeline_run_name, namespace=command.namespace
        )
        steps = self._port.fetch_step_logs(req)
        r = PipelineRunLogsResult.compute(request=None, steps=steps)
        return PipelineRunLogsResponse(
            pipeline_run_name=r.pipeline_run_name,
            namespace=r.namespace,
            pipeline_run_found=r.pipeline_run_found,
            is_still_running=r.is_still_running,
            failed_step_count=r.failed_step_count,
            total_step_count=r.total_step_count,
            steps=[asdict(s) for s in r.steps],
        )

    def xǁPipelineRunLogsUseCaseǁexecute__mutmut_10(self, command: PipelineRunLogsCommand) -> PipelineRunLogsResponse:
        req = PipelineRunLogsRequest(
            pipeline_run_name=command.pipeline_run_name, namespace=command.namespace
        )
        steps = self._port.fetch_step_logs(req)
        r = PipelineRunLogsResult.compute(request=req, steps=None)
        return PipelineRunLogsResponse(
            pipeline_run_name=r.pipeline_run_name,
            namespace=r.namespace,
            pipeline_run_found=r.pipeline_run_found,
            is_still_running=r.is_still_running,
            failed_step_count=r.failed_step_count,
            total_step_count=r.total_step_count,
            steps=[asdict(s) for s in r.steps],
        )

    def xǁPipelineRunLogsUseCaseǁexecute__mutmut_11(self, command: PipelineRunLogsCommand) -> PipelineRunLogsResponse:
        req = PipelineRunLogsRequest(
            pipeline_run_name=command.pipeline_run_name, namespace=command.namespace
        )
        steps = self._port.fetch_step_logs(req)
        r = PipelineRunLogsResult.compute(steps=steps)
        return PipelineRunLogsResponse(
            pipeline_run_name=r.pipeline_run_name,
            namespace=r.namespace,
            pipeline_run_found=r.pipeline_run_found,
            is_still_running=r.is_still_running,
            failed_step_count=r.failed_step_count,
            total_step_count=r.total_step_count,
            steps=[asdict(s) for s in r.steps],
        )

    def xǁPipelineRunLogsUseCaseǁexecute__mutmut_12(self, command: PipelineRunLogsCommand) -> PipelineRunLogsResponse:
        req = PipelineRunLogsRequest(
            pipeline_run_name=command.pipeline_run_name, namespace=command.namespace
        )
        steps = self._port.fetch_step_logs(req)
        r = PipelineRunLogsResult.compute(request=req, )
        return PipelineRunLogsResponse(
            pipeline_run_name=r.pipeline_run_name,
            namespace=r.namespace,
            pipeline_run_found=r.pipeline_run_found,
            is_still_running=r.is_still_running,
            failed_step_count=r.failed_step_count,
            total_step_count=r.total_step_count,
            steps=[asdict(s) for s in r.steps],
        )

    def xǁPipelineRunLogsUseCaseǁexecute__mutmut_13(self, command: PipelineRunLogsCommand) -> PipelineRunLogsResponse:
        req = PipelineRunLogsRequest(
            pipeline_run_name=command.pipeline_run_name, namespace=command.namespace
        )
        steps = self._port.fetch_step_logs(req)
        r = PipelineRunLogsResult.compute(request=req, steps=steps)
        return PipelineRunLogsResponse(
            pipeline_run_name=None,
            namespace=r.namespace,
            pipeline_run_found=r.pipeline_run_found,
            is_still_running=r.is_still_running,
            failed_step_count=r.failed_step_count,
            total_step_count=r.total_step_count,
            steps=[asdict(s) for s in r.steps],
        )

    def xǁPipelineRunLogsUseCaseǁexecute__mutmut_14(self, command: PipelineRunLogsCommand) -> PipelineRunLogsResponse:
        req = PipelineRunLogsRequest(
            pipeline_run_name=command.pipeline_run_name, namespace=command.namespace
        )
        steps = self._port.fetch_step_logs(req)
        r = PipelineRunLogsResult.compute(request=req, steps=steps)
        return PipelineRunLogsResponse(
            pipeline_run_name=r.pipeline_run_name,
            namespace=None,
            pipeline_run_found=r.pipeline_run_found,
            is_still_running=r.is_still_running,
            failed_step_count=r.failed_step_count,
            total_step_count=r.total_step_count,
            steps=[asdict(s) for s in r.steps],
        )

    def xǁPipelineRunLogsUseCaseǁexecute__mutmut_15(self, command: PipelineRunLogsCommand) -> PipelineRunLogsResponse:
        req = PipelineRunLogsRequest(
            pipeline_run_name=command.pipeline_run_name, namespace=command.namespace
        )
        steps = self._port.fetch_step_logs(req)
        r = PipelineRunLogsResult.compute(request=req, steps=steps)
        return PipelineRunLogsResponse(
            pipeline_run_name=r.pipeline_run_name,
            namespace=r.namespace,
            pipeline_run_found=None,
            is_still_running=r.is_still_running,
            failed_step_count=r.failed_step_count,
            total_step_count=r.total_step_count,
            steps=[asdict(s) for s in r.steps],
        )

    def xǁPipelineRunLogsUseCaseǁexecute__mutmut_16(self, command: PipelineRunLogsCommand) -> PipelineRunLogsResponse:
        req = PipelineRunLogsRequest(
            pipeline_run_name=command.pipeline_run_name, namespace=command.namespace
        )
        steps = self._port.fetch_step_logs(req)
        r = PipelineRunLogsResult.compute(request=req, steps=steps)
        return PipelineRunLogsResponse(
            pipeline_run_name=r.pipeline_run_name,
            namespace=r.namespace,
            pipeline_run_found=r.pipeline_run_found,
            is_still_running=None,
            failed_step_count=r.failed_step_count,
            total_step_count=r.total_step_count,
            steps=[asdict(s) for s in r.steps],
        )

    def xǁPipelineRunLogsUseCaseǁexecute__mutmut_17(self, command: PipelineRunLogsCommand) -> PipelineRunLogsResponse:
        req = PipelineRunLogsRequest(
            pipeline_run_name=command.pipeline_run_name, namespace=command.namespace
        )
        steps = self._port.fetch_step_logs(req)
        r = PipelineRunLogsResult.compute(request=req, steps=steps)
        return PipelineRunLogsResponse(
            pipeline_run_name=r.pipeline_run_name,
            namespace=r.namespace,
            pipeline_run_found=r.pipeline_run_found,
            is_still_running=r.is_still_running,
            failed_step_count=None,
            total_step_count=r.total_step_count,
            steps=[asdict(s) for s in r.steps],
        )

    def xǁPipelineRunLogsUseCaseǁexecute__mutmut_18(self, command: PipelineRunLogsCommand) -> PipelineRunLogsResponse:
        req = PipelineRunLogsRequest(
            pipeline_run_name=command.pipeline_run_name, namespace=command.namespace
        )
        steps = self._port.fetch_step_logs(req)
        r = PipelineRunLogsResult.compute(request=req, steps=steps)
        return PipelineRunLogsResponse(
            pipeline_run_name=r.pipeline_run_name,
            namespace=r.namespace,
            pipeline_run_found=r.pipeline_run_found,
            is_still_running=r.is_still_running,
            failed_step_count=r.failed_step_count,
            total_step_count=None,
            steps=[asdict(s) for s in r.steps],
        )

    def xǁPipelineRunLogsUseCaseǁexecute__mutmut_19(self, command: PipelineRunLogsCommand) -> PipelineRunLogsResponse:
        req = PipelineRunLogsRequest(
            pipeline_run_name=command.pipeline_run_name, namespace=command.namespace
        )
        steps = self._port.fetch_step_logs(req)
        r = PipelineRunLogsResult.compute(request=req, steps=steps)
        return PipelineRunLogsResponse(
            pipeline_run_name=r.pipeline_run_name,
            namespace=r.namespace,
            pipeline_run_found=r.pipeline_run_found,
            is_still_running=r.is_still_running,
            failed_step_count=r.failed_step_count,
            total_step_count=r.total_step_count,
            steps=None,
        )

    def xǁPipelineRunLogsUseCaseǁexecute__mutmut_20(self, command: PipelineRunLogsCommand) -> PipelineRunLogsResponse:
        req = PipelineRunLogsRequest(
            pipeline_run_name=command.pipeline_run_name, namespace=command.namespace
        )
        steps = self._port.fetch_step_logs(req)
        r = PipelineRunLogsResult.compute(request=req, steps=steps)
        return PipelineRunLogsResponse(
            namespace=r.namespace,
            pipeline_run_found=r.pipeline_run_found,
            is_still_running=r.is_still_running,
            failed_step_count=r.failed_step_count,
            total_step_count=r.total_step_count,
            steps=[asdict(s) for s in r.steps],
        )

    def xǁPipelineRunLogsUseCaseǁexecute__mutmut_21(self, command: PipelineRunLogsCommand) -> PipelineRunLogsResponse:
        req = PipelineRunLogsRequest(
            pipeline_run_name=command.pipeline_run_name, namespace=command.namespace
        )
        steps = self._port.fetch_step_logs(req)
        r = PipelineRunLogsResult.compute(request=req, steps=steps)
        return PipelineRunLogsResponse(
            pipeline_run_name=r.pipeline_run_name,
            pipeline_run_found=r.pipeline_run_found,
            is_still_running=r.is_still_running,
            failed_step_count=r.failed_step_count,
            total_step_count=r.total_step_count,
            steps=[asdict(s) for s in r.steps],
        )

    def xǁPipelineRunLogsUseCaseǁexecute__mutmut_22(self, command: PipelineRunLogsCommand) -> PipelineRunLogsResponse:
        req = PipelineRunLogsRequest(
            pipeline_run_name=command.pipeline_run_name, namespace=command.namespace
        )
        steps = self._port.fetch_step_logs(req)
        r = PipelineRunLogsResult.compute(request=req, steps=steps)
        return PipelineRunLogsResponse(
            pipeline_run_name=r.pipeline_run_name,
            namespace=r.namespace,
            is_still_running=r.is_still_running,
            failed_step_count=r.failed_step_count,
            total_step_count=r.total_step_count,
            steps=[asdict(s) for s in r.steps],
        )

    def xǁPipelineRunLogsUseCaseǁexecute__mutmut_23(self, command: PipelineRunLogsCommand) -> PipelineRunLogsResponse:
        req = PipelineRunLogsRequest(
            pipeline_run_name=command.pipeline_run_name, namespace=command.namespace
        )
        steps = self._port.fetch_step_logs(req)
        r = PipelineRunLogsResult.compute(request=req, steps=steps)
        return PipelineRunLogsResponse(
            pipeline_run_name=r.pipeline_run_name,
            namespace=r.namespace,
            pipeline_run_found=r.pipeline_run_found,
            failed_step_count=r.failed_step_count,
            total_step_count=r.total_step_count,
            steps=[asdict(s) for s in r.steps],
        )

    def xǁPipelineRunLogsUseCaseǁexecute__mutmut_24(self, command: PipelineRunLogsCommand) -> PipelineRunLogsResponse:
        req = PipelineRunLogsRequest(
            pipeline_run_name=command.pipeline_run_name, namespace=command.namespace
        )
        steps = self._port.fetch_step_logs(req)
        r = PipelineRunLogsResult.compute(request=req, steps=steps)
        return PipelineRunLogsResponse(
            pipeline_run_name=r.pipeline_run_name,
            namespace=r.namespace,
            pipeline_run_found=r.pipeline_run_found,
            is_still_running=r.is_still_running,
            total_step_count=r.total_step_count,
            steps=[asdict(s) for s in r.steps],
        )

    def xǁPipelineRunLogsUseCaseǁexecute__mutmut_25(self, command: PipelineRunLogsCommand) -> PipelineRunLogsResponse:
        req = PipelineRunLogsRequest(
            pipeline_run_name=command.pipeline_run_name, namespace=command.namespace
        )
        steps = self._port.fetch_step_logs(req)
        r = PipelineRunLogsResult.compute(request=req, steps=steps)
        return PipelineRunLogsResponse(
            pipeline_run_name=r.pipeline_run_name,
            namespace=r.namespace,
            pipeline_run_found=r.pipeline_run_found,
            is_still_running=r.is_still_running,
            failed_step_count=r.failed_step_count,
            steps=[asdict(s) for s in r.steps],
        )

    def xǁPipelineRunLogsUseCaseǁexecute__mutmut_26(self, command: PipelineRunLogsCommand) -> PipelineRunLogsResponse:
        req = PipelineRunLogsRequest(
            pipeline_run_name=command.pipeline_run_name, namespace=command.namespace
        )
        steps = self._port.fetch_step_logs(req)
        r = PipelineRunLogsResult.compute(request=req, steps=steps)
        return PipelineRunLogsResponse(
            pipeline_run_name=r.pipeline_run_name,
            namespace=r.namespace,
            pipeline_run_found=r.pipeline_run_found,
            is_still_running=r.is_still_running,
            failed_step_count=r.failed_step_count,
            total_step_count=r.total_step_count,
            )

    def xǁPipelineRunLogsUseCaseǁexecute__mutmut_27(self, command: PipelineRunLogsCommand) -> PipelineRunLogsResponse:
        req = PipelineRunLogsRequest(
            pipeline_run_name=command.pipeline_run_name, namespace=command.namespace
        )
        steps = self._port.fetch_step_logs(req)
        r = PipelineRunLogsResult.compute(request=req, steps=steps)
        return PipelineRunLogsResponse(
            pipeline_run_name=r.pipeline_run_name,
            namespace=r.namespace,
            pipeline_run_found=r.pipeline_run_found,
            is_still_running=r.is_still_running,
            failed_step_count=r.failed_step_count,
            total_step_count=r.total_step_count,
            steps=[asdict(None) for s in r.steps],
        )

mutants_xǁPipelineRunLogsUseCaseǁ__init____mutmut['_mutmut_orig'] = PipelineRunLogsUseCase.xǁPipelineRunLogsUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁPipelineRunLogsUseCaseǁ__init____mutmut['xǁPipelineRunLogsUseCaseǁ__init____mutmut_1'] = PipelineRunLogsUseCase.xǁPipelineRunLogsUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁPipelineRunLogsUseCaseǁexecute__mutmut['_mutmut_orig'] = PipelineRunLogsUseCase.xǁPipelineRunLogsUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPipelineRunLogsUseCaseǁexecute__mutmut['xǁPipelineRunLogsUseCaseǁexecute__mutmut_1'] = PipelineRunLogsUseCase.xǁPipelineRunLogsUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPipelineRunLogsUseCaseǁexecute__mutmut['xǁPipelineRunLogsUseCaseǁexecute__mutmut_2'] = PipelineRunLogsUseCase.xǁPipelineRunLogsUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPipelineRunLogsUseCaseǁexecute__mutmut['xǁPipelineRunLogsUseCaseǁexecute__mutmut_3'] = PipelineRunLogsUseCase.xǁPipelineRunLogsUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPipelineRunLogsUseCaseǁexecute__mutmut['xǁPipelineRunLogsUseCaseǁexecute__mutmut_4'] = PipelineRunLogsUseCase.xǁPipelineRunLogsUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPipelineRunLogsUseCaseǁexecute__mutmut['xǁPipelineRunLogsUseCaseǁexecute__mutmut_5'] = PipelineRunLogsUseCase.xǁPipelineRunLogsUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPipelineRunLogsUseCaseǁexecute__mutmut['xǁPipelineRunLogsUseCaseǁexecute__mutmut_6'] = PipelineRunLogsUseCase.xǁPipelineRunLogsUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPipelineRunLogsUseCaseǁexecute__mutmut['xǁPipelineRunLogsUseCaseǁexecute__mutmut_7'] = PipelineRunLogsUseCase.xǁPipelineRunLogsUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPipelineRunLogsUseCaseǁexecute__mutmut['xǁPipelineRunLogsUseCaseǁexecute__mutmut_8'] = PipelineRunLogsUseCase.xǁPipelineRunLogsUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁPipelineRunLogsUseCaseǁexecute__mutmut['xǁPipelineRunLogsUseCaseǁexecute__mutmut_9'] = PipelineRunLogsUseCase.xǁPipelineRunLogsUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁPipelineRunLogsUseCaseǁexecute__mutmut['xǁPipelineRunLogsUseCaseǁexecute__mutmut_10'] = PipelineRunLogsUseCase.xǁPipelineRunLogsUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁPipelineRunLogsUseCaseǁexecute__mutmut['xǁPipelineRunLogsUseCaseǁexecute__mutmut_11'] = PipelineRunLogsUseCase.xǁPipelineRunLogsUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁPipelineRunLogsUseCaseǁexecute__mutmut['xǁPipelineRunLogsUseCaseǁexecute__mutmut_12'] = PipelineRunLogsUseCase.xǁPipelineRunLogsUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁPipelineRunLogsUseCaseǁexecute__mutmut['xǁPipelineRunLogsUseCaseǁexecute__mutmut_13'] = PipelineRunLogsUseCase.xǁPipelineRunLogsUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁPipelineRunLogsUseCaseǁexecute__mutmut['xǁPipelineRunLogsUseCaseǁexecute__mutmut_14'] = PipelineRunLogsUseCase.xǁPipelineRunLogsUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁPipelineRunLogsUseCaseǁexecute__mutmut['xǁPipelineRunLogsUseCaseǁexecute__mutmut_15'] = PipelineRunLogsUseCase.xǁPipelineRunLogsUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁPipelineRunLogsUseCaseǁexecute__mutmut['xǁPipelineRunLogsUseCaseǁexecute__mutmut_16'] = PipelineRunLogsUseCase.xǁPipelineRunLogsUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁPipelineRunLogsUseCaseǁexecute__mutmut['xǁPipelineRunLogsUseCaseǁexecute__mutmut_17'] = PipelineRunLogsUseCase.xǁPipelineRunLogsUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁPipelineRunLogsUseCaseǁexecute__mutmut['xǁPipelineRunLogsUseCaseǁexecute__mutmut_18'] = PipelineRunLogsUseCase.xǁPipelineRunLogsUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁPipelineRunLogsUseCaseǁexecute__mutmut['xǁPipelineRunLogsUseCaseǁexecute__mutmut_19'] = PipelineRunLogsUseCase.xǁPipelineRunLogsUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁPipelineRunLogsUseCaseǁexecute__mutmut['xǁPipelineRunLogsUseCaseǁexecute__mutmut_20'] = PipelineRunLogsUseCase.xǁPipelineRunLogsUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁPipelineRunLogsUseCaseǁexecute__mutmut['xǁPipelineRunLogsUseCaseǁexecute__mutmut_21'] = PipelineRunLogsUseCase.xǁPipelineRunLogsUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁPipelineRunLogsUseCaseǁexecute__mutmut['xǁPipelineRunLogsUseCaseǁexecute__mutmut_22'] = PipelineRunLogsUseCase.xǁPipelineRunLogsUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁPipelineRunLogsUseCaseǁexecute__mutmut['xǁPipelineRunLogsUseCaseǁexecute__mutmut_23'] = PipelineRunLogsUseCase.xǁPipelineRunLogsUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁPipelineRunLogsUseCaseǁexecute__mutmut['xǁPipelineRunLogsUseCaseǁexecute__mutmut_24'] = PipelineRunLogsUseCase.xǁPipelineRunLogsUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁPipelineRunLogsUseCaseǁexecute__mutmut['xǁPipelineRunLogsUseCaseǁexecute__mutmut_25'] = PipelineRunLogsUseCase.xǁPipelineRunLogsUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁPipelineRunLogsUseCaseǁexecute__mutmut['xǁPipelineRunLogsUseCaseǁexecute__mutmut_26'] = PipelineRunLogsUseCase.xǁPipelineRunLogsUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁPipelineRunLogsUseCaseǁexecute__mutmut['xǁPipelineRunLogsUseCaseǁexecute__mutmut_27'] = PipelineRunLogsUseCase.xǁPipelineRunLogsUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
