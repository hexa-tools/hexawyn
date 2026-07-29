"""Unit tests for VanillaWhatIfSimulationAdapter."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest
from hexawyn.adapters.secondary.vanilla.adapters.what_if_simulation_adapter import (
    VanillaWhatIfSimulationAdapter,
)
from hexawyn.domain.errors import ClusterUnreachableError
from kubernetes import client


class _DeploymentMetadata:
    def __init__(self, name: str, namespace: str):
        self.name = name
        self.namespace = namespace


class _DeploymentSpec:
    def __init__(self, replicas: int):
        self.replicas = replicas


class _Deployment:
    def __init__(self, name: str, namespace: str, replicas: int):
        self.metadata = _DeploymentMetadata(name, namespace)
        self.spec = _DeploymentSpec(replicas)


class _PodMetadata:
    def __init__(self, name: str, namespace: str, owner_references=None):
        self.name = name
        self.namespace = namespace
        self.owner_references = owner_references


class _PodSpec:
    def __init__(self, containers: list | None = None, init_containers: list | None = None):
        self.containers = containers or []
        self.init_containers = init_containers or []


class _Pod:
    def __init__(
        self,
        name: str,
        namespace: str,
        containers: list | None = None,
        owner_refs=None,
    ):
        self.metadata = _PodMetadata(name, namespace, owner_refs)
        self.spec = _PodSpec(containers)


class _PodList:
    def __init__(self, items: list):
        self.items = items


class _DeploymentList:
    def __init__(self, items: list):
        self.items = items


class TestWhatIfBasics:
    def test_get_current_replicas_found(self) -> None:
        api = MagicMock()
        apps_api = MagicMock()
        apps_api.list_deployment_for_all_namespaces.return_value = _DeploymentList(
            [_Deployment("svc", "ns", 3)]
        )
        adapter = VanillaWhatIfSimulationAdapter(api=api, apps_api=apps_api)
        assert adapter.get_current_replicas("ns", "svc") == 3  # noqa: PLR2004

    def test_get_current_replicas_not_found(self) -> None:
        api = MagicMock()
        apps_api = MagicMock()
        apps_api.list_deployment_for_all_namespaces.return_value = _DeploymentList(
            [_Deployment("other", "other", 1)]
        )
        adapter = VanillaWhatIfSimulationAdapter(api=api, apps_api=apps_api)
        assert adapter.get_current_replicas("ns", "svc") == 0

    def test_get_current_replicas_api_error(self) -> None:
        api = MagicMock()
        apps_api = MagicMock()
        apps_api.list_deployment_for_all_namespaces.side_effect = Exception("err")
        adapter = VanillaWhatIfSimulationAdapter(api=api, apps_api=apps_api)
        assert adapter.get_current_replicas("ns", "svc") == 0

    def test_get_current_cpu_utilization_no_prometheus(self) -> None:
        api = MagicMock()
        apps_api = MagicMock()
        adapter = VanillaWhatIfSimulationAdapter(api=api, apps_api=apps_api)
        assert adapter.get_current_cpu_utilization("ns", "svc") == 0.0

    def test_get_current_cpu_utilization_with_prometheus(self) -> None:
        import httpx

        api = MagicMock()
        apps_api = MagicMock()
        adapter = VanillaWhatIfSimulationAdapter(
            api=api, apps_api=apps_api, prometheus_url="http://prom:9090"
        )
        mock_resp = MagicMock()
        mock_resp.raise_for_status.return_value = None
        mock_resp.json.return_value = {"data": {"result": [{"value": [None, "75.5"]}]}}
        with patch.object(httpx, "get", return_value=mock_resp):
            assert adapter.get_current_cpu_utilization("ns", "svc") == 75.5  # noqa: PLR2004

    def test_get_current_cpu_utilization_empty_result(self) -> None:
        import httpx

        api = MagicMock()
        apps_api = MagicMock()
        adapter = VanillaWhatIfSimulationAdapter(
            api=api, apps_api=apps_api, prometheus_url="http://prom:9090"
        )
        mock_resp = MagicMock()
        mock_resp.raise_for_status.return_value = None
        mock_resp.json.return_value = {"data": {"result": []}}
        with patch.object(httpx, "get", return_value=mock_resp):
            assert adapter.get_current_cpu_utilization("ns", "svc") == 0.0

    def test_get_current_cpu_utilization_http_error(self) -> None:
        import httpx

        api = MagicMock()
        apps_api = MagicMock()
        adapter = VanillaWhatIfSimulationAdapter(
            api=api, apps_api=apps_api, prometheus_url="http://prom:9090"
        )
        with patch.object(httpx, "get", side_effect=Exception("timeout")):
            assert adapter.get_current_cpu_utilization("ns", "svc") == 0.0


class TestPdbInfo:
    def test_no_pdb_method(self) -> None:
        api = MagicMock()
        apps_api = MagicMock()
        adapter = VanillaWhatIfSimulationAdapter(api=api, apps_api=apps_api)
        result = adapter.get_pdb_info("ns", "svc")
        assert result is None

    def test_pdb_not_found(self) -> None:
        api = MagicMock()
        api.list_namespaced_pod_disruption_budget = MagicMock()
        api.list_namespaced_pod_disruption_budget.return_value = _PodList([])
        apps_api = MagicMock()
        adapter = VanillaWhatIfSimulationAdapter(api=api, apps_api=apps_api)
        assert adapter.get_pdb_info("ns", "svc") is None

    def test_pdb_api_error(self) -> None:
        api = MagicMock()
        api.list_namespaced_pod_disruption_budget = MagicMock()
        api.list_namespaced_pod_disruption_budget.side_effect = Exception("err")
        apps_api = MagicMock()
        adapter = VanillaWhatIfSimulationAdapter(api=api, apps_api=apps_api)
        assert adapter.get_pdb_info("ns", "svc") is None

    def test_pdb_found(self) -> None:
        api = MagicMock()
        apps_api = MagicMock()
        adapter = VanillaWhatIfSimulationAdapter(api=api, apps_api=apps_api)

        pdb_item = MagicMock()
        pdb_item.metadata = MagicMock()
        pdb_item.metadata.name = "svc-pdb"
        pdb_item.spec = MagicMock()
        pdb_item.spec.min_available = 1

        api.list_namespaced_pod_disruption_budget = MagicMock()
        api.list_namespaced_pod_disruption_budget.return_value = _PodList([pdb_item])

        result = adapter.get_pdb_info("ns", "svc")
        assert result is not None
        assert result["min_available"] == 1  # type: ignore[index]


class TestHpaInfo:
    def test_hpa_not_found(self) -> None:
        api = MagicMock()
        apps_api = MagicMock()
        adapter = VanillaWhatIfSimulationAdapter(api=api, apps_api=apps_api)

        with patch.object(client, "AutoscalingV2Api", return_value=MagicMock()) as mock_api:
            mock_api.return_value.list_namespaced_horizontal_pod_autoscaler.return_value = _PodList(
                []
            )
            assert adapter.get_hpa_info("ns", "svc") is None

    def test_hpa_api_error(self) -> None:
        api = MagicMock()
        apps_api = MagicMock()
        adapter = VanillaWhatIfSimulationAdapter(api=api, apps_api=apps_api)

        with patch.object(client, "AutoscalingV2Api") as mock_api:
            mock_api.return_value.list_namespaced_horizontal_pod_autoscaler.side_effect = Exception(
                "hpa error"
            )
            assert adapter.get_hpa_info("ns", "svc") is None

    def test_hpa_found(self) -> None:
        api = MagicMock()
        apps_api = MagicMock()
        adapter = VanillaWhatIfSimulationAdapter(api=api, apps_api=apps_api)

        hpa = MagicMock()
        hpa.metadata = MagicMock()
        hpa.metadata.name = "svc-hpa"
        hpa.spec = MagicMock()
        hpa.spec.min_replicas = 2
        hpa.spec.max_replicas = 10
        hpa.status = MagicMock()
        hpa.status.current_replicas = 5

        with patch.object(client, "AutoscalingV2Api", return_value=MagicMock()) as mock_api:
            mock_api.return_value.list_namespaced_horizontal_pod_autoscaler.return_value = _PodList(
                [hpa]
            )
            result = adapter.get_hpa_info("ns", "svc")
            assert result is not None
            assert result["current_replicas"] == 5  # type: ignore[index]  # noqa: PLR2004


class TestServiceTopology:
    def test_returns_topology(self) -> None:
        api = MagicMock()
        apps_api = MagicMock()
        adapter = VanillaWhatIfSimulationAdapter(api=api, apps_api=apps_api)

        svc = MagicMock()
        svc.metadata = MagicMock()
        svc.metadata.name = "my-svc"
        svc.spec = MagicMock()
        svc.spec.selector = {"app": "my-app"}
        svc_list = MagicMock()
        svc_list.items = [svc]

        pod = MagicMock()
        pod.metadata = MagicMock()
        pod.metadata.name = "my-pod-abc"
        pod.status = MagicMock()
        pod.status.phase = "Running"
        pod_list = MagicMock()
        pod_list.items = [pod]

        api.list_namespaced_service.return_value = svc_list
        api.list_namespaced_pod.return_value = pod_list

        result = adapter.get_service_topology("ns", "svc")
        assert "my-svc" in result
        assert len(result["my-svc"]) == 1
        assert result["my-svc"][0]["name"] == "my-pod-abc"

    def test_handles_exception(self) -> None:
        api = MagicMock()
        apps_api = MagicMock()
        api.list_namespaced_service.side_effect = Exception("api error")
        adapter = VanillaWhatIfSimulationAdapter(api=api, apps_api=apps_api)
        assert adapter.get_service_topology("ns", "svc") == {}

    def test_service_with_no_metadata_skipped(self) -> None:
        api = MagicMock()
        apps_api = MagicMock()
        adapter = VanillaWhatIfSimulationAdapter(api=api, apps_api=apps_api)

        svc = MagicMock()
        svc.metadata = None
        svc_list = MagicMock()
        svc_list.items = [svc]

        api.list_namespaced_service.return_value = svc_list

        result = adapter.get_service_topology("ns", "svc")
        assert result == {}


class TestDependencyGraph:
    def test_get_dependency_graph_returns_dict(self) -> None:
        api = MagicMock()
        apps_api = MagicMock()
        adapter = VanillaWhatIfSimulationAdapter(api=api, apps_api=apps_api)

        svc = MagicMock()
        svc.metadata = MagicMock()
        svc.metadata.name = "my-svc"
        svc.spec = MagicMock()
        svc.spec.selector = {"app": "my-app"}
        svc_list = MagicMock()
        svc_list.items = [svc]

        pod = MagicMock()
        pod.metadata = MagicMock()
        pod.metadata.name = "pod-1"
        pod_list = MagicMock()
        pod_list.items = [pod]

        api.list_namespaced_service.return_value = svc_list
        api.list_namespaced_pod.return_value = pod_list

        result = adapter.get_dependency_graph("ns")
        assert isinstance(result, dict)
        assert "my-svc" in result

    def test_handles_exception(self) -> None:
        api = MagicMock()
        apps_api = MagicMock()
        api.list_namespaced_service.side_effect = Exception("api error")
        adapter = VanillaWhatIfSimulationAdapter(api=api, apps_api=apps_api)
        assert adapter.get_dependency_graph("ns") == {}

    def test_skips_services_without_metadata(self) -> None:
        api = MagicMock()
        apps_api = MagicMock()
        adapter = VanillaWhatIfSimulationAdapter(api=api, apps_api=apps_api)

        svc_no_meta = MagicMock()
        svc_no_meta.metadata = None
        svc_list = MagicMock()
        svc_list.items = [svc_no_meta]

        api.list_namespaced_service.return_value = svc_list

        result = adapter.get_dependency_graph("ns")
        assert result == {}


class TestProbeAudit:
    def test_list_failure_raises(self) -> None:
        api = MagicMock()
        api.list_pod_for_all_namespaces.side_effect = ConnectionError("down")
        apps_api = MagicMock()
        adapter = VanillaWhatIfSimulationAdapter(api=api, apps_api=apps_api)
        with pytest.raises(ClusterUnreachableError):
            adapter.get_probe_audit_data()

    def test_empty_cluster(self) -> None:
        api = MagicMock()
        api.list_pod_for_all_namespaces.return_value = _PodList([])
        apps_api = MagicMock()
        adapter = VanillaWhatIfSimulationAdapter(api=api, apps_api=apps_api)
        assert adapter.get_probe_audit_data() == []

    def test_pod_without_deployment_key_skipped(self) -> None:
        api = MagicMock()
        api.list_pod_for_all_namespaces.return_value = _PodList([_Pod("standalone", "ns", [])])
        apps_api = MagicMock()
        adapter = VanillaWhatIfSimulationAdapter(api=api, apps_api=apps_api)
        result = adapter.get_probe_audit_data()
        assert result == []

    def test_namespace_filter(self) -> None:
        api = MagicMock()
        api.list_pod_for_all_namespaces.return_value = _PodList(
            [
                _Pod("pod-a-abc123", "a", []),
                _Pod("pod-b-abc123", "b", []),
            ]
        )
        apps_api = MagicMock()
        adapter = VanillaWhatIfSimulationAdapter(api=api, apps_api=apps_api)
        result = adapter.get_probe_audit_data(namespace="a")
        assert len(result) == 1
        assert result[0]["namespace"] == "a"

    def test_already_seen_deployment_skipped(self) -> None:
        api = MagicMock()
        api.list_pod_for_all_namespaces.return_value = _PodList(
            [
                _Pod("deploy-abc123-xyz1", "ns", []),
                _Pod("deploy-abc123-xyz2", "ns", []),
            ]
        )
        apps_api = MagicMock()
        adapter = VanillaWhatIfSimulationAdapter(api=api, apps_api=apps_api)
        result = adapter.get_probe_audit_data()
        assert len(result) == 1
        assert result[0]["deployment_name"] == "deploy"
