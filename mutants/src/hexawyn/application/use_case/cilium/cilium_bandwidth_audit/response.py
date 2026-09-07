from __future__ import annotations

from dataclasses import dataclass
from typing import TypedDict


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class CiliumBandwidthEntryOutput(TypedDict):
    namespace: str
    pod: str
    ingress_limit: str | None
    egress_limit: str | None
    usage_ratio: float | None
    state: str
    note: str | None


@dataclass
class CiliumBandwidthAuditResponse:
    installed: bool = False
    status: str = "not_installed"
    total_pods: int = 0
    entries: list[CiliumBandwidthEntryOutput] | None = None
    note: str | None = None
    error: str | None = None
