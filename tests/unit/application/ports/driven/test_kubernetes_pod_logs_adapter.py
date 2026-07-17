from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest
from hexawyn.application.ports.driven.pod_logs_port import PodLogsPort
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    InsufficientPermissionsError,
    ResourceNotFoundError,
)
from hexawyn.domain.models.analyze_pod_logs import AnalyzePodLogsRequest


def _response(text: str) -> MagicMock:
    resp = MagicMock()
    resp.data = text.encode("utf-8")
    return resp


def _pod(restart_count: int = 0) -> MagicMock:
    pod = MagicMock()
    container_status = MagicMock()
    container_status.restart_count = restart_count
    pod.status.container_statuses = [container_status]
    return pod


class TestKubernetesPodLogsAdapterIsPort:
    def test_is_pod_logs_port(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_logs_adapter import (
            KubernetesPodLogsAdapter,
        )

        assert isinstance(KubernetesPodLogsAdapter(), PodLogsPort)


class TestKubernetesPodLogsAdapterHappyPath:
    def test_fetch_logs_returns_pod_log_lines(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_logs_adapter import (
            KubernetesPodLogsAdapter,
        )

        core_api = MagicMock()
        core_api.read_namespaced_pod_log.return_value = _response(
            "2024-01-01T00:00:00.000000000Z ERROR: connection timeout to postgres:5432\n"
            "2024-01-01T00:00:01.000000000Z pod started successfully\n"
        )
        core_api.read_namespaced_pod.return_value = _pod(restart_count=0)

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesPodLogsAdapter()
            lines = adapter.fetch_logs(
                AnalyzePodLogsRequest(pod_name="api-gateway-7f9b", namespace="prod")
            )

        assert len(lines) == 2
        assert lines[0].run_index == 0
        assert "connection timeout" in lines[0].message
        assert lines[0].level == "ERROR"


class TestKubernetesPodLogsAdapterErrors:
    def test_pod_not_found_raises_resource_not_found(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_logs_adapter import (
            KubernetesPodLogsAdapter,
        )

        class _NotFoundError(Exception):
            status = 404

        core_api = MagicMock()
        core_api.read_namespaced_pod_log.side_effect = _NotFoundError()

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesPodLogsAdapter()
            with pytest.raises(ResourceNotFoundError) as exc_info:
                adapter.fetch_logs(AnalyzePodLogsRequest(pod_name="ghost-pod", namespace="prod"))

        assert "ghost-pod" in str(exc_info.value)
        assert "prod" in str(exc_info.value)

    def test_forbidden_raises_insufficient_permissions(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_logs_adapter import (
            KubernetesPodLogsAdapter,
        )

        class _ForbiddenError(Exception):
            status = 403

        core_api = MagicMock()
        core_api.read_namespaced_pod_log.side_effect = _ForbiddenError()

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesPodLogsAdapter()
            with pytest.raises(InsufficientPermissionsError):
                adapter.fetch_logs(AnalyzePodLogsRequest(pod_name="secure-pod", namespace="prod"))

    def test_other_error_raises_cluster_unreachable(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_logs_adapter import (
            KubernetesPodLogsAdapter,
        )

        core_api = MagicMock()
        core_api.read_namespaced_pod_log.side_effect = TimeoutError("network down")

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesPodLogsAdapter()
            with pytest.raises(ClusterUnreachableError):
                adapter.fetch_logs(AnalyzePodLogsRequest(pod_name="pod-x", namespace="prod"))


class TestKubernetesPodLogsAdapterRestart:
    def test_restart_fetches_previous_logs_as_separate_run(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_logs_adapter import (
            KubernetesPodLogsAdapter,
        )

        core_api = MagicMock()
        core_api.read_namespaced_pod_log.side_effect = [
            _response("2024-01-01T00:00:01.000000000Z current run line\n"),
            _response("2024-01-01T00:00:00.000000000Z previous run line\n"),
        ]
        core_api.read_namespaced_pod.return_value = _pod(restart_count=1)

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesPodLogsAdapter()
            lines = adapter.fetch_logs(
                AnalyzePodLogsRequest(pod_name="flaky-pod", namespace="prod")
            )

        run_indexes = {line.run_index for line in lines}
        assert run_indexes == {0, 1}

    def test_no_restart_does_not_fetch_previous(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_logs_adapter import (
            KubernetesPodLogsAdapter,
        )

        core_api = MagicMock()
        core_api.read_namespaced_pod_log.return_value = _response(
            "2024-01-01T00:00:00.000000000Z ok\n"
        )
        core_api.read_namespaced_pod.return_value = _pod(restart_count=0)

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesPodLogsAdapter()
            adapter.fetch_logs(AnalyzePodLogsRequest(pod_name="stable-pod", namespace="prod"))

        assert core_api.read_namespaced_pod_log.call_count == 1


class TestKubernetesPodLogsAdapterSanitization:
    def test_non_utf8_bytes_are_sanitized(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_logs_adapter import (
            KubernetesPodLogsAdapter,
        )

        resp = MagicMock()
        resp.data = b"2024-01-01T00:00:00.000000000Z corrupted \xff\xfe frame\n"

        core_api = MagicMock()
        core_api.read_namespaced_pod_log.return_value = resp
        core_api.read_namespaced_pod.return_value = _pod(restart_count=0)

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesPodLogsAdapter()
            lines = adapter.fetch_logs(
                AnalyzePodLogsRequest(pod_name="binary-pod", namespace="prod")
            )

        assert "�" in lines[0].message


class TestKubernetesPodLogsAdapterJsonLogs:
    def test_json_structured_line_is_parsed(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_logs_adapter import (
            KubernetesPodLogsAdapter,
        )

        resp = _response(
            '2024-01-01T00:00:00.000000000Z {"level":"error","msg":"upstream connect error"}\n'
        )
        core_api = MagicMock()
        core_api.read_namespaced_pod_log.return_value = resp
        core_api.read_namespaced_pod.return_value = _pod(restart_count=0)

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesPodLogsAdapter()
            lines = adapter.fetch_logs(AnalyzePodLogsRequest(pod_name="json-pod", namespace="prod"))

        assert lines[0].is_json is True
        assert lines[0].message == "upstream connect error"
        assert lines[0].level == "ERROR"

    def test_malformed_json_like_line_falls_back_to_raw_text(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_logs_adapter import (
            KubernetesPodLogsAdapter,
        )

        resp = _response("2024-01-01T00:00:00.000000000Z {not valid json}\n")
        core_api = MagicMock()
        core_api.read_namespaced_pod_log.return_value = resp
        core_api.read_namespaced_pod.return_value = _pod(restart_count=0)

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesPodLogsAdapter()
            lines = adapter.fetch_logs(
                AnalyzePodLogsRequest(pod_name="malformed-pod", namespace="prod")
            )

        assert lines[0].is_json is False
        assert lines[0].message == "{not valid json}"


class TestKubernetesPodLogsAdapterEdgeCases:
    def test_skips_blank_lines(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_logs_adapter import (
            KubernetesPodLogsAdapter,
        )

        resp = _response(
            "2024-01-01T00:00:00.000000000Z first\n\n   \n2024-01-01T00:00:01.000000000Z second\n"
        )
        core_api = MagicMock()
        core_api.read_namespaced_pod_log.return_value = resp
        core_api.read_namespaced_pod.return_value = _pod(restart_count=0)

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesPodLogsAdapter()
            lines = adapter.fetch_logs(
                AnalyzePodLogsRequest(pod_name="blank-line-pod", namespace="prod")
            )

        assert len(lines) == 2

    def test_line_without_timestamp_prefix_keeps_full_text(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_logs_adapter import (
            KubernetesPodLogsAdapter,
        )

        resp = _response("no timestamp here just a message\n")
        core_api = MagicMock()
        core_api.read_namespaced_pod_log.return_value = resp
        core_api.read_namespaced_pod.return_value = _pod(restart_count=0)

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesPodLogsAdapter()
            lines = adapter.fetch_logs(
                AnalyzePodLogsRequest(pod_name="no-ts-pod", namespace="prod")
            )

        assert lines[0].timestamp == ""
        assert lines[0].message == "no timestamp here just a message"

    def test_previous_log_fetch_failure_is_ignored(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_logs_adapter import (
            KubernetesPodLogsAdapter,
        )

        core_api = MagicMock()
        core_api.read_namespaced_pod_log.side_effect = [
            _response("2024-01-01T00:00:00.000000000Z current run line\n"),
            RuntimeError("previous logs unavailable"),
        ]
        core_api.read_namespaced_pod.return_value = _pod(restart_count=1)

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesPodLogsAdapter()
            lines = adapter.fetch_logs(
                AnalyzePodLogsRequest(pod_name="flaky-pod", namespace="prod")
            )

        assert len(lines) == 1
        assert lines[0].run_index == 0

    def test_pod_status_lookup_failure_treated_as_no_restart(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_logs_adapter import (
            KubernetesPodLogsAdapter,
        )

        core_api = MagicMock()
        core_api.read_namespaced_pod_log.return_value = _response(
            "2024-01-01T00:00:00.000000000Z ok\n"
        )
        core_api.read_namespaced_pod.side_effect = RuntimeError("cannot read pod status")

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesPodLogsAdapter()
            lines = adapter.fetch_logs(
                AnalyzePodLogsRequest(pod_name="status-error-pod", namespace="prod")
            )

        assert core_api.read_namespaced_pod_log.call_count == 1
        assert len(lines) == 1
