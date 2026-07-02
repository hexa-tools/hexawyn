from __future__ import annotations

from hexawyn.adapters.secondary.gitops.otel_redundant_call_adapter import (
    OTelRedundantCallAdapter,
)
from hexawyn.application.ports.driven.redundant_call_detection_port import (
    RedundantCallDetectionPort,
)
from hexawyn.domain.models.redundant_calls import RedundantCallRequest


class TestOTelRedundantCallAdapter:
    def test_implements_port(self) -> None:
        assert isinstance(OTelRedundantCallAdapter(), RedundantCallDetectionPort)

    def test_fetch_returns_empty(self) -> None:
        r = OTelRedundantCallAdapter().fetch_spans(RedundantCallRequest(flow="test"))
        assert r == []
