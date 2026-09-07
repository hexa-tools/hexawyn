from __future__ import annotations

from hexawyn.application.ports.driven.hot_node_analysis_port import (
    HotNodeAnalysisPort,
    NodeInfoRaw,
    PodUsageRaw,
)
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError

_K8S_FORBIDDEN = 403
_BYTES_PER_GB = 1024.0**3
_METRICS_GROUP = "metrics.k8s.io"
_METRICS_VERSION = "v1beta1"
_METRICS_PLURAL = "pods"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut: MutantDict = {}  # type: ignore


class KubernetesNodeAnalysisAdapter(HotNodeAnalysisPort):
    """Secondary adapter — node allocatable/cordon status and cluster-wide
    pod usage joined to node assignment + DaemonSet ownership. Per-node
    utilization history comes from the existing MetricsQueryPort (ECA-31),
    not this adapter."""

    @_mutmut_mutated(mutants_xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut)
    def list_nodes(self) -> list[NodeInfoRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [
            NodeInfoRaw(
                name=node.metadata.name,
                allocatable_cpu_cores=_node_allocatable_cpu(node),
                allocatable_memory_gb=_node_allocatable_memory_gb(node),
                cordoned=bool(getattr(node.spec, "unschedulable", False)),
            )
            for node in node_list.items
        ]

    def xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_orig(self) -> list[NodeInfoRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [
            NodeInfoRaw(
                name=node.metadata.name,
                allocatable_cpu_cores=_node_allocatable_cpu(node),
                allocatable_memory_gb=_node_allocatable_memory_gb(node),
                cordoned=bool(getattr(node.spec, "unschedulable", False)),
            )
            for node in node_list.items
        ]

    def xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_1(self) -> list[NodeInfoRaw]:
        from kubernetes import client as k8s

        core_api = None
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [
            NodeInfoRaw(
                name=node.metadata.name,
                allocatable_cpu_cores=_node_allocatable_cpu(node),
                allocatable_memory_gb=_node_allocatable_memory_gb(node),
                cordoned=bool(getattr(node.spec, "unschedulable", False)),
            )
            for node in node_list.items
        ]

    def xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_2(self) -> list[NodeInfoRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = None
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [
            NodeInfoRaw(
                name=node.metadata.name,
                allocatable_cpu_cores=_node_allocatable_cpu(node),
                allocatable_memory_gb=_node_allocatable_memory_gb(node),
                cordoned=bool(getattr(node.spec, "unschedulable", False)),
            )
            for node in node_list.items
        ]

    def xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_3(self) -> list[NodeInfoRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(None) from exc

        return [
            NodeInfoRaw(
                name=node.metadata.name,
                allocatable_cpu_cores=_node_allocatable_cpu(node),
                allocatable_memory_gb=_node_allocatable_memory_gb(node),
                cordoned=bool(getattr(node.spec, "unschedulable", False)),
            )
            for node in node_list.items
        ]

    def xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_4(self) -> list[NodeInfoRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [
            NodeInfoRaw(
                name=None,
                allocatable_cpu_cores=_node_allocatable_cpu(node),
                allocatable_memory_gb=_node_allocatable_memory_gb(node),
                cordoned=bool(getattr(node.spec, "unschedulable", False)),
            )
            for node in node_list.items
        ]

    def xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_5(self) -> list[NodeInfoRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [
            NodeInfoRaw(
                name=node.metadata.name,
                allocatable_cpu_cores=None,
                allocatable_memory_gb=_node_allocatable_memory_gb(node),
                cordoned=bool(getattr(node.spec, "unschedulable", False)),
            )
            for node in node_list.items
        ]

    def xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_6(self) -> list[NodeInfoRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [
            NodeInfoRaw(
                name=node.metadata.name,
                allocatable_cpu_cores=_node_allocatable_cpu(node),
                allocatable_memory_gb=None,
                cordoned=bool(getattr(node.spec, "unschedulable", False)),
            )
            for node in node_list.items
        ]

    def xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_7(self) -> list[NodeInfoRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [
            NodeInfoRaw(
                name=node.metadata.name,
                allocatable_cpu_cores=_node_allocatable_cpu(node),
                allocatable_memory_gb=_node_allocatable_memory_gb(node),
                cordoned=None,
            )
            for node in node_list.items
        ]

    def xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_8(self) -> list[NodeInfoRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [
            NodeInfoRaw(
                allocatable_cpu_cores=_node_allocatable_cpu(node),
                allocatable_memory_gb=_node_allocatable_memory_gb(node),
                cordoned=bool(getattr(node.spec, "unschedulable", False)),
            )
            for node in node_list.items
        ]

    def xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_9(self) -> list[NodeInfoRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [
            NodeInfoRaw(
                name=node.metadata.name,
                allocatable_memory_gb=_node_allocatable_memory_gb(node),
                cordoned=bool(getattr(node.spec, "unschedulable", False)),
            )
            for node in node_list.items
        ]

    def xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_10(self) -> list[NodeInfoRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [
            NodeInfoRaw(
                name=node.metadata.name,
                allocatable_cpu_cores=_node_allocatable_cpu(node),
                cordoned=bool(getattr(node.spec, "unschedulable", False)),
            )
            for node in node_list.items
        ]

    def xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_11(self) -> list[NodeInfoRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [
            NodeInfoRaw(
                name=node.metadata.name,
                allocatable_cpu_cores=_node_allocatable_cpu(node),
                allocatable_memory_gb=_node_allocatable_memory_gb(node),
                )
            for node in node_list.items
        ]

    def xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_12(self) -> list[NodeInfoRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [
            NodeInfoRaw(
                name=node.metadata.name,
                allocatable_cpu_cores=_node_allocatable_cpu(None),
                allocatable_memory_gb=_node_allocatable_memory_gb(node),
                cordoned=bool(getattr(node.spec, "unschedulable", False)),
            )
            for node in node_list.items
        ]

    def xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_13(self) -> list[NodeInfoRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [
            NodeInfoRaw(
                name=node.metadata.name,
                allocatable_cpu_cores=_node_allocatable_cpu(node),
                allocatable_memory_gb=_node_allocatable_memory_gb(None),
                cordoned=bool(getattr(node.spec, "unschedulable", False)),
            )
            for node in node_list.items
        ]

    def xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_14(self) -> list[NodeInfoRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [
            NodeInfoRaw(
                name=node.metadata.name,
                allocatable_cpu_cores=_node_allocatable_cpu(node),
                allocatable_memory_gb=_node_allocatable_memory_gb(node),
                cordoned=bool(None),
            )
            for node in node_list.items
        ]

    def xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_15(self) -> list[NodeInfoRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [
            NodeInfoRaw(
                name=node.metadata.name,
                allocatable_cpu_cores=_node_allocatable_cpu(node),
                allocatable_memory_gb=_node_allocatable_memory_gb(node),
                cordoned=bool(getattr(None, "unschedulable", False)),
            )
            for node in node_list.items
        ]

    def xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_16(self) -> list[NodeInfoRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [
            NodeInfoRaw(
                name=node.metadata.name,
                allocatable_cpu_cores=_node_allocatable_cpu(node),
                allocatable_memory_gb=_node_allocatable_memory_gb(node),
                cordoned=bool(getattr(node.spec, None, False)),
            )
            for node in node_list.items
        ]

    def xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_17(self) -> list[NodeInfoRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [
            NodeInfoRaw(
                name=node.metadata.name,
                allocatable_cpu_cores=_node_allocatable_cpu(node),
                allocatable_memory_gb=_node_allocatable_memory_gb(node),
                cordoned=bool(getattr(node.spec, "unschedulable", None)),
            )
            for node in node_list.items
        ]

    def xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_18(self) -> list[NodeInfoRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [
            NodeInfoRaw(
                name=node.metadata.name,
                allocatable_cpu_cores=_node_allocatable_cpu(node),
                allocatable_memory_gb=_node_allocatable_memory_gb(node),
                cordoned=bool(getattr("unschedulable", False)),
            )
            for node in node_list.items
        ]

    def xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_19(self) -> list[NodeInfoRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [
            NodeInfoRaw(
                name=node.metadata.name,
                allocatable_cpu_cores=_node_allocatable_cpu(node),
                allocatable_memory_gb=_node_allocatable_memory_gb(node),
                cordoned=bool(getattr(node.spec, False)),
            )
            for node in node_list.items
        ]

    def xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_20(self) -> list[NodeInfoRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [
            NodeInfoRaw(
                name=node.metadata.name,
                allocatable_cpu_cores=_node_allocatable_cpu(node),
                allocatable_memory_gb=_node_allocatable_memory_gb(node),
                cordoned=bool(getattr(node.spec, "unschedulable", )),
            )
            for node in node_list.items
        ]

    def xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_21(self) -> list[NodeInfoRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [
            NodeInfoRaw(
                name=node.metadata.name,
                allocatable_cpu_cores=_node_allocatable_cpu(node),
                allocatable_memory_gb=_node_allocatable_memory_gb(node),
                cordoned=bool(getattr(node.spec, "XXunschedulableXX", False)),
            )
            for node in node_list.items
        ]

    def xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_22(self) -> list[NodeInfoRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [
            NodeInfoRaw(
                name=node.metadata.name,
                allocatable_cpu_cores=_node_allocatable_cpu(node),
                allocatable_memory_gb=_node_allocatable_memory_gb(node),
                cordoned=bool(getattr(node.spec, "UNSCHEDULABLE", False)),
            )
            for node in node_list.items
        ]

    def xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_23(self) -> list[NodeInfoRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            node_list = core_api.list_node()
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [
            NodeInfoRaw(
                name=node.metadata.name,
                allocatable_cpu_cores=_node_allocatable_cpu(node),
                allocatable_memory_gb=_node_allocatable_memory_gb(node),
                cordoned=bool(getattr(node.spec, "unschedulable", True)),
            )
            for node in node_list.items
        ]

    @_mutmut_mutated(mutants_xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut)
    def list_pod_usage(self) -> list[PodUsageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod_list = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        usage_by_key = _fetch_pod_metrics(k8s)

        results: list[PodUsageRaw] = []
        for pod in pod_list.items:
            node_name = getattr(pod.spec, "node_name", None)
            if not node_name:
                continue
            cpu, memory = usage_by_key.get((pod.metadata.namespace, pod.metadata.name), (0.0, 0.0))
            results.append(
                PodUsageRaw(
                    pod_name=pod.metadata.name,
                    namespace=pod.metadata.namespace,
                    node_name=node_name,
                    cpu_usage_cores=cpu,
                    memory_usage_gb=memory,
                    is_daemonset=_is_daemonset(pod),
                )
            )
        return results

    def xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_orig(self) -> list[PodUsageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod_list = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        usage_by_key = _fetch_pod_metrics(k8s)

        results: list[PodUsageRaw] = []
        for pod in pod_list.items:
            node_name = getattr(pod.spec, "node_name", None)
            if not node_name:
                continue
            cpu, memory = usage_by_key.get((pod.metadata.namespace, pod.metadata.name), (0.0, 0.0))
            results.append(
                PodUsageRaw(
                    pod_name=pod.metadata.name,
                    namespace=pod.metadata.namespace,
                    node_name=node_name,
                    cpu_usage_cores=cpu,
                    memory_usage_gb=memory,
                    is_daemonset=_is_daemonset(pod),
                )
            )
        return results

    def xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_1(self) -> list[PodUsageRaw]:
        from kubernetes import client as k8s

        core_api = None
        try:
            pod_list = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        usage_by_key = _fetch_pod_metrics(k8s)

        results: list[PodUsageRaw] = []
        for pod in pod_list.items:
            node_name = getattr(pod.spec, "node_name", None)
            if not node_name:
                continue
            cpu, memory = usage_by_key.get((pod.metadata.namespace, pod.metadata.name), (0.0, 0.0))
            results.append(
                PodUsageRaw(
                    pod_name=pod.metadata.name,
                    namespace=pod.metadata.namespace,
                    node_name=node_name,
                    cpu_usage_cores=cpu,
                    memory_usage_gb=memory,
                    is_daemonset=_is_daemonset(pod),
                )
            )
        return results

    def xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_2(self) -> list[PodUsageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod_list = None
        except Exception as exc:
            raise _translate_error(exc) from exc

        usage_by_key = _fetch_pod_metrics(k8s)

        results: list[PodUsageRaw] = []
        for pod in pod_list.items:
            node_name = getattr(pod.spec, "node_name", None)
            if not node_name:
                continue
            cpu, memory = usage_by_key.get((pod.metadata.namespace, pod.metadata.name), (0.0, 0.0))
            results.append(
                PodUsageRaw(
                    pod_name=pod.metadata.name,
                    namespace=pod.metadata.namespace,
                    node_name=node_name,
                    cpu_usage_cores=cpu,
                    memory_usage_gb=memory,
                    is_daemonset=_is_daemonset(pod),
                )
            )
        return results

    def xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_3(self) -> list[PodUsageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod_list = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(None) from exc

        usage_by_key = _fetch_pod_metrics(k8s)

        results: list[PodUsageRaw] = []
        for pod in pod_list.items:
            node_name = getattr(pod.spec, "node_name", None)
            if not node_name:
                continue
            cpu, memory = usage_by_key.get((pod.metadata.namespace, pod.metadata.name), (0.0, 0.0))
            results.append(
                PodUsageRaw(
                    pod_name=pod.metadata.name,
                    namespace=pod.metadata.namespace,
                    node_name=node_name,
                    cpu_usage_cores=cpu,
                    memory_usage_gb=memory,
                    is_daemonset=_is_daemonset(pod),
                )
            )
        return results

    def xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_4(self) -> list[PodUsageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod_list = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        usage_by_key = None

        results: list[PodUsageRaw] = []
        for pod in pod_list.items:
            node_name = getattr(pod.spec, "node_name", None)
            if not node_name:
                continue
            cpu, memory = usage_by_key.get((pod.metadata.namespace, pod.metadata.name), (0.0, 0.0))
            results.append(
                PodUsageRaw(
                    pod_name=pod.metadata.name,
                    namespace=pod.metadata.namespace,
                    node_name=node_name,
                    cpu_usage_cores=cpu,
                    memory_usage_gb=memory,
                    is_daemonset=_is_daemonset(pod),
                )
            )
        return results

    def xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_5(self) -> list[PodUsageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod_list = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        usage_by_key = _fetch_pod_metrics(None)

        results: list[PodUsageRaw] = []
        for pod in pod_list.items:
            node_name = getattr(pod.spec, "node_name", None)
            if not node_name:
                continue
            cpu, memory = usage_by_key.get((pod.metadata.namespace, pod.metadata.name), (0.0, 0.0))
            results.append(
                PodUsageRaw(
                    pod_name=pod.metadata.name,
                    namespace=pod.metadata.namespace,
                    node_name=node_name,
                    cpu_usage_cores=cpu,
                    memory_usage_gb=memory,
                    is_daemonset=_is_daemonset(pod),
                )
            )
        return results

    def xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_6(self) -> list[PodUsageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod_list = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        usage_by_key = _fetch_pod_metrics(k8s)

        results: list[PodUsageRaw] = None
        for pod in pod_list.items:
            node_name = getattr(pod.spec, "node_name", None)
            if not node_name:
                continue
            cpu, memory = usage_by_key.get((pod.metadata.namespace, pod.metadata.name), (0.0, 0.0))
            results.append(
                PodUsageRaw(
                    pod_name=pod.metadata.name,
                    namespace=pod.metadata.namespace,
                    node_name=node_name,
                    cpu_usage_cores=cpu,
                    memory_usage_gb=memory,
                    is_daemonset=_is_daemonset(pod),
                )
            )
        return results

    def xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_7(self) -> list[PodUsageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod_list = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        usage_by_key = _fetch_pod_metrics(k8s)

        results: list[PodUsageRaw] = []
        for pod in pod_list.items:
            node_name = None
            if not node_name:
                continue
            cpu, memory = usage_by_key.get((pod.metadata.namespace, pod.metadata.name), (0.0, 0.0))
            results.append(
                PodUsageRaw(
                    pod_name=pod.metadata.name,
                    namespace=pod.metadata.namespace,
                    node_name=node_name,
                    cpu_usage_cores=cpu,
                    memory_usage_gb=memory,
                    is_daemonset=_is_daemonset(pod),
                )
            )
        return results

    def xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_8(self) -> list[PodUsageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod_list = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        usage_by_key = _fetch_pod_metrics(k8s)

        results: list[PodUsageRaw] = []
        for pod in pod_list.items:
            node_name = getattr(None, "node_name", None)
            if not node_name:
                continue
            cpu, memory = usage_by_key.get((pod.metadata.namespace, pod.metadata.name), (0.0, 0.0))
            results.append(
                PodUsageRaw(
                    pod_name=pod.metadata.name,
                    namespace=pod.metadata.namespace,
                    node_name=node_name,
                    cpu_usage_cores=cpu,
                    memory_usage_gb=memory,
                    is_daemonset=_is_daemonset(pod),
                )
            )
        return results

    def xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_9(self) -> list[PodUsageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod_list = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        usage_by_key = _fetch_pod_metrics(k8s)

        results: list[PodUsageRaw] = []
        for pod in pod_list.items:
            node_name = getattr(pod.spec, None, None)
            if not node_name:
                continue
            cpu, memory = usage_by_key.get((pod.metadata.namespace, pod.metadata.name), (0.0, 0.0))
            results.append(
                PodUsageRaw(
                    pod_name=pod.metadata.name,
                    namespace=pod.metadata.namespace,
                    node_name=node_name,
                    cpu_usage_cores=cpu,
                    memory_usage_gb=memory,
                    is_daemonset=_is_daemonset(pod),
                )
            )
        return results

    def xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_10(self) -> list[PodUsageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod_list = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        usage_by_key = _fetch_pod_metrics(k8s)

        results: list[PodUsageRaw] = []
        for pod in pod_list.items:
            node_name = getattr("node_name", None)
            if not node_name:
                continue
            cpu, memory = usage_by_key.get((pod.metadata.namespace, pod.metadata.name), (0.0, 0.0))
            results.append(
                PodUsageRaw(
                    pod_name=pod.metadata.name,
                    namespace=pod.metadata.namespace,
                    node_name=node_name,
                    cpu_usage_cores=cpu,
                    memory_usage_gb=memory,
                    is_daemonset=_is_daemonset(pod),
                )
            )
        return results

    def xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_11(self) -> list[PodUsageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod_list = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        usage_by_key = _fetch_pod_metrics(k8s)

        results: list[PodUsageRaw] = []
        for pod in pod_list.items:
            node_name = getattr(pod.spec, None)
            if not node_name:
                continue
            cpu, memory = usage_by_key.get((pod.metadata.namespace, pod.metadata.name), (0.0, 0.0))
            results.append(
                PodUsageRaw(
                    pod_name=pod.metadata.name,
                    namespace=pod.metadata.namespace,
                    node_name=node_name,
                    cpu_usage_cores=cpu,
                    memory_usage_gb=memory,
                    is_daemonset=_is_daemonset(pod),
                )
            )
        return results

    def xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_12(self) -> list[PodUsageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod_list = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        usage_by_key = _fetch_pod_metrics(k8s)

        results: list[PodUsageRaw] = []
        for pod in pod_list.items:
            node_name = getattr(pod.spec, "node_name", )
            if not node_name:
                continue
            cpu, memory = usage_by_key.get((pod.metadata.namespace, pod.metadata.name), (0.0, 0.0))
            results.append(
                PodUsageRaw(
                    pod_name=pod.metadata.name,
                    namespace=pod.metadata.namespace,
                    node_name=node_name,
                    cpu_usage_cores=cpu,
                    memory_usage_gb=memory,
                    is_daemonset=_is_daemonset(pod),
                )
            )
        return results

    def xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_13(self) -> list[PodUsageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod_list = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        usage_by_key = _fetch_pod_metrics(k8s)

        results: list[PodUsageRaw] = []
        for pod in pod_list.items:
            node_name = getattr(pod.spec, "XXnode_nameXX", None)
            if not node_name:
                continue
            cpu, memory = usage_by_key.get((pod.metadata.namespace, pod.metadata.name), (0.0, 0.0))
            results.append(
                PodUsageRaw(
                    pod_name=pod.metadata.name,
                    namespace=pod.metadata.namespace,
                    node_name=node_name,
                    cpu_usage_cores=cpu,
                    memory_usage_gb=memory,
                    is_daemonset=_is_daemonset(pod),
                )
            )
        return results

    def xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_14(self) -> list[PodUsageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod_list = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        usage_by_key = _fetch_pod_metrics(k8s)

        results: list[PodUsageRaw] = []
        for pod in pod_list.items:
            node_name = getattr(pod.spec, "NODE_NAME", None)
            if not node_name:
                continue
            cpu, memory = usage_by_key.get((pod.metadata.namespace, pod.metadata.name), (0.0, 0.0))
            results.append(
                PodUsageRaw(
                    pod_name=pod.metadata.name,
                    namespace=pod.metadata.namespace,
                    node_name=node_name,
                    cpu_usage_cores=cpu,
                    memory_usage_gb=memory,
                    is_daemonset=_is_daemonset(pod),
                )
            )
        return results

    def xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_15(self) -> list[PodUsageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod_list = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        usage_by_key = _fetch_pod_metrics(k8s)

        results: list[PodUsageRaw] = []
        for pod in pod_list.items:
            node_name = getattr(pod.spec, "node_name", None)
            if node_name:
                continue
            cpu, memory = usage_by_key.get((pod.metadata.namespace, pod.metadata.name), (0.0, 0.0))
            results.append(
                PodUsageRaw(
                    pod_name=pod.metadata.name,
                    namespace=pod.metadata.namespace,
                    node_name=node_name,
                    cpu_usage_cores=cpu,
                    memory_usage_gb=memory,
                    is_daemonset=_is_daemonset(pod),
                )
            )
        return results

    def xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_16(self) -> list[PodUsageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod_list = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        usage_by_key = _fetch_pod_metrics(k8s)

        results: list[PodUsageRaw] = []
        for pod in pod_list.items:
            node_name = getattr(pod.spec, "node_name", None)
            if not node_name:
                break
            cpu, memory = usage_by_key.get((pod.metadata.namespace, pod.metadata.name), (0.0, 0.0))
            results.append(
                PodUsageRaw(
                    pod_name=pod.metadata.name,
                    namespace=pod.metadata.namespace,
                    node_name=node_name,
                    cpu_usage_cores=cpu,
                    memory_usage_gb=memory,
                    is_daemonset=_is_daemonset(pod),
                )
            )
        return results

    def xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_17(self) -> list[PodUsageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod_list = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        usage_by_key = _fetch_pod_metrics(k8s)

        results: list[PodUsageRaw] = []
        for pod in pod_list.items:
            node_name = getattr(pod.spec, "node_name", None)
            if not node_name:
                continue
            cpu, memory = None
            results.append(
                PodUsageRaw(
                    pod_name=pod.metadata.name,
                    namespace=pod.metadata.namespace,
                    node_name=node_name,
                    cpu_usage_cores=cpu,
                    memory_usage_gb=memory,
                    is_daemonset=_is_daemonset(pod),
                )
            )
        return results

    def xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_18(self) -> list[PodUsageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod_list = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        usage_by_key = _fetch_pod_metrics(k8s)

        results: list[PodUsageRaw] = []
        for pod in pod_list.items:
            node_name = getattr(pod.spec, "node_name", None)
            if not node_name:
                continue
            cpu, memory = usage_by_key.get(None, (0.0, 0.0))
            results.append(
                PodUsageRaw(
                    pod_name=pod.metadata.name,
                    namespace=pod.metadata.namespace,
                    node_name=node_name,
                    cpu_usage_cores=cpu,
                    memory_usage_gb=memory,
                    is_daemonset=_is_daemonset(pod),
                )
            )
        return results

    def xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_19(self) -> list[PodUsageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod_list = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        usage_by_key = _fetch_pod_metrics(k8s)

        results: list[PodUsageRaw] = []
        for pod in pod_list.items:
            node_name = getattr(pod.spec, "node_name", None)
            if not node_name:
                continue
            cpu, memory = usage_by_key.get((pod.metadata.namespace, pod.metadata.name), None)
            results.append(
                PodUsageRaw(
                    pod_name=pod.metadata.name,
                    namespace=pod.metadata.namespace,
                    node_name=node_name,
                    cpu_usage_cores=cpu,
                    memory_usage_gb=memory,
                    is_daemonset=_is_daemonset(pod),
                )
            )
        return results

    def xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_20(self) -> list[PodUsageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod_list = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        usage_by_key = _fetch_pod_metrics(k8s)

        results: list[PodUsageRaw] = []
        for pod in pod_list.items:
            node_name = getattr(pod.spec, "node_name", None)
            if not node_name:
                continue
            cpu, memory = usage_by_key.get((0.0, 0.0))
            results.append(
                PodUsageRaw(
                    pod_name=pod.metadata.name,
                    namespace=pod.metadata.namespace,
                    node_name=node_name,
                    cpu_usage_cores=cpu,
                    memory_usage_gb=memory,
                    is_daemonset=_is_daemonset(pod),
                )
            )
        return results

    def xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_21(self) -> list[PodUsageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod_list = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        usage_by_key = _fetch_pod_metrics(k8s)

        results: list[PodUsageRaw] = []
        for pod in pod_list.items:
            node_name = getattr(pod.spec, "node_name", None)
            if not node_name:
                continue
            cpu, memory = usage_by_key.get((pod.metadata.namespace, pod.metadata.name), )
            results.append(
                PodUsageRaw(
                    pod_name=pod.metadata.name,
                    namespace=pod.metadata.namespace,
                    node_name=node_name,
                    cpu_usage_cores=cpu,
                    memory_usage_gb=memory,
                    is_daemonset=_is_daemonset(pod),
                )
            )
        return results

    def xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_22(self) -> list[PodUsageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod_list = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        usage_by_key = _fetch_pod_metrics(k8s)

        results: list[PodUsageRaw] = []
        for pod in pod_list.items:
            node_name = getattr(pod.spec, "node_name", None)
            if not node_name:
                continue
            cpu, memory = usage_by_key.get((pod.metadata.namespace, pod.metadata.name), (1.0, 0.0))
            results.append(
                PodUsageRaw(
                    pod_name=pod.metadata.name,
                    namespace=pod.metadata.namespace,
                    node_name=node_name,
                    cpu_usage_cores=cpu,
                    memory_usage_gb=memory,
                    is_daemonset=_is_daemonset(pod),
                )
            )
        return results

    def xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_23(self) -> list[PodUsageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod_list = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        usage_by_key = _fetch_pod_metrics(k8s)

        results: list[PodUsageRaw] = []
        for pod in pod_list.items:
            node_name = getattr(pod.spec, "node_name", None)
            if not node_name:
                continue
            cpu, memory = usage_by_key.get((pod.metadata.namespace, pod.metadata.name), (0.0, 1.0))
            results.append(
                PodUsageRaw(
                    pod_name=pod.metadata.name,
                    namespace=pod.metadata.namespace,
                    node_name=node_name,
                    cpu_usage_cores=cpu,
                    memory_usage_gb=memory,
                    is_daemonset=_is_daemonset(pod),
                )
            )
        return results

    def xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_24(self) -> list[PodUsageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod_list = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        usage_by_key = _fetch_pod_metrics(k8s)

        results: list[PodUsageRaw] = []
        for pod in pod_list.items:
            node_name = getattr(pod.spec, "node_name", None)
            if not node_name:
                continue
            cpu, memory = usage_by_key.get((pod.metadata.namespace, pod.metadata.name), (0.0, 0.0))
            results.append(
                None
            )
        return results

    def xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_25(self) -> list[PodUsageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod_list = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        usage_by_key = _fetch_pod_metrics(k8s)

        results: list[PodUsageRaw] = []
        for pod in pod_list.items:
            node_name = getattr(pod.spec, "node_name", None)
            if not node_name:
                continue
            cpu, memory = usage_by_key.get((pod.metadata.namespace, pod.metadata.name), (0.0, 0.0))
            results.append(
                PodUsageRaw(
                    pod_name=None,
                    namespace=pod.metadata.namespace,
                    node_name=node_name,
                    cpu_usage_cores=cpu,
                    memory_usage_gb=memory,
                    is_daemonset=_is_daemonset(pod),
                )
            )
        return results

    def xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_26(self) -> list[PodUsageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod_list = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        usage_by_key = _fetch_pod_metrics(k8s)

        results: list[PodUsageRaw] = []
        for pod in pod_list.items:
            node_name = getattr(pod.spec, "node_name", None)
            if not node_name:
                continue
            cpu, memory = usage_by_key.get((pod.metadata.namespace, pod.metadata.name), (0.0, 0.0))
            results.append(
                PodUsageRaw(
                    pod_name=pod.metadata.name,
                    namespace=None,
                    node_name=node_name,
                    cpu_usage_cores=cpu,
                    memory_usage_gb=memory,
                    is_daemonset=_is_daemonset(pod),
                )
            )
        return results

    def xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_27(self) -> list[PodUsageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod_list = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        usage_by_key = _fetch_pod_metrics(k8s)

        results: list[PodUsageRaw] = []
        for pod in pod_list.items:
            node_name = getattr(pod.spec, "node_name", None)
            if not node_name:
                continue
            cpu, memory = usage_by_key.get((pod.metadata.namespace, pod.metadata.name), (0.0, 0.0))
            results.append(
                PodUsageRaw(
                    pod_name=pod.metadata.name,
                    namespace=pod.metadata.namespace,
                    node_name=None,
                    cpu_usage_cores=cpu,
                    memory_usage_gb=memory,
                    is_daemonset=_is_daemonset(pod),
                )
            )
        return results

    def xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_28(self) -> list[PodUsageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod_list = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        usage_by_key = _fetch_pod_metrics(k8s)

        results: list[PodUsageRaw] = []
        for pod in pod_list.items:
            node_name = getattr(pod.spec, "node_name", None)
            if not node_name:
                continue
            cpu, memory = usage_by_key.get((pod.metadata.namespace, pod.metadata.name), (0.0, 0.0))
            results.append(
                PodUsageRaw(
                    pod_name=pod.metadata.name,
                    namespace=pod.metadata.namespace,
                    node_name=node_name,
                    cpu_usage_cores=None,
                    memory_usage_gb=memory,
                    is_daemonset=_is_daemonset(pod),
                )
            )
        return results

    def xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_29(self) -> list[PodUsageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod_list = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        usage_by_key = _fetch_pod_metrics(k8s)

        results: list[PodUsageRaw] = []
        for pod in pod_list.items:
            node_name = getattr(pod.spec, "node_name", None)
            if not node_name:
                continue
            cpu, memory = usage_by_key.get((pod.metadata.namespace, pod.metadata.name), (0.0, 0.0))
            results.append(
                PodUsageRaw(
                    pod_name=pod.metadata.name,
                    namespace=pod.metadata.namespace,
                    node_name=node_name,
                    cpu_usage_cores=cpu,
                    memory_usage_gb=None,
                    is_daemonset=_is_daemonset(pod),
                )
            )
        return results

    def xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_30(self) -> list[PodUsageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod_list = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        usage_by_key = _fetch_pod_metrics(k8s)

        results: list[PodUsageRaw] = []
        for pod in pod_list.items:
            node_name = getattr(pod.spec, "node_name", None)
            if not node_name:
                continue
            cpu, memory = usage_by_key.get((pod.metadata.namespace, pod.metadata.name), (0.0, 0.0))
            results.append(
                PodUsageRaw(
                    pod_name=pod.metadata.name,
                    namespace=pod.metadata.namespace,
                    node_name=node_name,
                    cpu_usage_cores=cpu,
                    memory_usage_gb=memory,
                    is_daemonset=None,
                )
            )
        return results

    def xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_31(self) -> list[PodUsageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod_list = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        usage_by_key = _fetch_pod_metrics(k8s)

        results: list[PodUsageRaw] = []
        for pod in pod_list.items:
            node_name = getattr(pod.spec, "node_name", None)
            if not node_name:
                continue
            cpu, memory = usage_by_key.get((pod.metadata.namespace, pod.metadata.name), (0.0, 0.0))
            results.append(
                PodUsageRaw(
                    namespace=pod.metadata.namespace,
                    node_name=node_name,
                    cpu_usage_cores=cpu,
                    memory_usage_gb=memory,
                    is_daemonset=_is_daemonset(pod),
                )
            )
        return results

    def xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_32(self) -> list[PodUsageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod_list = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        usage_by_key = _fetch_pod_metrics(k8s)

        results: list[PodUsageRaw] = []
        for pod in pod_list.items:
            node_name = getattr(pod.spec, "node_name", None)
            if not node_name:
                continue
            cpu, memory = usage_by_key.get((pod.metadata.namespace, pod.metadata.name), (0.0, 0.0))
            results.append(
                PodUsageRaw(
                    pod_name=pod.metadata.name,
                    node_name=node_name,
                    cpu_usage_cores=cpu,
                    memory_usage_gb=memory,
                    is_daemonset=_is_daemonset(pod),
                )
            )
        return results

    def xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_33(self) -> list[PodUsageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod_list = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        usage_by_key = _fetch_pod_metrics(k8s)

        results: list[PodUsageRaw] = []
        for pod in pod_list.items:
            node_name = getattr(pod.spec, "node_name", None)
            if not node_name:
                continue
            cpu, memory = usage_by_key.get((pod.metadata.namespace, pod.metadata.name), (0.0, 0.0))
            results.append(
                PodUsageRaw(
                    pod_name=pod.metadata.name,
                    namespace=pod.metadata.namespace,
                    cpu_usage_cores=cpu,
                    memory_usage_gb=memory,
                    is_daemonset=_is_daemonset(pod),
                )
            )
        return results

    def xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_34(self) -> list[PodUsageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod_list = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        usage_by_key = _fetch_pod_metrics(k8s)

        results: list[PodUsageRaw] = []
        for pod in pod_list.items:
            node_name = getattr(pod.spec, "node_name", None)
            if not node_name:
                continue
            cpu, memory = usage_by_key.get((pod.metadata.namespace, pod.metadata.name), (0.0, 0.0))
            results.append(
                PodUsageRaw(
                    pod_name=pod.metadata.name,
                    namespace=pod.metadata.namespace,
                    node_name=node_name,
                    memory_usage_gb=memory,
                    is_daemonset=_is_daemonset(pod),
                )
            )
        return results

    def xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_35(self) -> list[PodUsageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod_list = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        usage_by_key = _fetch_pod_metrics(k8s)

        results: list[PodUsageRaw] = []
        for pod in pod_list.items:
            node_name = getattr(pod.spec, "node_name", None)
            if not node_name:
                continue
            cpu, memory = usage_by_key.get((pod.metadata.namespace, pod.metadata.name), (0.0, 0.0))
            results.append(
                PodUsageRaw(
                    pod_name=pod.metadata.name,
                    namespace=pod.metadata.namespace,
                    node_name=node_name,
                    cpu_usage_cores=cpu,
                    is_daemonset=_is_daemonset(pod),
                )
            )
        return results

    def xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_36(self) -> list[PodUsageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod_list = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        usage_by_key = _fetch_pod_metrics(k8s)

        results: list[PodUsageRaw] = []
        for pod in pod_list.items:
            node_name = getattr(pod.spec, "node_name", None)
            if not node_name:
                continue
            cpu, memory = usage_by_key.get((pod.metadata.namespace, pod.metadata.name), (0.0, 0.0))
            results.append(
                PodUsageRaw(
                    pod_name=pod.metadata.name,
                    namespace=pod.metadata.namespace,
                    node_name=node_name,
                    cpu_usage_cores=cpu,
                    memory_usage_gb=memory,
                    )
            )
        return results

    def xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_37(self) -> list[PodUsageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            pod_list = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        usage_by_key = _fetch_pod_metrics(k8s)

        results: list[PodUsageRaw] = []
        for pod in pod_list.items:
            node_name = getattr(pod.spec, "node_name", None)
            if not node_name:
                continue
            cpu, memory = usage_by_key.get((pod.metadata.namespace, pod.metadata.name), (0.0, 0.0))
            results.append(
                PodUsageRaw(
                    pod_name=pod.metadata.name,
                    namespace=pod.metadata.namespace,
                    node_name=node_name,
                    cpu_usage_cores=cpu,
                    memory_usage_gb=memory,
                    is_daemonset=_is_daemonset(None),
                )
            )
        return results

mutants_xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut['_mutmut_orig'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_1'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_2'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_3'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_4'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_5'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_6'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_7'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_8'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_9'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_10'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_11'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_12'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_13'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_14'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_14 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_15'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_15 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_16'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_16 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_17'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_17 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_18'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_18 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_19'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_19 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_20'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_20 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_21'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_21 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_22'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_22 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_23'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_nodes__mutmut_23 # type: ignore # mutmut generated

mutants_xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut['_mutmut_orig'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_1'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_2'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_3'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_4'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_5'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_6'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_7'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_8'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_9'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_10'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_11'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_12'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_13'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_14'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_14 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_15'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_15 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_16'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_16 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_17'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_17 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_18'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_18 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_19'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_19 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_20'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_20 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_21'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_21 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_22'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_22 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_23'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_23 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_24'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_24 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_25'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_25 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_26'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_26 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_27'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_27 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_28'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_28 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_29'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_29 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_30'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_30 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_31'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_31 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_32'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_32 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_33'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_33 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_34'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_34 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_35'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_35 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_36'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_36 # type: ignore # mutmut generated
mutants_xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut['xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_37'] = KubernetesNodeAnalysisAdapter.xǁKubernetesNodeAnalysisAdapterǁlist_pod_usage__mutmut_37 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__fetch_pod_metrics__mutmut)
def _fetch_pod_metrics(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_orig(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_1(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = None  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_2(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = None
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_3(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=None, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_4(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=None, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_5(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=None
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_6(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_7(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_8(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_9(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = None
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_10(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get(None, []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_11(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", None):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_12(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get([]):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_13(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", ):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_14(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("XXitemsXX", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_15(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("ITEMS", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_16(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = None
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_17(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get(None, {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_18(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", None)
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_19(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get({})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_20(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", )
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_21(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("XXmetadataXX", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_22(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("METADATA", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_23(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = None
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_24(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get(None, "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_25(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", None)
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_26(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_27(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", )
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_28(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("XXnamespaceXX", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_29(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("NAMESPACE", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_30(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "XXXX")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_31(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = None
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_32(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get(None, "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_33(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", None)
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_34(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_35(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", )
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_36(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("XXnameXX", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_37(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("NAME", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_38(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "XXXX")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_39(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = None
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_40(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 1.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_41(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = None
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_42(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 1.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_43(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get(None, []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_44(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", None):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_45(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get([]):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_46(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", ):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_47(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("XXcontainersXX", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_48(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("CONTAINERS", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_49(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = None
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_50(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get(None, {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_51(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", None)
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_52(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get({})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_53(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", )
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_54(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("XXusageXX", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_55(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("USAGE", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_56(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total = _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_57(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total -= _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_58(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(None)
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_59(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(None))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_60(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get(None, "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_61(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", None)))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_62(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_63(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", )))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_64(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("XXcpuXX", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_65(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("CPU", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_66(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "XX0XX")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_67(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total = _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_68(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total -= _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_69(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) * _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_70(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(None) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_71(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(None)) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_72(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get(None, "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_73(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", None))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_74(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_75(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", ))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_76(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("XXmemoryXX", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_77(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("MEMORY", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_78(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "XX0XX"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = (cpu_total, memory_total)
    return usage_by_key


def x__fetch_pod_metrics__mutmut_79(k8s: object) -> dict[tuple[str, str], tuple[float, float]]:
    custom_api = k8s.CustomObjectsApi()  # type: ignore[attr-defined]
    try:
        metrics = custom_api.list_cluster_custom_object(
            group=_METRICS_GROUP, version=_METRICS_VERSION, plural=_METRICS_PLURAL
        )
    except Exception:
        return {}

    usage_by_key: dict[tuple[str, str], tuple[float, float]] = {}
    for item in metrics.get("items", []):
        metadata = item.get("metadata", {})
        namespace = metadata.get("namespace", "")
        name = metadata.get("name", "")
        cpu_total = 0.0
        memory_total = 0.0
        for container in item.get("containers", []):
            usage = container.get("usage", {})
            cpu_total += _cpu_to_cores(str(usage.get("cpu", "0")))
            memory_total += _memory_to_bytes(str(usage.get("memory", "0"))) / _BYTES_PER_GB
        usage_by_key[(namespace, name)] = None
    return usage_by_key

mutants_x__fetch_pod_metrics__mutmut['_mutmut_orig'] = x__fetch_pod_metrics__mutmut_orig # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_1'] = x__fetch_pod_metrics__mutmut_1 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_2'] = x__fetch_pod_metrics__mutmut_2 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_3'] = x__fetch_pod_metrics__mutmut_3 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_4'] = x__fetch_pod_metrics__mutmut_4 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_5'] = x__fetch_pod_metrics__mutmut_5 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_6'] = x__fetch_pod_metrics__mutmut_6 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_7'] = x__fetch_pod_metrics__mutmut_7 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_8'] = x__fetch_pod_metrics__mutmut_8 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_9'] = x__fetch_pod_metrics__mutmut_9 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_10'] = x__fetch_pod_metrics__mutmut_10 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_11'] = x__fetch_pod_metrics__mutmut_11 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_12'] = x__fetch_pod_metrics__mutmut_12 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_13'] = x__fetch_pod_metrics__mutmut_13 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_14'] = x__fetch_pod_metrics__mutmut_14 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_15'] = x__fetch_pod_metrics__mutmut_15 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_16'] = x__fetch_pod_metrics__mutmut_16 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_17'] = x__fetch_pod_metrics__mutmut_17 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_18'] = x__fetch_pod_metrics__mutmut_18 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_19'] = x__fetch_pod_metrics__mutmut_19 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_20'] = x__fetch_pod_metrics__mutmut_20 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_21'] = x__fetch_pod_metrics__mutmut_21 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_22'] = x__fetch_pod_metrics__mutmut_22 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_23'] = x__fetch_pod_metrics__mutmut_23 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_24'] = x__fetch_pod_metrics__mutmut_24 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_25'] = x__fetch_pod_metrics__mutmut_25 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_26'] = x__fetch_pod_metrics__mutmut_26 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_27'] = x__fetch_pod_metrics__mutmut_27 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_28'] = x__fetch_pod_metrics__mutmut_28 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_29'] = x__fetch_pod_metrics__mutmut_29 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_30'] = x__fetch_pod_metrics__mutmut_30 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_31'] = x__fetch_pod_metrics__mutmut_31 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_32'] = x__fetch_pod_metrics__mutmut_32 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_33'] = x__fetch_pod_metrics__mutmut_33 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_34'] = x__fetch_pod_metrics__mutmut_34 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_35'] = x__fetch_pod_metrics__mutmut_35 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_36'] = x__fetch_pod_metrics__mutmut_36 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_37'] = x__fetch_pod_metrics__mutmut_37 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_38'] = x__fetch_pod_metrics__mutmut_38 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_39'] = x__fetch_pod_metrics__mutmut_39 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_40'] = x__fetch_pod_metrics__mutmut_40 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_41'] = x__fetch_pod_metrics__mutmut_41 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_42'] = x__fetch_pod_metrics__mutmut_42 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_43'] = x__fetch_pod_metrics__mutmut_43 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_44'] = x__fetch_pod_metrics__mutmut_44 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_45'] = x__fetch_pod_metrics__mutmut_45 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_46'] = x__fetch_pod_metrics__mutmut_46 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_47'] = x__fetch_pod_metrics__mutmut_47 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_48'] = x__fetch_pod_metrics__mutmut_48 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_49'] = x__fetch_pod_metrics__mutmut_49 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_50'] = x__fetch_pod_metrics__mutmut_50 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_51'] = x__fetch_pod_metrics__mutmut_51 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_52'] = x__fetch_pod_metrics__mutmut_52 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_53'] = x__fetch_pod_metrics__mutmut_53 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_54'] = x__fetch_pod_metrics__mutmut_54 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_55'] = x__fetch_pod_metrics__mutmut_55 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_56'] = x__fetch_pod_metrics__mutmut_56 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_57'] = x__fetch_pod_metrics__mutmut_57 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_58'] = x__fetch_pod_metrics__mutmut_58 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_59'] = x__fetch_pod_metrics__mutmut_59 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_60'] = x__fetch_pod_metrics__mutmut_60 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_61'] = x__fetch_pod_metrics__mutmut_61 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_62'] = x__fetch_pod_metrics__mutmut_62 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_63'] = x__fetch_pod_metrics__mutmut_63 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_64'] = x__fetch_pod_metrics__mutmut_64 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_65'] = x__fetch_pod_metrics__mutmut_65 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_66'] = x__fetch_pod_metrics__mutmut_66 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_67'] = x__fetch_pod_metrics__mutmut_67 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_68'] = x__fetch_pod_metrics__mutmut_68 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_69'] = x__fetch_pod_metrics__mutmut_69 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_70'] = x__fetch_pod_metrics__mutmut_70 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_71'] = x__fetch_pod_metrics__mutmut_71 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_72'] = x__fetch_pod_metrics__mutmut_72 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_73'] = x__fetch_pod_metrics__mutmut_73 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_74'] = x__fetch_pod_metrics__mutmut_74 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_75'] = x__fetch_pod_metrics__mutmut_75 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_76'] = x__fetch_pod_metrics__mutmut_76 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_77'] = x__fetch_pod_metrics__mutmut_77 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_78'] = x__fetch_pod_metrics__mutmut_78 # type: ignore # mutmut generated
mutants_x__fetch_pod_metrics__mutmut['x__fetch_pod_metrics__mutmut_79'] = x__fetch_pod_metrics__mutmut_79 # type: ignore # mutmut generated
mutants_x__is_daemonset__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__is_daemonset__mutmut)
def _is_daemonset(pod: object) -> bool:
    metadata = getattr(pod, "metadata", None)
    owner_refs = getattr(metadata, "owner_references", None)
    if not isinstance(owner_refs, list):
        return False
    return any(getattr(ref, "kind", None) == "DaemonSet" for ref in owner_refs)


def x__is_daemonset__mutmut_orig(pod: object) -> bool:
    metadata = getattr(pod, "metadata", None)
    owner_refs = getattr(metadata, "owner_references", None)
    if not isinstance(owner_refs, list):
        return False
    return any(getattr(ref, "kind", None) == "DaemonSet" for ref in owner_refs)


def x__is_daemonset__mutmut_1(pod: object) -> bool:
    metadata = None
    owner_refs = getattr(metadata, "owner_references", None)
    if not isinstance(owner_refs, list):
        return False
    return any(getattr(ref, "kind", None) == "DaemonSet" for ref in owner_refs)


def x__is_daemonset__mutmut_2(pod: object) -> bool:
    metadata = getattr(None, "metadata", None)
    owner_refs = getattr(metadata, "owner_references", None)
    if not isinstance(owner_refs, list):
        return False
    return any(getattr(ref, "kind", None) == "DaemonSet" for ref in owner_refs)


def x__is_daemonset__mutmut_3(pod: object) -> bool:
    metadata = getattr(pod, None, None)
    owner_refs = getattr(metadata, "owner_references", None)
    if not isinstance(owner_refs, list):
        return False
    return any(getattr(ref, "kind", None) == "DaemonSet" for ref in owner_refs)


def x__is_daemonset__mutmut_4(pod: object) -> bool:
    metadata = getattr("metadata", None)
    owner_refs = getattr(metadata, "owner_references", None)
    if not isinstance(owner_refs, list):
        return False
    return any(getattr(ref, "kind", None) == "DaemonSet" for ref in owner_refs)


def x__is_daemonset__mutmut_5(pod: object) -> bool:
    metadata = getattr(pod, None)
    owner_refs = getattr(metadata, "owner_references", None)
    if not isinstance(owner_refs, list):
        return False
    return any(getattr(ref, "kind", None) == "DaemonSet" for ref in owner_refs)


def x__is_daemonset__mutmut_6(pod: object) -> bool:
    metadata = getattr(pod, "metadata", )
    owner_refs = getattr(metadata, "owner_references", None)
    if not isinstance(owner_refs, list):
        return False
    return any(getattr(ref, "kind", None) == "DaemonSet" for ref in owner_refs)


def x__is_daemonset__mutmut_7(pod: object) -> bool:
    metadata = getattr(pod, "XXmetadataXX", None)
    owner_refs = getattr(metadata, "owner_references", None)
    if not isinstance(owner_refs, list):
        return False
    return any(getattr(ref, "kind", None) == "DaemonSet" for ref in owner_refs)


def x__is_daemonset__mutmut_8(pod: object) -> bool:
    metadata = getattr(pod, "METADATA", None)
    owner_refs = getattr(metadata, "owner_references", None)
    if not isinstance(owner_refs, list):
        return False
    return any(getattr(ref, "kind", None) == "DaemonSet" for ref in owner_refs)


def x__is_daemonset__mutmut_9(pod: object) -> bool:
    metadata = getattr(pod, "metadata", None)
    owner_refs = None
    if not isinstance(owner_refs, list):
        return False
    return any(getattr(ref, "kind", None) == "DaemonSet" for ref in owner_refs)


def x__is_daemonset__mutmut_10(pod: object) -> bool:
    metadata = getattr(pod, "metadata", None)
    owner_refs = getattr(None, "owner_references", None)
    if not isinstance(owner_refs, list):
        return False
    return any(getattr(ref, "kind", None) == "DaemonSet" for ref in owner_refs)


def x__is_daemonset__mutmut_11(pod: object) -> bool:
    metadata = getattr(pod, "metadata", None)
    owner_refs = getattr(metadata, None, None)
    if not isinstance(owner_refs, list):
        return False
    return any(getattr(ref, "kind", None) == "DaemonSet" for ref in owner_refs)


def x__is_daemonset__mutmut_12(pod: object) -> bool:
    metadata = getattr(pod, "metadata", None)
    owner_refs = getattr("owner_references", None)
    if not isinstance(owner_refs, list):
        return False
    return any(getattr(ref, "kind", None) == "DaemonSet" for ref in owner_refs)


def x__is_daemonset__mutmut_13(pod: object) -> bool:
    metadata = getattr(pod, "metadata", None)
    owner_refs = getattr(metadata, None)
    if not isinstance(owner_refs, list):
        return False
    return any(getattr(ref, "kind", None) == "DaemonSet" for ref in owner_refs)


def x__is_daemonset__mutmut_14(pod: object) -> bool:
    metadata = getattr(pod, "metadata", None)
    owner_refs = getattr(metadata, "owner_references", )
    if not isinstance(owner_refs, list):
        return False
    return any(getattr(ref, "kind", None) == "DaemonSet" for ref in owner_refs)


def x__is_daemonset__mutmut_15(pod: object) -> bool:
    metadata = getattr(pod, "metadata", None)
    owner_refs = getattr(metadata, "XXowner_referencesXX", None)
    if not isinstance(owner_refs, list):
        return False
    return any(getattr(ref, "kind", None) == "DaemonSet" for ref in owner_refs)


def x__is_daemonset__mutmut_16(pod: object) -> bool:
    metadata = getattr(pod, "metadata", None)
    owner_refs = getattr(metadata, "OWNER_REFERENCES", None)
    if not isinstance(owner_refs, list):
        return False
    return any(getattr(ref, "kind", None) == "DaemonSet" for ref in owner_refs)


def x__is_daemonset__mutmut_17(pod: object) -> bool:
    metadata = getattr(pod, "metadata", None)
    owner_refs = getattr(metadata, "owner_references", None)
    if isinstance(owner_refs, list):
        return False
    return any(getattr(ref, "kind", None) == "DaemonSet" for ref in owner_refs)


def x__is_daemonset__mutmut_18(pod: object) -> bool:
    metadata = getattr(pod, "metadata", None)
    owner_refs = getattr(metadata, "owner_references", None)
    if not isinstance(owner_refs, list):
        return True
    return any(getattr(ref, "kind", None) == "DaemonSet" for ref in owner_refs)


def x__is_daemonset__mutmut_19(pod: object) -> bool:
    metadata = getattr(pod, "metadata", None)
    owner_refs = getattr(metadata, "owner_references", None)
    if not isinstance(owner_refs, list):
        return False
    return any(None)


def x__is_daemonset__mutmut_20(pod: object) -> bool:
    metadata = getattr(pod, "metadata", None)
    owner_refs = getattr(metadata, "owner_references", None)
    if not isinstance(owner_refs, list):
        return False
    return any(getattr(None, "kind", None) == "DaemonSet" for ref in owner_refs)


def x__is_daemonset__mutmut_21(pod: object) -> bool:
    metadata = getattr(pod, "metadata", None)
    owner_refs = getattr(metadata, "owner_references", None)
    if not isinstance(owner_refs, list):
        return False
    return any(getattr(ref, None, None) == "DaemonSet" for ref in owner_refs)


def x__is_daemonset__mutmut_22(pod: object) -> bool:
    metadata = getattr(pod, "metadata", None)
    owner_refs = getattr(metadata, "owner_references", None)
    if not isinstance(owner_refs, list):
        return False
    return any(getattr("kind", None) == "DaemonSet" for ref in owner_refs)


def x__is_daemonset__mutmut_23(pod: object) -> bool:
    metadata = getattr(pod, "metadata", None)
    owner_refs = getattr(metadata, "owner_references", None)
    if not isinstance(owner_refs, list):
        return False
    return any(getattr(ref, None) == "DaemonSet" for ref in owner_refs)


def x__is_daemonset__mutmut_24(pod: object) -> bool:
    metadata = getattr(pod, "metadata", None)
    owner_refs = getattr(metadata, "owner_references", None)
    if not isinstance(owner_refs, list):
        return False
    return any(getattr(ref, "kind", ) == "DaemonSet" for ref in owner_refs)


def x__is_daemonset__mutmut_25(pod: object) -> bool:
    metadata = getattr(pod, "metadata", None)
    owner_refs = getattr(metadata, "owner_references", None)
    if not isinstance(owner_refs, list):
        return False
    return any(getattr(ref, "XXkindXX", None) == "DaemonSet" for ref in owner_refs)


def x__is_daemonset__mutmut_26(pod: object) -> bool:
    metadata = getattr(pod, "metadata", None)
    owner_refs = getattr(metadata, "owner_references", None)
    if not isinstance(owner_refs, list):
        return False
    return any(getattr(ref, "KIND", None) == "DaemonSet" for ref in owner_refs)


def x__is_daemonset__mutmut_27(pod: object) -> bool:
    metadata = getattr(pod, "metadata", None)
    owner_refs = getattr(metadata, "owner_references", None)
    if not isinstance(owner_refs, list):
        return False
    return any(getattr(ref, "kind", None) != "DaemonSet" for ref in owner_refs)


def x__is_daemonset__mutmut_28(pod: object) -> bool:
    metadata = getattr(pod, "metadata", None)
    owner_refs = getattr(metadata, "owner_references", None)
    if not isinstance(owner_refs, list):
        return False
    return any(getattr(ref, "kind", None) == "XXDaemonSetXX" for ref in owner_refs)


def x__is_daemonset__mutmut_29(pod: object) -> bool:
    metadata = getattr(pod, "metadata", None)
    owner_refs = getattr(metadata, "owner_references", None)
    if not isinstance(owner_refs, list):
        return False
    return any(getattr(ref, "kind", None) == "daemonset" for ref in owner_refs)


def x__is_daemonset__mutmut_30(pod: object) -> bool:
    metadata = getattr(pod, "metadata", None)
    owner_refs = getattr(metadata, "owner_references", None)
    if not isinstance(owner_refs, list):
        return False
    return any(getattr(ref, "kind", None) == "DAEMONSET" for ref in owner_refs)

mutants_x__is_daemonset__mutmut['_mutmut_orig'] = x__is_daemonset__mutmut_orig # type: ignore # mutmut generated
mutants_x__is_daemonset__mutmut['x__is_daemonset__mutmut_1'] = x__is_daemonset__mutmut_1 # type: ignore # mutmut generated
mutants_x__is_daemonset__mutmut['x__is_daemonset__mutmut_2'] = x__is_daemonset__mutmut_2 # type: ignore # mutmut generated
mutants_x__is_daemonset__mutmut['x__is_daemonset__mutmut_3'] = x__is_daemonset__mutmut_3 # type: ignore # mutmut generated
mutants_x__is_daemonset__mutmut['x__is_daemonset__mutmut_4'] = x__is_daemonset__mutmut_4 # type: ignore # mutmut generated
mutants_x__is_daemonset__mutmut['x__is_daemonset__mutmut_5'] = x__is_daemonset__mutmut_5 # type: ignore # mutmut generated
mutants_x__is_daemonset__mutmut['x__is_daemonset__mutmut_6'] = x__is_daemonset__mutmut_6 # type: ignore # mutmut generated
mutants_x__is_daemonset__mutmut['x__is_daemonset__mutmut_7'] = x__is_daemonset__mutmut_7 # type: ignore # mutmut generated
mutants_x__is_daemonset__mutmut['x__is_daemonset__mutmut_8'] = x__is_daemonset__mutmut_8 # type: ignore # mutmut generated
mutants_x__is_daemonset__mutmut['x__is_daemonset__mutmut_9'] = x__is_daemonset__mutmut_9 # type: ignore # mutmut generated
mutants_x__is_daemonset__mutmut['x__is_daemonset__mutmut_10'] = x__is_daemonset__mutmut_10 # type: ignore # mutmut generated
mutants_x__is_daemonset__mutmut['x__is_daemonset__mutmut_11'] = x__is_daemonset__mutmut_11 # type: ignore # mutmut generated
mutants_x__is_daemonset__mutmut['x__is_daemonset__mutmut_12'] = x__is_daemonset__mutmut_12 # type: ignore # mutmut generated
mutants_x__is_daemonset__mutmut['x__is_daemonset__mutmut_13'] = x__is_daemonset__mutmut_13 # type: ignore # mutmut generated
mutants_x__is_daemonset__mutmut['x__is_daemonset__mutmut_14'] = x__is_daemonset__mutmut_14 # type: ignore # mutmut generated
mutants_x__is_daemonset__mutmut['x__is_daemonset__mutmut_15'] = x__is_daemonset__mutmut_15 # type: ignore # mutmut generated
mutants_x__is_daemonset__mutmut['x__is_daemonset__mutmut_16'] = x__is_daemonset__mutmut_16 # type: ignore # mutmut generated
mutants_x__is_daemonset__mutmut['x__is_daemonset__mutmut_17'] = x__is_daemonset__mutmut_17 # type: ignore # mutmut generated
mutants_x__is_daemonset__mutmut['x__is_daemonset__mutmut_18'] = x__is_daemonset__mutmut_18 # type: ignore # mutmut generated
mutants_x__is_daemonset__mutmut['x__is_daemonset__mutmut_19'] = x__is_daemonset__mutmut_19 # type: ignore # mutmut generated
mutants_x__is_daemonset__mutmut['x__is_daemonset__mutmut_20'] = x__is_daemonset__mutmut_20 # type: ignore # mutmut generated
mutants_x__is_daemonset__mutmut['x__is_daemonset__mutmut_21'] = x__is_daemonset__mutmut_21 # type: ignore # mutmut generated
mutants_x__is_daemonset__mutmut['x__is_daemonset__mutmut_22'] = x__is_daemonset__mutmut_22 # type: ignore # mutmut generated
mutants_x__is_daemonset__mutmut['x__is_daemonset__mutmut_23'] = x__is_daemonset__mutmut_23 # type: ignore # mutmut generated
mutants_x__is_daemonset__mutmut['x__is_daemonset__mutmut_24'] = x__is_daemonset__mutmut_24 # type: ignore # mutmut generated
mutants_x__is_daemonset__mutmut['x__is_daemonset__mutmut_25'] = x__is_daemonset__mutmut_25 # type: ignore # mutmut generated
mutants_x__is_daemonset__mutmut['x__is_daemonset__mutmut_26'] = x__is_daemonset__mutmut_26 # type: ignore # mutmut generated
mutants_x__is_daemonset__mutmut['x__is_daemonset__mutmut_27'] = x__is_daemonset__mutmut_27 # type: ignore # mutmut generated
mutants_x__is_daemonset__mutmut['x__is_daemonset__mutmut_28'] = x__is_daemonset__mutmut_28 # type: ignore # mutmut generated
mutants_x__is_daemonset__mutmut['x__is_daemonset__mutmut_29'] = x__is_daemonset__mutmut_29 # type: ignore # mutmut generated
mutants_x__is_daemonset__mutmut['x__is_daemonset__mutmut_30'] = x__is_daemonset__mutmut_30 # type: ignore # mutmut generated
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
        return InsufficientPermissionsError("RBAC denied access to cluster node/pod info")
    return ClusterUnreachableError(f"Cannot list cluster node/pod info: {exc}")


def x__translate_error__mutmut_orig(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to cluster node/pod info")
    return ClusterUnreachableError(f"Cannot list cluster node/pod info: {exc}")


def x__translate_error__mutmut_1(exc: Exception) -> Exception:
    status = None
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to cluster node/pod info")
    return ClusterUnreachableError(f"Cannot list cluster node/pod info: {exc}")


def x__translate_error__mutmut_2(exc: Exception) -> Exception:
    status = getattr(None, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to cluster node/pod info")
    return ClusterUnreachableError(f"Cannot list cluster node/pod info: {exc}")


def x__translate_error__mutmut_3(exc: Exception) -> Exception:
    status = getattr(exc, None, None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to cluster node/pod info")
    return ClusterUnreachableError(f"Cannot list cluster node/pod info: {exc}")


def x__translate_error__mutmut_4(exc: Exception) -> Exception:
    status = getattr("status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to cluster node/pod info")
    return ClusterUnreachableError(f"Cannot list cluster node/pod info: {exc}")


def x__translate_error__mutmut_5(exc: Exception) -> Exception:
    status = getattr(exc, None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to cluster node/pod info")
    return ClusterUnreachableError(f"Cannot list cluster node/pod info: {exc}")


def x__translate_error__mutmut_6(exc: Exception) -> Exception:
    status = getattr(exc, "status", )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to cluster node/pod info")
    return ClusterUnreachableError(f"Cannot list cluster node/pod info: {exc}")


def x__translate_error__mutmut_7(exc: Exception) -> Exception:
    status = getattr(exc, "XXstatusXX", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to cluster node/pod info")
    return ClusterUnreachableError(f"Cannot list cluster node/pod info: {exc}")


def x__translate_error__mutmut_8(exc: Exception) -> Exception:
    status = getattr(exc, "STATUS", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to cluster node/pod info")
    return ClusterUnreachableError(f"Cannot list cluster node/pod info: {exc}")


def x__translate_error__mutmut_9(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status != _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to cluster node/pod info")
    return ClusterUnreachableError(f"Cannot list cluster node/pod info: {exc}")


def x__translate_error__mutmut_10(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(None)
    return ClusterUnreachableError(f"Cannot list cluster node/pod info: {exc}")


def x__translate_error__mutmut_11(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("XXRBAC denied access to cluster node/pod infoXX")
    return ClusterUnreachableError(f"Cannot list cluster node/pod info: {exc}")


def x__translate_error__mutmut_12(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("rbac denied access to cluster node/pod info")
    return ClusterUnreachableError(f"Cannot list cluster node/pod info: {exc}")


def x__translate_error__mutmut_13(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC DENIED ACCESS TO CLUSTER NODE/POD INFO")
    return ClusterUnreachableError(f"Cannot list cluster node/pod info: {exc}")


def x__translate_error__mutmut_14(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to cluster node/pod info")
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
