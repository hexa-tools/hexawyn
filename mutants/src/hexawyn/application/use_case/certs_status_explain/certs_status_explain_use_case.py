# mypy: ignore-errors
from __future__ import annotations

from hexawyn.application.ports.driven.cert_manager_port import CertManagerPort
from hexawyn.application.use_case.certs_status_explain.command import (
    CertsStatusExplainCommand,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCertsStatusExplainUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁCertsStatusExplainUseCaseǁexplain__mutmut: MutantDict = {}  # type: ignore


class CertsStatusExplainUseCase:
    @_mutmut_mutated(mutants_xǁCertsStatusExplainUseCaseǁ__init____mutmut)
    def __init__(self, port: CertManagerPort) -> None:
        self._port = port
    def xǁCertsStatusExplainUseCaseǁ__init____mutmut_orig(self, port: CertManagerPort) -> None:
        self._port = port
    def xǁCertsStatusExplainUseCaseǁ__init____mutmut_1(self, port: CertManagerPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁCertsStatusExplainUseCaseǁexplain__mutmut)
    def explain(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:  # noqa: F821  # type: ignore
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsStatusExplainResponse(  # noqa: F821  # type: ignore
            status=c.status.value,
            message=c.message,
            explanation=f"Certificate '{command.name}' is in status '{c.status.value}'.",
            fix_suggestion="Check the certificate message for details."
            if c.message
            else "No issues detected.",
        )

    def xǁCertsStatusExplainUseCaseǁexplain__mutmut_orig(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:  # noqa: F821  # type: ignore
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsStatusExplainResponse(  # noqa: F821  # type: ignore
            status=c.status.value,
            message=c.message,
            explanation=f"Certificate '{command.name}' is in status '{c.status.value}'.",
            fix_suggestion="Check the certificate message for details."
            if c.message
            else "No issues detected.",
        )

    def xǁCertsStatusExplainUseCaseǁexplain__mutmut_1(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:  # noqa: F821  # type: ignore
        c = None
        return CertsStatusExplainResponse(  # noqa: F821  # type: ignore
            status=c.status.value,
            message=c.message,
            explanation=f"Certificate '{command.name}' is in status '{c.status.value}'.",
            fix_suggestion="Check the certificate message for details."
            if c.message
            else "No issues detected.",
        )

    def xǁCertsStatusExplainUseCaseǁexplain__mutmut_2(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:  # noqa: F821  # type: ignore
        c = self._port.get_certificate(name=None, namespace=command.namespace)
        return CertsStatusExplainResponse(  # noqa: F821  # type: ignore
            status=c.status.value,
            message=c.message,
            explanation=f"Certificate '{command.name}' is in status '{c.status.value}'.",
            fix_suggestion="Check the certificate message for details."
            if c.message
            else "No issues detected.",
        )

    def xǁCertsStatusExplainUseCaseǁexplain__mutmut_3(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:  # noqa: F821  # type: ignore
        c = self._port.get_certificate(name=command.name, namespace=None)
        return CertsStatusExplainResponse(  # noqa: F821  # type: ignore
            status=c.status.value,
            message=c.message,
            explanation=f"Certificate '{command.name}' is in status '{c.status.value}'.",
            fix_suggestion="Check the certificate message for details."
            if c.message
            else "No issues detected.",
        )

    def xǁCertsStatusExplainUseCaseǁexplain__mutmut_4(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:  # noqa: F821  # type: ignore
        c = self._port.get_certificate(namespace=command.namespace)
        return CertsStatusExplainResponse(  # noqa: F821  # type: ignore
            status=c.status.value,
            message=c.message,
            explanation=f"Certificate '{command.name}' is in status '{c.status.value}'.",
            fix_suggestion="Check the certificate message for details."
            if c.message
            else "No issues detected.",
        )

    def xǁCertsStatusExplainUseCaseǁexplain__mutmut_5(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:  # noqa: F821  # type: ignore
        c = self._port.get_certificate(name=command.name, )
        return CertsStatusExplainResponse(  # noqa: F821  # type: ignore
            status=c.status.value,
            message=c.message,
            explanation=f"Certificate '{command.name}' is in status '{c.status.value}'.",
            fix_suggestion="Check the certificate message for details."
            if c.message
            else "No issues detected.",
        )

    def xǁCertsStatusExplainUseCaseǁexplain__mutmut_6(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:  # noqa: F821  # type: ignore
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsStatusExplainResponse(  # noqa: F821  # type: ignore
            status=None,
            message=c.message,
            explanation=f"Certificate '{command.name}' is in status '{c.status.value}'.",
            fix_suggestion="Check the certificate message for details."
            if c.message
            else "No issues detected.",
        )

    def xǁCertsStatusExplainUseCaseǁexplain__mutmut_7(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:  # noqa: F821  # type: ignore
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsStatusExplainResponse(  # noqa: F821  # type: ignore
            status=c.status.value,
            message=None,
            explanation=f"Certificate '{command.name}' is in status '{c.status.value}'.",
            fix_suggestion="Check the certificate message for details."
            if c.message
            else "No issues detected.",
        )

    def xǁCertsStatusExplainUseCaseǁexplain__mutmut_8(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:  # noqa: F821  # type: ignore
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsStatusExplainResponse(  # noqa: F821  # type: ignore
            status=c.status.value,
            message=c.message,
            explanation=None,
            fix_suggestion="Check the certificate message for details."
            if c.message
            else "No issues detected.",
        )

    def xǁCertsStatusExplainUseCaseǁexplain__mutmut_9(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:  # noqa: F821  # type: ignore
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsStatusExplainResponse(  # noqa: F821  # type: ignore
            status=c.status.value,
            message=c.message,
            explanation=f"Certificate '{command.name}' is in status '{c.status.value}'.",
            fix_suggestion=None,
        )

    def xǁCertsStatusExplainUseCaseǁexplain__mutmut_10(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:  # noqa: F821  # type: ignore
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsStatusExplainResponse(  # noqa: F821  # type: ignore
            message=c.message,
            explanation=f"Certificate '{command.name}' is in status '{c.status.value}'.",
            fix_suggestion="Check the certificate message for details."
            if c.message
            else "No issues detected.",
        )

    def xǁCertsStatusExplainUseCaseǁexplain__mutmut_11(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:  # noqa: F821  # type: ignore
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsStatusExplainResponse(  # noqa: F821  # type: ignore
            status=c.status.value,
            explanation=f"Certificate '{command.name}' is in status '{c.status.value}'.",
            fix_suggestion="Check the certificate message for details."
            if c.message
            else "No issues detected.",
        )

    def xǁCertsStatusExplainUseCaseǁexplain__mutmut_12(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:  # noqa: F821  # type: ignore
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsStatusExplainResponse(  # noqa: F821  # type: ignore
            status=c.status.value,
            message=c.message,
            fix_suggestion="Check the certificate message for details."
            if c.message
            else "No issues detected.",
        )

    def xǁCertsStatusExplainUseCaseǁexplain__mutmut_13(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:  # noqa: F821  # type: ignore
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsStatusExplainResponse(  # noqa: F821  # type: ignore
            status=c.status.value,
            message=c.message,
            explanation=f"Certificate '{command.name}' is in status '{c.status.value}'.",
            )

    def xǁCertsStatusExplainUseCaseǁexplain__mutmut_14(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:  # noqa: F821  # type: ignore
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsStatusExplainResponse(  # noqa: F821  # type: ignore
            status=c.status.value,
            message=c.message,
            explanation=f"Certificate '{command.name}' is in status '{c.status.value}'.",
            fix_suggestion="XXCheck the certificate message for details.XX"
            if c.message
            else "No issues detected.",
        )

    def xǁCertsStatusExplainUseCaseǁexplain__mutmut_15(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:  # noqa: F821  # type: ignore
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsStatusExplainResponse(  # noqa: F821  # type: ignore
            status=c.status.value,
            message=c.message,
            explanation=f"Certificate '{command.name}' is in status '{c.status.value}'.",
            fix_suggestion="check the certificate message for details."
            if c.message
            else "No issues detected.",
        )

    def xǁCertsStatusExplainUseCaseǁexplain__mutmut_16(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:  # noqa: F821  # type: ignore
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsStatusExplainResponse(  # noqa: F821  # type: ignore
            status=c.status.value,
            message=c.message,
            explanation=f"Certificate '{command.name}' is in status '{c.status.value}'.",
            fix_suggestion="CHECK THE CERTIFICATE MESSAGE FOR DETAILS."
            if c.message
            else "No issues detected.",
        )

    def xǁCertsStatusExplainUseCaseǁexplain__mutmut_17(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:  # noqa: F821  # type: ignore
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsStatusExplainResponse(  # noqa: F821  # type: ignore
            status=c.status.value,
            message=c.message,
            explanation=f"Certificate '{command.name}' is in status '{c.status.value}'.",
            fix_suggestion="Check the certificate message for details."
            if c.message
            else "XXNo issues detected.XX",
        )

    def xǁCertsStatusExplainUseCaseǁexplain__mutmut_18(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:  # noqa: F821  # type: ignore
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsStatusExplainResponse(  # noqa: F821  # type: ignore
            status=c.status.value,
            message=c.message,
            explanation=f"Certificate '{command.name}' is in status '{c.status.value}'.",
            fix_suggestion="Check the certificate message for details."
            if c.message
            else "no issues detected.",
        )

    def xǁCertsStatusExplainUseCaseǁexplain__mutmut_19(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse:  # noqa: F821  # type: ignore
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsStatusExplainResponse(  # noqa: F821  # type: ignore
            status=c.status.value,
            message=c.message,
            explanation=f"Certificate '{command.name}' is in status '{c.status.value}'.",
            fix_suggestion="Check the certificate message for details."
            if c.message
            else "NO ISSUES DETECTED.",
        )

mutants_xǁCertsStatusExplainUseCaseǁ__init____mutmut['_mutmut_orig'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCertsStatusExplainUseCaseǁ__init____mutmut['xǁCertsStatusExplainUseCaseǁ__init____mutmut_1'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁCertsStatusExplainUseCaseǁexplain__mutmut['_mutmut_orig'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁexplain__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCertsStatusExplainUseCaseǁexplain__mutmut['xǁCertsStatusExplainUseCaseǁexplain__mutmut_1'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁexplain__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCertsStatusExplainUseCaseǁexplain__mutmut['xǁCertsStatusExplainUseCaseǁexplain__mutmut_2'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁexplain__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCertsStatusExplainUseCaseǁexplain__mutmut['xǁCertsStatusExplainUseCaseǁexplain__mutmut_3'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁexplain__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCertsStatusExplainUseCaseǁexplain__mutmut['xǁCertsStatusExplainUseCaseǁexplain__mutmut_4'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁexplain__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCertsStatusExplainUseCaseǁexplain__mutmut['xǁCertsStatusExplainUseCaseǁexplain__mutmut_5'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁexplain__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCertsStatusExplainUseCaseǁexplain__mutmut['xǁCertsStatusExplainUseCaseǁexplain__mutmut_6'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁexplain__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCertsStatusExplainUseCaseǁexplain__mutmut['xǁCertsStatusExplainUseCaseǁexplain__mutmut_7'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁexplain__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCertsStatusExplainUseCaseǁexplain__mutmut['xǁCertsStatusExplainUseCaseǁexplain__mutmut_8'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁexplain__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCertsStatusExplainUseCaseǁexplain__mutmut['xǁCertsStatusExplainUseCaseǁexplain__mutmut_9'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁexplain__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCertsStatusExplainUseCaseǁexplain__mutmut['xǁCertsStatusExplainUseCaseǁexplain__mutmut_10'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁexplain__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCertsStatusExplainUseCaseǁexplain__mutmut['xǁCertsStatusExplainUseCaseǁexplain__mutmut_11'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁexplain__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCertsStatusExplainUseCaseǁexplain__mutmut['xǁCertsStatusExplainUseCaseǁexplain__mutmut_12'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁexplain__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCertsStatusExplainUseCaseǁexplain__mutmut['xǁCertsStatusExplainUseCaseǁexplain__mutmut_13'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁexplain__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCertsStatusExplainUseCaseǁexplain__mutmut['xǁCertsStatusExplainUseCaseǁexplain__mutmut_14'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁexplain__mutmut_14 # type: ignore # mutmut generated
mutants_xǁCertsStatusExplainUseCaseǁexplain__mutmut['xǁCertsStatusExplainUseCaseǁexplain__mutmut_15'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁexplain__mutmut_15 # type: ignore # mutmut generated
mutants_xǁCertsStatusExplainUseCaseǁexplain__mutmut['xǁCertsStatusExplainUseCaseǁexplain__mutmut_16'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁexplain__mutmut_16 # type: ignore # mutmut generated
mutants_xǁCertsStatusExplainUseCaseǁexplain__mutmut['xǁCertsStatusExplainUseCaseǁexplain__mutmut_17'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁexplain__mutmut_17 # type: ignore # mutmut generated
mutants_xǁCertsStatusExplainUseCaseǁexplain__mutmut['xǁCertsStatusExplainUseCaseǁexplain__mutmut_18'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁexplain__mutmut_18 # type: ignore # mutmut generated
mutants_xǁCertsStatusExplainUseCaseǁexplain__mutmut['xǁCertsStatusExplainUseCaseǁexplain__mutmut_19'] = CertsStatusExplainUseCase.xǁCertsStatusExplainUseCaseǁexplain__mutmut_19 # type: ignore # mutmut generated
