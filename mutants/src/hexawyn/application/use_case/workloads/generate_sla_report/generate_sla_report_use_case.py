from __future__ import annotations

from hexawyn.application.ports.driven.sla_report_port import SlaReportPort
from hexawyn.application.use_case.workloads.generate_sla_report.command import (
    GenerateSLAReportCommand,
)
from hexawyn.application.use_case.workloads.generate_sla_report.response import (
    GenerateSLAReportResponse,
)
from hexawyn.domain.services.sla_report.sla_report_service import SlaReportService


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁGenerateSLAReportUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁGenerateSLAReportUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class GenerateSLAReportUseCase:
    @_mutmut_mutated(mutants_xǁGenerateSLAReportUseCaseǁ__init____mutmut)
    def __init__(self, sla_port: SlaReportPort) -> None:
        self._port = sla_port
        self._engine = SlaReportService()
    def xǁGenerateSLAReportUseCaseǁ__init____mutmut_orig(self, sla_port: SlaReportPort) -> None:
        self._port = sla_port
        self._engine = SlaReportService()
    def xǁGenerateSLAReportUseCaseǁ__init____mutmut_1(self, sla_port: SlaReportPort) -> None:
        self._port = None
        self._engine = SlaReportService()
    def xǁGenerateSLAReportUseCaseǁ__init____mutmut_2(self, sla_port: SlaReportPort) -> None:
        self._port = sla_port
        self._engine = None

    @_mutmut_mutated(mutants_xǁGenerateSLAReportUseCaseǁexecute__mutmut)
    def execute(self, command: GenerateSLAReportCommand) -> GenerateSLAReportResponse:
        data = self._port.get_quarter_sla_data(command.quarter)
        previous_avg = self._port.get_previous_quarter_avg_uptime(command.quarter)
        result = self._engine.generate(
            data=data, quarter=command.quarter, previous_avg=previous_avg
        )
        return GenerateSLAReportResponse(result=result)

    def xǁGenerateSLAReportUseCaseǁexecute__mutmut_orig(self, command: GenerateSLAReportCommand) -> GenerateSLAReportResponse:
        data = self._port.get_quarter_sla_data(command.quarter)
        previous_avg = self._port.get_previous_quarter_avg_uptime(command.quarter)
        result = self._engine.generate(
            data=data, quarter=command.quarter, previous_avg=previous_avg
        )
        return GenerateSLAReportResponse(result=result)

    def xǁGenerateSLAReportUseCaseǁexecute__mutmut_1(self, command: GenerateSLAReportCommand) -> GenerateSLAReportResponse:
        data = None
        previous_avg = self._port.get_previous_quarter_avg_uptime(command.quarter)
        result = self._engine.generate(
            data=data, quarter=command.quarter, previous_avg=previous_avg
        )
        return GenerateSLAReportResponse(result=result)

    def xǁGenerateSLAReportUseCaseǁexecute__mutmut_2(self, command: GenerateSLAReportCommand) -> GenerateSLAReportResponse:
        data = self._port.get_quarter_sla_data(None)
        previous_avg = self._port.get_previous_quarter_avg_uptime(command.quarter)
        result = self._engine.generate(
            data=data, quarter=command.quarter, previous_avg=previous_avg
        )
        return GenerateSLAReportResponse(result=result)

    def xǁGenerateSLAReportUseCaseǁexecute__mutmut_3(self, command: GenerateSLAReportCommand) -> GenerateSLAReportResponse:
        data = self._port.get_quarter_sla_data(command.quarter)
        previous_avg = None
        result = self._engine.generate(
            data=data, quarter=command.quarter, previous_avg=previous_avg
        )
        return GenerateSLAReportResponse(result=result)

    def xǁGenerateSLAReportUseCaseǁexecute__mutmut_4(self, command: GenerateSLAReportCommand) -> GenerateSLAReportResponse:
        data = self._port.get_quarter_sla_data(command.quarter)
        previous_avg = self._port.get_previous_quarter_avg_uptime(None)
        result = self._engine.generate(
            data=data, quarter=command.quarter, previous_avg=previous_avg
        )
        return GenerateSLAReportResponse(result=result)

    def xǁGenerateSLAReportUseCaseǁexecute__mutmut_5(self, command: GenerateSLAReportCommand) -> GenerateSLAReportResponse:
        data = self._port.get_quarter_sla_data(command.quarter)
        previous_avg = self._port.get_previous_quarter_avg_uptime(command.quarter)
        result = None
        return GenerateSLAReportResponse(result=result)

    def xǁGenerateSLAReportUseCaseǁexecute__mutmut_6(self, command: GenerateSLAReportCommand) -> GenerateSLAReportResponse:
        data = self._port.get_quarter_sla_data(command.quarter)
        previous_avg = self._port.get_previous_quarter_avg_uptime(command.quarter)
        result = self._engine.generate(
            data=None, quarter=command.quarter, previous_avg=previous_avg
        )
        return GenerateSLAReportResponse(result=result)

    def xǁGenerateSLAReportUseCaseǁexecute__mutmut_7(self, command: GenerateSLAReportCommand) -> GenerateSLAReportResponse:
        data = self._port.get_quarter_sla_data(command.quarter)
        previous_avg = self._port.get_previous_quarter_avg_uptime(command.quarter)
        result = self._engine.generate(
            data=data, quarter=None, previous_avg=previous_avg
        )
        return GenerateSLAReportResponse(result=result)

    def xǁGenerateSLAReportUseCaseǁexecute__mutmut_8(self, command: GenerateSLAReportCommand) -> GenerateSLAReportResponse:
        data = self._port.get_quarter_sla_data(command.quarter)
        previous_avg = self._port.get_previous_quarter_avg_uptime(command.quarter)
        result = self._engine.generate(
            data=data, quarter=command.quarter, previous_avg=None
        )
        return GenerateSLAReportResponse(result=result)

    def xǁGenerateSLAReportUseCaseǁexecute__mutmut_9(self, command: GenerateSLAReportCommand) -> GenerateSLAReportResponse:
        data = self._port.get_quarter_sla_data(command.quarter)
        previous_avg = self._port.get_previous_quarter_avg_uptime(command.quarter)
        result = self._engine.generate(
            quarter=command.quarter, previous_avg=previous_avg
        )
        return GenerateSLAReportResponse(result=result)

    def xǁGenerateSLAReportUseCaseǁexecute__mutmut_10(self, command: GenerateSLAReportCommand) -> GenerateSLAReportResponse:
        data = self._port.get_quarter_sla_data(command.quarter)
        previous_avg = self._port.get_previous_quarter_avg_uptime(command.quarter)
        result = self._engine.generate(
            data=data, previous_avg=previous_avg
        )
        return GenerateSLAReportResponse(result=result)

    def xǁGenerateSLAReportUseCaseǁexecute__mutmut_11(self, command: GenerateSLAReportCommand) -> GenerateSLAReportResponse:
        data = self._port.get_quarter_sla_data(command.quarter)
        previous_avg = self._port.get_previous_quarter_avg_uptime(command.quarter)
        result = self._engine.generate(
            data=data, quarter=command.quarter, )
        return GenerateSLAReportResponse(result=result)

    def xǁGenerateSLAReportUseCaseǁexecute__mutmut_12(self, command: GenerateSLAReportCommand) -> GenerateSLAReportResponse:
        data = self._port.get_quarter_sla_data(command.quarter)
        previous_avg = self._port.get_previous_quarter_avg_uptime(command.quarter)
        result = self._engine.generate(
            data=data, quarter=command.quarter, previous_avg=previous_avg
        )
        return GenerateSLAReportResponse(result=None)

mutants_xǁGenerateSLAReportUseCaseǁ__init____mutmut['_mutmut_orig'] = GenerateSLAReportUseCase.xǁGenerateSLAReportUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁGenerateSLAReportUseCaseǁ__init____mutmut['xǁGenerateSLAReportUseCaseǁ__init____mutmut_1'] = GenerateSLAReportUseCase.xǁGenerateSLAReportUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁGenerateSLAReportUseCaseǁ__init____mutmut['xǁGenerateSLAReportUseCaseǁ__init____mutmut_2'] = GenerateSLAReportUseCase.xǁGenerateSLAReportUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁGenerateSLAReportUseCaseǁexecute__mutmut['_mutmut_orig'] = GenerateSLAReportUseCase.xǁGenerateSLAReportUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGenerateSLAReportUseCaseǁexecute__mutmut['xǁGenerateSLAReportUseCaseǁexecute__mutmut_1'] = GenerateSLAReportUseCase.xǁGenerateSLAReportUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGenerateSLAReportUseCaseǁexecute__mutmut['xǁGenerateSLAReportUseCaseǁexecute__mutmut_2'] = GenerateSLAReportUseCase.xǁGenerateSLAReportUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGenerateSLAReportUseCaseǁexecute__mutmut['xǁGenerateSLAReportUseCaseǁexecute__mutmut_3'] = GenerateSLAReportUseCase.xǁGenerateSLAReportUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGenerateSLAReportUseCaseǁexecute__mutmut['xǁGenerateSLAReportUseCaseǁexecute__mutmut_4'] = GenerateSLAReportUseCase.xǁGenerateSLAReportUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGenerateSLAReportUseCaseǁexecute__mutmut['xǁGenerateSLAReportUseCaseǁexecute__mutmut_5'] = GenerateSLAReportUseCase.xǁGenerateSLAReportUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGenerateSLAReportUseCaseǁexecute__mutmut['xǁGenerateSLAReportUseCaseǁexecute__mutmut_6'] = GenerateSLAReportUseCase.xǁGenerateSLAReportUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGenerateSLAReportUseCaseǁexecute__mutmut['xǁGenerateSLAReportUseCaseǁexecute__mutmut_7'] = GenerateSLAReportUseCase.xǁGenerateSLAReportUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGenerateSLAReportUseCaseǁexecute__mutmut['xǁGenerateSLAReportUseCaseǁexecute__mutmut_8'] = GenerateSLAReportUseCase.xǁGenerateSLAReportUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGenerateSLAReportUseCaseǁexecute__mutmut['xǁGenerateSLAReportUseCaseǁexecute__mutmut_9'] = GenerateSLAReportUseCase.xǁGenerateSLAReportUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGenerateSLAReportUseCaseǁexecute__mutmut['xǁGenerateSLAReportUseCaseǁexecute__mutmut_10'] = GenerateSLAReportUseCase.xǁGenerateSLAReportUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGenerateSLAReportUseCaseǁexecute__mutmut['xǁGenerateSLAReportUseCaseǁexecute__mutmut_11'] = GenerateSLAReportUseCase.xǁGenerateSLAReportUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGenerateSLAReportUseCaseǁexecute__mutmut['xǁGenerateSLAReportUseCaseǁexecute__mutmut_12'] = GenerateSLAReportUseCase.xǁGenerateSLAReportUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
