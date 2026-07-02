from abc import ABC, abstractmethod

from hexawyn.domain.models.error_attribution import ErrorAttributionRequest


class ErrorAttributionPort(ABC):
    @abstractmethod
    def fetch_error_attribution(
        self, request: ErrorAttributionRequest
    ) -> list[dict[str, object]]: ...
