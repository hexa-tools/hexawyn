from __future__ import annotations

from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class DetectUnintendedExternalExposureCommand:
    namespaces: list[str] | None = None
    allowlist: list[str] | None = None
