from abc import ABC, abstractmethod

from hexawyn.domain.models.span_bottleneck import BottleneckRequest, SpanBreakdown


class SpanBottleneckPort(ABC):
    @abstractmethod
    def fetch_db_spans(self, request: BottleneckRequest) -> SpanBreakdown: ...
    @abstractmethod
    def fetch_redis_spans(self, request: BottleneckRequest) -> SpanBreakdown | None: ...
