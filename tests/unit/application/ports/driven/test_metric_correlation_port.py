from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.metric_correlation_port import MetricCorrelationPort


class TestMetricCorrelationPort:
    def test_is_abstract(self) -> None:
        assert issubclass(MetricCorrelationPort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            MetricCorrelationPort()  # type: ignore[abstract]

    def test_has_methods(self) -> None:
        for n in ["fetch_primary_series", "fetch_correlated_series"]:
            assert getattr(getattr(MetricCorrelationPort, n), "__isabstractmethod__", False)
