"""Unit tests for KubernetesNamespaceAdapter (mocks kubernetes.client)."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest
from hexawyn.application.ports.driven.namespace_overview_port import NamespaceOverviewPort
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    InsufficientPermissionsError,
    ResourceNotFoundError,
)


def _k8s_error(status: int) -> Exception:
    exc = Exception("k8s error")
    exc.status = status  # type: ignore[attr-defined]
    return exc


def _namespace(phase: str = "Active") -> MagicMock:
    ns = MagicMock()
    ns.status.phase = phase
    return ns


def _pod(name: str, phase: str = "Running", waiting_reason: str | None = None) -> MagicMock:
    pod = MagicMock()
    pod.metadata.name = name
    pod.status.phase = phase
    if waiting_reason:
        container_status = MagicMock()
        container_status.state.waiting.reason = waiting_reason
        pod.status.container_statuses = [container_status]
    else:
        pod.status.container_statuses = []
    return pod


def _deployment(name: str, ready_replicas: int | None, replicas: int | None) -> MagicMock:
    dep = MagicMock()
    dep.metadata.name = name
    dep.status.ready_replicas = ready_replicas
    dep.spec.replicas = replicas
    return dep


def _hpa(name: str, current_replicas: int, max_replicas: int) -> MagicMock:
    hpa = MagicMock()
    hpa.metadata.name = name
    hpa.status.current_replicas = current_replicas
    hpa.spec.max_replicas = max_replicas
    return hpa


def _list(items: list) -> MagicMock:
    result = MagicMock()
    result.items = items
    return result


class TestImplementsPort:
    def test_implements_namespace_overview_port(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_namespace_adapter import (
            KubernetesNamespaceAdapter,
        )

        assert isinstance(KubernetesNamespaceAdapter(), NamespaceOverviewPort)


class TestNamespaceStatus:
    def test_active_status_returned(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_namespace_adapter import (
            KubernetesNamespaceAdapter,
        )

        core_api = MagicMock()
        core_api.read_namespace.return_value = _namespace("Active")
        core_api.list_namespaced_pod.return_value = _list([])
        core_api.list_namespaced_service.return_value = _list([])
        apps_api = MagicMock()
        apps_api.list_namespaced_deployment.return_value = _list([])
        autoscaling_api = MagicMock()
        autoscaling_api.list_namespaced_horizontal_pod_autoscaler.return_value = _list([])

        with (
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
            patch("kubernetes.client.AppsV1Api", return_value=apps_api),
            patch("kubernetes.client.AutoscalingV2Api", return_value=autoscaling_api),
        ):
            data = KubernetesNamespaceAdapter().get_namespace_overview_data("staging")

        assert data["namespace_status"] == "Active"

    def test_terminating_status_returned(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_namespace_adapter import (
            KubernetesNamespaceAdapter,
        )

        core_api = MagicMock()
        core_api.read_namespace.return_value = _namespace("Terminating")
        core_api.list_namespaced_pod.return_value = _list([])
        core_api.list_namespaced_service.return_value = _list([])
        apps_api = MagicMock()
        apps_api.list_namespaced_deployment.return_value = _list([])
        autoscaling_api = MagicMock()
        autoscaling_api.list_namespaced_horizontal_pod_autoscaler.return_value = _list([])

        with (
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
            patch("kubernetes.client.AppsV1Api", return_value=apps_api),
            patch("kubernetes.client.AutoscalingV2Api", return_value=autoscaling_api),
        ):
            data = KubernetesNamespaceAdapter().get_namespace_overview_data("staging")

        assert data["namespace_status"] == "Terminating"


class TestPodStatus:
    def test_waiting_reason_takes_priority_over_phase(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_namespace_adapter import (
            KubernetesNamespaceAdapter,
        )

        core_api = MagicMock()
        core_api.read_namespace.return_value = _namespace()
        core_api.list_namespaced_pod.return_value = _list(
            [_pod("checkout-pod-abc", phase="Running", waiting_reason="CrashLoopBackOff")]
        )
        core_api.list_namespaced_service.return_value = _list([])
        apps_api = MagicMock()
        apps_api.list_namespaced_deployment.return_value = _list([])
        autoscaling_api = MagicMock()
        autoscaling_api.list_namespaced_horizontal_pod_autoscaler.return_value = _list([])

        with (
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
            patch("kubernetes.client.AppsV1Api", return_value=apps_api),
            patch("kubernetes.client.AutoscalingV2Api", return_value=autoscaling_api),
        ):
            data = KubernetesNamespaceAdapter().get_namespace_overview_data("staging")

        assert data["pods"][0]["status"] == "CrashLoopBackOff"

    def test_phase_used_when_no_waiting_reason(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_namespace_adapter import (
            KubernetesNamespaceAdapter,
        )

        core_api = MagicMock()
        core_api.read_namespace.return_value = _namespace()
        core_api.list_namespaced_pod.return_value = _list([_pod("pod-a", phase="Running")])
        core_api.list_namespaced_service.return_value = _list([])
        apps_api = MagicMock()
        apps_api.list_namespaced_deployment.return_value = _list([])
        autoscaling_api = MagicMock()
        autoscaling_api.list_namespaced_horizontal_pod_autoscaler.return_value = _list([])

        with (
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
            patch("kubernetes.client.AppsV1Api", return_value=apps_api),
            patch("kubernetes.client.AutoscalingV2Api", return_value=autoscaling_api),
        ):
            data = KubernetesNamespaceAdapter().get_namespace_overview_data("staging")

        assert data["pods"][0]["status"] == "Running"


class TestDeploymentsServicesHpas:
    def test_deployment_ready_and_desired_extracted(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_namespace_adapter import (
            KubernetesNamespaceAdapter,
        )

        core_api = MagicMock()
        core_api.read_namespace.return_value = _namespace()
        core_api.list_namespaced_pod.return_value = _list([])
        core_api.list_namespaced_service.return_value = _list([MagicMock(), MagicMock()])
        apps_api = MagicMock()
        apps_api.list_namespaced_deployment.return_value = _list(
            [_deployment("payment-deploy", ready_replicas=0, replicas=2)]
        )
        autoscaling_api = MagicMock()
        autoscaling_api.list_namespaced_horizontal_pod_autoscaler.return_value = _list([])

        with (
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
            patch("kubernetes.client.AppsV1Api", return_value=apps_api),
            patch("kubernetes.client.AutoscalingV2Api", return_value=autoscaling_api),
        ):
            data = KubernetesNamespaceAdapter().get_namespace_overview_data("staging")

        assert data["deployments"][0] == {
            "name": "payment-deploy",
            "ready_replicas": 0,
            "desired_replicas": 2,
        }
        assert data["services_count"] == 2

    def test_deployment_none_replicas_default_to_zero(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_namespace_adapter import (
            KubernetesNamespaceAdapter,
        )

        core_api = MagicMock()
        core_api.read_namespace.return_value = _namespace()
        core_api.list_namespaced_pod.return_value = _list([])
        core_api.list_namespaced_service.return_value = _list([])
        apps_api = MagicMock()
        apps_api.list_namespaced_deployment.return_value = _list(
            [_deployment("fresh-deploy", ready_replicas=None, replicas=None)]
        )
        autoscaling_api = MagicMock()
        autoscaling_api.list_namespaced_horizontal_pod_autoscaler.return_value = _list([])

        with (
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
            patch("kubernetes.client.AppsV1Api", return_value=apps_api),
            patch("kubernetes.client.AutoscalingV2Api", return_value=autoscaling_api),
        ):
            data = KubernetesNamespaceAdapter().get_namespace_overview_data("staging")

        assert data["deployments"][0]["ready_replicas"] == 0
        assert data["deployments"][0]["desired_replicas"] == 0

    def test_hpa_current_and_max_extracted(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_namespace_adapter import (
            KubernetesNamespaceAdapter,
        )

        core_api = MagicMock()
        core_api.read_namespace.return_value = _namespace()
        core_api.list_namespaced_pod.return_value = _list([])
        core_api.list_namespaced_service.return_value = _list([])
        apps_api = MagicMock()
        apps_api.list_namespaced_deployment.return_value = _list([])
        autoscaling_api = MagicMock()
        autoscaling_api.list_namespaced_horizontal_pod_autoscaler.return_value = _list(
            [_hpa("checkout-hpa", current_replicas=10, max_replicas=10)]
        )

        with (
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
            patch("kubernetes.client.AppsV1Api", return_value=apps_api),
            patch("kubernetes.client.AutoscalingV2Api", return_value=autoscaling_api),
        ):
            data = KubernetesNamespaceAdapter().get_namespace_overview_data("staging")

        assert data["hpas"][0] == {
            "name": "checkout-hpa",
            "current_replicas": 10,
            "max_replicas": 10,
        }


class TestNamespaceLookupErrors:
    def test_namespace_not_found_raises_resource_not_found(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_namespace_adapter import (
            KubernetesNamespaceAdapter,
        )

        core_api = MagicMock()
        core_api.read_namespace.side_effect = _k8s_error(404)

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            with pytest.raises(ResourceNotFoundError):
                KubernetesNamespaceAdapter().get_namespace_overview_data("ghost")

    def test_rbac_denied_raises_insufficient_permissions(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_namespace_adapter import (
            KubernetesNamespaceAdapter,
        )

        core_api = MagicMock()
        core_api.read_namespace.side_effect = _k8s_error(403)

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            with pytest.raises(InsufficientPermissionsError):
                KubernetesNamespaceAdapter().get_namespace_overview_data("secret-ns")

    def test_other_error_raises_cluster_unreachable(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_namespace_adapter import (
            KubernetesNamespaceAdapter,
        )

        core_api = MagicMock()
        core_api.read_namespace.side_effect = _k8s_error(500)

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            with pytest.raises(ClusterUnreachableError):
                KubernetesNamespaceAdapter().get_namespace_overview_data("staging")
