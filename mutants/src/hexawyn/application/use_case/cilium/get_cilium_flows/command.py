from __future__ import annotations

from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class GetCiliumFlowsCommand:
    namespace: str | None = None
    pod: str | None = None
    direction: str | None = None
    verdict: str | None = None
    window_minutes: int = 15
    limit: int = 100
