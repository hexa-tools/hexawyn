from __future__ import annotations

from hexawyn.application.ports.driven.incident_cost_port import IncidentCostPort
from hexawyn.application.use_case.finops.analyze_incident_cost.command import (  # noqa: E501
    AnalyzeIncidentCostCommand,
)
from hexawyn.application.use_case.finops.analyze_incident_cost.response import (  # noqa: E501
    AnalyzeIncidentCostResponse,
)
from hexawyn.domain.services.incident_cost.incident_cost_calculator import (
    compute_incident_cost,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁAnalyzeIncidentCostUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁAnalyzeIncidentCostUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class AnalyzeIncidentCostUseCase:
    @_mutmut_mutated(mutants_xǁAnalyzeIncidentCostUseCaseǁ__init____mutmut)
    def __init__(self, incident_cost_port: IncidentCostPort) -> None:
        self._port = incident_cost_port
    def xǁAnalyzeIncidentCostUseCaseǁ__init____mutmut_orig(self, incident_cost_port: IncidentCostPort) -> None:
        self._port = incident_cost_port
    def xǁAnalyzeIncidentCostUseCaseǁ__init____mutmut_1(self, incident_cost_port: IncidentCostPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁAnalyzeIncidentCostUseCaseǁexecute__mutmut)
    def execute(self, command: AnalyzeIncidentCostCommand) -> AnalyzeIncidentCostResponse:
        data = self._port.get_incident_cost_data(command.incident_ref)
        result = compute_incident_cost(data)
        return AnalyzeIncidentCostResponse(result=result)

    def xǁAnalyzeIncidentCostUseCaseǁexecute__mutmut_orig(self, command: AnalyzeIncidentCostCommand) -> AnalyzeIncidentCostResponse:
        data = self._port.get_incident_cost_data(command.incident_ref)
        result = compute_incident_cost(data)
        return AnalyzeIncidentCostResponse(result=result)

    def xǁAnalyzeIncidentCostUseCaseǁexecute__mutmut_1(self, command: AnalyzeIncidentCostCommand) -> AnalyzeIncidentCostResponse:
        data = None
        result = compute_incident_cost(data)
        return AnalyzeIncidentCostResponse(result=result)

    def xǁAnalyzeIncidentCostUseCaseǁexecute__mutmut_2(self, command: AnalyzeIncidentCostCommand) -> AnalyzeIncidentCostResponse:
        data = self._port.get_incident_cost_data(None)
        result = compute_incident_cost(data)
        return AnalyzeIncidentCostResponse(result=result)

    def xǁAnalyzeIncidentCostUseCaseǁexecute__mutmut_3(self, command: AnalyzeIncidentCostCommand) -> AnalyzeIncidentCostResponse:
        data = self._port.get_incident_cost_data(command.incident_ref)
        result = None
        return AnalyzeIncidentCostResponse(result=result)

    def xǁAnalyzeIncidentCostUseCaseǁexecute__mutmut_4(self, command: AnalyzeIncidentCostCommand) -> AnalyzeIncidentCostResponse:
        data = self._port.get_incident_cost_data(command.incident_ref)
        result = compute_incident_cost(None)
        return AnalyzeIncidentCostResponse(result=result)

    def xǁAnalyzeIncidentCostUseCaseǁexecute__mutmut_5(self, command: AnalyzeIncidentCostCommand) -> AnalyzeIncidentCostResponse:
        data = self._port.get_incident_cost_data(command.incident_ref)
        result = compute_incident_cost(data)
        return AnalyzeIncidentCostResponse(result=None)

mutants_xǁAnalyzeIncidentCostUseCaseǁ__init____mutmut['_mutmut_orig'] = AnalyzeIncidentCostUseCase.xǁAnalyzeIncidentCostUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁAnalyzeIncidentCostUseCaseǁ__init____mutmut['xǁAnalyzeIncidentCostUseCaseǁ__init____mutmut_1'] = AnalyzeIncidentCostUseCase.xǁAnalyzeIncidentCostUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁAnalyzeIncidentCostUseCaseǁexecute__mutmut['_mutmut_orig'] = AnalyzeIncidentCostUseCase.xǁAnalyzeIncidentCostUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAnalyzeIncidentCostUseCaseǁexecute__mutmut['xǁAnalyzeIncidentCostUseCaseǁexecute__mutmut_1'] = AnalyzeIncidentCostUseCase.xǁAnalyzeIncidentCostUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAnalyzeIncidentCostUseCaseǁexecute__mutmut['xǁAnalyzeIncidentCostUseCaseǁexecute__mutmut_2'] = AnalyzeIncidentCostUseCase.xǁAnalyzeIncidentCostUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAnalyzeIncidentCostUseCaseǁexecute__mutmut['xǁAnalyzeIncidentCostUseCaseǁexecute__mutmut_3'] = AnalyzeIncidentCostUseCase.xǁAnalyzeIncidentCostUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAnalyzeIncidentCostUseCaseǁexecute__mutmut['xǁAnalyzeIncidentCostUseCaseǁexecute__mutmut_4'] = AnalyzeIncidentCostUseCase.xǁAnalyzeIncidentCostUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAnalyzeIncidentCostUseCaseǁexecute__mutmut['xǁAnalyzeIncidentCostUseCaseǁexecute__mutmut_5'] = AnalyzeIncidentCostUseCase.xǁAnalyzeIncidentCostUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
