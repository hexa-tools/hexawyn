from __future__ import annotations

from hexawyn.application.ports.driven.trace_log_correlation_port import TraceLogCorrelationPort
from hexawyn.domain.models.trace_log_correlation import (
    CorrelatedLog,
    TraceLogCorrelationRequest,
    TraceLogSpan,
)


class OTelTraceLogAdapter(TraceLogCorrelationPort):
    def fetch_error_spans(self, request: TraceLogCorrelationRequest) -> list[TraceLogSpan]:
        return []

    def fetch_correlated_logs(self, trace_id: str) -> list[CorrelatedLog]:
        return []
