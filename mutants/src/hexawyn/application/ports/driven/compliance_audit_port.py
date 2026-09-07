from abc import ABC, abstractmethod

from hexawyn.domain.models.sensitive_data_audit import AccessMatch, SensitiveAccessRequest


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ComplianceAuditPort(ABC):
    @abstractmethod
    def fetch_access_matches(self, request: SensitiveAccessRequest) -> list[AccessMatch]: ...
