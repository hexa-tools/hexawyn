from __future__ import annotations

from hexawyn.application.ports.driven.engineer_workload_port import EngineerWorkloadPort
from hexawyn.application.use_case.workloads.report_night_interventions.command import (  # noqa: E501
    ReportNightInterventionsCommand,
)
from hexawyn.application.use_case.workloads.report_night_interventions.response import (  # noqa: E501
    ReportNightInterventionsResponse,
)
from hexawyn.domain.services.engineer_workload.night_intervention_service import (
    compute_night_intervention_report,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁReportNightInterventionsUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁReportNightInterventionsUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class ReportNightInterventionsUseCase:
    @_mutmut_mutated(mutants_xǁReportNightInterventionsUseCaseǁ__init____mutmut)
    def __init__(self, workload_port: EngineerWorkloadPort) -> None:
        self._port = workload_port
    def xǁReportNightInterventionsUseCaseǁ__init____mutmut_orig(self, workload_port: EngineerWorkloadPort) -> None:
        self._port = workload_port
    def xǁReportNightInterventionsUseCaseǁ__init____mutmut_1(self, workload_port: EngineerWorkloadPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁReportNightInterventionsUseCaseǁexecute__mutmut)
    def execute(self, command: ReportNightInterventionsCommand) -> ReportNightInterventionsResponse:
        months = self._port.get_night_intervention_data(command.history_months)
        split = max(len(months) // 2, 1)
        previous = months[:split]
        current = months[split:]
        result = compute_night_intervention_report(current, previous, period="Ce mois")
        return ReportNightInterventionsResponse(result=result)

    def xǁReportNightInterventionsUseCaseǁexecute__mutmut_orig(self, command: ReportNightInterventionsCommand) -> ReportNightInterventionsResponse:
        months = self._port.get_night_intervention_data(command.history_months)
        split = max(len(months) // 2, 1)
        previous = months[:split]
        current = months[split:]
        result = compute_night_intervention_report(current, previous, period="Ce mois")
        return ReportNightInterventionsResponse(result=result)

    def xǁReportNightInterventionsUseCaseǁexecute__mutmut_1(self, command: ReportNightInterventionsCommand) -> ReportNightInterventionsResponse:
        months = None
        split = max(len(months) // 2, 1)
        previous = months[:split]
        current = months[split:]
        result = compute_night_intervention_report(current, previous, period="Ce mois")
        return ReportNightInterventionsResponse(result=result)

    def xǁReportNightInterventionsUseCaseǁexecute__mutmut_2(self, command: ReportNightInterventionsCommand) -> ReportNightInterventionsResponse:
        months = self._port.get_night_intervention_data(None)
        split = max(len(months) // 2, 1)
        previous = months[:split]
        current = months[split:]
        result = compute_night_intervention_report(current, previous, period="Ce mois")
        return ReportNightInterventionsResponse(result=result)

    def xǁReportNightInterventionsUseCaseǁexecute__mutmut_3(self, command: ReportNightInterventionsCommand) -> ReportNightInterventionsResponse:
        months = self._port.get_night_intervention_data(command.history_months)
        split = None
        previous = months[:split]
        current = months[split:]
        result = compute_night_intervention_report(current, previous, period="Ce mois")
        return ReportNightInterventionsResponse(result=result)

    def xǁReportNightInterventionsUseCaseǁexecute__mutmut_4(self, command: ReportNightInterventionsCommand) -> ReportNightInterventionsResponse:
        months = self._port.get_night_intervention_data(command.history_months)
        split = max(None, 1)
        previous = months[:split]
        current = months[split:]
        result = compute_night_intervention_report(current, previous, period="Ce mois")
        return ReportNightInterventionsResponse(result=result)

    def xǁReportNightInterventionsUseCaseǁexecute__mutmut_5(self, command: ReportNightInterventionsCommand) -> ReportNightInterventionsResponse:
        months = self._port.get_night_intervention_data(command.history_months)
        split = max(len(months) // 2, None)
        previous = months[:split]
        current = months[split:]
        result = compute_night_intervention_report(current, previous, period="Ce mois")
        return ReportNightInterventionsResponse(result=result)

    def xǁReportNightInterventionsUseCaseǁexecute__mutmut_6(self, command: ReportNightInterventionsCommand) -> ReportNightInterventionsResponse:
        months = self._port.get_night_intervention_data(command.history_months)
        split = max(1)
        previous = months[:split]
        current = months[split:]
        result = compute_night_intervention_report(current, previous, period="Ce mois")
        return ReportNightInterventionsResponse(result=result)

    def xǁReportNightInterventionsUseCaseǁexecute__mutmut_7(self, command: ReportNightInterventionsCommand) -> ReportNightInterventionsResponse:
        months = self._port.get_night_intervention_data(command.history_months)
        split = max(len(months) // 2, )
        previous = months[:split]
        current = months[split:]
        result = compute_night_intervention_report(current, previous, period="Ce mois")
        return ReportNightInterventionsResponse(result=result)

    def xǁReportNightInterventionsUseCaseǁexecute__mutmut_8(self, command: ReportNightInterventionsCommand) -> ReportNightInterventionsResponse:
        months = self._port.get_night_intervention_data(command.history_months)
        split = max(len(months) / 2, 1)
        previous = months[:split]
        current = months[split:]
        result = compute_night_intervention_report(current, previous, period="Ce mois")
        return ReportNightInterventionsResponse(result=result)

    def xǁReportNightInterventionsUseCaseǁexecute__mutmut_9(self, command: ReportNightInterventionsCommand) -> ReportNightInterventionsResponse:
        months = self._port.get_night_intervention_data(command.history_months)
        split = max(len(months) // 3, 1)
        previous = months[:split]
        current = months[split:]
        result = compute_night_intervention_report(current, previous, period="Ce mois")
        return ReportNightInterventionsResponse(result=result)

    def xǁReportNightInterventionsUseCaseǁexecute__mutmut_10(self, command: ReportNightInterventionsCommand) -> ReportNightInterventionsResponse:
        months = self._port.get_night_intervention_data(command.history_months)
        split = max(len(months) // 2, 2)
        previous = months[:split]
        current = months[split:]
        result = compute_night_intervention_report(current, previous, period="Ce mois")
        return ReportNightInterventionsResponse(result=result)

    def xǁReportNightInterventionsUseCaseǁexecute__mutmut_11(self, command: ReportNightInterventionsCommand) -> ReportNightInterventionsResponse:
        months = self._port.get_night_intervention_data(command.history_months)
        split = max(len(months) // 2, 1)
        previous = None
        current = months[split:]
        result = compute_night_intervention_report(current, previous, period="Ce mois")
        return ReportNightInterventionsResponse(result=result)

    def xǁReportNightInterventionsUseCaseǁexecute__mutmut_12(self, command: ReportNightInterventionsCommand) -> ReportNightInterventionsResponse:
        months = self._port.get_night_intervention_data(command.history_months)
        split = max(len(months) // 2, 1)
        previous = months[:split]
        current = None
        result = compute_night_intervention_report(current, previous, period="Ce mois")
        return ReportNightInterventionsResponse(result=result)

    def xǁReportNightInterventionsUseCaseǁexecute__mutmut_13(self, command: ReportNightInterventionsCommand) -> ReportNightInterventionsResponse:
        months = self._port.get_night_intervention_data(command.history_months)
        split = max(len(months) // 2, 1)
        previous = months[:split]
        current = months[split:]
        result = None
        return ReportNightInterventionsResponse(result=result)

    def xǁReportNightInterventionsUseCaseǁexecute__mutmut_14(self, command: ReportNightInterventionsCommand) -> ReportNightInterventionsResponse:
        months = self._port.get_night_intervention_data(command.history_months)
        split = max(len(months) // 2, 1)
        previous = months[:split]
        current = months[split:]
        result = compute_night_intervention_report(None, previous, period="Ce mois")
        return ReportNightInterventionsResponse(result=result)

    def xǁReportNightInterventionsUseCaseǁexecute__mutmut_15(self, command: ReportNightInterventionsCommand) -> ReportNightInterventionsResponse:
        months = self._port.get_night_intervention_data(command.history_months)
        split = max(len(months) // 2, 1)
        previous = months[:split]
        current = months[split:]
        result = compute_night_intervention_report(current, None, period="Ce mois")
        return ReportNightInterventionsResponse(result=result)

    def xǁReportNightInterventionsUseCaseǁexecute__mutmut_16(self, command: ReportNightInterventionsCommand) -> ReportNightInterventionsResponse:
        months = self._port.get_night_intervention_data(command.history_months)
        split = max(len(months) // 2, 1)
        previous = months[:split]
        current = months[split:]
        result = compute_night_intervention_report(current, previous, period=None)
        return ReportNightInterventionsResponse(result=result)

    def xǁReportNightInterventionsUseCaseǁexecute__mutmut_17(self, command: ReportNightInterventionsCommand) -> ReportNightInterventionsResponse:
        months = self._port.get_night_intervention_data(command.history_months)
        split = max(len(months) // 2, 1)
        previous = months[:split]
        current = months[split:]
        result = compute_night_intervention_report(previous, period="Ce mois")
        return ReportNightInterventionsResponse(result=result)

    def xǁReportNightInterventionsUseCaseǁexecute__mutmut_18(self, command: ReportNightInterventionsCommand) -> ReportNightInterventionsResponse:
        months = self._port.get_night_intervention_data(command.history_months)
        split = max(len(months) // 2, 1)
        previous = months[:split]
        current = months[split:]
        result = compute_night_intervention_report(current, period="Ce mois")
        return ReportNightInterventionsResponse(result=result)

    def xǁReportNightInterventionsUseCaseǁexecute__mutmut_19(self, command: ReportNightInterventionsCommand) -> ReportNightInterventionsResponse:
        months = self._port.get_night_intervention_data(command.history_months)
        split = max(len(months) // 2, 1)
        previous = months[:split]
        current = months[split:]
        result = compute_night_intervention_report(current, previous, )
        return ReportNightInterventionsResponse(result=result)

    def xǁReportNightInterventionsUseCaseǁexecute__mutmut_20(self, command: ReportNightInterventionsCommand) -> ReportNightInterventionsResponse:
        months = self._port.get_night_intervention_data(command.history_months)
        split = max(len(months) // 2, 1)
        previous = months[:split]
        current = months[split:]
        result = compute_night_intervention_report(current, previous, period="XXCe moisXX")
        return ReportNightInterventionsResponse(result=result)

    def xǁReportNightInterventionsUseCaseǁexecute__mutmut_21(self, command: ReportNightInterventionsCommand) -> ReportNightInterventionsResponse:
        months = self._port.get_night_intervention_data(command.history_months)
        split = max(len(months) // 2, 1)
        previous = months[:split]
        current = months[split:]
        result = compute_night_intervention_report(current, previous, period="ce mois")
        return ReportNightInterventionsResponse(result=result)

    def xǁReportNightInterventionsUseCaseǁexecute__mutmut_22(self, command: ReportNightInterventionsCommand) -> ReportNightInterventionsResponse:
        months = self._port.get_night_intervention_data(command.history_months)
        split = max(len(months) // 2, 1)
        previous = months[:split]
        current = months[split:]
        result = compute_night_intervention_report(current, previous, period="CE MOIS")
        return ReportNightInterventionsResponse(result=result)

    def xǁReportNightInterventionsUseCaseǁexecute__mutmut_23(self, command: ReportNightInterventionsCommand) -> ReportNightInterventionsResponse:
        months = self._port.get_night_intervention_data(command.history_months)
        split = max(len(months) // 2, 1)
        previous = months[:split]
        current = months[split:]
        result = compute_night_intervention_report(current, previous, period="Ce mois")
        return ReportNightInterventionsResponse(result=None)

mutants_xǁReportNightInterventionsUseCaseǁ__init____mutmut['_mutmut_orig'] = ReportNightInterventionsUseCase.xǁReportNightInterventionsUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁReportNightInterventionsUseCaseǁ__init____mutmut['xǁReportNightInterventionsUseCaseǁ__init____mutmut_1'] = ReportNightInterventionsUseCase.xǁReportNightInterventionsUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁReportNightInterventionsUseCaseǁexecute__mutmut['_mutmut_orig'] = ReportNightInterventionsUseCase.xǁReportNightInterventionsUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁReportNightInterventionsUseCaseǁexecute__mutmut['xǁReportNightInterventionsUseCaseǁexecute__mutmut_1'] = ReportNightInterventionsUseCase.xǁReportNightInterventionsUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁReportNightInterventionsUseCaseǁexecute__mutmut['xǁReportNightInterventionsUseCaseǁexecute__mutmut_2'] = ReportNightInterventionsUseCase.xǁReportNightInterventionsUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁReportNightInterventionsUseCaseǁexecute__mutmut['xǁReportNightInterventionsUseCaseǁexecute__mutmut_3'] = ReportNightInterventionsUseCase.xǁReportNightInterventionsUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁReportNightInterventionsUseCaseǁexecute__mutmut['xǁReportNightInterventionsUseCaseǁexecute__mutmut_4'] = ReportNightInterventionsUseCase.xǁReportNightInterventionsUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁReportNightInterventionsUseCaseǁexecute__mutmut['xǁReportNightInterventionsUseCaseǁexecute__mutmut_5'] = ReportNightInterventionsUseCase.xǁReportNightInterventionsUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁReportNightInterventionsUseCaseǁexecute__mutmut['xǁReportNightInterventionsUseCaseǁexecute__mutmut_6'] = ReportNightInterventionsUseCase.xǁReportNightInterventionsUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁReportNightInterventionsUseCaseǁexecute__mutmut['xǁReportNightInterventionsUseCaseǁexecute__mutmut_7'] = ReportNightInterventionsUseCase.xǁReportNightInterventionsUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁReportNightInterventionsUseCaseǁexecute__mutmut['xǁReportNightInterventionsUseCaseǁexecute__mutmut_8'] = ReportNightInterventionsUseCase.xǁReportNightInterventionsUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁReportNightInterventionsUseCaseǁexecute__mutmut['xǁReportNightInterventionsUseCaseǁexecute__mutmut_9'] = ReportNightInterventionsUseCase.xǁReportNightInterventionsUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁReportNightInterventionsUseCaseǁexecute__mutmut['xǁReportNightInterventionsUseCaseǁexecute__mutmut_10'] = ReportNightInterventionsUseCase.xǁReportNightInterventionsUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁReportNightInterventionsUseCaseǁexecute__mutmut['xǁReportNightInterventionsUseCaseǁexecute__mutmut_11'] = ReportNightInterventionsUseCase.xǁReportNightInterventionsUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁReportNightInterventionsUseCaseǁexecute__mutmut['xǁReportNightInterventionsUseCaseǁexecute__mutmut_12'] = ReportNightInterventionsUseCase.xǁReportNightInterventionsUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁReportNightInterventionsUseCaseǁexecute__mutmut['xǁReportNightInterventionsUseCaseǁexecute__mutmut_13'] = ReportNightInterventionsUseCase.xǁReportNightInterventionsUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁReportNightInterventionsUseCaseǁexecute__mutmut['xǁReportNightInterventionsUseCaseǁexecute__mutmut_14'] = ReportNightInterventionsUseCase.xǁReportNightInterventionsUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁReportNightInterventionsUseCaseǁexecute__mutmut['xǁReportNightInterventionsUseCaseǁexecute__mutmut_15'] = ReportNightInterventionsUseCase.xǁReportNightInterventionsUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁReportNightInterventionsUseCaseǁexecute__mutmut['xǁReportNightInterventionsUseCaseǁexecute__mutmut_16'] = ReportNightInterventionsUseCase.xǁReportNightInterventionsUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁReportNightInterventionsUseCaseǁexecute__mutmut['xǁReportNightInterventionsUseCaseǁexecute__mutmut_17'] = ReportNightInterventionsUseCase.xǁReportNightInterventionsUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁReportNightInterventionsUseCaseǁexecute__mutmut['xǁReportNightInterventionsUseCaseǁexecute__mutmut_18'] = ReportNightInterventionsUseCase.xǁReportNightInterventionsUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁReportNightInterventionsUseCaseǁexecute__mutmut['xǁReportNightInterventionsUseCaseǁexecute__mutmut_19'] = ReportNightInterventionsUseCase.xǁReportNightInterventionsUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁReportNightInterventionsUseCaseǁexecute__mutmut['xǁReportNightInterventionsUseCaseǁexecute__mutmut_20'] = ReportNightInterventionsUseCase.xǁReportNightInterventionsUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁReportNightInterventionsUseCaseǁexecute__mutmut['xǁReportNightInterventionsUseCaseǁexecute__mutmut_21'] = ReportNightInterventionsUseCase.xǁReportNightInterventionsUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁReportNightInterventionsUseCaseǁexecute__mutmut['xǁReportNightInterventionsUseCaseǁexecute__mutmut_22'] = ReportNightInterventionsUseCase.xǁReportNightInterventionsUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁReportNightInterventionsUseCaseǁexecute__mutmut['xǁReportNightInterventionsUseCaseǁexecute__mutmut_23'] = ReportNightInterventionsUseCase.xǁReportNightInterventionsUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
