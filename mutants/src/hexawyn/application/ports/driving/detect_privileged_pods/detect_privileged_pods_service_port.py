from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.security.detect_privileged_pods.command import (
    DetectPrivilegedPodsCommand,
)
from hexawyn.application.use_case.security.detect_privileged_pods.response import (
    DetectPrivilegedPodsResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class DetectPrivilegedPodsServicePort(ABC):
    @abstractmethod
    def audit_pod_security(
        self, command: DetectPrivilegedPodsCommand
    ) -> DetectPrivilegedPodsResponse: ...
