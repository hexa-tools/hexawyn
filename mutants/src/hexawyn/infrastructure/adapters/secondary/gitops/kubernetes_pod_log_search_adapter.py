from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driven.log_search_port import LogSearchPort, RawContainerLog
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    InsufficientPermissionsError,
    ResourceNotFoundError,
)

if TYPE_CHECKING:
    from kubernetes.client import CoreV1Api

_K8S_FORBIDDEN = 403
_K8S_NOT_FOUND = 404
_MAX_TAIL_LINES = 5000


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut: MutantDict = {}  # type: ignore


class KubernetesPodLogSearchAdapter(LogSearchPort):
    """Secondary adapter — reads every container's logs for one pod, tail-
    truncated server-side (`tail_lines`) since this feature scans every pod
    in the cluster, unlike the single-pod `analyze_pod_logs` adapter."""

    @_mutmut_mutated(mutants_xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut)
    def fetch_pod_container_logs(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod = core_api.read_namespaced_pod(name=pod_name, namespace=namespace)
        except Exception as exc:
            raise _translate_pod_error(exc, pod_name, namespace) from exc

        since_seconds = time_window_minutes * 60
        container_names = [container.name for container in pod.spec.containers]

        return [
            self._read_container_log(core_api, pod_name, namespace, container_name, since_seconds)
            for container_name in container_names
        ]

    def xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_orig(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod = core_api.read_namespaced_pod(name=pod_name, namespace=namespace)
        except Exception as exc:
            raise _translate_pod_error(exc, pod_name, namespace) from exc

        since_seconds = time_window_minutes * 60
        container_names = [container.name for container in pod.spec.containers]

        return [
            self._read_container_log(core_api, pod_name, namespace, container_name, since_seconds)
            for container_name in container_names
        ]

    def xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_1(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from kubernetes import client as k8s

        core_api = None
        try:
            pod = core_api.read_namespaced_pod(name=pod_name, namespace=namespace)
        except Exception as exc:
            raise _translate_pod_error(exc, pod_name, namespace) from exc

        since_seconds = time_window_minutes * 60
        container_names = [container.name for container in pod.spec.containers]

        return [
            self._read_container_log(core_api, pod_name, namespace, container_name, since_seconds)
            for container_name in container_names
        ]

    def xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_2(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod = None
        except Exception as exc:
            raise _translate_pod_error(exc, pod_name, namespace) from exc

        since_seconds = time_window_minutes * 60
        container_names = [container.name for container in pod.spec.containers]

        return [
            self._read_container_log(core_api, pod_name, namespace, container_name, since_seconds)
            for container_name in container_names
        ]

    def xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_3(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod = core_api.read_namespaced_pod(name=None, namespace=namespace)
        except Exception as exc:
            raise _translate_pod_error(exc, pod_name, namespace) from exc

        since_seconds = time_window_minutes * 60
        container_names = [container.name for container in pod.spec.containers]

        return [
            self._read_container_log(core_api, pod_name, namespace, container_name, since_seconds)
            for container_name in container_names
        ]

    def xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_4(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod = core_api.read_namespaced_pod(name=pod_name, namespace=None)
        except Exception as exc:
            raise _translate_pod_error(exc, pod_name, namespace) from exc

        since_seconds = time_window_minutes * 60
        container_names = [container.name for container in pod.spec.containers]

        return [
            self._read_container_log(core_api, pod_name, namespace, container_name, since_seconds)
            for container_name in container_names
        ]

    def xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_5(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod = core_api.read_namespaced_pod(namespace=namespace)
        except Exception as exc:
            raise _translate_pod_error(exc, pod_name, namespace) from exc

        since_seconds = time_window_minutes * 60
        container_names = [container.name for container in pod.spec.containers]

        return [
            self._read_container_log(core_api, pod_name, namespace, container_name, since_seconds)
            for container_name in container_names
        ]

    def xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_6(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod = core_api.read_namespaced_pod(name=pod_name, )
        except Exception as exc:
            raise _translate_pod_error(exc, pod_name, namespace) from exc

        since_seconds = time_window_minutes * 60
        container_names = [container.name for container in pod.spec.containers]

        return [
            self._read_container_log(core_api, pod_name, namespace, container_name, since_seconds)
            for container_name in container_names
        ]

    def xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_7(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod = core_api.read_namespaced_pod(name=pod_name, namespace=namespace)
        except Exception as exc:
            raise _translate_pod_error(None, pod_name, namespace) from exc

        since_seconds = time_window_minutes * 60
        container_names = [container.name for container in pod.spec.containers]

        return [
            self._read_container_log(core_api, pod_name, namespace, container_name, since_seconds)
            for container_name in container_names
        ]

    def xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_8(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod = core_api.read_namespaced_pod(name=pod_name, namespace=namespace)
        except Exception as exc:
            raise _translate_pod_error(exc, None, namespace) from exc

        since_seconds = time_window_minutes * 60
        container_names = [container.name for container in pod.spec.containers]

        return [
            self._read_container_log(core_api, pod_name, namespace, container_name, since_seconds)
            for container_name in container_names
        ]

    def xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_9(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod = core_api.read_namespaced_pod(name=pod_name, namespace=namespace)
        except Exception as exc:
            raise _translate_pod_error(exc, pod_name, None) from exc

        since_seconds = time_window_minutes * 60
        container_names = [container.name for container in pod.spec.containers]

        return [
            self._read_container_log(core_api, pod_name, namespace, container_name, since_seconds)
            for container_name in container_names
        ]

    def xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_10(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod = core_api.read_namespaced_pod(name=pod_name, namespace=namespace)
        except Exception as exc:
            raise _translate_pod_error(pod_name, namespace) from exc

        since_seconds = time_window_minutes * 60
        container_names = [container.name for container in pod.spec.containers]

        return [
            self._read_container_log(core_api, pod_name, namespace, container_name, since_seconds)
            for container_name in container_names
        ]

    def xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_11(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod = core_api.read_namespaced_pod(name=pod_name, namespace=namespace)
        except Exception as exc:
            raise _translate_pod_error(exc, namespace) from exc

        since_seconds = time_window_minutes * 60
        container_names = [container.name for container in pod.spec.containers]

        return [
            self._read_container_log(core_api, pod_name, namespace, container_name, since_seconds)
            for container_name in container_names
        ]

    def xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_12(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod = core_api.read_namespaced_pod(name=pod_name, namespace=namespace)
        except Exception as exc:
            raise _translate_pod_error(exc, pod_name, ) from exc

        since_seconds = time_window_minutes * 60
        container_names = [container.name for container in pod.spec.containers]

        return [
            self._read_container_log(core_api, pod_name, namespace, container_name, since_seconds)
            for container_name in container_names
        ]

    def xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_13(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod = core_api.read_namespaced_pod(name=pod_name, namespace=namespace)
        except Exception as exc:
            raise _translate_pod_error(exc, pod_name, namespace) from exc

        since_seconds = None
        container_names = [container.name for container in pod.spec.containers]

        return [
            self._read_container_log(core_api, pod_name, namespace, container_name, since_seconds)
            for container_name in container_names
        ]

    def xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_14(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod = core_api.read_namespaced_pod(name=pod_name, namespace=namespace)
        except Exception as exc:
            raise _translate_pod_error(exc, pod_name, namespace) from exc

        since_seconds = time_window_minutes / 60
        container_names = [container.name for container in pod.spec.containers]

        return [
            self._read_container_log(core_api, pod_name, namespace, container_name, since_seconds)
            for container_name in container_names
        ]

    def xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_15(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod = core_api.read_namespaced_pod(name=pod_name, namespace=namespace)
        except Exception as exc:
            raise _translate_pod_error(exc, pod_name, namespace) from exc

        since_seconds = time_window_minutes * 61
        container_names = [container.name for container in pod.spec.containers]

        return [
            self._read_container_log(core_api, pod_name, namespace, container_name, since_seconds)
            for container_name in container_names
        ]

    def xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_16(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod = core_api.read_namespaced_pod(name=pod_name, namespace=namespace)
        except Exception as exc:
            raise _translate_pod_error(exc, pod_name, namespace) from exc

        since_seconds = time_window_minutes * 60
        container_names = None

        return [
            self._read_container_log(core_api, pod_name, namespace, container_name, since_seconds)
            for container_name in container_names
        ]

    def xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_17(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod = core_api.read_namespaced_pod(name=pod_name, namespace=namespace)
        except Exception as exc:
            raise _translate_pod_error(exc, pod_name, namespace) from exc

        since_seconds = time_window_minutes * 60
        container_names = [container.name for container in pod.spec.containers]

        return [
            self._read_container_log(None, pod_name, namespace, container_name, since_seconds)
            for container_name in container_names
        ]

    def xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_18(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod = core_api.read_namespaced_pod(name=pod_name, namespace=namespace)
        except Exception as exc:
            raise _translate_pod_error(exc, pod_name, namespace) from exc

        since_seconds = time_window_minutes * 60
        container_names = [container.name for container in pod.spec.containers]

        return [
            self._read_container_log(core_api, None, namespace, container_name, since_seconds)
            for container_name in container_names
        ]

    def xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_19(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod = core_api.read_namespaced_pod(name=pod_name, namespace=namespace)
        except Exception as exc:
            raise _translate_pod_error(exc, pod_name, namespace) from exc

        since_seconds = time_window_minutes * 60
        container_names = [container.name for container in pod.spec.containers]

        return [
            self._read_container_log(core_api, pod_name, None, container_name, since_seconds)
            for container_name in container_names
        ]

    def xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_20(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod = core_api.read_namespaced_pod(name=pod_name, namespace=namespace)
        except Exception as exc:
            raise _translate_pod_error(exc, pod_name, namespace) from exc

        since_seconds = time_window_minutes * 60
        container_names = [container.name for container in pod.spec.containers]

        return [
            self._read_container_log(core_api, pod_name, namespace, None, since_seconds)
            for container_name in container_names
        ]

    def xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_21(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod = core_api.read_namespaced_pod(name=pod_name, namespace=namespace)
        except Exception as exc:
            raise _translate_pod_error(exc, pod_name, namespace) from exc

        since_seconds = time_window_minutes * 60
        container_names = [container.name for container in pod.spec.containers]

        return [
            self._read_container_log(core_api, pod_name, namespace, container_name, None)
            for container_name in container_names
        ]

    def xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_22(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod = core_api.read_namespaced_pod(name=pod_name, namespace=namespace)
        except Exception as exc:
            raise _translate_pod_error(exc, pod_name, namespace) from exc

        since_seconds = time_window_minutes * 60
        container_names = [container.name for container in pod.spec.containers]

        return [
            self._read_container_log(pod_name, namespace, container_name, since_seconds)
            for container_name in container_names
        ]

    def xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_23(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod = core_api.read_namespaced_pod(name=pod_name, namespace=namespace)
        except Exception as exc:
            raise _translate_pod_error(exc, pod_name, namespace) from exc

        since_seconds = time_window_minutes * 60
        container_names = [container.name for container in pod.spec.containers]

        return [
            self._read_container_log(core_api, namespace, container_name, since_seconds)
            for container_name in container_names
        ]

    def xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_24(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod = core_api.read_namespaced_pod(name=pod_name, namespace=namespace)
        except Exception as exc:
            raise _translate_pod_error(exc, pod_name, namespace) from exc

        since_seconds = time_window_minutes * 60
        container_names = [container.name for container in pod.spec.containers]

        return [
            self._read_container_log(core_api, pod_name, container_name, since_seconds)
            for container_name in container_names
        ]

    def xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_25(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod = core_api.read_namespaced_pod(name=pod_name, namespace=namespace)
        except Exception as exc:
            raise _translate_pod_error(exc, pod_name, namespace) from exc

        since_seconds = time_window_minutes * 60
        container_names = [container.name for container in pod.spec.containers]

        return [
            self._read_container_log(core_api, pod_name, namespace, since_seconds)
            for container_name in container_names
        ]

    def xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_26(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod = core_api.read_namespaced_pod(name=pod_name, namespace=namespace)
        except Exception as exc:
            raise _translate_pod_error(exc, pod_name, namespace) from exc

        since_seconds = time_window_minutes * 60
        container_names = [container.name for container in pod.spec.containers]

        return [
            self._read_container_log(core_api, pod_name, namespace, container_name, )
            for container_name in container_names
        ]

    @_mutmut_mutated(mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut)
    def _read_container_log(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                container=container_name,
                since_seconds=since_seconds,
                tail_lines=_MAX_TAIL_LINES,
                timestamps=True,
                _preload_content=False,
            )
        except Exception:
            return RawContainerLog(container=container_name, lines=[], truncated=False)

        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=container_name, lines=lines, truncated=len(lines) >= _MAX_TAIL_LINES
        )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_orig(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                container=container_name,
                since_seconds=since_seconds,
                tail_lines=_MAX_TAIL_LINES,
                timestamps=True,
                _preload_content=False,
            )
        except Exception:
            return RawContainerLog(container=container_name, lines=[], truncated=False)

        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=container_name, lines=lines, truncated=len(lines) >= _MAX_TAIL_LINES
        )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_1(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = None
        except Exception:
            return RawContainerLog(container=container_name, lines=[], truncated=False)

        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=container_name, lines=lines, truncated=len(lines) >= _MAX_TAIL_LINES
        )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_2(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=None,
                namespace=namespace,
                container=container_name,
                since_seconds=since_seconds,
                tail_lines=_MAX_TAIL_LINES,
                timestamps=True,
                _preload_content=False,
            )
        except Exception:
            return RawContainerLog(container=container_name, lines=[], truncated=False)

        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=container_name, lines=lines, truncated=len(lines) >= _MAX_TAIL_LINES
        )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_3(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=None,
                container=container_name,
                since_seconds=since_seconds,
                tail_lines=_MAX_TAIL_LINES,
                timestamps=True,
                _preload_content=False,
            )
        except Exception:
            return RawContainerLog(container=container_name, lines=[], truncated=False)

        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=container_name, lines=lines, truncated=len(lines) >= _MAX_TAIL_LINES
        )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_4(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                container=None,
                since_seconds=since_seconds,
                tail_lines=_MAX_TAIL_LINES,
                timestamps=True,
                _preload_content=False,
            )
        except Exception:
            return RawContainerLog(container=container_name, lines=[], truncated=False)

        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=container_name, lines=lines, truncated=len(lines) >= _MAX_TAIL_LINES
        )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_5(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                container=container_name,
                since_seconds=None,
                tail_lines=_MAX_TAIL_LINES,
                timestamps=True,
                _preload_content=False,
            )
        except Exception:
            return RawContainerLog(container=container_name, lines=[], truncated=False)

        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=container_name, lines=lines, truncated=len(lines) >= _MAX_TAIL_LINES
        )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_6(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                container=container_name,
                since_seconds=since_seconds,
                tail_lines=None,
                timestamps=True,
                _preload_content=False,
            )
        except Exception:
            return RawContainerLog(container=container_name, lines=[], truncated=False)

        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=container_name, lines=lines, truncated=len(lines) >= _MAX_TAIL_LINES
        )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_7(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                container=container_name,
                since_seconds=since_seconds,
                tail_lines=_MAX_TAIL_LINES,
                timestamps=None,
                _preload_content=False,
            )
        except Exception:
            return RawContainerLog(container=container_name, lines=[], truncated=False)

        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=container_name, lines=lines, truncated=len(lines) >= _MAX_TAIL_LINES
        )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_8(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                container=container_name,
                since_seconds=since_seconds,
                tail_lines=_MAX_TAIL_LINES,
                timestamps=True,
                _preload_content=None,
            )
        except Exception:
            return RawContainerLog(container=container_name, lines=[], truncated=False)

        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=container_name, lines=lines, truncated=len(lines) >= _MAX_TAIL_LINES
        )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_9(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                namespace=namespace,
                container=container_name,
                since_seconds=since_seconds,
                tail_lines=_MAX_TAIL_LINES,
                timestamps=True,
                _preload_content=False,
            )
        except Exception:
            return RawContainerLog(container=container_name, lines=[], truncated=False)

        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=container_name, lines=lines, truncated=len(lines) >= _MAX_TAIL_LINES
        )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_10(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=pod_name,
                container=container_name,
                since_seconds=since_seconds,
                tail_lines=_MAX_TAIL_LINES,
                timestamps=True,
                _preload_content=False,
            )
        except Exception:
            return RawContainerLog(container=container_name, lines=[], truncated=False)

        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=container_name, lines=lines, truncated=len(lines) >= _MAX_TAIL_LINES
        )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_11(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                since_seconds=since_seconds,
                tail_lines=_MAX_TAIL_LINES,
                timestamps=True,
                _preload_content=False,
            )
        except Exception:
            return RawContainerLog(container=container_name, lines=[], truncated=False)

        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=container_name, lines=lines, truncated=len(lines) >= _MAX_TAIL_LINES
        )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_12(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                container=container_name,
                tail_lines=_MAX_TAIL_LINES,
                timestamps=True,
                _preload_content=False,
            )
        except Exception:
            return RawContainerLog(container=container_name, lines=[], truncated=False)

        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=container_name, lines=lines, truncated=len(lines) >= _MAX_TAIL_LINES
        )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_13(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                container=container_name,
                since_seconds=since_seconds,
                timestamps=True,
                _preload_content=False,
            )
        except Exception:
            return RawContainerLog(container=container_name, lines=[], truncated=False)

        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=container_name, lines=lines, truncated=len(lines) >= _MAX_TAIL_LINES
        )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_14(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                container=container_name,
                since_seconds=since_seconds,
                tail_lines=_MAX_TAIL_LINES,
                _preload_content=False,
            )
        except Exception:
            return RawContainerLog(container=container_name, lines=[], truncated=False)

        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=container_name, lines=lines, truncated=len(lines) >= _MAX_TAIL_LINES
        )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_15(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                container=container_name,
                since_seconds=since_seconds,
                tail_lines=_MAX_TAIL_LINES,
                timestamps=True,
                )
        except Exception:
            return RawContainerLog(container=container_name, lines=[], truncated=False)

        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=container_name, lines=lines, truncated=len(lines) >= _MAX_TAIL_LINES
        )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_16(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                container=container_name,
                since_seconds=since_seconds,
                tail_lines=_MAX_TAIL_LINES,
                timestamps=False,
                _preload_content=False,
            )
        except Exception:
            return RawContainerLog(container=container_name, lines=[], truncated=False)

        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=container_name, lines=lines, truncated=len(lines) >= _MAX_TAIL_LINES
        )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_17(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                container=container_name,
                since_seconds=since_seconds,
                tail_lines=_MAX_TAIL_LINES,
                timestamps=True,
                _preload_content=True,
            )
        except Exception:
            return RawContainerLog(container=container_name, lines=[], truncated=False)

        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=container_name, lines=lines, truncated=len(lines) >= _MAX_TAIL_LINES
        )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_18(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                container=container_name,
                since_seconds=since_seconds,
                tail_lines=_MAX_TAIL_LINES,
                timestamps=True,
                _preload_content=False,
            )
        except Exception:
            return RawContainerLog(container=None, lines=[], truncated=False)

        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=container_name, lines=lines, truncated=len(lines) >= _MAX_TAIL_LINES
        )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_19(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                container=container_name,
                since_seconds=since_seconds,
                tail_lines=_MAX_TAIL_LINES,
                timestamps=True,
                _preload_content=False,
            )
        except Exception:
            return RawContainerLog(container=container_name, lines=None, truncated=False)

        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=container_name, lines=lines, truncated=len(lines) >= _MAX_TAIL_LINES
        )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_20(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                container=container_name,
                since_seconds=since_seconds,
                tail_lines=_MAX_TAIL_LINES,
                timestamps=True,
                _preload_content=False,
            )
        except Exception:
            return RawContainerLog(container=container_name, lines=[], truncated=None)

        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=container_name, lines=lines, truncated=len(lines) >= _MAX_TAIL_LINES
        )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_21(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                container=container_name,
                since_seconds=since_seconds,
                tail_lines=_MAX_TAIL_LINES,
                timestamps=True,
                _preload_content=False,
            )
        except Exception:
            return RawContainerLog(lines=[], truncated=False)

        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=container_name, lines=lines, truncated=len(lines) >= _MAX_TAIL_LINES
        )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_22(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                container=container_name,
                since_seconds=since_seconds,
                tail_lines=_MAX_TAIL_LINES,
                timestamps=True,
                _preload_content=False,
            )
        except Exception:
            return RawContainerLog(container=container_name, truncated=False)

        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=container_name, lines=lines, truncated=len(lines) >= _MAX_TAIL_LINES
        )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_23(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                container=container_name,
                since_seconds=since_seconds,
                tail_lines=_MAX_TAIL_LINES,
                timestamps=True,
                _preload_content=False,
            )
        except Exception:
            return RawContainerLog(container=container_name, lines=[], )

        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=container_name, lines=lines, truncated=len(lines) >= _MAX_TAIL_LINES
        )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_24(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                container=container_name,
                since_seconds=since_seconds,
                tail_lines=_MAX_TAIL_LINES,
                timestamps=True,
                _preload_content=False,
            )
        except Exception:
            return RawContainerLog(container=container_name, lines=[], truncated=True)

        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=container_name, lines=lines, truncated=len(lines) >= _MAX_TAIL_LINES
        )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_25(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                container=container_name,
                since_seconds=since_seconds,
                tail_lines=_MAX_TAIL_LINES,
                timestamps=True,
                _preload_content=False,
            )
        except Exception:
            return RawContainerLog(container=container_name, lines=[], truncated=False)

        raw_bytes: bytes = None
        text = raw_bytes.decode("utf-8", errors="replace")
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=container_name, lines=lines, truncated=len(lines) >= _MAX_TAIL_LINES
        )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_26(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                container=container_name,
                since_seconds=since_seconds,
                tail_lines=_MAX_TAIL_LINES,
                timestamps=True,
                _preload_content=False,
            )
        except Exception:
            return RawContainerLog(container=container_name, lines=[], truncated=False)

        raw_bytes: bytes = response.data
        text = None
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=container_name, lines=lines, truncated=len(lines) >= _MAX_TAIL_LINES
        )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_27(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                container=container_name,
                since_seconds=since_seconds,
                tail_lines=_MAX_TAIL_LINES,
                timestamps=True,
                _preload_content=False,
            )
        except Exception:
            return RawContainerLog(container=container_name, lines=[], truncated=False)

        raw_bytes: bytes = response.data
        text = raw_bytes.decode(None, errors="replace")
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=container_name, lines=lines, truncated=len(lines) >= _MAX_TAIL_LINES
        )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_28(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                container=container_name,
                since_seconds=since_seconds,
                tail_lines=_MAX_TAIL_LINES,
                timestamps=True,
                _preload_content=False,
            )
        except Exception:
            return RawContainerLog(container=container_name, lines=[], truncated=False)

        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors=None)
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=container_name, lines=lines, truncated=len(lines) >= _MAX_TAIL_LINES
        )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_29(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                container=container_name,
                since_seconds=since_seconds,
                tail_lines=_MAX_TAIL_LINES,
                timestamps=True,
                _preload_content=False,
            )
        except Exception:
            return RawContainerLog(container=container_name, lines=[], truncated=False)

        raw_bytes: bytes = response.data
        text = raw_bytes.decode(errors="replace")
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=container_name, lines=lines, truncated=len(lines) >= _MAX_TAIL_LINES
        )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_30(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                container=container_name,
                since_seconds=since_seconds,
                tail_lines=_MAX_TAIL_LINES,
                timestamps=True,
                _preload_content=False,
            )
        except Exception:
            return RawContainerLog(container=container_name, lines=[], truncated=False)

        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", )
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=container_name, lines=lines, truncated=len(lines) >= _MAX_TAIL_LINES
        )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_31(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                container=container_name,
                since_seconds=since_seconds,
                tail_lines=_MAX_TAIL_LINES,
                timestamps=True,
                _preload_content=False,
            )
        except Exception:
            return RawContainerLog(container=container_name, lines=[], truncated=False)

        raw_bytes: bytes = response.data
        text = raw_bytes.decode("XXutf-8XX", errors="replace")
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=container_name, lines=lines, truncated=len(lines) >= _MAX_TAIL_LINES
        )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_32(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                container=container_name,
                since_seconds=since_seconds,
                tail_lines=_MAX_TAIL_LINES,
                timestamps=True,
                _preload_content=False,
            )
        except Exception:
            return RawContainerLog(container=container_name, lines=[], truncated=False)

        raw_bytes: bytes = response.data
        text = raw_bytes.decode("UTF-8", errors="replace")
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=container_name, lines=lines, truncated=len(lines) >= _MAX_TAIL_LINES
        )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_33(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                container=container_name,
                since_seconds=since_seconds,
                tail_lines=_MAX_TAIL_LINES,
                timestamps=True,
                _preload_content=False,
            )
        except Exception:
            return RawContainerLog(container=container_name, lines=[], truncated=False)

        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="XXreplaceXX")
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=container_name, lines=lines, truncated=len(lines) >= _MAX_TAIL_LINES
        )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_34(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                container=container_name,
                since_seconds=since_seconds,
                tail_lines=_MAX_TAIL_LINES,
                timestamps=True,
                _preload_content=False,
            )
        except Exception:
            return RawContainerLog(container=container_name, lines=[], truncated=False)

        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="REPLACE")
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=container_name, lines=lines, truncated=len(lines) >= _MAX_TAIL_LINES
        )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_35(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                container=container_name,
                since_seconds=since_seconds,
                tail_lines=_MAX_TAIL_LINES,
                timestamps=True,
                _preload_content=False,
            )
        except Exception:
            return RawContainerLog(container=container_name, lines=[], truncated=False)

        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        lines = None
        return RawContainerLog(
            container=container_name, lines=lines, truncated=len(lines) >= _MAX_TAIL_LINES
        )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_36(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                container=container_name,
                since_seconds=since_seconds,
                tail_lines=_MAX_TAIL_LINES,
                timestamps=True,
                _preload_content=False,
            )
        except Exception:
            return RawContainerLog(container=container_name, lines=[], truncated=False)

        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=None, lines=lines, truncated=len(lines) >= _MAX_TAIL_LINES
        )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_37(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                container=container_name,
                since_seconds=since_seconds,
                tail_lines=_MAX_TAIL_LINES,
                timestamps=True,
                _preload_content=False,
            )
        except Exception:
            return RawContainerLog(container=container_name, lines=[], truncated=False)

        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=container_name, lines=None, truncated=len(lines) >= _MAX_TAIL_LINES
        )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_38(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                container=container_name,
                since_seconds=since_seconds,
                tail_lines=_MAX_TAIL_LINES,
                timestamps=True,
                _preload_content=False,
            )
        except Exception:
            return RawContainerLog(container=container_name, lines=[], truncated=False)

        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=container_name, lines=lines, truncated=None
        )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_39(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                container=container_name,
                since_seconds=since_seconds,
                tail_lines=_MAX_TAIL_LINES,
                timestamps=True,
                _preload_content=False,
            )
        except Exception:
            return RawContainerLog(container=container_name, lines=[], truncated=False)

        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            lines=lines, truncated=len(lines) >= _MAX_TAIL_LINES
        )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_40(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                container=container_name,
                since_seconds=since_seconds,
                tail_lines=_MAX_TAIL_LINES,
                timestamps=True,
                _preload_content=False,
            )
        except Exception:
            return RawContainerLog(container=container_name, lines=[], truncated=False)

        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=container_name, truncated=len(lines) >= _MAX_TAIL_LINES
        )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_41(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                container=container_name,
                since_seconds=since_seconds,
                tail_lines=_MAX_TAIL_LINES,
                timestamps=True,
                _preload_content=False,
            )
        except Exception:
            return RawContainerLog(container=container_name, lines=[], truncated=False)

        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=container_name, lines=lines, )

    def xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_42(  # noqa: PLR0913
        self,
        core_api: CoreV1Api,
        pod_name: str,
        namespace: str,
        container_name: str,
        since_seconds: int,
    ) -> RawContainerLog:
        try:
            response = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                container=container_name,
                since_seconds=since_seconds,
                tail_lines=_MAX_TAIL_LINES,
                timestamps=True,
                _preload_content=False,
            )
        except Exception:
            return RawContainerLog(container=container_name, lines=[], truncated=False)

        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        lines = [line for line in text.splitlines() if line.strip()]
        return RawContainerLog(
            container=container_name, lines=lines, truncated=len(lines) > _MAX_TAIL_LINES
        )

mutants_xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut['_mutmut_orig'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut['xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_1'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut['xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_2'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut['xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_3'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut['xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_4'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut['xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_5'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut['xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_6'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut['xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_7'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut['xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_8'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut['xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_9'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut['xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_10'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut['xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_11'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut['xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_12'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut['xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_13'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut['xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_14'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_14 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut['xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_15'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_15 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut['xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_16'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_16 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut['xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_17'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_17 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut['xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_18'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_18 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut['xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_19'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_19 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut['xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_20'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_20 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut['xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_21'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_21 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut['xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_22'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_22 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut['xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_23'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_23 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut['xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_24'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_24 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut['xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_25'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_25 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut['xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_26'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁfetch_pod_container_logs__mutmut_26 # type: ignore # mutmut generated

mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['_mutmut_orig'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_1'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_2'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_3'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_4'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_5'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_6'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_7'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_8'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_9'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_10'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_11'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_12'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_13'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_14'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_14 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_15'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_15 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_16'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_16 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_17'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_17 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_18'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_18 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_19'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_19 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_20'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_20 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_21'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_21 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_22'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_22 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_23'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_23 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_24'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_24 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_25'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_25 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_26'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_26 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_27'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_27 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_28'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_28 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_29'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_29 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_30'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_30 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_31'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_31 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_32'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_32 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_33'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_33 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_34'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_34 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_35'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_35 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_36'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_36 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_37'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_37 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_38'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_38 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_39'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_39 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_40'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_40 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_41'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_41 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut['xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_42'] = KubernetesPodLogSearchAdapter.xǁKubernetesPodLogSearchAdapterǁ_read_container_log__mutmut_42 # type: ignore # mutmut generated
mutants_x__translate_pod_error__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__translate_pod_error__mutmut)
def _translate_pod_error(exc: Exception, pod_name: str, namespace: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"pod_name": pod_name, "namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {pod_name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to pod {pod_name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot read pod {pod_name!r}: {exc}")


def x__translate_pod_error__mutmut_orig(exc: Exception, pod_name: str, namespace: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"pod_name": pod_name, "namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {pod_name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to pod {pod_name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot read pod {pod_name!r}: {exc}")


def x__translate_pod_error__mutmut_1(exc: Exception, pod_name: str, namespace: str) -> Exception:
    status = None
    context = {"pod_name": pod_name, "namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {pod_name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to pod {pod_name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot read pod {pod_name!r}: {exc}")


def x__translate_pod_error__mutmut_2(exc: Exception, pod_name: str, namespace: str) -> Exception:
    status = getattr(None, "status", None)
    context = {"pod_name": pod_name, "namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {pod_name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to pod {pod_name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot read pod {pod_name!r}: {exc}")


def x__translate_pod_error__mutmut_3(exc: Exception, pod_name: str, namespace: str) -> Exception:
    status = getattr(exc, None, None)
    context = {"pod_name": pod_name, "namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {pod_name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to pod {pod_name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot read pod {pod_name!r}: {exc}")


def x__translate_pod_error__mutmut_4(exc: Exception, pod_name: str, namespace: str) -> Exception:
    status = getattr("status", None)
    context = {"pod_name": pod_name, "namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {pod_name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to pod {pod_name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot read pod {pod_name!r}: {exc}")


def x__translate_pod_error__mutmut_5(exc: Exception, pod_name: str, namespace: str) -> Exception:
    status = getattr(exc, None)
    context = {"pod_name": pod_name, "namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {pod_name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to pod {pod_name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot read pod {pod_name!r}: {exc}")


def x__translate_pod_error__mutmut_6(exc: Exception, pod_name: str, namespace: str) -> Exception:
    status = getattr(exc, "status", )
    context = {"pod_name": pod_name, "namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {pod_name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to pod {pod_name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot read pod {pod_name!r}: {exc}")


def x__translate_pod_error__mutmut_7(exc: Exception, pod_name: str, namespace: str) -> Exception:
    status = getattr(exc, "XXstatusXX", None)
    context = {"pod_name": pod_name, "namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {pod_name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to pod {pod_name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot read pod {pod_name!r}: {exc}")


def x__translate_pod_error__mutmut_8(exc: Exception, pod_name: str, namespace: str) -> Exception:
    status = getattr(exc, "STATUS", None)
    context = {"pod_name": pod_name, "namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {pod_name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to pod {pod_name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot read pod {pod_name!r}: {exc}")


def x__translate_pod_error__mutmut_9(exc: Exception, pod_name: str, namespace: str) -> Exception:
    status = getattr(exc, "status", None)
    context = None
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {pod_name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to pod {pod_name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot read pod {pod_name!r}: {exc}")


def x__translate_pod_error__mutmut_10(exc: Exception, pod_name: str, namespace: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"XXpod_nameXX": pod_name, "namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {pod_name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to pod {pod_name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot read pod {pod_name!r}: {exc}")


def x__translate_pod_error__mutmut_11(exc: Exception, pod_name: str, namespace: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"POD_NAME": pod_name, "namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {pod_name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to pod {pod_name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot read pod {pod_name!r}: {exc}")


def x__translate_pod_error__mutmut_12(exc: Exception, pod_name: str, namespace: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"pod_name": pod_name, "XXnamespaceXX": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {pod_name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to pod {pod_name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot read pod {pod_name!r}: {exc}")


def x__translate_pod_error__mutmut_13(exc: Exception, pod_name: str, namespace: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"pod_name": pod_name, "NAMESPACE": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {pod_name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to pod {pod_name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot read pod {pod_name!r}: {exc}")


def x__translate_pod_error__mutmut_14(exc: Exception, pod_name: str, namespace: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"pod_name": pod_name, "namespace": namespace}
    if status != _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {pod_name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to pod {pod_name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot read pod {pod_name!r}: {exc}")


def x__translate_pod_error__mutmut_15(exc: Exception, pod_name: str, namespace: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"pod_name": pod_name, "namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            None, context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to pod {pod_name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot read pod {pod_name!r}: {exc}")


def x__translate_pod_error__mutmut_16(exc: Exception, pod_name: str, namespace: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"pod_name": pod_name, "namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {pod_name!r} not found in namespace {namespace!r}", context=None
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to pod {pod_name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot read pod {pod_name!r}: {exc}")


def x__translate_pod_error__mutmut_17(exc: Exception, pod_name: str, namespace: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"pod_name": pod_name, "namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to pod {pod_name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot read pod {pod_name!r}: {exc}")


def x__translate_pod_error__mutmut_18(exc: Exception, pod_name: str, namespace: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"pod_name": pod_name, "namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {pod_name!r} not found in namespace {namespace!r}", )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to pod {pod_name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot read pod {pod_name!r}: {exc}")


def x__translate_pod_error__mutmut_19(exc: Exception, pod_name: str, namespace: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"pod_name": pod_name, "namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {pod_name!r} not found in namespace {namespace!r}", context=context
        )
    if status != _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to pod {pod_name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot read pod {pod_name!r}: {exc}")


def x__translate_pod_error__mutmut_20(exc: Exception, pod_name: str, namespace: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"pod_name": pod_name, "namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {pod_name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            None, context=context
        )
    return ClusterUnreachableError(f"Cannot read pod {pod_name!r}: {exc}")


def x__translate_pod_error__mutmut_21(exc: Exception, pod_name: str, namespace: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"pod_name": pod_name, "namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {pod_name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to pod {pod_name!r} in namespace {namespace!r}", context=None
        )
    return ClusterUnreachableError(f"Cannot read pod {pod_name!r}: {exc}")


def x__translate_pod_error__mutmut_22(exc: Exception, pod_name: str, namespace: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"pod_name": pod_name, "namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {pod_name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            context=context
        )
    return ClusterUnreachableError(f"Cannot read pod {pod_name!r}: {exc}")


def x__translate_pod_error__mutmut_23(exc: Exception, pod_name: str, namespace: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"pod_name": pod_name, "namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {pod_name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to pod {pod_name!r} in namespace {namespace!r}", )
    return ClusterUnreachableError(f"Cannot read pod {pod_name!r}: {exc}")


def x__translate_pod_error__mutmut_24(exc: Exception, pod_name: str, namespace: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"pod_name": pod_name, "namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {pod_name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to pod {pod_name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(None)

mutants_x__translate_pod_error__mutmut['_mutmut_orig'] = x__translate_pod_error__mutmut_orig # type: ignore # mutmut generated
mutants_x__translate_pod_error__mutmut['x__translate_pod_error__mutmut_1'] = x__translate_pod_error__mutmut_1 # type: ignore # mutmut generated
mutants_x__translate_pod_error__mutmut['x__translate_pod_error__mutmut_2'] = x__translate_pod_error__mutmut_2 # type: ignore # mutmut generated
mutants_x__translate_pod_error__mutmut['x__translate_pod_error__mutmut_3'] = x__translate_pod_error__mutmut_3 # type: ignore # mutmut generated
mutants_x__translate_pod_error__mutmut['x__translate_pod_error__mutmut_4'] = x__translate_pod_error__mutmut_4 # type: ignore # mutmut generated
mutants_x__translate_pod_error__mutmut['x__translate_pod_error__mutmut_5'] = x__translate_pod_error__mutmut_5 # type: ignore # mutmut generated
mutants_x__translate_pod_error__mutmut['x__translate_pod_error__mutmut_6'] = x__translate_pod_error__mutmut_6 # type: ignore # mutmut generated
mutants_x__translate_pod_error__mutmut['x__translate_pod_error__mutmut_7'] = x__translate_pod_error__mutmut_7 # type: ignore # mutmut generated
mutants_x__translate_pod_error__mutmut['x__translate_pod_error__mutmut_8'] = x__translate_pod_error__mutmut_8 # type: ignore # mutmut generated
mutants_x__translate_pod_error__mutmut['x__translate_pod_error__mutmut_9'] = x__translate_pod_error__mutmut_9 # type: ignore # mutmut generated
mutants_x__translate_pod_error__mutmut['x__translate_pod_error__mutmut_10'] = x__translate_pod_error__mutmut_10 # type: ignore # mutmut generated
mutants_x__translate_pod_error__mutmut['x__translate_pod_error__mutmut_11'] = x__translate_pod_error__mutmut_11 # type: ignore # mutmut generated
mutants_x__translate_pod_error__mutmut['x__translate_pod_error__mutmut_12'] = x__translate_pod_error__mutmut_12 # type: ignore # mutmut generated
mutants_x__translate_pod_error__mutmut['x__translate_pod_error__mutmut_13'] = x__translate_pod_error__mutmut_13 # type: ignore # mutmut generated
mutants_x__translate_pod_error__mutmut['x__translate_pod_error__mutmut_14'] = x__translate_pod_error__mutmut_14 # type: ignore # mutmut generated
mutants_x__translate_pod_error__mutmut['x__translate_pod_error__mutmut_15'] = x__translate_pod_error__mutmut_15 # type: ignore # mutmut generated
mutants_x__translate_pod_error__mutmut['x__translate_pod_error__mutmut_16'] = x__translate_pod_error__mutmut_16 # type: ignore # mutmut generated
mutants_x__translate_pod_error__mutmut['x__translate_pod_error__mutmut_17'] = x__translate_pod_error__mutmut_17 # type: ignore # mutmut generated
mutants_x__translate_pod_error__mutmut['x__translate_pod_error__mutmut_18'] = x__translate_pod_error__mutmut_18 # type: ignore # mutmut generated
mutants_x__translate_pod_error__mutmut['x__translate_pod_error__mutmut_19'] = x__translate_pod_error__mutmut_19 # type: ignore # mutmut generated
mutants_x__translate_pod_error__mutmut['x__translate_pod_error__mutmut_20'] = x__translate_pod_error__mutmut_20 # type: ignore # mutmut generated
mutants_x__translate_pod_error__mutmut['x__translate_pod_error__mutmut_21'] = x__translate_pod_error__mutmut_21 # type: ignore # mutmut generated
mutants_x__translate_pod_error__mutmut['x__translate_pod_error__mutmut_22'] = x__translate_pod_error__mutmut_22 # type: ignore # mutmut generated
mutants_x__translate_pod_error__mutmut['x__translate_pod_error__mutmut_23'] = x__translate_pod_error__mutmut_23 # type: ignore # mutmut generated
mutants_x__translate_pod_error__mutmut['x__translate_pod_error__mutmut_24'] = x__translate_pod_error__mutmut_24 # type: ignore # mutmut generated
