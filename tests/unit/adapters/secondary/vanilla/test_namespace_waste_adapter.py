"""Unit tests for VanillaNamespaceWasteAdapter."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.adapters.secondary.vanilla.adapters.namespace_waste_adapter import (
    VanillaNamespaceWasteAdapter,
)
from hexawyn.domain.errors import (
    ClusterUnreachableError,
)


class _NamespaceMetadata:
    def __init__(self, name: str, creation_timestamp):
        self.name = name
        self.creation_timestamp = creation_timestamp


class _Namespace:
    def __init__(self, name: str, creation_timestamp):
        self.metadata = _NamespaceMetadata(name, creation_timestamp)


class _NamespaceList:
    def __init__(self, items: list):
        self.items = items


class _Container:
    def __init__(self, requests: dict | None = None):
        self.resources = _ContainerResources(requests)


class _ContainerResources:
    def __init__(self, requests: dict | None = None):
        self.requests = requests or {}


class _PodSpec:
    def __init__(self, containers: list | None = None):
        self.containers = containers or []


class _PodMetadata:
    def __init__(self, name: str, namespace: str):
        self.name = name
        self.namespace = namespace


class _Pod:
    def __init__(self, name: str, namespace: str, containers: list | None = None):
        self.metadata = _PodMetadata(name, namespace)
        self.spec = _PodSpec(containers)


class _PodList:
    def __init__(self, items: list):
        self.items = items


class TestVanillaNamespaceWasteAdapter:
    def test_get_all_namespace_waste_data_empty_cluster(self) -> None:
        """Returns empty list when cluster has no namespaces."""
        api = MagicMock()
        api.list_namespace.return_value = _NamespaceList([])
        api.list_pod_for_all_namespaces.return_value = _PodList([])

        adapter = VanillaNamespaceWasteAdapter(api=api)
        result = adapter.get_all_namespace_waste_data(window_days=7)

        assert result == []

    def test_get_all_namespace_waste_data_single_namespace_no_pods(self) -> None:
        """Namespace with no pods gets default values."""
        from datetime import UTC, datetime, timedelta

        ts = datetime.now(UTC) - timedelta(hours=24)
        api = MagicMock()
        api.list_namespace.return_value = _NamespaceList([_Namespace("default", ts)])
        api.list_pod_for_all_namespaces.return_value = _PodList([])

        adapter = VanillaNamespaceWasteAdapter(api=api)
        result = adapter.get_all_namespace_waste_data(window_days=7)

        assert len(result) == 1
        assert result[0]["namespace"] == "default"
        assert result[0]["cpu_requested_cores"] is None
        assert result[0]["memory_requested_gb"] is None
        assert result[0]["age_hours"] == pytest.approx(24.0, rel=0.1)
        assert result[0]["has_resource_requests"] is False

    def test_get_all_namespace_waste_data_with_resource_requests(self) -> None:
        """Pods with CPU requests contribute to namespace totals."""
        from datetime import UTC, datetime, timedelta

        ts = datetime.now(UTC) - timedelta(hours=48)
        api = MagicMock()
        api.list_namespace.return_value = _NamespaceList([_Namespace("app", ts)])
        container = _Container({"cpu": "500m", "memory": "256Mi"})
        api.list_pod_for_all_namespaces.return_value = _PodList([_Pod("pod-1", "app", [container])])

        adapter = VanillaNamespaceWasteAdapter(api=api)
        result = adapter.get_all_namespace_waste_data(window_days=7)

        assert len(result) == 1
        assert result[0]["namespace"] == "app"
        assert result[0]["cpu_requested_cores"] == 0.5  # noqa: PLR2004
        assert result[0]["memory_requested_gb"] is not None
        assert result[0]["has_resource_requests"] is True

    def test_list_namespace_failure_raises_cluster_unreachable(self) -> None:
        api = MagicMock()
        api.list_namespace.side_effect = ConnectionError("no route to host")

        adapter = VanillaNamespaceWasteAdapter(api=api)
        with pytest.raises(ClusterUnreachableError):
            adapter.get_all_namespace_waste_data(window_days=7)

    def test_list_pods_failure_raises_cluster_unreachable(self) -> None:
        from datetime import UTC, datetime, timedelta

        ts = datetime.now(UTC) - timedelta(hours=1)
        api = MagicMock()
        api.list_namespace.return_value = _NamespaceList([_Namespace("ns", ts)])
        api.list_pod_for_all_namespaces.side_effect = TimeoutError("timeout")

        adapter = VanillaNamespaceWasteAdapter(api=api)
        with pytest.raises(ClusterUnreachableError):
            adapter.get_all_namespace_waste_data(window_days=7)

    def test_prometheus_unavailable_without_url_returns_empty_usage(self) -> None:
        """When no prometheus_url, usage is empty dict (zero maps)."""
        from datetime import UTC, datetime, timedelta

        ts = datetime.now(UTC) - timedelta(hours=1)
        api = MagicMock()
        api.list_namespace.return_value = _NamespaceList([_Namespace("ns", ts)])
        container = _Container({"cpu": "100m"})
        api.list_pod_for_all_namespaces.return_value = _PodList([_Pod("pod-1", "ns", [container])])

        adapter = VanillaNamespaceWasteAdapter(api=api, prometheus_url="")
        result = adapter.get_all_namespace_waste_data(window_days=7)

        assert len(result) == 1
        assert result[0]["cpu_actual_avg_cores"] is None
        assert result[0]["memory_actual_avg_gb"] is None

    def test_multiple_namespaces_sorted_alphabetically(self) -> None:
        from datetime import UTC, datetime, timedelta

        ts = datetime.now(UTC) - timedelta(hours=1)
        api = MagicMock()
        api.list_namespace.return_value = _NamespaceList(
            [
                _Namespace("z-ns", ts),
                _Namespace("a-ns", ts),
                _Namespace("m-ns", ts),
            ]
        )
        api.list_pod_for_all_namespaces.return_value = _PodList([])

        adapter = VanillaNamespaceWasteAdapter(api=api)
        result = adapter.get_all_namespace_waste_data(window_days=7)

        namespaces = [r["namespace"] for r in result]
        assert namespaces == sorted(namespaces)
