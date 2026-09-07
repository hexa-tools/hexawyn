from __future__ import annotations

from dataclasses import dataclass, field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class CalicoEncryptionStatusResponse:
    installed: bool = False
    not_installed_marker: str | None = None
    wireguard_enabled: bool | None = None
    mode: str | None = None
    per_node: list[object] = field(default_factory=list)
    summary: str | None = None
    error: str | None = None
