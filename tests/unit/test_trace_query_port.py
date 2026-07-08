from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.trace_query_port import TraceQueryPort


class TestTraceQueryPort:
    def test_is_abstract(self) -> None:
        assert issubclass(TraceQueryPort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            TraceQueryPort()  # type: ignore[abstract]

    def test_has_methods(self) -> None:
        for n in ["fetch_slow_spans", "fetch_total_traces"]:
            assert getattr(getattr(TraceQueryPort, n), "__isabstractmethod__", False)
