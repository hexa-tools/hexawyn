from abc import ABC, abstractmethod

from hexawyn.domain.models.span_bottleneck import BottleneckRequest, SpanBreakdown


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class SpanBottleneckPort(ABC):
    @abstractmethod
    def fetch_db_spans(self, request: BottleneckRequest) -> SpanBreakdown: ...
    @abstractmethod
    def fetch_redis_spans(self, request: BottleneckRequest) -> SpanBreakdown | None: ...
