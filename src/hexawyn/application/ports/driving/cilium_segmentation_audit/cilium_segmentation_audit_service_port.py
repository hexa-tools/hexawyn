from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cilium.cilium_segmentation_audit.command import (
    CiliumSegmentationAuditCommand,
)
from hexawyn.application.use_case.cilium.cilium_segmentation_audit.response import (
    CiliumSegmentationAuditResponse,
)


class CiliumSegmentationAuditServicePort(ABC):
    @abstractmethod
    def audit(self, command: CiliumSegmentationAuditCommand) -> CiliumSegmentationAuditResponse: ...
