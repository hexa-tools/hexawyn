from __future__ import annotations

from hexawyn.application.ports.driven.cert_manager_port import CertManagerPort
from hexawyn.application.use_case.cert_manager.certs_status_explain.command import (
    CertsStatusExplainCommand,
)
from hexawyn.application.use_case.cert_manager.certs_status_explain.response import (
    CertsStatusExplainResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCertsStatusExplainUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁCertsStatusExplainUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class CertsStatusExplainUseCase:
    @_mutmut_mutated(mutants_xǁCertsStatusExplainUseCaseǁ__init____mutmut)
    def __init__(self, port: CertManagerPort) -> None:
        self._port = port
    def xǁCertsStatusExplainUseCaseǁ__init____mutmut_orig(self, port: CertManagerPort) -> None:
        self._port = port
    def xǁCertsStatusExplainUseCaseǁ__init____mutmut_1(self, port: CertManagerPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁCertsStatusExplainUseCaseǁexecute__mutmut)
    def execute(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsStatusExplainResponse(
            status=c.status.value,
            message=c.message,
            explanation=f"Certificate '{command.name}' is in status '{c.status.value}'.",
            fix_suggestion="Check the certificate message for details."
            if c.message
            else "No issues detected.",
        )

    def xǁCertsStatusExplainUseCaseǁexecute__mutmut_orig(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsStatusExplainResponse(
            status=c.status.value,
            message=c.message,
            explanation=f"Certificate '{command.name}' is in status '{c.status.value}'.",
            fix_suggestion="Check the certificate message for details."
            if c.message
            else "No issues detected.",
        )

    def xǁCertsStatusExplainUseCaseǁexecute__mutmut_1(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:
        c = None
        return CertsStatusExplainResponse(
            status=c.status.value,
            message=c.message,
            explanation=f"Certificate '{command.name}' is in status '{c.status.value}'.",
            fix_suggestion="Check the certificate message for details."
            if c.message
            else "No issues detected.",
        )

    def xǁCertsStatusExplainUseCaseǁexecute__mutmut_2(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:
        c = self._port.get_certificate(name=None, namespace=command.namespace)
        return CertsStatusExplainResponse(
            status=c.status.value,
            message=c.message,
            explanation=f"Certificate '{command.name}' is in status '{c.status.value}'.",
            fix_suggestion="Check the certificate message for details."
            if c.message
            else "No issues detected.",
        )

    def xǁCertsStatusExplainUseCaseǁexecute__mutmut_3(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:
        c = self._port.get_certificate(name=command.name, namespace=None)
        return CertsStatusExplainResponse(
            status=c.status.value,
            message=c.message,
            explanation=f"Certificate '{command.name}' is in status '{c.status.value}'.",
            fix_suggestion="Check the certificate message for details."
            if c.message
            else "No issues detected.",
        )

    def xǁCertsStatusExplainUseCaseǁexecute__mutmut_4(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:
        c = self._port.get_certificate(namespace=command.namespace)
        return CertsStatusExplainResponse(
            status=c.status.value,
            message=c.message,
            explanation=f"Certificate '{command.name}' is in status '{c.status.value}'.",
            fix_suggestion="Check the certificate message for details."
            if c.message
            else "No issues detected.",
        )

    def xǁCertsStatusExplainUseCaseǁexecute__mutmut_5(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:
        c = self._port.get_certificate(name=command.name, )
        return CertsStatusExplainResponse(
            status=c.status.value,
            message=c.message,
            explanation=f"Certificate '{command.name}' is in status '{c.status.value}'.",
            fix_suggestion="Check the certificate message for details."
            if c.message
            else "No issues detected.",
        )

    def xǁCertsStatusExplainUseCaseǁexecute__mutmut_6(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsStatusExplainResponse(
            status=None,
            message=c.message,
            explanation=f"Certificate '{command.name}' is in status '{c.status.value}'.",
            fix_suggestion="Check the certificate message for details."
            if c.message
            else "No issues detected.",
        )

    def xǁCertsStatusExplainUseCaseǁexecute__mutmut_7(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsStatusExplainResponse(
            status=c.status.value,
            message=None,
            explanation=f"Certificate '{command.name}' is in status '{c.status.value}'.",
            fix_suggestion="Check the certificate message for details."
            if c.message
            else "No issues detected.",
        )

    def xǁCertsStatusExplainUseCaseǁexecute__mutmut_8(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsStatusExplainResponse(
            status=c.status.value,
            message=c.message,
            explanation=None,
            fix_suggestion="Check the certificate message for details."
            if c.message
            else "No issues detected.",
        )

    def xǁCertsStatusExplainUseCaseǁexecute__mutmut_9(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsStatusExplainResponse(
            status=c.status.value,
            message=c.message,
            explanation=f"Certificate '{command.name}' is in status '{c.status.value}'.",
            fix_suggestion=None,
        )

    def xǁCertsStatusExplainUseCaseǁexecute__mutmut_10(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsStatusExplainResponse(
            message=c.message,
            explanation=f"Certificate '{command.name}' is in status '{c.status.value}'.",
            fix_suggestion="Check the certificate message for details."
            if c.message
            else "No issues detected.",
        )

    def xǁCertsStatusExplainUseCaseǁexecute__mutmut_11(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsStatusExplainResponse(
            status=c.status.value,
            explanation=f"Certificate '{command.name}' is in status '{c.status.value}'.",
            fix_suggestion="Check the certificate message for details."
            if c.message
            else "No issues detected.",
        )

    def xǁCertsStatusExplainUseCaseǁexecute__mutmut_12(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsStatusExplainResponse(
            status=c.status.value,
            message=c.message,
            fix_suggestion="Check the certificate message for details."
            if c.message
            else "No issues detected.",
        )

    def xǁCertsStatusExplainUseCaseǁexecute__mutmut_13(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsStatusExplainResponse(
            status=c.status.value,
            message=c.message,
            explanation=f"Certificate '{command.name}' is in status '{c.status.value}'.",
            )

    def xǁCertsStatusExplainUseCaseǁexecute__mutmut_14(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsStatusExplainResponse(
            status=c.status.value,
            message=c.message,
            explanation=f"Certificate '{command.name}' is in status '{c.status.value}'.",
            fix_suggestion="XXCheck the certificate message for details.XX"
            if c.message
            else "No issues detected.",
        )

    def xǁCertsStatusExplainUseCaseǁexecute__mutmut_15(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsStatusExplainResponse(
            status=c.status.value,
            message=c.message,
            explanation=f"Certificate '{command.name}' is in status '{c.status.value}'.",
            fix_suggestion="check the certificate message for details."
            if c.message
            else "No issues detected.",
        )

    def xǁCertsStatusExplainUseCaseǁexecute__mutmut_16(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsStatusExplainResponse(
            status=c.status.value,
            message=c.message,
            explanation=f"Certificate '{command.name}' is in status '{c.status.value}'.",
            fix_suggestion="CHECK THE CERTIFICATE MESSAGE FOR DETAILS."
            if c.message
            else "No issues detected.",
        )

    def xǁCertsStatusExplainUseCaseǁexecute__mutmut_17(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsStatusExplainResponse(
            status=c.status.value,
            message=c.message,
            explanation=f"Certificate '{command.name}' is in status '{c.status.value}'.",
            fix_suggestion="Check the certificate message for details."
            if c.message
            else "XXNo issues detected.XX",
        )

    def xǁCertsStatusExplainUseCaseǁexecute__mutmut_18(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsStatusExplainResponse(
            status=c.status.value,
            message=c.message,
            explanation=f"Certificate '{command.name}' is in status '{c.status.value}'.",
            fix_suggestion="Check the certificate message for details."
            if c.message
            else "no issues detected.",
        )

    def xǁCertsStatusExplainUseCaseǁexecute__mutmut_19(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsStatusExplainResponse(
            status=c.status.value,
            message=c.message,
            explanation=f"Certificate '{command.name}' is in status '{c.status.value}'.",
            fix_suggestion="Check the certificate message for details."
            if c.message
            else "NO ISSUES DETECTED.",
        )

mutants_xǁCertsStatusExplainUseCaseǁ__init____mutmut['_mutmut_orig'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCertsStatusExplainUseCaseǁ__init____mutmut['xǁCertsStatusExplainUseCaseǁ__init____mutmut_1'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁCertsStatusExplainUseCaseǁexecute__mutmut['_mutmut_orig'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCertsStatusExplainUseCaseǁexecute__mutmut['xǁCertsStatusExplainUseCaseǁexecute__mutmut_1'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCertsStatusExplainUseCaseǁexecute__mutmut['xǁCertsStatusExplainUseCaseǁexecute__mutmut_2'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCertsStatusExplainUseCaseǁexecute__mutmut['xǁCertsStatusExplainUseCaseǁexecute__mutmut_3'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCertsStatusExplainUseCaseǁexecute__mutmut['xǁCertsStatusExplainUseCaseǁexecute__mutmut_4'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCertsStatusExplainUseCaseǁexecute__mutmut['xǁCertsStatusExplainUseCaseǁexecute__mutmut_5'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCertsStatusExplainUseCaseǁexecute__mutmut['xǁCertsStatusExplainUseCaseǁexecute__mutmut_6'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCertsStatusExplainUseCaseǁexecute__mutmut['xǁCertsStatusExplainUseCaseǁexecute__mutmut_7'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCertsStatusExplainUseCaseǁexecute__mutmut['xǁCertsStatusExplainUseCaseǁexecute__mutmut_8'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCertsStatusExplainUseCaseǁexecute__mutmut['xǁCertsStatusExplainUseCaseǁexecute__mutmut_9'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCertsStatusExplainUseCaseǁexecute__mutmut['xǁCertsStatusExplainUseCaseǁexecute__mutmut_10'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCertsStatusExplainUseCaseǁexecute__mutmut['xǁCertsStatusExplainUseCaseǁexecute__mutmut_11'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCertsStatusExplainUseCaseǁexecute__mutmut['xǁCertsStatusExplainUseCaseǁexecute__mutmut_12'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCertsStatusExplainUseCaseǁexecute__mutmut['xǁCertsStatusExplainUseCaseǁexecute__mutmut_13'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCertsStatusExplainUseCaseǁexecute__mutmut['xǁCertsStatusExplainUseCaseǁexecute__mutmut_14'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁCertsStatusExplainUseCaseǁexecute__mutmut['xǁCertsStatusExplainUseCaseǁexecute__mutmut_15'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁCertsStatusExplainUseCaseǁexecute__mutmut['xǁCertsStatusExplainUseCaseǁexecute__mutmut_16'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁCertsStatusExplainUseCaseǁexecute__mutmut['xǁCertsStatusExplainUseCaseǁexecute__mutmut_17'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁCertsStatusExplainUseCaseǁexecute__mutmut['xǁCertsStatusExplainUseCaseǁexecute__mutmut_18'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁCertsStatusExplainUseCaseǁexecute__mutmut['xǁCertsStatusExplainUseCaseǁexecute__mutmut_19'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
