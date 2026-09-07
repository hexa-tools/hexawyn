from __future__ import annotations

from hexawyn.application.ports.driven.probe_audit_port import ProbeAuditPort
from hexawyn.application.use_case.security.detect_missing_probes.command import (
    DetectMissingProbesCommand,
)
from hexawyn.application.use_case.security.detect_missing_probes.response import (
    DetectMissingProbesResponse,
)
from hexawyn.domain.services.probe_audit.probe_audit_engine import (
    ProbeAuditEngine,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁDetectMissingProbesUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDetectMissingProbesUseCaseǁdetect_missing_probes__mutmut: MutantDict = {}  # type: ignore


class DetectMissingProbesUseCase:
    @_mutmut_mutated(mutants_xǁDetectMissingProbesUseCaseǁ__init____mutmut)
    def __init__(self, probe_audit_port: ProbeAuditPort) -> None:
        self._port = probe_audit_port
        self._engine = ProbeAuditEngine()
    def xǁDetectMissingProbesUseCaseǁ__init____mutmut_orig(self, probe_audit_port: ProbeAuditPort) -> None:
        self._port = probe_audit_port
        self._engine = ProbeAuditEngine()
    def xǁDetectMissingProbesUseCaseǁ__init____mutmut_1(self, probe_audit_port: ProbeAuditPort) -> None:
        self._port = None
        self._engine = ProbeAuditEngine()
    def xǁDetectMissingProbesUseCaseǁ__init____mutmut_2(self, probe_audit_port: ProbeAuditPort) -> None:
        self._port = probe_audit_port
        self._engine = None

    @_mutmut_mutated(mutants_xǁDetectMissingProbesUseCaseǁdetect_missing_probes__mutmut)
    def detect_missing_probes(
        self, command: DetectMissingProbesCommand
    ) -> DetectMissingProbesResponse:
        deployments_raw = self._port.get_probe_audit_data(command.namespace)
        deployments: list[dict[str, object]] = [dict(d) for d in deployments_raw]
        result = self._engine.detect(deployments)
        return DetectMissingProbesResponse(result=result)  # type: ignore

    def xǁDetectMissingProbesUseCaseǁdetect_missing_probes__mutmut_orig(
        self, command: DetectMissingProbesCommand
    ) -> DetectMissingProbesResponse:
        deployments_raw = self._port.get_probe_audit_data(command.namespace)
        deployments: list[dict[str, object]] = [dict(d) for d in deployments_raw]
        result = self._engine.detect(deployments)
        return DetectMissingProbesResponse(result=result)  # type: ignore

    def xǁDetectMissingProbesUseCaseǁdetect_missing_probes__mutmut_1(
        self, command: DetectMissingProbesCommand
    ) -> DetectMissingProbesResponse:
        deployments_raw = None
        deployments: list[dict[str, object]] = [dict(d) for d in deployments_raw]
        result = self._engine.detect(deployments)
        return DetectMissingProbesResponse(result=result)  # type: ignore

    def xǁDetectMissingProbesUseCaseǁdetect_missing_probes__mutmut_2(
        self, command: DetectMissingProbesCommand
    ) -> DetectMissingProbesResponse:
        deployments_raw = self._port.get_probe_audit_data(None)
        deployments: list[dict[str, object]] = [dict(d) for d in deployments_raw]
        result = self._engine.detect(deployments)
        return DetectMissingProbesResponse(result=result)  # type: ignore

    def xǁDetectMissingProbesUseCaseǁdetect_missing_probes__mutmut_3(
        self, command: DetectMissingProbesCommand
    ) -> DetectMissingProbesResponse:
        deployments_raw = self._port.get_probe_audit_data(command.namespace)
        deployments: list[dict[str, object]] = None
        result = self._engine.detect(deployments)
        return DetectMissingProbesResponse(result=result)  # type: ignore

    def xǁDetectMissingProbesUseCaseǁdetect_missing_probes__mutmut_4(
        self, command: DetectMissingProbesCommand
    ) -> DetectMissingProbesResponse:
        deployments_raw = self._port.get_probe_audit_data(command.namespace)
        deployments: list[dict[str, object]] = [dict(None) for d in deployments_raw]
        result = self._engine.detect(deployments)
        return DetectMissingProbesResponse(result=result)  # type: ignore

    def xǁDetectMissingProbesUseCaseǁdetect_missing_probes__mutmut_5(
        self, command: DetectMissingProbesCommand
    ) -> DetectMissingProbesResponse:
        deployments_raw = self._port.get_probe_audit_data(command.namespace)
        deployments: list[dict[str, object]] = [dict(d) for d in deployments_raw]
        result = None
        return DetectMissingProbesResponse(result=result)  # type: ignore

    def xǁDetectMissingProbesUseCaseǁdetect_missing_probes__mutmut_6(
        self, command: DetectMissingProbesCommand
    ) -> DetectMissingProbesResponse:
        deployments_raw = self._port.get_probe_audit_data(command.namespace)
        deployments: list[dict[str, object]] = [dict(d) for d in deployments_raw]
        result = self._engine.detect(None)
        return DetectMissingProbesResponse(result=result)  # type: ignore

    def xǁDetectMissingProbesUseCaseǁdetect_missing_probes__mutmut_7(
        self, command: DetectMissingProbesCommand
    ) -> DetectMissingProbesResponse:
        deployments_raw = self._port.get_probe_audit_data(command.namespace)
        deployments: list[dict[str, object]] = [dict(d) for d in deployments_raw]
        result = self._engine.detect(deployments)
        return DetectMissingProbesResponse(result=None)  # type: ignore

mutants_xǁDetectMissingProbesUseCaseǁ__init____mutmut['_mutmut_orig'] = DetectMissingProbesUseCase.xǁDetectMissingProbesUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDetectMissingProbesUseCaseǁ__init____mutmut['xǁDetectMissingProbesUseCaseǁ__init____mutmut_1'] = DetectMissingProbesUseCase.xǁDetectMissingProbesUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDetectMissingProbesUseCaseǁ__init____mutmut['xǁDetectMissingProbesUseCaseǁ__init____mutmut_2'] = DetectMissingProbesUseCase.xǁDetectMissingProbesUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁDetectMissingProbesUseCaseǁdetect_missing_probes__mutmut['_mutmut_orig'] = DetectMissingProbesUseCase.xǁDetectMissingProbesUseCaseǁdetect_missing_probes__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDetectMissingProbesUseCaseǁdetect_missing_probes__mutmut['xǁDetectMissingProbesUseCaseǁdetect_missing_probes__mutmut_1'] = DetectMissingProbesUseCase.xǁDetectMissingProbesUseCaseǁdetect_missing_probes__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDetectMissingProbesUseCaseǁdetect_missing_probes__mutmut['xǁDetectMissingProbesUseCaseǁdetect_missing_probes__mutmut_2'] = DetectMissingProbesUseCase.xǁDetectMissingProbesUseCaseǁdetect_missing_probes__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDetectMissingProbesUseCaseǁdetect_missing_probes__mutmut['xǁDetectMissingProbesUseCaseǁdetect_missing_probes__mutmut_3'] = DetectMissingProbesUseCase.xǁDetectMissingProbesUseCaseǁdetect_missing_probes__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDetectMissingProbesUseCaseǁdetect_missing_probes__mutmut['xǁDetectMissingProbesUseCaseǁdetect_missing_probes__mutmut_4'] = DetectMissingProbesUseCase.xǁDetectMissingProbesUseCaseǁdetect_missing_probes__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDetectMissingProbesUseCaseǁdetect_missing_probes__mutmut['xǁDetectMissingProbesUseCaseǁdetect_missing_probes__mutmut_5'] = DetectMissingProbesUseCase.xǁDetectMissingProbesUseCaseǁdetect_missing_probes__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDetectMissingProbesUseCaseǁdetect_missing_probes__mutmut['xǁDetectMissingProbesUseCaseǁdetect_missing_probes__mutmut_6'] = DetectMissingProbesUseCase.xǁDetectMissingProbesUseCaseǁdetect_missing_probes__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDetectMissingProbesUseCaseǁdetect_missing_probes__mutmut['xǁDetectMissingProbesUseCaseǁdetect_missing_probes__mutmut_7'] = DetectMissingProbesUseCase.xǁDetectMissingProbesUseCaseǁdetect_missing_probes__mutmut_7 # type: ignore # mutmut generated
