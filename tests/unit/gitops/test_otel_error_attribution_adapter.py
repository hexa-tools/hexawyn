# Auto-generated test for otel_error_attribution_adapter

from __future__ import annotations


class TestOtelErrorAttributionAdapterUnit:
    def test_returns_list(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_error_attribution_adapter import (
            OTelErrorAttributionAdapter,
        )
        from hexawyn.domain.models.error_attribution import ErrorAttributionRequest

        adapter = OTelErrorAttributionAdapter()
        result = adapter.fetch_error_attribution(ErrorAttributionRequest(gateway="gw-1"))
        assert isinstance(result, list)
