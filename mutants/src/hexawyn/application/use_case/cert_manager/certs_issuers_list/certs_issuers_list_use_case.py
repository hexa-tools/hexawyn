from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.cert_manager_port import CertManagerPort
from hexawyn.application.use_case.cert_manager.certs_issuers_list.command import (
    CertsIssuersListCommand,
)
from hexawyn.application.use_case.cert_manager.certs_issuers_list.response import (
    CertsIssuersListResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCertsIssuersListUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁCertsIssuersListUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class CertsIssuersListUseCase:
    @_mutmut_mutated(mutants_xǁCertsIssuersListUseCaseǁ__init____mutmut)
    def __init__(self, port: CertManagerPort) -> None:
        self._port = port
    def xǁCertsIssuersListUseCaseǁ__init____mutmut_orig(self, port: CertManagerPort) -> None:
        self._port = port
    def xǁCertsIssuersListUseCaseǁ__init____mutmut_1(self, port: CertManagerPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁCertsIssuersListUseCaseǁexecute__mutmut)
    def execute(self, command: CertsIssuersListCommand) -> CertsIssuersListResponse:
        issuers = self._port.list_issuers(namespace=command.namespace)
        return CertsIssuersListResponse(issuers=[asdict(i) for i in issuers])

    def xǁCertsIssuersListUseCaseǁexecute__mutmut_orig(self, command: CertsIssuersListCommand) -> CertsIssuersListResponse:
        issuers = self._port.list_issuers(namespace=command.namespace)
        return CertsIssuersListResponse(issuers=[asdict(i) for i in issuers])

    def xǁCertsIssuersListUseCaseǁexecute__mutmut_1(self, command: CertsIssuersListCommand) -> CertsIssuersListResponse:
        issuers = None
        return CertsIssuersListResponse(issuers=[asdict(i) for i in issuers])

    def xǁCertsIssuersListUseCaseǁexecute__mutmut_2(self, command: CertsIssuersListCommand) -> CertsIssuersListResponse:
        issuers = self._port.list_issuers(namespace=None)
        return CertsIssuersListResponse(issuers=[asdict(i) for i in issuers])

    def xǁCertsIssuersListUseCaseǁexecute__mutmut_3(self, command: CertsIssuersListCommand) -> CertsIssuersListResponse:
        issuers = self._port.list_issuers(namespace=command.namespace)
        return CertsIssuersListResponse(issuers=None)

    def xǁCertsIssuersListUseCaseǁexecute__mutmut_4(self, command: CertsIssuersListCommand) -> CertsIssuersListResponse:
        issuers = self._port.list_issuers(namespace=command.namespace)
        return CertsIssuersListResponse(issuers=[asdict(None) for i in issuers])

mutants_xǁCertsIssuersListUseCaseǁ__init____mutmut['_mutmut_orig'] = CertsIssuersListUseCase.xǁCertsIssuersListUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCertsIssuersListUseCaseǁ__init____mutmut['xǁCertsIssuersListUseCaseǁ__init____mutmut_1'] = CertsIssuersListUseCase.xǁCertsIssuersListUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁCertsIssuersListUseCaseǁexecute__mutmut['_mutmut_orig'] = CertsIssuersListUseCase.xǁCertsIssuersListUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCertsIssuersListUseCaseǁexecute__mutmut['xǁCertsIssuersListUseCaseǁexecute__mutmut_1'] = CertsIssuersListUseCase.xǁCertsIssuersListUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCertsIssuersListUseCaseǁexecute__mutmut['xǁCertsIssuersListUseCaseǁexecute__mutmut_2'] = CertsIssuersListUseCase.xǁCertsIssuersListUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCertsIssuersListUseCaseǁexecute__mutmut['xǁCertsIssuersListUseCaseǁexecute__mutmut_3'] = CertsIssuersListUseCase.xǁCertsIssuersListUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCertsIssuersListUseCaseǁexecute__mutmut['xǁCertsIssuersListUseCaseǁexecute__mutmut_4'] = CertsIssuersListUseCase.xǁCertsIssuersListUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
