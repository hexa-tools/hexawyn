from __future__ import annotations

from datetime import UTC, datetime

from hexawyn.application.ports.driven.mttr_trend_port import MTTRTrendPort
from hexawyn.application.use_case.workloads.compute_mttr_trend.command import (
    ComputeMTTRTrendCommand,
)
from hexawyn.application.use_case.workloads.compute_mttr_trend.response import (
    ComputeMTTRTrendResponse,
)
from hexawyn.domain.services.mttr_trend.mttr_trend_engine import MTTRTrendEngine


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁComputeMTTRTrendUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁComputeMTTRTrendUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class ComputeMTTRTrendUseCase:
    @_mutmut_mutated(mutants_xǁComputeMTTRTrendUseCaseǁ__init____mutmut)
    def __init__(self, mttr_port: MTTRTrendPort) -> None:
        self._port = mttr_port
        self._engine = MTTRTrendEngine()
    def xǁComputeMTTRTrendUseCaseǁ__init____mutmut_orig(self, mttr_port: MTTRTrendPort) -> None:
        self._port = mttr_port
        self._engine = MTTRTrendEngine()
    def xǁComputeMTTRTrendUseCaseǁ__init____mutmut_1(self, mttr_port: MTTRTrendPort) -> None:
        self._port = None
        self._engine = MTTRTrendEngine()
    def xǁComputeMTTRTrendUseCaseǁ__init____mutmut_2(self, mttr_port: MTTRTrendPort) -> None:
        self._port = mttr_port
        self._engine = None

    @_mutmut_mutated(mutants_xǁComputeMTTRTrendUseCaseǁexecute__mutmut)
    def execute(self, command: ComputeMTTRTrendCommand) -> ComputeMTTRTrendResponse:
        now = datetime.now(UTC)
        if command.months:
            months = command.months
        else:
            months = _last_3_months(now.year, now.month)

        months_data: dict[str, list[dict[str, object]]] = {}
        for month in months:
            raw = self._port.fetch_incidents_by_month(month)
            months_data[month] = [dict(i) for i in raw]

        result = self._engine.compute(months_data)
        return ComputeMTTRTrendResponse(result=result)  # type: ignore

    def xǁComputeMTTRTrendUseCaseǁexecute__mutmut_orig(self, command: ComputeMTTRTrendCommand) -> ComputeMTTRTrendResponse:
        now = datetime.now(UTC)
        if command.months:
            months = command.months
        else:
            months = _last_3_months(now.year, now.month)

        months_data: dict[str, list[dict[str, object]]] = {}
        for month in months:
            raw = self._port.fetch_incidents_by_month(month)
            months_data[month] = [dict(i) for i in raw]

        result = self._engine.compute(months_data)
        return ComputeMTTRTrendResponse(result=result)  # type: ignore

    def xǁComputeMTTRTrendUseCaseǁexecute__mutmut_1(self, command: ComputeMTTRTrendCommand) -> ComputeMTTRTrendResponse:
        now = None
        if command.months:
            months = command.months
        else:
            months = _last_3_months(now.year, now.month)

        months_data: dict[str, list[dict[str, object]]] = {}
        for month in months:
            raw = self._port.fetch_incidents_by_month(month)
            months_data[month] = [dict(i) for i in raw]

        result = self._engine.compute(months_data)
        return ComputeMTTRTrendResponse(result=result)  # type: ignore

    def xǁComputeMTTRTrendUseCaseǁexecute__mutmut_2(self, command: ComputeMTTRTrendCommand) -> ComputeMTTRTrendResponse:
        now = datetime.now(None)
        if command.months:
            months = command.months
        else:
            months = _last_3_months(now.year, now.month)

        months_data: dict[str, list[dict[str, object]]] = {}
        for month in months:
            raw = self._port.fetch_incidents_by_month(month)
            months_data[month] = [dict(i) for i in raw]

        result = self._engine.compute(months_data)
        return ComputeMTTRTrendResponse(result=result)  # type: ignore

    def xǁComputeMTTRTrendUseCaseǁexecute__mutmut_3(self, command: ComputeMTTRTrendCommand) -> ComputeMTTRTrendResponse:
        now = datetime.now(UTC)
        if command.months:
            months = None
        else:
            months = _last_3_months(now.year, now.month)

        months_data: dict[str, list[dict[str, object]]] = {}
        for month in months:
            raw = self._port.fetch_incidents_by_month(month)
            months_data[month] = [dict(i) for i in raw]

        result = self._engine.compute(months_data)
        return ComputeMTTRTrendResponse(result=result)  # type: ignore

    def xǁComputeMTTRTrendUseCaseǁexecute__mutmut_4(self, command: ComputeMTTRTrendCommand) -> ComputeMTTRTrendResponse:
        now = datetime.now(UTC)
        if command.months:
            months = command.months
        else:
            months = None

        months_data: dict[str, list[dict[str, object]]] = {}
        for month in months:
            raw = self._port.fetch_incidents_by_month(month)
            months_data[month] = [dict(i) for i in raw]

        result = self._engine.compute(months_data)
        return ComputeMTTRTrendResponse(result=result)  # type: ignore

    def xǁComputeMTTRTrendUseCaseǁexecute__mutmut_5(self, command: ComputeMTTRTrendCommand) -> ComputeMTTRTrendResponse:
        now = datetime.now(UTC)
        if command.months:
            months = command.months
        else:
            months = _last_3_months(None, now.month)

        months_data: dict[str, list[dict[str, object]]] = {}
        for month in months:
            raw = self._port.fetch_incidents_by_month(month)
            months_data[month] = [dict(i) for i in raw]

        result = self._engine.compute(months_data)
        return ComputeMTTRTrendResponse(result=result)  # type: ignore

    def xǁComputeMTTRTrendUseCaseǁexecute__mutmut_6(self, command: ComputeMTTRTrendCommand) -> ComputeMTTRTrendResponse:
        now = datetime.now(UTC)
        if command.months:
            months = command.months
        else:
            months = _last_3_months(now.year, None)

        months_data: dict[str, list[dict[str, object]]] = {}
        for month in months:
            raw = self._port.fetch_incidents_by_month(month)
            months_data[month] = [dict(i) for i in raw]

        result = self._engine.compute(months_data)
        return ComputeMTTRTrendResponse(result=result)  # type: ignore

    def xǁComputeMTTRTrendUseCaseǁexecute__mutmut_7(self, command: ComputeMTTRTrendCommand) -> ComputeMTTRTrendResponse:
        now = datetime.now(UTC)
        if command.months:
            months = command.months
        else:
            months = _last_3_months(now.month)

        months_data: dict[str, list[dict[str, object]]] = {}
        for month in months:
            raw = self._port.fetch_incidents_by_month(month)
            months_data[month] = [dict(i) for i in raw]

        result = self._engine.compute(months_data)
        return ComputeMTTRTrendResponse(result=result)  # type: ignore

    def xǁComputeMTTRTrendUseCaseǁexecute__mutmut_8(self, command: ComputeMTTRTrendCommand) -> ComputeMTTRTrendResponse:
        now = datetime.now(UTC)
        if command.months:
            months = command.months
        else:
            months = _last_3_months(now.year, )

        months_data: dict[str, list[dict[str, object]]] = {}
        for month in months:
            raw = self._port.fetch_incidents_by_month(month)
            months_data[month] = [dict(i) for i in raw]

        result = self._engine.compute(months_data)
        return ComputeMTTRTrendResponse(result=result)  # type: ignore

    def xǁComputeMTTRTrendUseCaseǁexecute__mutmut_9(self, command: ComputeMTTRTrendCommand) -> ComputeMTTRTrendResponse:
        now = datetime.now(UTC)
        if command.months:
            months = command.months
        else:
            months = _last_3_months(now.year, now.month)

        months_data: dict[str, list[dict[str, object]]] = None
        for month in months:
            raw = self._port.fetch_incidents_by_month(month)
            months_data[month] = [dict(i) for i in raw]

        result = self._engine.compute(months_data)
        return ComputeMTTRTrendResponse(result=result)  # type: ignore

    def xǁComputeMTTRTrendUseCaseǁexecute__mutmut_10(self, command: ComputeMTTRTrendCommand) -> ComputeMTTRTrendResponse:
        now = datetime.now(UTC)
        if command.months:
            months = command.months
        else:
            months = _last_3_months(now.year, now.month)

        months_data: dict[str, list[dict[str, object]]] = {}
        for month in months:
            raw = None
            months_data[month] = [dict(i) for i in raw]

        result = self._engine.compute(months_data)
        return ComputeMTTRTrendResponse(result=result)  # type: ignore

    def xǁComputeMTTRTrendUseCaseǁexecute__mutmut_11(self, command: ComputeMTTRTrendCommand) -> ComputeMTTRTrendResponse:
        now = datetime.now(UTC)
        if command.months:
            months = command.months
        else:
            months = _last_3_months(now.year, now.month)

        months_data: dict[str, list[dict[str, object]]] = {}
        for month in months:
            raw = self._port.fetch_incidents_by_month(None)
            months_data[month] = [dict(i) for i in raw]

        result = self._engine.compute(months_data)
        return ComputeMTTRTrendResponse(result=result)  # type: ignore

    def xǁComputeMTTRTrendUseCaseǁexecute__mutmut_12(self, command: ComputeMTTRTrendCommand) -> ComputeMTTRTrendResponse:
        now = datetime.now(UTC)
        if command.months:
            months = command.months
        else:
            months = _last_3_months(now.year, now.month)

        months_data: dict[str, list[dict[str, object]]] = {}
        for month in months:
            raw = self._port.fetch_incidents_by_month(month)
            months_data[month] = None

        result = self._engine.compute(months_data)
        return ComputeMTTRTrendResponse(result=result)  # type: ignore

    def xǁComputeMTTRTrendUseCaseǁexecute__mutmut_13(self, command: ComputeMTTRTrendCommand) -> ComputeMTTRTrendResponse:
        now = datetime.now(UTC)
        if command.months:
            months = command.months
        else:
            months = _last_3_months(now.year, now.month)

        months_data: dict[str, list[dict[str, object]]] = {}
        for month in months:
            raw = self._port.fetch_incidents_by_month(month)
            months_data[month] = [dict(None) for i in raw]

        result = self._engine.compute(months_data)
        return ComputeMTTRTrendResponse(result=result)  # type: ignore

    def xǁComputeMTTRTrendUseCaseǁexecute__mutmut_14(self, command: ComputeMTTRTrendCommand) -> ComputeMTTRTrendResponse:
        now = datetime.now(UTC)
        if command.months:
            months = command.months
        else:
            months = _last_3_months(now.year, now.month)

        months_data: dict[str, list[dict[str, object]]] = {}
        for month in months:
            raw = self._port.fetch_incidents_by_month(month)
            months_data[month] = [dict(i) for i in raw]

        result = None
        return ComputeMTTRTrendResponse(result=result)  # type: ignore

    def xǁComputeMTTRTrendUseCaseǁexecute__mutmut_15(self, command: ComputeMTTRTrendCommand) -> ComputeMTTRTrendResponse:
        now = datetime.now(UTC)
        if command.months:
            months = command.months
        else:
            months = _last_3_months(now.year, now.month)

        months_data: dict[str, list[dict[str, object]]] = {}
        for month in months:
            raw = self._port.fetch_incidents_by_month(month)
            months_data[month] = [dict(i) for i in raw]

        result = self._engine.compute(None)
        return ComputeMTTRTrendResponse(result=result)  # type: ignore

    def xǁComputeMTTRTrendUseCaseǁexecute__mutmut_16(self, command: ComputeMTTRTrendCommand) -> ComputeMTTRTrendResponse:
        now = datetime.now(UTC)
        if command.months:
            months = command.months
        else:
            months = _last_3_months(now.year, now.month)

        months_data: dict[str, list[dict[str, object]]] = {}
        for month in months:
            raw = self._port.fetch_incidents_by_month(month)
            months_data[month] = [dict(i) for i in raw]

        result = self._engine.compute(months_data)
        return ComputeMTTRTrendResponse(result=None)  # type: ignore

mutants_xǁComputeMTTRTrendUseCaseǁ__init____mutmut['_mutmut_orig'] = ComputeMTTRTrendUseCase.xǁComputeMTTRTrendUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁComputeMTTRTrendUseCaseǁ__init____mutmut['xǁComputeMTTRTrendUseCaseǁ__init____mutmut_1'] = ComputeMTTRTrendUseCase.xǁComputeMTTRTrendUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁComputeMTTRTrendUseCaseǁ__init____mutmut['xǁComputeMTTRTrendUseCaseǁ__init____mutmut_2'] = ComputeMTTRTrendUseCase.xǁComputeMTTRTrendUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁComputeMTTRTrendUseCaseǁexecute__mutmut['_mutmut_orig'] = ComputeMTTRTrendUseCase.xǁComputeMTTRTrendUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁComputeMTTRTrendUseCaseǁexecute__mutmut['xǁComputeMTTRTrendUseCaseǁexecute__mutmut_1'] = ComputeMTTRTrendUseCase.xǁComputeMTTRTrendUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁComputeMTTRTrendUseCaseǁexecute__mutmut['xǁComputeMTTRTrendUseCaseǁexecute__mutmut_2'] = ComputeMTTRTrendUseCase.xǁComputeMTTRTrendUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁComputeMTTRTrendUseCaseǁexecute__mutmut['xǁComputeMTTRTrendUseCaseǁexecute__mutmut_3'] = ComputeMTTRTrendUseCase.xǁComputeMTTRTrendUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁComputeMTTRTrendUseCaseǁexecute__mutmut['xǁComputeMTTRTrendUseCaseǁexecute__mutmut_4'] = ComputeMTTRTrendUseCase.xǁComputeMTTRTrendUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁComputeMTTRTrendUseCaseǁexecute__mutmut['xǁComputeMTTRTrendUseCaseǁexecute__mutmut_5'] = ComputeMTTRTrendUseCase.xǁComputeMTTRTrendUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁComputeMTTRTrendUseCaseǁexecute__mutmut['xǁComputeMTTRTrendUseCaseǁexecute__mutmut_6'] = ComputeMTTRTrendUseCase.xǁComputeMTTRTrendUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁComputeMTTRTrendUseCaseǁexecute__mutmut['xǁComputeMTTRTrendUseCaseǁexecute__mutmut_7'] = ComputeMTTRTrendUseCase.xǁComputeMTTRTrendUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁComputeMTTRTrendUseCaseǁexecute__mutmut['xǁComputeMTTRTrendUseCaseǁexecute__mutmut_8'] = ComputeMTTRTrendUseCase.xǁComputeMTTRTrendUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁComputeMTTRTrendUseCaseǁexecute__mutmut['xǁComputeMTTRTrendUseCaseǁexecute__mutmut_9'] = ComputeMTTRTrendUseCase.xǁComputeMTTRTrendUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁComputeMTTRTrendUseCaseǁexecute__mutmut['xǁComputeMTTRTrendUseCaseǁexecute__mutmut_10'] = ComputeMTTRTrendUseCase.xǁComputeMTTRTrendUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁComputeMTTRTrendUseCaseǁexecute__mutmut['xǁComputeMTTRTrendUseCaseǁexecute__mutmut_11'] = ComputeMTTRTrendUseCase.xǁComputeMTTRTrendUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁComputeMTTRTrendUseCaseǁexecute__mutmut['xǁComputeMTTRTrendUseCaseǁexecute__mutmut_12'] = ComputeMTTRTrendUseCase.xǁComputeMTTRTrendUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁComputeMTTRTrendUseCaseǁexecute__mutmut['xǁComputeMTTRTrendUseCaseǁexecute__mutmut_13'] = ComputeMTTRTrendUseCase.xǁComputeMTTRTrendUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁComputeMTTRTrendUseCaseǁexecute__mutmut['xǁComputeMTTRTrendUseCaseǁexecute__mutmut_14'] = ComputeMTTRTrendUseCase.xǁComputeMTTRTrendUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁComputeMTTRTrendUseCaseǁexecute__mutmut['xǁComputeMTTRTrendUseCaseǁexecute__mutmut_15'] = ComputeMTTRTrendUseCase.xǁComputeMTTRTrendUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁComputeMTTRTrendUseCaseǁexecute__mutmut['xǁComputeMTTRTrendUseCaseǁexecute__mutmut_16'] = ComputeMTTRTrendUseCase.xǁComputeMTTRTrendUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_x__last_3_months__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__last_3_months__mutmut)
def _last_3_months(year: int, month: int) -> list[str]:
    result = []
    y, m = year, month
    for _ in range(3):
        result.append(f"{y}-{m:02d}")
        if m == 1:
            m = 12
            y -= 1
        else:
            m -= 1
    result.reverse()
    return result


def x__last_3_months__mutmut_orig(year: int, month: int) -> list[str]:
    result = []
    y, m = year, month
    for _ in range(3):
        result.append(f"{y}-{m:02d}")
        if m == 1:
            m = 12
            y -= 1
        else:
            m -= 1
    result.reverse()
    return result


def x__last_3_months__mutmut_1(year: int, month: int) -> list[str]:
    result = None
    y, m = year, month
    for _ in range(3):
        result.append(f"{y}-{m:02d}")
        if m == 1:
            m = 12
            y -= 1
        else:
            m -= 1
    result.reverse()
    return result


def x__last_3_months__mutmut_2(year: int, month: int) -> list[str]:
    result = []
    y, m = None
    for _ in range(3):
        result.append(f"{y}-{m:02d}")
        if m == 1:
            m = 12
            y -= 1
        else:
            m -= 1
    result.reverse()
    return result


def x__last_3_months__mutmut_3(year: int, month: int) -> list[str]:
    result = []
    y, m = year, month
    for _ in range(None):
        result.append(f"{y}-{m:02d}")
        if m == 1:
            m = 12
            y -= 1
        else:
            m -= 1
    result.reverse()
    return result


def x__last_3_months__mutmut_4(year: int, month: int) -> list[str]:
    result = []
    y, m = year, month
    for _ in range(4):
        result.append(f"{y}-{m:02d}")
        if m == 1:
            m = 12
            y -= 1
        else:
            m -= 1
    result.reverse()
    return result


def x__last_3_months__mutmut_5(year: int, month: int) -> list[str]:
    result = []
    y, m = year, month
    for _ in range(3):
        result.append(None)
        if m == 1:
            m = 12
            y -= 1
        else:
            m -= 1
    result.reverse()
    return result


def x__last_3_months__mutmut_6(year: int, month: int) -> list[str]:
    result = []
    y, m = year, month
    for _ in range(3):
        result.append(f"{y}-{m:02d}")
        if m != 1:
            m = 12
            y -= 1
        else:
            m -= 1
    result.reverse()
    return result


def x__last_3_months__mutmut_7(year: int, month: int) -> list[str]:
    result = []
    y, m = year, month
    for _ in range(3):
        result.append(f"{y}-{m:02d}")
        if m == 2:
            m = 12
            y -= 1
        else:
            m -= 1
    result.reverse()
    return result


def x__last_3_months__mutmut_8(year: int, month: int) -> list[str]:
    result = []
    y, m = year, month
    for _ in range(3):
        result.append(f"{y}-{m:02d}")
        if m == 1:
            m = None
            y -= 1
        else:
            m -= 1
    result.reverse()
    return result


def x__last_3_months__mutmut_9(year: int, month: int) -> list[str]:
    result = []
    y, m = year, month
    for _ in range(3):
        result.append(f"{y}-{m:02d}")
        if m == 1:
            m = 13
            y -= 1
        else:
            m -= 1
    result.reverse()
    return result


def x__last_3_months__mutmut_10(year: int, month: int) -> list[str]:
    result = []
    y, m = year, month
    for _ in range(3):
        result.append(f"{y}-{m:02d}")
        if m == 1:
            m = 12
            y = 1
        else:
            m -= 1
    result.reverse()
    return result


def x__last_3_months__mutmut_11(year: int, month: int) -> list[str]:
    result = []
    y, m = year, month
    for _ in range(3):
        result.append(f"{y}-{m:02d}")
        if m == 1:
            m = 12
            y += 1
        else:
            m -= 1
    result.reverse()
    return result


def x__last_3_months__mutmut_12(year: int, month: int) -> list[str]:
    result = []
    y, m = year, month
    for _ in range(3):
        result.append(f"{y}-{m:02d}")
        if m == 1:
            m = 12
            y -= 2
        else:
            m -= 1
    result.reverse()
    return result


def x__last_3_months__mutmut_13(year: int, month: int) -> list[str]:
    result = []
    y, m = year, month
    for _ in range(3):
        result.append(f"{y}-{m:02d}")
        if m == 1:
            m = 12
            y -= 1
        else:
            m = 1
    result.reverse()
    return result


def x__last_3_months__mutmut_14(year: int, month: int) -> list[str]:
    result = []
    y, m = year, month
    for _ in range(3):
        result.append(f"{y}-{m:02d}")
        if m == 1:
            m = 12
            y -= 1
        else:
            m += 1
    result.reverse()
    return result


def x__last_3_months__mutmut_15(year: int, month: int) -> list[str]:
    result = []
    y, m = year, month
    for _ in range(3):
        result.append(f"{y}-{m:02d}")
        if m == 1:
            m = 12
            y -= 1
        else:
            m -= 2
    result.reverse()
    return result

mutants_x__last_3_months__mutmut['_mutmut_orig'] = x__last_3_months__mutmut_orig # type: ignore # mutmut generated
mutants_x__last_3_months__mutmut['x__last_3_months__mutmut_1'] = x__last_3_months__mutmut_1 # type: ignore # mutmut generated
mutants_x__last_3_months__mutmut['x__last_3_months__mutmut_2'] = x__last_3_months__mutmut_2 # type: ignore # mutmut generated
mutants_x__last_3_months__mutmut['x__last_3_months__mutmut_3'] = x__last_3_months__mutmut_3 # type: ignore # mutmut generated
mutants_x__last_3_months__mutmut['x__last_3_months__mutmut_4'] = x__last_3_months__mutmut_4 # type: ignore # mutmut generated
mutants_x__last_3_months__mutmut['x__last_3_months__mutmut_5'] = x__last_3_months__mutmut_5 # type: ignore # mutmut generated
mutants_x__last_3_months__mutmut['x__last_3_months__mutmut_6'] = x__last_3_months__mutmut_6 # type: ignore # mutmut generated
mutants_x__last_3_months__mutmut['x__last_3_months__mutmut_7'] = x__last_3_months__mutmut_7 # type: ignore # mutmut generated
mutants_x__last_3_months__mutmut['x__last_3_months__mutmut_8'] = x__last_3_months__mutmut_8 # type: ignore # mutmut generated
mutants_x__last_3_months__mutmut['x__last_3_months__mutmut_9'] = x__last_3_months__mutmut_9 # type: ignore # mutmut generated
mutants_x__last_3_months__mutmut['x__last_3_months__mutmut_10'] = x__last_3_months__mutmut_10 # type: ignore # mutmut generated
mutants_x__last_3_months__mutmut['x__last_3_months__mutmut_11'] = x__last_3_months__mutmut_11 # type: ignore # mutmut generated
mutants_x__last_3_months__mutmut['x__last_3_months__mutmut_12'] = x__last_3_months__mutmut_12 # type: ignore # mutmut generated
mutants_x__last_3_months__mutmut['x__last_3_months__mutmut_13'] = x__last_3_months__mutmut_13 # type: ignore # mutmut generated
mutants_x__last_3_months__mutmut['x__last_3_months__mutmut_14'] = x__last_3_months__mutmut_14 # type: ignore # mutmut generated
mutants_x__last_3_months__mutmut['x__last_3_months__mutmut_15'] = x__last_3_months__mutmut_15 # type: ignore # mutmut generated
