from __future__ import annotations

from dataclasses import dataclass
from typing import TypedDict


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class CiliumIdentityOutput(TypedDict):
    id: str
    labels: list[str]
    endpoint_count: int


@dataclass
class ListCiliumIdentitiesResponse:
    installed: bool = False
    status: str = "not_installed"
    total_identities: int = 0
    identities: list[CiliumIdentityOutput] | None = None
    note: str | None = None
    error: str | None = None
