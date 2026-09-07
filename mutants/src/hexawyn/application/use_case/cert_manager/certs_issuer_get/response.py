from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class CertsIssuerGetResponse:
    name: str = ""
    namespace: str | None = None
    kind: str = ""
    issuer_type: str = "unknown"
    ready: bool = False
    server: str | None = None
    message: str | None = None
    error: str | None = None
