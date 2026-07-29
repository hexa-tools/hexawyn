from __future__ import annotations

from hexawyn.adapters.secondary.gitops.otel_http_client import search_jaeger_traces
from hexawyn.application.ports.driven.slo_breach_prediction_port import (
    SLOBreachPredictionPort,
)
from hexawyn.domain.models.slo_breach_prediction import SLOBreachPredictionRequest


class OTelSLOPredictionAdapter(SLOBreachPredictionPort):
    def fetch_trend_metrics(self, request: SLOBreachPredictionRequest) -> list[dict[str, object]]:
        traces = search_jaeger_traces(
            service="",
            limit=50,
        )
        result: list[dict[str, object]] = []
        for trace in traces:
            result.append(
                {
                    "trace_id": trace["traceID"],
                    "duration_ms": float(trace.get("duration", 0)) / 1000.0,
                    "has_errors": bool(trace.get("hasErrors")),
                }
            )
        return result
