from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.admin_endpoint_audit.admin_endpoint_audit_command import (
    AdminEndpointAuditCommand,
)
from hexawyn.application.ports.driving.admin_endpoint_audit.admin_endpoint_audit_response import (
    AdminEndpointAuditResponse,
)


class AdminEndpointAuditServicePort(ABC):
    @abstractmethod
    def audit(self, command: AdminEndpointAuditCommand) -> AdminEndpointAuditResponse: ...
