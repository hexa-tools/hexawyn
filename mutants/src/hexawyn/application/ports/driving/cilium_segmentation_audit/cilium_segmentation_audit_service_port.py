from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cilium.cilium_segmentation_audit.command import (
    CiliumSegmentationAuditCommand,
)
from hexawyn.application.use_case.cilium.cilium_segmentation_audit.response import (
    CiliumSegmentationAuditResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class CiliumSegmentationAuditServicePort(ABC):
    @abstractmethod
    def audit(self, command: CiliumSegmentationAuditCommand) -> CiliumSegmentationAuditResponse: ...
