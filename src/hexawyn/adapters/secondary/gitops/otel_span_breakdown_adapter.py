from __future__ import annotations

import math

from hexawyn.adapters.secondary.gitops.otel_http_client import query_prometheus_instant
from hexawyn.application.ports.driven.span_bottleneck_port import SpanBottleneckPort
from hexawyn.domain.models.span_bottleneck import BottleneckRequest, SpanBreakdown


class OTelSpanBreakdownAdapter(SpanBottleneckPort):
    def fetch_db_spans(self, request: BottleneckRequest) -> SpanBreakdown:
        breakdown, _ = self._fetch_breakdown(
            request, category="db", label_filter='db_system!="redis"'
        )
        return breakdown

    def fetch_redis_spans(self, request: BottleneckRequest) -> SpanBreakdown | None:
        breakdown, sample_count = self._fetch_breakdown(
            request, category="redis", label_filter='db_system="redis"'
        )
        return breakdown if sample_count > 0 else None

    def _fetch_breakdown(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )
