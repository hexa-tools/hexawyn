from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.detect_privileged_pods.detect_privileged_pods_command import (
    DetectPrivilegedPodsCommand,
)
from hexawyn.application.ports.driving.detect_privileged_pods.detect_privileged_pods_response import (
    DetectPrivilegedPodsResponse,
)


class DetectPrivilegedPodsServicePort(ABC):
    @abstractmethod
    def audit_pod_security(
        self, command: DetectPrivilegedPodsCommand
    ) -> DetectPrivilegedPodsResponse: ...
