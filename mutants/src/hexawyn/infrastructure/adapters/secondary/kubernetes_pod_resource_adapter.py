"""KubernetesPodResourceAdapter — combines pod spec limits with Metrics API usage."""

from __future__ import annotations

from hexawyn.application.ports.driven.pod_resource_metrics_port import (
    ContainerMetricsRecord,
    PodResourceMetricsPort,
)
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    InsufficientPermissionsError,
    MetricsUnavailableError,
)

_METRICS_GROUP = "metrics.k8s.io"
_METRICS_VERSION = "v1beta1"
_METRICS_PLURAL = "pods"
_K8S_FORBIDDEN = 403
_K8S_NOT_FOUND = 404


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut: MutantDict = {}  # type: ignore


class KubernetesPodResourceAdapter(PodResourceMetricsPort):
    """Secondary adapter — reads pod resource limits and live usage from K8s."""

    @_mutmut_mutated(mutants_xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut)
    def list_container_resources(self, namespace: str) -> list[ContainerMetricsRecord]:
        limits_by_pod = self._fetch_pod_limits(namespace)
        usage_by_pod = self._fetch_metrics(namespace)
        return _merge(limits_by_pod, usage_by_pod, namespace)

    def xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut_orig(self, namespace: str) -> list[ContainerMetricsRecord]:
        limits_by_pod = self._fetch_pod_limits(namespace)
        usage_by_pod = self._fetch_metrics(namespace)
        return _merge(limits_by_pod, usage_by_pod, namespace)

    def xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut_1(self, namespace: str) -> list[ContainerMetricsRecord]:
        limits_by_pod = None
        usage_by_pod = self._fetch_metrics(namespace)
        return _merge(limits_by_pod, usage_by_pod, namespace)

    def xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut_2(self, namespace: str) -> list[ContainerMetricsRecord]:
        limits_by_pod = self._fetch_pod_limits(None)
        usage_by_pod = self._fetch_metrics(namespace)
        return _merge(limits_by_pod, usage_by_pod, namespace)

    def xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut_3(self, namespace: str) -> list[ContainerMetricsRecord]:
        limits_by_pod = self._fetch_pod_limits(namespace)
        usage_by_pod = None
        return _merge(limits_by_pod, usage_by_pod, namespace)

    def xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut_4(self, namespace: str) -> list[ContainerMetricsRecord]:
        limits_by_pod = self._fetch_pod_limits(namespace)
        usage_by_pod = self._fetch_metrics(None)
        return _merge(limits_by_pod, usage_by_pod, namespace)

    def xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut_5(self, namespace: str) -> list[ContainerMetricsRecord]:
        limits_by_pod = self._fetch_pod_limits(namespace)
        usage_by_pod = self._fetch_metrics(namespace)
        return _merge(None, usage_by_pod, namespace)

    def xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut_6(self, namespace: str) -> list[ContainerMetricsRecord]:
        limits_by_pod = self._fetch_pod_limits(namespace)
        usage_by_pod = self._fetch_metrics(namespace)
        return _merge(limits_by_pod, None, namespace)

    def xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut_7(self, namespace: str) -> list[ContainerMetricsRecord]:
        limits_by_pod = self._fetch_pod_limits(namespace)
        usage_by_pod = self._fetch_metrics(namespace)
        return _merge(limits_by_pod, usage_by_pod, None)

    def xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut_8(self, namespace: str) -> list[ContainerMetricsRecord]:
        limits_by_pod = self._fetch_pod_limits(namespace)
        usage_by_pod = self._fetch_metrics(namespace)
        return _merge(usage_by_pod, namespace)

    def xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut_9(self, namespace: str) -> list[ContainerMetricsRecord]:
        limits_by_pod = self._fetch_pod_limits(namespace)
        usage_by_pod = self._fetch_metrics(namespace)
        return _merge(limits_by_pod, namespace)

    def xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut_10(self, namespace: str) -> list[ContainerMetricsRecord]:
        limits_by_pod = self._fetch_pod_limits(namespace)
        usage_by_pod = self._fetch_metrics(namespace)
        return _merge(limits_by_pod, usage_by_pod, )

    @_mutmut_mutated(mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut)
    def _fetch_pod_limits(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_orig(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_1(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = None
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_2(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = None
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_3(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=None)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_4(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = None
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_5(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(None, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_6(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, None, None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_7(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr("status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_8(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_9(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", )
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_10(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "XXstatusXX", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_11(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "STATUS", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_12(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status != _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_13(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    None,
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_14(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context=None,
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_15(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_16(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_17(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"XXnamespaceXX": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_18(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"NAMESPACE": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_19(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                None
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_20(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = None
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_21(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = None
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_22(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = None
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_23(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers and []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_24(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = None
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_25(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits and {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_26(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    None
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_27(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(None),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_28(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get(None)),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_29(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("XXcpuXX")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_30(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("CPU")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_31(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(None),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_32(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get(None)),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_33(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("XXmemoryXX")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_34(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("MEMORY")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_35(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_36(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers and []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_37(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = None
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_38(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits and {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_39(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    None
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_40(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(None),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_41(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get(None)),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_42(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("XXcpuXX")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_43(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("CPU")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_44(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(None),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_45(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get(None)),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_46(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("XXmemoryXX")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_47(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("MEMORY")),
                        False,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_48(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            result[pod_name] = containers
        return result

    def xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_49(
        self, namespace: str
    ) -> dict[str, list[tuple[str, int | None, int | None, bool]]]:
        from kubernetes import client as k8s

        try:
            core_api = k8s.CoreV1Api()
            pod_list = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pods in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list pods in namespace {namespace!r}: {exc}"
            ) from exc

        result: dict[str, list[tuple[str, int | None, int | None, bool]]] = {}
        for pod in pod_list.items:
            pod_name: str = pod.metadata.name
            containers: list[tuple[str, int | None, int | None, bool]] = []
            for c in pod.spec.init_containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        True,
                    )
                )
            for c in pod.spec.containers or []:
                limits = c.resources.limits or {} if c.resources else {}
                containers.append(
                    (
                        c.name,
                        _parse_cpu(limits.get("cpu")),
                        _parse_memory(limits.get("memory")),
                        False,
                    )
                )
            result[pod_name] = None
        return result

    @_mutmut_mutated(mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut)
    def _fetch_metrics(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_orig(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_1(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = None
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_2(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = None
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_3(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=None,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_4(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=None,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_5(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=None,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_6(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=None,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_7(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_8(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_9(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_10(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_11(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = None
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_12(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(None, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_13(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, None, None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_14(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr("status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_15(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_16(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", )
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_17(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "XXstatusXX", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_18(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "STATUS", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_19(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status != _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_20(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    None,
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_21(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context=None,
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_22(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_23(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_24(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"XXnamespaceXX": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_25(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"NAMESPACE": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_26(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status != _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_27(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    None
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_28(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "XXKubernetes Metrics API not available — install metrics-serverXX"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_29(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "kubernetes metrics api not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_30(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "KUBERNETES METRICS API NOT AVAILABLE — INSTALL METRICS-SERVER"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_31(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                None
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_32(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = None
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_33(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = None
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_34(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") and [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_35(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get(None) or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_36(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("XXitemsXX") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_37(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("ITEMS") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_38(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = None
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_39(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get(None, "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_40(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", None)
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_41(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_42(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", )
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_43(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get(None, {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_44(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", None).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_45(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get({}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_46(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", ).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_47(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("XXmetadataXX", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_48(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("METADATA", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_49(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("XXnameXX", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_50(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("NAME", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_51(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "XXXX")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_52(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = None
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_53(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") and []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_54(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get(None) or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_55(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("XXcontainersXX") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_56(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("CONTAINERS") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_57(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = None
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_58(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get(None, {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_59(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", None)
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_60(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get({})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_61(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", )
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_62(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("XXusageXX", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_63(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("USAGE", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_64(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = None
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_65(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) and 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_66(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(None) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_67(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get(None)) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_68(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("XXcpuXX")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_69(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("CPU")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_70(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 1
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_71(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = None
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_72(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) and 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_73(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(None) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_74(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get(None)) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_75(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("XXmemoryXX")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_76(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("MEMORY")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_77(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 1
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_78(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = None
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_79(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["XXnameXX"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_80(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["NAME"]] = (cpu_m, mem_b)
            usage[pod_name] = containers_usage
        return usage

    def xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_81(self, namespace: str) -> dict[str, dict[str, tuple[int, int]]]:
        from kubernetes import client as k8s

        try:
            custom_api = k8s.CustomObjectsApi()
            raw = custom_api.list_namespaced_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                namespace=namespace,
                plural=_METRICS_PLURAL,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to pod metrics in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise MetricsUnavailableError(
                    "Kubernetes Metrics API not available — install metrics-server"
                ) from exc
            raise ClusterUnreachableError(
                f"Metrics API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        usage: dict[str, dict[str, tuple[int, int]]] = {}
        items = raw.get("items") or [] if isinstance(raw, dict) else []
        for item in items:
            pod_name = item.get("metadata", {}).get("name", "")
            containers_usage: dict[str, tuple[int, int]] = {}
            for c in item.get("containers") or []:
                u = c.get("usage", {})
                cpu_m = _parse_cpu(u.get("cpu")) or 0
                mem_b = _parse_memory(u.get("memory")) or 0
                containers_usage[c["name"]] = (cpu_m, mem_b)
            usage[pod_name] = None
        return usage

mutants_xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut['_mutmut_orig'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut['xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut_1'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut['xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut_2'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut['xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut_3'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut['xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut_4'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut['xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut_5'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut['xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut_6'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut['xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut_7'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut['xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut_8'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut['xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut_9'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut['xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut_10'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁlist_container_resources__mutmut_10 # type: ignore # mutmut generated

mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['_mutmut_orig'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_1'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_2'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_3'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_4'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_5'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_6'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_7'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_8'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_9'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_10'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_11'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_12'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_13'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_14'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_14 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_15'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_15 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_16'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_16 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_17'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_17 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_18'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_18 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_19'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_19 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_20'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_20 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_21'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_21 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_22'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_22 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_23'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_23 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_24'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_24 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_25'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_25 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_26'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_26 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_27'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_27 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_28'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_28 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_29'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_29 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_30'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_30 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_31'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_31 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_32'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_32 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_33'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_33 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_34'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_34 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_35'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_35 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_36'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_36 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_37'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_37 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_38'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_38 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_39'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_39 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_40'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_40 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_41'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_41 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_42'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_42 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_43'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_43 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_44'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_44 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_45'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_45 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_46'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_46 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_47'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_47 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_48'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_48 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_49'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_pod_limits__mutmut_49 # type: ignore # mutmut generated

mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['_mutmut_orig'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_1'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_2'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_3'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_4'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_5'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_6'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_7'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_8'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_9'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_10'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_11'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_12'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_13'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_14'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_14 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_15'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_15 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_16'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_16 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_17'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_17 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_18'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_18 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_19'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_19 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_20'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_20 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_21'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_21 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_22'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_22 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_23'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_23 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_24'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_24 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_25'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_25 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_26'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_26 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_27'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_27 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_28'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_28 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_29'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_29 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_30'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_30 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_31'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_31 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_32'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_32 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_33'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_33 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_34'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_34 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_35'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_35 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_36'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_36 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_37'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_37 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_38'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_38 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_39'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_39 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_40'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_40 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_41'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_41 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_42'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_42 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_43'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_43 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_44'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_44 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_45'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_45 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_46'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_46 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_47'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_47 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_48'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_48 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_49'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_49 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_50'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_50 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_51'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_51 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_52'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_52 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_53'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_53 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_54'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_54 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_55'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_55 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_56'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_56 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_57'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_57 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_58'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_58 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_59'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_59 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_60'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_60 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_61'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_61 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_62'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_62 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_63'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_63 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_64'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_64 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_65'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_65 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_66'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_66 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_67'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_67 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_68'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_68 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_69'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_69 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_70'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_70 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_71'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_71 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_72'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_72 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_73'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_73 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_74'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_74 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_75'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_75 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_76'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_76 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_77'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_77 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_78'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_78 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_79'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_79 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_80'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_80 # type: ignore # mutmut generated
mutants_xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut['xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_81'] = KubernetesPodResourceAdapter.xǁKubernetesPodResourceAdapterǁ_fetch_metrics__mutmut_81 # type: ignore # mutmut generated
mutants_x__parse_cpu__mutmut: MutantDict = {}  # type: ignore


# ── Helpers ────────────────────────────────────────────────────────────────


@_mutmut_mutated(mutants_x__parse_cpu__mutmut)
def _parse_cpu(value: str | None) -> int | None:
    """Parse K8s CPU string to millicores. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    if value.endswith("m"):
        return int(value[:-1])
    try:
        return int(float(value) * 1000)
    except ValueError:
        return None


# ── Helpers ────────────────────────────────────────────────────────────────


def x__parse_cpu__mutmut_orig(value: str | None) -> int | None:
    """Parse K8s CPU string to millicores. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    if value.endswith("m"):
        return int(value[:-1])
    try:
        return int(float(value) * 1000)
    except ValueError:
        return None


# ── Helpers ────────────────────────────────────────────────────────────────


def x__parse_cpu__mutmut_1(value: str | None) -> int | None:
    """Parse K8s CPU string to millicores. Returns None if not set."""
    if value:
        return None
    value = value.strip()
    if value.endswith("m"):
        return int(value[:-1])
    try:
        return int(float(value) * 1000)
    except ValueError:
        return None


# ── Helpers ────────────────────────────────────────────────────────────────


def x__parse_cpu__mutmut_2(value: str | None) -> int | None:
    """Parse K8s CPU string to millicores. Returns None if not set."""
    if not value:
        return None
    value = None
    if value.endswith("m"):
        return int(value[:-1])
    try:
        return int(float(value) * 1000)
    except ValueError:
        return None


# ── Helpers ────────────────────────────────────────────────────────────────


def x__parse_cpu__mutmut_3(value: str | None) -> int | None:
    """Parse K8s CPU string to millicores. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    if value.endswith(None):
        return int(value[:-1])
    try:
        return int(float(value) * 1000)
    except ValueError:
        return None


# ── Helpers ────────────────────────────────────────────────────────────────


def x__parse_cpu__mutmut_4(value: str | None) -> int | None:
    """Parse K8s CPU string to millicores. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    if value.endswith("XXmXX"):
        return int(value[:-1])
    try:
        return int(float(value) * 1000)
    except ValueError:
        return None


# ── Helpers ────────────────────────────────────────────────────────────────


def x__parse_cpu__mutmut_5(value: str | None) -> int | None:
    """Parse K8s CPU string to millicores. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    if value.endswith("M"):
        return int(value[:-1])
    try:
        return int(float(value) * 1000)
    except ValueError:
        return None


# ── Helpers ────────────────────────────────────────────────────────────────


def x__parse_cpu__mutmut_6(value: str | None) -> int | None:
    """Parse K8s CPU string to millicores. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    if value.endswith("m"):
        return int(None)
    try:
        return int(float(value) * 1000)
    except ValueError:
        return None


# ── Helpers ────────────────────────────────────────────────────────────────


def x__parse_cpu__mutmut_7(value: str | None) -> int | None:
    """Parse K8s CPU string to millicores. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    if value.endswith("m"):
        return int(value[:+1])
    try:
        return int(float(value) * 1000)
    except ValueError:
        return None


# ── Helpers ────────────────────────────────────────────────────────────────


def x__parse_cpu__mutmut_8(value: str | None) -> int | None:
    """Parse K8s CPU string to millicores. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    if value.endswith("m"):
        return int(value[:-2])
    try:
        return int(float(value) * 1000)
    except ValueError:
        return None


# ── Helpers ────────────────────────────────────────────────────────────────


def x__parse_cpu__mutmut_9(value: str | None) -> int | None:
    """Parse K8s CPU string to millicores. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    if value.endswith("m"):
        return int(value[:-1])
    try:
        return int(None)
    except ValueError:
        return None


# ── Helpers ────────────────────────────────────────────────────────────────


def x__parse_cpu__mutmut_10(value: str | None) -> int | None:
    """Parse K8s CPU string to millicores. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    if value.endswith("m"):
        return int(value[:-1])
    try:
        return int(float(value) / 1000)
    except ValueError:
        return None


# ── Helpers ────────────────────────────────────────────────────────────────


def x__parse_cpu__mutmut_11(value: str | None) -> int | None:
    """Parse K8s CPU string to millicores. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    if value.endswith("m"):
        return int(value[:-1])
    try:
        return int(float(None) * 1000)
    except ValueError:
        return None


# ── Helpers ────────────────────────────────────────────────────────────────


def x__parse_cpu__mutmut_12(value: str | None) -> int | None:
    """Parse K8s CPU string to millicores. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    if value.endswith("m"):
        return int(value[:-1])
    try:
        return int(float(value) * 1001)
    except ValueError:
        return None

mutants_x__parse_cpu__mutmut['_mutmut_orig'] = x__parse_cpu__mutmut_orig # type: ignore # mutmut generated
mutants_x__parse_cpu__mutmut['x__parse_cpu__mutmut_1'] = x__parse_cpu__mutmut_1 # type: ignore # mutmut generated
mutants_x__parse_cpu__mutmut['x__parse_cpu__mutmut_2'] = x__parse_cpu__mutmut_2 # type: ignore # mutmut generated
mutants_x__parse_cpu__mutmut['x__parse_cpu__mutmut_3'] = x__parse_cpu__mutmut_3 # type: ignore # mutmut generated
mutants_x__parse_cpu__mutmut['x__parse_cpu__mutmut_4'] = x__parse_cpu__mutmut_4 # type: ignore # mutmut generated
mutants_x__parse_cpu__mutmut['x__parse_cpu__mutmut_5'] = x__parse_cpu__mutmut_5 # type: ignore # mutmut generated
mutants_x__parse_cpu__mutmut['x__parse_cpu__mutmut_6'] = x__parse_cpu__mutmut_6 # type: ignore # mutmut generated
mutants_x__parse_cpu__mutmut['x__parse_cpu__mutmut_7'] = x__parse_cpu__mutmut_7 # type: ignore # mutmut generated
mutants_x__parse_cpu__mutmut['x__parse_cpu__mutmut_8'] = x__parse_cpu__mutmut_8 # type: ignore # mutmut generated
mutants_x__parse_cpu__mutmut['x__parse_cpu__mutmut_9'] = x__parse_cpu__mutmut_9 # type: ignore # mutmut generated
mutants_x__parse_cpu__mutmut['x__parse_cpu__mutmut_10'] = x__parse_cpu__mutmut_10 # type: ignore # mutmut generated
mutants_x__parse_cpu__mutmut['x__parse_cpu__mutmut_11'] = x__parse_cpu__mutmut_11 # type: ignore # mutmut generated
mutants_x__parse_cpu__mutmut['x__parse_cpu__mutmut_12'] = x__parse_cpu__mutmut_12 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__parse_memory__mutmut)
def _parse_memory(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1024**2,
        "Gi": 1024**3,
        "Ti": 1024**4,
        "K": 1000,
        "M": 1000**2,
        "G": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_orig(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1024**2,
        "Gi": 1024**3,
        "Ti": 1024**4,
        "K": 1000,
        "M": 1000**2,
        "G": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_1(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1024**2,
        "Gi": 1024**3,
        "Ti": 1024**4,
        "K": 1000,
        "M": 1000**2,
        "G": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_2(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = None
    _units = {
        "Ki": 1024,
        "Mi": 1024**2,
        "Gi": 1024**3,
        "Ti": 1024**4,
        "K": 1000,
        "M": 1000**2,
        "G": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_3(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = None
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_4(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "XXKiXX": 1024,
        "Mi": 1024**2,
        "Gi": 1024**3,
        "Ti": 1024**4,
        "K": 1000,
        "M": 1000**2,
        "G": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_5(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "ki": 1024,
        "Mi": 1024**2,
        "Gi": 1024**3,
        "Ti": 1024**4,
        "K": 1000,
        "M": 1000**2,
        "G": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_6(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "KI": 1024,
        "Mi": 1024**2,
        "Gi": 1024**3,
        "Ti": 1024**4,
        "K": 1000,
        "M": 1000**2,
        "G": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_7(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1025,
        "Mi": 1024**2,
        "Gi": 1024**3,
        "Ti": 1024**4,
        "K": 1000,
        "M": 1000**2,
        "G": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_8(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "XXMiXX": 1024**2,
        "Gi": 1024**3,
        "Ti": 1024**4,
        "K": 1000,
        "M": 1000**2,
        "G": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_9(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "mi": 1024**2,
        "Gi": 1024**3,
        "Ti": 1024**4,
        "K": 1000,
        "M": 1000**2,
        "G": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_10(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "MI": 1024**2,
        "Gi": 1024**3,
        "Ti": 1024**4,
        "K": 1000,
        "M": 1000**2,
        "G": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_11(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1024 * 2,
        "Gi": 1024**3,
        "Ti": 1024**4,
        "K": 1000,
        "M": 1000**2,
        "G": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_12(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1025**2,
        "Gi": 1024**3,
        "Ti": 1024**4,
        "K": 1000,
        "M": 1000**2,
        "G": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_13(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1024**3,
        "Gi": 1024**3,
        "Ti": 1024**4,
        "K": 1000,
        "M": 1000**2,
        "G": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_14(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1024**2,
        "XXGiXX": 1024**3,
        "Ti": 1024**4,
        "K": 1000,
        "M": 1000**2,
        "G": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_15(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1024**2,
        "gi": 1024**3,
        "Ti": 1024**4,
        "K": 1000,
        "M": 1000**2,
        "G": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_16(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1024**2,
        "GI": 1024**3,
        "Ti": 1024**4,
        "K": 1000,
        "M": 1000**2,
        "G": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_17(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1024**2,
        "Gi": 1024 * 3,
        "Ti": 1024**4,
        "K": 1000,
        "M": 1000**2,
        "G": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_18(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1024**2,
        "Gi": 1025**3,
        "Ti": 1024**4,
        "K": 1000,
        "M": 1000**2,
        "G": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_19(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1024**2,
        "Gi": 1024**4,
        "Ti": 1024**4,
        "K": 1000,
        "M": 1000**2,
        "G": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_20(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1024**2,
        "Gi": 1024**3,
        "XXTiXX": 1024**4,
        "K": 1000,
        "M": 1000**2,
        "G": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_21(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1024**2,
        "Gi": 1024**3,
        "ti": 1024**4,
        "K": 1000,
        "M": 1000**2,
        "G": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_22(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1024**2,
        "Gi": 1024**3,
        "TI": 1024**4,
        "K": 1000,
        "M": 1000**2,
        "G": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_23(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1024**2,
        "Gi": 1024**3,
        "Ti": 1024 * 4,
        "K": 1000,
        "M": 1000**2,
        "G": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_24(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1024**2,
        "Gi": 1024**3,
        "Ti": 1025**4,
        "K": 1000,
        "M": 1000**2,
        "G": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_25(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1024**2,
        "Gi": 1024**3,
        "Ti": 1024**5,
        "K": 1000,
        "M": 1000**2,
        "G": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_26(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1024**2,
        "Gi": 1024**3,
        "Ti": 1024**4,
        "XXKXX": 1000,
        "M": 1000**2,
        "G": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_27(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1024**2,
        "Gi": 1024**3,
        "Ti": 1024**4,
        "k": 1000,
        "M": 1000**2,
        "G": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_28(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1024**2,
        "Gi": 1024**3,
        "Ti": 1024**4,
        "K": 1001,
        "M": 1000**2,
        "G": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_29(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1024**2,
        "Gi": 1024**3,
        "Ti": 1024**4,
        "K": 1000,
        "XXMXX": 1000**2,
        "G": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_30(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1024**2,
        "Gi": 1024**3,
        "Ti": 1024**4,
        "K": 1000,
        "m": 1000**2,
        "G": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_31(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1024**2,
        "Gi": 1024**3,
        "Ti": 1024**4,
        "K": 1000,
        "M": 1000 * 2,
        "G": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_32(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1024**2,
        "Gi": 1024**3,
        "Ti": 1024**4,
        "K": 1000,
        "M": 1001**2,
        "G": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_33(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1024**2,
        "Gi": 1024**3,
        "Ti": 1024**4,
        "K": 1000,
        "M": 1000**3,
        "G": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_34(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1024**2,
        "Gi": 1024**3,
        "Ti": 1024**4,
        "K": 1000,
        "M": 1000**2,
        "XXGXX": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_35(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1024**2,
        "Gi": 1024**3,
        "Ti": 1024**4,
        "K": 1000,
        "M": 1000**2,
        "g": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_36(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1024**2,
        "Gi": 1024**3,
        "Ti": 1024**4,
        "K": 1000,
        "M": 1000**2,
        "G": 1000 * 3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_37(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1024**2,
        "Gi": 1024**3,
        "Ti": 1024**4,
        "K": 1000,
        "M": 1000**2,
        "G": 1001**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_38(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1024**2,
        "Gi": 1024**3,
        "Ti": 1024**4,
        "K": 1000,
        "M": 1000**2,
        "G": 1000**4,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_39(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1024**2,
        "Gi": 1024**3,
        "Ti": 1024**4,
        "K": 1000,
        "M": 1000**2,
        "G": 1000**3,
        "XXTXX": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_40(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1024**2,
        "Gi": 1024**3,
        "Ti": 1024**4,
        "K": 1000,
        "M": 1000**2,
        "G": 1000**3,
        "t": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_41(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1024**2,
        "Gi": 1024**3,
        "Ti": 1024**4,
        "K": 1000,
        "M": 1000**2,
        "G": 1000**3,
        "T": 1000 * 4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_42(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1024**2,
        "Gi": 1024**3,
        "Ti": 1024**4,
        "K": 1000,
        "M": 1000**2,
        "G": 1000**3,
        "T": 1001**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_43(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1024**2,
        "Gi": 1024**3,
        "Ti": 1024**4,
        "K": 1000,
        "M": 1000**2,
        "G": 1000**3,
        "T": 1000**5,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_44(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1024**2,
        "Gi": 1024**3,
        "Ti": 1024**4,
        "K": 1000,
        "M": 1000**2,
        "G": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(None):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_45(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1024**2,
        "Gi": 1024**3,
        "Ti": 1024**4,
        "K": 1000,
        "M": 1000**2,
        "G": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(None)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_46(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1024**2,
        "Gi": 1024**3,
        "Ti": 1024**4,
        "K": 1000,
        "M": 1000**2,
        "G": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) / multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_47(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1024**2,
        "Gi": 1024**3,
        "Ti": 1024**4,
        "K": 1000,
        "M": 1000**2,
        "G": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(None) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_48(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1024**2,
        "Gi": 1024**3,
        "Ti": 1024**4,
        "K": 1000,
        "M": 1000**2,
        "G": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: +len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(value)
    except ValueError:
        return None


def x__parse_memory__mutmut_49(value: str | None) -> int | None:
    """Parse K8s memory string to bytes. Returns None if not set."""
    if not value:
        return None
    value = value.strip()
    _units = {
        "Ki": 1024,
        "Mi": 1024**2,
        "Gi": 1024**3,
        "Ti": 1024**4,
        "K": 1000,
        "M": 1000**2,
        "G": 1000**3,
        "T": 1000**4,
    }
    for suffix, multiplier in _units.items():
        if value.endswith(suffix):
            try:
                return int(float(value[: -len(suffix)]) * multiplier)
            except ValueError:
                return None
    try:
        return int(None)
    except ValueError:
        return None

mutants_x__parse_memory__mutmut['_mutmut_orig'] = x__parse_memory__mutmut_orig # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_1'] = x__parse_memory__mutmut_1 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_2'] = x__parse_memory__mutmut_2 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_3'] = x__parse_memory__mutmut_3 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_4'] = x__parse_memory__mutmut_4 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_5'] = x__parse_memory__mutmut_5 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_6'] = x__parse_memory__mutmut_6 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_7'] = x__parse_memory__mutmut_7 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_8'] = x__parse_memory__mutmut_8 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_9'] = x__parse_memory__mutmut_9 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_10'] = x__parse_memory__mutmut_10 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_11'] = x__parse_memory__mutmut_11 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_12'] = x__parse_memory__mutmut_12 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_13'] = x__parse_memory__mutmut_13 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_14'] = x__parse_memory__mutmut_14 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_15'] = x__parse_memory__mutmut_15 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_16'] = x__parse_memory__mutmut_16 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_17'] = x__parse_memory__mutmut_17 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_18'] = x__parse_memory__mutmut_18 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_19'] = x__parse_memory__mutmut_19 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_20'] = x__parse_memory__mutmut_20 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_21'] = x__parse_memory__mutmut_21 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_22'] = x__parse_memory__mutmut_22 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_23'] = x__parse_memory__mutmut_23 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_24'] = x__parse_memory__mutmut_24 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_25'] = x__parse_memory__mutmut_25 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_26'] = x__parse_memory__mutmut_26 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_27'] = x__parse_memory__mutmut_27 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_28'] = x__parse_memory__mutmut_28 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_29'] = x__parse_memory__mutmut_29 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_30'] = x__parse_memory__mutmut_30 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_31'] = x__parse_memory__mutmut_31 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_32'] = x__parse_memory__mutmut_32 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_33'] = x__parse_memory__mutmut_33 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_34'] = x__parse_memory__mutmut_34 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_35'] = x__parse_memory__mutmut_35 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_36'] = x__parse_memory__mutmut_36 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_37'] = x__parse_memory__mutmut_37 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_38'] = x__parse_memory__mutmut_38 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_39'] = x__parse_memory__mutmut_39 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_40'] = x__parse_memory__mutmut_40 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_41'] = x__parse_memory__mutmut_41 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_42'] = x__parse_memory__mutmut_42 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_43'] = x__parse_memory__mutmut_43 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_44'] = x__parse_memory__mutmut_44 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_45'] = x__parse_memory__mutmut_45 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_46'] = x__parse_memory__mutmut_46 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_47'] = x__parse_memory__mutmut_47 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_48'] = x__parse_memory__mutmut_48 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_49'] = x__parse_memory__mutmut_49 # type: ignore # mutmut generated
mutants_x__merge__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__merge__mutmut)
def _merge(
    limits_by_pod: dict[str, list[tuple[str, int | None, int | None, bool]]],
    usage_by_pod: dict[str, dict[str, tuple[int, int]]],
    namespace: str,
) -> list[ContainerMetricsRecord]:
    records: list[ContainerMetricsRecord] = []
    for pod_name, containers in limits_by_pod.items():
        pod_usage = usage_by_pod.get(pod_name, {})
        for container_name, cpu_limit, mem_limit, is_init in containers:
            cpu_used, mem_used = pod_usage.get(container_name, (0, 0))
            records.append(
                ContainerMetricsRecord(
                    container_name=container_name,
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_usage_millicores=cpu_used,
                    cpu_limit_millicores=cpu_limit,
                    memory_usage_bytes=mem_used,
                    memory_limit_bytes=mem_limit,
                    is_init_container=is_init,
                )
            )
    return records


def x__merge__mutmut_orig(
    limits_by_pod: dict[str, list[tuple[str, int | None, int | None, bool]]],
    usage_by_pod: dict[str, dict[str, tuple[int, int]]],
    namespace: str,
) -> list[ContainerMetricsRecord]:
    records: list[ContainerMetricsRecord] = []
    for pod_name, containers in limits_by_pod.items():
        pod_usage = usage_by_pod.get(pod_name, {})
        for container_name, cpu_limit, mem_limit, is_init in containers:
            cpu_used, mem_used = pod_usage.get(container_name, (0, 0))
            records.append(
                ContainerMetricsRecord(
                    container_name=container_name,
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_usage_millicores=cpu_used,
                    cpu_limit_millicores=cpu_limit,
                    memory_usage_bytes=mem_used,
                    memory_limit_bytes=mem_limit,
                    is_init_container=is_init,
                )
            )
    return records


def x__merge__mutmut_1(
    limits_by_pod: dict[str, list[tuple[str, int | None, int | None, bool]]],
    usage_by_pod: dict[str, dict[str, tuple[int, int]]],
    namespace: str,
) -> list[ContainerMetricsRecord]:
    records: list[ContainerMetricsRecord] = None
    for pod_name, containers in limits_by_pod.items():
        pod_usage = usage_by_pod.get(pod_name, {})
        for container_name, cpu_limit, mem_limit, is_init in containers:
            cpu_used, mem_used = pod_usage.get(container_name, (0, 0))
            records.append(
                ContainerMetricsRecord(
                    container_name=container_name,
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_usage_millicores=cpu_used,
                    cpu_limit_millicores=cpu_limit,
                    memory_usage_bytes=mem_used,
                    memory_limit_bytes=mem_limit,
                    is_init_container=is_init,
                )
            )
    return records


def x__merge__mutmut_2(
    limits_by_pod: dict[str, list[tuple[str, int | None, int | None, bool]]],
    usage_by_pod: dict[str, dict[str, tuple[int, int]]],
    namespace: str,
) -> list[ContainerMetricsRecord]:
    records: list[ContainerMetricsRecord] = []
    for pod_name, containers in limits_by_pod.items():
        pod_usage = None
        for container_name, cpu_limit, mem_limit, is_init in containers:
            cpu_used, mem_used = pod_usage.get(container_name, (0, 0))
            records.append(
                ContainerMetricsRecord(
                    container_name=container_name,
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_usage_millicores=cpu_used,
                    cpu_limit_millicores=cpu_limit,
                    memory_usage_bytes=mem_used,
                    memory_limit_bytes=mem_limit,
                    is_init_container=is_init,
                )
            )
    return records


def x__merge__mutmut_3(
    limits_by_pod: dict[str, list[tuple[str, int | None, int | None, bool]]],
    usage_by_pod: dict[str, dict[str, tuple[int, int]]],
    namespace: str,
) -> list[ContainerMetricsRecord]:
    records: list[ContainerMetricsRecord] = []
    for pod_name, containers in limits_by_pod.items():
        pod_usage = usage_by_pod.get(None, {})
        for container_name, cpu_limit, mem_limit, is_init in containers:
            cpu_used, mem_used = pod_usage.get(container_name, (0, 0))
            records.append(
                ContainerMetricsRecord(
                    container_name=container_name,
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_usage_millicores=cpu_used,
                    cpu_limit_millicores=cpu_limit,
                    memory_usage_bytes=mem_used,
                    memory_limit_bytes=mem_limit,
                    is_init_container=is_init,
                )
            )
    return records


def x__merge__mutmut_4(
    limits_by_pod: dict[str, list[tuple[str, int | None, int | None, bool]]],
    usage_by_pod: dict[str, dict[str, tuple[int, int]]],
    namespace: str,
) -> list[ContainerMetricsRecord]:
    records: list[ContainerMetricsRecord] = []
    for pod_name, containers in limits_by_pod.items():
        pod_usage = usage_by_pod.get(pod_name, None)
        for container_name, cpu_limit, mem_limit, is_init in containers:
            cpu_used, mem_used = pod_usage.get(container_name, (0, 0))
            records.append(
                ContainerMetricsRecord(
                    container_name=container_name,
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_usage_millicores=cpu_used,
                    cpu_limit_millicores=cpu_limit,
                    memory_usage_bytes=mem_used,
                    memory_limit_bytes=mem_limit,
                    is_init_container=is_init,
                )
            )
    return records


def x__merge__mutmut_5(
    limits_by_pod: dict[str, list[tuple[str, int | None, int | None, bool]]],
    usage_by_pod: dict[str, dict[str, tuple[int, int]]],
    namespace: str,
) -> list[ContainerMetricsRecord]:
    records: list[ContainerMetricsRecord] = []
    for pod_name, containers in limits_by_pod.items():
        pod_usage = usage_by_pod.get({})
        for container_name, cpu_limit, mem_limit, is_init in containers:
            cpu_used, mem_used = pod_usage.get(container_name, (0, 0))
            records.append(
                ContainerMetricsRecord(
                    container_name=container_name,
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_usage_millicores=cpu_used,
                    cpu_limit_millicores=cpu_limit,
                    memory_usage_bytes=mem_used,
                    memory_limit_bytes=mem_limit,
                    is_init_container=is_init,
                )
            )
    return records


def x__merge__mutmut_6(
    limits_by_pod: dict[str, list[tuple[str, int | None, int | None, bool]]],
    usage_by_pod: dict[str, dict[str, tuple[int, int]]],
    namespace: str,
) -> list[ContainerMetricsRecord]:
    records: list[ContainerMetricsRecord] = []
    for pod_name, containers in limits_by_pod.items():
        pod_usage = usage_by_pod.get(pod_name, )
        for container_name, cpu_limit, mem_limit, is_init in containers:
            cpu_used, mem_used = pod_usage.get(container_name, (0, 0))
            records.append(
                ContainerMetricsRecord(
                    container_name=container_name,
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_usage_millicores=cpu_used,
                    cpu_limit_millicores=cpu_limit,
                    memory_usage_bytes=mem_used,
                    memory_limit_bytes=mem_limit,
                    is_init_container=is_init,
                )
            )
    return records


def x__merge__mutmut_7(
    limits_by_pod: dict[str, list[tuple[str, int | None, int | None, bool]]],
    usage_by_pod: dict[str, dict[str, tuple[int, int]]],
    namespace: str,
) -> list[ContainerMetricsRecord]:
    records: list[ContainerMetricsRecord] = []
    for pod_name, containers in limits_by_pod.items():
        pod_usage = usage_by_pod.get(pod_name, {})
        for container_name, cpu_limit, mem_limit, is_init in containers:
            cpu_used, mem_used = None
            records.append(
                ContainerMetricsRecord(
                    container_name=container_name,
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_usage_millicores=cpu_used,
                    cpu_limit_millicores=cpu_limit,
                    memory_usage_bytes=mem_used,
                    memory_limit_bytes=mem_limit,
                    is_init_container=is_init,
                )
            )
    return records


def x__merge__mutmut_8(
    limits_by_pod: dict[str, list[tuple[str, int | None, int | None, bool]]],
    usage_by_pod: dict[str, dict[str, tuple[int, int]]],
    namespace: str,
) -> list[ContainerMetricsRecord]:
    records: list[ContainerMetricsRecord] = []
    for pod_name, containers in limits_by_pod.items():
        pod_usage = usage_by_pod.get(pod_name, {})
        for container_name, cpu_limit, mem_limit, is_init in containers:
            cpu_used, mem_used = pod_usage.get(None, (0, 0))
            records.append(
                ContainerMetricsRecord(
                    container_name=container_name,
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_usage_millicores=cpu_used,
                    cpu_limit_millicores=cpu_limit,
                    memory_usage_bytes=mem_used,
                    memory_limit_bytes=mem_limit,
                    is_init_container=is_init,
                )
            )
    return records


def x__merge__mutmut_9(
    limits_by_pod: dict[str, list[tuple[str, int | None, int | None, bool]]],
    usage_by_pod: dict[str, dict[str, tuple[int, int]]],
    namespace: str,
) -> list[ContainerMetricsRecord]:
    records: list[ContainerMetricsRecord] = []
    for pod_name, containers in limits_by_pod.items():
        pod_usage = usage_by_pod.get(pod_name, {})
        for container_name, cpu_limit, mem_limit, is_init in containers:
            cpu_used, mem_used = pod_usage.get(container_name, None)
            records.append(
                ContainerMetricsRecord(
                    container_name=container_name,
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_usage_millicores=cpu_used,
                    cpu_limit_millicores=cpu_limit,
                    memory_usage_bytes=mem_used,
                    memory_limit_bytes=mem_limit,
                    is_init_container=is_init,
                )
            )
    return records


def x__merge__mutmut_10(
    limits_by_pod: dict[str, list[tuple[str, int | None, int | None, bool]]],
    usage_by_pod: dict[str, dict[str, tuple[int, int]]],
    namespace: str,
) -> list[ContainerMetricsRecord]:
    records: list[ContainerMetricsRecord] = []
    for pod_name, containers in limits_by_pod.items():
        pod_usage = usage_by_pod.get(pod_name, {})
        for container_name, cpu_limit, mem_limit, is_init in containers:
            cpu_used, mem_used = pod_usage.get((0, 0))
            records.append(
                ContainerMetricsRecord(
                    container_name=container_name,
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_usage_millicores=cpu_used,
                    cpu_limit_millicores=cpu_limit,
                    memory_usage_bytes=mem_used,
                    memory_limit_bytes=mem_limit,
                    is_init_container=is_init,
                )
            )
    return records


def x__merge__mutmut_11(
    limits_by_pod: dict[str, list[tuple[str, int | None, int | None, bool]]],
    usage_by_pod: dict[str, dict[str, tuple[int, int]]],
    namespace: str,
) -> list[ContainerMetricsRecord]:
    records: list[ContainerMetricsRecord] = []
    for pod_name, containers in limits_by_pod.items():
        pod_usage = usage_by_pod.get(pod_name, {})
        for container_name, cpu_limit, mem_limit, is_init in containers:
            cpu_used, mem_used = pod_usage.get(container_name, )
            records.append(
                ContainerMetricsRecord(
                    container_name=container_name,
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_usage_millicores=cpu_used,
                    cpu_limit_millicores=cpu_limit,
                    memory_usage_bytes=mem_used,
                    memory_limit_bytes=mem_limit,
                    is_init_container=is_init,
                )
            )
    return records


def x__merge__mutmut_12(
    limits_by_pod: dict[str, list[tuple[str, int | None, int | None, bool]]],
    usage_by_pod: dict[str, dict[str, tuple[int, int]]],
    namespace: str,
) -> list[ContainerMetricsRecord]:
    records: list[ContainerMetricsRecord] = []
    for pod_name, containers in limits_by_pod.items():
        pod_usage = usage_by_pod.get(pod_name, {})
        for container_name, cpu_limit, mem_limit, is_init in containers:
            cpu_used, mem_used = pod_usage.get(container_name, (1, 0))
            records.append(
                ContainerMetricsRecord(
                    container_name=container_name,
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_usage_millicores=cpu_used,
                    cpu_limit_millicores=cpu_limit,
                    memory_usage_bytes=mem_used,
                    memory_limit_bytes=mem_limit,
                    is_init_container=is_init,
                )
            )
    return records


def x__merge__mutmut_13(
    limits_by_pod: dict[str, list[tuple[str, int | None, int | None, bool]]],
    usage_by_pod: dict[str, dict[str, tuple[int, int]]],
    namespace: str,
) -> list[ContainerMetricsRecord]:
    records: list[ContainerMetricsRecord] = []
    for pod_name, containers in limits_by_pod.items():
        pod_usage = usage_by_pod.get(pod_name, {})
        for container_name, cpu_limit, mem_limit, is_init in containers:
            cpu_used, mem_used = pod_usage.get(container_name, (0, 1))
            records.append(
                ContainerMetricsRecord(
                    container_name=container_name,
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_usage_millicores=cpu_used,
                    cpu_limit_millicores=cpu_limit,
                    memory_usage_bytes=mem_used,
                    memory_limit_bytes=mem_limit,
                    is_init_container=is_init,
                )
            )
    return records


def x__merge__mutmut_14(
    limits_by_pod: dict[str, list[tuple[str, int | None, int | None, bool]]],
    usage_by_pod: dict[str, dict[str, tuple[int, int]]],
    namespace: str,
) -> list[ContainerMetricsRecord]:
    records: list[ContainerMetricsRecord] = []
    for pod_name, containers in limits_by_pod.items():
        pod_usage = usage_by_pod.get(pod_name, {})
        for container_name, cpu_limit, mem_limit, is_init in containers:
            cpu_used, mem_used = pod_usage.get(container_name, (0, 0))
            records.append(
                None
            )
    return records


def x__merge__mutmut_15(
    limits_by_pod: dict[str, list[tuple[str, int | None, int | None, bool]]],
    usage_by_pod: dict[str, dict[str, tuple[int, int]]],
    namespace: str,
) -> list[ContainerMetricsRecord]:
    records: list[ContainerMetricsRecord] = []
    for pod_name, containers in limits_by_pod.items():
        pod_usage = usage_by_pod.get(pod_name, {})
        for container_name, cpu_limit, mem_limit, is_init in containers:
            cpu_used, mem_used = pod_usage.get(container_name, (0, 0))
            records.append(
                ContainerMetricsRecord(
                    container_name=None,
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_usage_millicores=cpu_used,
                    cpu_limit_millicores=cpu_limit,
                    memory_usage_bytes=mem_used,
                    memory_limit_bytes=mem_limit,
                    is_init_container=is_init,
                )
            )
    return records


def x__merge__mutmut_16(
    limits_by_pod: dict[str, list[tuple[str, int | None, int | None, bool]]],
    usage_by_pod: dict[str, dict[str, tuple[int, int]]],
    namespace: str,
) -> list[ContainerMetricsRecord]:
    records: list[ContainerMetricsRecord] = []
    for pod_name, containers in limits_by_pod.items():
        pod_usage = usage_by_pod.get(pod_name, {})
        for container_name, cpu_limit, mem_limit, is_init in containers:
            cpu_used, mem_used = pod_usage.get(container_name, (0, 0))
            records.append(
                ContainerMetricsRecord(
                    container_name=container_name,
                    pod_name=None,
                    namespace=namespace,
                    cpu_usage_millicores=cpu_used,
                    cpu_limit_millicores=cpu_limit,
                    memory_usage_bytes=mem_used,
                    memory_limit_bytes=mem_limit,
                    is_init_container=is_init,
                )
            )
    return records


def x__merge__mutmut_17(
    limits_by_pod: dict[str, list[tuple[str, int | None, int | None, bool]]],
    usage_by_pod: dict[str, dict[str, tuple[int, int]]],
    namespace: str,
) -> list[ContainerMetricsRecord]:
    records: list[ContainerMetricsRecord] = []
    for pod_name, containers in limits_by_pod.items():
        pod_usage = usage_by_pod.get(pod_name, {})
        for container_name, cpu_limit, mem_limit, is_init in containers:
            cpu_used, mem_used = pod_usage.get(container_name, (0, 0))
            records.append(
                ContainerMetricsRecord(
                    container_name=container_name,
                    pod_name=pod_name,
                    namespace=None,
                    cpu_usage_millicores=cpu_used,
                    cpu_limit_millicores=cpu_limit,
                    memory_usage_bytes=mem_used,
                    memory_limit_bytes=mem_limit,
                    is_init_container=is_init,
                )
            )
    return records


def x__merge__mutmut_18(
    limits_by_pod: dict[str, list[tuple[str, int | None, int | None, bool]]],
    usage_by_pod: dict[str, dict[str, tuple[int, int]]],
    namespace: str,
) -> list[ContainerMetricsRecord]:
    records: list[ContainerMetricsRecord] = []
    for pod_name, containers in limits_by_pod.items():
        pod_usage = usage_by_pod.get(pod_name, {})
        for container_name, cpu_limit, mem_limit, is_init in containers:
            cpu_used, mem_used = pod_usage.get(container_name, (0, 0))
            records.append(
                ContainerMetricsRecord(
                    container_name=container_name,
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_usage_millicores=None,
                    cpu_limit_millicores=cpu_limit,
                    memory_usage_bytes=mem_used,
                    memory_limit_bytes=mem_limit,
                    is_init_container=is_init,
                )
            )
    return records


def x__merge__mutmut_19(
    limits_by_pod: dict[str, list[tuple[str, int | None, int | None, bool]]],
    usage_by_pod: dict[str, dict[str, tuple[int, int]]],
    namespace: str,
) -> list[ContainerMetricsRecord]:
    records: list[ContainerMetricsRecord] = []
    for pod_name, containers in limits_by_pod.items():
        pod_usage = usage_by_pod.get(pod_name, {})
        for container_name, cpu_limit, mem_limit, is_init in containers:
            cpu_used, mem_used = pod_usage.get(container_name, (0, 0))
            records.append(
                ContainerMetricsRecord(
                    container_name=container_name,
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_usage_millicores=cpu_used,
                    cpu_limit_millicores=None,
                    memory_usage_bytes=mem_used,
                    memory_limit_bytes=mem_limit,
                    is_init_container=is_init,
                )
            )
    return records


def x__merge__mutmut_20(
    limits_by_pod: dict[str, list[tuple[str, int | None, int | None, bool]]],
    usage_by_pod: dict[str, dict[str, tuple[int, int]]],
    namespace: str,
) -> list[ContainerMetricsRecord]:
    records: list[ContainerMetricsRecord] = []
    for pod_name, containers in limits_by_pod.items():
        pod_usage = usage_by_pod.get(pod_name, {})
        for container_name, cpu_limit, mem_limit, is_init in containers:
            cpu_used, mem_used = pod_usage.get(container_name, (0, 0))
            records.append(
                ContainerMetricsRecord(
                    container_name=container_name,
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_usage_millicores=cpu_used,
                    cpu_limit_millicores=cpu_limit,
                    memory_usage_bytes=None,
                    memory_limit_bytes=mem_limit,
                    is_init_container=is_init,
                )
            )
    return records


def x__merge__mutmut_21(
    limits_by_pod: dict[str, list[tuple[str, int | None, int | None, bool]]],
    usage_by_pod: dict[str, dict[str, tuple[int, int]]],
    namespace: str,
) -> list[ContainerMetricsRecord]:
    records: list[ContainerMetricsRecord] = []
    for pod_name, containers in limits_by_pod.items():
        pod_usage = usage_by_pod.get(pod_name, {})
        for container_name, cpu_limit, mem_limit, is_init in containers:
            cpu_used, mem_used = pod_usage.get(container_name, (0, 0))
            records.append(
                ContainerMetricsRecord(
                    container_name=container_name,
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_usage_millicores=cpu_used,
                    cpu_limit_millicores=cpu_limit,
                    memory_usage_bytes=mem_used,
                    memory_limit_bytes=None,
                    is_init_container=is_init,
                )
            )
    return records


def x__merge__mutmut_22(
    limits_by_pod: dict[str, list[tuple[str, int | None, int | None, bool]]],
    usage_by_pod: dict[str, dict[str, tuple[int, int]]],
    namespace: str,
) -> list[ContainerMetricsRecord]:
    records: list[ContainerMetricsRecord] = []
    for pod_name, containers in limits_by_pod.items():
        pod_usage = usage_by_pod.get(pod_name, {})
        for container_name, cpu_limit, mem_limit, is_init in containers:
            cpu_used, mem_used = pod_usage.get(container_name, (0, 0))
            records.append(
                ContainerMetricsRecord(
                    container_name=container_name,
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_usage_millicores=cpu_used,
                    cpu_limit_millicores=cpu_limit,
                    memory_usage_bytes=mem_used,
                    memory_limit_bytes=mem_limit,
                    is_init_container=None,
                )
            )
    return records


def x__merge__mutmut_23(
    limits_by_pod: dict[str, list[tuple[str, int | None, int | None, bool]]],
    usage_by_pod: dict[str, dict[str, tuple[int, int]]],
    namespace: str,
) -> list[ContainerMetricsRecord]:
    records: list[ContainerMetricsRecord] = []
    for pod_name, containers in limits_by_pod.items():
        pod_usage = usage_by_pod.get(pod_name, {})
        for container_name, cpu_limit, mem_limit, is_init in containers:
            cpu_used, mem_used = pod_usage.get(container_name, (0, 0))
            records.append(
                ContainerMetricsRecord(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_usage_millicores=cpu_used,
                    cpu_limit_millicores=cpu_limit,
                    memory_usage_bytes=mem_used,
                    memory_limit_bytes=mem_limit,
                    is_init_container=is_init,
                )
            )
    return records


def x__merge__mutmut_24(
    limits_by_pod: dict[str, list[tuple[str, int | None, int | None, bool]]],
    usage_by_pod: dict[str, dict[str, tuple[int, int]]],
    namespace: str,
) -> list[ContainerMetricsRecord]:
    records: list[ContainerMetricsRecord] = []
    for pod_name, containers in limits_by_pod.items():
        pod_usage = usage_by_pod.get(pod_name, {})
        for container_name, cpu_limit, mem_limit, is_init in containers:
            cpu_used, mem_used = pod_usage.get(container_name, (0, 0))
            records.append(
                ContainerMetricsRecord(
                    container_name=container_name,
                    namespace=namespace,
                    cpu_usage_millicores=cpu_used,
                    cpu_limit_millicores=cpu_limit,
                    memory_usage_bytes=mem_used,
                    memory_limit_bytes=mem_limit,
                    is_init_container=is_init,
                )
            )
    return records


def x__merge__mutmut_25(
    limits_by_pod: dict[str, list[tuple[str, int | None, int | None, bool]]],
    usage_by_pod: dict[str, dict[str, tuple[int, int]]],
    namespace: str,
) -> list[ContainerMetricsRecord]:
    records: list[ContainerMetricsRecord] = []
    for pod_name, containers in limits_by_pod.items():
        pod_usage = usage_by_pod.get(pod_name, {})
        for container_name, cpu_limit, mem_limit, is_init in containers:
            cpu_used, mem_used = pod_usage.get(container_name, (0, 0))
            records.append(
                ContainerMetricsRecord(
                    container_name=container_name,
                    pod_name=pod_name,
                    cpu_usage_millicores=cpu_used,
                    cpu_limit_millicores=cpu_limit,
                    memory_usage_bytes=mem_used,
                    memory_limit_bytes=mem_limit,
                    is_init_container=is_init,
                )
            )
    return records


def x__merge__mutmut_26(
    limits_by_pod: dict[str, list[tuple[str, int | None, int | None, bool]]],
    usage_by_pod: dict[str, dict[str, tuple[int, int]]],
    namespace: str,
) -> list[ContainerMetricsRecord]:
    records: list[ContainerMetricsRecord] = []
    for pod_name, containers in limits_by_pod.items():
        pod_usage = usage_by_pod.get(pod_name, {})
        for container_name, cpu_limit, mem_limit, is_init in containers:
            cpu_used, mem_used = pod_usage.get(container_name, (0, 0))
            records.append(
                ContainerMetricsRecord(
                    container_name=container_name,
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_limit_millicores=cpu_limit,
                    memory_usage_bytes=mem_used,
                    memory_limit_bytes=mem_limit,
                    is_init_container=is_init,
                )
            )
    return records


def x__merge__mutmut_27(
    limits_by_pod: dict[str, list[tuple[str, int | None, int | None, bool]]],
    usage_by_pod: dict[str, dict[str, tuple[int, int]]],
    namespace: str,
) -> list[ContainerMetricsRecord]:
    records: list[ContainerMetricsRecord] = []
    for pod_name, containers in limits_by_pod.items():
        pod_usage = usage_by_pod.get(pod_name, {})
        for container_name, cpu_limit, mem_limit, is_init in containers:
            cpu_used, mem_used = pod_usage.get(container_name, (0, 0))
            records.append(
                ContainerMetricsRecord(
                    container_name=container_name,
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_usage_millicores=cpu_used,
                    memory_usage_bytes=mem_used,
                    memory_limit_bytes=mem_limit,
                    is_init_container=is_init,
                )
            )
    return records


def x__merge__mutmut_28(
    limits_by_pod: dict[str, list[tuple[str, int | None, int | None, bool]]],
    usage_by_pod: dict[str, dict[str, tuple[int, int]]],
    namespace: str,
) -> list[ContainerMetricsRecord]:
    records: list[ContainerMetricsRecord] = []
    for pod_name, containers in limits_by_pod.items():
        pod_usage = usage_by_pod.get(pod_name, {})
        for container_name, cpu_limit, mem_limit, is_init in containers:
            cpu_used, mem_used = pod_usage.get(container_name, (0, 0))
            records.append(
                ContainerMetricsRecord(
                    container_name=container_name,
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_usage_millicores=cpu_used,
                    cpu_limit_millicores=cpu_limit,
                    memory_limit_bytes=mem_limit,
                    is_init_container=is_init,
                )
            )
    return records


def x__merge__mutmut_29(
    limits_by_pod: dict[str, list[tuple[str, int | None, int | None, bool]]],
    usage_by_pod: dict[str, dict[str, tuple[int, int]]],
    namespace: str,
) -> list[ContainerMetricsRecord]:
    records: list[ContainerMetricsRecord] = []
    for pod_name, containers in limits_by_pod.items():
        pod_usage = usage_by_pod.get(pod_name, {})
        for container_name, cpu_limit, mem_limit, is_init in containers:
            cpu_used, mem_used = pod_usage.get(container_name, (0, 0))
            records.append(
                ContainerMetricsRecord(
                    container_name=container_name,
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_usage_millicores=cpu_used,
                    cpu_limit_millicores=cpu_limit,
                    memory_usage_bytes=mem_used,
                    is_init_container=is_init,
                )
            )
    return records


def x__merge__mutmut_30(
    limits_by_pod: dict[str, list[tuple[str, int | None, int | None, bool]]],
    usage_by_pod: dict[str, dict[str, tuple[int, int]]],
    namespace: str,
) -> list[ContainerMetricsRecord]:
    records: list[ContainerMetricsRecord] = []
    for pod_name, containers in limits_by_pod.items():
        pod_usage = usage_by_pod.get(pod_name, {})
        for container_name, cpu_limit, mem_limit, is_init in containers:
            cpu_used, mem_used = pod_usage.get(container_name, (0, 0))
            records.append(
                ContainerMetricsRecord(
                    container_name=container_name,
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_usage_millicores=cpu_used,
                    cpu_limit_millicores=cpu_limit,
                    memory_usage_bytes=mem_used,
                    memory_limit_bytes=mem_limit,
                    )
            )
    return records

mutants_x__merge__mutmut['_mutmut_orig'] = x__merge__mutmut_orig # type: ignore # mutmut generated
mutants_x__merge__mutmut['x__merge__mutmut_1'] = x__merge__mutmut_1 # type: ignore # mutmut generated
mutants_x__merge__mutmut['x__merge__mutmut_2'] = x__merge__mutmut_2 # type: ignore # mutmut generated
mutants_x__merge__mutmut['x__merge__mutmut_3'] = x__merge__mutmut_3 # type: ignore # mutmut generated
mutants_x__merge__mutmut['x__merge__mutmut_4'] = x__merge__mutmut_4 # type: ignore # mutmut generated
mutants_x__merge__mutmut['x__merge__mutmut_5'] = x__merge__mutmut_5 # type: ignore # mutmut generated
mutants_x__merge__mutmut['x__merge__mutmut_6'] = x__merge__mutmut_6 # type: ignore # mutmut generated
mutants_x__merge__mutmut['x__merge__mutmut_7'] = x__merge__mutmut_7 # type: ignore # mutmut generated
mutants_x__merge__mutmut['x__merge__mutmut_8'] = x__merge__mutmut_8 # type: ignore # mutmut generated
mutants_x__merge__mutmut['x__merge__mutmut_9'] = x__merge__mutmut_9 # type: ignore # mutmut generated
mutants_x__merge__mutmut['x__merge__mutmut_10'] = x__merge__mutmut_10 # type: ignore # mutmut generated
mutants_x__merge__mutmut['x__merge__mutmut_11'] = x__merge__mutmut_11 # type: ignore # mutmut generated
mutants_x__merge__mutmut['x__merge__mutmut_12'] = x__merge__mutmut_12 # type: ignore # mutmut generated
mutants_x__merge__mutmut['x__merge__mutmut_13'] = x__merge__mutmut_13 # type: ignore # mutmut generated
mutants_x__merge__mutmut['x__merge__mutmut_14'] = x__merge__mutmut_14 # type: ignore # mutmut generated
mutants_x__merge__mutmut['x__merge__mutmut_15'] = x__merge__mutmut_15 # type: ignore # mutmut generated
mutants_x__merge__mutmut['x__merge__mutmut_16'] = x__merge__mutmut_16 # type: ignore # mutmut generated
mutants_x__merge__mutmut['x__merge__mutmut_17'] = x__merge__mutmut_17 # type: ignore # mutmut generated
mutants_x__merge__mutmut['x__merge__mutmut_18'] = x__merge__mutmut_18 # type: ignore # mutmut generated
mutants_x__merge__mutmut['x__merge__mutmut_19'] = x__merge__mutmut_19 # type: ignore # mutmut generated
mutants_x__merge__mutmut['x__merge__mutmut_20'] = x__merge__mutmut_20 # type: ignore # mutmut generated
mutants_x__merge__mutmut['x__merge__mutmut_21'] = x__merge__mutmut_21 # type: ignore # mutmut generated
mutants_x__merge__mutmut['x__merge__mutmut_22'] = x__merge__mutmut_22 # type: ignore # mutmut generated
mutants_x__merge__mutmut['x__merge__mutmut_23'] = x__merge__mutmut_23 # type: ignore # mutmut generated
mutants_x__merge__mutmut['x__merge__mutmut_24'] = x__merge__mutmut_24 # type: ignore # mutmut generated
mutants_x__merge__mutmut['x__merge__mutmut_25'] = x__merge__mutmut_25 # type: ignore # mutmut generated
mutants_x__merge__mutmut['x__merge__mutmut_26'] = x__merge__mutmut_26 # type: ignore # mutmut generated
mutants_x__merge__mutmut['x__merge__mutmut_27'] = x__merge__mutmut_27 # type: ignore # mutmut generated
mutants_x__merge__mutmut['x__merge__mutmut_28'] = x__merge__mutmut_28 # type: ignore # mutmut generated
mutants_x__merge__mutmut['x__merge__mutmut_29'] = x__merge__mutmut_29 # type: ignore # mutmut generated
mutants_x__merge__mutmut['x__merge__mutmut_30'] = x__merge__mutmut_30 # type: ignore # mutmut generated
