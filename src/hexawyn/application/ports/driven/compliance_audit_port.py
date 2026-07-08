from abc import ABC, abstractmethod

from hexawyn.domain.models.sensitive_data_audit import AccessMatch, SensitiveAccessRequest


class ComplianceAuditPort(ABC):
    @abstractmethod
    def fetch_access_matches(self, request: SensitiveAccessRequest) -> list[AccessMatch]: ...
