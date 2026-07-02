from __future__ import annotations

from hexawyn.application.ports.driven.redundant_call_detection_port import (
    RedundantCallDetectionPort,
)
from hexawyn.domain.models.redundant_calls import RedundantCallRequest, SpanInfo


class OTelRedundantCallAdapter(RedundantCallDetectionPort):
    def fetch_spans(self, request: RedundantCallRequest) -> list[SpanInfo]:
        return []
