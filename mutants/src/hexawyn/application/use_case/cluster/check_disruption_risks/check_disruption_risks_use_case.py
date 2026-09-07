from __future__ import annotations

from hexawyn.application.ports.driven.disruption_risk_port import DisruptionRiskPort
from hexawyn.application.use_case.cluster.check_disruption_risks.command import (  # noqa: E501
    CheckDisruptionRisksCommand,
)
from hexawyn.application.use_case.cluster.check_disruption_risks.response import (  # noqa: E501
    CheckDisruptionRisksResponse,
)
from hexawyn.domain.services.disruption_risk.disruption_risk_service import (
    compute_disruption_risks,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCheckDisruptionRisksUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁCheckDisruptionRisksUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class CheckDisruptionRisksUseCase:
    @_mutmut_mutated(mutants_xǁCheckDisruptionRisksUseCaseǁ__init____mutmut)
    def __init__(self, disruption_risk_port: DisruptionRiskPort) -> None:
        self._port = disruption_risk_port
    def xǁCheckDisruptionRisksUseCaseǁ__init____mutmut_orig(self, disruption_risk_port: DisruptionRiskPort) -> None:
        self._port = disruption_risk_port
    def xǁCheckDisruptionRisksUseCaseǁ__init____mutmut_1(self, disruption_risk_port: DisruptionRiskPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁCheckDisruptionRisksUseCaseǁexecute__mutmut)
    def execute(self, command: CheckDisruptionRisksCommand) -> CheckDisruptionRisksResponse:
        raw = self._port.get_disruption_risks(command.warning_days)
        has_data = bool(raw)
        result = compute_disruption_risks(raw, period="Semaine en cours", has_data=has_data)
        return CheckDisruptionRisksResponse(result=result)

    def xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_orig(self, command: CheckDisruptionRisksCommand) -> CheckDisruptionRisksResponse:
        raw = self._port.get_disruption_risks(command.warning_days)
        has_data = bool(raw)
        result = compute_disruption_risks(raw, period="Semaine en cours", has_data=has_data)
        return CheckDisruptionRisksResponse(result=result)

    def xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_1(self, command: CheckDisruptionRisksCommand) -> CheckDisruptionRisksResponse:
        raw = None
        has_data = bool(raw)
        result = compute_disruption_risks(raw, period="Semaine en cours", has_data=has_data)
        return CheckDisruptionRisksResponse(result=result)

    def xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_2(self, command: CheckDisruptionRisksCommand) -> CheckDisruptionRisksResponse:
        raw = self._port.get_disruption_risks(None)
        has_data = bool(raw)
        result = compute_disruption_risks(raw, period="Semaine en cours", has_data=has_data)
        return CheckDisruptionRisksResponse(result=result)

    def xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_3(self, command: CheckDisruptionRisksCommand) -> CheckDisruptionRisksResponse:
        raw = self._port.get_disruption_risks(command.warning_days)
        has_data = None
        result = compute_disruption_risks(raw, period="Semaine en cours", has_data=has_data)
        return CheckDisruptionRisksResponse(result=result)

    def xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_4(self, command: CheckDisruptionRisksCommand) -> CheckDisruptionRisksResponse:
        raw = self._port.get_disruption_risks(command.warning_days)
        has_data = bool(None)
        result = compute_disruption_risks(raw, period="Semaine en cours", has_data=has_data)
        return CheckDisruptionRisksResponse(result=result)

    def xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_5(self, command: CheckDisruptionRisksCommand) -> CheckDisruptionRisksResponse:
        raw = self._port.get_disruption_risks(command.warning_days)
        has_data = bool(raw)
        result = None
        return CheckDisruptionRisksResponse(result=result)

    def xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_6(self, command: CheckDisruptionRisksCommand) -> CheckDisruptionRisksResponse:
        raw = self._port.get_disruption_risks(command.warning_days)
        has_data = bool(raw)
        result = compute_disruption_risks(None, period="Semaine en cours", has_data=has_data)
        return CheckDisruptionRisksResponse(result=result)

    def xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_7(self, command: CheckDisruptionRisksCommand) -> CheckDisruptionRisksResponse:
        raw = self._port.get_disruption_risks(command.warning_days)
        has_data = bool(raw)
        result = compute_disruption_risks(raw, period=None, has_data=has_data)
        return CheckDisruptionRisksResponse(result=result)

    def xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_8(self, command: CheckDisruptionRisksCommand) -> CheckDisruptionRisksResponse:
        raw = self._port.get_disruption_risks(command.warning_days)
        has_data = bool(raw)
        result = compute_disruption_risks(raw, period="Semaine en cours", has_data=None)
        return CheckDisruptionRisksResponse(result=result)

    def xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_9(self, command: CheckDisruptionRisksCommand) -> CheckDisruptionRisksResponse:
        raw = self._port.get_disruption_risks(command.warning_days)
        has_data = bool(raw)
        result = compute_disruption_risks(period="Semaine en cours", has_data=has_data)
        return CheckDisruptionRisksResponse(result=result)

    def xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_10(self, command: CheckDisruptionRisksCommand) -> CheckDisruptionRisksResponse:
        raw = self._port.get_disruption_risks(command.warning_days)
        has_data = bool(raw)
        result = compute_disruption_risks(raw, has_data=has_data)
        return CheckDisruptionRisksResponse(result=result)

    def xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_11(self, command: CheckDisruptionRisksCommand) -> CheckDisruptionRisksResponse:
        raw = self._port.get_disruption_risks(command.warning_days)
        has_data = bool(raw)
        result = compute_disruption_risks(raw, period="Semaine en cours", )
        return CheckDisruptionRisksResponse(result=result)

    def xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_12(self, command: CheckDisruptionRisksCommand) -> CheckDisruptionRisksResponse:
        raw = self._port.get_disruption_risks(command.warning_days)
        has_data = bool(raw)
        result = compute_disruption_risks(raw, period="XXSemaine en coursXX", has_data=has_data)
        return CheckDisruptionRisksResponse(result=result)

    def xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_13(self, command: CheckDisruptionRisksCommand) -> CheckDisruptionRisksResponse:
        raw = self._port.get_disruption_risks(command.warning_days)
        has_data = bool(raw)
        result = compute_disruption_risks(raw, period="semaine en cours", has_data=has_data)
        return CheckDisruptionRisksResponse(result=result)

    def xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_14(self, command: CheckDisruptionRisksCommand) -> CheckDisruptionRisksResponse:
        raw = self._port.get_disruption_risks(command.warning_days)
        has_data = bool(raw)
        result = compute_disruption_risks(raw, period="SEMAINE EN COURS", has_data=has_data)
        return CheckDisruptionRisksResponse(result=result)

    def xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_15(self, command: CheckDisruptionRisksCommand) -> CheckDisruptionRisksResponse:
        raw = self._port.get_disruption_risks(command.warning_days)
        has_data = bool(raw)
        result = compute_disruption_risks(raw, period="Semaine en cours", has_data=has_data)
        return CheckDisruptionRisksResponse(result=None)

mutants_xǁCheckDisruptionRisksUseCaseǁ__init____mutmut['_mutmut_orig'] = CheckDisruptionRisksUseCase.xǁCheckDisruptionRisksUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCheckDisruptionRisksUseCaseǁ__init____mutmut['xǁCheckDisruptionRisksUseCaseǁ__init____mutmut_1'] = CheckDisruptionRisksUseCase.xǁCheckDisruptionRisksUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁCheckDisruptionRisksUseCaseǁexecute__mutmut['_mutmut_orig'] = CheckDisruptionRisksUseCase.xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCheckDisruptionRisksUseCaseǁexecute__mutmut['xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_1'] = CheckDisruptionRisksUseCase.xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCheckDisruptionRisksUseCaseǁexecute__mutmut['xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_2'] = CheckDisruptionRisksUseCase.xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCheckDisruptionRisksUseCaseǁexecute__mutmut['xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_3'] = CheckDisruptionRisksUseCase.xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCheckDisruptionRisksUseCaseǁexecute__mutmut['xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_4'] = CheckDisruptionRisksUseCase.xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCheckDisruptionRisksUseCaseǁexecute__mutmut['xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_5'] = CheckDisruptionRisksUseCase.xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCheckDisruptionRisksUseCaseǁexecute__mutmut['xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_6'] = CheckDisruptionRisksUseCase.xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCheckDisruptionRisksUseCaseǁexecute__mutmut['xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_7'] = CheckDisruptionRisksUseCase.xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCheckDisruptionRisksUseCaseǁexecute__mutmut['xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_8'] = CheckDisruptionRisksUseCase.xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCheckDisruptionRisksUseCaseǁexecute__mutmut['xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_9'] = CheckDisruptionRisksUseCase.xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCheckDisruptionRisksUseCaseǁexecute__mutmut['xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_10'] = CheckDisruptionRisksUseCase.xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCheckDisruptionRisksUseCaseǁexecute__mutmut['xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_11'] = CheckDisruptionRisksUseCase.xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCheckDisruptionRisksUseCaseǁexecute__mutmut['xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_12'] = CheckDisruptionRisksUseCase.xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCheckDisruptionRisksUseCaseǁexecute__mutmut['xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_13'] = CheckDisruptionRisksUseCase.xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCheckDisruptionRisksUseCaseǁexecute__mutmut['xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_14'] = CheckDisruptionRisksUseCase.xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁCheckDisruptionRisksUseCaseǁexecute__mutmut['xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_15'] = CheckDisruptionRisksUseCase.xǁCheckDisruptionRisksUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
