from __future__ import annotations

from hexawyn.application.ports.driving.detect_over_provisioned_namespaces.detect_over_provisioned_namespaces_command import (
    DetectOverProvisionedNamespacesCommand,
)
from hexawyn.application.ports.driving.detect_over_provisioned_namespaces.detect_over_provisioned_namespaces_response import (
    DetectOverProvisionedNamespacesResponse,
)
from hexawyn.application.ports.driving.detect_over_provisioned_namespaces.detect_over_provisioned_namespaces_service_port import (
    DetectOverProvisionedNamespacesServicePort,
)


class DetectOverProvisionedNamespacesUseCase:
    """Entry point — depends only on the service port abstraction."""

    def __init__(self, service: DetectOverProvisionedNamespacesServicePort) -> None:
        self._service = service

    def execute(
        self, command: DetectOverProvisionedNamespacesCommand
    ) -> DetectOverProvisionedNamespacesResponse:
        return self._service.detect_over_provisioned_namespaces(command)
