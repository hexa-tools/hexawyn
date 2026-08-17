# mypy: ignore-errors
"""Integration tests: GetNamespaceResourceAllocationUseCase → VanillaAdapter → mocked K8s API."""

from unittest.mock import MagicMock

import pytest
from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter
from hexawyn.application.use_case.cluster.get_namespace_resource_allocation.command import (
    GetNamespaceResourceAllocationCommand,
)
from hexawyn.application.use_case.cluster.get_namespace_resource_allocation.get_namespace_resource_allocation_use_case import (  # noqa: E501
    GetNamespaceResourceAllocationUseCase,
)


def _container(cpu: str | None = "500m", memory: str | None = "1Gi") -> MagicMock:
    c = MagicMock()
    requests: dict[str, str] = {}
    if cpu:
        requests["cpu"] = cpu
    if memory:
        requests["memory"] = memory
    c.resources.requests = requests or None
    return c


def _pod(namespace: str, cpu: str | None = "500m", memory: str | None = "1Gi") -> MagicMock:
    from datetime import UTC, datetime, timedelta

    pod = MagicMock()
    pod.metadata.namespace = namespace
    pod.metadata.creation_timestamp = datetime.now(UTC) - timedelta(days=30)
    pod.spec.containers = [_container(cpu, memory)]
    return pod


def _fake_core_api(pods: list[MagicMock]) -> MagicMock:
    api = MagicMock()
    pod_list = MagicMock()
    pod_list.items = pods
    api.list_pod_for_all_namespaces.return_value = pod_list
    return api


def _build_use_case(api: MagicMock) -> GetNamespaceResourceAllocationUseCase:
    adapter = VanillaAdapter("test-cluster", api=api)
    return GetNamespaceResourceAllocationUseCase(k8s_port=adapter)


@pytest.mark.integration
class TestGetNamespaceResourceAllocationIntegration:
    def test_vanilla_adapter_implements_k8s_port(self) -> None:
        from hexawyn.application.ports.driven.k8s_port import K8sPort

        assert isinstance(VanillaAdapter("test"), K8sPort)

    def test_multiple_namespaces_ranked_by_cpu_descending(self) -> None:
        pods = [
            _pod("production", cpu="3000m", memory="6Gi"),
            _pod("staging", cpu="4000m", memory="8Gi"),
            _pod("monitoring", cpu="2000m", memory="4Gi"),
        ]
        api = _fake_core_api(pods)

        use_case = _build_use_case(api)
        result = use_case.execute(GetNamespaceResourceAllocationCommand())

        assert len(result.allocations) == 3  # noqa: PLR2004
        assert result.allocations[0]["namespace"] == "staging"
        assert result.allocations[0]["total_cpu_cores"] == 4.0  # noqa: PLR2004
        assert result.allocations[0]["total_memory_gb"] == 8.0  # noqa: PLR2004
        assert result.allocations[0]["pod_count"] == 1
        assert result.allocations[1]["namespace"] == "production"
        assert result.allocations[1]["total_cpu_cores"] == 3.0  # noqa: PLR2004
        assert result.allocations[2]["namespace"] == "monitoring"
        assert result.allocations[2]["total_cpu_cores"] == 2.0  # noqa: PLR2004

    def test_no_resource_requests_treated_as_zero(self) -> None:
        pods = [
            _pod("bare-ns", cpu=None, memory=None),
            _pod("rich-ns", cpu="2000m", memory="4Gi"),
        ]
        api = _fake_core_api(pods)

        use_case = _build_use_case(api)
        result = use_case.execute(GetNamespaceResourceAllocationCommand())

        assert len(result.allocations) == 2  # noqa: PLR2004
        bare = next(a for a in result.allocations if a["namespace"] == "bare-ns")
        rich = next(a for a in result.allocations if a["namespace"] == "rich-ns")
        assert bare["total_cpu_cores"] == 0.0
        assert bare["total_memory_gb"] == 0.0
        assert bare["pod_count"] == 1
        assert rich["total_cpu_cores"] == 2.0  # noqa: PLR2004
        assert rich["total_memory_gb"] == 4.0  # noqa: PLR2004

    def test_empty_cluster_returns_empty_allocations(self) -> None:
        api = _fake_core_api([])

        use_case = _build_use_case(api)
        result = use_case.execute(GetNamespaceResourceAllocationCommand())

        assert result.allocations == []

    def test_single_namespace_multiple_pods_aggregates(self) -> None:
        pods = [
            _pod("production", cpu="1000m", memory="1Gi"),
            _pod("production", cpu="2000m", memory="2Gi"),
            _pod("production", cpu="500m", memory="512Mi"),
        ]
        api = _fake_core_api(pods)

        use_case = _build_use_case(api)
        result = use_case.execute(GetNamespaceResourceAllocationCommand())

        assert len(result.allocations) == 1  # noqa: PLR2004
        assert result.allocations[0]["namespace"] == "production"
        assert result.allocations[0]["total_cpu_cores"] == 3.5  # noqa: PLR2004
        assert result.allocations[0]["pod_count"] == 3  # noqa: PLR2004

    def test_tied_cpu_returns_both_namespaces(self) -> None:
        pods = [
            _pod("ns-a", cpu="2000m", memory="1Gi"),
            _pod("ns-b", cpu="2000m", memory="4Gi"),
        ]
        api = _fake_core_api(pods)

        use_case = _build_use_case(api)
        result = use_case.execute(GetNamespaceResourceAllocationCommand())

        assert len(result.allocations) == 2  # noqa: PLR2004
        assert result.allocations[0]["total_cpu_cores"] == 2.0  # noqa: PLR2004
        assert result.allocations[1]["total_cpu_cores"] == 2.0  # noqa: PLR2004

    def test_conversion_millicores_to_cores_precise(self) -> None:
        pods = [
            _pod("ns", cpu="2500m", memory="5120Mi"),
        ]
        api = _fake_core_api(pods)

        use_case = _build_use_case(api)
        result = use_case.execute(GetNamespaceResourceAllocationCommand())

        assert result.allocations[0]["total_cpu_cores"] == 2.5  # noqa: PLR2004
        assert result.allocations[0]["total_memory_gb"] == 5.0  # noqa: PLR2004
