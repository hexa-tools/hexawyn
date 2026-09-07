from __future__ import annotations

from dataclasses import dataclass, field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class GetCalicoHostEndpointsResponse:
    installed: bool = False
    not_installed_marker: str | None = None
    total: int = 0
    endpoints: list[object] = field(default_factory=list)
    error: str | None = None
