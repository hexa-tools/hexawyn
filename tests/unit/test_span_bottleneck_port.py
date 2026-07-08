from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.span_bottleneck_port import SpanBottleneckPort


class TestSpanBottleneckPort:
    def test_is_abstract(self) -> None:
        assert issubclass(SpanBottleneckPort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            SpanBottleneckPort()  # type: ignore[abstract]

    def test_has_methods(self) -> None:
        for name in ["fetch_db_spans", "fetch_redis_spans"]:
            assert getattr(getattr(SpanBottleneckPort, name), "__isabstractmethod__", False)
