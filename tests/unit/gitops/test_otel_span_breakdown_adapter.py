from __future__ import annotations

from unittest.mock import patch

from hexawyn.adapters.secondary.gitops.otel_http_client import PrometheusMetricDict


def _metric(value: float, labels: dict[str, str] | None = None) -> list[PrometheusMetricDict]:
    return [{"name": "", "value": value, "labels": labels or {}}]


def _fake_db_query(query: str) -> list[PrometheusMetricDict]:
    if query.startswith("histogram_quantile(0.95"):
        return _metric(0.05)
    if query.startswith("histogram_quantile(1.0"):
        return _metric(0.12)
    if query.startswith("topk"):
        return _metric(0.08, {"db_operation": "SELECT users"})
    if query.startswith("rate(db_client_duration_seconds_count"):
        return _metric(42.0)
    return _metric(0.08)


class TestOtelSpanBreakdownAdapterUnit:
    def test_returns_breakdown(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_span_breakdown_adapter import (
            OTelSpanBreakdownAdapter,
        )
        from hexawyn.domain.models.span_bottleneck import BottleneckRequest

        adapter = OTelSpanBreakdownAdapter()
        result = adapter.fetch_db_spans(BottleneckRequest())
        assert result.category == "db"

    def test_fetch_redis_spans_returns_none(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_span_breakdown_adapter import (
            OTelSpanBreakdownAdapter,
        )
        from hexawyn.domain.models.span_bottleneck import BottleneckRequest

        adapter = OTelSpanBreakdownAdapter()
        result = adapter.fetch_redis_spans(BottleneckRequest())
        assert result is None

    def test_fetch_db_spans_parses_real_metrics(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_span_breakdown_adapter import (
            OTelSpanBreakdownAdapter,
        )
        from hexawyn.domain.models.span_bottleneck import BottleneckRequest

        with patch(
            "hexawyn.adapters.secondary.gitops.otel_span_breakdown_adapter"
            ".query_prometheus_instant",
            side_effect=_fake_db_query,
        ):
            adapter = OTelSpanBreakdownAdapter()
            result = adapter.fetch_db_spans(BottleneckRequest())

        assert result.category == "db"
        assert result.avg_ms == 80.0  # noqa: PLR2004
        assert result.p95_ms == 50.0  # noqa: PLR2004
        assert result.max_ms == 120.0  # noqa: PLR2004
        assert result.slowest_operation == "SELECT users"

    def test_fetch_redis_spans_returns_data_when_present(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_span_breakdown_adapter import (
            OTelSpanBreakdownAdapter,
        )
        from hexawyn.domain.models.span_bottleneck import BottleneckRequest

        with patch(
            "hexawyn.adapters.secondary.gitops.otel_span_breakdown_adapter"
            ".query_prometheus_instant",
            side_effect=_fake_db_query,
        ):
            adapter = OTelSpanBreakdownAdapter()
            result = adapter.fetch_redis_spans(BottleneckRequest())

        assert result is not None
        assert result.category == "redis"
        assert result.avg_ms == 80.0  # noqa: PLR2004

    def test_fetch_db_spans_exception_returns_zeros(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_span_breakdown_adapter import (
            OTelSpanBreakdownAdapter,
        )
        from hexawyn.domain.models.span_bottleneck import BottleneckRequest

        with patch(
            "hexawyn.adapters.secondary.gitops.otel_span_breakdown_adapter"
            ".query_prometheus_instant",
            side_effect=RuntimeError("prometheus unreachable"),
        ):
            adapter = OTelSpanBreakdownAdapter()
            result = adapter.fetch_db_spans(BottleneckRequest())

        assert result.avg_ms == 0.0
        assert result.p95_ms == 0.0
        assert result.max_ms == 0.0
        assert result.slowest_operation is None

    def test_max_ms_falls_back_when_infinite(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_span_breakdown_adapter import (
            OTelSpanBreakdownAdapter,
        )
        from hexawyn.domain.models.span_bottleneck import BottleneckRequest

        def fake_query(query: str) -> list[PrometheusMetricDict]:
            if query.startswith("histogram_quantile(0.95"):
                return _metric(0.05)
            if query.startswith("histogram_quantile(1.0"):
                return _metric(float("inf"))
            if query.startswith("topk"):
                return []
            if query.startswith("rate(db_client_duration_seconds_count"):
                return _metric(10.0)
            return _metric(0.06)

        with patch(
            "hexawyn.adapters.secondary.gitops.otel_span_breakdown_adapter"
            ".query_prometheus_instant",
            side_effect=fake_query,
        ):
            adapter = OTelSpanBreakdownAdapter()
            result = adapter.fetch_db_spans(BottleneckRequest())

        assert result.max_ms == result.p95_ms
        assert result.max_ms == 50.0  # noqa: PLR2004
