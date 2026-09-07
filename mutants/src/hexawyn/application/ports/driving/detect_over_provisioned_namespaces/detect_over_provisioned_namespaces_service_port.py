from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.finops.detect_over_provisioned_namespaces.command import (
    DetectOverProvisionedNamespacesCommand,
)
from hexawyn.application.use_case.finops.detect_over_provisioned_namespaces.response import (
    DetectOverProvisionedNamespacesResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class DetectOverProvisionedNamespacesServicePort(ABC):
    @abstractmethod
    def detect_over_provisioned_namespaces(
        self, command: DetectOverProvisionedNamespacesCommand
    ) -> DetectOverProvisionedNamespacesResponse: ...
