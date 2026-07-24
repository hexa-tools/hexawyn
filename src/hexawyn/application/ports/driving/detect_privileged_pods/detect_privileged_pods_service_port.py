from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.detect_privileged_pods.command import (
    DetectPrivilegedPodsCommand,
)
from hexawyn.application.use_case.detect_privileged_pods.response import (
    DetectPrivilegedPodsResponse,
)


class DetectPrivilegedPodsServicePort(ABC):
    @abstractmethod
    def audit_pod_security(
        self, command: DetectPrivilegedPodsCommand
    ) -> DetectPrivilegedPodsResponse: ...
