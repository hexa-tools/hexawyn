from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driving.execute_prometheus_query.execute_prometheus_query_service_port import (
    ExecutePrometheusQueryServicePort,
)


class TestExecutePrometheusQueryServicePort:
    def test_is_abstract(self) -> None:
        assert issubclass(ExecutePrometheusQueryServicePort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            ExecutePrometheusQueryServicePort()  # type: ignore[abstract]
