from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driven.k8s_port import PodInfo
from hexawyn.application.use_case.cluster.get_namespace_resource_allocation import (
    GetNamespaceResourceAllocationUseCase,
)
from hexawyn.application.use_case.cluster.get_namespace_resource_allocation.command import (
    GetNamespaceResourceAllocationCommand,
)
from hexawyn.application.use_case.cluster.get_namespace_resource_allocation.response import (
    GetNamespaceResourceAllocationResponse,
)


class TestGetNamespaceResourceAllocationUseCase:
    def _make_pod(
        self,
        namespace: str,
        name: str = "test-pod",
        cpu_millicores: int | None = None,
        memory_mib: int | None = None,
    ) -> PodInfo:
        pod: PodInfo = {"name": name, "namespace": namespace, "status": "Running"}
        if cpu_millicores is not None:
            pod["cpu_request_millicores"] = cpu_millicores
        if memory_mib is not None:
            pod["memory_request_mib"] = memory_mib
        return pod

    def test_imports_exist(self) -> None:
        assert GetNamespaceResourceAllocationCommand is not None
        assert GetNamespaceResourceAllocationUseCase is not None
        assert GetNamespaceResourceAllocationResponse is not None

    def test_empty_cluster_returns_empty_allocations(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_pods.return_value = []

        use_case = GetNamespaceResourceAllocationUseCase(k8s_port=k8s_port)
        result = use_case.execute(GetNamespaceResourceAllocationCommand())

        assert isinstance(result.allocations, list)
        assert len(result.allocations) == 0

    def test_single_namespace_single_pod_returns_single_entry(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_pods.return_value = [
            self._make_pod("staging", "pod-1", cpu_millicores=2000, memory_mib=4096),
        ]

        use_case = GetNamespaceResourceAllocationUseCase(k8s_port=k8s_port)
        result = use_case.execute(GetNamespaceResourceAllocationCommand())

        assert len(result.allocations) == 1  # noqa: PLR2004
        allocation = result.allocations[0]
        assert allocation["namespace"] == "staging"
        assert allocation["total_cpu_cores"] == 2.0  # noqa: PLR2004
        assert allocation["total_memory_gb"] == 4.0  # noqa: PLR2004
        assert allocation["pod_count"] == 1

    def test_multiple_pods_same_namespace_aggregates_correctly(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_pods.return_value = [
            self._make_pod("production", "pod-a", cpu_millicores=1000, memory_mib=1024),
            self._make_pod("production", "pod-b", cpu_millicores=2000, memory_mib=2048),
            self._make_pod("production", "pod-c", cpu_millicores=500, memory_mib=512),
        ]

        use_case = GetNamespaceResourceAllocationUseCase(k8s_port=k8s_port)
        result = use_case.execute(GetNamespaceResourceAllocationCommand())

        assert len(result.allocations) == 1  # noqa: PLR2004
        allocation = result.allocations[0]
        assert allocation["namespace"] == "production"
        assert allocation["total_cpu_cores"] == 3.5  # noqa: PLR2004
        assert allocation["total_memory_gb"] == pytest.approx(3.5, abs=0.01)
        assert allocation["pod_count"] == 3  # noqa: PLR2004

    def test_multiple_namespaces_ranked_by_cpu_descending(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_pods.return_value = [
            self._make_pod("staging", "pod-1", cpu_millicores=4000, memory_mib=8192),
            self._make_pod("production", "pod-2", cpu_millicores=3000, memory_mib=6144),
            self._make_pod("monitoring", "pod-3", cpu_millicores=2000, memory_mib=4096),
        ]

        use_case = GetNamespaceResourceAllocationUseCase(k8s_port=k8s_port)
        result = use_case.execute(GetNamespaceResourceAllocationCommand())

        assert len(result.allocations) == 3  # noqa: PLR2004
        assert result.allocations[0]["namespace"] == "staging"
        assert result.allocations[0]["total_cpu_cores"] == 4.0  # noqa: PLR2004
        assert result.allocations[1]["namespace"] == "production"
        assert result.allocations[1]["total_cpu_cores"] == 3.0  # noqa: PLR2004
        assert result.allocations[2]["namespace"] == "monitoring"
        assert result.allocations[2]["total_cpu_cores"] == 2.0  # noqa: PLR2004

    def test_pods_without_resource_requests_treated_as_zero(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_pods.return_value = [
            self._make_pod("no-requests-ns", "pod-bare"),
            self._make_pod("with-requests-ns", "pod-with", cpu_millicores=1000, memory_mib=1024),
        ]

        use_case = GetNamespaceResourceAllocationUseCase(k8s_port=k8s_port)
        result = use_case.execute(GetNamespaceResourceAllocationCommand())

        assert len(result.allocations) == 2  # noqa: PLR2004
        bare_ns = next(a for a in result.allocations if a["namespace"] == "no-requests-ns")
        assert bare_ns["total_cpu_cores"] == 0.0
        assert bare_ns["total_memory_gb"] == 0.0
        assert bare_ns["pod_count"] == 1

    def test_pod_missing_namespace_skipped(self) -> None:
        k8s_port = MagicMock()
        pod_without_ns: PodInfo = {"name": "orphan-pod", "status": "Running"}
        k8s_port.list_pods.return_value = [
            pod_without_ns,
            self._make_pod("valid-ns", "ok-pod", cpu_millicores=500, memory_mib=512),
        ]

        use_case = GetNamespaceResourceAllocationUseCase(k8s_port=k8s_port)
        result = use_case.execute(GetNamespaceResourceAllocationCommand())

        assert len(result.allocations) == 1  # noqa: PLR2004
        assert result.allocations[0]["namespace"] == "valid-ns"

    def test_zero_cpu_and_zero_memory_converted_correctly(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_pods.return_value = [
            self._make_pod("zero-ns", "zero-pod", cpu_millicores=0, memory_mib=0),
        ]

        use_case = GetNamespaceResourceAllocationUseCase(k8s_port=k8s_port)
        result = use_case.execute(GetNamespaceResourceAllocationCommand())

        assert len(result.allocations) == 1  # noqa: PLR2004
        assert result.allocations[0]["total_cpu_cores"] == 0.0
        assert result.allocations[0]["total_memory_gb"] == 0.0
        assert result.allocations[0]["pod_count"] == 1

    def test_tied_cpu_sorted_stable(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_pods.return_value = [
            self._make_pod("ns-a", "pod-a", cpu_millicores=2000, memory_mib=1024),
            self._make_pod("ns-b", "pod-b", cpu_millicores=2000, memory_mib=2048),
        ]

        use_case = GetNamespaceResourceAllocationUseCase(k8s_port=k8s_port)
        result = use_case.execute(GetNamespaceResourceAllocationCommand())

        assert len(result.allocations) == 2  # noqa: PLR2004
        assert result.allocations[0]["total_cpu_cores"] == 2.0  # noqa: PLR2004
        assert result.allocations[1]["total_cpu_cores"] == 2.0  # noqa: PLR2004
