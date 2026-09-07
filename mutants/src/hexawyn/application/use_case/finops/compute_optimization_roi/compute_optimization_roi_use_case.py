from __future__ import annotations

from hexawyn.application.ports.driven.optimization_roi_port import OptimizationRoiPort
from hexawyn.application.use_case.finops.compute_optimization_roi.command import (  # noqa: E501
    ComputeOptimizationRoiCommand,
)
from hexawyn.application.use_case.finops.compute_optimization_roi.response import (  # noqa: E501
    ComputeOptimizationRoiResponse,
)
from hexawyn.domain.services.optimization_roi.optimization_roi_service import (
    OptimizationRoiService,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁComputeOptimizationRoiUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁComputeOptimizationRoiUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class ComputeOptimizationRoiUseCase:
    @_mutmut_mutated(mutants_xǁComputeOptimizationRoiUseCaseǁ__init____mutmut)
    def __init__(self, roi_port: OptimizationRoiPort) -> None:
        self._port = roi_port
        self._engine = OptimizationRoiService()
    def xǁComputeOptimizationRoiUseCaseǁ__init____mutmut_orig(self, roi_port: OptimizationRoiPort) -> None:
        self._port = roi_port
        self._engine = OptimizationRoiService()
    def xǁComputeOptimizationRoiUseCaseǁ__init____mutmut_1(self, roi_port: OptimizationRoiPort) -> None:
        self._port = None
        self._engine = OptimizationRoiService()
    def xǁComputeOptimizationRoiUseCaseǁ__init____mutmut_2(self, roi_port: OptimizationRoiPort) -> None:
        self._port = roi_port
        self._engine = None

    @_mutmut_mutated(mutants_xǁComputeOptimizationRoiUseCaseǁexecute__mutmut)
    def execute(self, command: ComputeOptimizationRoiCommand) -> ComputeOptimizationRoiResponse:
        data = self._port.get_sprint_roi_data(command.sprint_id)
        result = self._engine.compute(data, traffic_growth_pct=command.traffic_growth_pct)
        return ComputeOptimizationRoiResponse(result=result)

    def xǁComputeOptimizationRoiUseCaseǁexecute__mutmut_orig(self, command: ComputeOptimizationRoiCommand) -> ComputeOptimizationRoiResponse:
        data = self._port.get_sprint_roi_data(command.sprint_id)
        result = self._engine.compute(data, traffic_growth_pct=command.traffic_growth_pct)
        return ComputeOptimizationRoiResponse(result=result)

    def xǁComputeOptimizationRoiUseCaseǁexecute__mutmut_1(self, command: ComputeOptimizationRoiCommand) -> ComputeOptimizationRoiResponse:
        data = None
        result = self._engine.compute(data, traffic_growth_pct=command.traffic_growth_pct)
        return ComputeOptimizationRoiResponse(result=result)

    def xǁComputeOptimizationRoiUseCaseǁexecute__mutmut_2(self, command: ComputeOptimizationRoiCommand) -> ComputeOptimizationRoiResponse:
        data = self._port.get_sprint_roi_data(None)
        result = self._engine.compute(data, traffic_growth_pct=command.traffic_growth_pct)
        return ComputeOptimizationRoiResponse(result=result)

    def xǁComputeOptimizationRoiUseCaseǁexecute__mutmut_3(self, command: ComputeOptimizationRoiCommand) -> ComputeOptimizationRoiResponse:
        data = self._port.get_sprint_roi_data(command.sprint_id)
        result = None
        return ComputeOptimizationRoiResponse(result=result)

    def xǁComputeOptimizationRoiUseCaseǁexecute__mutmut_4(self, command: ComputeOptimizationRoiCommand) -> ComputeOptimizationRoiResponse:
        data = self._port.get_sprint_roi_data(command.sprint_id)
        result = self._engine.compute(None, traffic_growth_pct=command.traffic_growth_pct)
        return ComputeOptimizationRoiResponse(result=result)

    def xǁComputeOptimizationRoiUseCaseǁexecute__mutmut_5(self, command: ComputeOptimizationRoiCommand) -> ComputeOptimizationRoiResponse:
        data = self._port.get_sprint_roi_data(command.sprint_id)
        result = self._engine.compute(data, traffic_growth_pct=None)
        return ComputeOptimizationRoiResponse(result=result)

    def xǁComputeOptimizationRoiUseCaseǁexecute__mutmut_6(self, command: ComputeOptimizationRoiCommand) -> ComputeOptimizationRoiResponse:
        data = self._port.get_sprint_roi_data(command.sprint_id)
        result = self._engine.compute(traffic_growth_pct=command.traffic_growth_pct)
        return ComputeOptimizationRoiResponse(result=result)

    def xǁComputeOptimizationRoiUseCaseǁexecute__mutmut_7(self, command: ComputeOptimizationRoiCommand) -> ComputeOptimizationRoiResponse:
        data = self._port.get_sprint_roi_data(command.sprint_id)
        result = self._engine.compute(data, )
        return ComputeOptimizationRoiResponse(result=result)

    def xǁComputeOptimizationRoiUseCaseǁexecute__mutmut_8(self, command: ComputeOptimizationRoiCommand) -> ComputeOptimizationRoiResponse:
        data = self._port.get_sprint_roi_data(command.sprint_id)
        result = self._engine.compute(data, traffic_growth_pct=command.traffic_growth_pct)
        return ComputeOptimizationRoiResponse(result=None)

mutants_xǁComputeOptimizationRoiUseCaseǁ__init____mutmut['_mutmut_orig'] = ComputeOptimizationRoiUseCase.xǁComputeOptimizationRoiUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁComputeOptimizationRoiUseCaseǁ__init____mutmut['xǁComputeOptimizationRoiUseCaseǁ__init____mutmut_1'] = ComputeOptimizationRoiUseCase.xǁComputeOptimizationRoiUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁComputeOptimizationRoiUseCaseǁ__init____mutmut['xǁComputeOptimizationRoiUseCaseǁ__init____mutmut_2'] = ComputeOptimizationRoiUseCase.xǁComputeOptimizationRoiUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁComputeOptimizationRoiUseCaseǁexecute__mutmut['_mutmut_orig'] = ComputeOptimizationRoiUseCase.xǁComputeOptimizationRoiUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁComputeOptimizationRoiUseCaseǁexecute__mutmut['xǁComputeOptimizationRoiUseCaseǁexecute__mutmut_1'] = ComputeOptimizationRoiUseCase.xǁComputeOptimizationRoiUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁComputeOptimizationRoiUseCaseǁexecute__mutmut['xǁComputeOptimizationRoiUseCaseǁexecute__mutmut_2'] = ComputeOptimizationRoiUseCase.xǁComputeOptimizationRoiUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁComputeOptimizationRoiUseCaseǁexecute__mutmut['xǁComputeOptimizationRoiUseCaseǁexecute__mutmut_3'] = ComputeOptimizationRoiUseCase.xǁComputeOptimizationRoiUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁComputeOptimizationRoiUseCaseǁexecute__mutmut['xǁComputeOptimizationRoiUseCaseǁexecute__mutmut_4'] = ComputeOptimizationRoiUseCase.xǁComputeOptimizationRoiUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁComputeOptimizationRoiUseCaseǁexecute__mutmut['xǁComputeOptimizationRoiUseCaseǁexecute__mutmut_5'] = ComputeOptimizationRoiUseCase.xǁComputeOptimizationRoiUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁComputeOptimizationRoiUseCaseǁexecute__mutmut['xǁComputeOptimizationRoiUseCaseǁexecute__mutmut_6'] = ComputeOptimizationRoiUseCase.xǁComputeOptimizationRoiUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁComputeOptimizationRoiUseCaseǁexecute__mutmut['xǁComputeOptimizationRoiUseCaseǁexecute__mutmut_7'] = ComputeOptimizationRoiUseCase.xǁComputeOptimizationRoiUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁComputeOptimizationRoiUseCaseǁexecute__mutmut['xǁComputeOptimizationRoiUseCaseǁexecute__mutmut_8'] = ComputeOptimizationRoiUseCase.xǁComputeOptimizationRoiUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
