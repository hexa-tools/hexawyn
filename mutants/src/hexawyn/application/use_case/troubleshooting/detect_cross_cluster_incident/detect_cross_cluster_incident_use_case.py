from __future__ import annotations

from hexawyn.application.ports.driven.cross_cluster_incident_port import (
    CrossClusterIncidentPort,
)
from hexawyn.application.use_case.troubleshooting.detect_cross_cluster_incident.command import (  # noqa: E501
    DetectCrossClusterIncidentCommand,
)
from hexawyn.application.use_case.troubleshooting.detect_cross_cluster_incident.response import (  # noqa: E501
    DetectCrossClusterIncidentResponse,
)
from hexawyn.domain.services.cross_cluster_correlation.cross_cluster_correlation_service import (  # noqa: E501
    correlate,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁDetectCrossClusterIncidentUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDetectCrossClusterIncidentUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class DetectCrossClusterIncidentUseCase:
    @_mutmut_mutated(mutants_xǁDetectCrossClusterIncidentUseCaseǁ__init____mutmut)
    def __init__(self, incident_port: CrossClusterIncidentPort) -> None:
        self._port = incident_port
    def xǁDetectCrossClusterIncidentUseCaseǁ__init____mutmut_orig(self, incident_port: CrossClusterIncidentPort) -> None:
        self._port = incident_port
    def xǁDetectCrossClusterIncidentUseCaseǁ__init____mutmut_1(self, incident_port: CrossClusterIncidentPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁDetectCrossClusterIncidentUseCaseǁexecute__mutmut)
    def execute(
        self, command: DetectCrossClusterIncidentCommand
    ) -> DetectCrossClusterIncidentResponse:
        failures = self._port.list_all_cluster_failures()
        result = correlate(failures, window_minutes=command.window_minutes)
        return DetectCrossClusterIncidentResponse(result=result)

    def xǁDetectCrossClusterIncidentUseCaseǁexecute__mutmut_orig(
        self, command: DetectCrossClusterIncidentCommand
    ) -> DetectCrossClusterIncidentResponse:
        failures = self._port.list_all_cluster_failures()
        result = correlate(failures, window_minutes=command.window_minutes)
        return DetectCrossClusterIncidentResponse(result=result)

    def xǁDetectCrossClusterIncidentUseCaseǁexecute__mutmut_1(
        self, command: DetectCrossClusterIncidentCommand
    ) -> DetectCrossClusterIncidentResponse:
        failures = None
        result = correlate(failures, window_minutes=command.window_minutes)
        return DetectCrossClusterIncidentResponse(result=result)

    def xǁDetectCrossClusterIncidentUseCaseǁexecute__mutmut_2(
        self, command: DetectCrossClusterIncidentCommand
    ) -> DetectCrossClusterIncidentResponse:
        failures = self._port.list_all_cluster_failures()
        result = None
        return DetectCrossClusterIncidentResponse(result=result)

    def xǁDetectCrossClusterIncidentUseCaseǁexecute__mutmut_3(
        self, command: DetectCrossClusterIncidentCommand
    ) -> DetectCrossClusterIncidentResponse:
        failures = self._port.list_all_cluster_failures()
        result = correlate(None, window_minutes=command.window_minutes)
        return DetectCrossClusterIncidentResponse(result=result)

    def xǁDetectCrossClusterIncidentUseCaseǁexecute__mutmut_4(
        self, command: DetectCrossClusterIncidentCommand
    ) -> DetectCrossClusterIncidentResponse:
        failures = self._port.list_all_cluster_failures()
        result = correlate(failures, window_minutes=None)
        return DetectCrossClusterIncidentResponse(result=result)

    def xǁDetectCrossClusterIncidentUseCaseǁexecute__mutmut_5(
        self, command: DetectCrossClusterIncidentCommand
    ) -> DetectCrossClusterIncidentResponse:
        failures = self._port.list_all_cluster_failures()
        result = correlate(window_minutes=command.window_minutes)
        return DetectCrossClusterIncidentResponse(result=result)

    def xǁDetectCrossClusterIncidentUseCaseǁexecute__mutmut_6(
        self, command: DetectCrossClusterIncidentCommand
    ) -> DetectCrossClusterIncidentResponse:
        failures = self._port.list_all_cluster_failures()
        result = correlate(failures, )
        return DetectCrossClusterIncidentResponse(result=result)

    def xǁDetectCrossClusterIncidentUseCaseǁexecute__mutmut_7(
        self, command: DetectCrossClusterIncidentCommand
    ) -> DetectCrossClusterIncidentResponse:
        failures = self._port.list_all_cluster_failures()
        result = correlate(failures, window_minutes=command.window_minutes)
        return DetectCrossClusterIncidentResponse(result=None)

mutants_xǁDetectCrossClusterIncidentUseCaseǁ__init____mutmut['_mutmut_orig'] = DetectCrossClusterIncidentUseCase.xǁDetectCrossClusterIncidentUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDetectCrossClusterIncidentUseCaseǁ__init____mutmut['xǁDetectCrossClusterIncidentUseCaseǁ__init____mutmut_1'] = DetectCrossClusterIncidentUseCase.xǁDetectCrossClusterIncidentUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁDetectCrossClusterIncidentUseCaseǁexecute__mutmut['_mutmut_orig'] = DetectCrossClusterIncidentUseCase.xǁDetectCrossClusterIncidentUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDetectCrossClusterIncidentUseCaseǁexecute__mutmut['xǁDetectCrossClusterIncidentUseCaseǁexecute__mutmut_1'] = DetectCrossClusterIncidentUseCase.xǁDetectCrossClusterIncidentUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDetectCrossClusterIncidentUseCaseǁexecute__mutmut['xǁDetectCrossClusterIncidentUseCaseǁexecute__mutmut_2'] = DetectCrossClusterIncidentUseCase.xǁDetectCrossClusterIncidentUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDetectCrossClusterIncidentUseCaseǁexecute__mutmut['xǁDetectCrossClusterIncidentUseCaseǁexecute__mutmut_3'] = DetectCrossClusterIncidentUseCase.xǁDetectCrossClusterIncidentUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDetectCrossClusterIncidentUseCaseǁexecute__mutmut['xǁDetectCrossClusterIncidentUseCaseǁexecute__mutmut_4'] = DetectCrossClusterIncidentUseCase.xǁDetectCrossClusterIncidentUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDetectCrossClusterIncidentUseCaseǁexecute__mutmut['xǁDetectCrossClusterIncidentUseCaseǁexecute__mutmut_5'] = DetectCrossClusterIncidentUseCase.xǁDetectCrossClusterIncidentUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDetectCrossClusterIncidentUseCaseǁexecute__mutmut['xǁDetectCrossClusterIncidentUseCaseǁexecute__mutmut_6'] = DetectCrossClusterIncidentUseCase.xǁDetectCrossClusterIncidentUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDetectCrossClusterIncidentUseCaseǁexecute__mutmut['xǁDetectCrossClusterIncidentUseCaseǁexecute__mutmut_7'] = DetectCrossClusterIncidentUseCase.xǁDetectCrossClusterIncidentUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
