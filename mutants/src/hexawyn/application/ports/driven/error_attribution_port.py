from abc import ABC, abstractmethod

from hexawyn.domain.models.error_attribution import ErrorAttributionRequest


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ErrorAttributionPort(ABC):
    @abstractmethod
    def fetch_error_attribution(
        self, request: ErrorAttributionRequest
    ) -> list[dict[str, object]]: ...
