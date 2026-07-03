"""Unit tests for KubernetesPodLogSearchAdapter (mocks kubernetes.client)."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest
from hexawyn.application.ports.driven.log_search_port import LogSearchPort
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    InsufficientPermissionsError,
    ResourceNotFoundError,
)


def _response(text: str) -> MagicMock:
    resp = MagicMock()
    resp.data = text.encode("utf-8")
    return resp


def _pod(container_names: list[str]) -> MagicMock:
    pod = MagicMock()
    pod.spec.containers = [MagicMock(name=name) for name in container_names]
    for container, name in zip(pod.spec.containers, container_names, strict=True):
        container.name = name
    return pod


def _k8s_error(status: int) -> Exception:
    exc = Exception("k8s error")
    exc.status = status  # type: ignore[attr-defined]
    return exc


class TestImplementsPort:
    def test_implements_log_search_port(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
            KubernetesPodLogSearchAdapter,
        )

        assert isinstance(KubernetesPodLogSearchAdapter(), LogSearchPort)


class TestSingleContainer:
    def test_returns_lines_for_one_container(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
            KubernetesPodLogSearchAdapter,
        )

        core_api = MagicMock()
        core_api.read_namespaced_pod.return_value = _pod(["app"])
        core_api.read_namespaced_pod_log.return_value = _response(
            "2024-01-01T10:32:15Z connection refused to postgres\n"
        )

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            results = KubernetesPodLogSearchAdapter().fetch_pod_container_logs(
                "checkout-pod-abc12", "production", time_window_minutes=60
            )

        assert len(results) == 1
        assert results[0]["container"] == "app"
        assert "connection refused to postgres" in results[0]["lines"][0]

    def test_tail_lines_passed_through(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
            KubernetesPodLogSearchAdapter,
        )

        core_api = MagicMock()
        core_api.read_namespaced_pod.return_value = _pod(["app"])
        core_api.read_namespaced_pod_log.return_value = _response("line\n")

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            KubernetesPodLogSearchAdapter().fetch_pod_container_logs(
                "checkout-pod-abc12", "production", time_window_minutes=60
            )

        _, kwargs = core_api.read_namespaced_pod_log.call_args
        assert kwargs["tail_lines"] == 5000
        assert kwargs["since_seconds"] == 3600
        assert kwargs["container"] == "app"


class TestMultipleContainers:
    def test_each_container_fetched_separately(self) -> None:
        """TC4: pattern matches in multiple containers of the same pod."""
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
            KubernetesPodLogSearchAdapter,
        )

        core_api = MagicMock()
        core_api.read_namespaced_pod.return_value = _pod(["app", "sidecar"])
        core_api.read_namespaced_pod_log.return_value = _response("connection refused\n")

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            results = KubernetesPodLogSearchAdapter().fetch_pod_container_logs(
                "checkout-pod-abc12", "production", time_window_minutes=60
            )

        assert {result["container"] for result in results} == {"app", "sidecar"}
        assert core_api.read_namespaced_pod_log.call_count == 2


class TestBinaryData:
    def test_undecodable_bytes_replaced_not_raised(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
            KubernetesPodLogSearchAdapter,
        )

        core_api = MagicMock()
        core_api.read_namespaced_pod.return_value = _pod(["app"])
        response = MagicMock()
        response.data = b"2024-01-01T10:00:00Z valid \xff\xfe binary garbage"
        core_api.read_namespaced_pod_log.return_value = response

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            results = KubernetesPodLogSearchAdapter().fetch_pod_container_logs(
                "pod-a", "production", time_window_minutes=60
            )

        assert len(results[0]["lines"]) == 1


class TestNoLogsAvailable:
    def test_container_log_fetch_failure_returns_empty_not_raise(self) -> None:
        """Edge case: pod has completed/evicted (no live logs) → handled gracefully."""
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
            KubernetesPodLogSearchAdapter,
        )

        core_api = MagicMock()
        core_api.read_namespaced_pod.return_value = _pod(["app"])
        core_api.read_namespaced_pod_log.side_effect = _k8s_error(400)

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            results = KubernetesPodLogSearchAdapter().fetch_pod_container_logs(
                "evicted-pod", "production", time_window_minutes=60
            )

        assert results == [{"container": "app", "lines": [], "truncated": False}]


class TestPodLookupErrors:
    def test_pod_not_found_raises_resource_not_found(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
            KubernetesPodLogSearchAdapter,
        )

        core_api = MagicMock()
        core_api.read_namespaced_pod.side_effect = _k8s_error(404)

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            with pytest.raises(ResourceNotFoundError):
                KubernetesPodLogSearchAdapter().fetch_pod_container_logs(
                    "gone-pod", "production", time_window_minutes=60
                )

    def test_rbac_denied_raises_insufficient_permissions(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
            KubernetesPodLogSearchAdapter,
        )

        core_api = MagicMock()
        core_api.read_namespaced_pod.side_effect = _k8s_error(403)

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            with pytest.raises(InsufficientPermissionsError):
                KubernetesPodLogSearchAdapter().fetch_pod_container_logs(
                    "secret-pod", "production", time_window_minutes=60
                )

    def test_other_error_raises_cluster_unreachable(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
            KubernetesPodLogSearchAdapter,
        )

        core_api = MagicMock()
        core_api.read_namespaced_pod.side_effect = _k8s_error(500)

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            with pytest.raises(ClusterUnreachableError):
                KubernetesPodLogSearchAdapter().fetch_pod_container_logs(
                    "pod-a", "production", time_window_minutes=60
                )
