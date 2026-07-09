from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driven.cluster_resource_metrics_port import (
    ClusterDailyUsage,
    ClusterResourceMetricsPort,
    ClusterUsageSnapshot,
    NodeUtilizationSeries,
)


class TestClusterResourceMetricsPortContract:
    def test_port_is_abstract(self) -> None:
        with pytest.raises(TypeError):
            ClusterResourceMetricsPort()  # type: ignore[abstract]

    def test_abstract_methods_are_defined(self) -> None:
        methods = {"get_current_usage", "get_daily_usage", "get_node_utilization"}
        abstract_methods = set(ClusterResourceMetricsPort.__abstractmethods__)
        assert methods == abstract_methods

    def test_concrete_subclass_can_be_instantiated(self) -> None:
        from datetime import datetime

        class FakeMetrics(ClusterResourceMetricsPort):
            def get_current_usage(self, timeout_seconds: float) -> ClusterUsageSnapshot:
                return {"cpu_cores": 1.0, "memory_gb": 2.0}

            def get_daily_usage(
                self, start: datetime, end: datetime, timeout_seconds: float
            ) -> ClusterDailyUsage:
                return {"cpu_daily_cores": [1.0], "memory_daily_gb": [2.0]}

            def get_node_utilization(
                self, start: datetime, end: datetime, timeout_seconds: float
            ) -> dict[str, NodeUtilizationSeries]:
                return {"node-1": {"cpu_percent_series": [], "memory_percent_series": []}}

        adapter = FakeMetrics()

        assert adapter.get_current_usage(1.0)["cpu_cores"] == 1.0

    def test_typed_dicts_have_expected_keys(self) -> None:
        assert set(ClusterUsageSnapshot.__annotations__) == {"cpu_cores", "memory_gb"}
        assert set(ClusterDailyUsage.__annotations__) == {"cpu_daily_cores", "memory_daily_gb"}
        assert set(NodeUtilizationSeries.__annotations__) == {
            "cpu_percent_series",
            "memory_percent_series",
        }

    def test_is_usable_as_spec_for_mock(self) -> None:
        mock = MagicMock(spec=ClusterResourceMetricsPort)
        mock.get_current_usage.return_value = {"cpu_cores": 3.0, "memory_gb": 4.0}

        assert mock.get_current_usage(1.0)["memory_gb"] == 4.0
