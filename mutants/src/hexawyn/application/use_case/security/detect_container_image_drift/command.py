from __future__ import annotations

from dataclasses import dataclass, field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class DetectContainerImageDriftCommand:
    namespace: str
    kustomize_paths: list[str] = field(default_factory=list)
