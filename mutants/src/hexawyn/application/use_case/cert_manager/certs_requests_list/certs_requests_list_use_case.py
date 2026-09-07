from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.cert_manager_port import CertManagerPort
from hexawyn.application.use_case.cert_manager.certs_requests_list.command import (
    CertsRequestsListCommand,
)
from hexawyn.application.use_case.cert_manager.certs_requests_list.response import (
    CertsRequestsListResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCertsRequestsListUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁCertsRequestsListUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class CertsRequestsListUseCase:
    @_mutmut_mutated(mutants_xǁCertsRequestsListUseCaseǁ__init____mutmut)
    def __init__(self, port: CertManagerPort) -> None:
        self._port = port
    def xǁCertsRequestsListUseCaseǁ__init____mutmut_orig(self, port: CertManagerPort) -> None:
        self._port = port
    def xǁCertsRequestsListUseCaseǁ__init____mutmut_1(self, port: CertManagerPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁCertsRequestsListUseCaseǁexecute__mutmut)
    def execute(self, command: CertsRequestsListCommand) -> CertsRequestsListResponse:
        reqs = self._port.list_requests(namespace=command.namespace)
        return CertsRequestsListResponse(requests=[asdict(r) for r in reqs])

    def xǁCertsRequestsListUseCaseǁexecute__mutmut_orig(self, command: CertsRequestsListCommand) -> CertsRequestsListResponse:
        reqs = self._port.list_requests(namespace=command.namespace)
        return CertsRequestsListResponse(requests=[asdict(r) for r in reqs])

    def xǁCertsRequestsListUseCaseǁexecute__mutmut_1(self, command: CertsRequestsListCommand) -> CertsRequestsListResponse:
        reqs = None
        return CertsRequestsListResponse(requests=[asdict(r) for r in reqs])

    def xǁCertsRequestsListUseCaseǁexecute__mutmut_2(self, command: CertsRequestsListCommand) -> CertsRequestsListResponse:
        reqs = self._port.list_requests(namespace=None)
        return CertsRequestsListResponse(requests=[asdict(r) for r in reqs])

    def xǁCertsRequestsListUseCaseǁexecute__mutmut_3(self, command: CertsRequestsListCommand) -> CertsRequestsListResponse:
        reqs = self._port.list_requests(namespace=command.namespace)
        return CertsRequestsListResponse(requests=None)

    def xǁCertsRequestsListUseCaseǁexecute__mutmut_4(self, command: CertsRequestsListCommand) -> CertsRequestsListResponse:
        reqs = self._port.list_requests(namespace=command.namespace)
        return CertsRequestsListResponse(requests=[asdict(None) for r in reqs])

mutants_xǁCertsRequestsListUseCaseǁ__init____mutmut['_mutmut_orig'] = CertsRequestsListUseCase.xǁCertsRequestsListUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCertsRequestsListUseCaseǁ__init____mutmut['xǁCertsRequestsListUseCaseǁ__init____mutmut_1'] = CertsRequestsListUseCase.xǁCertsRequestsListUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁCertsRequestsListUseCaseǁexecute__mutmut['_mutmut_orig'] = CertsRequestsListUseCase.xǁCertsRequestsListUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCertsRequestsListUseCaseǁexecute__mutmut['xǁCertsRequestsListUseCaseǁexecute__mutmut_1'] = CertsRequestsListUseCase.xǁCertsRequestsListUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCertsRequestsListUseCaseǁexecute__mutmut['xǁCertsRequestsListUseCaseǁexecute__mutmut_2'] = CertsRequestsListUseCase.xǁCertsRequestsListUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCertsRequestsListUseCaseǁexecute__mutmut['xǁCertsRequestsListUseCaseǁexecute__mutmut_3'] = CertsRequestsListUseCase.xǁCertsRequestsListUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCertsRequestsListUseCaseǁexecute__mutmut['xǁCertsRequestsListUseCaseǁexecute__mutmut_4'] = CertsRequestsListUseCase.xǁCertsRequestsListUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
