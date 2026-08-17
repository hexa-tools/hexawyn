from __future__ import annotations

from unittest.mock import MagicMock


class TestVanillaPodMetricsAdapter:
    def test_get_pod_metrics_empty_cluster(self) -> None:
        from hexawyn.adapters.secondary.vanilla.adapters.pod_metrics_adapter import (
            VanillaPodMetricsAdapter,
        )

        metrics_api = MagicMock()
        raw_response = {"items": []}
        metrics_api.list_cluster_custom_object.return_value = raw_response

        adapter = VanillaPodMetricsAdapter(metrics_api=metrics_api, cluster_name="test")
        result = adapter.get_pod_metrics()

        assert isinstance(result, list)
        assert len(result) == 0

    def test_get_pod_metrics_parses_single_pod(self) -> None:
        from hexawyn.adapters.secondary.vanilla.adapters.pod_metrics_adapter import (
            VanillaPodMetricsAdapter,
        )

        metrics_api = MagicMock()
        raw_response = {
            "items": [
                {
                    "metadata": {"name": "pod-1", "namespace": "dev"},
                    "containers": [
                        {"usage": {"cpu": "500000000n", "memory": "1048576Ki"}},
                    ],
                },
            ],
        }
        metrics_api.list_cluster_custom_object.return_value = raw_response

        adapter = VanillaPodMetricsAdapter(metrics_api=metrics_api, cluster_name="test")
        result = adapter.get_pod_metrics()

        assert len(result) == 1  # noqa: PLR2004
        snapshot = result[0]
        assert snapshot["name"] == "pod-1"
        assert snapshot["namespace"] == "dev"
        assert snapshot["cpu_cores"] == 0.5  # noqa: PLR2004
        assert snapshot["memory_gb"] == 1.0

    def test_get_pod_metrics_namespace_filter(self) -> None:
        from hexawyn.adapters.secondary.vanilla.adapters.pod_metrics_adapter import (
            VanillaPodMetricsAdapter,
        )

        metrics_api = MagicMock()
        metrics_api.list_namespaced_custom_object.return_value = {"items": []}

        adapter = VanillaPodMetricsAdapter(metrics_api=metrics_api, cluster_name="test")
        result = adapter.get_pod_metrics(namespace="dev")

        assert isinstance(result, list)
        metrics_api.list_namespaced_custom_object.assert_called_once()

    def test_get_pod_metrics_api_error_raises(self) -> None:
        import pytest
        from hexawyn.adapters.secondary.vanilla.adapters.pod_metrics_adapter import (
            VanillaPodMetricsAdapter,
        )
        from hexawyn.domain.errors import MetricsUnavailableError

        metrics_api = MagicMock()
        metrics_api.list_cluster_custom_object.side_effect = RuntimeError("timeout")

        adapter = VanillaPodMetricsAdapter(metrics_api=metrics_api, cluster_name="test")
        with pytest.raises(MetricsUnavailableError):
            adapter.get_pod_metrics()

    def test_get_pod_metrics_handles_missing_metadata(self) -> None:
        from hexawyn.adapters.secondary.vanilla.adapters.pod_metrics_adapter import (
            VanillaPodMetricsAdapter,
        )

        metrics_api = MagicMock()
        raw_response = {
            "items": [
                {
                    "containers": [
                        {"usage": {"cpu": "100m", "memory": "512Mi"}},
                    ],
                },
            ],
        }
        metrics_api.list_cluster_custom_object.return_value = raw_response

        adapter = VanillaPodMetricsAdapter(metrics_api=metrics_api, cluster_name="test")
        result = adapter.get_pod_metrics()

        assert len(result) == 1  # noqa: PLR2004
        assert result[0]["name"] == "unknown"
        assert result[0]["namespace"] == "unknown"

    def test_get_pod_metrics_missing_usage_handled(self) -> None:
        from hexawyn.adapters.secondary.vanilla.adapters.pod_metrics_adapter import (
            VanillaPodMetricsAdapter,
        )

        metrics_api = MagicMock()
        raw_response = {
            "items": [
                {
                    "metadata": {"name": "bare-pod", "namespace": "ns"},
                    "containers": [{}],
                },
            ],
        }
        metrics_api.list_cluster_custom_object.return_value = raw_response

        adapter = VanillaPodMetricsAdapter(metrics_api=metrics_api, cluster_name="test")
        result = adapter.get_pod_metrics()

        assert result[0]["cpu_cores"] == 0.0
        assert result[0]["memory_gb"] == 0.0

    def test_get_pod_metrics_multiple_containers_summed(self) -> None:
        from hexawyn.adapters.secondary.vanilla.adapters.pod_metrics_adapter import (
            VanillaPodMetricsAdapter,
        )

        metrics_api = MagicMock()
        raw_response = {
            "items": [
                {
                    "metadata": {"name": "multi-container", "namespace": "dev"},
                    "containers": [
                        {"usage": {"cpu": "100m", "memory": "256Mi"}},
                        {"usage": {"cpu": "200m", "memory": "256Mi"}},
                    ],
                },
            ],
        }
        metrics_api.list_cluster_custom_object.return_value = raw_response

        adapter = VanillaPodMetricsAdapter(metrics_api=metrics_api, cluster_name="test")
        result = adapter.get_pod_metrics()

        assert result[0]["cpu_cores"] == 0.3  # noqa: PLR2004
        assert result[0]["memory_gb"] == 0.5  # noqa: PLR2004

    def test_get_pod_metrics_without_metrics_api_raises(self) -> None:
        import pytest
        from hexawyn.adapters.secondary.vanilla.adapters.pod_metrics_adapter import (
            VanillaPodMetricsAdapter,
        )
        from hexawyn.domain.errors import MetricsUnavailableError

        adapter = VanillaPodMetricsAdapter(metrics_api=None, cluster_name="test")
        with pytest.raises(MetricsUnavailableError):
            adapter.get_pod_metrics()

    def test_get_pod_metrics_non_list_containers_ignored(self) -> None:
        from hexawyn.adapters.secondary.vanilla.adapters.pod_metrics_adapter import (
            VanillaPodMetricsAdapter,
        )

        metrics_api = MagicMock()
        raw_response = {
            "items": [
                {
                    "metadata": {"name": "weird-pod", "namespace": "ns"},
                    "containers": "not-a-list",
                },
            ],
        }
        metrics_api.list_cluster_custom_object.return_value = raw_response

        adapter = VanillaPodMetricsAdapter(metrics_api=metrics_api, cluster_name="test")
        result = adapter.get_pod_metrics()

        assert result[0]["cpu_cores"] == 0.0
        assert result[0]["memory_gb"] == 0.0

    def test_get_pod_metrics_non_dict_container_skipped(self) -> None:
        from hexawyn.adapters.secondary.vanilla.adapters.pod_metrics_adapter import (
            VanillaPodMetricsAdapter,
        )

        metrics_api = MagicMock()
        raw_response = {
            "items": [
                {
                    "metadata": {"name": "odd-container", "namespace": "ns"},
                    "containers": [
                        "plain-string-container",
                        {"usage": {"cpu": "100m", "memory": "512Mi"}},
                    ],
                },
            ],
        }
        metrics_api.list_cluster_custom_object.return_value = raw_response

        adapter = VanillaPodMetricsAdapter(metrics_api=metrics_api, cluster_name="test")
        result = adapter.get_pod_metrics()

        assert result[0]["name"] == "odd-container"
        assert result[0]["cpu_cores"] == 0.1  # noqa: PLR2004
        assert result[0]["memory_gb"] == 0.5  # noqa: PLR2004
