from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest
from hexawyn.adapters.secondary.gitops.kubernetes_adaptive_investigation_adapter import (
    KubernetesAdaptiveInvestigationAdapter,
    _extract_container_status,
    _translate_error,
)
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    InsufficientPermissionsError,
    ResourceNotFoundError,
)


class TestKubernetesAdaptiveInvestigationAdapter:
    def test_investigate_resource_pod_success(self) -> None:
        adapter = KubernetesAdaptiveInvestigationAdapter()
        mock_pod = MagicMock()
        mock_pod.status.container_statuses = []

        mock_core = MagicMock()
        mock_core.read_namespaced_pod.return_value = mock_pod
        mock_core.list_namespaced_event.return_value = MagicMock(items=[])
        mock_response = MagicMock()
        mock_response.data = b"log line 1\nlog line 2\n"
        mock_core.read_namespaced_pod_log.return_value = mock_response

        with patch("kubernetes.client.CoreV1Api", return_value=mock_core):
            result = adapter.investigate_resource("default", "Pod", "my-pod")

            assert isinstance(result["events"], list)
            assert isinstance(result["logs"], list)
            assert isinstance(result["restart_count"], int)

    def test_investigate_resource_deployment_verifies_and_returns(self) -> None:
        adapter = KubernetesAdaptiveInvestigationAdapter()

        mock_core = MagicMock()
        mock_core.list_namespaced_event.return_value = MagicMock(items=[])
        mock_apps = MagicMock()
        mock_apps.read_namespaced_deployment.return_value = MagicMock()

        with patch("kubernetes.client.CoreV1Api", return_value=mock_core):
            with patch("kubernetes.client.AppsV1Api", return_value=mock_apps):
                result = adapter.investigate_resource("default", "Deployment", "my-deploy")

                assert result["logs"] == []
                assert result["restart_count"] == 0

    def test_investigate_pod_returns_restart_count_and_logs(self) -> None:
        adapter = KubernetesAdaptiveInvestigationAdapter()
        mock_pod = MagicMock()
        mock_status = MagicMock()
        mock_status.restart_count = 3
        mock_status.last_state = MagicMock()
        mock_status.last_state.terminated = None
        mock_pod.status.container_statuses = [mock_status]

        mock_core = MagicMock()
        mock_core.read_namespaced_pod.return_value = mock_pod
        mock_core.read_namespaced_pod_log.return_value = MagicMock(data=b"log content\n")

        import kubernetes.client as k8s_mod

        restart_count, termination_reason, logs = adapter._investigate_pod(
            k8s_mod, mock_core, "default", "my-pod"
        )

        assert restart_count == 3  # noqa: PLR2004
        assert isinstance(logs, list)

    def test_verify_deployment_exists_not_found_raises(self) -> None:
        adapter = KubernetesAdaptiveInvestigationAdapter()

        class NotFoundError(Exception):
            status = 404

        mock_apps = MagicMock()
        mock_apps.read_namespaced_deployment.side_effect = NotFoundError("not found")

        with patch("kubernetes.client.AppsV1Api", return_value=mock_apps):
            import kubernetes.client as k8s_mod

            with pytest.raises(ResourceNotFoundError):
                adapter._verify_deployment_exists(k8s_mod, "default", "missing-deploy")

    def test_fetch_events_returns_formatted_strings(self) -> None:
        adapter = KubernetesAdaptiveInvestigationAdapter()
        mock_event = MagicMock()
        mock_event.involved_object.name = "my-pod"
        mock_event.reason = "OOMKilled"
        mock_event.message = "Container was OOMKilled"
        mock_event.count = 2

        mock_core = MagicMock()
        mock_core.list_namespaced_event.return_value = MagicMock(items=[mock_event])

        events = adapter._fetch_events(mock_core, "default", "my-pod")

        assert len(events) == 1
        assert "OOMKilled" in events[0]
        assert "x2" in events[0]

    def test_fetch_events_limit_max(self) -> None:
        adapter = KubernetesAdaptiveInvestigationAdapter()

        mock_core = MagicMock()
        items = []
        for i in range(10):
            event = MagicMock()
            event.involved_object.name = "my-pod"
            event.reason = f"Event{i}"
            event.message = f"msg {i}"
            event.count = 1
            items.append(event)
        mock_core.list_namespaced_event.return_value = MagicMock(items=items)

        events = adapter._fetch_events(mock_core, "default", "my-pod")

        assert len(events) == 5  # noqa: PLR2004

    def test_fetch_logs_returns_lines(self) -> None:
        adapter = KubernetesAdaptiveInvestigationAdapter()
        mock_core = MagicMock()
        mock_response = MagicMock()
        mock_response.data = b"line 1\nline 2\n  \nline 3\n"
        mock_core.read_namespaced_pod_log.return_value = mock_response

        logs = adapter._fetch_logs(mock_core, "default", "my-pod")

        assert len(logs) == 3  # noqa: PLR2004
        assert "line 1" in logs[0]

    def test_fetch_logs_returns_empty_on_exception(self) -> None:
        adapter = KubernetesAdaptiveInvestigationAdapter()
        mock_core = MagicMock()
        mock_core.read_namespaced_pod_log.side_effect = RuntimeError("fail")

        logs = adapter._fetch_logs(mock_core, "default", "my-pod")

        assert logs == []

    def test_fetch_events_error_raises_translated(self) -> None:
        adapter = KubernetesAdaptiveInvestigationAdapter()

        class NotFoundError(Exception):
            status = 404

        mock_core = MagicMock()
        mock_core.list_namespaced_event.side_effect = NotFoundError("not found")

        with pytest.raises(ResourceNotFoundError):
            adapter._fetch_events(mock_core, "default", "my-pod")


class TestExtractContainerStatus:
    def test_extracts_restart_and_terminated_reason(self) -> None:
        mock_pod = MagicMock()
        mock_status1 = MagicMock()
        mock_status1.restart_count = 2
        mock_status1.last_state.terminated = None
        mock_status2 = MagicMock()
        mock_status2.restart_count = 1
        terminated = MagicMock()
        terminated.reason = "OOMKilled"
        mock_status2.last_state.terminated = terminated
        mock_pod.status.container_statuses = [mock_status1, mock_status2]

        restart, reason = _extract_container_status(mock_pod)

        assert restart == 3  # noqa: PLR2004
        assert reason == "OOMKilled"

    def test_no_container_statuses_returns_defaults(self) -> None:
        mock_pod = MagicMock()
        mock_pod.status.container_statuses = None

        restart, reason = _extract_container_status(mock_pod)

        assert restart == 0
        assert reason is None


class TestTranslateError:
    def test_not_found(self) -> None:
        class Exc(Exception):  # noqa: N818
            status = 404

        result = _translate_error(Exc(), "ns", "resource")
        assert isinstance(result, ResourceNotFoundError)

    def test_forbidden(self) -> None:
        class Exc(Exception):  # noqa: N818
            status = 403

        result = _translate_error(Exc(), "ns", "resource")
        assert isinstance(result, InsufficientPermissionsError)

    def test_other(self) -> None:
        result = _translate_error(Exception("boom"), "ns", "resource")
        assert isinstance(result, ClusterUnreachableError)
