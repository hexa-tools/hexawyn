from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.latency_percentile_port import LatencyPercentilePort


class TestLatencyPercentilePort:
    def test_is_abstract(self) -> None:
        assert issubclass(LatencyPercentilePort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            LatencyPercentilePort()  # type: ignore[abstract]

    def test_has_methods(self) -> None:
        assert getattr(
            getattr(LatencyPercentilePort, "fetch_percentiles"), "__isabstractmethod__", False
        )
