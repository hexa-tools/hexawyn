from dataclasses import dataclass

from hexawyn.domain.models.tls_compliance import TLSComplianceReport


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class AuditTlsComplianceResponse:
    result: TLSComplianceReport
