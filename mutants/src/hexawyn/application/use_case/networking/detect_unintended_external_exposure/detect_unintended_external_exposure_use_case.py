from hexawyn.application.ports.driven.external_exposure_audit_port import ExternalExposureAuditPort
from hexawyn.application.use_case.networking.detect_unintended_external_exposure.command import (
    DetectUnintendedExternalExposureCommand,
)
from hexawyn.application.use_case.networking.detect_unintended_external_exposure.response import (
    DetectUnintendedExternalExposureResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁDetectUnintendedExternalExposureUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDetectUnintendedExternalExposureUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class DetectUnintendedExternalExposureUseCase:
    @_mutmut_mutated(mutants_xǁDetectUnintendedExternalExposureUseCaseǁ__init____mutmut)
    def __init__(self, port: ExternalExposureAuditPort) -> None:
        self._port = port
    def xǁDetectUnintendedExternalExposureUseCaseǁ__init____mutmut_orig(self, port: ExternalExposureAuditPort) -> None:
        self._port = port
    def xǁDetectUnintendedExternalExposureUseCaseǁ__init____mutmut_1(self, port: ExternalExposureAuditPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁDetectUnintendedExternalExposureUseCaseǁexecute__mutmut)
    def execute(
        self, command: DetectUnintendedExternalExposureCommand
    ) -> DetectUnintendedExternalExposureResponse:
        services = self._port.list_external_services()
        return DetectUnintendedExternalExposureResponse(
            total_external_services_checked=len(services),
            findings=services,  # type: ignore
        )

    def xǁDetectUnintendedExternalExposureUseCaseǁexecute__mutmut_orig(
        self, command: DetectUnintendedExternalExposureCommand
    ) -> DetectUnintendedExternalExposureResponse:
        services = self._port.list_external_services()
        return DetectUnintendedExternalExposureResponse(
            total_external_services_checked=len(services),
            findings=services,  # type: ignore
        )

    def xǁDetectUnintendedExternalExposureUseCaseǁexecute__mutmut_1(
        self, command: DetectUnintendedExternalExposureCommand
    ) -> DetectUnintendedExternalExposureResponse:
        services = None
        return DetectUnintendedExternalExposureResponse(
            total_external_services_checked=len(services),
            findings=services,  # type: ignore
        )

    def xǁDetectUnintendedExternalExposureUseCaseǁexecute__mutmut_2(
        self, command: DetectUnintendedExternalExposureCommand
    ) -> DetectUnintendedExternalExposureResponse:
        services = self._port.list_external_services()
        return DetectUnintendedExternalExposureResponse(
            total_external_services_checked=None,
            findings=services,  # type: ignore
        )

    def xǁDetectUnintendedExternalExposureUseCaseǁexecute__mutmut_3(
        self, command: DetectUnintendedExternalExposureCommand
    ) -> DetectUnintendedExternalExposureResponse:
        services = self._port.list_external_services()
        return DetectUnintendedExternalExposureResponse(
            total_external_services_checked=len(services),
            findings=None,  # type: ignore
        )

    def xǁDetectUnintendedExternalExposureUseCaseǁexecute__mutmut_4(
        self, command: DetectUnintendedExternalExposureCommand
    ) -> DetectUnintendedExternalExposureResponse:
        services = self._port.list_external_services()
        return DetectUnintendedExternalExposureResponse(
            findings=services,  # type: ignore
        )

    def xǁDetectUnintendedExternalExposureUseCaseǁexecute__mutmut_5(
        self, command: DetectUnintendedExternalExposureCommand
    ) -> DetectUnintendedExternalExposureResponse:
        services = self._port.list_external_services()
        return DetectUnintendedExternalExposureResponse(
            total_external_services_checked=len(services),
            )

mutants_xǁDetectUnintendedExternalExposureUseCaseǁ__init____mutmut['_mutmut_orig'] = DetectUnintendedExternalExposureUseCase.xǁDetectUnintendedExternalExposureUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDetectUnintendedExternalExposureUseCaseǁ__init____mutmut['xǁDetectUnintendedExternalExposureUseCaseǁ__init____mutmut_1'] = DetectUnintendedExternalExposureUseCase.xǁDetectUnintendedExternalExposureUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁDetectUnintendedExternalExposureUseCaseǁexecute__mutmut['_mutmut_orig'] = DetectUnintendedExternalExposureUseCase.xǁDetectUnintendedExternalExposureUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDetectUnintendedExternalExposureUseCaseǁexecute__mutmut['xǁDetectUnintendedExternalExposureUseCaseǁexecute__mutmut_1'] = DetectUnintendedExternalExposureUseCase.xǁDetectUnintendedExternalExposureUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDetectUnintendedExternalExposureUseCaseǁexecute__mutmut['xǁDetectUnintendedExternalExposureUseCaseǁexecute__mutmut_2'] = DetectUnintendedExternalExposureUseCase.xǁDetectUnintendedExternalExposureUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDetectUnintendedExternalExposureUseCaseǁexecute__mutmut['xǁDetectUnintendedExternalExposureUseCaseǁexecute__mutmut_3'] = DetectUnintendedExternalExposureUseCase.xǁDetectUnintendedExternalExposureUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDetectUnintendedExternalExposureUseCaseǁexecute__mutmut['xǁDetectUnintendedExternalExposureUseCaseǁexecute__mutmut_4'] = DetectUnintendedExternalExposureUseCase.xǁDetectUnintendedExternalExposureUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDetectUnintendedExternalExposureUseCaseǁexecute__mutmut['xǁDetectUnintendedExternalExposureUseCaseǁexecute__mutmut_5'] = DetectUnintendedExternalExposureUseCase.xǁDetectUnintendedExternalExposureUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
