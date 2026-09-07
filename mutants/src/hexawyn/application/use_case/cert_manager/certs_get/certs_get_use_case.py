from __future__ import annotations

from hexawyn.application.ports.driven.cert_manager_port import CertManagerPort
from hexawyn.application.use_case.cert_manager.certs_get.command import CertsGetCommand
from hexawyn.application.use_case.cert_manager.certs_get.response import CertsGetResponse


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCertsGetUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁCertsGetUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class CertsGetUseCase:
    @_mutmut_mutated(mutants_xǁCertsGetUseCaseǁ__init____mutmut)
    def __init__(self, port: CertManagerPort) -> None:
        self._port = port
    def xǁCertsGetUseCaseǁ__init____mutmut_orig(self, port: CertManagerPort) -> None:
        self._port = port
    def xǁCertsGetUseCaseǁ__init____mutmut_1(self, port: CertManagerPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁCertsGetUseCaseǁexecute__mutmut)
    def execute(self, command: CertsGetCommand) -> CertsGetResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsGetResponse(
            name=c.name,
            namespace=c.namespace,
            status=c.status.value,
            issuer_name=c.issuer_name,
            issuer_type=c.issuer_type.value,
            dns_names=c.dns_names,
            not_before=c.not_before,
            not_after=c.not_after,
            days_until_expiry=c.days_until_expiry,
            renewal_time=c.renewal_time,
            auto_renew=c.auto_renew,
            message=c.message,
        )

    def xǁCertsGetUseCaseǁexecute__mutmut_orig(self, command: CertsGetCommand) -> CertsGetResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsGetResponse(
            name=c.name,
            namespace=c.namespace,
            status=c.status.value,
            issuer_name=c.issuer_name,
            issuer_type=c.issuer_type.value,
            dns_names=c.dns_names,
            not_before=c.not_before,
            not_after=c.not_after,
            days_until_expiry=c.days_until_expiry,
            renewal_time=c.renewal_time,
            auto_renew=c.auto_renew,
            message=c.message,
        )

    def xǁCertsGetUseCaseǁexecute__mutmut_1(self, command: CertsGetCommand) -> CertsGetResponse:
        c = None
        return CertsGetResponse(
            name=c.name,
            namespace=c.namespace,
            status=c.status.value,
            issuer_name=c.issuer_name,
            issuer_type=c.issuer_type.value,
            dns_names=c.dns_names,
            not_before=c.not_before,
            not_after=c.not_after,
            days_until_expiry=c.days_until_expiry,
            renewal_time=c.renewal_time,
            auto_renew=c.auto_renew,
            message=c.message,
        )

    def xǁCertsGetUseCaseǁexecute__mutmut_2(self, command: CertsGetCommand) -> CertsGetResponse:
        c = self._port.get_certificate(name=None, namespace=command.namespace)
        return CertsGetResponse(
            name=c.name,
            namespace=c.namespace,
            status=c.status.value,
            issuer_name=c.issuer_name,
            issuer_type=c.issuer_type.value,
            dns_names=c.dns_names,
            not_before=c.not_before,
            not_after=c.not_after,
            days_until_expiry=c.days_until_expiry,
            renewal_time=c.renewal_time,
            auto_renew=c.auto_renew,
            message=c.message,
        )

    def xǁCertsGetUseCaseǁexecute__mutmut_3(self, command: CertsGetCommand) -> CertsGetResponse:
        c = self._port.get_certificate(name=command.name, namespace=None)
        return CertsGetResponse(
            name=c.name,
            namespace=c.namespace,
            status=c.status.value,
            issuer_name=c.issuer_name,
            issuer_type=c.issuer_type.value,
            dns_names=c.dns_names,
            not_before=c.not_before,
            not_after=c.not_after,
            days_until_expiry=c.days_until_expiry,
            renewal_time=c.renewal_time,
            auto_renew=c.auto_renew,
            message=c.message,
        )

    def xǁCertsGetUseCaseǁexecute__mutmut_4(self, command: CertsGetCommand) -> CertsGetResponse:
        c = self._port.get_certificate(namespace=command.namespace)
        return CertsGetResponse(
            name=c.name,
            namespace=c.namespace,
            status=c.status.value,
            issuer_name=c.issuer_name,
            issuer_type=c.issuer_type.value,
            dns_names=c.dns_names,
            not_before=c.not_before,
            not_after=c.not_after,
            days_until_expiry=c.days_until_expiry,
            renewal_time=c.renewal_time,
            auto_renew=c.auto_renew,
            message=c.message,
        )

    def xǁCertsGetUseCaseǁexecute__mutmut_5(self, command: CertsGetCommand) -> CertsGetResponse:
        c = self._port.get_certificate(name=command.name, )
        return CertsGetResponse(
            name=c.name,
            namespace=c.namespace,
            status=c.status.value,
            issuer_name=c.issuer_name,
            issuer_type=c.issuer_type.value,
            dns_names=c.dns_names,
            not_before=c.not_before,
            not_after=c.not_after,
            days_until_expiry=c.days_until_expiry,
            renewal_time=c.renewal_time,
            auto_renew=c.auto_renew,
            message=c.message,
        )

    def xǁCertsGetUseCaseǁexecute__mutmut_6(self, command: CertsGetCommand) -> CertsGetResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsGetResponse(
            name=None,
            namespace=c.namespace,
            status=c.status.value,
            issuer_name=c.issuer_name,
            issuer_type=c.issuer_type.value,
            dns_names=c.dns_names,
            not_before=c.not_before,
            not_after=c.not_after,
            days_until_expiry=c.days_until_expiry,
            renewal_time=c.renewal_time,
            auto_renew=c.auto_renew,
            message=c.message,
        )

    def xǁCertsGetUseCaseǁexecute__mutmut_7(self, command: CertsGetCommand) -> CertsGetResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsGetResponse(
            name=c.name,
            namespace=None,
            status=c.status.value,
            issuer_name=c.issuer_name,
            issuer_type=c.issuer_type.value,
            dns_names=c.dns_names,
            not_before=c.not_before,
            not_after=c.not_after,
            days_until_expiry=c.days_until_expiry,
            renewal_time=c.renewal_time,
            auto_renew=c.auto_renew,
            message=c.message,
        )

    def xǁCertsGetUseCaseǁexecute__mutmut_8(self, command: CertsGetCommand) -> CertsGetResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsGetResponse(
            name=c.name,
            namespace=c.namespace,
            status=None,
            issuer_name=c.issuer_name,
            issuer_type=c.issuer_type.value,
            dns_names=c.dns_names,
            not_before=c.not_before,
            not_after=c.not_after,
            days_until_expiry=c.days_until_expiry,
            renewal_time=c.renewal_time,
            auto_renew=c.auto_renew,
            message=c.message,
        )

    def xǁCertsGetUseCaseǁexecute__mutmut_9(self, command: CertsGetCommand) -> CertsGetResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsGetResponse(
            name=c.name,
            namespace=c.namespace,
            status=c.status.value,
            issuer_name=None,
            issuer_type=c.issuer_type.value,
            dns_names=c.dns_names,
            not_before=c.not_before,
            not_after=c.not_after,
            days_until_expiry=c.days_until_expiry,
            renewal_time=c.renewal_time,
            auto_renew=c.auto_renew,
            message=c.message,
        )

    def xǁCertsGetUseCaseǁexecute__mutmut_10(self, command: CertsGetCommand) -> CertsGetResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsGetResponse(
            name=c.name,
            namespace=c.namespace,
            status=c.status.value,
            issuer_name=c.issuer_name,
            issuer_type=None,
            dns_names=c.dns_names,
            not_before=c.not_before,
            not_after=c.not_after,
            days_until_expiry=c.days_until_expiry,
            renewal_time=c.renewal_time,
            auto_renew=c.auto_renew,
            message=c.message,
        )

    def xǁCertsGetUseCaseǁexecute__mutmut_11(self, command: CertsGetCommand) -> CertsGetResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsGetResponse(
            name=c.name,
            namespace=c.namespace,
            status=c.status.value,
            issuer_name=c.issuer_name,
            issuer_type=c.issuer_type.value,
            dns_names=None,
            not_before=c.not_before,
            not_after=c.not_after,
            days_until_expiry=c.days_until_expiry,
            renewal_time=c.renewal_time,
            auto_renew=c.auto_renew,
            message=c.message,
        )

    def xǁCertsGetUseCaseǁexecute__mutmut_12(self, command: CertsGetCommand) -> CertsGetResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsGetResponse(
            name=c.name,
            namespace=c.namespace,
            status=c.status.value,
            issuer_name=c.issuer_name,
            issuer_type=c.issuer_type.value,
            dns_names=c.dns_names,
            not_before=None,
            not_after=c.not_after,
            days_until_expiry=c.days_until_expiry,
            renewal_time=c.renewal_time,
            auto_renew=c.auto_renew,
            message=c.message,
        )

    def xǁCertsGetUseCaseǁexecute__mutmut_13(self, command: CertsGetCommand) -> CertsGetResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsGetResponse(
            name=c.name,
            namespace=c.namespace,
            status=c.status.value,
            issuer_name=c.issuer_name,
            issuer_type=c.issuer_type.value,
            dns_names=c.dns_names,
            not_before=c.not_before,
            not_after=None,
            days_until_expiry=c.days_until_expiry,
            renewal_time=c.renewal_time,
            auto_renew=c.auto_renew,
            message=c.message,
        )

    def xǁCertsGetUseCaseǁexecute__mutmut_14(self, command: CertsGetCommand) -> CertsGetResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsGetResponse(
            name=c.name,
            namespace=c.namespace,
            status=c.status.value,
            issuer_name=c.issuer_name,
            issuer_type=c.issuer_type.value,
            dns_names=c.dns_names,
            not_before=c.not_before,
            not_after=c.not_after,
            days_until_expiry=None,
            renewal_time=c.renewal_time,
            auto_renew=c.auto_renew,
            message=c.message,
        )

    def xǁCertsGetUseCaseǁexecute__mutmut_15(self, command: CertsGetCommand) -> CertsGetResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsGetResponse(
            name=c.name,
            namespace=c.namespace,
            status=c.status.value,
            issuer_name=c.issuer_name,
            issuer_type=c.issuer_type.value,
            dns_names=c.dns_names,
            not_before=c.not_before,
            not_after=c.not_after,
            days_until_expiry=c.days_until_expiry,
            renewal_time=None,
            auto_renew=c.auto_renew,
            message=c.message,
        )

    def xǁCertsGetUseCaseǁexecute__mutmut_16(self, command: CertsGetCommand) -> CertsGetResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsGetResponse(
            name=c.name,
            namespace=c.namespace,
            status=c.status.value,
            issuer_name=c.issuer_name,
            issuer_type=c.issuer_type.value,
            dns_names=c.dns_names,
            not_before=c.not_before,
            not_after=c.not_after,
            days_until_expiry=c.days_until_expiry,
            renewal_time=c.renewal_time,
            auto_renew=None,
            message=c.message,
        )

    def xǁCertsGetUseCaseǁexecute__mutmut_17(self, command: CertsGetCommand) -> CertsGetResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsGetResponse(
            name=c.name,
            namespace=c.namespace,
            status=c.status.value,
            issuer_name=c.issuer_name,
            issuer_type=c.issuer_type.value,
            dns_names=c.dns_names,
            not_before=c.not_before,
            not_after=c.not_after,
            days_until_expiry=c.days_until_expiry,
            renewal_time=c.renewal_time,
            auto_renew=c.auto_renew,
            message=None,
        )

    def xǁCertsGetUseCaseǁexecute__mutmut_18(self, command: CertsGetCommand) -> CertsGetResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsGetResponse(
            namespace=c.namespace,
            status=c.status.value,
            issuer_name=c.issuer_name,
            issuer_type=c.issuer_type.value,
            dns_names=c.dns_names,
            not_before=c.not_before,
            not_after=c.not_after,
            days_until_expiry=c.days_until_expiry,
            renewal_time=c.renewal_time,
            auto_renew=c.auto_renew,
            message=c.message,
        )

    def xǁCertsGetUseCaseǁexecute__mutmut_19(self, command: CertsGetCommand) -> CertsGetResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsGetResponse(
            name=c.name,
            status=c.status.value,
            issuer_name=c.issuer_name,
            issuer_type=c.issuer_type.value,
            dns_names=c.dns_names,
            not_before=c.not_before,
            not_after=c.not_after,
            days_until_expiry=c.days_until_expiry,
            renewal_time=c.renewal_time,
            auto_renew=c.auto_renew,
            message=c.message,
        )

    def xǁCertsGetUseCaseǁexecute__mutmut_20(self, command: CertsGetCommand) -> CertsGetResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsGetResponse(
            name=c.name,
            namespace=c.namespace,
            issuer_name=c.issuer_name,
            issuer_type=c.issuer_type.value,
            dns_names=c.dns_names,
            not_before=c.not_before,
            not_after=c.not_after,
            days_until_expiry=c.days_until_expiry,
            renewal_time=c.renewal_time,
            auto_renew=c.auto_renew,
            message=c.message,
        )

    def xǁCertsGetUseCaseǁexecute__mutmut_21(self, command: CertsGetCommand) -> CertsGetResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsGetResponse(
            name=c.name,
            namespace=c.namespace,
            status=c.status.value,
            issuer_type=c.issuer_type.value,
            dns_names=c.dns_names,
            not_before=c.not_before,
            not_after=c.not_after,
            days_until_expiry=c.days_until_expiry,
            renewal_time=c.renewal_time,
            auto_renew=c.auto_renew,
            message=c.message,
        )

    def xǁCertsGetUseCaseǁexecute__mutmut_22(self, command: CertsGetCommand) -> CertsGetResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsGetResponse(
            name=c.name,
            namespace=c.namespace,
            status=c.status.value,
            issuer_name=c.issuer_name,
            dns_names=c.dns_names,
            not_before=c.not_before,
            not_after=c.not_after,
            days_until_expiry=c.days_until_expiry,
            renewal_time=c.renewal_time,
            auto_renew=c.auto_renew,
            message=c.message,
        )

    def xǁCertsGetUseCaseǁexecute__mutmut_23(self, command: CertsGetCommand) -> CertsGetResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsGetResponse(
            name=c.name,
            namespace=c.namespace,
            status=c.status.value,
            issuer_name=c.issuer_name,
            issuer_type=c.issuer_type.value,
            not_before=c.not_before,
            not_after=c.not_after,
            days_until_expiry=c.days_until_expiry,
            renewal_time=c.renewal_time,
            auto_renew=c.auto_renew,
            message=c.message,
        )

    def xǁCertsGetUseCaseǁexecute__mutmut_24(self, command: CertsGetCommand) -> CertsGetResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsGetResponse(
            name=c.name,
            namespace=c.namespace,
            status=c.status.value,
            issuer_name=c.issuer_name,
            issuer_type=c.issuer_type.value,
            dns_names=c.dns_names,
            not_after=c.not_after,
            days_until_expiry=c.days_until_expiry,
            renewal_time=c.renewal_time,
            auto_renew=c.auto_renew,
            message=c.message,
        )

    def xǁCertsGetUseCaseǁexecute__mutmut_25(self, command: CertsGetCommand) -> CertsGetResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsGetResponse(
            name=c.name,
            namespace=c.namespace,
            status=c.status.value,
            issuer_name=c.issuer_name,
            issuer_type=c.issuer_type.value,
            dns_names=c.dns_names,
            not_before=c.not_before,
            days_until_expiry=c.days_until_expiry,
            renewal_time=c.renewal_time,
            auto_renew=c.auto_renew,
            message=c.message,
        )

    def xǁCertsGetUseCaseǁexecute__mutmut_26(self, command: CertsGetCommand) -> CertsGetResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsGetResponse(
            name=c.name,
            namespace=c.namespace,
            status=c.status.value,
            issuer_name=c.issuer_name,
            issuer_type=c.issuer_type.value,
            dns_names=c.dns_names,
            not_before=c.not_before,
            not_after=c.not_after,
            renewal_time=c.renewal_time,
            auto_renew=c.auto_renew,
            message=c.message,
        )

    def xǁCertsGetUseCaseǁexecute__mutmut_27(self, command: CertsGetCommand) -> CertsGetResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsGetResponse(
            name=c.name,
            namespace=c.namespace,
            status=c.status.value,
            issuer_name=c.issuer_name,
            issuer_type=c.issuer_type.value,
            dns_names=c.dns_names,
            not_before=c.not_before,
            not_after=c.not_after,
            days_until_expiry=c.days_until_expiry,
            auto_renew=c.auto_renew,
            message=c.message,
        )

    def xǁCertsGetUseCaseǁexecute__mutmut_28(self, command: CertsGetCommand) -> CertsGetResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsGetResponse(
            name=c.name,
            namespace=c.namespace,
            status=c.status.value,
            issuer_name=c.issuer_name,
            issuer_type=c.issuer_type.value,
            dns_names=c.dns_names,
            not_before=c.not_before,
            not_after=c.not_after,
            days_until_expiry=c.days_until_expiry,
            renewal_time=c.renewal_time,
            message=c.message,
        )

    def xǁCertsGetUseCaseǁexecute__mutmut_29(self, command: CertsGetCommand) -> CertsGetResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsGetResponse(
            name=c.name,
            namespace=c.namespace,
            status=c.status.value,
            issuer_name=c.issuer_name,
            issuer_type=c.issuer_type.value,
            dns_names=c.dns_names,
            not_before=c.not_before,
            not_after=c.not_after,
            days_until_expiry=c.days_until_expiry,
            renewal_time=c.renewal_time,
            auto_renew=c.auto_renew,
            )

mutants_xǁCertsGetUseCaseǁ__init____mutmut['_mutmut_orig'] = CertsGetUseCase.xǁCertsGetUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCertsGetUseCaseǁ__init____mutmut['xǁCertsGetUseCaseǁ__init____mutmut_1'] = CertsGetUseCase.xǁCertsGetUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁCertsGetUseCaseǁexecute__mutmut['_mutmut_orig'] = CertsGetUseCase.xǁCertsGetUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCertsGetUseCaseǁexecute__mutmut['xǁCertsGetUseCaseǁexecute__mutmut_1'] = CertsGetUseCase.xǁCertsGetUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCertsGetUseCaseǁexecute__mutmut['xǁCertsGetUseCaseǁexecute__mutmut_2'] = CertsGetUseCase.xǁCertsGetUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCertsGetUseCaseǁexecute__mutmut['xǁCertsGetUseCaseǁexecute__mutmut_3'] = CertsGetUseCase.xǁCertsGetUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCertsGetUseCaseǁexecute__mutmut['xǁCertsGetUseCaseǁexecute__mutmut_4'] = CertsGetUseCase.xǁCertsGetUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCertsGetUseCaseǁexecute__mutmut['xǁCertsGetUseCaseǁexecute__mutmut_5'] = CertsGetUseCase.xǁCertsGetUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCertsGetUseCaseǁexecute__mutmut['xǁCertsGetUseCaseǁexecute__mutmut_6'] = CertsGetUseCase.xǁCertsGetUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCertsGetUseCaseǁexecute__mutmut['xǁCertsGetUseCaseǁexecute__mutmut_7'] = CertsGetUseCase.xǁCertsGetUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCertsGetUseCaseǁexecute__mutmut['xǁCertsGetUseCaseǁexecute__mutmut_8'] = CertsGetUseCase.xǁCertsGetUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCertsGetUseCaseǁexecute__mutmut['xǁCertsGetUseCaseǁexecute__mutmut_9'] = CertsGetUseCase.xǁCertsGetUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCertsGetUseCaseǁexecute__mutmut['xǁCertsGetUseCaseǁexecute__mutmut_10'] = CertsGetUseCase.xǁCertsGetUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCertsGetUseCaseǁexecute__mutmut['xǁCertsGetUseCaseǁexecute__mutmut_11'] = CertsGetUseCase.xǁCertsGetUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCertsGetUseCaseǁexecute__mutmut['xǁCertsGetUseCaseǁexecute__mutmut_12'] = CertsGetUseCase.xǁCertsGetUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCertsGetUseCaseǁexecute__mutmut['xǁCertsGetUseCaseǁexecute__mutmut_13'] = CertsGetUseCase.xǁCertsGetUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCertsGetUseCaseǁexecute__mutmut['xǁCertsGetUseCaseǁexecute__mutmut_14'] = CertsGetUseCase.xǁCertsGetUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁCertsGetUseCaseǁexecute__mutmut['xǁCertsGetUseCaseǁexecute__mutmut_15'] = CertsGetUseCase.xǁCertsGetUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁCertsGetUseCaseǁexecute__mutmut['xǁCertsGetUseCaseǁexecute__mutmut_16'] = CertsGetUseCase.xǁCertsGetUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁCertsGetUseCaseǁexecute__mutmut['xǁCertsGetUseCaseǁexecute__mutmut_17'] = CertsGetUseCase.xǁCertsGetUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁCertsGetUseCaseǁexecute__mutmut['xǁCertsGetUseCaseǁexecute__mutmut_18'] = CertsGetUseCase.xǁCertsGetUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁCertsGetUseCaseǁexecute__mutmut['xǁCertsGetUseCaseǁexecute__mutmut_19'] = CertsGetUseCase.xǁCertsGetUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁCertsGetUseCaseǁexecute__mutmut['xǁCertsGetUseCaseǁexecute__mutmut_20'] = CertsGetUseCase.xǁCertsGetUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁCertsGetUseCaseǁexecute__mutmut['xǁCertsGetUseCaseǁexecute__mutmut_21'] = CertsGetUseCase.xǁCertsGetUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁCertsGetUseCaseǁexecute__mutmut['xǁCertsGetUseCaseǁexecute__mutmut_22'] = CertsGetUseCase.xǁCertsGetUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁCertsGetUseCaseǁexecute__mutmut['xǁCertsGetUseCaseǁexecute__mutmut_23'] = CertsGetUseCase.xǁCertsGetUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁCertsGetUseCaseǁexecute__mutmut['xǁCertsGetUseCaseǁexecute__mutmut_24'] = CertsGetUseCase.xǁCertsGetUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁCertsGetUseCaseǁexecute__mutmut['xǁCertsGetUseCaseǁexecute__mutmut_25'] = CertsGetUseCase.xǁCertsGetUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁCertsGetUseCaseǁexecute__mutmut['xǁCertsGetUseCaseǁexecute__mutmut_26'] = CertsGetUseCase.xǁCertsGetUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁCertsGetUseCaseǁexecute__mutmut['xǁCertsGetUseCaseǁexecute__mutmut_27'] = CertsGetUseCase.xǁCertsGetUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁCertsGetUseCaseǁexecute__mutmut['xǁCertsGetUseCaseǁexecute__mutmut_28'] = CertsGetUseCase.xǁCertsGetUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁCertsGetUseCaseǁexecute__mutmut['xǁCertsGetUseCaseǁexecute__mutmut_29'] = CertsGetUseCase.xǁCertsGetUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
