from __future__ import annotations

from hexawyn.adapters.secondary.gitops.otel_error_attribution_adapter import (
    OTelErrorAttributionAdapter,
)
from hexawyn.application.ports.driven.error_attribution_port import ErrorAttributionPort
from hexawyn.domain.models.error_attribution import ErrorAttributionRequest


class TestOTelErrorAttributionAdapter:
    def test_implements_port(self) -> None:
        assert isinstance(OTelErrorAttributionAdapter(), ErrorAttributionPort)

    def test_fetch_returns_empty(self) -> None:
        r = OTelErrorAttributionAdapter().fetch_error_attribution(
            ErrorAttributionRequest(gateway="x")
        )
        assert r == []
