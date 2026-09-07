from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class DetectOverProvisionedNamespacesResponse:
    report: object = None
    prometheus_available: bool = False
    error: str | None = None
