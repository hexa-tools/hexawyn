from __future__ import annotations

from hexawyn.application.ports.driven.cert_manager_port import CertManagerPort
from hexawyn.application.use_case.cert_manager.certs_issuer_get.command import (
    CertsIssuerGetCommand,
)
from hexawyn.application.use_case.cert_manager.certs_issuer_get.response import (
    CertsIssuerGetResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCertsIssuerGetUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁCertsIssuerGetUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class CertsIssuerGetUseCase:
    @_mutmut_mutated(mutants_xǁCertsIssuerGetUseCaseǁ__init____mutmut)
    def __init__(self, port: CertManagerPort) -> None:
        self._port = port
    def xǁCertsIssuerGetUseCaseǁ__init____mutmut_orig(self, port: CertManagerPort) -> None:
        self._port = port
    def xǁCertsIssuerGetUseCaseǁ__init____mutmut_1(self, port: CertManagerPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁCertsIssuerGetUseCaseǁexecute__mutmut)
    def execute(self, command: CertsIssuerGetCommand) -> CertsIssuerGetResponse:
        i = self._port.get_issuer(name=command.name, namespace=command.namespace)
        return CertsIssuerGetResponse(
            name=i.name,
            namespace=i.namespace,
            kind=i.kind,
            issuer_type=i.issuer_type.value,
            ready=i.ready,
            server=i.server,
            message=i.message,
        )

    def xǁCertsIssuerGetUseCaseǁexecute__mutmut_orig(self, command: CertsIssuerGetCommand) -> CertsIssuerGetResponse:
        i = self._port.get_issuer(name=command.name, namespace=command.namespace)
        return CertsIssuerGetResponse(
            name=i.name,
            namespace=i.namespace,
            kind=i.kind,
            issuer_type=i.issuer_type.value,
            ready=i.ready,
            server=i.server,
            message=i.message,
        )

    def xǁCertsIssuerGetUseCaseǁexecute__mutmut_1(self, command: CertsIssuerGetCommand) -> CertsIssuerGetResponse:
        i = None
        return CertsIssuerGetResponse(
            name=i.name,
            namespace=i.namespace,
            kind=i.kind,
            issuer_type=i.issuer_type.value,
            ready=i.ready,
            server=i.server,
            message=i.message,
        )

    def xǁCertsIssuerGetUseCaseǁexecute__mutmut_2(self, command: CertsIssuerGetCommand) -> CertsIssuerGetResponse:
        i = self._port.get_issuer(name=None, namespace=command.namespace)
        return CertsIssuerGetResponse(
            name=i.name,
            namespace=i.namespace,
            kind=i.kind,
            issuer_type=i.issuer_type.value,
            ready=i.ready,
            server=i.server,
            message=i.message,
        )

    def xǁCertsIssuerGetUseCaseǁexecute__mutmut_3(self, command: CertsIssuerGetCommand) -> CertsIssuerGetResponse:
        i = self._port.get_issuer(name=command.name, namespace=None)
        return CertsIssuerGetResponse(
            name=i.name,
            namespace=i.namespace,
            kind=i.kind,
            issuer_type=i.issuer_type.value,
            ready=i.ready,
            server=i.server,
            message=i.message,
        )

    def xǁCertsIssuerGetUseCaseǁexecute__mutmut_4(self, command: CertsIssuerGetCommand) -> CertsIssuerGetResponse:
        i = self._port.get_issuer(namespace=command.namespace)
        return CertsIssuerGetResponse(
            name=i.name,
            namespace=i.namespace,
            kind=i.kind,
            issuer_type=i.issuer_type.value,
            ready=i.ready,
            server=i.server,
            message=i.message,
        )

    def xǁCertsIssuerGetUseCaseǁexecute__mutmut_5(self, command: CertsIssuerGetCommand) -> CertsIssuerGetResponse:
        i = self._port.get_issuer(name=command.name, )
        return CertsIssuerGetResponse(
            name=i.name,
            namespace=i.namespace,
            kind=i.kind,
            issuer_type=i.issuer_type.value,
            ready=i.ready,
            server=i.server,
            message=i.message,
        )

    def xǁCertsIssuerGetUseCaseǁexecute__mutmut_6(self, command: CertsIssuerGetCommand) -> CertsIssuerGetResponse:
        i = self._port.get_issuer(name=command.name, namespace=command.namespace)
        return CertsIssuerGetResponse(
            name=None,
            namespace=i.namespace,
            kind=i.kind,
            issuer_type=i.issuer_type.value,
            ready=i.ready,
            server=i.server,
            message=i.message,
        )

    def xǁCertsIssuerGetUseCaseǁexecute__mutmut_7(self, command: CertsIssuerGetCommand) -> CertsIssuerGetResponse:
        i = self._port.get_issuer(name=command.name, namespace=command.namespace)
        return CertsIssuerGetResponse(
            name=i.name,
            namespace=None,
            kind=i.kind,
            issuer_type=i.issuer_type.value,
            ready=i.ready,
            server=i.server,
            message=i.message,
        )

    def xǁCertsIssuerGetUseCaseǁexecute__mutmut_8(self, command: CertsIssuerGetCommand) -> CertsIssuerGetResponse:
        i = self._port.get_issuer(name=command.name, namespace=command.namespace)
        return CertsIssuerGetResponse(
            name=i.name,
            namespace=i.namespace,
            kind=None,
            issuer_type=i.issuer_type.value,
            ready=i.ready,
            server=i.server,
            message=i.message,
        )

    def xǁCertsIssuerGetUseCaseǁexecute__mutmut_9(self, command: CertsIssuerGetCommand) -> CertsIssuerGetResponse:
        i = self._port.get_issuer(name=command.name, namespace=command.namespace)
        return CertsIssuerGetResponse(
            name=i.name,
            namespace=i.namespace,
            kind=i.kind,
            issuer_type=None,
            ready=i.ready,
            server=i.server,
            message=i.message,
        )

    def xǁCertsIssuerGetUseCaseǁexecute__mutmut_10(self, command: CertsIssuerGetCommand) -> CertsIssuerGetResponse:
        i = self._port.get_issuer(name=command.name, namespace=command.namespace)
        return CertsIssuerGetResponse(
            name=i.name,
            namespace=i.namespace,
            kind=i.kind,
            issuer_type=i.issuer_type.value,
            ready=None,
            server=i.server,
            message=i.message,
        )

    def xǁCertsIssuerGetUseCaseǁexecute__mutmut_11(self, command: CertsIssuerGetCommand) -> CertsIssuerGetResponse:
        i = self._port.get_issuer(name=command.name, namespace=command.namespace)
        return CertsIssuerGetResponse(
            name=i.name,
            namespace=i.namespace,
            kind=i.kind,
            issuer_type=i.issuer_type.value,
            ready=i.ready,
            server=None,
            message=i.message,
        )

    def xǁCertsIssuerGetUseCaseǁexecute__mutmut_12(self, command: CertsIssuerGetCommand) -> CertsIssuerGetResponse:
        i = self._port.get_issuer(name=command.name, namespace=command.namespace)
        return CertsIssuerGetResponse(
            name=i.name,
            namespace=i.namespace,
            kind=i.kind,
            issuer_type=i.issuer_type.value,
            ready=i.ready,
            server=i.server,
            message=None,
        )

    def xǁCertsIssuerGetUseCaseǁexecute__mutmut_13(self, command: CertsIssuerGetCommand) -> CertsIssuerGetResponse:
        i = self._port.get_issuer(name=command.name, namespace=command.namespace)
        return CertsIssuerGetResponse(
            namespace=i.namespace,
            kind=i.kind,
            issuer_type=i.issuer_type.value,
            ready=i.ready,
            server=i.server,
            message=i.message,
        )

    def xǁCertsIssuerGetUseCaseǁexecute__mutmut_14(self, command: CertsIssuerGetCommand) -> CertsIssuerGetResponse:
        i = self._port.get_issuer(name=command.name, namespace=command.namespace)
        return CertsIssuerGetResponse(
            name=i.name,
            kind=i.kind,
            issuer_type=i.issuer_type.value,
            ready=i.ready,
            server=i.server,
            message=i.message,
        )

    def xǁCertsIssuerGetUseCaseǁexecute__mutmut_15(self, command: CertsIssuerGetCommand) -> CertsIssuerGetResponse:
        i = self._port.get_issuer(name=command.name, namespace=command.namespace)
        return CertsIssuerGetResponse(
            name=i.name,
            namespace=i.namespace,
            issuer_type=i.issuer_type.value,
            ready=i.ready,
            server=i.server,
            message=i.message,
        )

    def xǁCertsIssuerGetUseCaseǁexecute__mutmut_16(self, command: CertsIssuerGetCommand) -> CertsIssuerGetResponse:
        i = self._port.get_issuer(name=command.name, namespace=command.namespace)
        return CertsIssuerGetResponse(
            name=i.name,
            namespace=i.namespace,
            kind=i.kind,
            ready=i.ready,
            server=i.server,
            message=i.message,
        )

    def xǁCertsIssuerGetUseCaseǁexecute__mutmut_17(self, command: CertsIssuerGetCommand) -> CertsIssuerGetResponse:
        i = self._port.get_issuer(name=command.name, namespace=command.namespace)
        return CertsIssuerGetResponse(
            name=i.name,
            namespace=i.namespace,
            kind=i.kind,
            issuer_type=i.issuer_type.value,
            server=i.server,
            message=i.message,
        )

    def xǁCertsIssuerGetUseCaseǁexecute__mutmut_18(self, command: CertsIssuerGetCommand) -> CertsIssuerGetResponse:
        i = self._port.get_issuer(name=command.name, namespace=command.namespace)
        return CertsIssuerGetResponse(
            name=i.name,
            namespace=i.namespace,
            kind=i.kind,
            issuer_type=i.issuer_type.value,
            ready=i.ready,
            message=i.message,
        )

    def xǁCertsIssuerGetUseCaseǁexecute__mutmut_19(self, command: CertsIssuerGetCommand) -> CertsIssuerGetResponse:
        i = self._port.get_issuer(name=command.name, namespace=command.namespace)
        return CertsIssuerGetResponse(
            name=i.name,
            namespace=i.namespace,
            kind=i.kind,
            issuer_type=i.issuer_type.value,
            ready=i.ready,
            server=i.server,
            )

mutants_xǁCertsIssuerGetUseCaseǁ__init____mutmut['_mutmut_orig'] = CertsIssuerGetUseCase.xǁCertsIssuerGetUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCertsIssuerGetUseCaseǁ__init____mutmut['xǁCertsIssuerGetUseCaseǁ__init____mutmut_1'] = CertsIssuerGetUseCase.xǁCertsIssuerGetUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁCertsIssuerGetUseCaseǁexecute__mutmut['_mutmut_orig'] = CertsIssuerGetUseCase.xǁCertsIssuerGetUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCertsIssuerGetUseCaseǁexecute__mutmut['xǁCertsIssuerGetUseCaseǁexecute__mutmut_1'] = CertsIssuerGetUseCase.xǁCertsIssuerGetUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCertsIssuerGetUseCaseǁexecute__mutmut['xǁCertsIssuerGetUseCaseǁexecute__mutmut_2'] = CertsIssuerGetUseCase.xǁCertsIssuerGetUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCertsIssuerGetUseCaseǁexecute__mutmut['xǁCertsIssuerGetUseCaseǁexecute__mutmut_3'] = CertsIssuerGetUseCase.xǁCertsIssuerGetUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCertsIssuerGetUseCaseǁexecute__mutmut['xǁCertsIssuerGetUseCaseǁexecute__mutmut_4'] = CertsIssuerGetUseCase.xǁCertsIssuerGetUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCertsIssuerGetUseCaseǁexecute__mutmut['xǁCertsIssuerGetUseCaseǁexecute__mutmut_5'] = CertsIssuerGetUseCase.xǁCertsIssuerGetUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCertsIssuerGetUseCaseǁexecute__mutmut['xǁCertsIssuerGetUseCaseǁexecute__mutmut_6'] = CertsIssuerGetUseCase.xǁCertsIssuerGetUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCertsIssuerGetUseCaseǁexecute__mutmut['xǁCertsIssuerGetUseCaseǁexecute__mutmut_7'] = CertsIssuerGetUseCase.xǁCertsIssuerGetUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCertsIssuerGetUseCaseǁexecute__mutmut['xǁCertsIssuerGetUseCaseǁexecute__mutmut_8'] = CertsIssuerGetUseCase.xǁCertsIssuerGetUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCertsIssuerGetUseCaseǁexecute__mutmut['xǁCertsIssuerGetUseCaseǁexecute__mutmut_9'] = CertsIssuerGetUseCase.xǁCertsIssuerGetUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCertsIssuerGetUseCaseǁexecute__mutmut['xǁCertsIssuerGetUseCaseǁexecute__mutmut_10'] = CertsIssuerGetUseCase.xǁCertsIssuerGetUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCertsIssuerGetUseCaseǁexecute__mutmut['xǁCertsIssuerGetUseCaseǁexecute__mutmut_11'] = CertsIssuerGetUseCase.xǁCertsIssuerGetUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCertsIssuerGetUseCaseǁexecute__mutmut['xǁCertsIssuerGetUseCaseǁexecute__mutmut_12'] = CertsIssuerGetUseCase.xǁCertsIssuerGetUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCertsIssuerGetUseCaseǁexecute__mutmut['xǁCertsIssuerGetUseCaseǁexecute__mutmut_13'] = CertsIssuerGetUseCase.xǁCertsIssuerGetUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCertsIssuerGetUseCaseǁexecute__mutmut['xǁCertsIssuerGetUseCaseǁexecute__mutmut_14'] = CertsIssuerGetUseCase.xǁCertsIssuerGetUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁCertsIssuerGetUseCaseǁexecute__mutmut['xǁCertsIssuerGetUseCaseǁexecute__mutmut_15'] = CertsIssuerGetUseCase.xǁCertsIssuerGetUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁCertsIssuerGetUseCaseǁexecute__mutmut['xǁCertsIssuerGetUseCaseǁexecute__mutmut_16'] = CertsIssuerGetUseCase.xǁCertsIssuerGetUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁCertsIssuerGetUseCaseǁexecute__mutmut['xǁCertsIssuerGetUseCaseǁexecute__mutmut_17'] = CertsIssuerGetUseCase.xǁCertsIssuerGetUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁCertsIssuerGetUseCaseǁexecute__mutmut['xǁCertsIssuerGetUseCaseǁexecute__mutmut_18'] = CertsIssuerGetUseCase.xǁCertsIssuerGetUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁCertsIssuerGetUseCaseǁexecute__mutmut['xǁCertsIssuerGetUseCaseǁexecute__mutmut_19'] = CertsIssuerGetUseCase.xǁCertsIssuerGetUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
