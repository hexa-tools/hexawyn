from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.troubleshooting.adaptive_namespace_investigation.command import (
    AdaptiveNamespaceInvestigationCommand,
)
from hexawyn.application.use_case.troubleshooting.adaptive_namespace_investigation.response import (
    AdaptiveNamespaceInvestigationResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class AdaptiveNamespaceInvestigationServicePort(ABC):
    @abstractmethod
    def investigate(
        self, command: AdaptiveNamespaceInvestigationCommand
    ) -> AdaptiveNamespaceInvestigationResponse: ...
