from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.cert_manager_port import CertManagerPort
from hexawyn.application.use_case.cert_manager.certs_list.command import CertsListCommand
from hexawyn.application.use_case.cert_manager.certs_list.response import CertsListResponse


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCertsListUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁCertsListUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class CertsListUseCase:
    @_mutmut_mutated(mutants_xǁCertsListUseCaseǁ__init____mutmut)
    def __init__(self, port: CertManagerPort) -> None:
        self._port = port
    def xǁCertsListUseCaseǁ__init____mutmut_orig(self, port: CertManagerPort) -> None:
        self._port = port
    def xǁCertsListUseCaseǁ__init____mutmut_1(self, port: CertManagerPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁCertsListUseCaseǁexecute__mutmut)
    def execute(self, command: CertsListCommand) -> CertsListResponse:
        certs = self._port.list_certificates(namespace=command.namespace)
        return CertsListResponse(certificates=[asdict(c) for c in certs])

    def xǁCertsListUseCaseǁexecute__mutmut_orig(self, command: CertsListCommand) -> CertsListResponse:
        certs = self._port.list_certificates(namespace=command.namespace)
        return CertsListResponse(certificates=[asdict(c) for c in certs])

    def xǁCertsListUseCaseǁexecute__mutmut_1(self, command: CertsListCommand) -> CertsListResponse:
        certs = None
        return CertsListResponse(certificates=[asdict(c) for c in certs])

    def xǁCertsListUseCaseǁexecute__mutmut_2(self, command: CertsListCommand) -> CertsListResponse:
        certs = self._port.list_certificates(namespace=None)
        return CertsListResponse(certificates=[asdict(c) for c in certs])

    def xǁCertsListUseCaseǁexecute__mutmut_3(self, command: CertsListCommand) -> CertsListResponse:
        certs = self._port.list_certificates(namespace=command.namespace)
        return CertsListResponse(certificates=None)

    def xǁCertsListUseCaseǁexecute__mutmut_4(self, command: CertsListCommand) -> CertsListResponse:
        certs = self._port.list_certificates(namespace=command.namespace)
        return CertsListResponse(certificates=[asdict(None) for c in certs])

mutants_xǁCertsListUseCaseǁ__init____mutmut['_mutmut_orig'] = CertsListUseCase.xǁCertsListUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCertsListUseCaseǁ__init____mutmut['xǁCertsListUseCaseǁ__init____mutmut_1'] = CertsListUseCase.xǁCertsListUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁCertsListUseCaseǁexecute__mutmut['_mutmut_orig'] = CertsListUseCase.xǁCertsListUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCertsListUseCaseǁexecute__mutmut['xǁCertsListUseCaseǁexecute__mutmut_1'] = CertsListUseCase.xǁCertsListUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCertsListUseCaseǁexecute__mutmut['xǁCertsListUseCaseǁexecute__mutmut_2'] = CertsListUseCase.xǁCertsListUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCertsListUseCaseǁexecute__mutmut['xǁCertsListUseCaseǁexecute__mutmut_3'] = CertsListUseCase.xǁCertsListUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCertsListUseCaseǁexecute__mutmut['xǁCertsListUseCaseǁexecute__mutmut_4'] = CertsListUseCase.xǁCertsListUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
