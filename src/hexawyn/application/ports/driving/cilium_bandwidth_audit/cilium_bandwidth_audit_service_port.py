from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cilium.cilium_bandwidth_audit.command import (
    CiliumBandwidthAuditCommand,
)
from hexawyn.application.use_case.cilium.cilium_bandwidth_audit.response import (
    CiliumBandwidthAuditResponse,
)


class CiliumBandwidthAuditServicePort(ABC):
    @abstractmethod
    def audit(self, command: CiliumBandwidthAuditCommand) -> CiliumBandwidthAuditResponse: ...
