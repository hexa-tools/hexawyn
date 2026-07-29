from __future__ import annotations

from hexawyn.adapters.secondary.gitops.otel_http_client import search_jaeger_traces
from hexawyn.application.ports.driven.error_attribution_port import (
    ErrorAttributionPort,
)
from hexawyn.domain.models.error_attribution import ErrorAttributionRequest


class OTelErrorAttributionAdapter(ErrorAttributionPort):
    def fetch_error_attribution(self, request: ErrorAttributionRequest) -> list[dict[str, object]]:
        if not request.gateway:
            return []

        traces = search_jaeger_traces(
            service=request.gateway,
            with_errors=True,
            limit=20,
        )
        result: list[dict[str, object]] = []
        for trace in traces:
            result.append(
                {
                    "trace_id": trace["traceID"],
                    "error": bool(trace.get("hasErrors")),
                    "service": request.gateway,
                }
            )
        return result
