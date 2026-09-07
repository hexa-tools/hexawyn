from __future__ import annotations

from hexawyn.application.ports.driven.weekly_reliability_report_port import (
    WeeklyReliabilityReportPort,
)
from hexawyn.application.use_case.workloads.generate_weekly_reliability_report.command import (
    GenerateWeeklyReliabilityReportCommand,
)
from hexawyn.application.use_case.workloads.generate_weekly_reliability_report.response import (
    GenerateWeeklyReliabilityReportResponse,
)
from hexawyn.domain.services.reliability_report.weekly_reliability_report_engine import (
    WeeklyReliabilityReportEngine,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁGenerateWeeklyReliabilityReportUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut: MutantDict = {}  # type: ignore


class GenerateWeeklyReliabilityReportUseCase:
    @_mutmut_mutated(mutants_xǁGenerateWeeklyReliabilityReportUseCaseǁ__init____mutmut)
    def __init__(self, reliability_port: WeeklyReliabilityReportPort) -> None:
        self._port = reliability_port
        self._engine = WeeklyReliabilityReportEngine()
    def xǁGenerateWeeklyReliabilityReportUseCaseǁ__init____mutmut_orig(self, reliability_port: WeeklyReliabilityReportPort) -> None:
        self._port = reliability_port
        self._engine = WeeklyReliabilityReportEngine()
    def xǁGenerateWeeklyReliabilityReportUseCaseǁ__init____mutmut_1(self, reliability_port: WeeklyReliabilityReportPort) -> None:
        self._port = None
        self._engine = WeeklyReliabilityReportEngine()
    def xǁGenerateWeeklyReliabilityReportUseCaseǁ__init____mutmut_2(self, reliability_port: WeeklyReliabilityReportPort) -> None:
        self._port = reliability_port
        self._engine = None

    @_mutmut_mutated(mutants_xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut)
    def generate_report(
        self, command: GenerateWeeklyReliabilityReportCommand
    ) -> GenerateWeeklyReliabilityReportResponse:
        services_raw = self._port.fetch_service_reliability(command.window_days)  # type: ignore
        incidents_raw = self._port.fetch_incidents(command.window_days)  # type: ignore

        services: list[dict[str, object]] = [dict(s) for s in services_raw]
        incidents: list[dict[str, object]] = [dict(i) for i in incidents_raw]

        result = self._engine.compute(services, incidents)
        return GenerateWeeklyReliabilityReportResponse(result=result)  # type: ignore

    def xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_orig(
        self, command: GenerateWeeklyReliabilityReportCommand
    ) -> GenerateWeeklyReliabilityReportResponse:
        services_raw = self._port.fetch_service_reliability(command.window_days)  # type: ignore
        incidents_raw = self._port.fetch_incidents(command.window_days)  # type: ignore

        services: list[dict[str, object]] = [dict(s) for s in services_raw]
        incidents: list[dict[str, object]] = [dict(i) for i in incidents_raw]

        result = self._engine.compute(services, incidents)
        return GenerateWeeklyReliabilityReportResponse(result=result)  # type: ignore

    def xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_1(
        self, command: GenerateWeeklyReliabilityReportCommand
    ) -> GenerateWeeklyReliabilityReportResponse:
        services_raw = None  # type: ignore
        incidents_raw = self._port.fetch_incidents(command.window_days)  # type: ignore

        services: list[dict[str, object]] = [dict(s) for s in services_raw]
        incidents: list[dict[str, object]] = [dict(i) for i in incidents_raw]

        result = self._engine.compute(services, incidents)
        return GenerateWeeklyReliabilityReportResponse(result=result)  # type: ignore

    def xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_2(
        self, command: GenerateWeeklyReliabilityReportCommand
    ) -> GenerateWeeklyReliabilityReportResponse:
        services_raw = self._port.fetch_service_reliability(None)  # type: ignore
        incidents_raw = self._port.fetch_incidents(command.window_days)  # type: ignore

        services: list[dict[str, object]] = [dict(s) for s in services_raw]
        incidents: list[dict[str, object]] = [dict(i) for i in incidents_raw]

        result = self._engine.compute(services, incidents)
        return GenerateWeeklyReliabilityReportResponse(result=result)  # type: ignore

    def xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_3(
        self, command: GenerateWeeklyReliabilityReportCommand
    ) -> GenerateWeeklyReliabilityReportResponse:
        services_raw = self._port.fetch_service_reliability(command.window_days)  # type: ignore
        incidents_raw = None  # type: ignore

        services: list[dict[str, object]] = [dict(s) for s in services_raw]
        incidents: list[dict[str, object]] = [dict(i) for i in incidents_raw]

        result = self._engine.compute(services, incidents)
        return GenerateWeeklyReliabilityReportResponse(result=result)  # type: ignore

    def xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_4(
        self, command: GenerateWeeklyReliabilityReportCommand
    ) -> GenerateWeeklyReliabilityReportResponse:
        services_raw = self._port.fetch_service_reliability(command.window_days)  # type: ignore
        incidents_raw = self._port.fetch_incidents(None)  # type: ignore

        services: list[dict[str, object]] = [dict(s) for s in services_raw]
        incidents: list[dict[str, object]] = [dict(i) for i in incidents_raw]

        result = self._engine.compute(services, incidents)
        return GenerateWeeklyReliabilityReportResponse(result=result)  # type: ignore

    def xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_5(
        self, command: GenerateWeeklyReliabilityReportCommand
    ) -> GenerateWeeklyReliabilityReportResponse:
        services_raw = self._port.fetch_service_reliability(command.window_days)  # type: ignore
        incidents_raw = self._port.fetch_incidents(command.window_days)  # type: ignore

        services: list[dict[str, object]] = None
        incidents: list[dict[str, object]] = [dict(i) for i in incidents_raw]

        result = self._engine.compute(services, incidents)
        return GenerateWeeklyReliabilityReportResponse(result=result)  # type: ignore

    def xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_6(
        self, command: GenerateWeeklyReliabilityReportCommand
    ) -> GenerateWeeklyReliabilityReportResponse:
        services_raw = self._port.fetch_service_reliability(command.window_days)  # type: ignore
        incidents_raw = self._port.fetch_incidents(command.window_days)  # type: ignore

        services: list[dict[str, object]] = [dict(None) for s in services_raw]
        incidents: list[dict[str, object]] = [dict(i) for i in incidents_raw]

        result = self._engine.compute(services, incidents)
        return GenerateWeeklyReliabilityReportResponse(result=result)  # type: ignore

    def xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_7(
        self, command: GenerateWeeklyReliabilityReportCommand
    ) -> GenerateWeeklyReliabilityReportResponse:
        services_raw = self._port.fetch_service_reliability(command.window_days)  # type: ignore
        incidents_raw = self._port.fetch_incidents(command.window_days)  # type: ignore

        services: list[dict[str, object]] = [dict(s) for s in services_raw]
        incidents: list[dict[str, object]] = None

        result = self._engine.compute(services, incidents)
        return GenerateWeeklyReliabilityReportResponse(result=result)  # type: ignore

    def xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_8(
        self, command: GenerateWeeklyReliabilityReportCommand
    ) -> GenerateWeeklyReliabilityReportResponse:
        services_raw = self._port.fetch_service_reliability(command.window_days)  # type: ignore
        incidents_raw = self._port.fetch_incidents(command.window_days)  # type: ignore

        services: list[dict[str, object]] = [dict(s) for s in services_raw]
        incidents: list[dict[str, object]] = [dict(None) for i in incidents_raw]

        result = self._engine.compute(services, incidents)
        return GenerateWeeklyReliabilityReportResponse(result=result)  # type: ignore

    def xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_9(
        self, command: GenerateWeeklyReliabilityReportCommand
    ) -> GenerateWeeklyReliabilityReportResponse:
        services_raw = self._port.fetch_service_reliability(command.window_days)  # type: ignore
        incidents_raw = self._port.fetch_incidents(command.window_days)  # type: ignore

        services: list[dict[str, object]] = [dict(s) for s in services_raw]
        incidents: list[dict[str, object]] = [dict(i) for i in incidents_raw]

        result = None
        return GenerateWeeklyReliabilityReportResponse(result=result)  # type: ignore

    def xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_10(
        self, command: GenerateWeeklyReliabilityReportCommand
    ) -> GenerateWeeklyReliabilityReportResponse:
        services_raw = self._port.fetch_service_reliability(command.window_days)  # type: ignore
        incidents_raw = self._port.fetch_incidents(command.window_days)  # type: ignore

        services: list[dict[str, object]] = [dict(s) for s in services_raw]
        incidents: list[dict[str, object]] = [dict(i) for i in incidents_raw]

        result = self._engine.compute(None, incidents)
        return GenerateWeeklyReliabilityReportResponse(result=result)  # type: ignore

    def xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_11(
        self, command: GenerateWeeklyReliabilityReportCommand
    ) -> GenerateWeeklyReliabilityReportResponse:
        services_raw = self._port.fetch_service_reliability(command.window_days)  # type: ignore
        incidents_raw = self._port.fetch_incidents(command.window_days)  # type: ignore

        services: list[dict[str, object]] = [dict(s) for s in services_raw]
        incidents: list[dict[str, object]] = [dict(i) for i in incidents_raw]

        result = self._engine.compute(services, None)
        return GenerateWeeklyReliabilityReportResponse(result=result)  # type: ignore

    def xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_12(
        self, command: GenerateWeeklyReliabilityReportCommand
    ) -> GenerateWeeklyReliabilityReportResponse:
        services_raw = self._port.fetch_service_reliability(command.window_days)  # type: ignore
        incidents_raw = self._port.fetch_incidents(command.window_days)  # type: ignore

        services: list[dict[str, object]] = [dict(s) for s in services_raw]
        incidents: list[dict[str, object]] = [dict(i) for i in incidents_raw]

        result = self._engine.compute(incidents)
        return GenerateWeeklyReliabilityReportResponse(result=result)  # type: ignore

    def xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_13(
        self, command: GenerateWeeklyReliabilityReportCommand
    ) -> GenerateWeeklyReliabilityReportResponse:
        services_raw = self._port.fetch_service_reliability(command.window_days)  # type: ignore
        incidents_raw = self._port.fetch_incidents(command.window_days)  # type: ignore

        services: list[dict[str, object]] = [dict(s) for s in services_raw]
        incidents: list[dict[str, object]] = [dict(i) for i in incidents_raw]

        result = self._engine.compute(services, )
        return GenerateWeeklyReliabilityReportResponse(result=result)  # type: ignore

    def xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_14(
        self, command: GenerateWeeklyReliabilityReportCommand
    ) -> GenerateWeeklyReliabilityReportResponse:
        services_raw = self._port.fetch_service_reliability(command.window_days)  # type: ignore
        incidents_raw = self._port.fetch_incidents(command.window_days)  # type: ignore

        services: list[dict[str, object]] = [dict(s) for s in services_raw]
        incidents: list[dict[str, object]] = [dict(i) for i in incidents_raw]

        result = self._engine.compute(services, incidents)
        return GenerateWeeklyReliabilityReportResponse(result=None)  # type: ignore

mutants_xǁGenerateWeeklyReliabilityReportUseCaseǁ__init____mutmut['_mutmut_orig'] = GenerateWeeklyReliabilityReportUseCase.xǁGenerateWeeklyReliabilityReportUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁGenerateWeeklyReliabilityReportUseCaseǁ__init____mutmut['xǁGenerateWeeklyReliabilityReportUseCaseǁ__init____mutmut_1'] = GenerateWeeklyReliabilityReportUseCase.xǁGenerateWeeklyReliabilityReportUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁGenerateWeeklyReliabilityReportUseCaseǁ__init____mutmut['xǁGenerateWeeklyReliabilityReportUseCaseǁ__init____mutmut_2'] = GenerateWeeklyReliabilityReportUseCase.xǁGenerateWeeklyReliabilityReportUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut['_mutmut_orig'] = GenerateWeeklyReliabilityReportUseCase.xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut['xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_1'] = GenerateWeeklyReliabilityReportUseCase.xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut['xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_2'] = GenerateWeeklyReliabilityReportUseCase.xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut['xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_3'] = GenerateWeeklyReliabilityReportUseCase.xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut['xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_4'] = GenerateWeeklyReliabilityReportUseCase.xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut['xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_5'] = GenerateWeeklyReliabilityReportUseCase.xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut['xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_6'] = GenerateWeeklyReliabilityReportUseCase.xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut['xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_7'] = GenerateWeeklyReliabilityReportUseCase.xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut['xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_8'] = GenerateWeeklyReliabilityReportUseCase.xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut['xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_9'] = GenerateWeeklyReliabilityReportUseCase.xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut['xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_10'] = GenerateWeeklyReliabilityReportUseCase.xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut['xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_11'] = GenerateWeeklyReliabilityReportUseCase.xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut['xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_12'] = GenerateWeeklyReliabilityReportUseCase.xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut['xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_13'] = GenerateWeeklyReliabilityReportUseCase.xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut['xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_14'] = GenerateWeeklyReliabilityReportUseCase.xǁGenerateWeeklyReliabilityReportUseCaseǁgenerate_report__mutmut_14 # type: ignore # mutmut generated
