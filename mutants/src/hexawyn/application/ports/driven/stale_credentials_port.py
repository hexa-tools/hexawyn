from abc import ABC, abstractmethod
from typing import TypedDict


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class StaleCredentialRaw(TypedDict):
    name: str
    risk_level: str
    days_unrotated: int


class StaleCredentialsPort(ABC):
    @abstractmethod
    def get_stale_credentials(self, min_days: int) -> list[StaleCredentialRaw]: ...
