from __future__ import annotations

from hexawyn.application.ports.driven.keda_port import KedaPort
from hexawyn.application.use_case.keda.keda_triggerauth_get.command import (
    KedaTriggerauthGetCommand,
)
from hexawyn.application.use_case.keda.keda_triggerauth_get.response import (
    KedaTriggerauthGetResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁKedaTriggerauthGetUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁKedaTriggerauthGetUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class KedaTriggerauthGetUseCase:
    @_mutmut_mutated(mutants_xǁKedaTriggerauthGetUseCaseǁ__init____mutmut)
    def __init__(self, port: KedaPort) -> None:
        self._port = port
    def xǁKedaTriggerauthGetUseCaseǁ__init____mutmut_orig(self, port: KedaPort) -> None:
        self._port = port
    def xǁKedaTriggerauthGetUseCaseǁ__init____mutmut_1(self, port: KedaPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁKedaTriggerauthGetUseCaseǁexecute__mutmut)
    def execute(self, command: KedaTriggerauthGetCommand) -> KedaTriggerauthGetResponse:
        a = self._port.get_trigger_auth(name=command.name, namespace=command.namespace)
        return KedaTriggerauthGetResponse(
            name=a.name,
            namespace=a.namespace,
            kind=a.kind,
            auth_type=a.auth_type.value,
            secret_names=a.secret_names,
            environment_names=a.environment_names,
            pod_identity_provider=a.pod_identity_provider,  # type: ignore
            ready=a.ready,
            message=a.message,  # type: ignore
        )

    def xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_orig(self, command: KedaTriggerauthGetCommand) -> KedaTriggerauthGetResponse:
        a = self._port.get_trigger_auth(name=command.name, namespace=command.namespace)
        return KedaTriggerauthGetResponse(
            name=a.name,
            namespace=a.namespace,
            kind=a.kind,
            auth_type=a.auth_type.value,
            secret_names=a.secret_names,
            environment_names=a.environment_names,
            pod_identity_provider=a.pod_identity_provider,  # type: ignore
            ready=a.ready,
            message=a.message,  # type: ignore
        )

    def xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_1(self, command: KedaTriggerauthGetCommand) -> KedaTriggerauthGetResponse:
        a = None
        return KedaTriggerauthGetResponse(
            name=a.name,
            namespace=a.namespace,
            kind=a.kind,
            auth_type=a.auth_type.value,
            secret_names=a.secret_names,
            environment_names=a.environment_names,
            pod_identity_provider=a.pod_identity_provider,  # type: ignore
            ready=a.ready,
            message=a.message,  # type: ignore
        )

    def xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_2(self, command: KedaTriggerauthGetCommand) -> KedaTriggerauthGetResponse:
        a = self._port.get_trigger_auth(name=None, namespace=command.namespace)
        return KedaTriggerauthGetResponse(
            name=a.name,
            namespace=a.namespace,
            kind=a.kind,
            auth_type=a.auth_type.value,
            secret_names=a.secret_names,
            environment_names=a.environment_names,
            pod_identity_provider=a.pod_identity_provider,  # type: ignore
            ready=a.ready,
            message=a.message,  # type: ignore
        )

    def xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_3(self, command: KedaTriggerauthGetCommand) -> KedaTriggerauthGetResponse:
        a = self._port.get_trigger_auth(name=command.name, namespace=None)
        return KedaTriggerauthGetResponse(
            name=a.name,
            namespace=a.namespace,
            kind=a.kind,
            auth_type=a.auth_type.value,
            secret_names=a.secret_names,
            environment_names=a.environment_names,
            pod_identity_provider=a.pod_identity_provider,  # type: ignore
            ready=a.ready,
            message=a.message,  # type: ignore
        )

    def xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_4(self, command: KedaTriggerauthGetCommand) -> KedaTriggerauthGetResponse:
        a = self._port.get_trigger_auth(namespace=command.namespace)
        return KedaTriggerauthGetResponse(
            name=a.name,
            namespace=a.namespace,
            kind=a.kind,
            auth_type=a.auth_type.value,
            secret_names=a.secret_names,
            environment_names=a.environment_names,
            pod_identity_provider=a.pod_identity_provider,  # type: ignore
            ready=a.ready,
            message=a.message,  # type: ignore
        )

    def xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_5(self, command: KedaTriggerauthGetCommand) -> KedaTriggerauthGetResponse:
        a = self._port.get_trigger_auth(name=command.name, )
        return KedaTriggerauthGetResponse(
            name=a.name,
            namespace=a.namespace,
            kind=a.kind,
            auth_type=a.auth_type.value,
            secret_names=a.secret_names,
            environment_names=a.environment_names,
            pod_identity_provider=a.pod_identity_provider,  # type: ignore
            ready=a.ready,
            message=a.message,  # type: ignore
        )

    def xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_6(self, command: KedaTriggerauthGetCommand) -> KedaTriggerauthGetResponse:
        a = self._port.get_trigger_auth(name=command.name, namespace=command.namespace)
        return KedaTriggerauthGetResponse(
            name=None,
            namespace=a.namespace,
            kind=a.kind,
            auth_type=a.auth_type.value,
            secret_names=a.secret_names,
            environment_names=a.environment_names,
            pod_identity_provider=a.pod_identity_provider,  # type: ignore
            ready=a.ready,
            message=a.message,  # type: ignore
        )

    def xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_7(self, command: KedaTriggerauthGetCommand) -> KedaTriggerauthGetResponse:
        a = self._port.get_trigger_auth(name=command.name, namespace=command.namespace)
        return KedaTriggerauthGetResponse(
            name=a.name,
            namespace=None,
            kind=a.kind,
            auth_type=a.auth_type.value,
            secret_names=a.secret_names,
            environment_names=a.environment_names,
            pod_identity_provider=a.pod_identity_provider,  # type: ignore
            ready=a.ready,
            message=a.message,  # type: ignore
        )

    def xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_8(self, command: KedaTriggerauthGetCommand) -> KedaTriggerauthGetResponse:
        a = self._port.get_trigger_auth(name=command.name, namespace=command.namespace)
        return KedaTriggerauthGetResponse(
            name=a.name,
            namespace=a.namespace,
            kind=None,
            auth_type=a.auth_type.value,
            secret_names=a.secret_names,
            environment_names=a.environment_names,
            pod_identity_provider=a.pod_identity_provider,  # type: ignore
            ready=a.ready,
            message=a.message,  # type: ignore
        )

    def xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_9(self, command: KedaTriggerauthGetCommand) -> KedaTriggerauthGetResponse:
        a = self._port.get_trigger_auth(name=command.name, namespace=command.namespace)
        return KedaTriggerauthGetResponse(
            name=a.name,
            namespace=a.namespace,
            kind=a.kind,
            auth_type=None,
            secret_names=a.secret_names,
            environment_names=a.environment_names,
            pod_identity_provider=a.pod_identity_provider,  # type: ignore
            ready=a.ready,
            message=a.message,  # type: ignore
        )

    def xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_10(self, command: KedaTriggerauthGetCommand) -> KedaTriggerauthGetResponse:
        a = self._port.get_trigger_auth(name=command.name, namespace=command.namespace)
        return KedaTriggerauthGetResponse(
            name=a.name,
            namespace=a.namespace,
            kind=a.kind,
            auth_type=a.auth_type.value,
            secret_names=None,
            environment_names=a.environment_names,
            pod_identity_provider=a.pod_identity_provider,  # type: ignore
            ready=a.ready,
            message=a.message,  # type: ignore
        )

    def xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_11(self, command: KedaTriggerauthGetCommand) -> KedaTriggerauthGetResponse:
        a = self._port.get_trigger_auth(name=command.name, namespace=command.namespace)
        return KedaTriggerauthGetResponse(
            name=a.name,
            namespace=a.namespace,
            kind=a.kind,
            auth_type=a.auth_type.value,
            secret_names=a.secret_names,
            environment_names=None,
            pod_identity_provider=a.pod_identity_provider,  # type: ignore
            ready=a.ready,
            message=a.message,  # type: ignore
        )

    def xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_12(self, command: KedaTriggerauthGetCommand) -> KedaTriggerauthGetResponse:
        a = self._port.get_trigger_auth(name=command.name, namespace=command.namespace)
        return KedaTriggerauthGetResponse(
            name=a.name,
            namespace=a.namespace,
            kind=a.kind,
            auth_type=a.auth_type.value,
            secret_names=a.secret_names,
            environment_names=a.environment_names,
            pod_identity_provider=None,  # type: ignore
            ready=a.ready,
            message=a.message,  # type: ignore
        )

    def xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_13(self, command: KedaTriggerauthGetCommand) -> KedaTriggerauthGetResponse:
        a = self._port.get_trigger_auth(name=command.name, namespace=command.namespace)
        return KedaTriggerauthGetResponse(
            name=a.name,
            namespace=a.namespace,
            kind=a.kind,
            auth_type=a.auth_type.value,
            secret_names=a.secret_names,
            environment_names=a.environment_names,
            pod_identity_provider=a.pod_identity_provider,  # type: ignore
            ready=None,
            message=a.message,  # type: ignore
        )

    def xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_14(self, command: KedaTriggerauthGetCommand) -> KedaTriggerauthGetResponse:
        a = self._port.get_trigger_auth(name=command.name, namespace=command.namespace)
        return KedaTriggerauthGetResponse(
            name=a.name,
            namespace=a.namespace,
            kind=a.kind,
            auth_type=a.auth_type.value,
            secret_names=a.secret_names,
            environment_names=a.environment_names,
            pod_identity_provider=a.pod_identity_provider,  # type: ignore
            ready=a.ready,
            message=None,  # type: ignore
        )

    def xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_15(self, command: KedaTriggerauthGetCommand) -> KedaTriggerauthGetResponse:
        a = self._port.get_trigger_auth(name=command.name, namespace=command.namespace)
        return KedaTriggerauthGetResponse(
            namespace=a.namespace,
            kind=a.kind,
            auth_type=a.auth_type.value,
            secret_names=a.secret_names,
            environment_names=a.environment_names,
            pod_identity_provider=a.pod_identity_provider,  # type: ignore
            ready=a.ready,
            message=a.message,  # type: ignore
        )

    def xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_16(self, command: KedaTriggerauthGetCommand) -> KedaTriggerauthGetResponse:
        a = self._port.get_trigger_auth(name=command.name, namespace=command.namespace)
        return KedaTriggerauthGetResponse(
            name=a.name,
            kind=a.kind,
            auth_type=a.auth_type.value,
            secret_names=a.secret_names,
            environment_names=a.environment_names,
            pod_identity_provider=a.pod_identity_provider,  # type: ignore
            ready=a.ready,
            message=a.message,  # type: ignore
        )

    def xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_17(self, command: KedaTriggerauthGetCommand) -> KedaTriggerauthGetResponse:
        a = self._port.get_trigger_auth(name=command.name, namespace=command.namespace)
        return KedaTriggerauthGetResponse(
            name=a.name,
            namespace=a.namespace,
            auth_type=a.auth_type.value,
            secret_names=a.secret_names,
            environment_names=a.environment_names,
            pod_identity_provider=a.pod_identity_provider,  # type: ignore
            ready=a.ready,
            message=a.message,  # type: ignore
        )

    def xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_18(self, command: KedaTriggerauthGetCommand) -> KedaTriggerauthGetResponse:
        a = self._port.get_trigger_auth(name=command.name, namespace=command.namespace)
        return KedaTriggerauthGetResponse(
            name=a.name,
            namespace=a.namespace,
            kind=a.kind,
            secret_names=a.secret_names,
            environment_names=a.environment_names,
            pod_identity_provider=a.pod_identity_provider,  # type: ignore
            ready=a.ready,
            message=a.message,  # type: ignore
        )

    def xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_19(self, command: KedaTriggerauthGetCommand) -> KedaTriggerauthGetResponse:
        a = self._port.get_trigger_auth(name=command.name, namespace=command.namespace)
        return KedaTriggerauthGetResponse(
            name=a.name,
            namespace=a.namespace,
            kind=a.kind,
            auth_type=a.auth_type.value,
            environment_names=a.environment_names,
            pod_identity_provider=a.pod_identity_provider,  # type: ignore
            ready=a.ready,
            message=a.message,  # type: ignore
        )

    def xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_20(self, command: KedaTriggerauthGetCommand) -> KedaTriggerauthGetResponse:
        a = self._port.get_trigger_auth(name=command.name, namespace=command.namespace)
        return KedaTriggerauthGetResponse(
            name=a.name,
            namespace=a.namespace,
            kind=a.kind,
            auth_type=a.auth_type.value,
            secret_names=a.secret_names,
            pod_identity_provider=a.pod_identity_provider,  # type: ignore
            ready=a.ready,
            message=a.message,  # type: ignore
        )

    def xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_21(self, command: KedaTriggerauthGetCommand) -> KedaTriggerauthGetResponse:
        a = self._port.get_trigger_auth(name=command.name, namespace=command.namespace)
        return KedaTriggerauthGetResponse(
            name=a.name,
            namespace=a.namespace,
            kind=a.kind,
            auth_type=a.auth_type.value,
            secret_names=a.secret_names,
            environment_names=a.environment_names,
            ready=a.ready,
            message=a.message,  # type: ignore
        )

    def xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_22(self, command: KedaTriggerauthGetCommand) -> KedaTriggerauthGetResponse:
        a = self._port.get_trigger_auth(name=command.name, namespace=command.namespace)
        return KedaTriggerauthGetResponse(
            name=a.name,
            namespace=a.namespace,
            kind=a.kind,
            auth_type=a.auth_type.value,
            secret_names=a.secret_names,
            environment_names=a.environment_names,
            pod_identity_provider=a.pod_identity_provider,  # type: ignore
            message=a.message,  # type: ignore
        )

    def xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_23(self, command: KedaTriggerauthGetCommand) -> KedaTriggerauthGetResponse:
        a = self._port.get_trigger_auth(name=command.name, namespace=command.namespace)
        return KedaTriggerauthGetResponse(
            name=a.name,
            namespace=a.namespace,
            kind=a.kind,
            auth_type=a.auth_type.value,
            secret_names=a.secret_names,
            environment_names=a.environment_names,
            pod_identity_provider=a.pod_identity_provider,  # type: ignore
            ready=a.ready,
            )

mutants_xǁKedaTriggerauthGetUseCaseǁ__init____mutmut['_mutmut_orig'] = KedaTriggerauthGetUseCase.xǁKedaTriggerauthGetUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁKedaTriggerauthGetUseCaseǁ__init____mutmut['xǁKedaTriggerauthGetUseCaseǁ__init____mutmut_1'] = KedaTriggerauthGetUseCase.xǁKedaTriggerauthGetUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁKedaTriggerauthGetUseCaseǁexecute__mutmut['_mutmut_orig'] = KedaTriggerauthGetUseCase.xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKedaTriggerauthGetUseCaseǁexecute__mutmut['xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_1'] = KedaTriggerauthGetUseCase.xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKedaTriggerauthGetUseCaseǁexecute__mutmut['xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_2'] = KedaTriggerauthGetUseCase.xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKedaTriggerauthGetUseCaseǁexecute__mutmut['xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_3'] = KedaTriggerauthGetUseCase.xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKedaTriggerauthGetUseCaseǁexecute__mutmut['xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_4'] = KedaTriggerauthGetUseCase.xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKedaTriggerauthGetUseCaseǁexecute__mutmut['xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_5'] = KedaTriggerauthGetUseCase.xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKedaTriggerauthGetUseCaseǁexecute__mutmut['xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_6'] = KedaTriggerauthGetUseCase.xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKedaTriggerauthGetUseCaseǁexecute__mutmut['xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_7'] = KedaTriggerauthGetUseCase.xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKedaTriggerauthGetUseCaseǁexecute__mutmut['xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_8'] = KedaTriggerauthGetUseCase.xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKedaTriggerauthGetUseCaseǁexecute__mutmut['xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_9'] = KedaTriggerauthGetUseCase.xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKedaTriggerauthGetUseCaseǁexecute__mutmut['xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_10'] = KedaTriggerauthGetUseCase.xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKedaTriggerauthGetUseCaseǁexecute__mutmut['xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_11'] = KedaTriggerauthGetUseCase.xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKedaTriggerauthGetUseCaseǁexecute__mutmut['xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_12'] = KedaTriggerauthGetUseCase.xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKedaTriggerauthGetUseCaseǁexecute__mutmut['xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_13'] = KedaTriggerauthGetUseCase.xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKedaTriggerauthGetUseCaseǁexecute__mutmut['xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_14'] = KedaTriggerauthGetUseCase.xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁKedaTriggerauthGetUseCaseǁexecute__mutmut['xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_15'] = KedaTriggerauthGetUseCase.xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁKedaTriggerauthGetUseCaseǁexecute__mutmut['xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_16'] = KedaTriggerauthGetUseCase.xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁKedaTriggerauthGetUseCaseǁexecute__mutmut['xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_17'] = KedaTriggerauthGetUseCase.xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁKedaTriggerauthGetUseCaseǁexecute__mutmut['xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_18'] = KedaTriggerauthGetUseCase.xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁKedaTriggerauthGetUseCaseǁexecute__mutmut['xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_19'] = KedaTriggerauthGetUseCase.xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁKedaTriggerauthGetUseCaseǁexecute__mutmut['xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_20'] = KedaTriggerauthGetUseCase.xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁKedaTriggerauthGetUseCaseǁexecute__mutmut['xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_21'] = KedaTriggerauthGetUseCase.xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁKedaTriggerauthGetUseCaseǁexecute__mutmut['xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_22'] = KedaTriggerauthGetUseCase.xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁKedaTriggerauthGetUseCaseǁexecute__mutmut['xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_23'] = KedaTriggerauthGetUseCase.xǁKedaTriggerauthGetUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
