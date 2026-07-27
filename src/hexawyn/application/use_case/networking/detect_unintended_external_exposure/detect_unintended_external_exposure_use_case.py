from hexawyn.application.ports.driven.external_exposure_audit_port import ExternalExposureAuditPort
from hexawyn.application.use_case.networking.detect_unintended_external_exposure.command import (
    DetectUnintendedExternalExposureCommand,
)
from hexawyn.application.use_case.networking.detect_unintended_external_exposure.response import (
    DetectUnintendedExternalExposureResponse,
)


class DetectUnintendedExternalExposureUseCase:
    def __init__(self, port: ExternalExposureAuditPort) -> None:
        self._port = port

    def execute(
        self, command: DetectUnintendedExternalExposureCommand
    ) -> DetectUnintendedExternalExposureResponse:
        services = self._port.list_external_services()
        return DetectUnintendedExternalExposureResponse(
            total_external_services_checked=len(services),
            findings=services,  # type: ignore
        )
