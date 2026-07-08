from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.trace_log_correlation_port import (
    TraceLogCorrelationPort,
)


class TestTraceLogCorrelationPort:
    def test_is_abstract(self) -> None:
        assert issubclass(TraceLogCorrelationPort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            TraceLogCorrelationPort()  # type: ignore[abstract]

    def test_has_methods(self) -> None:
        for n in ["fetch_error_spans", "fetch_correlated_logs"]:
            assert getattr(getattr(TraceLogCorrelationPort, n), "__isabstractmethod__", False)
