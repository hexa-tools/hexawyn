from abc import ABC, abstractmethod

from hexawyn.domain.models.redundant_calls import RedundantCallRequest, SpanInfo


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class RedundantCallDetectionPort(ABC):
    @abstractmethod
    def fetch_spans(self, request: RedundantCallRequest) -> list[SpanInfo]: ...
