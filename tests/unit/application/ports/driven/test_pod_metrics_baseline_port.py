from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.pod_metrics_baseline_port import PodMetricsBaselinePort


class TestPodMetricsBaselinePort:
    def test_is_abstract(self) -> None:
        assert issubclass(PodMetricsBaselinePort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            PodMetricsBaselinePort()  # type: ignore[abstract]
