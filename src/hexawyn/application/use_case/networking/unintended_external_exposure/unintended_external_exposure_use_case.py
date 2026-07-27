from __future__ import annotations

from hexawyn.application.ports.driven.external_exposure_audit_port import (
    ExternalExposureAuditPort,
)
from hexawyn.application.use_case.networking.unintended_external_exposure.command import (
    UnintendedExternalExposureCommand,
)
from hexawyn.application.use_case.networking.unintended_external_exposure.response import (
    UnintendedExternalExposureResponse,
)


class UnintendedExternalExposureUseCase:
    def __init__(self, port: ExternalExposureAuditPort) -> None:
        self._port = port

    def execute(
        self,
        command: UnintendedExternalExposureCommand,
    ) -> UnintendedExternalExposureResponse:
        services = self._port.audit_external_exposure(  # type: ignore
            namespace=command.namespace,
        )
        return UnintendedExternalExposureResponse(
            namespace=command.namespace or "",
            total_services=len(services),
            findings=[],
        )
