from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.security.admin_endpoint_audit.command import (
    AdminEndpointAuditCommand,
)
from hexawyn.application.use_case.security.admin_endpoint_audit.response import (
    AdminEndpointAuditResponse,
)


class AdminEndpointAuditServicePort(ABC):
    @abstractmethod
    def audit(self, command: AdminEndpointAuditCommand) -> AdminEndpointAuditResponse: ...
