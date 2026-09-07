from __future__ import annotations

from hexawyn.application.ports.driven.recurring_incident_port import (
    RecurringIncidentPort,
)
from hexawyn.application.use_case.troubleshooting.detect_recurring_incidents.command import (
    DetectRecurringIncidentsCommand,
)
from hexawyn.application.use_case.troubleshooting.detect_recurring_incidents.response import (
    DetectRecurringIncidentsResponse,
)
from hexawyn.domain.services.recurring_incident.recurring_incident_engine import (
    RecurringIncidentEngine,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁDetectRecurringIncidentsUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDetectRecurringIncidentsUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class DetectRecurringIncidentsUseCase:
    @_mutmut_mutated(mutants_xǁDetectRecurringIncidentsUseCaseǁ__init____mutmut)
    def __init__(self, incident_port: RecurringIncidentPort) -> None:
        self._port = incident_port
        self._engine = RecurringIncidentEngine()
    def xǁDetectRecurringIncidentsUseCaseǁ__init____mutmut_orig(self, incident_port: RecurringIncidentPort) -> None:
        self._port = incident_port
        self._engine = RecurringIncidentEngine()
    def xǁDetectRecurringIncidentsUseCaseǁ__init____mutmut_1(self, incident_port: RecurringIncidentPort) -> None:
        self._port = None
        self._engine = RecurringIncidentEngine()
    def xǁDetectRecurringIncidentsUseCaseǁ__init____mutmut_2(self, incident_port: RecurringIncidentPort) -> None:
        self._port = incident_port
        self._engine = None

    @_mutmut_mutated(mutants_xǁDetectRecurringIncidentsUseCaseǁexecute__mutmut)
    def execute(self, command: DetectRecurringIncidentsCommand) -> DetectRecurringIncidentsResponse:
        raw = self._port.fetch_incidents(command.window_days)
        incidents: list[dict[str, object]] = [dict(i) for i in raw]
        result = self._engine.compute(incidents)
        return DetectRecurringIncidentsResponse(result=result)

    def xǁDetectRecurringIncidentsUseCaseǁexecute__mutmut_orig(self, command: DetectRecurringIncidentsCommand) -> DetectRecurringIncidentsResponse:
        raw = self._port.fetch_incidents(command.window_days)
        incidents: list[dict[str, object]] = [dict(i) for i in raw]
        result = self._engine.compute(incidents)
        return DetectRecurringIncidentsResponse(result=result)

    def xǁDetectRecurringIncidentsUseCaseǁexecute__mutmut_1(self, command: DetectRecurringIncidentsCommand) -> DetectRecurringIncidentsResponse:
        raw = None
        incidents: list[dict[str, object]] = [dict(i) for i in raw]
        result = self._engine.compute(incidents)
        return DetectRecurringIncidentsResponse(result=result)

    def xǁDetectRecurringIncidentsUseCaseǁexecute__mutmut_2(self, command: DetectRecurringIncidentsCommand) -> DetectRecurringIncidentsResponse:
        raw = self._port.fetch_incidents(None)
        incidents: list[dict[str, object]] = [dict(i) for i in raw]
        result = self._engine.compute(incidents)
        return DetectRecurringIncidentsResponse(result=result)

    def xǁDetectRecurringIncidentsUseCaseǁexecute__mutmut_3(self, command: DetectRecurringIncidentsCommand) -> DetectRecurringIncidentsResponse:
        raw = self._port.fetch_incidents(command.window_days)
        incidents: list[dict[str, object]] = None
        result = self._engine.compute(incidents)
        return DetectRecurringIncidentsResponse(result=result)

    def xǁDetectRecurringIncidentsUseCaseǁexecute__mutmut_4(self, command: DetectRecurringIncidentsCommand) -> DetectRecurringIncidentsResponse:
        raw = self._port.fetch_incidents(command.window_days)
        incidents: list[dict[str, object]] = [dict(None) for i in raw]
        result = self._engine.compute(incidents)
        return DetectRecurringIncidentsResponse(result=result)

    def xǁDetectRecurringIncidentsUseCaseǁexecute__mutmut_5(self, command: DetectRecurringIncidentsCommand) -> DetectRecurringIncidentsResponse:
        raw = self._port.fetch_incidents(command.window_days)
        incidents: list[dict[str, object]] = [dict(i) for i in raw]
        result = None
        return DetectRecurringIncidentsResponse(result=result)

    def xǁDetectRecurringIncidentsUseCaseǁexecute__mutmut_6(self, command: DetectRecurringIncidentsCommand) -> DetectRecurringIncidentsResponse:
        raw = self._port.fetch_incidents(command.window_days)
        incidents: list[dict[str, object]] = [dict(i) for i in raw]
        result = self._engine.compute(None)
        return DetectRecurringIncidentsResponse(result=result)

    def xǁDetectRecurringIncidentsUseCaseǁexecute__mutmut_7(self, command: DetectRecurringIncidentsCommand) -> DetectRecurringIncidentsResponse:
        raw = self._port.fetch_incidents(command.window_days)
        incidents: list[dict[str, object]] = [dict(i) for i in raw]
        result = self._engine.compute(incidents)
        return DetectRecurringIncidentsResponse(result=None)

mutants_xǁDetectRecurringIncidentsUseCaseǁ__init____mutmut['_mutmut_orig'] = DetectRecurringIncidentsUseCase.xǁDetectRecurringIncidentsUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDetectRecurringIncidentsUseCaseǁ__init____mutmut['xǁDetectRecurringIncidentsUseCaseǁ__init____mutmut_1'] = DetectRecurringIncidentsUseCase.xǁDetectRecurringIncidentsUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDetectRecurringIncidentsUseCaseǁ__init____mutmut['xǁDetectRecurringIncidentsUseCaseǁ__init____mutmut_2'] = DetectRecurringIncidentsUseCase.xǁDetectRecurringIncidentsUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁDetectRecurringIncidentsUseCaseǁexecute__mutmut['_mutmut_orig'] = DetectRecurringIncidentsUseCase.xǁDetectRecurringIncidentsUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDetectRecurringIncidentsUseCaseǁexecute__mutmut['xǁDetectRecurringIncidentsUseCaseǁexecute__mutmut_1'] = DetectRecurringIncidentsUseCase.xǁDetectRecurringIncidentsUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDetectRecurringIncidentsUseCaseǁexecute__mutmut['xǁDetectRecurringIncidentsUseCaseǁexecute__mutmut_2'] = DetectRecurringIncidentsUseCase.xǁDetectRecurringIncidentsUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDetectRecurringIncidentsUseCaseǁexecute__mutmut['xǁDetectRecurringIncidentsUseCaseǁexecute__mutmut_3'] = DetectRecurringIncidentsUseCase.xǁDetectRecurringIncidentsUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDetectRecurringIncidentsUseCaseǁexecute__mutmut['xǁDetectRecurringIncidentsUseCaseǁexecute__mutmut_4'] = DetectRecurringIncidentsUseCase.xǁDetectRecurringIncidentsUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDetectRecurringIncidentsUseCaseǁexecute__mutmut['xǁDetectRecurringIncidentsUseCaseǁexecute__mutmut_5'] = DetectRecurringIncidentsUseCase.xǁDetectRecurringIncidentsUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDetectRecurringIncidentsUseCaseǁexecute__mutmut['xǁDetectRecurringIncidentsUseCaseǁexecute__mutmut_6'] = DetectRecurringIncidentsUseCase.xǁDetectRecurringIncidentsUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDetectRecurringIncidentsUseCaseǁexecute__mutmut['xǁDetectRecurringIncidentsUseCaseǁexecute__mutmut_7'] = DetectRecurringIncidentsUseCase.xǁDetectRecurringIncidentsUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
