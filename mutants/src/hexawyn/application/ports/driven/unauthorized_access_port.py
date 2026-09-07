from abc import ABC, abstractmethod
from typing import TypedDict


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class UnauthorizedAccessRaw(TypedDict):
    attempt_count: int
    window_minutes: int
    source_type: str


class UnauthorizedAccessPort(ABC):
    @abstractmethod
    def get_unauthorized_access_data(self) -> UnauthorizedAccessRaw: ...
