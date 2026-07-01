from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.trace_event_correlation_port import (
    TraceEventCorrelationPort,
)


class TestTraceEventCorrelationPort:
    def test_is_abstract(self) -> None:
        assert issubclass(TraceEventCorrelationPort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            TraceEventCorrelationPort()  # type: ignore[abstract]

    def test_has_methods(self) -> None:
        for n in ["fetch_k8s_events", "fetch_slowest_span"]:
            assert getattr(getattr(TraceEventCorrelationPort, n), "__isabstractmethod__", False)
