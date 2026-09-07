from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.calico.calico_segmentation_audit.command import (
    CalicoSegmentationAuditCommand,
)
from hexawyn.application.use_case.calico.calico_segmentation_audit.response import (
    CalicoSegmentationAuditResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class CalicoSegmentationAuditServicePort(ABC):
    """Inbound port for the Calico segmentation matrix audit."""

    @abstractmethod
    def audit(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse: ...
