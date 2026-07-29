from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.finops.detect_over_provisioned_namespaces.command import (
    DetectOverProvisionedNamespacesCommand,
)
from hexawyn.application.use_case.finops.detect_over_provisioned_namespaces.response import (
    DetectOverProvisionedNamespacesResponse,
)


class DetectOverProvisionedNamespacesServicePort(ABC):
    @abstractmethod
    def detect_over_provisioned_namespaces(
        self, command: DetectOverProvisionedNamespacesCommand
    ) -> DetectOverProvisionedNamespacesResponse: ...
