from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.slow_trace_search_port import SlowTraceSearchPort


class TestSlowTraceSearchPort:
    def test_is_abstract(self) -> None:
        assert issubclass(SlowTraceSearchPort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            SlowTraceSearchPort()  # type: ignore[abstract]

    def test_has_methods(self) -> None:
        assert getattr(
            getattr(SlowTraceSearchPort, "search_pod_traces"), "__isabstractmethod__", False
        )
