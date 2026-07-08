from abc import ABC, abstractmethod

from hexawyn.domain.models.redundant_calls import RedundantCallRequest, SpanInfo


class RedundantCallDetectionPort(ABC):
    @abstractmethod
    def fetch_spans(self, request: RedundantCallRequest) -> list[SpanInfo]: ...
