from __future__ import annotations

from dataclasses import dataclass, field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class ListCalicoIpPoolsResponse:
    installed: bool = False
    not_installed_marker: str | None = None
    total: int = 0
    pools: list[object] = field(default_factory=list)
    error: str | None = None
