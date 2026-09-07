from __future__ import annotations

from hexawyn.application.ports.driven.prediction_roi_port import PredictionRoiPort
from hexawyn.application.use_case.finops.compute_prediction_roi.command import (  # noqa: E501
    ComputePredictionRoiCommand,
)
from hexawyn.application.use_case.finops.compute_prediction_roi.response import (  # noqa: E501
    ComputePredictionRoiResponse,
)
from hexawyn.domain.services.prediction_roi.prediction_roi_calculator import (
    compute_prediction_roi,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁComputePredictionRoiUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁComputePredictionRoiUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class ComputePredictionRoiUseCase:
    @_mutmut_mutated(mutants_xǁComputePredictionRoiUseCaseǁ__init____mutmut)
    def __init__(self, prediction_roi_port: PredictionRoiPort) -> None:
        self._port = prediction_roi_port
    def xǁComputePredictionRoiUseCaseǁ__init____mutmut_orig(self, prediction_roi_port: PredictionRoiPort) -> None:
        self._port = prediction_roi_port
    def xǁComputePredictionRoiUseCaseǁ__init____mutmut_1(self, prediction_roi_port: PredictionRoiPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁComputePredictionRoiUseCaseǁexecute__mutmut)
    def execute(self, command: ComputePredictionRoiCommand) -> ComputePredictionRoiResponse:
        data = self._port.get_prediction_roi_data(command.period)
        result = compute_prediction_roi(data, period=command.period)
        return ComputePredictionRoiResponse(result=result)

    def xǁComputePredictionRoiUseCaseǁexecute__mutmut_orig(self, command: ComputePredictionRoiCommand) -> ComputePredictionRoiResponse:
        data = self._port.get_prediction_roi_data(command.period)
        result = compute_prediction_roi(data, period=command.period)
        return ComputePredictionRoiResponse(result=result)

    def xǁComputePredictionRoiUseCaseǁexecute__mutmut_1(self, command: ComputePredictionRoiCommand) -> ComputePredictionRoiResponse:
        data = None
        result = compute_prediction_roi(data, period=command.period)
        return ComputePredictionRoiResponse(result=result)

    def xǁComputePredictionRoiUseCaseǁexecute__mutmut_2(self, command: ComputePredictionRoiCommand) -> ComputePredictionRoiResponse:
        data = self._port.get_prediction_roi_data(None)
        result = compute_prediction_roi(data, period=command.period)
        return ComputePredictionRoiResponse(result=result)

    def xǁComputePredictionRoiUseCaseǁexecute__mutmut_3(self, command: ComputePredictionRoiCommand) -> ComputePredictionRoiResponse:
        data = self._port.get_prediction_roi_data(command.period)
        result = None
        return ComputePredictionRoiResponse(result=result)

    def xǁComputePredictionRoiUseCaseǁexecute__mutmut_4(self, command: ComputePredictionRoiCommand) -> ComputePredictionRoiResponse:
        data = self._port.get_prediction_roi_data(command.period)
        result = compute_prediction_roi(None, period=command.period)
        return ComputePredictionRoiResponse(result=result)

    def xǁComputePredictionRoiUseCaseǁexecute__mutmut_5(self, command: ComputePredictionRoiCommand) -> ComputePredictionRoiResponse:
        data = self._port.get_prediction_roi_data(command.period)
        result = compute_prediction_roi(data, period=None)
        return ComputePredictionRoiResponse(result=result)

    def xǁComputePredictionRoiUseCaseǁexecute__mutmut_6(self, command: ComputePredictionRoiCommand) -> ComputePredictionRoiResponse:
        data = self._port.get_prediction_roi_data(command.period)
        result = compute_prediction_roi(period=command.period)
        return ComputePredictionRoiResponse(result=result)

    def xǁComputePredictionRoiUseCaseǁexecute__mutmut_7(self, command: ComputePredictionRoiCommand) -> ComputePredictionRoiResponse:
        data = self._port.get_prediction_roi_data(command.period)
        result = compute_prediction_roi(data, )
        return ComputePredictionRoiResponse(result=result)

    def xǁComputePredictionRoiUseCaseǁexecute__mutmut_8(self, command: ComputePredictionRoiCommand) -> ComputePredictionRoiResponse:
        data = self._port.get_prediction_roi_data(command.period)
        result = compute_prediction_roi(data, period=command.period)
        return ComputePredictionRoiResponse(result=None)

mutants_xǁComputePredictionRoiUseCaseǁ__init____mutmut['_mutmut_orig'] = ComputePredictionRoiUseCase.xǁComputePredictionRoiUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁComputePredictionRoiUseCaseǁ__init____mutmut['xǁComputePredictionRoiUseCaseǁ__init____mutmut_1'] = ComputePredictionRoiUseCase.xǁComputePredictionRoiUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁComputePredictionRoiUseCaseǁexecute__mutmut['_mutmut_orig'] = ComputePredictionRoiUseCase.xǁComputePredictionRoiUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁComputePredictionRoiUseCaseǁexecute__mutmut['xǁComputePredictionRoiUseCaseǁexecute__mutmut_1'] = ComputePredictionRoiUseCase.xǁComputePredictionRoiUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁComputePredictionRoiUseCaseǁexecute__mutmut['xǁComputePredictionRoiUseCaseǁexecute__mutmut_2'] = ComputePredictionRoiUseCase.xǁComputePredictionRoiUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁComputePredictionRoiUseCaseǁexecute__mutmut['xǁComputePredictionRoiUseCaseǁexecute__mutmut_3'] = ComputePredictionRoiUseCase.xǁComputePredictionRoiUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁComputePredictionRoiUseCaseǁexecute__mutmut['xǁComputePredictionRoiUseCaseǁexecute__mutmut_4'] = ComputePredictionRoiUseCase.xǁComputePredictionRoiUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁComputePredictionRoiUseCaseǁexecute__mutmut['xǁComputePredictionRoiUseCaseǁexecute__mutmut_5'] = ComputePredictionRoiUseCase.xǁComputePredictionRoiUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁComputePredictionRoiUseCaseǁexecute__mutmut['xǁComputePredictionRoiUseCaseǁexecute__mutmut_6'] = ComputePredictionRoiUseCase.xǁComputePredictionRoiUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁComputePredictionRoiUseCaseǁexecute__mutmut['xǁComputePredictionRoiUseCaseǁexecute__mutmut_7'] = ComputePredictionRoiUseCase.xǁComputePredictionRoiUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁComputePredictionRoiUseCaseǁexecute__mutmut['xǁComputePredictionRoiUseCaseǁexecute__mutmut_8'] = ComputePredictionRoiUseCase.xǁComputePredictionRoiUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
