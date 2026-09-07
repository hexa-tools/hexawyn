from __future__ import annotations

from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class DetectCiliumDenialsCommand:
    namespace: str | None = None
    window_minutes: int = 5
    limit: int = 100
