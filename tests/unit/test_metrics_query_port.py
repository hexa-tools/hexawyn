from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.metrics_query_port import MetricsQueryPort


class TestMetricsQueryPort:
    def test_is_abstract(self) -> None:
        assert issubclass(MetricsQueryPort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            MetricsQueryPort()  # type: ignore[abstract]
