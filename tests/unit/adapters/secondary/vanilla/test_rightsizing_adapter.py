"""Unit tests for VanillaRightsizingAdapter."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.adapters.secondary.vanilla.adapters.rightsizing_adapter import (
    VanillaRightsizingAdapter,
)
from hexawyn.domain.errors import ClusterUnreachableError


class TestVanillaRightsizingAdapter:
    def test_get_workload_rightsizing_data_empty(self) -> None:
        apps_api = MagicMock()
        apps_api.list_deployment_for_all_namespaces.return_value = _DeploymentList([])
        metrics_api = MagicMock()
        metrics_api.list_cluster_custom_object.return_value = {"items": []}

        adapter = VanillaRightsizingAdapter(apps_api=apps_api, metrics_api=metrics_api)
        result = adapter.get_workload_rightsizing_data()

        assert result == []

    def test_get_workload_rightsizing_data_single_deployment(self) -> None:
        apps_api = MagicMock()
        apps_api.list_deployment_for_all_namespaces.return_value = _DeploymentList(
            [_Deployment("web", "prod", "100m", "256Mi")]
        )
        metrics_api = MagicMock()
        metrics_api.list_cluster_custom_object.return_value = {"items": []}

        adapter = VanillaRightsizingAdapter(apps_api=apps_api, metrics_api=metrics_api)
        result = adapter.get_workload_rightsizing_data()

        assert len(result) == 1
        assert result[0]["resource_name"] == "web"
        assert result[0]["namespace"] == "prod"
        assert result[0]["kind"] == "Deployment"

    def test_get_workload_rightsizing_data_apps_api_failure(self) -> None:
        apps_api = MagicMock()
        apps_api.list_deployment_for_all_namespaces.side_effect = ConnectionError("down")
        metrics_api = MagicMock()

        adapter = VanillaRightsizingAdapter(apps_api=apps_api, metrics_api=metrics_api)
        with pytest.raises(ClusterUnreachableError):
            adapter.get_workload_rightsizing_data()

    def test_get_workload_rightsizing_data_metrics_api_graceful_degradation(self) -> None:
        apps_api = MagicMock()
        apps_api.list_deployment_for_all_namespaces.return_value = _DeploymentList(
            [_Deployment("svc", "ns", "200m", "512Mi")]
        )
        metrics_api = MagicMock()
        metrics_api.list_cluster_custom_object.side_effect = Exception("no metrics")

        adapter = VanillaRightsizingAdapter(apps_api=apps_api, metrics_api=metrics_api)
        result = adapter.get_workload_rightsizing_data()

        assert len(result) == 1
        assert result[0]["resource_name"] == "svc"
        assert result[0]["cpu_actual_cores"] is None
        assert result[0]["memory_actual_mi"] is None


class _DeploymentMetadata:
    def __init__(self, name: str, namespace: str):
        self.name = name
        self.namespace = namespace


class _DeploymentSpec:
    def __init__(self, template):
        self.template = template


class _PodTemplateSpec:
    def __init__(self, spec):
        self.spec = spec


class _PodSpec:
    def __init__(self, containers: list):
        self.containers = containers


class _Container:
    def __init__(self, resources: dict | None = None):
        self.resources = _Resources(resources)


class _Resources:
    def __init__(self, reqs: dict | None = None):
        self.requests = reqs or {}


class _Deployment:
    def __init__(self, name: str, namespace: str, cpu: str, memory: str):
        self.metadata = _DeploymentMetadata(name, namespace)
        container = _Container({"cpu": cpu, "memory": memory})
        pod_spec = _PodSpec([container])
        template_spec = _PodTemplateSpec(pod_spec)
        self.spec = _DeploymentSpec(template_spec)


class _DeploymentList:
    def __init__(self, items: list):
        self.items = items
