from __future__ import annotations

from unittest.mock import Mock, patch

import pytest
from hexawyn.adapters.secondary.datadog.datadog_traces_adapter import (
    DatadogTracesAdapter,
    _as_float,
    _translate_error,
)
from hexawyn.application.ports.driven.trace_query_port import TraceQueryPort
from hexawyn.domain.errors import (
    AdapterTimeoutError,
    InsufficientPermissionsError,
    TracesUnavailableError,
)
from hexawyn.domain.models.latency_diagnostic import LatencyDiagnosticRequest


def _span_mock(trace_id: str, operation_name: str, duration: float) -> Mock:
    attrs = Mock()
    attrs.trace_id = trace_id
    attrs.operation_name = operation_name
    attrs.duration = duration
    span = Mock()
    span.id = f"{trace_id}-1"
    span.attributes = attrs
    return span


def _spans_api_mock(spans: list[Mock] | None = None) -> Mock:
    api = Mock()
    response = Mock()
    response.data = spans or []
    api.list_spans.return_value = response
    return api


class TestDatadogTracesAdapter:
    def test_implements_port(self) -> None:
        adapter = DatadogTracesAdapter(spans_api=Mock())
        assert isinstance(adapter, TraceQueryPort)

    # ── fetch_slow_spans ────────────────────────────────────

    def test_fetch_slow_spans_groups_by_trace_id(self) -> None:
        span_a = _span_mock("trace-1", "op-1", 600.0)
        span_b = _span_mock("trace-1", "op-2", 300.0)
        span_c = _span_mock("trace-2", "op-3", 800.0)
        api = _spans_api_mock([span_a, span_b, span_c])

        request = LatencyDiagnosticRequest(
            service_name="payments", time_window_minutes=15, threshold_ms=500.0
        )
        adapter = DatadogTracesAdapter(spans_api=api)
        result = adapter.fetch_slow_spans(request)

        assert len(result) == 2  # noqa: PLR2004
        trace_ids = {spans[0].trace_id for spans in result}
        assert trace_ids == {"trace-1", "trace-2"}

    def test_fetch_slow_spans_sets_trace_span_fields(self) -> None:
        span = _span_mock("trace-abc", "slow-op", 999.0)
        api = _spans_api_mock([span])

        request = LatencyDiagnosticRequest(
            service_name="auth", time_window_minutes=10, threshold_ms=100.0
        )
        adapter = DatadogTracesAdapter(spans_api=api)
        result = adapter.fetch_slow_spans(request)

        assert len(result) == 1
        assert len(result[0]) == 1
        out_span = result[0][0]
        assert out_span.trace_id == "trace-abc"
        assert out_span.span_name == "slow-op"
        assert out_span.duration_ms == 999.0  # noqa: PLR2004

    def test_fetch_slow_spans_empty_returns_empty_list(self) -> None:
        api = _spans_api_mock([])

        request = LatencyDiagnosticRequest(
            service_name="empty-service", time_window_minutes=15, threshold_ms=500.0
        )
        adapter = DatadogTracesAdapter(spans_api=api)
        result = adapter.fetch_slow_spans(request)

        assert result == []

    def test_fetch_slow_spans_handles_non_float_duration(self) -> None:
        span = _span_mock("trace-x", "op-y", 700)  # type: ignore[arg-type]
        span.attributes.duration = "750.5"
        api = _spans_api_mock([span])

        request = LatencyDiagnosticRequest(
            service_name="svc", time_window_minutes=15, threshold_ms=500.0
        )
        adapter = DatadogTracesAdapter(spans_api=api)
        result = adapter.fetch_slow_spans(request)

        assert result[0][0].duration_ms == 750.5  # noqa: PLR2004

    # ── fetch_total_traces ──────────────────────────────────

    def test_fetch_total_traces_counts_unique_trace_ids(self) -> None:
        span_a = _span_mock("trace-1", "op-1", 100.0)
        span_b = _span_mock("trace-1", "op-2", 200.0)
        span_c = _span_mock("trace-2", "op-3", 300.0)
        api = _spans_api_mock([span_a, span_b, span_c])

        request = LatencyDiagnosticRequest(
            service_name="svc", time_window_minutes=15, threshold_ms=500.0
        )
        adapter = DatadogTracesAdapter(spans_api=api)
        result = adapter.fetch_total_traces(request)

        assert result == 2  # noqa: PLR2004

    def test_fetch_total_traces_empty_returns_zero(self) -> None:
        api = _spans_api_mock([])

        request = LatencyDiagnosticRequest(
            service_name="svc", time_window_minutes=15, threshold_ms=500.0
        )
        adapter = DatadogTracesAdapter(spans_api=api)
        result = adapter.fetch_total_traces(request)

        assert result == 0

    # ── filter helpers ──────────────────────────────────────

    def test_slow_filter_includes_threshold_and_service(self) -> None:
        request = LatencyDiagnosticRequest(
            service_name="checkout", time_window_minutes=15, threshold_ms=250.0
        )
        adapter = DatadogTracesAdapter(spans_api=Mock())
        result = adapter._slow_filter(request)

        assert "checkout" in result
        assert ">250ms" in result
        assert "@duration" in result

    def test_total_filter_includes_service_name(self) -> None:
        request = LatencyDiagnosticRequest(
            service_name="web-api", time_window_minutes=15, threshold_ms=500.0
        )
        adapter = DatadogTracesAdapter(spans_api=Mock())
        result = adapter._total_filter(request)

        assert result == "service:web-api"

    def test_slow_filter_uses_int_threshold(self) -> None:
        request = LatencyDiagnosticRequest(
            service_name="svc", time_window_minutes=15, threshold_ms=1234.56
        )
        adapter = DatadogTracesAdapter(spans_api=Mock())
        result = adapter._slow_filter(request)

        assert ">1234ms" in result

    # ── error translation ───────────────────────────────────

    def test_api_error_rate_limit_raises_adapter_timeout(self) -> None:
        from datadog_api_client.exceptions import ApiException

        api = Mock()
        api.list_spans.side_effect = ApiException(status=429)
        adapter = DatadogTracesAdapter(spans_api=api)
        request = LatencyDiagnosticRequest(service_name="svc")

        with pytest.raises(AdapterTimeoutError):
            adapter.fetch_slow_spans(request)

    def test_api_error_401_raises_insufficient_permissions(self) -> None:
        from datadog_api_client.exceptions import ApiException

        api = Mock()
        api.list_spans.side_effect = ApiException(status=401)
        adapter = DatadogTracesAdapter(spans_api=api)
        request = LatencyDiagnosticRequest(service_name="svc")

        with pytest.raises(InsufficientPermissionsError):
            adapter.fetch_total_traces(request)

    def test_api_error_403_raises_insufficient_permissions(self) -> None:
        from datadog_api_client.exceptions import ApiException

        api = Mock()
        api.list_spans.side_effect = ApiException(status=403)
        adapter = DatadogTracesAdapter(spans_api=api)
        request = LatencyDiagnosticRequest(service_name="svc")

        with pytest.raises(InsufficientPermissionsError):
            adapter.fetch_slow_spans(request)

    def test_api_error_generic_raises_traces_unavailable(self) -> None:
        from datadog_api_client.exceptions import ApiException

        api = Mock()
        api.list_spans.side_effect = ApiException(status=500)
        adapter = DatadogTracesAdapter(spans_api=api)
        request = LatencyDiagnosticRequest(service_name="svc")

        with pytest.raises(TracesUnavailableError):
            adapter.fetch_slow_spans(request)

    # ── lazy API construction ───────────────────────────────

    def test_lazy_api_construction_when_spans_api_is_none(self) -> None:
        with patch(
            "hexawyn.adapters.secondary.datadog.datadog_traces_adapter._build_spans_api"
        ) as mock_build:
            mock_build.return_value = _spans_api_mock([_span_mock("t1", "op", 100.0)])
            adapter = DatadogTracesAdapter(key="k", app_key="a", site="s")
            request = LatencyDiagnosticRequest(service_name="svc")
            adapter.fetch_slow_spans(request)
            mock_build.assert_called_once_with("k", "a", "s")


class TestHelpers:
    def test_as_float_int(self) -> None:
        assert _as_float(42) == 42.0  # noqa: PLR2004

    def test_as_float_float(self) -> None:
        assert _as_float(3.14) == 3.14  # noqa: PLR2004

    def test_as_float_numeric_string(self) -> None:
        assert _as_float("123.45") == 123.45  # noqa: PLR2004

    def test_as_float_invalid_string_returns_zero(self) -> None:
        assert _as_float("not-a-number") == 0.0

    def test_as_float_none_returns_zero(self) -> None:
        assert _as_float(None) == 0.0

    def test_translate_error_rate_limit(self) -> None:
        from datadog_api_client.exceptions import ApiException

        exc = ApiException(status=429)
        result = _translate_error(exc)
        assert isinstance(result, AdapterTimeoutError)

    def test_translate_error_401(self) -> None:
        from datadog_api_client.exceptions import ApiException

        exc = ApiException(status=401)
        result = _translate_error(exc)
        assert isinstance(result, InsufficientPermissionsError)

    def test_translate_error_403(self) -> None:
        from datadog_api_client.exceptions import ApiException

        exc = ApiException(status=403)
        result = _translate_error(exc)
        assert isinstance(result, InsufficientPermissionsError)

    def test_translate_error_unknown(self) -> None:
        from datadog_api_client.exceptions import ApiException

        exc = ApiException(status=502)
        result = _translate_error(exc)
        assert isinstance(result, TracesUnavailableError)
