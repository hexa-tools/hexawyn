from __future__ import annotations

from hexawyn.application.ports.driven.tls_compliance_port import TLSCompliancePort
from hexawyn.application.use_case.security.audit_tls_compliance.command import (
    AuditTlsComplianceCommand,
)
from hexawyn.application.use_case.security.audit_tls_compliance.response import (
    AuditTlsComplianceResponse,
)
from hexawyn.domain.services.tls_compliance.tls_compliance_engine import (
    TLSComplianceEngine,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁAuditTLSComplianceUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁAuditTLSComplianceUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class AuditTLSComplianceUseCase:
    @_mutmut_mutated(mutants_xǁAuditTLSComplianceUseCaseǁ__init____mutmut)
    def __init__(self, tls_port: TLSCompliancePort) -> None:
        self._port = tls_port
        self._engine = TLSComplianceEngine()
    def xǁAuditTLSComplianceUseCaseǁ__init____mutmut_orig(self, tls_port: TLSCompliancePort) -> None:
        self._port = tls_port
        self._engine = TLSComplianceEngine()
    def xǁAuditTLSComplianceUseCaseǁ__init____mutmut_1(self, tls_port: TLSCompliancePort) -> None:
        self._port = None
        self._engine = TLSComplianceEngine()
    def xǁAuditTLSComplianceUseCaseǁ__init____mutmut_2(self, tls_port: TLSCompliancePort) -> None:
        self._port = tls_port
        self._engine = None

    @_mutmut_mutated(mutants_xǁAuditTLSComplianceUseCaseǁexecute__mutmut)
    def execute(self, command: AuditTlsComplianceCommand) -> AuditTlsComplianceResponse:
        raw = self._port.scan_services()
        services: list[dict[str, object]] = [dict(s) for s in raw]
        result = self._engine.compute(services)
        return AuditTlsComplianceResponse(result=result)

    def xǁAuditTLSComplianceUseCaseǁexecute__mutmut_orig(self, command: AuditTlsComplianceCommand) -> AuditTlsComplianceResponse:
        raw = self._port.scan_services()
        services: list[dict[str, object]] = [dict(s) for s in raw]
        result = self._engine.compute(services)
        return AuditTlsComplianceResponse(result=result)

    def xǁAuditTLSComplianceUseCaseǁexecute__mutmut_1(self, command: AuditTlsComplianceCommand) -> AuditTlsComplianceResponse:
        raw = None
        services: list[dict[str, object]] = [dict(s) for s in raw]
        result = self._engine.compute(services)
        return AuditTlsComplianceResponse(result=result)

    def xǁAuditTLSComplianceUseCaseǁexecute__mutmut_2(self, command: AuditTlsComplianceCommand) -> AuditTlsComplianceResponse:
        raw = self._port.scan_services()
        services: list[dict[str, object]] = None
        result = self._engine.compute(services)
        return AuditTlsComplianceResponse(result=result)

    def xǁAuditTLSComplianceUseCaseǁexecute__mutmut_3(self, command: AuditTlsComplianceCommand) -> AuditTlsComplianceResponse:
        raw = self._port.scan_services()
        services: list[dict[str, object]] = [dict(None) for s in raw]
        result = self._engine.compute(services)
        return AuditTlsComplianceResponse(result=result)

    def xǁAuditTLSComplianceUseCaseǁexecute__mutmut_4(self, command: AuditTlsComplianceCommand) -> AuditTlsComplianceResponse:
        raw = self._port.scan_services()
        services: list[dict[str, object]] = [dict(s) for s in raw]
        result = None
        return AuditTlsComplianceResponse(result=result)

    def xǁAuditTLSComplianceUseCaseǁexecute__mutmut_5(self, command: AuditTlsComplianceCommand) -> AuditTlsComplianceResponse:
        raw = self._port.scan_services()
        services: list[dict[str, object]] = [dict(s) for s in raw]
        result = self._engine.compute(None)
        return AuditTlsComplianceResponse(result=result)

    def xǁAuditTLSComplianceUseCaseǁexecute__mutmut_6(self, command: AuditTlsComplianceCommand) -> AuditTlsComplianceResponse:
        raw = self._port.scan_services()
        services: list[dict[str, object]] = [dict(s) for s in raw]
        result = self._engine.compute(services)
        return AuditTlsComplianceResponse(result=None)

mutants_xǁAuditTLSComplianceUseCaseǁ__init____mutmut['_mutmut_orig'] = AuditTLSComplianceUseCase.xǁAuditTLSComplianceUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁAuditTLSComplianceUseCaseǁ__init____mutmut['xǁAuditTLSComplianceUseCaseǁ__init____mutmut_1'] = AuditTLSComplianceUseCase.xǁAuditTLSComplianceUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁAuditTLSComplianceUseCaseǁ__init____mutmut['xǁAuditTLSComplianceUseCaseǁ__init____mutmut_2'] = AuditTLSComplianceUseCase.xǁAuditTLSComplianceUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁAuditTLSComplianceUseCaseǁexecute__mutmut['_mutmut_orig'] = AuditTLSComplianceUseCase.xǁAuditTLSComplianceUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAuditTLSComplianceUseCaseǁexecute__mutmut['xǁAuditTLSComplianceUseCaseǁexecute__mutmut_1'] = AuditTLSComplianceUseCase.xǁAuditTLSComplianceUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAuditTLSComplianceUseCaseǁexecute__mutmut['xǁAuditTLSComplianceUseCaseǁexecute__mutmut_2'] = AuditTLSComplianceUseCase.xǁAuditTLSComplianceUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAuditTLSComplianceUseCaseǁexecute__mutmut['xǁAuditTLSComplianceUseCaseǁexecute__mutmut_3'] = AuditTLSComplianceUseCase.xǁAuditTLSComplianceUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAuditTLSComplianceUseCaseǁexecute__mutmut['xǁAuditTLSComplianceUseCaseǁexecute__mutmut_4'] = AuditTLSComplianceUseCase.xǁAuditTLSComplianceUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAuditTLSComplianceUseCaseǁexecute__mutmut['xǁAuditTLSComplianceUseCaseǁexecute__mutmut_5'] = AuditTLSComplianceUseCase.xǁAuditTLSComplianceUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAuditTLSComplianceUseCaseǁexecute__mutmut['xǁAuditTLSComplianceUseCaseǁexecute__mutmut_6'] = AuditTLSComplianceUseCase.xǁAuditTLSComplianceUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
