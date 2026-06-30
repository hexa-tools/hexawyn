from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.detect_over_provisioned_namespaces.detect_over_provisioned_namespaces_command import (
    DetectOverProvisionedNamespacesCommand,
)
from hexawyn.application.ports.driving.detect_over_provisioned_namespaces.detect_over_provisioned_namespaces_response import (
    DetectOverProvisionedNamespacesResponse,
)


class DetectOverProvisionedNamespacesServicePort(ABC):
    @abstractmethod
    def detect_over_provisioned_namespaces(
        self, command: DetectOverProvisionedNamespacesCommand
    ) -> DetectOverProvisionedNamespacesResponse: ...
