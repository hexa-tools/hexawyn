from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driven.k8s_port import PodInfo
from hexawyn.application.use_case.workloads.list_pods.command import ListPodsCommand
from hexawyn.application.use_case.workloads.list_pods.list_pods_use_case import (
    ListPodsUseCase,
)
from hexawyn.application.use_case.workloads.list_pods.response import ListPodsResponse


class TestListPodsUseCase:
    def test_execute_returns_list_pods_response(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_pods.return_value = []

        use_case = ListPodsUseCase(k8s_port=k8s_port)
        result = use_case.execute(ListPodsCommand(namespace="default"))

        assert isinstance(result, ListPodsResponse)

    def test_execute_returns_pods_from_port(self) -> None:
        expected_pod: PodInfo = {
            "name": "nginx",
            "namespace": "default",
            "status": "Running",
            "restarts": 0,
            "age": "5d",
        }
        k8s_port = MagicMock()
        k8s_port.list_pods.return_value = [expected_pod]

        use_case = ListPodsUseCase(k8s_port=k8s_port)
        result = use_case.execute(ListPodsCommand(namespace="default"))

        assert len(result.pods) == 1
        assert result.pods[0]["name"] == "nginx"

    def test_execute_passes_namespace_to_port(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_pods.return_value = []

        use_case = ListPodsUseCase(k8s_port=k8s_port)
        use_case.execute(ListPodsCommand(namespace="production"))

        k8s_port.list_pods.assert_called_once_with(namespace="production")

    def test_execute_sorts_unhealthy_pods_first(self) -> None:
        crash_pod: PodInfo = {
            "name": "crash",
            "status": "CrashLoopBackOff",
            "namespace": "default",
            "restarts": 10,
            "age": "1h",
        }
        running_pod: PodInfo = {
            "name": "nginx",
            "status": "Running",
            "namespace": "default",
            "restarts": 0,
            "age": "30d",
        }
        k8s_port = MagicMock()
        k8s_port.list_pods.return_value = [running_pod, crash_pod]

        use_case = ListPodsUseCase(k8s_port=k8s_port)
        result = use_case.execute(ListPodsCommand(namespace="default"))

        assert result.pods[0]["name"] == "crash"
        assert result.pods[1]["name"] == "nginx"

    def test_execute_preserves_sort_stability_for_same_severity(self) -> None:
        crash_a: PodInfo = {
            "name": "a-crash",
            "status": "CrashLoop",
            "namespace": "default",
            "restarts": 5,
            "age": "1h",
        }
        crash_b: PodInfo = {
            "name": "b-crash",
            "status": "CrashLoop",
            "namespace": "default",
            "restarts": 3,
            "age": "2h",
        }
        k8s_port = MagicMock()
        k8s_port.list_pods.return_value = [crash_b, crash_a]

        use_case = ListPodsUseCase(k8s_port=k8s_port)
        result = use_case.execute(ListPodsCommand(namespace="default"))

        assert result.pods[0]["name"] == "a-crash"
        assert result.pods[1]["name"] == "b-crash"

    def test_execute_with_all_healthy_pods_no_sort_change(self) -> None:
        pod_a: PodInfo = {
            "name": "a",
            "status": "Running",
            "namespace": "ns",
            "restarts": 0,
            "age": "1d",
        }
        pod_b: PodInfo = {
            "name": "b",
            "status": "Running",
            "namespace": "ns",
            "restarts": 0,
            "age": "2d",
        }
        k8s_port = MagicMock()
        k8s_port.list_pods.return_value = [pod_b, pod_a]

        use_case = ListPodsUseCase(k8s_port=k8s_port)
        result = use_case.execute(ListPodsCommand(namespace="ns"))

        assert result.pods[0]["name"] == "a"
        assert result.pods[1]["name"] == "b"
