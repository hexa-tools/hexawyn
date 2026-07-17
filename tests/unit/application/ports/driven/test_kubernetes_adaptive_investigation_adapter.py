from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest
from hexawyn.application.ports.driven.adaptive_investigation_port import AdaptiveInvestigationPort
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    InsufficientPermissionsError,
    ResourceNotFoundError,
)


def _event(name: str, reason: str, message: str, count: int = 1) -> MagicMock:
    event = MagicMock()
    event.involved_object.name = name
    event.reason = reason
    event.message = message
    event.count = count
    return event


def _log_response(text: str) -> MagicMock:
    resp = MagicMock()
    resp.data = text.encode("utf-8")
    return resp


def _pod(restart_count: int = 0, termination_reason: str | None = None) -> MagicMock:
    pod = MagicMock()
    status = MagicMock()
    status.restart_count = restart_count
    if termination_reason:
        status.last_state.terminated.reason = termination_reason
    else:
        status.last_state.terminated = None
    pod.status.container_statuses = [status]
    return pod


class TestKubernetesAdaptiveInvestigationAdapterIsPort:
    def test_is_adaptive_investigation_port(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_adaptive_investigation_adapter import (
            KubernetesAdaptiveInvestigationAdapter,
        )

        assert isinstance(KubernetesAdaptiveInvestigationAdapter(), AdaptiveInvestigationPort)


class TestPodDrillDown:
    def test_returns_events_logs_restart_count(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_adaptive_investigation_adapter import (
            KubernetesAdaptiveInvestigationAdapter,
        )

        core_api = MagicMock()
        core_api.read_namespaced_pod.return_value = _pod(restart_count=45)
        event_list = MagicMock()
        event_list.items = [
            _event("payment-pod-abc", "BackOff", "Back-off restarting failed container", count=10),
            _event("other-pod", "Scheduled", "Successfully assigned"),
        ]
        core_api.list_namespaced_event.return_value = event_list
        core_api.read_namespaced_pod_log.return_value = _log_response(
            "panic: runtime error: invalid memory address\n"
        )

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesAdaptiveInvestigationAdapter()
            result = adapter.investigate_resource("production", "Pod", "payment-pod-abc")

        assert result["restart_count"] == 45
        assert len(result["events"]) == 1
        assert "Back-off" in result["events"][0]
        assert "panic: runtime error" in result["logs"][0]
        assert result["last_termination_reason"] is None

    def test_oomkilled_termination_reason_surfaced(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_adaptive_investigation_adapter import (
            KubernetesAdaptiveInvestigationAdapter,
        )

        core_api = MagicMock()
        core_api.read_namespaced_pod.return_value = _pod(
            restart_count=12, termination_reason="OOMKilled"
        )
        event_list = MagicMock()
        event_list.items = []
        core_api.list_namespaced_event.return_value = event_list
        core_api.read_namespaced_pod_log.return_value = _log_response("")

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesAdaptiveInvestigationAdapter()
            result = adapter.investigate_resource("production", "Pod", "auth-pod-xyz")

        assert result["last_termination_reason"] == "OOMKilled"

    def test_empty_events_investigation_continues(self) -> None:
        """Edge case: pod events empty → investigation continues with
        available data."""
        from hexawyn.adapters.secondary.gitops.kubernetes_adaptive_investigation_adapter import (
            KubernetesAdaptiveInvestigationAdapter,
        )

        core_api = MagicMock()
        core_api.read_namespaced_pod.return_value = _pod(restart_count=1)
        event_list = MagicMock()
        event_list.items = []
        core_api.list_namespaced_event.return_value = event_list
        core_api.read_namespaced_pod_log.return_value = _log_response("still starting up\n")

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesAdaptiveInvestigationAdapter()
            result = adapter.investigate_resource("production", "Pod", "payment-pod-abc")

        assert result["events"] == []
        assert result["logs"] == ["still starting up"]

    def test_pod_not_found_raises_resource_not_found_error(self) -> None:
        """Edge case: resource disappears between overview and drill-down."""
        from hexawyn.adapters.secondary.gitops.kubernetes_adaptive_investigation_adapter import (
            KubernetesAdaptiveInvestigationAdapter,
        )

        core_api = MagicMock()
        not_found = Exception("not found")
        not_found.status = 404  # type: ignore[attr-defined]
        core_api.read_namespaced_pod.side_effect = not_found

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesAdaptiveInvestigationAdapter()
            with pytest.raises(ResourceNotFoundError):
                adapter.investigate_resource("production", "Pod", "ghost-pod")

    def test_cluster_unreachable_translates_other_errors(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_adaptive_investigation_adapter import (
            KubernetesAdaptiveInvestigationAdapter,
        )

        core_api = MagicMock()
        core_api.read_namespaced_pod.side_effect = Exception("connection reset")

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesAdaptiveInvestigationAdapter()
            with pytest.raises(ClusterUnreachableError):
                adapter.investigate_resource("production", "Pod", "payment-pod-abc")

    def test_forbidden_translates_to_insufficient_permissions(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_adaptive_investigation_adapter import (
            KubernetesAdaptiveInvestigationAdapter,
        )

        core_api = MagicMock()
        forbidden = Exception("forbidden")
        forbidden.status = 403  # type: ignore[attr-defined]
        core_api.read_namespaced_pod.side_effect = forbidden

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesAdaptiveInvestigationAdapter()
            with pytest.raises(InsufficientPermissionsError):
                adapter.investigate_resource("production", "Pod", "payment-pod-abc")

    def test_events_fetch_failure_propagates(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_adaptive_investigation_adapter import (
            KubernetesAdaptiveInvestigationAdapter,
        )

        core_api = MagicMock()
        core_api.read_namespaced_pod.return_value = _pod(restart_count=1)
        core_api.read_namespaced_pod_log.return_value = _log_response("ok\n")
        core_api.list_namespaced_event.side_effect = Exception("connection reset")

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesAdaptiveInvestigationAdapter()
            with pytest.raises(ClusterUnreachableError):
                adapter.investigate_resource("production", "Pod", "payment-pod-abc")

    def test_logs_fetch_failure_returns_empty_logs(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_adaptive_investigation_adapter import (
            KubernetesAdaptiveInvestigationAdapter,
        )

        core_api = MagicMock()
        core_api.read_namespaced_pod.return_value = _pod(restart_count=1)
        core_api.read_namespaced_pod_log.side_effect = Exception("connection reset")
        event_list = MagicMock()
        event_list.items = []
        core_api.list_namespaced_event.return_value = event_list

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesAdaptiveInvestigationAdapter()
            result = adapter.investigate_resource("production", "Pod", "payment-pod-abc")

        assert result["logs"] == []


class TestDeploymentDrillDown:
    def test_deployment_kind_skips_logs_and_termination_reason(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_adaptive_investigation_adapter import (
            KubernetesAdaptiveInvestigationAdapter,
        )

        core_api = MagicMock()
        event_list = MagicMock()
        event_list.items = [
            _event("checkout-deploy", "ScalingReplicaSet", "Scaled down replica set"),
        ]
        core_api.list_namespaced_event.return_value = event_list
        apps_api = MagicMock()
        apps_api.read_namespaced_deployment.return_value = MagicMock()

        with (
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
            patch("kubernetes.client.AppsV1Api", return_value=apps_api),
        ):
            adapter = KubernetesAdaptiveInvestigationAdapter()
            result = adapter.investigate_resource("production", "Deployment", "checkout-deploy")

        assert result["logs"] == []
        assert result["last_termination_reason"] is None
        assert result["restart_count"] == 0
        assert len(result["events"]) == 1

    def test_deployment_not_found_raises_resource_not_found_error(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_adaptive_investigation_adapter import (
            KubernetesAdaptiveInvestigationAdapter,
        )

        core_api = MagicMock()
        apps_api = MagicMock()
        not_found = Exception("not found")
        not_found.status = 404  # type: ignore[attr-defined]
        apps_api.read_namespaced_deployment.side_effect = not_found

        with (
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
            patch("kubernetes.client.AppsV1Api", return_value=apps_api),
        ):
            adapter = KubernetesAdaptiveInvestigationAdapter()
            with pytest.raises(ResourceNotFoundError):
                adapter.investigate_resource("production", "Deployment", "ghost-deploy")
