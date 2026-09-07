from __future__ import annotations

from hexawyn.application.ports.driven.capacity_forecast_port import (
    CapacityForecastPort,
    ClusterCapacityInfoRaw,
)
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError

_K8S_FORBIDDEN = 403
_AUTOSCALER_NAME_HINT = "cluster-autoscaler"
_BYTES_PER_GB = 1024.0**3
_KUBE_SYSTEM_NAMESPACE = "kube-system"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut: MutantDict = {}  # type: ignore


class KubernetesCapacityForecastAdapter(CapacityForecastPort):
    """Secondary adapter — sums node-allocatable CPU/memory and detects
    cluster-autoscaler presence. Cluster CPU/memory usage history is fetched
    separately via the existing MetricsQueryPort (ECA-31) — deliberately not
    duplicated here (see plan Context)."""

    @_mutmut_mutated(mutants_xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut)
    def get_cluster_capacity_info(self) -> ClusterCapacityInfoRaw:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(exc) from exc

        total_cpu = sum(_node_allocatable_cpu(node) for node in node_list.items)
        total_memory_gb = sum(_node_allocatable_memory_gb(node) for node in node_list.items)

        return ClusterCapacityInfoRaw(
            total_allocatable_cpu_cores=total_cpu,
            total_allocatable_memory_gb=total_memory_gb,
            autoscaler_enabled=_detect_autoscaler(k8s),
        )

    def xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_orig(self) -> ClusterCapacityInfoRaw:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(exc) from exc

        total_cpu = sum(_node_allocatable_cpu(node) for node in node_list.items)
        total_memory_gb = sum(_node_allocatable_memory_gb(node) for node in node_list.items)

        return ClusterCapacityInfoRaw(
            total_allocatable_cpu_cores=total_cpu,
            total_allocatable_memory_gb=total_memory_gb,
            autoscaler_enabled=_detect_autoscaler(k8s),
        )

    def xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_1(self) -> ClusterCapacityInfoRaw:
        from kubernetes import client as k8s

        core_api = None
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(exc) from exc

        total_cpu = sum(_node_allocatable_cpu(node) for node in node_list.items)
        total_memory_gb = sum(_node_allocatable_memory_gb(node) for node in node_list.items)

        return ClusterCapacityInfoRaw(
            total_allocatable_cpu_cores=total_cpu,
            total_allocatable_memory_gb=total_memory_gb,
            autoscaler_enabled=_detect_autoscaler(k8s),
        )

    def xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_2(self) -> ClusterCapacityInfoRaw:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = None
        except Exception as exc:
            raise _translate_error(exc) from exc

        total_cpu = sum(_node_allocatable_cpu(node) for node in node_list.items)
        total_memory_gb = sum(_node_allocatable_memory_gb(node) for node in node_list.items)

        return ClusterCapacityInfoRaw(
            total_allocatable_cpu_cores=total_cpu,
            total_allocatable_memory_gb=total_memory_gb,
            autoscaler_enabled=_detect_autoscaler(k8s),
        )

    def xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_3(self) -> ClusterCapacityInfoRaw:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(None) from exc

        total_cpu = sum(_node_allocatable_cpu(node) for node in node_list.items)
        total_memory_gb = sum(_node_allocatable_memory_gb(node) for node in node_list.items)

        return ClusterCapacityInfoRaw(
            total_allocatable_cpu_cores=total_cpu,
            total_allocatable_memory_gb=total_memory_gb,
            autoscaler_enabled=_detect_autoscaler(k8s),
        )

    def xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_4(self) -> ClusterCapacityInfoRaw:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(exc) from exc

        total_cpu = None
        total_memory_gb = sum(_node_allocatable_memory_gb(node) for node in node_list.items)

        return ClusterCapacityInfoRaw(
            total_allocatable_cpu_cores=total_cpu,
            total_allocatable_memory_gb=total_memory_gb,
            autoscaler_enabled=_detect_autoscaler(k8s),
        )

    def xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_5(self) -> ClusterCapacityInfoRaw:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(exc) from exc

        total_cpu = sum(None)
        total_memory_gb = sum(_node_allocatable_memory_gb(node) for node in node_list.items)

        return ClusterCapacityInfoRaw(
            total_allocatable_cpu_cores=total_cpu,
            total_allocatable_memory_gb=total_memory_gb,
            autoscaler_enabled=_detect_autoscaler(k8s),
        )

    def xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_6(self) -> ClusterCapacityInfoRaw:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(exc) from exc

        total_cpu = sum(_node_allocatable_cpu(None) for node in node_list.items)
        total_memory_gb = sum(_node_allocatable_memory_gb(node) for node in node_list.items)

        return ClusterCapacityInfoRaw(
            total_allocatable_cpu_cores=total_cpu,
            total_allocatable_memory_gb=total_memory_gb,
            autoscaler_enabled=_detect_autoscaler(k8s),
        )

    def xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_7(self) -> ClusterCapacityInfoRaw:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(exc) from exc

        total_cpu = sum(_node_allocatable_cpu(node) for node in node_list.items)
        total_memory_gb = None

        return ClusterCapacityInfoRaw(
            total_allocatable_cpu_cores=total_cpu,
            total_allocatable_memory_gb=total_memory_gb,
            autoscaler_enabled=_detect_autoscaler(k8s),
        )

    def xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_8(self) -> ClusterCapacityInfoRaw:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(exc) from exc

        total_cpu = sum(_node_allocatable_cpu(node) for node in node_list.items)
        total_memory_gb = sum(None)

        return ClusterCapacityInfoRaw(
            total_allocatable_cpu_cores=total_cpu,
            total_allocatable_memory_gb=total_memory_gb,
            autoscaler_enabled=_detect_autoscaler(k8s),
        )

    def xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_9(self) -> ClusterCapacityInfoRaw:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(exc) from exc

        total_cpu = sum(_node_allocatable_cpu(node) for node in node_list.items)
        total_memory_gb = sum(_node_allocatable_memory_gb(None) for node in node_list.items)

        return ClusterCapacityInfoRaw(
            total_allocatable_cpu_cores=total_cpu,
            total_allocatable_memory_gb=total_memory_gb,
            autoscaler_enabled=_detect_autoscaler(k8s),
        )

    def xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_10(self) -> ClusterCapacityInfoRaw:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(exc) from exc

        total_cpu = sum(_node_allocatable_cpu(node) for node in node_list.items)
        total_memory_gb = sum(_node_allocatable_memory_gb(node) for node in node_list.items)

        return ClusterCapacityInfoRaw(
            total_allocatable_cpu_cores=None,
            total_allocatable_memory_gb=total_memory_gb,
            autoscaler_enabled=_detect_autoscaler(k8s),
        )

    def xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_11(self) -> ClusterCapacityInfoRaw:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(exc) from exc

        total_cpu = sum(_node_allocatable_cpu(node) for node in node_list.items)
        total_memory_gb = sum(_node_allocatable_memory_gb(node) for node in node_list.items)

        return ClusterCapacityInfoRaw(
            total_allocatable_cpu_cores=total_cpu,
            total_allocatable_memory_gb=None,
            autoscaler_enabled=_detect_autoscaler(k8s),
        )

    def xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_12(self) -> ClusterCapacityInfoRaw:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(exc) from exc

        total_cpu = sum(_node_allocatable_cpu(node) for node in node_list.items)
        total_memory_gb = sum(_node_allocatable_memory_gb(node) for node in node_list.items)

        return ClusterCapacityInfoRaw(
            total_allocatable_cpu_cores=total_cpu,
            total_allocatable_memory_gb=total_memory_gb,
            autoscaler_enabled=None,
        )

    def xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_13(self) -> ClusterCapacityInfoRaw:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(exc) from exc

        total_cpu = sum(_node_allocatable_cpu(node) for node in node_list.items)
        total_memory_gb = sum(_node_allocatable_memory_gb(node) for node in node_list.items)

        return ClusterCapacityInfoRaw(
            total_allocatable_memory_gb=total_memory_gb,
            autoscaler_enabled=_detect_autoscaler(k8s),
        )

    def xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_14(self) -> ClusterCapacityInfoRaw:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(exc) from exc

        total_cpu = sum(_node_allocatable_cpu(node) for node in node_list.items)
        total_memory_gb = sum(_node_allocatable_memory_gb(node) for node in node_list.items)

        return ClusterCapacityInfoRaw(
            total_allocatable_cpu_cores=total_cpu,
            autoscaler_enabled=_detect_autoscaler(k8s),
        )

    def xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_15(self) -> ClusterCapacityInfoRaw:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(exc) from exc

        total_cpu = sum(_node_allocatable_cpu(node) for node in node_list.items)
        total_memory_gb = sum(_node_allocatable_memory_gb(node) for node in node_list.items)

        return ClusterCapacityInfoRaw(
            total_allocatable_cpu_cores=total_cpu,
            total_allocatable_memory_gb=total_memory_gb,
            )

    def xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_16(self) -> ClusterCapacityInfoRaw:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(exc) from exc

        total_cpu = sum(_node_allocatable_cpu(node) for node in node_list.items)
        total_memory_gb = sum(_node_allocatable_memory_gb(node) for node in node_list.items)

        return ClusterCapacityInfoRaw(
            total_allocatable_cpu_cores=total_cpu,
            total_allocatable_memory_gb=total_memory_gb,
            autoscaler_enabled=_detect_autoscaler(None),
        )

mutants_xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut['_mutmut_orig'] = KubernetesCapacityForecastAdapter.xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut['xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_1'] = KubernetesCapacityForecastAdapter.xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut['xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_2'] = KubernetesCapacityForecastAdapter.xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut['xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_3'] = KubernetesCapacityForecastAdapter.xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut['xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_4'] = KubernetesCapacityForecastAdapter.xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut['xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_5'] = KubernetesCapacityForecastAdapter.xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut['xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_6'] = KubernetesCapacityForecastAdapter.xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut['xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_7'] = KubernetesCapacityForecastAdapter.xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut['xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_8'] = KubernetesCapacityForecastAdapter.xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut['xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_9'] = KubernetesCapacityForecastAdapter.xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut['xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_10'] = KubernetesCapacityForecastAdapter.xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut['xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_11'] = KubernetesCapacityForecastAdapter.xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut['xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_12'] = KubernetesCapacityForecastAdapter.xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut['xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_13'] = KubernetesCapacityForecastAdapter.xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut['xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_14'] = KubernetesCapacityForecastAdapter.xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_14 # type: ignore # mutmut generated
mutants_xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut['xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_15'] = KubernetesCapacityForecastAdapter.xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_15 # type: ignore # mutmut generated
mutants_xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut['xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_16'] = KubernetesCapacityForecastAdapter.xǁKubernetesCapacityForecastAdapterǁget_cluster_capacity_info__mutmut_16 # type: ignore # mutmut generated
mutants_x__detect_autoscaler__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__detect_autoscaler__mutmut)
def _detect_autoscaler(k8s: object) -> bool:
    apps_api = k8s.AppsV1Api()  # type: ignore[attr-defined]
    try:
        deployments = apps_api.list_namespaced_deployment(namespace=_KUBE_SYSTEM_NAMESPACE)
    except Exception:
        return False
    return any(
        _AUTOSCALER_NAME_HINT in (deployment.metadata.name or "").lower()
        for deployment in deployments.items
    )


def x__detect_autoscaler__mutmut_orig(k8s: object) -> bool:
    apps_api = k8s.AppsV1Api()  # type: ignore[attr-defined]
    try:
        deployments = apps_api.list_namespaced_deployment(namespace=_KUBE_SYSTEM_NAMESPACE)
    except Exception:
        return False
    return any(
        _AUTOSCALER_NAME_HINT in (deployment.metadata.name or "").lower()
        for deployment in deployments.items
    )


def x__detect_autoscaler__mutmut_1(k8s: object) -> bool:
    apps_api = None  # type: ignore[attr-defined]
    try:
        deployments = apps_api.list_namespaced_deployment(namespace=_KUBE_SYSTEM_NAMESPACE)
    except Exception:
        return False
    return any(
        _AUTOSCALER_NAME_HINT in (deployment.metadata.name or "").lower()
        for deployment in deployments.items
    )


def x__detect_autoscaler__mutmut_2(k8s: object) -> bool:
    apps_api = k8s.AppsV1Api()  # type: ignore[attr-defined]
    try:
        deployments = None
    except Exception:
        return False
    return any(
        _AUTOSCALER_NAME_HINT in (deployment.metadata.name or "").lower()
        for deployment in deployments.items
    )


def x__detect_autoscaler__mutmut_3(k8s: object) -> bool:
    apps_api = k8s.AppsV1Api()  # type: ignore[attr-defined]
    try:
        deployments = apps_api.list_namespaced_deployment(namespace=None)
    except Exception:
        return False
    return any(
        _AUTOSCALER_NAME_HINT in (deployment.metadata.name or "").lower()
        for deployment in deployments.items
    )


def x__detect_autoscaler__mutmut_4(k8s: object) -> bool:
    apps_api = k8s.AppsV1Api()  # type: ignore[attr-defined]
    try:
        deployments = apps_api.list_namespaced_deployment(namespace=_KUBE_SYSTEM_NAMESPACE)
    except Exception:
        return True
    return any(
        _AUTOSCALER_NAME_HINT in (deployment.metadata.name or "").lower()
        for deployment in deployments.items
    )


def x__detect_autoscaler__mutmut_5(k8s: object) -> bool:
    apps_api = k8s.AppsV1Api()  # type: ignore[attr-defined]
    try:
        deployments = apps_api.list_namespaced_deployment(namespace=_KUBE_SYSTEM_NAMESPACE)
    except Exception:
        return False
    return any(
        None
    )


def x__detect_autoscaler__mutmut_6(k8s: object) -> bool:
    apps_api = k8s.AppsV1Api()  # type: ignore[attr-defined]
    try:
        deployments = apps_api.list_namespaced_deployment(namespace=_KUBE_SYSTEM_NAMESPACE)
    except Exception:
        return False
    return any(
        _AUTOSCALER_NAME_HINT not in (deployment.metadata.name or "").lower()
        for deployment in deployments.items
    )


def x__detect_autoscaler__mutmut_7(k8s: object) -> bool:
    apps_api = k8s.AppsV1Api()  # type: ignore[attr-defined]
    try:
        deployments = apps_api.list_namespaced_deployment(namespace=_KUBE_SYSTEM_NAMESPACE)
    except Exception:
        return False
    return any(
        _AUTOSCALER_NAME_HINT in (deployment.metadata.name or "").upper()
        for deployment in deployments.items
    )


def x__detect_autoscaler__mutmut_8(k8s: object) -> bool:
    apps_api = k8s.AppsV1Api()  # type: ignore[attr-defined]
    try:
        deployments = apps_api.list_namespaced_deployment(namespace=_KUBE_SYSTEM_NAMESPACE)
    except Exception:
        return False
    return any(
        _AUTOSCALER_NAME_HINT in (deployment.metadata.name and "").lower()
        for deployment in deployments.items
    )


def x__detect_autoscaler__mutmut_9(k8s: object) -> bool:
    apps_api = k8s.AppsV1Api()  # type: ignore[attr-defined]
    try:
        deployments = apps_api.list_namespaced_deployment(namespace=_KUBE_SYSTEM_NAMESPACE)
    except Exception:
        return False
    return any(
        _AUTOSCALER_NAME_HINT in (deployment.metadata.name or "XXXX").lower()
        for deployment in deployments.items
    )

mutants_x__detect_autoscaler__mutmut['_mutmut_orig'] = x__detect_autoscaler__mutmut_orig # type: ignore # mutmut generated
mutants_x__detect_autoscaler__mutmut['x__detect_autoscaler__mutmut_1'] = x__detect_autoscaler__mutmut_1 # type: ignore # mutmut generated
mutants_x__detect_autoscaler__mutmut['x__detect_autoscaler__mutmut_2'] = x__detect_autoscaler__mutmut_2 # type: ignore # mutmut generated
mutants_x__detect_autoscaler__mutmut['x__detect_autoscaler__mutmut_3'] = x__detect_autoscaler__mutmut_3 # type: ignore # mutmut generated
mutants_x__detect_autoscaler__mutmut['x__detect_autoscaler__mutmut_4'] = x__detect_autoscaler__mutmut_4 # type: ignore # mutmut generated
mutants_x__detect_autoscaler__mutmut['x__detect_autoscaler__mutmut_5'] = x__detect_autoscaler__mutmut_5 # type: ignore # mutmut generated
mutants_x__detect_autoscaler__mutmut['x__detect_autoscaler__mutmut_6'] = x__detect_autoscaler__mutmut_6 # type: ignore # mutmut generated
mutants_x__detect_autoscaler__mutmut['x__detect_autoscaler__mutmut_7'] = x__detect_autoscaler__mutmut_7 # type: ignore # mutmut generated
mutants_x__detect_autoscaler__mutmut['x__detect_autoscaler__mutmut_8'] = x__detect_autoscaler__mutmut_8 # type: ignore # mutmut generated
mutants_x__detect_autoscaler__mutmut['x__detect_autoscaler__mutmut_9'] = x__detect_autoscaler__mutmut_9 # type: ignore # mutmut generated
mutants_x__node_allocatable__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__node_allocatable__mutmut)
def _node_allocatable(node: object) -> dict[str, str]:
    status = getattr(node, "status", None)
    allocatable = getattr(status, "allocatable", None)
    return allocatable if isinstance(allocatable, dict) else {}


def x__node_allocatable__mutmut_orig(node: object) -> dict[str, str]:
    status = getattr(node, "status", None)
    allocatable = getattr(status, "allocatable", None)
    return allocatable if isinstance(allocatable, dict) else {}


def x__node_allocatable__mutmut_1(node: object) -> dict[str, str]:
    status = None
    allocatable = getattr(status, "allocatable", None)
    return allocatable if isinstance(allocatable, dict) else {}


def x__node_allocatable__mutmut_2(node: object) -> dict[str, str]:
    status = getattr(None, "status", None)
    allocatable = getattr(status, "allocatable", None)
    return allocatable if isinstance(allocatable, dict) else {}


def x__node_allocatable__mutmut_3(node: object) -> dict[str, str]:
    status = getattr(node, None, None)
    allocatable = getattr(status, "allocatable", None)
    return allocatable if isinstance(allocatable, dict) else {}


def x__node_allocatable__mutmut_4(node: object) -> dict[str, str]:
    status = getattr("status", None)
    allocatable = getattr(status, "allocatable", None)
    return allocatable if isinstance(allocatable, dict) else {}


def x__node_allocatable__mutmut_5(node: object) -> dict[str, str]:
    status = getattr(node, None)
    allocatable = getattr(status, "allocatable", None)
    return allocatable if isinstance(allocatable, dict) else {}


def x__node_allocatable__mutmut_6(node: object) -> dict[str, str]:
    status = getattr(node, "status", )
    allocatable = getattr(status, "allocatable", None)
    return allocatable if isinstance(allocatable, dict) else {}


def x__node_allocatable__mutmut_7(node: object) -> dict[str, str]:
    status = getattr(node, "XXstatusXX", None)
    allocatable = getattr(status, "allocatable", None)
    return allocatable if isinstance(allocatable, dict) else {}


def x__node_allocatable__mutmut_8(node: object) -> dict[str, str]:
    status = getattr(node, "STATUS", None)
    allocatable = getattr(status, "allocatable", None)
    return allocatable if isinstance(allocatable, dict) else {}


def x__node_allocatable__mutmut_9(node: object) -> dict[str, str]:
    status = getattr(node, "status", None)
    allocatable = None
    return allocatable if isinstance(allocatable, dict) else {}


def x__node_allocatable__mutmut_10(node: object) -> dict[str, str]:
    status = getattr(node, "status", None)
    allocatable = getattr(None, "allocatable", None)
    return allocatable if isinstance(allocatable, dict) else {}


def x__node_allocatable__mutmut_11(node: object) -> dict[str, str]:
    status = getattr(node, "status", None)
    allocatable = getattr(status, None, None)
    return allocatable if isinstance(allocatable, dict) else {}


def x__node_allocatable__mutmut_12(node: object) -> dict[str, str]:
    status = getattr(node, "status", None)
    allocatable = getattr("allocatable", None)
    return allocatable if isinstance(allocatable, dict) else {}


def x__node_allocatable__mutmut_13(node: object) -> dict[str, str]:
    status = getattr(node, "status", None)
    allocatable = getattr(status, None)
    return allocatable if isinstance(allocatable, dict) else {}


def x__node_allocatable__mutmut_14(node: object) -> dict[str, str]:
    status = getattr(node, "status", None)
    allocatable = getattr(status, "allocatable", )
    return allocatable if isinstance(allocatable, dict) else {}


def x__node_allocatable__mutmut_15(node: object) -> dict[str, str]:
    status = getattr(node, "status", None)
    allocatable = getattr(status, "XXallocatableXX", None)
    return allocatable if isinstance(allocatable, dict) else {}


def x__node_allocatable__mutmut_16(node: object) -> dict[str, str]:
    status = getattr(node, "status", None)
    allocatable = getattr(status, "ALLOCATABLE", None)
    return allocatable if isinstance(allocatable, dict) else {}

mutants_x__node_allocatable__mutmut['_mutmut_orig'] = x__node_allocatable__mutmut_orig # type: ignore # mutmut generated
mutants_x__node_allocatable__mutmut['x__node_allocatable__mutmut_1'] = x__node_allocatable__mutmut_1 # type: ignore # mutmut generated
mutants_x__node_allocatable__mutmut['x__node_allocatable__mutmut_2'] = x__node_allocatable__mutmut_2 # type: ignore # mutmut generated
mutants_x__node_allocatable__mutmut['x__node_allocatable__mutmut_3'] = x__node_allocatable__mutmut_3 # type: ignore # mutmut generated
mutants_x__node_allocatable__mutmut['x__node_allocatable__mutmut_4'] = x__node_allocatable__mutmut_4 # type: ignore # mutmut generated
mutants_x__node_allocatable__mutmut['x__node_allocatable__mutmut_5'] = x__node_allocatable__mutmut_5 # type: ignore # mutmut generated
mutants_x__node_allocatable__mutmut['x__node_allocatable__mutmut_6'] = x__node_allocatable__mutmut_6 # type: ignore # mutmut generated
mutants_x__node_allocatable__mutmut['x__node_allocatable__mutmut_7'] = x__node_allocatable__mutmut_7 # type: ignore # mutmut generated
mutants_x__node_allocatable__mutmut['x__node_allocatable__mutmut_8'] = x__node_allocatable__mutmut_8 # type: ignore # mutmut generated
mutants_x__node_allocatable__mutmut['x__node_allocatable__mutmut_9'] = x__node_allocatable__mutmut_9 # type: ignore # mutmut generated
mutants_x__node_allocatable__mutmut['x__node_allocatable__mutmut_10'] = x__node_allocatable__mutmut_10 # type: ignore # mutmut generated
mutants_x__node_allocatable__mutmut['x__node_allocatable__mutmut_11'] = x__node_allocatable__mutmut_11 # type: ignore # mutmut generated
mutants_x__node_allocatable__mutmut['x__node_allocatable__mutmut_12'] = x__node_allocatable__mutmut_12 # type: ignore # mutmut generated
mutants_x__node_allocatable__mutmut['x__node_allocatable__mutmut_13'] = x__node_allocatable__mutmut_13 # type: ignore # mutmut generated
mutants_x__node_allocatable__mutmut['x__node_allocatable__mutmut_14'] = x__node_allocatable__mutmut_14 # type: ignore # mutmut generated
mutants_x__node_allocatable__mutmut['x__node_allocatable__mutmut_15'] = x__node_allocatable__mutmut_15 # type: ignore # mutmut generated
mutants_x__node_allocatable__mutmut['x__node_allocatable__mutmut_16'] = x__node_allocatable__mutmut_16 # type: ignore # mutmut generated
mutants_x__node_allocatable_cpu__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__node_allocatable_cpu__mutmut)
def _node_allocatable_cpu(node: object) -> float:
    return _cpu_to_cores(str(_node_allocatable(node).get("cpu", "0")))


def x__node_allocatable_cpu__mutmut_orig(node: object) -> float:
    return _cpu_to_cores(str(_node_allocatable(node).get("cpu", "0")))


def x__node_allocatable_cpu__mutmut_1(node: object) -> float:
    return _cpu_to_cores(None)


def x__node_allocatable_cpu__mutmut_2(node: object) -> float:
    return _cpu_to_cores(str(None))


def x__node_allocatable_cpu__mutmut_3(node: object) -> float:
    return _cpu_to_cores(str(_node_allocatable(node).get(None, "0")))


def x__node_allocatable_cpu__mutmut_4(node: object) -> float:
    return _cpu_to_cores(str(_node_allocatable(node).get("cpu", None)))


def x__node_allocatable_cpu__mutmut_5(node: object) -> float:
    return _cpu_to_cores(str(_node_allocatable(node).get("0")))


def x__node_allocatable_cpu__mutmut_6(node: object) -> float:
    return _cpu_to_cores(str(_node_allocatable(node).get("cpu", )))


def x__node_allocatable_cpu__mutmut_7(node: object) -> float:
    return _cpu_to_cores(str(_node_allocatable(None).get("cpu", "0")))


def x__node_allocatable_cpu__mutmut_8(node: object) -> float:
    return _cpu_to_cores(str(_node_allocatable(node).get("XXcpuXX", "0")))


def x__node_allocatable_cpu__mutmut_9(node: object) -> float:
    return _cpu_to_cores(str(_node_allocatable(node).get("CPU", "0")))


def x__node_allocatable_cpu__mutmut_10(node: object) -> float:
    return _cpu_to_cores(str(_node_allocatable(node).get("cpu", "XX0XX")))

mutants_x__node_allocatable_cpu__mutmut['_mutmut_orig'] = x__node_allocatable_cpu__mutmut_orig # type: ignore # mutmut generated
mutants_x__node_allocatable_cpu__mutmut['x__node_allocatable_cpu__mutmut_1'] = x__node_allocatable_cpu__mutmut_1 # type: ignore # mutmut generated
mutants_x__node_allocatable_cpu__mutmut['x__node_allocatable_cpu__mutmut_2'] = x__node_allocatable_cpu__mutmut_2 # type: ignore # mutmut generated
mutants_x__node_allocatable_cpu__mutmut['x__node_allocatable_cpu__mutmut_3'] = x__node_allocatable_cpu__mutmut_3 # type: ignore # mutmut generated
mutants_x__node_allocatable_cpu__mutmut['x__node_allocatable_cpu__mutmut_4'] = x__node_allocatable_cpu__mutmut_4 # type: ignore # mutmut generated
mutants_x__node_allocatable_cpu__mutmut['x__node_allocatable_cpu__mutmut_5'] = x__node_allocatable_cpu__mutmut_5 # type: ignore # mutmut generated
mutants_x__node_allocatable_cpu__mutmut['x__node_allocatable_cpu__mutmut_6'] = x__node_allocatable_cpu__mutmut_6 # type: ignore # mutmut generated
mutants_x__node_allocatable_cpu__mutmut['x__node_allocatable_cpu__mutmut_7'] = x__node_allocatable_cpu__mutmut_7 # type: ignore # mutmut generated
mutants_x__node_allocatable_cpu__mutmut['x__node_allocatable_cpu__mutmut_8'] = x__node_allocatable_cpu__mutmut_8 # type: ignore # mutmut generated
mutants_x__node_allocatable_cpu__mutmut['x__node_allocatable_cpu__mutmut_9'] = x__node_allocatable_cpu__mutmut_9 # type: ignore # mutmut generated
mutants_x__node_allocatable_cpu__mutmut['x__node_allocatable_cpu__mutmut_10'] = x__node_allocatable_cpu__mutmut_10 # type: ignore # mutmut generated
mutants_x__node_allocatable_memory_gb__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__node_allocatable_memory_gb__mutmut)
def _node_allocatable_memory_gb(node: object) -> float:
    return _memory_to_bytes(str(_node_allocatable(node).get("memory", "0"))) / _BYTES_PER_GB


def x__node_allocatable_memory_gb__mutmut_orig(node: object) -> float:
    return _memory_to_bytes(str(_node_allocatable(node).get("memory", "0"))) / _BYTES_PER_GB


def x__node_allocatable_memory_gb__mutmut_1(node: object) -> float:
    return _memory_to_bytes(str(_node_allocatable(node).get("memory", "0"))) * _BYTES_PER_GB


def x__node_allocatable_memory_gb__mutmut_2(node: object) -> float:
    return _memory_to_bytes(None) / _BYTES_PER_GB


def x__node_allocatable_memory_gb__mutmut_3(node: object) -> float:
    return _memory_to_bytes(str(None)) / _BYTES_PER_GB


def x__node_allocatable_memory_gb__mutmut_4(node: object) -> float:
    return _memory_to_bytes(str(_node_allocatable(node).get(None, "0"))) / _BYTES_PER_GB


def x__node_allocatable_memory_gb__mutmut_5(node: object) -> float:
    return _memory_to_bytes(str(_node_allocatable(node).get("memory", None))) / _BYTES_PER_GB


def x__node_allocatable_memory_gb__mutmut_6(node: object) -> float:
    return _memory_to_bytes(str(_node_allocatable(node).get("0"))) / _BYTES_PER_GB


def x__node_allocatable_memory_gb__mutmut_7(node: object) -> float:
    return _memory_to_bytes(str(_node_allocatable(node).get("memory", ))) / _BYTES_PER_GB


def x__node_allocatable_memory_gb__mutmut_8(node: object) -> float:
    return _memory_to_bytes(str(_node_allocatable(None).get("memory", "0"))) / _BYTES_PER_GB


def x__node_allocatable_memory_gb__mutmut_9(node: object) -> float:
    return _memory_to_bytes(str(_node_allocatable(node).get("XXmemoryXX", "0"))) / _BYTES_PER_GB


def x__node_allocatable_memory_gb__mutmut_10(node: object) -> float:
    return _memory_to_bytes(str(_node_allocatable(node).get("MEMORY", "0"))) / _BYTES_PER_GB


def x__node_allocatable_memory_gb__mutmut_11(node: object) -> float:
    return _memory_to_bytes(str(_node_allocatable(node).get("memory", "XX0XX"))) / _BYTES_PER_GB

mutants_x__node_allocatable_memory_gb__mutmut['_mutmut_orig'] = x__node_allocatable_memory_gb__mutmut_orig # type: ignore # mutmut generated
mutants_x__node_allocatable_memory_gb__mutmut['x__node_allocatable_memory_gb__mutmut_1'] = x__node_allocatable_memory_gb__mutmut_1 # type: ignore # mutmut generated
mutants_x__node_allocatable_memory_gb__mutmut['x__node_allocatable_memory_gb__mutmut_2'] = x__node_allocatable_memory_gb__mutmut_2 # type: ignore # mutmut generated
mutants_x__node_allocatable_memory_gb__mutmut['x__node_allocatable_memory_gb__mutmut_3'] = x__node_allocatable_memory_gb__mutmut_3 # type: ignore # mutmut generated
mutants_x__node_allocatable_memory_gb__mutmut['x__node_allocatable_memory_gb__mutmut_4'] = x__node_allocatable_memory_gb__mutmut_4 # type: ignore # mutmut generated
mutants_x__node_allocatable_memory_gb__mutmut['x__node_allocatable_memory_gb__mutmut_5'] = x__node_allocatable_memory_gb__mutmut_5 # type: ignore # mutmut generated
mutants_x__node_allocatable_memory_gb__mutmut['x__node_allocatable_memory_gb__mutmut_6'] = x__node_allocatable_memory_gb__mutmut_6 # type: ignore # mutmut generated
mutants_x__node_allocatable_memory_gb__mutmut['x__node_allocatable_memory_gb__mutmut_7'] = x__node_allocatable_memory_gb__mutmut_7 # type: ignore # mutmut generated
mutants_x__node_allocatable_memory_gb__mutmut['x__node_allocatable_memory_gb__mutmut_8'] = x__node_allocatable_memory_gb__mutmut_8 # type: ignore # mutmut generated
mutants_x__node_allocatable_memory_gb__mutmut['x__node_allocatable_memory_gb__mutmut_9'] = x__node_allocatable_memory_gb__mutmut_9 # type: ignore # mutmut generated
mutants_x__node_allocatable_memory_gb__mutmut['x__node_allocatable_memory_gb__mutmut_10'] = x__node_allocatable_memory_gb__mutmut_10 # type: ignore # mutmut generated
mutants_x__node_allocatable_memory_gb__mutmut['x__node_allocatable_memory_gb__mutmut_11'] = x__node_allocatable_memory_gb__mutmut_11 # type: ignore # mutmut generated
mutants_x__cpu_to_cores__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__cpu_to_cores__mutmut)
def _cpu_to_cores(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x__cpu_to_cores__mutmut_orig(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x__cpu_to_cores__mutmut_1(value: str) -> float:
    if value.endswith(None):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x__cpu_to_cores__mutmut_2(value: str) -> float:
    if value.endswith("XXnXX"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x__cpu_to_cores__mutmut_3(value: str) -> float:
    if value.endswith("N"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x__cpu_to_cores__mutmut_4(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") * 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x__cpu_to_cores__mutmut_5(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(None, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x__cpu_to_cores__mutmut_6(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, None) / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x__cpu_to_cores__mutmut_7(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix("n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x__cpu_to_cores__mutmut_8(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, ) / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x__cpu_to_cores__mutmut_9(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "XXnXX") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x__cpu_to_cores__mutmut_10(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "N") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x__cpu_to_cores__mutmut_11(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1000000001
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x__cpu_to_cores__mutmut_12(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith(None):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x__cpu_to_cores__mutmut_13(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("XXuXX"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x__cpu_to_cores__mutmut_14(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("U"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x__cpu_to_cores__mutmut_15(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") * 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x__cpu_to_cores__mutmut_16(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(None, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x__cpu_to_cores__mutmut_17(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, None) / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x__cpu_to_cores__mutmut_18(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix("u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x__cpu_to_cores__mutmut_19(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, ) / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x__cpu_to_cores__mutmut_20(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "XXuXX") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x__cpu_to_cores__mutmut_21(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "U") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x__cpu_to_cores__mutmut_22(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1000001
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x__cpu_to_cores__mutmut_23(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith(None):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x__cpu_to_cores__mutmut_24(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("XXmXX"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x__cpu_to_cores__mutmut_25(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("M"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x__cpu_to_cores__mutmut_26(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") * 1_000
    return _safe_float(value)


def x__cpu_to_cores__mutmut_27(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(None, "m") / 1_000
    return _safe_float(value)


def x__cpu_to_cores__mutmut_28(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, None) / 1_000
    return _safe_float(value)


def x__cpu_to_cores__mutmut_29(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix("m") / 1_000
    return _safe_float(value)


def x__cpu_to_cores__mutmut_30(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, ) / 1_000
    return _safe_float(value)


def x__cpu_to_cores__mutmut_31(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "XXmXX") / 1_000
    return _safe_float(value)


def x__cpu_to_cores__mutmut_32(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "M") / 1_000
    return _safe_float(value)


def x__cpu_to_cores__mutmut_33(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1001
    return _safe_float(value)


def x__cpu_to_cores__mutmut_34(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(None)

mutants_x__cpu_to_cores__mutmut['_mutmut_orig'] = x__cpu_to_cores__mutmut_orig # type: ignore # mutmut generated
mutants_x__cpu_to_cores__mutmut['x__cpu_to_cores__mutmut_1'] = x__cpu_to_cores__mutmut_1 # type: ignore # mutmut generated
mutants_x__cpu_to_cores__mutmut['x__cpu_to_cores__mutmut_2'] = x__cpu_to_cores__mutmut_2 # type: ignore # mutmut generated
mutants_x__cpu_to_cores__mutmut['x__cpu_to_cores__mutmut_3'] = x__cpu_to_cores__mutmut_3 # type: ignore # mutmut generated
mutants_x__cpu_to_cores__mutmut['x__cpu_to_cores__mutmut_4'] = x__cpu_to_cores__mutmut_4 # type: ignore # mutmut generated
mutants_x__cpu_to_cores__mutmut['x__cpu_to_cores__mutmut_5'] = x__cpu_to_cores__mutmut_5 # type: ignore # mutmut generated
mutants_x__cpu_to_cores__mutmut['x__cpu_to_cores__mutmut_6'] = x__cpu_to_cores__mutmut_6 # type: ignore # mutmut generated
mutants_x__cpu_to_cores__mutmut['x__cpu_to_cores__mutmut_7'] = x__cpu_to_cores__mutmut_7 # type: ignore # mutmut generated
mutants_x__cpu_to_cores__mutmut['x__cpu_to_cores__mutmut_8'] = x__cpu_to_cores__mutmut_8 # type: ignore # mutmut generated
mutants_x__cpu_to_cores__mutmut['x__cpu_to_cores__mutmut_9'] = x__cpu_to_cores__mutmut_9 # type: ignore # mutmut generated
mutants_x__cpu_to_cores__mutmut['x__cpu_to_cores__mutmut_10'] = x__cpu_to_cores__mutmut_10 # type: ignore # mutmut generated
mutants_x__cpu_to_cores__mutmut['x__cpu_to_cores__mutmut_11'] = x__cpu_to_cores__mutmut_11 # type: ignore # mutmut generated
mutants_x__cpu_to_cores__mutmut['x__cpu_to_cores__mutmut_12'] = x__cpu_to_cores__mutmut_12 # type: ignore # mutmut generated
mutants_x__cpu_to_cores__mutmut['x__cpu_to_cores__mutmut_13'] = x__cpu_to_cores__mutmut_13 # type: ignore # mutmut generated
mutants_x__cpu_to_cores__mutmut['x__cpu_to_cores__mutmut_14'] = x__cpu_to_cores__mutmut_14 # type: ignore # mutmut generated
mutants_x__cpu_to_cores__mutmut['x__cpu_to_cores__mutmut_15'] = x__cpu_to_cores__mutmut_15 # type: ignore # mutmut generated
mutants_x__cpu_to_cores__mutmut['x__cpu_to_cores__mutmut_16'] = x__cpu_to_cores__mutmut_16 # type: ignore # mutmut generated
mutants_x__cpu_to_cores__mutmut['x__cpu_to_cores__mutmut_17'] = x__cpu_to_cores__mutmut_17 # type: ignore # mutmut generated
mutants_x__cpu_to_cores__mutmut['x__cpu_to_cores__mutmut_18'] = x__cpu_to_cores__mutmut_18 # type: ignore # mutmut generated
mutants_x__cpu_to_cores__mutmut['x__cpu_to_cores__mutmut_19'] = x__cpu_to_cores__mutmut_19 # type: ignore # mutmut generated
mutants_x__cpu_to_cores__mutmut['x__cpu_to_cores__mutmut_20'] = x__cpu_to_cores__mutmut_20 # type: ignore # mutmut generated
mutants_x__cpu_to_cores__mutmut['x__cpu_to_cores__mutmut_21'] = x__cpu_to_cores__mutmut_21 # type: ignore # mutmut generated
mutants_x__cpu_to_cores__mutmut['x__cpu_to_cores__mutmut_22'] = x__cpu_to_cores__mutmut_22 # type: ignore # mutmut generated
mutants_x__cpu_to_cores__mutmut['x__cpu_to_cores__mutmut_23'] = x__cpu_to_cores__mutmut_23 # type: ignore # mutmut generated
mutants_x__cpu_to_cores__mutmut['x__cpu_to_cores__mutmut_24'] = x__cpu_to_cores__mutmut_24 # type: ignore # mutmut generated
mutants_x__cpu_to_cores__mutmut['x__cpu_to_cores__mutmut_25'] = x__cpu_to_cores__mutmut_25 # type: ignore # mutmut generated
mutants_x__cpu_to_cores__mutmut['x__cpu_to_cores__mutmut_26'] = x__cpu_to_cores__mutmut_26 # type: ignore # mutmut generated
mutants_x__cpu_to_cores__mutmut['x__cpu_to_cores__mutmut_27'] = x__cpu_to_cores__mutmut_27 # type: ignore # mutmut generated
mutants_x__cpu_to_cores__mutmut['x__cpu_to_cores__mutmut_28'] = x__cpu_to_cores__mutmut_28 # type: ignore # mutmut generated
mutants_x__cpu_to_cores__mutmut['x__cpu_to_cores__mutmut_29'] = x__cpu_to_cores__mutmut_29 # type: ignore # mutmut generated
mutants_x__cpu_to_cores__mutmut['x__cpu_to_cores__mutmut_30'] = x__cpu_to_cores__mutmut_30 # type: ignore # mutmut generated
mutants_x__cpu_to_cores__mutmut['x__cpu_to_cores__mutmut_31'] = x__cpu_to_cores__mutmut_31 # type: ignore # mutmut generated
mutants_x__cpu_to_cores__mutmut['x__cpu_to_cores__mutmut_32'] = x__cpu_to_cores__mutmut_32 # type: ignore # mutmut generated
mutants_x__cpu_to_cores__mutmut['x__cpu_to_cores__mutmut_33'] = x__cpu_to_cores__mutmut_33 # type: ignore # mutmut generated
mutants_x__cpu_to_cores__mutmut['x__cpu_to_cores__mutmut_34'] = x__cpu_to_cores__mutmut_34 # type: ignore # mutmut generated
mutants_x__memory_to_bytes__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__memory_to_bytes__mutmut)
def _memory_to_bytes(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x__memory_to_bytes__mutmut_orig(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x__memory_to_bytes__mutmut_1(value: str) -> float:
    multipliers = None
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x__memory_to_bytes__mutmut_2(value: str) -> float:
    multipliers = {"XXKiXX": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x__memory_to_bytes__mutmut_3(value: str) -> float:
    multipliers = {"ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x__memory_to_bytes__mutmut_4(value: str) -> float:
    multipliers = {"KI": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x__memory_to_bytes__mutmut_5(value: str) -> float:
    multipliers = {"Ki": 1025.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x__memory_to_bytes__mutmut_6(value: str) -> float:
    multipliers = {"Ki": 1024.0, "XXMiXX": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x__memory_to_bytes__mutmut_7(value: str) -> float:
    multipliers = {"Ki": 1024.0, "mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x__memory_to_bytes__mutmut_8(value: str) -> float:
    multipliers = {"Ki": 1024.0, "MI": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x__memory_to_bytes__mutmut_9(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0 * 2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x__memory_to_bytes__mutmut_10(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1025.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x__memory_to_bytes__mutmut_11(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**3, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x__memory_to_bytes__mutmut_12(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "XXGiXX": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x__memory_to_bytes__mutmut_13(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x__memory_to_bytes__mutmut_14(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "GI": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x__memory_to_bytes__mutmut_15(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0 * 3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x__memory_to_bytes__mutmut_16(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1025.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x__memory_to_bytes__mutmut_17(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**4, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x__memory_to_bytes__mutmut_18(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "XXTiXX": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x__memory_to_bytes__mutmut_19(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x__memory_to_bytes__mutmut_20(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "TI": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x__memory_to_bytes__mutmut_21(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0 * 4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x__memory_to_bytes__mutmut_22(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1025.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x__memory_to_bytes__mutmut_23(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**5}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x__memory_to_bytes__mutmut_24(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(None):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x__memory_to_bytes__mutmut_25(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) / multiplier
    return _safe_float(value)


def x__memory_to_bytes__mutmut_26(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(None, suffix) * multiplier
    return _safe_float(value)


def x__memory_to_bytes__mutmut_27(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, None) * multiplier
    return _safe_float(value)


def x__memory_to_bytes__mutmut_28(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(suffix) * multiplier
    return _safe_float(value)


def x__memory_to_bytes__mutmut_29(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, ) * multiplier
    return _safe_float(value)


def x__memory_to_bytes__mutmut_30(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(None)

mutants_x__memory_to_bytes__mutmut['_mutmut_orig'] = x__memory_to_bytes__mutmut_orig # type: ignore # mutmut generated
mutants_x__memory_to_bytes__mutmut['x__memory_to_bytes__mutmut_1'] = x__memory_to_bytes__mutmut_1 # type: ignore # mutmut generated
mutants_x__memory_to_bytes__mutmut['x__memory_to_bytes__mutmut_2'] = x__memory_to_bytes__mutmut_2 # type: ignore # mutmut generated
mutants_x__memory_to_bytes__mutmut['x__memory_to_bytes__mutmut_3'] = x__memory_to_bytes__mutmut_3 # type: ignore # mutmut generated
mutants_x__memory_to_bytes__mutmut['x__memory_to_bytes__mutmut_4'] = x__memory_to_bytes__mutmut_4 # type: ignore # mutmut generated
mutants_x__memory_to_bytes__mutmut['x__memory_to_bytes__mutmut_5'] = x__memory_to_bytes__mutmut_5 # type: ignore # mutmut generated
mutants_x__memory_to_bytes__mutmut['x__memory_to_bytes__mutmut_6'] = x__memory_to_bytes__mutmut_6 # type: ignore # mutmut generated
mutants_x__memory_to_bytes__mutmut['x__memory_to_bytes__mutmut_7'] = x__memory_to_bytes__mutmut_7 # type: ignore # mutmut generated
mutants_x__memory_to_bytes__mutmut['x__memory_to_bytes__mutmut_8'] = x__memory_to_bytes__mutmut_8 # type: ignore # mutmut generated
mutants_x__memory_to_bytes__mutmut['x__memory_to_bytes__mutmut_9'] = x__memory_to_bytes__mutmut_9 # type: ignore # mutmut generated
mutants_x__memory_to_bytes__mutmut['x__memory_to_bytes__mutmut_10'] = x__memory_to_bytes__mutmut_10 # type: ignore # mutmut generated
mutants_x__memory_to_bytes__mutmut['x__memory_to_bytes__mutmut_11'] = x__memory_to_bytes__mutmut_11 # type: ignore # mutmut generated
mutants_x__memory_to_bytes__mutmut['x__memory_to_bytes__mutmut_12'] = x__memory_to_bytes__mutmut_12 # type: ignore # mutmut generated
mutants_x__memory_to_bytes__mutmut['x__memory_to_bytes__mutmut_13'] = x__memory_to_bytes__mutmut_13 # type: ignore # mutmut generated
mutants_x__memory_to_bytes__mutmut['x__memory_to_bytes__mutmut_14'] = x__memory_to_bytes__mutmut_14 # type: ignore # mutmut generated
mutants_x__memory_to_bytes__mutmut['x__memory_to_bytes__mutmut_15'] = x__memory_to_bytes__mutmut_15 # type: ignore # mutmut generated
mutants_x__memory_to_bytes__mutmut['x__memory_to_bytes__mutmut_16'] = x__memory_to_bytes__mutmut_16 # type: ignore # mutmut generated
mutants_x__memory_to_bytes__mutmut['x__memory_to_bytes__mutmut_17'] = x__memory_to_bytes__mutmut_17 # type: ignore # mutmut generated
mutants_x__memory_to_bytes__mutmut['x__memory_to_bytes__mutmut_18'] = x__memory_to_bytes__mutmut_18 # type: ignore # mutmut generated
mutants_x__memory_to_bytes__mutmut['x__memory_to_bytes__mutmut_19'] = x__memory_to_bytes__mutmut_19 # type: ignore # mutmut generated
mutants_x__memory_to_bytes__mutmut['x__memory_to_bytes__mutmut_20'] = x__memory_to_bytes__mutmut_20 # type: ignore # mutmut generated
mutants_x__memory_to_bytes__mutmut['x__memory_to_bytes__mutmut_21'] = x__memory_to_bytes__mutmut_21 # type: ignore # mutmut generated
mutants_x__memory_to_bytes__mutmut['x__memory_to_bytes__mutmut_22'] = x__memory_to_bytes__mutmut_22 # type: ignore # mutmut generated
mutants_x__memory_to_bytes__mutmut['x__memory_to_bytes__mutmut_23'] = x__memory_to_bytes__mutmut_23 # type: ignore # mutmut generated
mutants_x__memory_to_bytes__mutmut['x__memory_to_bytes__mutmut_24'] = x__memory_to_bytes__mutmut_24 # type: ignore # mutmut generated
mutants_x__memory_to_bytes__mutmut['x__memory_to_bytes__mutmut_25'] = x__memory_to_bytes__mutmut_25 # type: ignore # mutmut generated
mutants_x__memory_to_bytes__mutmut['x__memory_to_bytes__mutmut_26'] = x__memory_to_bytes__mutmut_26 # type: ignore # mutmut generated
mutants_x__memory_to_bytes__mutmut['x__memory_to_bytes__mutmut_27'] = x__memory_to_bytes__mutmut_27 # type: ignore # mutmut generated
mutants_x__memory_to_bytes__mutmut['x__memory_to_bytes__mutmut_28'] = x__memory_to_bytes__mutmut_28 # type: ignore # mutmut generated
mutants_x__memory_to_bytes__mutmut['x__memory_to_bytes__mutmut_29'] = x__memory_to_bytes__mutmut_29 # type: ignore # mutmut generated
mutants_x__memory_to_bytes__mutmut['x__memory_to_bytes__mutmut_30'] = x__memory_to_bytes__mutmut_30 # type: ignore # mutmut generated
mutants_x__float_prefix__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__float_prefix__mutmut)
def _float_prefix(value: str, suffix: str) -> float:
    return _safe_float(value[: -len(suffix)])


def x__float_prefix__mutmut_orig(value: str, suffix: str) -> float:
    return _safe_float(value[: -len(suffix)])


def x__float_prefix__mutmut_1(value: str, suffix: str) -> float:
    return _safe_float(None)


def x__float_prefix__mutmut_2(value: str, suffix: str) -> float:
    return _safe_float(value[: +len(suffix)])

mutants_x__float_prefix__mutmut['_mutmut_orig'] = x__float_prefix__mutmut_orig # type: ignore # mutmut generated
mutants_x__float_prefix__mutmut['x__float_prefix__mutmut_1'] = x__float_prefix__mutmut_1 # type: ignore # mutmut generated
mutants_x__float_prefix__mutmut['x__float_prefix__mutmut_2'] = x__float_prefix__mutmut_2 # type: ignore # mutmut generated
mutants_x__safe_float__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__safe_float__mutmut)
def _safe_float(value: str) -> float:
    try:
        return float(value)
    except ValueError:
        return 0.0


def x__safe_float__mutmut_orig(value: str) -> float:
    try:
        return float(value)
    except ValueError:
        return 0.0


def x__safe_float__mutmut_1(value: str) -> float:
    try:
        return float(None)
    except ValueError:
        return 0.0


def x__safe_float__mutmut_2(value: str) -> float:
    try:
        return float(value)
    except ValueError:
        return 1.0

mutants_x__safe_float__mutmut['_mutmut_orig'] = x__safe_float__mutmut_orig # type: ignore # mutmut generated
mutants_x__safe_float__mutmut['x__safe_float__mutmut_1'] = x__safe_float__mutmut_1 # type: ignore # mutmut generated
mutants_x__safe_float__mutmut['x__safe_float__mutmut_2'] = x__safe_float__mutmut_2 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__translate_error__mutmut)
def _translate_error(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list cluster nodes")
    return ClusterUnreachableError(f"Cannot list cluster nodes: {exc}")


def x__translate_error__mutmut_orig(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list cluster nodes")
    return ClusterUnreachableError(f"Cannot list cluster nodes: {exc}")


def x__translate_error__mutmut_1(exc: Exception) -> Exception:
    status = None
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list cluster nodes")
    return ClusterUnreachableError(f"Cannot list cluster nodes: {exc}")


def x__translate_error__mutmut_2(exc: Exception) -> Exception:
    status = getattr(None, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list cluster nodes")
    return ClusterUnreachableError(f"Cannot list cluster nodes: {exc}")


def x__translate_error__mutmut_3(exc: Exception) -> Exception:
    status = getattr(exc, None, None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list cluster nodes")
    return ClusterUnreachableError(f"Cannot list cluster nodes: {exc}")


def x__translate_error__mutmut_4(exc: Exception) -> Exception:
    status = getattr("status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list cluster nodes")
    return ClusterUnreachableError(f"Cannot list cluster nodes: {exc}")


def x__translate_error__mutmut_5(exc: Exception) -> Exception:
    status = getattr(exc, None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list cluster nodes")
    return ClusterUnreachableError(f"Cannot list cluster nodes: {exc}")


def x__translate_error__mutmut_6(exc: Exception) -> Exception:
    status = getattr(exc, "status", )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list cluster nodes")
    return ClusterUnreachableError(f"Cannot list cluster nodes: {exc}")


def x__translate_error__mutmut_7(exc: Exception) -> Exception:
    status = getattr(exc, "XXstatusXX", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list cluster nodes")
    return ClusterUnreachableError(f"Cannot list cluster nodes: {exc}")


def x__translate_error__mutmut_8(exc: Exception) -> Exception:
    status = getattr(exc, "STATUS", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list cluster nodes")
    return ClusterUnreachableError(f"Cannot list cluster nodes: {exc}")


def x__translate_error__mutmut_9(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status != _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list cluster nodes")
    return ClusterUnreachableError(f"Cannot list cluster nodes: {exc}")


def x__translate_error__mutmut_10(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(None)
    return ClusterUnreachableError(f"Cannot list cluster nodes: {exc}")


def x__translate_error__mutmut_11(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("XXRBAC denied access to list cluster nodesXX")
    return ClusterUnreachableError(f"Cannot list cluster nodes: {exc}")


def x__translate_error__mutmut_12(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("rbac denied access to list cluster nodes")
    return ClusterUnreachableError(f"Cannot list cluster nodes: {exc}")


def x__translate_error__mutmut_13(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC DENIED ACCESS TO LIST CLUSTER NODES")
    return ClusterUnreachableError(f"Cannot list cluster nodes: {exc}")


def x__translate_error__mutmut_14(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list cluster nodes")
    return ClusterUnreachableError(None)

mutants_x__translate_error__mutmut['_mutmut_orig'] = x__translate_error__mutmut_orig # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_1'] = x__translate_error__mutmut_1 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_2'] = x__translate_error__mutmut_2 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_3'] = x__translate_error__mutmut_3 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_4'] = x__translate_error__mutmut_4 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_5'] = x__translate_error__mutmut_5 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_6'] = x__translate_error__mutmut_6 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_7'] = x__translate_error__mutmut_7 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_8'] = x__translate_error__mutmut_8 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_9'] = x__translate_error__mutmut_9 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_10'] = x__translate_error__mutmut_10 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_11'] = x__translate_error__mutmut_11 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_12'] = x__translate_error__mutmut_12 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_13'] = x__translate_error__mutmut_13 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_14'] = x__translate_error__mutmut_14 # type: ignore # mutmut generated
