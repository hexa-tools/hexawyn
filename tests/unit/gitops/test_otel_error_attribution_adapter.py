from __future__ import annotations

from unittest.mock import patch


class TestOtelErrorAttributionAdapterUnit:
    def test_returns_list(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_error_attribution_adapter import (
            OTelErrorAttributionAdapter,
        )
        from hexawyn.domain.models.error_attribution import ErrorAttributionRequest

        adapter = OTelErrorAttributionAdapter()
        result = adapter.fetch_error_attribution(ErrorAttributionRequest(gateway="gw-1"))
        assert isinstance(result, list)

    def test_empty_gateway_returns_empty_list(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_error_attribution_adapter import (
            OTelErrorAttributionAdapter,
        )
        from hexawyn.domain.models.error_attribution import ErrorAttributionRequest

        adapter = OTelErrorAttributionAdapter()
        result = adapter.fetch_error_attribution(ErrorAttributionRequest(gateway=""))
        assert result == []

    def test_mocked_traces_populate_result(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_error_attribution_adapter import (
            OTelErrorAttributionAdapter,
        )
        from hexawyn.domain.models.error_attribution import ErrorAttributionRequest

        mock_traces = [
            {"traceID": "trace-001", "hasErrors": True},
            {"traceID": "trace-002", "hasErrors": False},
        ]
        with patch(
            "hexawyn.adapters.secondary.gitops.otel_error_attribution_adapter.search_jaeger_traces",
            return_value=mock_traces,
        ):
            adapter = OTelErrorAttributionAdapter()
            result = adapter.fetch_error_attribution(ErrorAttributionRequest(gateway="gw-1"))
            assert len(result) == 2  # noqa: PLR2004
            assert result[0]["trace_id"] == "trace-001"
