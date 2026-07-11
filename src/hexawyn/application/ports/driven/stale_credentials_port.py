from abc import ABC, abstractmethod
from typing import TypedDict


class StaleCredentialRaw(TypedDict):
    name: str
    risk_level: str
    days_unrotated: int


class StaleCredentialsPort(ABC):
    @abstractmethod
    def get_stale_credentials(self, min_days: int) -> list[StaleCredentialRaw]: ...
