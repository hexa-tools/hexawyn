from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.pipeline_for_service_port import PipelineForServicePort
from hexawyn.application.use_case.pipelines.pipeline_for_service.command import (
    PipelineForServiceCommand,
)
from hexawyn.application.use_case.pipelines.pipeline_for_service.response import (
    PipelineForServiceResponse,
)
from hexawyn.domain.models.pipeline_for_service import (
    PipelineForServiceRequest,
    PipelineForServiceResult,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁPipelineForUseCaseUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁPipelineForUseCaseUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class PipelineForUseCaseUseCase:
    @_mutmut_mutated(mutants_xǁPipelineForUseCaseUseCaseǁ__init____mutmut)
    def __init__(self, port: PipelineForServicePort) -> None:
        self._port = port
    def xǁPipelineForUseCaseUseCaseǁ__init____mutmut_orig(self, port: PipelineForServicePort) -> None:
        self._port = port
    def xǁPipelineForUseCaseUseCaseǁ__init____mutmut_1(self, port: PipelineForServicePort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁPipelineForUseCaseUseCaseǁexecute__mutmut)
    def execute(self, command: PipelineForServiceCommand) -> PipelineForServiceResponse:
        req = PipelineForServiceRequest(service_name=command.service_name)
        pipelines = self._port.find_pipelines(req)
        r = PipelineForServiceResult.compute(request=req, pipelines=pipelines)
        return PipelineForServiceResponse(
            service_name=r.service_name,
            pipelines_found=r.pipelines_found,
            pipelines=[asdict(p) for p in r.pipelines],
        )

    def xǁPipelineForUseCaseUseCaseǁexecute__mutmut_orig(self, command: PipelineForServiceCommand) -> PipelineForServiceResponse:
        req = PipelineForServiceRequest(service_name=command.service_name)
        pipelines = self._port.find_pipelines(req)
        r = PipelineForServiceResult.compute(request=req, pipelines=pipelines)
        return PipelineForServiceResponse(
            service_name=r.service_name,
            pipelines_found=r.pipelines_found,
            pipelines=[asdict(p) for p in r.pipelines],
        )

    def xǁPipelineForUseCaseUseCaseǁexecute__mutmut_1(self, command: PipelineForServiceCommand) -> PipelineForServiceResponse:
        req = None
        pipelines = self._port.find_pipelines(req)
        r = PipelineForServiceResult.compute(request=req, pipelines=pipelines)
        return PipelineForServiceResponse(
            service_name=r.service_name,
            pipelines_found=r.pipelines_found,
            pipelines=[asdict(p) for p in r.pipelines],
        )

    def xǁPipelineForUseCaseUseCaseǁexecute__mutmut_2(self, command: PipelineForServiceCommand) -> PipelineForServiceResponse:
        req = PipelineForServiceRequest(service_name=None)
        pipelines = self._port.find_pipelines(req)
        r = PipelineForServiceResult.compute(request=req, pipelines=pipelines)
        return PipelineForServiceResponse(
            service_name=r.service_name,
            pipelines_found=r.pipelines_found,
            pipelines=[asdict(p) for p in r.pipelines],
        )

    def xǁPipelineForUseCaseUseCaseǁexecute__mutmut_3(self, command: PipelineForServiceCommand) -> PipelineForServiceResponse:
        req = PipelineForServiceRequest(service_name=command.service_name)
        pipelines = None
        r = PipelineForServiceResult.compute(request=req, pipelines=pipelines)
        return PipelineForServiceResponse(
            service_name=r.service_name,
            pipelines_found=r.pipelines_found,
            pipelines=[asdict(p) for p in r.pipelines],
        )

    def xǁPipelineForUseCaseUseCaseǁexecute__mutmut_4(self, command: PipelineForServiceCommand) -> PipelineForServiceResponse:
        req = PipelineForServiceRequest(service_name=command.service_name)
        pipelines = self._port.find_pipelines(None)
        r = PipelineForServiceResult.compute(request=req, pipelines=pipelines)
        return PipelineForServiceResponse(
            service_name=r.service_name,
            pipelines_found=r.pipelines_found,
            pipelines=[asdict(p) for p in r.pipelines],
        )

    def xǁPipelineForUseCaseUseCaseǁexecute__mutmut_5(self, command: PipelineForServiceCommand) -> PipelineForServiceResponse:
        req = PipelineForServiceRequest(service_name=command.service_name)
        pipelines = self._port.find_pipelines(req)
        r = None
        return PipelineForServiceResponse(
            service_name=r.service_name,
            pipelines_found=r.pipelines_found,
            pipelines=[asdict(p) for p in r.pipelines],
        )

    def xǁPipelineForUseCaseUseCaseǁexecute__mutmut_6(self, command: PipelineForServiceCommand) -> PipelineForServiceResponse:
        req = PipelineForServiceRequest(service_name=command.service_name)
        pipelines = self._port.find_pipelines(req)
        r = PipelineForServiceResult.compute(request=None, pipelines=pipelines)
        return PipelineForServiceResponse(
            service_name=r.service_name,
            pipelines_found=r.pipelines_found,
            pipelines=[asdict(p) for p in r.pipelines],
        )

    def xǁPipelineForUseCaseUseCaseǁexecute__mutmut_7(self, command: PipelineForServiceCommand) -> PipelineForServiceResponse:
        req = PipelineForServiceRequest(service_name=command.service_name)
        pipelines = self._port.find_pipelines(req)
        r = PipelineForServiceResult.compute(request=req, pipelines=None)
        return PipelineForServiceResponse(
            service_name=r.service_name,
            pipelines_found=r.pipelines_found,
            pipelines=[asdict(p) for p in r.pipelines],
        )

    def xǁPipelineForUseCaseUseCaseǁexecute__mutmut_8(self, command: PipelineForServiceCommand) -> PipelineForServiceResponse:
        req = PipelineForServiceRequest(service_name=command.service_name)
        pipelines = self._port.find_pipelines(req)
        r = PipelineForServiceResult.compute(pipelines=pipelines)
        return PipelineForServiceResponse(
            service_name=r.service_name,
            pipelines_found=r.pipelines_found,
            pipelines=[asdict(p) for p in r.pipelines],
        )

    def xǁPipelineForUseCaseUseCaseǁexecute__mutmut_9(self, command: PipelineForServiceCommand) -> PipelineForServiceResponse:
        req = PipelineForServiceRequest(service_name=command.service_name)
        pipelines = self._port.find_pipelines(req)
        r = PipelineForServiceResult.compute(request=req, )
        return PipelineForServiceResponse(
            service_name=r.service_name,
            pipelines_found=r.pipelines_found,
            pipelines=[asdict(p) for p in r.pipelines],
        )

    def xǁPipelineForUseCaseUseCaseǁexecute__mutmut_10(self, command: PipelineForServiceCommand) -> PipelineForServiceResponse:
        req = PipelineForServiceRequest(service_name=command.service_name)
        pipelines = self._port.find_pipelines(req)
        r = PipelineForServiceResult.compute(request=req, pipelines=pipelines)
        return PipelineForServiceResponse(
            service_name=None,
            pipelines_found=r.pipelines_found,
            pipelines=[asdict(p) for p in r.pipelines],
        )

    def xǁPipelineForUseCaseUseCaseǁexecute__mutmut_11(self, command: PipelineForServiceCommand) -> PipelineForServiceResponse:
        req = PipelineForServiceRequest(service_name=command.service_name)
        pipelines = self._port.find_pipelines(req)
        r = PipelineForServiceResult.compute(request=req, pipelines=pipelines)
        return PipelineForServiceResponse(
            service_name=r.service_name,
            pipelines_found=None,
            pipelines=[asdict(p) for p in r.pipelines],
        )

    def xǁPipelineForUseCaseUseCaseǁexecute__mutmut_12(self, command: PipelineForServiceCommand) -> PipelineForServiceResponse:
        req = PipelineForServiceRequest(service_name=command.service_name)
        pipelines = self._port.find_pipelines(req)
        r = PipelineForServiceResult.compute(request=req, pipelines=pipelines)
        return PipelineForServiceResponse(
            service_name=r.service_name,
            pipelines_found=r.pipelines_found,
            pipelines=None,
        )

    def xǁPipelineForUseCaseUseCaseǁexecute__mutmut_13(self, command: PipelineForServiceCommand) -> PipelineForServiceResponse:
        req = PipelineForServiceRequest(service_name=command.service_name)
        pipelines = self._port.find_pipelines(req)
        r = PipelineForServiceResult.compute(request=req, pipelines=pipelines)
        return PipelineForServiceResponse(
            pipelines_found=r.pipelines_found,
            pipelines=[asdict(p) for p in r.pipelines],
        )

    def xǁPipelineForUseCaseUseCaseǁexecute__mutmut_14(self, command: PipelineForServiceCommand) -> PipelineForServiceResponse:
        req = PipelineForServiceRequest(service_name=command.service_name)
        pipelines = self._port.find_pipelines(req)
        r = PipelineForServiceResult.compute(request=req, pipelines=pipelines)
        return PipelineForServiceResponse(
            service_name=r.service_name,
            pipelines=[asdict(p) for p in r.pipelines],
        )

    def xǁPipelineForUseCaseUseCaseǁexecute__mutmut_15(self, command: PipelineForServiceCommand) -> PipelineForServiceResponse:
        req = PipelineForServiceRequest(service_name=command.service_name)
        pipelines = self._port.find_pipelines(req)
        r = PipelineForServiceResult.compute(request=req, pipelines=pipelines)
        return PipelineForServiceResponse(
            service_name=r.service_name,
            pipelines_found=r.pipelines_found,
            )

    def xǁPipelineForUseCaseUseCaseǁexecute__mutmut_16(self, command: PipelineForServiceCommand) -> PipelineForServiceResponse:
        req = PipelineForServiceRequest(service_name=command.service_name)
        pipelines = self._port.find_pipelines(req)
        r = PipelineForServiceResult.compute(request=req, pipelines=pipelines)
        return PipelineForServiceResponse(
            service_name=r.service_name,
            pipelines_found=r.pipelines_found,
            pipelines=[asdict(None) for p in r.pipelines],
        )

mutants_xǁPipelineForUseCaseUseCaseǁ__init____mutmut['_mutmut_orig'] = PipelineForUseCaseUseCase.xǁPipelineForUseCaseUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁPipelineForUseCaseUseCaseǁ__init____mutmut['xǁPipelineForUseCaseUseCaseǁ__init____mutmut_1'] = PipelineForUseCaseUseCase.xǁPipelineForUseCaseUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁPipelineForUseCaseUseCaseǁexecute__mutmut['_mutmut_orig'] = PipelineForUseCaseUseCase.xǁPipelineForUseCaseUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPipelineForUseCaseUseCaseǁexecute__mutmut['xǁPipelineForUseCaseUseCaseǁexecute__mutmut_1'] = PipelineForUseCaseUseCase.xǁPipelineForUseCaseUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPipelineForUseCaseUseCaseǁexecute__mutmut['xǁPipelineForUseCaseUseCaseǁexecute__mutmut_2'] = PipelineForUseCaseUseCase.xǁPipelineForUseCaseUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPipelineForUseCaseUseCaseǁexecute__mutmut['xǁPipelineForUseCaseUseCaseǁexecute__mutmut_3'] = PipelineForUseCaseUseCase.xǁPipelineForUseCaseUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPipelineForUseCaseUseCaseǁexecute__mutmut['xǁPipelineForUseCaseUseCaseǁexecute__mutmut_4'] = PipelineForUseCaseUseCase.xǁPipelineForUseCaseUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPipelineForUseCaseUseCaseǁexecute__mutmut['xǁPipelineForUseCaseUseCaseǁexecute__mutmut_5'] = PipelineForUseCaseUseCase.xǁPipelineForUseCaseUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPipelineForUseCaseUseCaseǁexecute__mutmut['xǁPipelineForUseCaseUseCaseǁexecute__mutmut_6'] = PipelineForUseCaseUseCase.xǁPipelineForUseCaseUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPipelineForUseCaseUseCaseǁexecute__mutmut['xǁPipelineForUseCaseUseCaseǁexecute__mutmut_7'] = PipelineForUseCaseUseCase.xǁPipelineForUseCaseUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPipelineForUseCaseUseCaseǁexecute__mutmut['xǁPipelineForUseCaseUseCaseǁexecute__mutmut_8'] = PipelineForUseCaseUseCase.xǁPipelineForUseCaseUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁPipelineForUseCaseUseCaseǁexecute__mutmut['xǁPipelineForUseCaseUseCaseǁexecute__mutmut_9'] = PipelineForUseCaseUseCase.xǁPipelineForUseCaseUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁPipelineForUseCaseUseCaseǁexecute__mutmut['xǁPipelineForUseCaseUseCaseǁexecute__mutmut_10'] = PipelineForUseCaseUseCase.xǁPipelineForUseCaseUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁPipelineForUseCaseUseCaseǁexecute__mutmut['xǁPipelineForUseCaseUseCaseǁexecute__mutmut_11'] = PipelineForUseCaseUseCase.xǁPipelineForUseCaseUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁPipelineForUseCaseUseCaseǁexecute__mutmut['xǁPipelineForUseCaseUseCaseǁexecute__mutmut_12'] = PipelineForUseCaseUseCase.xǁPipelineForUseCaseUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁPipelineForUseCaseUseCaseǁexecute__mutmut['xǁPipelineForUseCaseUseCaseǁexecute__mutmut_13'] = PipelineForUseCaseUseCase.xǁPipelineForUseCaseUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁPipelineForUseCaseUseCaseǁexecute__mutmut['xǁPipelineForUseCaseUseCaseǁexecute__mutmut_14'] = PipelineForUseCaseUseCase.xǁPipelineForUseCaseUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁPipelineForUseCaseUseCaseǁexecute__mutmut['xǁPipelineForUseCaseUseCaseǁexecute__mutmut_15'] = PipelineForUseCaseUseCase.xǁPipelineForUseCaseUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁPipelineForUseCaseUseCaseǁexecute__mutmut['xǁPipelineForUseCaseUseCaseǁexecute__mutmut_16'] = PipelineForUseCaseUseCase.xǁPipelineForUseCaseUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
