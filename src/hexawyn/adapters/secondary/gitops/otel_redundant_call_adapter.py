from __future__ import annotations

from hexawyn.adapters.secondary.gitops.otel_http_client import search_jaeger_traces
from hexawyn.application.ports.driven.redundant_call_detection_port import (
    RedundantCallDetectionPort,
)
from hexawyn.domain.models.redundant_calls import RedundantCallRequest, SpanInfo


class OTelRedundantCallAdapter(RedundantCallDetectionPort):
    def fetch_spans(self, request: RedundantCallRequest) -> list[SpanInfo]:
        traces = search_jaeger_traces(
            service="",
            limit=20,
        )
        result: list[SpanInfo] = []
        for trace in traces:
            result.append(
                SpanInfo(
                    span_name=f"trace:{trace['traceID'][:8]}",
                    service_name="",
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                )
            )
        return result
