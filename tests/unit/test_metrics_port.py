from abc import ABC

import pytest

from hexawyn.application.ports.driven.metrics_port import MetricsPort


class TestMetricsPort:
    def test_is_abstract(self):
        assert issubclass(MetricsPort, ABC)

    def test_cannot_instantiate_directly(self):
        with pytest.raises(TypeError):
            MetricsPort()
