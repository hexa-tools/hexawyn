from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.keda_port import KedaPort
from hexawyn.application.use_case.keda.keda_triggerauth_list.command import (
    KedaTriggerauthListCommand,
)
from hexawyn.application.use_case.keda.keda_triggerauth_list.response import (
    KedaTriggerauthListResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁKedaTriggerauthListUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁKedaTriggerauthListUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class KedaTriggerauthListUseCase:
    @_mutmut_mutated(mutants_xǁKedaTriggerauthListUseCaseǁ__init____mutmut)
    def __init__(self, port: KedaPort) -> None:
        self._port = port
    def xǁKedaTriggerauthListUseCaseǁ__init____mutmut_orig(self, port: KedaPort) -> None:
        self._port = port
    def xǁKedaTriggerauthListUseCaseǁ__init____mutmut_1(self, port: KedaPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁKedaTriggerauthListUseCaseǁexecute__mutmut)
    def execute(self, command: KedaTriggerauthListCommand) -> KedaTriggerauthListResponse:
        auths = self._port.list_trigger_auths(namespace=command.namespace)
        return KedaTriggerauthListResponse(trigger_auths=[asdict(a) for a in auths])

    def xǁKedaTriggerauthListUseCaseǁexecute__mutmut_orig(self, command: KedaTriggerauthListCommand) -> KedaTriggerauthListResponse:
        auths = self._port.list_trigger_auths(namespace=command.namespace)
        return KedaTriggerauthListResponse(trigger_auths=[asdict(a) for a in auths])

    def xǁKedaTriggerauthListUseCaseǁexecute__mutmut_1(self, command: KedaTriggerauthListCommand) -> KedaTriggerauthListResponse:
        auths = None
        return KedaTriggerauthListResponse(trigger_auths=[asdict(a) for a in auths])

    def xǁKedaTriggerauthListUseCaseǁexecute__mutmut_2(self, command: KedaTriggerauthListCommand) -> KedaTriggerauthListResponse:
        auths = self._port.list_trigger_auths(namespace=None)
        return KedaTriggerauthListResponse(trigger_auths=[asdict(a) for a in auths])

    def xǁKedaTriggerauthListUseCaseǁexecute__mutmut_3(self, command: KedaTriggerauthListCommand) -> KedaTriggerauthListResponse:
        auths = self._port.list_trigger_auths(namespace=command.namespace)
        return KedaTriggerauthListResponse(trigger_auths=None)

    def xǁKedaTriggerauthListUseCaseǁexecute__mutmut_4(self, command: KedaTriggerauthListCommand) -> KedaTriggerauthListResponse:
        auths = self._port.list_trigger_auths(namespace=command.namespace)
        return KedaTriggerauthListResponse(trigger_auths=[asdict(None) for a in auths])

mutants_xǁKedaTriggerauthListUseCaseǁ__init____mutmut['_mutmut_orig'] = KedaTriggerauthListUseCase.xǁKedaTriggerauthListUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁKedaTriggerauthListUseCaseǁ__init____mutmut['xǁKedaTriggerauthListUseCaseǁ__init____mutmut_1'] = KedaTriggerauthListUseCase.xǁKedaTriggerauthListUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁKedaTriggerauthListUseCaseǁexecute__mutmut['_mutmut_orig'] = KedaTriggerauthListUseCase.xǁKedaTriggerauthListUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKedaTriggerauthListUseCaseǁexecute__mutmut['xǁKedaTriggerauthListUseCaseǁexecute__mutmut_1'] = KedaTriggerauthListUseCase.xǁKedaTriggerauthListUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKedaTriggerauthListUseCaseǁexecute__mutmut['xǁKedaTriggerauthListUseCaseǁexecute__mutmut_2'] = KedaTriggerauthListUseCase.xǁKedaTriggerauthListUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKedaTriggerauthListUseCaseǁexecute__mutmut['xǁKedaTriggerauthListUseCaseǁexecute__mutmut_3'] = KedaTriggerauthListUseCase.xǁKedaTriggerauthListUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKedaTriggerauthListUseCaseǁexecute__mutmut['xǁKedaTriggerauthListUseCaseǁexecute__mutmut_4'] = KedaTriggerauthListUseCase.xǁKedaTriggerauthListUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
