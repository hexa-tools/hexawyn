from __future__ import annotations

from hexawyn.application.ports.driven.pod_metrics_port import (
    PodMetricSnapshot,
    PodMetricsPort,
)


class TestPodMetricsPort:
    def test_pod_metric_snapshot_typed_dict(self) -> None:
        snapshot: PodMetricSnapshot = {
            "name": "pod-abc",
            "namespace": "dev",
            "cpu_cores": 0.35,
            "memory_gb": 1.5,
        }
        assert snapshot["name"] == "pod-abc"
        assert snapshot["cpu_cores"] == 0.35  # noqa: PLR2004
        assert isinstance(snapshot["memory_gb"], float)

    def test_port_is_abstract(self) -> None:
        import inspect

        assert inspect.isabstract(PodMetricsPort)
        assert hasattr(PodMetricsPort, "get_pod_metrics")
