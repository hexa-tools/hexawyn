from __future__ import annotations

import json
from typing import TYPE_CHECKING

from hexawyn.application.ports.driven.pod_log_watch_port import PodLogWatchPort
from hexawyn.domain.errors import ClusterUnreachableError, ResourceNotFoundError

if TYPE_CHECKING:
    from collections.abc import Iterator

    from hexawyn.domain.models.analyze_pod_logs import PodLogLine
    from hexawyn.domain.models.watch_pod_logs import WatchPodLogsRequest

_K8S_NOT_FOUND = 404
_LEVEL_KEYWORDS = ("FATAL", "ERROR", "WARN", "WARNING", "INFO", "DEBUG")
_MIN_TIMESTAMP_LENGTH = 20


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁKubernetesPodLogWatchAdapterǁwatch__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut: MutantDict = {}  # type: ignore


class KubernetesPodLogWatchAdapter(PodLogWatchPort):
    """Secondary adapter — live-tails pod logs via the Kubernetes watch API.

    Reconnects transparently on transient network errors (up to
    request.max_reconnect_attempts) without ever buffering the full log
    output — each line is yielded as it arrives.
    """

    @_mutmut_mutated(mutants_xǁKubernetesPodLogWatchAdapterǁwatch__mutmut)
    def watch(self, request: WatchPodLogsRequest) -> Iterator[PodLogLine]:
        from kubernetes import client as k8s
        from kubernetes import watch as k8s_watch

        core_api = k8s.CoreV1Api()
        self._ensure_pod_exists(core_api, request)

        attempts = 0
        while True:
            try:
                watcher = k8s_watch.Watch()
                stream = watcher.stream(
                    core_api.read_namespaced_pod_log,
                    name=request.pod_name,
                    namespace=request.namespace,
                    follow=True,
                    timestamps=True,
                    _request_timeout=request.timeout_seconds,
                )
                for raw_line in stream:
                    yield _parse_line(raw_line)
                return
            except Exception as exc:
                attempts += 1
                if attempts > request.max_reconnect_attempts:
                    raise ClusterUnreachableError(
                        f"Lost connection to pod {request.pod_name!r} after "
                        f"{attempts - 1} reconnect attempts: {exc}"
                    ) from exc

    def xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_orig(self, request: WatchPodLogsRequest) -> Iterator[PodLogLine]:
        from kubernetes import client as k8s
        from kubernetes import watch as k8s_watch

        core_api = k8s.CoreV1Api()
        self._ensure_pod_exists(core_api, request)

        attempts = 0
        while True:
            try:
                watcher = k8s_watch.Watch()
                stream = watcher.stream(
                    core_api.read_namespaced_pod_log,
                    name=request.pod_name,
                    namespace=request.namespace,
                    follow=True,
                    timestamps=True,
                    _request_timeout=request.timeout_seconds,
                )
                for raw_line in stream:
                    yield _parse_line(raw_line)
                return
            except Exception as exc:
                attempts += 1
                if attempts > request.max_reconnect_attempts:
                    raise ClusterUnreachableError(
                        f"Lost connection to pod {request.pod_name!r} after "
                        f"{attempts - 1} reconnect attempts: {exc}"
                    ) from exc

    def xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_1(self, request: WatchPodLogsRequest) -> Iterator[PodLogLine]:
        from kubernetes import client as k8s
        from kubernetes import watch as k8s_watch

        core_api = None
        self._ensure_pod_exists(core_api, request)

        attempts = 0
        while True:
            try:
                watcher = k8s_watch.Watch()
                stream = watcher.stream(
                    core_api.read_namespaced_pod_log,
                    name=request.pod_name,
                    namespace=request.namespace,
                    follow=True,
                    timestamps=True,
                    _request_timeout=request.timeout_seconds,
                )
                for raw_line in stream:
                    yield _parse_line(raw_line)
                return
            except Exception as exc:
                attempts += 1
                if attempts > request.max_reconnect_attempts:
                    raise ClusterUnreachableError(
                        f"Lost connection to pod {request.pod_name!r} after "
                        f"{attempts - 1} reconnect attempts: {exc}"
                    ) from exc

    def xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_2(self, request: WatchPodLogsRequest) -> Iterator[PodLogLine]:
        from kubernetes import client as k8s
        from kubernetes import watch as k8s_watch

        core_api = k8s.CoreV1Api()
        self._ensure_pod_exists(None, request)

        attempts = 0
        while True:
            try:
                watcher = k8s_watch.Watch()
                stream = watcher.stream(
                    core_api.read_namespaced_pod_log,
                    name=request.pod_name,
                    namespace=request.namespace,
                    follow=True,
                    timestamps=True,
                    _request_timeout=request.timeout_seconds,
                )
                for raw_line in stream:
                    yield _parse_line(raw_line)
                return
            except Exception as exc:
                attempts += 1
                if attempts > request.max_reconnect_attempts:
                    raise ClusterUnreachableError(
                        f"Lost connection to pod {request.pod_name!r} after "
                        f"{attempts - 1} reconnect attempts: {exc}"
                    ) from exc

    def xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_3(self, request: WatchPodLogsRequest) -> Iterator[PodLogLine]:
        from kubernetes import client as k8s
        from kubernetes import watch as k8s_watch

        core_api = k8s.CoreV1Api()
        self._ensure_pod_exists(core_api, None)

        attempts = 0
        while True:
            try:
                watcher = k8s_watch.Watch()
                stream = watcher.stream(
                    core_api.read_namespaced_pod_log,
                    name=request.pod_name,
                    namespace=request.namespace,
                    follow=True,
                    timestamps=True,
                    _request_timeout=request.timeout_seconds,
                )
                for raw_line in stream:
                    yield _parse_line(raw_line)
                return
            except Exception as exc:
                attempts += 1
                if attempts > request.max_reconnect_attempts:
                    raise ClusterUnreachableError(
                        f"Lost connection to pod {request.pod_name!r} after "
                        f"{attempts - 1} reconnect attempts: {exc}"
                    ) from exc

    def xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_4(self, request: WatchPodLogsRequest) -> Iterator[PodLogLine]:
        from kubernetes import client as k8s
        from kubernetes import watch as k8s_watch

        core_api = k8s.CoreV1Api()
        self._ensure_pod_exists(request)

        attempts = 0
        while True:
            try:
                watcher = k8s_watch.Watch()
                stream = watcher.stream(
                    core_api.read_namespaced_pod_log,
                    name=request.pod_name,
                    namespace=request.namespace,
                    follow=True,
                    timestamps=True,
                    _request_timeout=request.timeout_seconds,
                )
                for raw_line in stream:
                    yield _parse_line(raw_line)
                return
            except Exception as exc:
                attempts += 1
                if attempts > request.max_reconnect_attempts:
                    raise ClusterUnreachableError(
                        f"Lost connection to pod {request.pod_name!r} after "
                        f"{attempts - 1} reconnect attempts: {exc}"
                    ) from exc

    def xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_5(self, request: WatchPodLogsRequest) -> Iterator[PodLogLine]:
        from kubernetes import client as k8s
        from kubernetes import watch as k8s_watch

        core_api = k8s.CoreV1Api()
        self._ensure_pod_exists(core_api, )

        attempts = 0
        while True:
            try:
                watcher = k8s_watch.Watch()
                stream = watcher.stream(
                    core_api.read_namespaced_pod_log,
                    name=request.pod_name,
                    namespace=request.namespace,
                    follow=True,
                    timestamps=True,
                    _request_timeout=request.timeout_seconds,
                )
                for raw_line in stream:
                    yield _parse_line(raw_line)
                return
            except Exception as exc:
                attempts += 1
                if attempts > request.max_reconnect_attempts:
                    raise ClusterUnreachableError(
                        f"Lost connection to pod {request.pod_name!r} after "
                        f"{attempts - 1} reconnect attempts: {exc}"
                    ) from exc

    def xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_6(self, request: WatchPodLogsRequest) -> Iterator[PodLogLine]:
        from kubernetes import client as k8s
        from kubernetes import watch as k8s_watch

        core_api = k8s.CoreV1Api()
        self._ensure_pod_exists(core_api, request)

        attempts = None
        while True:
            try:
                watcher = k8s_watch.Watch()
                stream = watcher.stream(
                    core_api.read_namespaced_pod_log,
                    name=request.pod_name,
                    namespace=request.namespace,
                    follow=True,
                    timestamps=True,
                    _request_timeout=request.timeout_seconds,
                )
                for raw_line in stream:
                    yield _parse_line(raw_line)
                return
            except Exception as exc:
                attempts += 1
                if attempts > request.max_reconnect_attempts:
                    raise ClusterUnreachableError(
                        f"Lost connection to pod {request.pod_name!r} after "
                        f"{attempts - 1} reconnect attempts: {exc}"
                    ) from exc

    def xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_7(self, request: WatchPodLogsRequest) -> Iterator[PodLogLine]:
        from kubernetes import client as k8s
        from kubernetes import watch as k8s_watch

        core_api = k8s.CoreV1Api()
        self._ensure_pod_exists(core_api, request)

        attempts = 1
        while True:
            try:
                watcher = k8s_watch.Watch()
                stream = watcher.stream(
                    core_api.read_namespaced_pod_log,
                    name=request.pod_name,
                    namespace=request.namespace,
                    follow=True,
                    timestamps=True,
                    _request_timeout=request.timeout_seconds,
                )
                for raw_line in stream:
                    yield _parse_line(raw_line)
                return
            except Exception as exc:
                attempts += 1
                if attempts > request.max_reconnect_attempts:
                    raise ClusterUnreachableError(
                        f"Lost connection to pod {request.pod_name!r} after "
                        f"{attempts - 1} reconnect attempts: {exc}"
                    ) from exc

    def xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_8(self, request: WatchPodLogsRequest) -> Iterator[PodLogLine]:
        from kubernetes import client as k8s
        from kubernetes import watch as k8s_watch

        core_api = k8s.CoreV1Api()
        self._ensure_pod_exists(core_api, request)

        attempts = 0
        while False:
            try:
                watcher = k8s_watch.Watch()
                stream = watcher.stream(
                    core_api.read_namespaced_pod_log,
                    name=request.pod_name,
                    namespace=request.namespace,
                    follow=True,
                    timestamps=True,
                    _request_timeout=request.timeout_seconds,
                )
                for raw_line in stream:
                    yield _parse_line(raw_line)
                return
            except Exception as exc:
                attempts += 1
                if attempts > request.max_reconnect_attempts:
                    raise ClusterUnreachableError(
                        f"Lost connection to pod {request.pod_name!r} after "
                        f"{attempts - 1} reconnect attempts: {exc}"
                    ) from exc

    def xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_9(self, request: WatchPodLogsRequest) -> Iterator[PodLogLine]:
        from kubernetes import client as k8s
        from kubernetes import watch as k8s_watch

        core_api = k8s.CoreV1Api()
        self._ensure_pod_exists(core_api, request)

        attempts = 0
        while True:
            try:
                watcher = None
                stream = watcher.stream(
                    core_api.read_namespaced_pod_log,
                    name=request.pod_name,
                    namespace=request.namespace,
                    follow=True,
                    timestamps=True,
                    _request_timeout=request.timeout_seconds,
                )
                for raw_line in stream:
                    yield _parse_line(raw_line)
                return
            except Exception as exc:
                attempts += 1
                if attempts > request.max_reconnect_attempts:
                    raise ClusterUnreachableError(
                        f"Lost connection to pod {request.pod_name!r} after "
                        f"{attempts - 1} reconnect attempts: {exc}"
                    ) from exc

    def xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_10(self, request: WatchPodLogsRequest) -> Iterator[PodLogLine]:
        from kubernetes import client as k8s
        from kubernetes import watch as k8s_watch

        core_api = k8s.CoreV1Api()
        self._ensure_pod_exists(core_api, request)

        attempts = 0
        while True:
            try:
                watcher = k8s_watch.Watch()
                stream = None
                for raw_line in stream:
                    yield _parse_line(raw_line)
                return
            except Exception as exc:
                attempts += 1
                if attempts > request.max_reconnect_attempts:
                    raise ClusterUnreachableError(
                        f"Lost connection to pod {request.pod_name!r} after "
                        f"{attempts - 1} reconnect attempts: {exc}"
                    ) from exc

    def xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_11(self, request: WatchPodLogsRequest) -> Iterator[PodLogLine]:
        from kubernetes import client as k8s
        from kubernetes import watch as k8s_watch

        core_api = k8s.CoreV1Api()
        self._ensure_pod_exists(core_api, request)

        attempts = 0
        while True:
            try:
                watcher = k8s_watch.Watch()
                stream = watcher.stream(
                    None,
                    name=request.pod_name,
                    namespace=request.namespace,
                    follow=True,
                    timestamps=True,
                    _request_timeout=request.timeout_seconds,
                )
                for raw_line in stream:
                    yield _parse_line(raw_line)
                return
            except Exception as exc:
                attempts += 1
                if attempts > request.max_reconnect_attempts:
                    raise ClusterUnreachableError(
                        f"Lost connection to pod {request.pod_name!r} after "
                        f"{attempts - 1} reconnect attempts: {exc}"
                    ) from exc

    def xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_12(self, request: WatchPodLogsRequest) -> Iterator[PodLogLine]:
        from kubernetes import client as k8s
        from kubernetes import watch as k8s_watch

        core_api = k8s.CoreV1Api()
        self._ensure_pod_exists(core_api, request)

        attempts = 0
        while True:
            try:
                watcher = k8s_watch.Watch()
                stream = watcher.stream(
                    core_api.read_namespaced_pod_log,
                    name=None,
                    namespace=request.namespace,
                    follow=True,
                    timestamps=True,
                    _request_timeout=request.timeout_seconds,
                )
                for raw_line in stream:
                    yield _parse_line(raw_line)
                return
            except Exception as exc:
                attempts += 1
                if attempts > request.max_reconnect_attempts:
                    raise ClusterUnreachableError(
                        f"Lost connection to pod {request.pod_name!r} after "
                        f"{attempts - 1} reconnect attempts: {exc}"
                    ) from exc

    def xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_13(self, request: WatchPodLogsRequest) -> Iterator[PodLogLine]:
        from kubernetes import client as k8s
        from kubernetes import watch as k8s_watch

        core_api = k8s.CoreV1Api()
        self._ensure_pod_exists(core_api, request)

        attempts = 0
        while True:
            try:
                watcher = k8s_watch.Watch()
                stream = watcher.stream(
                    core_api.read_namespaced_pod_log,
                    name=request.pod_name,
                    namespace=None,
                    follow=True,
                    timestamps=True,
                    _request_timeout=request.timeout_seconds,
                )
                for raw_line in stream:
                    yield _parse_line(raw_line)
                return
            except Exception as exc:
                attempts += 1
                if attempts > request.max_reconnect_attempts:
                    raise ClusterUnreachableError(
                        f"Lost connection to pod {request.pod_name!r} after "
                        f"{attempts - 1} reconnect attempts: {exc}"
                    ) from exc

    def xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_14(self, request: WatchPodLogsRequest) -> Iterator[PodLogLine]:
        from kubernetes import client as k8s
        from kubernetes import watch as k8s_watch

        core_api = k8s.CoreV1Api()
        self._ensure_pod_exists(core_api, request)

        attempts = 0
        while True:
            try:
                watcher = k8s_watch.Watch()
                stream = watcher.stream(
                    core_api.read_namespaced_pod_log,
                    name=request.pod_name,
                    namespace=request.namespace,
                    follow=None,
                    timestamps=True,
                    _request_timeout=request.timeout_seconds,
                )
                for raw_line in stream:
                    yield _parse_line(raw_line)
                return
            except Exception as exc:
                attempts += 1
                if attempts > request.max_reconnect_attempts:
                    raise ClusterUnreachableError(
                        f"Lost connection to pod {request.pod_name!r} after "
                        f"{attempts - 1} reconnect attempts: {exc}"
                    ) from exc

    def xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_15(self, request: WatchPodLogsRequest) -> Iterator[PodLogLine]:
        from kubernetes import client as k8s
        from kubernetes import watch as k8s_watch

        core_api = k8s.CoreV1Api()
        self._ensure_pod_exists(core_api, request)

        attempts = 0
        while True:
            try:
                watcher = k8s_watch.Watch()
                stream = watcher.stream(
                    core_api.read_namespaced_pod_log,
                    name=request.pod_name,
                    namespace=request.namespace,
                    follow=True,
                    timestamps=None,
                    _request_timeout=request.timeout_seconds,
                )
                for raw_line in stream:
                    yield _parse_line(raw_line)
                return
            except Exception as exc:
                attempts += 1
                if attempts > request.max_reconnect_attempts:
                    raise ClusterUnreachableError(
                        f"Lost connection to pod {request.pod_name!r} after "
                        f"{attempts - 1} reconnect attempts: {exc}"
                    ) from exc

    def xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_16(self, request: WatchPodLogsRequest) -> Iterator[PodLogLine]:
        from kubernetes import client as k8s
        from kubernetes import watch as k8s_watch

        core_api = k8s.CoreV1Api()
        self._ensure_pod_exists(core_api, request)

        attempts = 0
        while True:
            try:
                watcher = k8s_watch.Watch()
                stream = watcher.stream(
                    core_api.read_namespaced_pod_log,
                    name=request.pod_name,
                    namespace=request.namespace,
                    follow=True,
                    timestamps=True,
                    _request_timeout=None,
                )
                for raw_line in stream:
                    yield _parse_line(raw_line)
                return
            except Exception as exc:
                attempts += 1
                if attempts > request.max_reconnect_attempts:
                    raise ClusterUnreachableError(
                        f"Lost connection to pod {request.pod_name!r} after "
                        f"{attempts - 1} reconnect attempts: {exc}"
                    ) from exc

    def xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_17(self, request: WatchPodLogsRequest) -> Iterator[PodLogLine]:
        from kubernetes import client as k8s
        from kubernetes import watch as k8s_watch

        core_api = k8s.CoreV1Api()
        self._ensure_pod_exists(core_api, request)

        attempts = 0
        while True:
            try:
                watcher = k8s_watch.Watch()
                stream = watcher.stream(
                    name=request.pod_name,
                    namespace=request.namespace,
                    follow=True,
                    timestamps=True,
                    _request_timeout=request.timeout_seconds,
                )
                for raw_line in stream:
                    yield _parse_line(raw_line)
                return
            except Exception as exc:
                attempts += 1
                if attempts > request.max_reconnect_attempts:
                    raise ClusterUnreachableError(
                        f"Lost connection to pod {request.pod_name!r} after "
                        f"{attempts - 1} reconnect attempts: {exc}"
                    ) from exc

    def xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_18(self, request: WatchPodLogsRequest) -> Iterator[PodLogLine]:
        from kubernetes import client as k8s
        from kubernetes import watch as k8s_watch

        core_api = k8s.CoreV1Api()
        self._ensure_pod_exists(core_api, request)

        attempts = 0
        while True:
            try:
                watcher = k8s_watch.Watch()
                stream = watcher.stream(
                    core_api.read_namespaced_pod_log,
                    namespace=request.namespace,
                    follow=True,
                    timestamps=True,
                    _request_timeout=request.timeout_seconds,
                )
                for raw_line in stream:
                    yield _parse_line(raw_line)
                return
            except Exception as exc:
                attempts += 1
                if attempts > request.max_reconnect_attempts:
                    raise ClusterUnreachableError(
                        f"Lost connection to pod {request.pod_name!r} after "
                        f"{attempts - 1} reconnect attempts: {exc}"
                    ) from exc

    def xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_19(self, request: WatchPodLogsRequest) -> Iterator[PodLogLine]:
        from kubernetes import client as k8s
        from kubernetes import watch as k8s_watch

        core_api = k8s.CoreV1Api()
        self._ensure_pod_exists(core_api, request)

        attempts = 0
        while True:
            try:
                watcher = k8s_watch.Watch()
                stream = watcher.stream(
                    core_api.read_namespaced_pod_log,
                    name=request.pod_name,
                    follow=True,
                    timestamps=True,
                    _request_timeout=request.timeout_seconds,
                )
                for raw_line in stream:
                    yield _parse_line(raw_line)
                return
            except Exception as exc:
                attempts += 1
                if attempts > request.max_reconnect_attempts:
                    raise ClusterUnreachableError(
                        f"Lost connection to pod {request.pod_name!r} after "
                        f"{attempts - 1} reconnect attempts: {exc}"
                    ) from exc

    def xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_20(self, request: WatchPodLogsRequest) -> Iterator[PodLogLine]:
        from kubernetes import client as k8s
        from kubernetes import watch as k8s_watch

        core_api = k8s.CoreV1Api()
        self._ensure_pod_exists(core_api, request)

        attempts = 0
        while True:
            try:
                watcher = k8s_watch.Watch()
                stream = watcher.stream(
                    core_api.read_namespaced_pod_log,
                    name=request.pod_name,
                    namespace=request.namespace,
                    timestamps=True,
                    _request_timeout=request.timeout_seconds,
                )
                for raw_line in stream:
                    yield _parse_line(raw_line)
                return
            except Exception as exc:
                attempts += 1
                if attempts > request.max_reconnect_attempts:
                    raise ClusterUnreachableError(
                        f"Lost connection to pod {request.pod_name!r} after "
                        f"{attempts - 1} reconnect attempts: {exc}"
                    ) from exc

    def xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_21(self, request: WatchPodLogsRequest) -> Iterator[PodLogLine]:
        from kubernetes import client as k8s
        from kubernetes import watch as k8s_watch

        core_api = k8s.CoreV1Api()
        self._ensure_pod_exists(core_api, request)

        attempts = 0
        while True:
            try:
                watcher = k8s_watch.Watch()
                stream = watcher.stream(
                    core_api.read_namespaced_pod_log,
                    name=request.pod_name,
                    namespace=request.namespace,
                    follow=True,
                    _request_timeout=request.timeout_seconds,
                )
                for raw_line in stream:
                    yield _parse_line(raw_line)
                return
            except Exception as exc:
                attempts += 1
                if attempts > request.max_reconnect_attempts:
                    raise ClusterUnreachableError(
                        f"Lost connection to pod {request.pod_name!r} after "
                        f"{attempts - 1} reconnect attempts: {exc}"
                    ) from exc

    def xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_22(self, request: WatchPodLogsRequest) -> Iterator[PodLogLine]:
        from kubernetes import client as k8s
        from kubernetes import watch as k8s_watch

        core_api = k8s.CoreV1Api()
        self._ensure_pod_exists(core_api, request)

        attempts = 0
        while True:
            try:
                watcher = k8s_watch.Watch()
                stream = watcher.stream(
                    core_api.read_namespaced_pod_log,
                    name=request.pod_name,
                    namespace=request.namespace,
                    follow=True,
                    timestamps=True,
                    )
                for raw_line in stream:
                    yield _parse_line(raw_line)
                return
            except Exception as exc:
                attempts += 1
                if attempts > request.max_reconnect_attempts:
                    raise ClusterUnreachableError(
                        f"Lost connection to pod {request.pod_name!r} after "
                        f"{attempts - 1} reconnect attempts: {exc}"
                    ) from exc

    def xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_23(self, request: WatchPodLogsRequest) -> Iterator[PodLogLine]:
        from kubernetes import client as k8s
        from kubernetes import watch as k8s_watch

        core_api = k8s.CoreV1Api()
        self._ensure_pod_exists(core_api, request)

        attempts = 0
        while True:
            try:
                watcher = k8s_watch.Watch()
                stream = watcher.stream(
                    core_api.read_namespaced_pod_log,
                    name=request.pod_name,
                    namespace=request.namespace,
                    follow=False,
                    timestamps=True,
                    _request_timeout=request.timeout_seconds,
                )
                for raw_line in stream:
                    yield _parse_line(raw_line)
                return
            except Exception as exc:
                attempts += 1
                if attempts > request.max_reconnect_attempts:
                    raise ClusterUnreachableError(
                        f"Lost connection to pod {request.pod_name!r} after "
                        f"{attempts - 1} reconnect attempts: {exc}"
                    ) from exc

    def xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_24(self, request: WatchPodLogsRequest) -> Iterator[PodLogLine]:
        from kubernetes import client as k8s
        from kubernetes import watch as k8s_watch

        core_api = k8s.CoreV1Api()
        self._ensure_pod_exists(core_api, request)

        attempts = 0
        while True:
            try:
                watcher = k8s_watch.Watch()
                stream = watcher.stream(
                    core_api.read_namespaced_pod_log,
                    name=request.pod_name,
                    namespace=request.namespace,
                    follow=True,
                    timestamps=False,
                    _request_timeout=request.timeout_seconds,
                )
                for raw_line in stream:
                    yield _parse_line(raw_line)
                return
            except Exception as exc:
                attempts += 1
                if attempts > request.max_reconnect_attempts:
                    raise ClusterUnreachableError(
                        f"Lost connection to pod {request.pod_name!r} after "
                        f"{attempts - 1} reconnect attempts: {exc}"
                    ) from exc

    def xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_25(self, request: WatchPodLogsRequest) -> Iterator[PodLogLine]:
        from kubernetes import client as k8s
        from kubernetes import watch as k8s_watch

        core_api = k8s.CoreV1Api()
        self._ensure_pod_exists(core_api, request)

        attempts = 0
        while True:
            try:
                watcher = k8s_watch.Watch()
                stream = watcher.stream(
                    core_api.read_namespaced_pod_log,
                    name=request.pod_name,
                    namespace=request.namespace,
                    follow=True,
                    timestamps=True,
                    _request_timeout=request.timeout_seconds,
                )
                for raw_line in stream:
                    yield _parse_line(None)
                return
            except Exception as exc:
                attempts += 1
                if attempts > request.max_reconnect_attempts:
                    raise ClusterUnreachableError(
                        f"Lost connection to pod {request.pod_name!r} after "
                        f"{attempts - 1} reconnect attempts: {exc}"
                    ) from exc

    def xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_26(self, request: WatchPodLogsRequest) -> Iterator[PodLogLine]:
        from kubernetes import client as k8s
        from kubernetes import watch as k8s_watch

        core_api = k8s.CoreV1Api()
        self._ensure_pod_exists(core_api, request)

        attempts = 0
        while True:
            try:
                watcher = k8s_watch.Watch()
                stream = watcher.stream(
                    core_api.read_namespaced_pod_log,
                    name=request.pod_name,
                    namespace=request.namespace,
                    follow=True,
                    timestamps=True,
                    _request_timeout=request.timeout_seconds,
                )
                for raw_line in stream:
                    yield _parse_line(raw_line)
                return
            except Exception as exc:
                attempts = 1
                if attempts > request.max_reconnect_attempts:
                    raise ClusterUnreachableError(
                        f"Lost connection to pod {request.pod_name!r} after "
                        f"{attempts - 1} reconnect attempts: {exc}"
                    ) from exc

    def xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_27(self, request: WatchPodLogsRequest) -> Iterator[PodLogLine]:
        from kubernetes import client as k8s
        from kubernetes import watch as k8s_watch

        core_api = k8s.CoreV1Api()
        self._ensure_pod_exists(core_api, request)

        attempts = 0
        while True:
            try:
                watcher = k8s_watch.Watch()
                stream = watcher.stream(
                    core_api.read_namespaced_pod_log,
                    name=request.pod_name,
                    namespace=request.namespace,
                    follow=True,
                    timestamps=True,
                    _request_timeout=request.timeout_seconds,
                )
                for raw_line in stream:
                    yield _parse_line(raw_line)
                return
            except Exception as exc:
                attempts -= 1
                if attempts > request.max_reconnect_attempts:
                    raise ClusterUnreachableError(
                        f"Lost connection to pod {request.pod_name!r} after "
                        f"{attempts - 1} reconnect attempts: {exc}"
                    ) from exc

    def xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_28(self, request: WatchPodLogsRequest) -> Iterator[PodLogLine]:
        from kubernetes import client as k8s
        from kubernetes import watch as k8s_watch

        core_api = k8s.CoreV1Api()
        self._ensure_pod_exists(core_api, request)

        attempts = 0
        while True:
            try:
                watcher = k8s_watch.Watch()
                stream = watcher.stream(
                    core_api.read_namespaced_pod_log,
                    name=request.pod_name,
                    namespace=request.namespace,
                    follow=True,
                    timestamps=True,
                    _request_timeout=request.timeout_seconds,
                )
                for raw_line in stream:
                    yield _parse_line(raw_line)
                return
            except Exception as exc:
                attempts += 2
                if attempts > request.max_reconnect_attempts:
                    raise ClusterUnreachableError(
                        f"Lost connection to pod {request.pod_name!r} after "
                        f"{attempts - 1} reconnect attempts: {exc}"
                    ) from exc

    def xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_29(self, request: WatchPodLogsRequest) -> Iterator[PodLogLine]:
        from kubernetes import client as k8s
        from kubernetes import watch as k8s_watch

        core_api = k8s.CoreV1Api()
        self._ensure_pod_exists(core_api, request)

        attempts = 0
        while True:
            try:
                watcher = k8s_watch.Watch()
                stream = watcher.stream(
                    core_api.read_namespaced_pod_log,
                    name=request.pod_name,
                    namespace=request.namespace,
                    follow=True,
                    timestamps=True,
                    _request_timeout=request.timeout_seconds,
                )
                for raw_line in stream:
                    yield _parse_line(raw_line)
                return
            except Exception as exc:
                attempts += 1
                if attempts >= request.max_reconnect_attempts:
                    raise ClusterUnreachableError(
                        f"Lost connection to pod {request.pod_name!r} after "
                        f"{attempts - 1} reconnect attempts: {exc}"
                    ) from exc

    def xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_30(self, request: WatchPodLogsRequest) -> Iterator[PodLogLine]:
        from kubernetes import client as k8s
        from kubernetes import watch as k8s_watch

        core_api = k8s.CoreV1Api()
        self._ensure_pod_exists(core_api, request)

        attempts = 0
        while True:
            try:
                watcher = k8s_watch.Watch()
                stream = watcher.stream(
                    core_api.read_namespaced_pod_log,
                    name=request.pod_name,
                    namespace=request.namespace,
                    follow=True,
                    timestamps=True,
                    _request_timeout=request.timeout_seconds,
                )
                for raw_line in stream:
                    yield _parse_line(raw_line)
                return
            except Exception as exc:
                attempts += 1
                if attempts > request.max_reconnect_attempts:
                    raise ClusterUnreachableError(
                        None
                    ) from exc

    def xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_31(self, request: WatchPodLogsRequest) -> Iterator[PodLogLine]:
        from kubernetes import client as k8s
        from kubernetes import watch as k8s_watch

        core_api = k8s.CoreV1Api()
        self._ensure_pod_exists(core_api, request)

        attempts = 0
        while True:
            try:
                watcher = k8s_watch.Watch()
                stream = watcher.stream(
                    core_api.read_namespaced_pod_log,
                    name=request.pod_name,
                    namespace=request.namespace,
                    follow=True,
                    timestamps=True,
                    _request_timeout=request.timeout_seconds,
                )
                for raw_line in stream:
                    yield _parse_line(raw_line)
                return
            except Exception as exc:
                attempts += 1
                if attempts > request.max_reconnect_attempts:
                    raise ClusterUnreachableError(
                        f"Lost connection to pod {request.pod_name!r} after "
                        f"{attempts + 1} reconnect attempts: {exc}"
                    ) from exc

    def xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_32(self, request: WatchPodLogsRequest) -> Iterator[PodLogLine]:
        from kubernetes import client as k8s
        from kubernetes import watch as k8s_watch

        core_api = k8s.CoreV1Api()
        self._ensure_pod_exists(core_api, request)

        attempts = 0
        while True:
            try:
                watcher = k8s_watch.Watch()
                stream = watcher.stream(
                    core_api.read_namespaced_pod_log,
                    name=request.pod_name,
                    namespace=request.namespace,
                    follow=True,
                    timestamps=True,
                    _request_timeout=request.timeout_seconds,
                )
                for raw_line in stream:
                    yield _parse_line(raw_line)
                return
            except Exception as exc:
                attempts += 1
                if attempts > request.max_reconnect_attempts:
                    raise ClusterUnreachableError(
                        f"Lost connection to pod {request.pod_name!r} after "
                        f"{attempts - 2} reconnect attempts: {exc}"
                    ) from exc

    @_mutmut_mutated(mutants_xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut)
    def pod_exists(self, pod_name: str, namespace: str) -> bool:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            core_api.read_namespaced_pod(name=pod_name, namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            return status != _K8S_NOT_FOUND
        return True

    def xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_orig(self, pod_name: str, namespace: str) -> bool:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            core_api.read_namespaced_pod(name=pod_name, namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            return status != _K8S_NOT_FOUND
        return True

    def xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_1(self, pod_name: str, namespace: str) -> bool:
        from kubernetes import client as k8s

        core_api = None
        try:
            core_api.read_namespaced_pod(name=pod_name, namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            return status != _K8S_NOT_FOUND
        return True

    def xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_2(self, pod_name: str, namespace: str) -> bool:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            core_api.read_namespaced_pod(name=None, namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            return status != _K8S_NOT_FOUND
        return True

    def xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_3(self, pod_name: str, namespace: str) -> bool:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            core_api.read_namespaced_pod(name=pod_name, namespace=None)
        except Exception as exc:
            status = getattr(exc, "status", None)
            return status != _K8S_NOT_FOUND
        return True

    def xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_4(self, pod_name: str, namespace: str) -> bool:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            core_api.read_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            return status != _K8S_NOT_FOUND
        return True

    def xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_5(self, pod_name: str, namespace: str) -> bool:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            core_api.read_namespaced_pod(name=pod_name, )
        except Exception as exc:
            status = getattr(exc, "status", None)
            return status != _K8S_NOT_FOUND
        return True

    def xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_6(self, pod_name: str, namespace: str) -> bool:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            core_api.read_namespaced_pod(name=pod_name, namespace=namespace)
        except Exception as exc:
            status = None
            return status != _K8S_NOT_FOUND
        return True

    def xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_7(self, pod_name: str, namespace: str) -> bool:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            core_api.read_namespaced_pod(name=pod_name, namespace=namespace)
        except Exception as exc:
            status = getattr(None, "status", None)
            return status != _K8S_NOT_FOUND
        return True

    def xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_8(self, pod_name: str, namespace: str) -> bool:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            core_api.read_namespaced_pod(name=pod_name, namespace=namespace)
        except Exception as exc:
            status = getattr(exc, None, None)
            return status != _K8S_NOT_FOUND
        return True

    def xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_9(self, pod_name: str, namespace: str) -> bool:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            core_api.read_namespaced_pod(name=pod_name, namespace=namespace)
        except Exception as exc:
            status = getattr("status", None)
            return status != _K8S_NOT_FOUND
        return True

    def xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_10(self, pod_name: str, namespace: str) -> bool:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            core_api.read_namespaced_pod(name=pod_name, namespace=namespace)
        except Exception as exc:
            status = getattr(exc, None)
            return status != _K8S_NOT_FOUND
        return True

    def xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_11(self, pod_name: str, namespace: str) -> bool:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            core_api.read_namespaced_pod(name=pod_name, namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", )
            return status != _K8S_NOT_FOUND
        return True

    def xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_12(self, pod_name: str, namespace: str) -> bool:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            core_api.read_namespaced_pod(name=pod_name, namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "XXstatusXX", None)
            return status != _K8S_NOT_FOUND
        return True

    def xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_13(self, pod_name: str, namespace: str) -> bool:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            core_api.read_namespaced_pod(name=pod_name, namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "STATUS", None)
            return status != _K8S_NOT_FOUND
        return True

    def xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_14(self, pod_name: str, namespace: str) -> bool:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            core_api.read_namespaced_pod(name=pod_name, namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            return status == _K8S_NOT_FOUND
        return True

    def xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_15(self, pod_name: str, namespace: str) -> bool:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            core_api.read_namespaced_pod(name=pod_name, namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            return status != _K8S_NOT_FOUND
        return False

    @_mutmut_mutated(mutants_xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut)
    def _ensure_pod_exists(self, core_api: object, request: WatchPodLogsRequest) -> None:
        try:
            core_api.read_namespaced_pod(  # type: ignore[attr-defined]
                name=request.pod_name, namespace=request.namespace
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ResourceNotFoundError(
                    f"Pod {request.pod_name!r} not found in namespace {request.namespace!r}",
                    context={"pod_name": request.pod_name, "namespace": request.namespace},
                ) from exc

    def xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_orig(self, core_api: object, request: WatchPodLogsRequest) -> None:
        try:
            core_api.read_namespaced_pod(  # type: ignore[attr-defined]
                name=request.pod_name, namespace=request.namespace
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ResourceNotFoundError(
                    f"Pod {request.pod_name!r} not found in namespace {request.namespace!r}",
                    context={"pod_name": request.pod_name, "namespace": request.namespace},
                ) from exc

    def xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_1(self, core_api: object, request: WatchPodLogsRequest) -> None:
        try:
            core_api.read_namespaced_pod(  # type: ignore[attr-defined]
                name=None, namespace=request.namespace
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ResourceNotFoundError(
                    f"Pod {request.pod_name!r} not found in namespace {request.namespace!r}",
                    context={"pod_name": request.pod_name, "namespace": request.namespace},
                ) from exc

    def xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_2(self, core_api: object, request: WatchPodLogsRequest) -> None:
        try:
            core_api.read_namespaced_pod(  # type: ignore[attr-defined]
                name=request.pod_name, namespace=None
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ResourceNotFoundError(
                    f"Pod {request.pod_name!r} not found in namespace {request.namespace!r}",
                    context={"pod_name": request.pod_name, "namespace": request.namespace},
                ) from exc

    def xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_3(self, core_api: object, request: WatchPodLogsRequest) -> None:
        try:
            core_api.read_namespaced_pod(  # type: ignore[attr-defined]
                namespace=request.namespace
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ResourceNotFoundError(
                    f"Pod {request.pod_name!r} not found in namespace {request.namespace!r}",
                    context={"pod_name": request.pod_name, "namespace": request.namespace},
                ) from exc

    def xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_4(self, core_api: object, request: WatchPodLogsRequest) -> None:
        try:
            core_api.read_namespaced_pod(  # type: ignore[attr-defined]
                name=request.pod_name, )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ResourceNotFoundError(
                    f"Pod {request.pod_name!r} not found in namespace {request.namespace!r}",
                    context={"pod_name": request.pod_name, "namespace": request.namespace},
                ) from exc

    def xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_5(self, core_api: object, request: WatchPodLogsRequest) -> None:
        try:
            core_api.read_namespaced_pod(  # type: ignore[attr-defined]
                name=request.pod_name, namespace=request.namespace
            )
        except Exception as exc:
            status = None
            if status == _K8S_NOT_FOUND:
                raise ResourceNotFoundError(
                    f"Pod {request.pod_name!r} not found in namespace {request.namespace!r}",
                    context={"pod_name": request.pod_name, "namespace": request.namespace},
                ) from exc

    def xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_6(self, core_api: object, request: WatchPodLogsRequest) -> None:
        try:
            core_api.read_namespaced_pod(  # type: ignore[attr-defined]
                name=request.pod_name, namespace=request.namespace
            )
        except Exception as exc:
            status = getattr(None, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ResourceNotFoundError(
                    f"Pod {request.pod_name!r} not found in namespace {request.namespace!r}",
                    context={"pod_name": request.pod_name, "namespace": request.namespace},
                ) from exc

    def xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_7(self, core_api: object, request: WatchPodLogsRequest) -> None:
        try:
            core_api.read_namespaced_pod(  # type: ignore[attr-defined]
                name=request.pod_name, namespace=request.namespace
            )
        except Exception as exc:
            status = getattr(exc, None, None)
            if status == _K8S_NOT_FOUND:
                raise ResourceNotFoundError(
                    f"Pod {request.pod_name!r} not found in namespace {request.namespace!r}",
                    context={"pod_name": request.pod_name, "namespace": request.namespace},
                ) from exc

    def xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_8(self, core_api: object, request: WatchPodLogsRequest) -> None:
        try:
            core_api.read_namespaced_pod(  # type: ignore[attr-defined]
                name=request.pod_name, namespace=request.namespace
            )
        except Exception as exc:
            status = getattr("status", None)
            if status == _K8S_NOT_FOUND:
                raise ResourceNotFoundError(
                    f"Pod {request.pod_name!r} not found in namespace {request.namespace!r}",
                    context={"pod_name": request.pod_name, "namespace": request.namespace},
                ) from exc

    def xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_9(self, core_api: object, request: WatchPodLogsRequest) -> None:
        try:
            core_api.read_namespaced_pod(  # type: ignore[attr-defined]
                name=request.pod_name, namespace=request.namespace
            )
        except Exception as exc:
            status = getattr(exc, None)
            if status == _K8S_NOT_FOUND:
                raise ResourceNotFoundError(
                    f"Pod {request.pod_name!r} not found in namespace {request.namespace!r}",
                    context={"pod_name": request.pod_name, "namespace": request.namespace},
                ) from exc

    def xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_10(self, core_api: object, request: WatchPodLogsRequest) -> None:
        try:
            core_api.read_namespaced_pod(  # type: ignore[attr-defined]
                name=request.pod_name, namespace=request.namespace
            )
        except Exception as exc:
            status = getattr(exc, "status", )
            if status == _K8S_NOT_FOUND:
                raise ResourceNotFoundError(
                    f"Pod {request.pod_name!r} not found in namespace {request.namespace!r}",
                    context={"pod_name": request.pod_name, "namespace": request.namespace},
                ) from exc

    def xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_11(self, core_api: object, request: WatchPodLogsRequest) -> None:
        try:
            core_api.read_namespaced_pod(  # type: ignore[attr-defined]
                name=request.pod_name, namespace=request.namespace
            )
        except Exception as exc:
            status = getattr(exc, "XXstatusXX", None)
            if status == _K8S_NOT_FOUND:
                raise ResourceNotFoundError(
                    f"Pod {request.pod_name!r} not found in namespace {request.namespace!r}",
                    context={"pod_name": request.pod_name, "namespace": request.namespace},
                ) from exc

    def xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_12(self, core_api: object, request: WatchPodLogsRequest) -> None:
        try:
            core_api.read_namespaced_pod(  # type: ignore[attr-defined]
                name=request.pod_name, namespace=request.namespace
            )
        except Exception as exc:
            status = getattr(exc, "STATUS", None)
            if status == _K8S_NOT_FOUND:
                raise ResourceNotFoundError(
                    f"Pod {request.pod_name!r} not found in namespace {request.namespace!r}",
                    context={"pod_name": request.pod_name, "namespace": request.namespace},
                ) from exc

    def xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_13(self, core_api: object, request: WatchPodLogsRequest) -> None:
        try:
            core_api.read_namespaced_pod(  # type: ignore[attr-defined]
                name=request.pod_name, namespace=request.namespace
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status != _K8S_NOT_FOUND:
                raise ResourceNotFoundError(
                    f"Pod {request.pod_name!r} not found in namespace {request.namespace!r}",
                    context={"pod_name": request.pod_name, "namespace": request.namespace},
                ) from exc

    def xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_14(self, core_api: object, request: WatchPodLogsRequest) -> None:
        try:
            core_api.read_namespaced_pod(  # type: ignore[attr-defined]
                name=request.pod_name, namespace=request.namespace
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ResourceNotFoundError(
                    None,
                    context={"pod_name": request.pod_name, "namespace": request.namespace},
                ) from exc

    def xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_15(self, core_api: object, request: WatchPodLogsRequest) -> None:
        try:
            core_api.read_namespaced_pod(  # type: ignore[attr-defined]
                name=request.pod_name, namespace=request.namespace
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ResourceNotFoundError(
                    f"Pod {request.pod_name!r} not found in namespace {request.namespace!r}",
                    context=None,
                ) from exc

    def xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_16(self, core_api: object, request: WatchPodLogsRequest) -> None:
        try:
            core_api.read_namespaced_pod(  # type: ignore[attr-defined]
                name=request.pod_name, namespace=request.namespace
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ResourceNotFoundError(
                    context={"pod_name": request.pod_name, "namespace": request.namespace},
                ) from exc

    def xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_17(self, core_api: object, request: WatchPodLogsRequest) -> None:
        try:
            core_api.read_namespaced_pod(  # type: ignore[attr-defined]
                name=request.pod_name, namespace=request.namespace
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ResourceNotFoundError(
                    f"Pod {request.pod_name!r} not found in namespace {request.namespace!r}",
                    ) from exc

    def xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_18(self, core_api: object, request: WatchPodLogsRequest) -> None:
        try:
            core_api.read_namespaced_pod(  # type: ignore[attr-defined]
                name=request.pod_name, namespace=request.namespace
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ResourceNotFoundError(
                    f"Pod {request.pod_name!r} not found in namespace {request.namespace!r}",
                    context={"XXpod_nameXX": request.pod_name, "namespace": request.namespace},
                ) from exc

    def xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_19(self, core_api: object, request: WatchPodLogsRequest) -> None:
        try:
            core_api.read_namespaced_pod(  # type: ignore[attr-defined]
                name=request.pod_name, namespace=request.namespace
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ResourceNotFoundError(
                    f"Pod {request.pod_name!r} not found in namespace {request.namespace!r}",
                    context={"POD_NAME": request.pod_name, "namespace": request.namespace},
                ) from exc

    def xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_20(self, core_api: object, request: WatchPodLogsRequest) -> None:
        try:
            core_api.read_namespaced_pod(  # type: ignore[attr-defined]
                name=request.pod_name, namespace=request.namespace
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ResourceNotFoundError(
                    f"Pod {request.pod_name!r} not found in namespace {request.namespace!r}",
                    context={"pod_name": request.pod_name, "XXnamespaceXX": request.namespace},
                ) from exc

    def xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_21(self, core_api: object, request: WatchPodLogsRequest) -> None:
        try:
            core_api.read_namespaced_pod(  # type: ignore[attr-defined]
                name=request.pod_name, namespace=request.namespace
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ResourceNotFoundError(
                    f"Pod {request.pod_name!r} not found in namespace {request.namespace!r}",
                    context={"pod_name": request.pod_name, "NAMESPACE": request.namespace},
                ) from exc

mutants_xǁKubernetesPodLogWatchAdapterǁwatch__mutmut['_mutmut_orig'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁwatch__mutmut['xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_1'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁwatch__mutmut['xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_2'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁwatch__mutmut['xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_3'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁwatch__mutmut['xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_4'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁwatch__mutmut['xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_5'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁwatch__mutmut['xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_6'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁwatch__mutmut['xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_7'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁwatch__mutmut['xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_8'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁwatch__mutmut['xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_9'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁwatch__mutmut['xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_10'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁwatch__mutmut['xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_11'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁwatch__mutmut['xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_12'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁwatch__mutmut['xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_13'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁwatch__mutmut['xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_14'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_14 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁwatch__mutmut['xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_15'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_15 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁwatch__mutmut['xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_16'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_16 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁwatch__mutmut['xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_17'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_17 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁwatch__mutmut['xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_18'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_18 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁwatch__mutmut['xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_19'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_19 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁwatch__mutmut['xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_20'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_20 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁwatch__mutmut['xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_21'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_21 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁwatch__mutmut['xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_22'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_22 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁwatch__mutmut['xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_23'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_23 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁwatch__mutmut['xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_24'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_24 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁwatch__mutmut['xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_25'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_25 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁwatch__mutmut['xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_26'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_26 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁwatch__mutmut['xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_27'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_27 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁwatch__mutmut['xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_28'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_28 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁwatch__mutmut['xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_29'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_29 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁwatch__mutmut['xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_30'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_30 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁwatch__mutmut['xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_31'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_31 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁwatch__mutmut['xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_32'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁwatch__mutmut_32 # type: ignore # mutmut generated

mutants_xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut['_mutmut_orig'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut['xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_1'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut['xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_2'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut['xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_3'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut['xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_4'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut['xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_5'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut['xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_6'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut['xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_7'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut['xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_8'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut['xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_9'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut['xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_10'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut['xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_11'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut['xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_12'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut['xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_13'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut['xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_14'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_14 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut['xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_15'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁpod_exists__mutmut_15 # type: ignore # mutmut generated

mutants_xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut['_mutmut_orig'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut['xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_1'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut['xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_2'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut['xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_3'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut['xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_4'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut['xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_5'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut['xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_6'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut['xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_7'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut['xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_8'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut['xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_9'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut['xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_10'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut['xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_11'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut['xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_12'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut['xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_13'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut['xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_14'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_14 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut['xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_15'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_15 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut['xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_16'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_16 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut['xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_17'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_17 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut['xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_18'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_18 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut['xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_19'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_19 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut['xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_20'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_20 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut['xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_21'] = KubernetesPodLogWatchAdapter.xǁKubernetesPodLogWatchAdapterǁ_ensure_pod_exists__mutmut_21 # type: ignore # mutmut generated
mutants_x__parse_line__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__parse_line__mutmut)
def _parse_line(raw_line: str) -> PodLogLine:
    from hexawyn.domain.models.analyze_pod_logs import PodLogLine

    timestamp, message = _split_timestamp(raw_line)
    is_json, message, level = _parse_message(message)
    return PodLogLine(
        timestamp=timestamp, level=level, message=message, run_index=0, is_json=is_json
    )


def x__parse_line__mutmut_orig(raw_line: str) -> PodLogLine:
    from hexawyn.domain.models.analyze_pod_logs import PodLogLine

    timestamp, message = _split_timestamp(raw_line)
    is_json, message, level = _parse_message(message)
    return PodLogLine(
        timestamp=timestamp, level=level, message=message, run_index=0, is_json=is_json
    )


def x__parse_line__mutmut_1(raw_line: str) -> PodLogLine:
    from hexawyn.domain.models.analyze_pod_logs import PodLogLine

    timestamp, message = None
    is_json, message, level = _parse_message(message)
    return PodLogLine(
        timestamp=timestamp, level=level, message=message, run_index=0, is_json=is_json
    )


def x__parse_line__mutmut_2(raw_line: str) -> PodLogLine:
    from hexawyn.domain.models.analyze_pod_logs import PodLogLine

    timestamp, message = _split_timestamp(None)
    is_json, message, level = _parse_message(message)
    return PodLogLine(
        timestamp=timestamp, level=level, message=message, run_index=0, is_json=is_json
    )


def x__parse_line__mutmut_3(raw_line: str) -> PodLogLine:
    from hexawyn.domain.models.analyze_pod_logs import PodLogLine

    timestamp, message = _split_timestamp(raw_line)
    is_json, message, level = None
    return PodLogLine(
        timestamp=timestamp, level=level, message=message, run_index=0, is_json=is_json
    )


def x__parse_line__mutmut_4(raw_line: str) -> PodLogLine:
    from hexawyn.domain.models.analyze_pod_logs import PodLogLine

    timestamp, message = _split_timestamp(raw_line)
    is_json, message, level = _parse_message(None)
    return PodLogLine(
        timestamp=timestamp, level=level, message=message, run_index=0, is_json=is_json
    )


def x__parse_line__mutmut_5(raw_line: str) -> PodLogLine:
    from hexawyn.domain.models.analyze_pod_logs import PodLogLine

    timestamp, message = _split_timestamp(raw_line)
    is_json, message, level = _parse_message(message)
    return PodLogLine(
        timestamp=None, level=level, message=message, run_index=0, is_json=is_json
    )


def x__parse_line__mutmut_6(raw_line: str) -> PodLogLine:
    from hexawyn.domain.models.analyze_pod_logs import PodLogLine

    timestamp, message = _split_timestamp(raw_line)
    is_json, message, level = _parse_message(message)
    return PodLogLine(
        timestamp=timestamp, level=None, message=message, run_index=0, is_json=is_json
    )


def x__parse_line__mutmut_7(raw_line: str) -> PodLogLine:
    from hexawyn.domain.models.analyze_pod_logs import PodLogLine

    timestamp, message = _split_timestamp(raw_line)
    is_json, message, level = _parse_message(message)
    return PodLogLine(
        timestamp=timestamp, level=level, message=None, run_index=0, is_json=is_json
    )


def x__parse_line__mutmut_8(raw_line: str) -> PodLogLine:
    from hexawyn.domain.models.analyze_pod_logs import PodLogLine

    timestamp, message = _split_timestamp(raw_line)
    is_json, message, level = _parse_message(message)
    return PodLogLine(
        timestamp=timestamp, level=level, message=message, run_index=None, is_json=is_json
    )


def x__parse_line__mutmut_9(raw_line: str) -> PodLogLine:
    from hexawyn.domain.models.analyze_pod_logs import PodLogLine

    timestamp, message = _split_timestamp(raw_line)
    is_json, message, level = _parse_message(message)
    return PodLogLine(
        timestamp=timestamp, level=level, message=message, run_index=0, is_json=None
    )


def x__parse_line__mutmut_10(raw_line: str) -> PodLogLine:
    from hexawyn.domain.models.analyze_pod_logs import PodLogLine

    timestamp, message = _split_timestamp(raw_line)
    is_json, message, level = _parse_message(message)
    return PodLogLine(
        level=level, message=message, run_index=0, is_json=is_json
    )


def x__parse_line__mutmut_11(raw_line: str) -> PodLogLine:
    from hexawyn.domain.models.analyze_pod_logs import PodLogLine

    timestamp, message = _split_timestamp(raw_line)
    is_json, message, level = _parse_message(message)
    return PodLogLine(
        timestamp=timestamp, message=message, run_index=0, is_json=is_json
    )


def x__parse_line__mutmut_12(raw_line: str) -> PodLogLine:
    from hexawyn.domain.models.analyze_pod_logs import PodLogLine

    timestamp, message = _split_timestamp(raw_line)
    is_json, message, level = _parse_message(message)
    return PodLogLine(
        timestamp=timestamp, level=level, run_index=0, is_json=is_json
    )


def x__parse_line__mutmut_13(raw_line: str) -> PodLogLine:
    from hexawyn.domain.models.analyze_pod_logs import PodLogLine

    timestamp, message = _split_timestamp(raw_line)
    is_json, message, level = _parse_message(message)
    return PodLogLine(
        timestamp=timestamp, level=level, message=message, is_json=is_json
    )


def x__parse_line__mutmut_14(raw_line: str) -> PodLogLine:
    from hexawyn.domain.models.analyze_pod_logs import PodLogLine

    timestamp, message = _split_timestamp(raw_line)
    is_json, message, level = _parse_message(message)
    return PodLogLine(
        timestamp=timestamp, level=level, message=message, run_index=0, )


def x__parse_line__mutmut_15(raw_line: str) -> PodLogLine:
    from hexawyn.domain.models.analyze_pod_logs import PodLogLine

    timestamp, message = _split_timestamp(raw_line)
    is_json, message, level = _parse_message(message)
    return PodLogLine(
        timestamp=timestamp, level=level, message=message, run_index=1, is_json=is_json
    )

mutants_x__parse_line__mutmut['_mutmut_orig'] = x__parse_line__mutmut_orig # type: ignore # mutmut generated
mutants_x__parse_line__mutmut['x__parse_line__mutmut_1'] = x__parse_line__mutmut_1 # type: ignore # mutmut generated
mutants_x__parse_line__mutmut['x__parse_line__mutmut_2'] = x__parse_line__mutmut_2 # type: ignore # mutmut generated
mutants_x__parse_line__mutmut['x__parse_line__mutmut_3'] = x__parse_line__mutmut_3 # type: ignore # mutmut generated
mutants_x__parse_line__mutmut['x__parse_line__mutmut_4'] = x__parse_line__mutmut_4 # type: ignore # mutmut generated
mutants_x__parse_line__mutmut['x__parse_line__mutmut_5'] = x__parse_line__mutmut_5 # type: ignore # mutmut generated
mutants_x__parse_line__mutmut['x__parse_line__mutmut_6'] = x__parse_line__mutmut_6 # type: ignore # mutmut generated
mutants_x__parse_line__mutmut['x__parse_line__mutmut_7'] = x__parse_line__mutmut_7 # type: ignore # mutmut generated
mutants_x__parse_line__mutmut['x__parse_line__mutmut_8'] = x__parse_line__mutmut_8 # type: ignore # mutmut generated
mutants_x__parse_line__mutmut['x__parse_line__mutmut_9'] = x__parse_line__mutmut_9 # type: ignore # mutmut generated
mutants_x__parse_line__mutmut['x__parse_line__mutmut_10'] = x__parse_line__mutmut_10 # type: ignore # mutmut generated
mutants_x__parse_line__mutmut['x__parse_line__mutmut_11'] = x__parse_line__mutmut_11 # type: ignore # mutmut generated
mutants_x__parse_line__mutmut['x__parse_line__mutmut_12'] = x__parse_line__mutmut_12 # type: ignore # mutmut generated
mutants_x__parse_line__mutmut['x__parse_line__mutmut_13'] = x__parse_line__mutmut_13 # type: ignore # mutmut generated
mutants_x__parse_line__mutmut['x__parse_line__mutmut_14'] = x__parse_line__mutmut_14 # type: ignore # mutmut generated
mutants_x__parse_line__mutmut['x__parse_line__mutmut_15'] = x__parse_line__mutmut_15 # type: ignore # mutmut generated
mutants_x__split_timestamp__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__split_timestamp__mutmut)
def _split_timestamp(raw_line: str) -> tuple[str, str]:
    token, _, rest = raw_line.partition(" ")
    if len(token) >= _MIN_TIMESTAMP_LENGTH and "T" in token:
        return token, rest
    return "", raw_line


def x__split_timestamp__mutmut_orig(raw_line: str) -> tuple[str, str]:
    token, _, rest = raw_line.partition(" ")
    if len(token) >= _MIN_TIMESTAMP_LENGTH and "T" in token:
        return token, rest
    return "", raw_line


def x__split_timestamp__mutmut_1(raw_line: str) -> tuple[str, str]:
    token, _, rest = None
    if len(token) >= _MIN_TIMESTAMP_LENGTH and "T" in token:
        return token, rest
    return "", raw_line


def x__split_timestamp__mutmut_2(raw_line: str) -> tuple[str, str]:
    token, _, rest = raw_line.partition(None)
    if len(token) >= _MIN_TIMESTAMP_LENGTH and "T" in token:
        return token, rest
    return "", raw_line


def x__split_timestamp__mutmut_3(raw_line: str) -> tuple[str, str]:
    token, _, rest = raw_line.rpartition(" ")
    if len(token) >= _MIN_TIMESTAMP_LENGTH and "T" in token:
        return token, rest
    return "", raw_line


def x__split_timestamp__mutmut_4(raw_line: str) -> tuple[str, str]:
    token, _, rest = raw_line.partition("XX XX")
    if len(token) >= _MIN_TIMESTAMP_LENGTH and "T" in token:
        return token, rest
    return "", raw_line


def x__split_timestamp__mutmut_5(raw_line: str) -> tuple[str, str]:
    token, _, rest = raw_line.partition(" ")
    if len(token) >= _MIN_TIMESTAMP_LENGTH or "T" in token:
        return token, rest
    return "", raw_line


def x__split_timestamp__mutmut_6(raw_line: str) -> tuple[str, str]:
    token, _, rest = raw_line.partition(" ")
    if len(token) > _MIN_TIMESTAMP_LENGTH and "T" in token:
        return token, rest
    return "", raw_line


def x__split_timestamp__mutmut_7(raw_line: str) -> tuple[str, str]:
    token, _, rest = raw_line.partition(" ")
    if len(token) >= _MIN_TIMESTAMP_LENGTH and "XXTXX" in token:
        return token, rest
    return "", raw_line


def x__split_timestamp__mutmut_8(raw_line: str) -> tuple[str, str]:
    token, _, rest = raw_line.partition(" ")
    if len(token) >= _MIN_TIMESTAMP_LENGTH and "t" in token:
        return token, rest
    return "", raw_line


def x__split_timestamp__mutmut_9(raw_line: str) -> tuple[str, str]:
    token, _, rest = raw_line.partition(" ")
    if len(token) >= _MIN_TIMESTAMP_LENGTH and "T" not in token:
        return token, rest
    return "", raw_line


def x__split_timestamp__mutmut_10(raw_line: str) -> tuple[str, str]:
    token, _, rest = raw_line.partition(" ")
    if len(token) >= _MIN_TIMESTAMP_LENGTH and "T" in token:
        return token, rest
    return "XXXX", raw_line

mutants_x__split_timestamp__mutmut['_mutmut_orig'] = x__split_timestamp__mutmut_orig # type: ignore # mutmut generated
mutants_x__split_timestamp__mutmut['x__split_timestamp__mutmut_1'] = x__split_timestamp__mutmut_1 # type: ignore # mutmut generated
mutants_x__split_timestamp__mutmut['x__split_timestamp__mutmut_2'] = x__split_timestamp__mutmut_2 # type: ignore # mutmut generated
mutants_x__split_timestamp__mutmut['x__split_timestamp__mutmut_3'] = x__split_timestamp__mutmut_3 # type: ignore # mutmut generated
mutants_x__split_timestamp__mutmut['x__split_timestamp__mutmut_4'] = x__split_timestamp__mutmut_4 # type: ignore # mutmut generated
mutants_x__split_timestamp__mutmut['x__split_timestamp__mutmut_5'] = x__split_timestamp__mutmut_5 # type: ignore # mutmut generated
mutants_x__split_timestamp__mutmut['x__split_timestamp__mutmut_6'] = x__split_timestamp__mutmut_6 # type: ignore # mutmut generated
mutants_x__split_timestamp__mutmut['x__split_timestamp__mutmut_7'] = x__split_timestamp__mutmut_7 # type: ignore # mutmut generated
mutants_x__split_timestamp__mutmut['x__split_timestamp__mutmut_8'] = x__split_timestamp__mutmut_8 # type: ignore # mutmut generated
mutants_x__split_timestamp__mutmut['x__split_timestamp__mutmut_9'] = x__split_timestamp__mutmut_9 # type: ignore # mutmut generated
mutants_x__split_timestamp__mutmut['x__split_timestamp__mutmut_10'] = x__split_timestamp__mutmut_10 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__parse_message__mutmut)
def _parse_message(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_orig(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_1(message: str) -> tuple[bool, str, str]:
    stripped = None
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_2(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") or stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_3(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith(None) and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_4(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("XX{XX") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_5(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith(None):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_6(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("XX}XX"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_7(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = None
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_8(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(None)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_9(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = ""
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_10(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = None
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_11(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(None)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_12(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") and stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_13(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") and data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_14(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") and data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_15(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get(None) or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_16(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("XXmsgXX") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_17(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("MSG") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_18(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get(None) or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_19(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("XXmessageXX") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_20(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("MESSAGE") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_21(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get(None) or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_22(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("XXerrorXX") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_23(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("ERROR") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_24(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = None
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_25(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").lower()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_26(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(None).upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_27(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") and "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_28(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") and data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_29(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get(None) or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_30(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("XXlevelXX") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_31(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("LEVEL") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_32(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get(None) or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_33(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("XXseverityXX") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_34(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("SEVERITY") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_35(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "XXXX").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_36(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return False, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_37(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level and _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_38(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(None)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_39(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return True, message, _detect_level(message)


def x__parse_message__mutmut_40(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(None)

mutants_x__parse_message__mutmut['_mutmut_orig'] = x__parse_message__mutmut_orig # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_1'] = x__parse_message__mutmut_1 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_2'] = x__parse_message__mutmut_2 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_3'] = x__parse_message__mutmut_3 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_4'] = x__parse_message__mutmut_4 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_5'] = x__parse_message__mutmut_5 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_6'] = x__parse_message__mutmut_6 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_7'] = x__parse_message__mutmut_7 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_8'] = x__parse_message__mutmut_8 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_9'] = x__parse_message__mutmut_9 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_10'] = x__parse_message__mutmut_10 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_11'] = x__parse_message__mutmut_11 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_12'] = x__parse_message__mutmut_12 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_13'] = x__parse_message__mutmut_13 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_14'] = x__parse_message__mutmut_14 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_15'] = x__parse_message__mutmut_15 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_16'] = x__parse_message__mutmut_16 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_17'] = x__parse_message__mutmut_17 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_18'] = x__parse_message__mutmut_18 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_19'] = x__parse_message__mutmut_19 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_20'] = x__parse_message__mutmut_20 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_21'] = x__parse_message__mutmut_21 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_22'] = x__parse_message__mutmut_22 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_23'] = x__parse_message__mutmut_23 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_24'] = x__parse_message__mutmut_24 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_25'] = x__parse_message__mutmut_25 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_26'] = x__parse_message__mutmut_26 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_27'] = x__parse_message__mutmut_27 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_28'] = x__parse_message__mutmut_28 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_29'] = x__parse_message__mutmut_29 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_30'] = x__parse_message__mutmut_30 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_31'] = x__parse_message__mutmut_31 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_32'] = x__parse_message__mutmut_32 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_33'] = x__parse_message__mutmut_33 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_34'] = x__parse_message__mutmut_34 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_35'] = x__parse_message__mutmut_35 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_36'] = x__parse_message__mutmut_36 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_37'] = x__parse_message__mutmut_37 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_38'] = x__parse_message__mutmut_38 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_39'] = x__parse_message__mutmut_39 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_40'] = x__parse_message__mutmut_40 # type: ignore # mutmut generated
mutants_x__detect_level__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__detect_level__mutmut)
def _detect_level(message: str) -> str:
    upper = message.upper()
    for keyword in _LEVEL_KEYWORDS:
        if keyword in upper:
            return "ERROR" if keyword == "FATAL" else keyword
    return "INFO"


def x__detect_level__mutmut_orig(message: str) -> str:
    upper = message.upper()
    for keyword in _LEVEL_KEYWORDS:
        if keyword in upper:
            return "ERROR" if keyword == "FATAL" else keyword
    return "INFO"


def x__detect_level__mutmut_1(message: str) -> str:
    upper = None
    for keyword in _LEVEL_KEYWORDS:
        if keyword in upper:
            return "ERROR" if keyword == "FATAL" else keyword
    return "INFO"


def x__detect_level__mutmut_2(message: str) -> str:
    upper = message.lower()
    for keyword in _LEVEL_KEYWORDS:
        if keyword in upper:
            return "ERROR" if keyword == "FATAL" else keyword
    return "INFO"


def x__detect_level__mutmut_3(message: str) -> str:
    upper = message.upper()
    for keyword in _LEVEL_KEYWORDS:
        if keyword not in upper:
            return "ERROR" if keyword == "FATAL" else keyword
    return "INFO"


def x__detect_level__mutmut_4(message: str) -> str:
    upper = message.upper()
    for keyword in _LEVEL_KEYWORDS:
        if keyword in upper:
            return "XXERRORXX" if keyword == "FATAL" else keyword
    return "INFO"


def x__detect_level__mutmut_5(message: str) -> str:
    upper = message.upper()
    for keyword in _LEVEL_KEYWORDS:
        if keyword in upper:
            return "error" if keyword == "FATAL" else keyword
    return "INFO"


def x__detect_level__mutmut_6(message: str) -> str:
    upper = message.upper()
    for keyword in _LEVEL_KEYWORDS:
        if keyword in upper:
            return "ERROR" if keyword != "FATAL" else keyword
    return "INFO"


def x__detect_level__mutmut_7(message: str) -> str:
    upper = message.upper()
    for keyword in _LEVEL_KEYWORDS:
        if keyword in upper:
            return "ERROR" if keyword == "XXFATALXX" else keyword
    return "INFO"


def x__detect_level__mutmut_8(message: str) -> str:
    upper = message.upper()
    for keyword in _LEVEL_KEYWORDS:
        if keyword in upper:
            return "ERROR" if keyword == "fatal" else keyword
    return "INFO"


def x__detect_level__mutmut_9(message: str) -> str:
    upper = message.upper()
    for keyword in _LEVEL_KEYWORDS:
        if keyword in upper:
            return "ERROR" if keyword == "FATAL" else keyword
    return "XXINFOXX"


def x__detect_level__mutmut_10(message: str) -> str:
    upper = message.upper()
    for keyword in _LEVEL_KEYWORDS:
        if keyword in upper:
            return "ERROR" if keyword == "FATAL" else keyword
    return "info"

mutants_x__detect_level__mutmut['_mutmut_orig'] = x__detect_level__mutmut_orig # type: ignore # mutmut generated
mutants_x__detect_level__mutmut['x__detect_level__mutmut_1'] = x__detect_level__mutmut_1 # type: ignore # mutmut generated
mutants_x__detect_level__mutmut['x__detect_level__mutmut_2'] = x__detect_level__mutmut_2 # type: ignore # mutmut generated
mutants_x__detect_level__mutmut['x__detect_level__mutmut_3'] = x__detect_level__mutmut_3 # type: ignore # mutmut generated
mutants_x__detect_level__mutmut['x__detect_level__mutmut_4'] = x__detect_level__mutmut_4 # type: ignore # mutmut generated
mutants_x__detect_level__mutmut['x__detect_level__mutmut_5'] = x__detect_level__mutmut_5 # type: ignore # mutmut generated
mutants_x__detect_level__mutmut['x__detect_level__mutmut_6'] = x__detect_level__mutmut_6 # type: ignore # mutmut generated
mutants_x__detect_level__mutmut['x__detect_level__mutmut_7'] = x__detect_level__mutmut_7 # type: ignore # mutmut generated
mutants_x__detect_level__mutmut['x__detect_level__mutmut_8'] = x__detect_level__mutmut_8 # type: ignore # mutmut generated
mutants_x__detect_level__mutmut['x__detect_level__mutmut_9'] = x__detect_level__mutmut_9 # type: ignore # mutmut generated
mutants_x__detect_level__mutmut['x__detect_level__mutmut_10'] = x__detect_level__mutmut_10 # type: ignore # mutmut generated
