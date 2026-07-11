from abc import ABC, abstractmethod
from typing import TypedDict


class UnauthorizedAccessRaw(TypedDict):
    attempt_count: int
    window_minutes: int
    source_type: str


class UnauthorizedAccessPort(ABC):
    @abstractmethod
    def get_unauthorized_access_data(self) -> UnauthorizedAccessRaw: ...
