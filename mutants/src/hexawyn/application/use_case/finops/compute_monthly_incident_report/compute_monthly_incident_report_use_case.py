from __future__ import annotations

from datetime import UTC, datetime

from hexawyn.application.ports.driven.monthly_incident_port import MonthlyIncidentPort
from hexawyn.application.use_case.finops.compute_monthly_incident_report.command import (
    ComputeMonthlyIncidentReportCommand,
)
from hexawyn.application.use_case.finops.compute_monthly_incident_report.response import (
    ComputeMonthlyIncidentReportResponse,
)
from hexawyn.domain.services.monthly_incident.monthly_incident_report_engine import (
    MonthlyIncidentReportEngine,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁComputeMonthlyIncidentReportUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class ComputeMonthlyIncidentReportUseCase:
    @_mutmut_mutated(mutants_xǁComputeMonthlyIncidentReportUseCaseǁ__init____mutmut)
    def __init__(self, incident_port: MonthlyIncidentPort) -> None:
        self._port = incident_port
        self._engine = MonthlyIncidentReportEngine()
    def xǁComputeMonthlyIncidentReportUseCaseǁ__init____mutmut_orig(self, incident_port: MonthlyIncidentPort) -> None:
        self._port = incident_port
        self._engine = MonthlyIncidentReportEngine()
    def xǁComputeMonthlyIncidentReportUseCaseǁ__init____mutmut_1(self, incident_port: MonthlyIncidentPort) -> None:
        self._port = None
        self._engine = MonthlyIncidentReportEngine()
    def xǁComputeMonthlyIncidentReportUseCaseǁ__init____mutmut_2(self, incident_port: MonthlyIncidentPort) -> None:
        self._port = incident_port
        self._engine = None

    @_mutmut_mutated(mutants_xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut)
    def execute(
        self, command: ComputeMonthlyIncidentReportCommand
    ) -> ComputeMonthlyIncidentReportResponse:
        now = datetime.now(UTC)
        if command.month:
            month = command.month
        else:
            month = now.strftime("%Y-%m")

        prev_month = _previous_month(now.year, now.month)

        current_raw = self._port.fetch_incidents(month)
        prev_raw = self._port.fetch_incidents(prev_month)

        current: list[dict[str, object]] = [dict(i) for i in current_raw]
        prev: list[dict[str, object]] = [dict(i) for i in prev_raw]

        result = self._engine.compute(current, previous_incidents=prev)
        return ComputeMonthlyIncidentReportResponse(result=result)  # type: ignore

    def xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_orig(
        self, command: ComputeMonthlyIncidentReportCommand
    ) -> ComputeMonthlyIncidentReportResponse:
        now = datetime.now(UTC)
        if command.month:
            month = command.month
        else:
            month = now.strftime("%Y-%m")

        prev_month = _previous_month(now.year, now.month)

        current_raw = self._port.fetch_incidents(month)
        prev_raw = self._port.fetch_incidents(prev_month)

        current: list[dict[str, object]] = [dict(i) for i in current_raw]
        prev: list[dict[str, object]] = [dict(i) for i in prev_raw]

        result = self._engine.compute(current, previous_incidents=prev)
        return ComputeMonthlyIncidentReportResponse(result=result)  # type: ignore

    def xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_1(
        self, command: ComputeMonthlyIncidentReportCommand
    ) -> ComputeMonthlyIncidentReportResponse:
        now = None
        if command.month:
            month = command.month
        else:
            month = now.strftime("%Y-%m")

        prev_month = _previous_month(now.year, now.month)

        current_raw = self._port.fetch_incidents(month)
        prev_raw = self._port.fetch_incidents(prev_month)

        current: list[dict[str, object]] = [dict(i) for i in current_raw]
        prev: list[dict[str, object]] = [dict(i) for i in prev_raw]

        result = self._engine.compute(current, previous_incidents=prev)
        return ComputeMonthlyIncidentReportResponse(result=result)  # type: ignore

    def xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_2(
        self, command: ComputeMonthlyIncidentReportCommand
    ) -> ComputeMonthlyIncidentReportResponse:
        now = datetime.now(None)
        if command.month:
            month = command.month
        else:
            month = now.strftime("%Y-%m")

        prev_month = _previous_month(now.year, now.month)

        current_raw = self._port.fetch_incidents(month)
        prev_raw = self._port.fetch_incidents(prev_month)

        current: list[dict[str, object]] = [dict(i) for i in current_raw]
        prev: list[dict[str, object]] = [dict(i) for i in prev_raw]

        result = self._engine.compute(current, previous_incidents=prev)
        return ComputeMonthlyIncidentReportResponse(result=result)  # type: ignore

    def xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_3(
        self, command: ComputeMonthlyIncidentReportCommand
    ) -> ComputeMonthlyIncidentReportResponse:
        now = datetime.now(UTC)
        if command.month:
            month = None
        else:
            month = now.strftime("%Y-%m")

        prev_month = _previous_month(now.year, now.month)

        current_raw = self._port.fetch_incidents(month)
        prev_raw = self._port.fetch_incidents(prev_month)

        current: list[dict[str, object]] = [dict(i) for i in current_raw]
        prev: list[dict[str, object]] = [dict(i) for i in prev_raw]

        result = self._engine.compute(current, previous_incidents=prev)
        return ComputeMonthlyIncidentReportResponse(result=result)  # type: ignore

    def xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_4(
        self, command: ComputeMonthlyIncidentReportCommand
    ) -> ComputeMonthlyIncidentReportResponse:
        now = datetime.now(UTC)
        if command.month:
            month = command.month
        else:
            month = None

        prev_month = _previous_month(now.year, now.month)

        current_raw = self._port.fetch_incidents(month)
        prev_raw = self._port.fetch_incidents(prev_month)

        current: list[dict[str, object]] = [dict(i) for i in current_raw]
        prev: list[dict[str, object]] = [dict(i) for i in prev_raw]

        result = self._engine.compute(current, previous_incidents=prev)
        return ComputeMonthlyIncidentReportResponse(result=result)  # type: ignore

    def xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_5(
        self, command: ComputeMonthlyIncidentReportCommand
    ) -> ComputeMonthlyIncidentReportResponse:
        now = datetime.now(UTC)
        if command.month:
            month = command.month
        else:
            month = now.strftime(None)

        prev_month = _previous_month(now.year, now.month)

        current_raw = self._port.fetch_incidents(month)
        prev_raw = self._port.fetch_incidents(prev_month)

        current: list[dict[str, object]] = [dict(i) for i in current_raw]
        prev: list[dict[str, object]] = [dict(i) for i in prev_raw]

        result = self._engine.compute(current, previous_incidents=prev)
        return ComputeMonthlyIncidentReportResponse(result=result)  # type: ignore

    def xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_6(
        self, command: ComputeMonthlyIncidentReportCommand
    ) -> ComputeMonthlyIncidentReportResponse:
        now = datetime.now(UTC)
        if command.month:
            month = command.month
        else:
            month = now.strftime("XX%Y-%mXX")

        prev_month = _previous_month(now.year, now.month)

        current_raw = self._port.fetch_incidents(month)
        prev_raw = self._port.fetch_incidents(prev_month)

        current: list[dict[str, object]] = [dict(i) for i in current_raw]
        prev: list[dict[str, object]] = [dict(i) for i in prev_raw]

        result = self._engine.compute(current, previous_incidents=prev)
        return ComputeMonthlyIncidentReportResponse(result=result)  # type: ignore

    def xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_7(
        self, command: ComputeMonthlyIncidentReportCommand
    ) -> ComputeMonthlyIncidentReportResponse:
        now = datetime.now(UTC)
        if command.month:
            month = command.month
        else:
            month = now.strftime("%y-%m")

        prev_month = _previous_month(now.year, now.month)

        current_raw = self._port.fetch_incidents(month)
        prev_raw = self._port.fetch_incidents(prev_month)

        current: list[dict[str, object]] = [dict(i) for i in current_raw]
        prev: list[dict[str, object]] = [dict(i) for i in prev_raw]

        result = self._engine.compute(current, previous_incidents=prev)
        return ComputeMonthlyIncidentReportResponse(result=result)  # type: ignore

    def xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_8(
        self, command: ComputeMonthlyIncidentReportCommand
    ) -> ComputeMonthlyIncidentReportResponse:
        now = datetime.now(UTC)
        if command.month:
            month = command.month
        else:
            month = now.strftime("%Y-%M")

        prev_month = _previous_month(now.year, now.month)

        current_raw = self._port.fetch_incidents(month)
        prev_raw = self._port.fetch_incidents(prev_month)

        current: list[dict[str, object]] = [dict(i) for i in current_raw]
        prev: list[dict[str, object]] = [dict(i) for i in prev_raw]

        result = self._engine.compute(current, previous_incidents=prev)
        return ComputeMonthlyIncidentReportResponse(result=result)  # type: ignore

    def xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_9(
        self, command: ComputeMonthlyIncidentReportCommand
    ) -> ComputeMonthlyIncidentReportResponse:
        now = datetime.now(UTC)
        if command.month:
            month = command.month
        else:
            month = now.strftime("%Y-%m")

        prev_month = None

        current_raw = self._port.fetch_incidents(month)
        prev_raw = self._port.fetch_incidents(prev_month)

        current: list[dict[str, object]] = [dict(i) for i in current_raw]
        prev: list[dict[str, object]] = [dict(i) for i in prev_raw]

        result = self._engine.compute(current, previous_incidents=prev)
        return ComputeMonthlyIncidentReportResponse(result=result)  # type: ignore

    def xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_10(
        self, command: ComputeMonthlyIncidentReportCommand
    ) -> ComputeMonthlyIncidentReportResponse:
        now = datetime.now(UTC)
        if command.month:
            month = command.month
        else:
            month = now.strftime("%Y-%m")

        prev_month = _previous_month(None, now.month)

        current_raw = self._port.fetch_incidents(month)
        prev_raw = self._port.fetch_incidents(prev_month)

        current: list[dict[str, object]] = [dict(i) for i in current_raw]
        prev: list[dict[str, object]] = [dict(i) for i in prev_raw]

        result = self._engine.compute(current, previous_incidents=prev)
        return ComputeMonthlyIncidentReportResponse(result=result)  # type: ignore

    def xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_11(
        self, command: ComputeMonthlyIncidentReportCommand
    ) -> ComputeMonthlyIncidentReportResponse:
        now = datetime.now(UTC)
        if command.month:
            month = command.month
        else:
            month = now.strftime("%Y-%m")

        prev_month = _previous_month(now.year, None)

        current_raw = self._port.fetch_incidents(month)
        prev_raw = self._port.fetch_incidents(prev_month)

        current: list[dict[str, object]] = [dict(i) for i in current_raw]
        prev: list[dict[str, object]] = [dict(i) for i in prev_raw]

        result = self._engine.compute(current, previous_incidents=prev)
        return ComputeMonthlyIncidentReportResponse(result=result)  # type: ignore

    def xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_12(
        self, command: ComputeMonthlyIncidentReportCommand
    ) -> ComputeMonthlyIncidentReportResponse:
        now = datetime.now(UTC)
        if command.month:
            month = command.month
        else:
            month = now.strftime("%Y-%m")

        prev_month = _previous_month(now.month)

        current_raw = self._port.fetch_incidents(month)
        prev_raw = self._port.fetch_incidents(prev_month)

        current: list[dict[str, object]] = [dict(i) for i in current_raw]
        prev: list[dict[str, object]] = [dict(i) for i in prev_raw]

        result = self._engine.compute(current, previous_incidents=prev)
        return ComputeMonthlyIncidentReportResponse(result=result)  # type: ignore

    def xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_13(
        self, command: ComputeMonthlyIncidentReportCommand
    ) -> ComputeMonthlyIncidentReportResponse:
        now = datetime.now(UTC)
        if command.month:
            month = command.month
        else:
            month = now.strftime("%Y-%m")

        prev_month = _previous_month(now.year, )

        current_raw = self._port.fetch_incidents(month)
        prev_raw = self._port.fetch_incidents(prev_month)

        current: list[dict[str, object]] = [dict(i) for i in current_raw]
        prev: list[dict[str, object]] = [dict(i) for i in prev_raw]

        result = self._engine.compute(current, previous_incidents=prev)
        return ComputeMonthlyIncidentReportResponse(result=result)  # type: ignore

    def xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_14(
        self, command: ComputeMonthlyIncidentReportCommand
    ) -> ComputeMonthlyIncidentReportResponse:
        now = datetime.now(UTC)
        if command.month:
            month = command.month
        else:
            month = now.strftime("%Y-%m")

        prev_month = _previous_month(now.year, now.month)

        current_raw = None
        prev_raw = self._port.fetch_incidents(prev_month)

        current: list[dict[str, object]] = [dict(i) for i in current_raw]
        prev: list[dict[str, object]] = [dict(i) for i in prev_raw]

        result = self._engine.compute(current, previous_incidents=prev)
        return ComputeMonthlyIncidentReportResponse(result=result)  # type: ignore

    def xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_15(
        self, command: ComputeMonthlyIncidentReportCommand
    ) -> ComputeMonthlyIncidentReportResponse:
        now = datetime.now(UTC)
        if command.month:
            month = command.month
        else:
            month = now.strftime("%Y-%m")

        prev_month = _previous_month(now.year, now.month)

        current_raw = self._port.fetch_incidents(None)
        prev_raw = self._port.fetch_incidents(prev_month)

        current: list[dict[str, object]] = [dict(i) for i in current_raw]
        prev: list[dict[str, object]] = [dict(i) for i in prev_raw]

        result = self._engine.compute(current, previous_incidents=prev)
        return ComputeMonthlyIncidentReportResponse(result=result)  # type: ignore

    def xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_16(
        self, command: ComputeMonthlyIncidentReportCommand
    ) -> ComputeMonthlyIncidentReportResponse:
        now = datetime.now(UTC)
        if command.month:
            month = command.month
        else:
            month = now.strftime("%Y-%m")

        prev_month = _previous_month(now.year, now.month)

        current_raw = self._port.fetch_incidents(month)
        prev_raw = None

        current: list[dict[str, object]] = [dict(i) for i in current_raw]
        prev: list[dict[str, object]] = [dict(i) for i in prev_raw]

        result = self._engine.compute(current, previous_incidents=prev)
        return ComputeMonthlyIncidentReportResponse(result=result)  # type: ignore

    def xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_17(
        self, command: ComputeMonthlyIncidentReportCommand
    ) -> ComputeMonthlyIncidentReportResponse:
        now = datetime.now(UTC)
        if command.month:
            month = command.month
        else:
            month = now.strftime("%Y-%m")

        prev_month = _previous_month(now.year, now.month)

        current_raw = self._port.fetch_incidents(month)
        prev_raw = self._port.fetch_incidents(None)

        current: list[dict[str, object]] = [dict(i) for i in current_raw]
        prev: list[dict[str, object]] = [dict(i) for i in prev_raw]

        result = self._engine.compute(current, previous_incidents=prev)
        return ComputeMonthlyIncidentReportResponse(result=result)  # type: ignore

    def xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_18(
        self, command: ComputeMonthlyIncidentReportCommand
    ) -> ComputeMonthlyIncidentReportResponse:
        now = datetime.now(UTC)
        if command.month:
            month = command.month
        else:
            month = now.strftime("%Y-%m")

        prev_month = _previous_month(now.year, now.month)

        current_raw = self._port.fetch_incidents(month)
        prev_raw = self._port.fetch_incidents(prev_month)

        current: list[dict[str, object]] = None
        prev: list[dict[str, object]] = [dict(i) for i in prev_raw]

        result = self._engine.compute(current, previous_incidents=prev)
        return ComputeMonthlyIncidentReportResponse(result=result)  # type: ignore

    def xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_19(
        self, command: ComputeMonthlyIncidentReportCommand
    ) -> ComputeMonthlyIncidentReportResponse:
        now = datetime.now(UTC)
        if command.month:
            month = command.month
        else:
            month = now.strftime("%Y-%m")

        prev_month = _previous_month(now.year, now.month)

        current_raw = self._port.fetch_incidents(month)
        prev_raw = self._port.fetch_incidents(prev_month)

        current: list[dict[str, object]] = [dict(None) for i in current_raw]
        prev: list[dict[str, object]] = [dict(i) for i in prev_raw]

        result = self._engine.compute(current, previous_incidents=prev)
        return ComputeMonthlyIncidentReportResponse(result=result)  # type: ignore

    def xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_20(
        self, command: ComputeMonthlyIncidentReportCommand
    ) -> ComputeMonthlyIncidentReportResponse:
        now = datetime.now(UTC)
        if command.month:
            month = command.month
        else:
            month = now.strftime("%Y-%m")

        prev_month = _previous_month(now.year, now.month)

        current_raw = self._port.fetch_incidents(month)
        prev_raw = self._port.fetch_incidents(prev_month)

        current: list[dict[str, object]] = [dict(i) for i in current_raw]
        prev: list[dict[str, object]] = None

        result = self._engine.compute(current, previous_incidents=prev)
        return ComputeMonthlyIncidentReportResponse(result=result)  # type: ignore

    def xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_21(
        self, command: ComputeMonthlyIncidentReportCommand
    ) -> ComputeMonthlyIncidentReportResponse:
        now = datetime.now(UTC)
        if command.month:
            month = command.month
        else:
            month = now.strftime("%Y-%m")

        prev_month = _previous_month(now.year, now.month)

        current_raw = self._port.fetch_incidents(month)
        prev_raw = self._port.fetch_incidents(prev_month)

        current: list[dict[str, object]] = [dict(i) for i in current_raw]
        prev: list[dict[str, object]] = [dict(None) for i in prev_raw]

        result = self._engine.compute(current, previous_incidents=prev)
        return ComputeMonthlyIncidentReportResponse(result=result)  # type: ignore

    def xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_22(
        self, command: ComputeMonthlyIncidentReportCommand
    ) -> ComputeMonthlyIncidentReportResponse:
        now = datetime.now(UTC)
        if command.month:
            month = command.month
        else:
            month = now.strftime("%Y-%m")

        prev_month = _previous_month(now.year, now.month)

        current_raw = self._port.fetch_incidents(month)
        prev_raw = self._port.fetch_incidents(prev_month)

        current: list[dict[str, object]] = [dict(i) for i in current_raw]
        prev: list[dict[str, object]] = [dict(i) for i in prev_raw]

        result = None
        return ComputeMonthlyIncidentReportResponse(result=result)  # type: ignore

    def xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_23(
        self, command: ComputeMonthlyIncidentReportCommand
    ) -> ComputeMonthlyIncidentReportResponse:
        now = datetime.now(UTC)
        if command.month:
            month = command.month
        else:
            month = now.strftime("%Y-%m")

        prev_month = _previous_month(now.year, now.month)

        current_raw = self._port.fetch_incidents(month)
        prev_raw = self._port.fetch_incidents(prev_month)

        current: list[dict[str, object]] = [dict(i) for i in current_raw]
        prev: list[dict[str, object]] = [dict(i) for i in prev_raw]

        result = self._engine.compute(None, previous_incidents=prev)
        return ComputeMonthlyIncidentReportResponse(result=result)  # type: ignore

    def xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_24(
        self, command: ComputeMonthlyIncidentReportCommand
    ) -> ComputeMonthlyIncidentReportResponse:
        now = datetime.now(UTC)
        if command.month:
            month = command.month
        else:
            month = now.strftime("%Y-%m")

        prev_month = _previous_month(now.year, now.month)

        current_raw = self._port.fetch_incidents(month)
        prev_raw = self._port.fetch_incidents(prev_month)

        current: list[dict[str, object]] = [dict(i) for i in current_raw]
        prev: list[dict[str, object]] = [dict(i) for i in prev_raw]

        result = self._engine.compute(current, previous_incidents=None)
        return ComputeMonthlyIncidentReportResponse(result=result)  # type: ignore

    def xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_25(
        self, command: ComputeMonthlyIncidentReportCommand
    ) -> ComputeMonthlyIncidentReportResponse:
        now = datetime.now(UTC)
        if command.month:
            month = command.month
        else:
            month = now.strftime("%Y-%m")

        prev_month = _previous_month(now.year, now.month)

        current_raw = self._port.fetch_incidents(month)
        prev_raw = self._port.fetch_incidents(prev_month)

        current: list[dict[str, object]] = [dict(i) for i in current_raw]
        prev: list[dict[str, object]] = [dict(i) for i in prev_raw]

        result = self._engine.compute(previous_incidents=prev)
        return ComputeMonthlyIncidentReportResponse(result=result)  # type: ignore

    def xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_26(
        self, command: ComputeMonthlyIncidentReportCommand
    ) -> ComputeMonthlyIncidentReportResponse:
        now = datetime.now(UTC)
        if command.month:
            month = command.month
        else:
            month = now.strftime("%Y-%m")

        prev_month = _previous_month(now.year, now.month)

        current_raw = self._port.fetch_incidents(month)
        prev_raw = self._port.fetch_incidents(prev_month)

        current: list[dict[str, object]] = [dict(i) for i in current_raw]
        prev: list[dict[str, object]] = [dict(i) for i in prev_raw]

        result = self._engine.compute(current, )
        return ComputeMonthlyIncidentReportResponse(result=result)  # type: ignore

    def xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_27(
        self, command: ComputeMonthlyIncidentReportCommand
    ) -> ComputeMonthlyIncidentReportResponse:
        now = datetime.now(UTC)
        if command.month:
            month = command.month
        else:
            month = now.strftime("%Y-%m")

        prev_month = _previous_month(now.year, now.month)

        current_raw = self._port.fetch_incidents(month)
        prev_raw = self._port.fetch_incidents(prev_month)

        current: list[dict[str, object]] = [dict(i) for i in current_raw]
        prev: list[dict[str, object]] = [dict(i) for i in prev_raw]

        result = self._engine.compute(current, previous_incidents=prev)
        return ComputeMonthlyIncidentReportResponse(result=None)  # type: ignore

mutants_xǁComputeMonthlyIncidentReportUseCaseǁ__init____mutmut['_mutmut_orig'] = ComputeMonthlyIncidentReportUseCase.xǁComputeMonthlyIncidentReportUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁComputeMonthlyIncidentReportUseCaseǁ__init____mutmut['xǁComputeMonthlyIncidentReportUseCaseǁ__init____mutmut_1'] = ComputeMonthlyIncidentReportUseCase.xǁComputeMonthlyIncidentReportUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁComputeMonthlyIncidentReportUseCaseǁ__init____mutmut['xǁComputeMonthlyIncidentReportUseCaseǁ__init____mutmut_2'] = ComputeMonthlyIncidentReportUseCase.xǁComputeMonthlyIncidentReportUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut['_mutmut_orig'] = ComputeMonthlyIncidentReportUseCase.xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut['xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_1'] = ComputeMonthlyIncidentReportUseCase.xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut['xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_2'] = ComputeMonthlyIncidentReportUseCase.xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut['xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_3'] = ComputeMonthlyIncidentReportUseCase.xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut['xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_4'] = ComputeMonthlyIncidentReportUseCase.xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut['xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_5'] = ComputeMonthlyIncidentReportUseCase.xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut['xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_6'] = ComputeMonthlyIncidentReportUseCase.xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut['xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_7'] = ComputeMonthlyIncidentReportUseCase.xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut['xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_8'] = ComputeMonthlyIncidentReportUseCase.xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut['xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_9'] = ComputeMonthlyIncidentReportUseCase.xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut['xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_10'] = ComputeMonthlyIncidentReportUseCase.xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut['xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_11'] = ComputeMonthlyIncidentReportUseCase.xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut['xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_12'] = ComputeMonthlyIncidentReportUseCase.xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut['xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_13'] = ComputeMonthlyIncidentReportUseCase.xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut['xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_14'] = ComputeMonthlyIncidentReportUseCase.xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut['xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_15'] = ComputeMonthlyIncidentReportUseCase.xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut['xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_16'] = ComputeMonthlyIncidentReportUseCase.xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut['xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_17'] = ComputeMonthlyIncidentReportUseCase.xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut['xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_18'] = ComputeMonthlyIncidentReportUseCase.xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut['xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_19'] = ComputeMonthlyIncidentReportUseCase.xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut['xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_20'] = ComputeMonthlyIncidentReportUseCase.xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut['xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_21'] = ComputeMonthlyIncidentReportUseCase.xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut['xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_22'] = ComputeMonthlyIncidentReportUseCase.xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut['xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_23'] = ComputeMonthlyIncidentReportUseCase.xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut['xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_24'] = ComputeMonthlyIncidentReportUseCase.xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut['xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_25'] = ComputeMonthlyIncidentReportUseCase.xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut['xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_26'] = ComputeMonthlyIncidentReportUseCase.xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut['xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_27'] = ComputeMonthlyIncidentReportUseCase.xǁComputeMonthlyIncidentReportUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_x__previous_month__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__previous_month__mutmut)
def _previous_month(year: int, month: int) -> str:
    if month == 1:
        return f"{year - 1}-12"
    return f"{year}-{month - 1:02d}"


def x__previous_month__mutmut_orig(year: int, month: int) -> str:
    if month == 1:
        return f"{year - 1}-12"
    return f"{year}-{month - 1:02d}"


def x__previous_month__mutmut_1(year: int, month: int) -> str:
    if month != 1:
        return f"{year - 1}-12"
    return f"{year}-{month - 1:02d}"


def x__previous_month__mutmut_2(year: int, month: int) -> str:
    if month == 2:
        return f"{year - 1}-12"
    return f"{year}-{month - 1:02d}"


def x__previous_month__mutmut_3(year: int, month: int) -> str:
    if month == 1:
        return f"{year + 1}-12"
    return f"{year}-{month - 1:02d}"


def x__previous_month__mutmut_4(year: int, month: int) -> str:
    if month == 1:
        return f"{year - 2}-12"
    return f"{year}-{month - 1:02d}"


def x__previous_month__mutmut_5(year: int, month: int) -> str:
    if month == 1:
        return f"{year - 1}-12"
    return f"{year}-{month + 1:02d}"


def x__previous_month__mutmut_6(year: int, month: int) -> str:
    if month == 1:
        return f"{year - 1}-12"
    return f"{year}-{month - 2:02d}"

mutants_x__previous_month__mutmut['_mutmut_orig'] = x__previous_month__mutmut_orig # type: ignore # mutmut generated
mutants_x__previous_month__mutmut['x__previous_month__mutmut_1'] = x__previous_month__mutmut_1 # type: ignore # mutmut generated
mutants_x__previous_month__mutmut['x__previous_month__mutmut_2'] = x__previous_month__mutmut_2 # type: ignore # mutmut generated
mutants_x__previous_month__mutmut['x__previous_month__mutmut_3'] = x__previous_month__mutmut_3 # type: ignore # mutmut generated
mutants_x__previous_month__mutmut['x__previous_month__mutmut_4'] = x__previous_month__mutmut_4 # type: ignore # mutmut generated
mutants_x__previous_month__mutmut['x__previous_month__mutmut_5'] = x__previous_month__mutmut_5 # type: ignore # mutmut generated
mutants_x__previous_month__mutmut['x__previous_month__mutmut_6'] = x__previous_month__mutmut_6 # type: ignore # mutmut generated
