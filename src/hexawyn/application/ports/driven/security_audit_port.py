from abc import ABC, abstractmethod

from hexawyn.domain.models.admin_endpoint_audit import AdminAuditRequest, FailedAdminCall


class SecurityAuditPort(ABC):
    @abstractmethod
    def fetch_failed_admin_calls(self, request: AdminAuditRequest) -> list[FailedAdminCall]: ...
    @abstractmethod
    def fetch_total_requests(self, request: AdminAuditRequest) -> int: ...
