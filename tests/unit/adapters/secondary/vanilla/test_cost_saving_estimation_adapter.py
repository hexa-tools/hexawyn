"""Unit tests for VanillaCostSavingAdapter."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest
from hexawyn.adapters.secondary.vanilla.adapters.cost_saving_estimation_adapter import (
    VanillaCostSavingAdapter,
)
from hexawyn.domain.errors import ClusterUnreachableError


class _PodMetadata:
    def __init__(self, name: str, namespace: str):
        self.name = name
        self.namespace = namespace


class _PodSpec:
    def __init__(self, containers: list | None = None):
        self.containers = containers or []


class _Pod:
    def __init__(self, name: str, namespace: str, containers: list | None = None):
        self.metadata = _PodMetadata(name, namespace)
        self.spec = _PodSpec(containers)


class _PodList:
    def __init__(self, items: list):
        self.items = items


class TestVanillaCostSavingAdapter:
    def test_get_pod_resource_data_empty(self) -> None:
        api = MagicMock()
        api.list_pod_for_all_namespaces.return_value = _PodList([])

        with patch(
            "hexawyn.adapters.secondary.vanilla.adapters.cost_saving_estimation_adapter.client",
            create=True,
        ) as mock_client:
            mock_auto_api = MagicMock()
            mock_auto_api.list_horizontal_pod_autoscaler_for_all_namespaces.return_value = _PodList(
                []
            )
            mock_client.AutoscalingV2Api.return_value = mock_auto_api

            adapter = VanillaCostSavingAdapter(api=api)
            result = adapter.get_pod_resource_data()

        assert result == []

    def test_get_pod_resource_data_single_pod(self) -> None:
        api = MagicMock()
        api.list_pod_for_all_namespaces.return_value = _PodList([_Pod("pod-1", "default", [])])

        with patch(
            "hexawyn.adapters.secondary.vanilla.adapters.cost_saving_estimation_adapter.client",
            create=True,
        ) as mock_client:
            mock_auto_api = MagicMock()
            mock_auto_api.list_horizontal_pod_autoscaler_for_all_namespaces.return_value = _PodList(
                []
            )
            mock_client.AutoscalingV2Api.return_value = mock_auto_api

            adapter = VanillaCostSavingAdapter(api=api)
            result = adapter.get_pod_resource_data()

        assert len(result) == 1
        assert result[0]["pod_name"] == "pod-1"
        assert result[0]["namespace"] == "default"

    def test_get_pod_resource_data_api_failure(self) -> None:
        api = MagicMock()
        api.list_pod_for_all_namespaces.side_effect = ConnectionError("down")

        adapter = VanillaCostSavingAdapter(api=api)
        with pytest.raises(ClusterUnreachableError):
            adapter.get_pod_resource_data()

    def test_get_previous_total_saving_returns_none_on_db_failure(self) -> None:
        api = MagicMock()
        adapter = VanillaCostSavingAdapter(api=api)
        result = adapter.get_previous_total_saving()
        assert result is None

    def test_store_total_saving_does_not_raise(self) -> None:
        api = MagicMock()
        adapter = VanillaCostSavingAdapter(api=api)
        adapter.store_total_saving(100.0)


class TestFetchHpaMap:
    def test_returns_hpa_map(self) -> None:
        from kubernetes import client

        api = MagicMock()
        adapter = VanillaCostSavingAdapter(api=api)

        hpa = MagicMock()
        hpa.metadata = MagicMock()
        hpa.metadata.namespace = "ns"
        hpa.spec = MagicMock()
        hpa.spec.scale_target_ref = MagicMock()
        hpa.spec.scale_target_ref.name = "my-deploy"
        hpa.spec.min_replicas = 3

        mock_auto = MagicMock()
        mock_auto_item = MagicMock()
        mock_auto_item.items = [hpa]
        mock_auto.list_horizontal_pod_autoscaler_for_all_namespaces.return_value = mock_auto_item

        with patch.object(client, "AutoscalingV2Api", return_value=mock_auto):
            result = adapter._fetch_hpa_map()
            assert result == {"ns/my-deploy": 3}

    def test_handles_exception(self) -> None:
        from kubernetes import client

        api = MagicMock()
        adapter = VanillaCostSavingAdapter(api=api)

        with patch.object(client, "AutoscalingV2Api") as mock:
            mock.side_effect = Exception("hpa error")
            assert adapter._fetch_hpa_map() == {}


class TestFetchPodPrometheusMap:
    def test_no_prometheus_url(self) -> None:
        api = MagicMock()
        adapter = VanillaCostSavingAdapter(api=api, prometheus_url="")
        assert adapter._fetch_pod_prometheus_map("query") == {}

    def test_returns_results(self) -> None:
        import httpx

        api = MagicMock()
        adapter = VanillaCostSavingAdapter(api=api, prometheus_url="http://prom:9090")
        mock_resp = MagicMock()
        mock_resp.raise_for_status.return_value = None
        mock_resp.json.return_value = {
            "status": "success",
            "data": {
                "resultType": "vector",
                "result": [
                    {
                        "metric": {"namespace": "ns", "pod": "my-pod"},
                        "value": [1700000000, "0.42"],
                    },
                ],
            },
        }
        with patch.object(httpx, "get", return_value=mock_resp):
            result = adapter._fetch_pod_prometheus_map("query")
            assert result == {"ns/my-pod": 0.42}

    def test_handles_exception(self) -> None:
        import httpx

        api = MagicMock()
        adapter = VanillaCostSavingAdapter(api=api, prometheus_url="http://prom:9090")
        with patch.object(httpx, "get", side_effect=Exception("timeout")):
            assert adapter._fetch_pod_prometheus_map("query") == {}
