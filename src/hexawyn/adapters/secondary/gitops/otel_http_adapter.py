from __future__ import annotations

from hexawyn.application.ports.driven.trace_query_port import TraceQueryPort
from hexawyn.domain.models.latency_diagnostic import LatencyDiagnosticRequest, TraceSpan


class OTelHTTPAdapter(TraceQueryPort):
    def fetch_slow_spans(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        return []

    def fetch_total_traces(self, request: LatencyDiagnosticRequest) -> int:
        return 0
