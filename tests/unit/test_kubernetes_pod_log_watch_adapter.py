from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest
from hexawyn.application.ports.driven.pod_log_watch_port import PodLogWatchPort
from hexawyn.domain.errors import ClusterUnreachableError, ResourceNotFoundError
from hexawyn.domain.models.watch_pod_logs import WatchPodLogsRequest


class TestKubernetesPodLogWatchAdapterIsPort:
    def test_is_pod_log_watch_port(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_log_watch_adapter import (
            KubernetesPodLogWatchAdapter,
        )

        assert isinstance(KubernetesPodLogWatchAdapter(), PodLogWatchPort)


class TestKubernetesPodLogWatchAdapterHappyPath:
    def test_watch_yields_parsed_lines(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_log_watch_adapter import (
            KubernetesPodLogWatchAdapter,
        )

        core_api = MagicMock()
        core_api.read_namespaced_pod.return_value = MagicMock()
        watcher = MagicMock()
        watcher.stream.return_value = iter(
            [
                "2024-01-01T00:00:00.000000000Z pod healthy",
                "2024-01-01T00:00:01.000000000Z OOMKilled memory limit exceeded",
            ]
        )

        with (
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
            patch("kubernetes.watch.Watch", return_value=watcher),
        ):
            adapter = KubernetesPodLogWatchAdapter()
            request = WatchPodLogsRequest(pod_name="payment-service-7f9b", namespace="prod")
            lines = list(adapter.watch(request))

        assert len(lines) == 2
        assert lines[1].message == "OOMKilled memory limit exceeded"
        assert lines[1].timestamp == "2024-01-01T00:00:01.000000000Z"

    def test_line_without_timestamp_prefix_keeps_full_text(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_log_watch_adapter import (
            KubernetesPodLogWatchAdapter,
        )

        core_api = MagicMock()
        core_api.read_namespaced_pod.return_value = MagicMock()
        watcher = MagicMock()
        watcher.stream.return_value = iter(["no timestamp here just a message"])

        with (
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
            patch("kubernetes.watch.Watch", return_value=watcher),
        ):
            adapter = KubernetesPodLogWatchAdapter()
            request = WatchPodLogsRequest(pod_name="p", namespace="ns")
            lines = list(adapter.watch(request))

        assert lines[0].timestamp == ""
        assert lines[0].message == "no timestamp here just a message"

    def test_json_structured_line_is_parsed(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_log_watch_adapter import (
            KubernetesPodLogWatchAdapter,
        )

        core_api = MagicMock()
        core_api.read_namespaced_pod.return_value = MagicMock()
        watcher = MagicMock()
        watcher.stream.return_value = iter(
            ['2024-01-01T00:00:00.000000000Z {"level":"fatal","msg":"panic: nil pointer"}']
        )

        with (
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
            patch("kubernetes.watch.Watch", return_value=watcher),
        ):
            adapter = KubernetesPodLogWatchAdapter()
            request = WatchPodLogsRequest(pod_name="p", namespace="ns")
            lines = list(adapter.watch(request))

        assert lines[0].is_json is True
        assert lines[0].message == "panic: nil pointer"
        assert lines[0].level == "FATAL"

    def test_malformed_json_like_line_falls_back_to_raw_text(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_log_watch_adapter import (
            KubernetesPodLogWatchAdapter,
        )

        core_api = MagicMock()
        core_api.read_namespaced_pod.return_value = MagicMock()
        watcher = MagicMock()
        watcher.stream.return_value = iter(["2024-01-01T00:00:00.000000000Z {not valid json}"])

        with (
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
            patch("kubernetes.watch.Watch", return_value=watcher),
        ):
            adapter = KubernetesPodLogWatchAdapter()
            request = WatchPodLogsRequest(pod_name="p", namespace="ns")
            lines = list(adapter.watch(request))

        assert lines[0].is_json is False
        assert lines[0].message == "{not valid json}"

    def test_fatal_level_line_detected(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_log_watch_adapter import (
            KubernetesPodLogWatchAdapter,
        )

        core_api = MagicMock()
        core_api.read_namespaced_pod.return_value = MagicMock()
        watcher = MagicMock()
        watcher.stream.return_value = iter(["2024-01-01T00:00:00.000000000Z FATAL crash detected"])

        with (
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
            patch("kubernetes.watch.Watch", return_value=watcher),
        ):
            adapter = KubernetesPodLogWatchAdapter()
            request = WatchPodLogsRequest(pod_name="p", namespace="ns")
            lines = list(adapter.watch(request))

        assert lines[0].level == "ERROR"


class TestKubernetesPodLogWatchAdapterPodNotFoundAtStart:
    def test_raises_resource_not_found(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_log_watch_adapter import (
            KubernetesPodLogWatchAdapter,
        )

        class _NotFoundError(Exception):
            status = 404

        core_api = MagicMock()
        core_api.read_namespaced_pod.side_effect = _NotFoundError()

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesPodLogWatchAdapter()
            request = WatchPodLogsRequest(pod_name="ghost-pod", namespace="prod")
            with pytest.raises(ResourceNotFoundError):
                list(adapter.watch(request))


class TestKubernetesPodLogWatchAdapterReconnect:
    """TC4: Network interruption -> reconnects automatically up to 3 times."""

    def test_reconnects_after_transient_failure(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_log_watch_adapter import (
            KubernetesPodLogWatchAdapter,
        )

        core_api = MagicMock()
        core_api.read_namespaced_pod.return_value = MagicMock()

        def _failing_stream() -> object:
            raise ConnectionError("network interrupted")
            yield  # pragma: no cover - unreachable, makes this a generator

        def _successful_stream() -> object:
            yield "2024-01-01T00:00:00.000000000Z pod healthy after reconnect"

        watcher = MagicMock()
        watcher.stream.side_effect = [_failing_stream(), _successful_stream()]

        with (
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
            patch("kubernetes.watch.Watch", return_value=watcher),
        ):
            adapter = KubernetesPodLogWatchAdapter()
            request = WatchPodLogsRequest(pod_name="p", namespace="ns", max_reconnect_attempts=3)
            lines = list(adapter.watch(request))

        assert len(lines) == 1
        assert "after reconnect" in lines[0].message
        assert watcher.stream.call_count == 2

    def test_raises_after_exhausting_reconnect_attempts(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_log_watch_adapter import (
            KubernetesPodLogWatchAdapter,
        )

        core_api = MagicMock()
        core_api.read_namespaced_pod.return_value = MagicMock()

        def _always_failing_stream() -> object:
            raise ConnectionError("network interrupted")
            yield  # pragma: no cover

        watcher = MagicMock()
        watcher.stream.side_effect = [
            _always_failing_stream(),
            _always_failing_stream(),
            _always_failing_stream(),
            _always_failing_stream(),
        ]

        with (
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
            patch("kubernetes.watch.Watch", return_value=watcher),
        ):
            adapter = KubernetesPodLogWatchAdapter()
            request = WatchPodLogsRequest(pod_name="p", namespace="ns", max_reconnect_attempts=3)
            with pytest.raises(ClusterUnreachableError):
                list(adapter.watch(request))


class TestKubernetesPodLogWatchAdapterPodExists:
    def test_returns_true_when_pod_found(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_log_watch_adapter import (
            KubernetesPodLogWatchAdapter,
        )

        core_api = MagicMock()
        core_api.read_namespaced_pod.return_value = MagicMock()

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesPodLogWatchAdapter()
            assert adapter.pod_exists("p", "ns") is True

    def test_returns_false_when_pod_not_found(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_log_watch_adapter import (
            KubernetesPodLogWatchAdapter,
        )

        class _NotFoundError(Exception):
            status = 404

        core_api = MagicMock()
        core_api.read_namespaced_pod.side_effect = _NotFoundError()

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesPodLogWatchAdapter()
            assert adapter.pod_exists("p", "ns") is False

    def test_returns_true_on_unknown_error_conservatively(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_log_watch_adapter import (
            KubernetesPodLogWatchAdapter,
        )

        core_api = MagicMock()
        core_api.read_namespaced_pod.side_effect = TimeoutError("network down")

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesPodLogWatchAdapter()
            assert adapter.pod_exists("p", "ns") is True
