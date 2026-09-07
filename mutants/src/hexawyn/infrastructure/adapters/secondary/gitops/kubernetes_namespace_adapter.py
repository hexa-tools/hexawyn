from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driven.namespace_overview_port import (
    DeploymentStatusRaw,
    HpaStatusRaw,
    NamespaceOverviewPort,
    NamespaceOverviewRawData,
    PodStatusRaw,
)
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    InsufficientPermissionsError,
    ResourceNotFoundError,
)

if TYPE_CHECKING:
    from kubernetes.client import V1Deployment, V1HorizontalPodAutoscaler, V1Pod

_K8S_FORBIDDEN = 403
_K8S_NOT_FOUND = 404


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut: MutantDict = {}  # type: ignore


class KubernetesNamespaceAdapter(NamespaceOverviewPort):
    """Secondary adapter — one bulk fetch of pods/deployments/services/HPAs
    for a namespace, used to build a compact, conservative health overview."""

    @_mutmut_mutated(mutants_xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut)
    def get_namespace_overview_data(self, namespace: str) -> NamespaceOverviewRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            ns = core_api.read_namespace(name=namespace)
        except Exception as exc:
            raise _translate_namespace_error(exc, namespace) from exc

        apps_api = k8s.AppsV1Api()
        autoscaling_api = k8s.AutoscalingV2Api()

        pod_list = core_api.list_namespaced_pod(namespace=namespace)
        deployment_list = apps_api.list_namespaced_deployment(namespace=namespace)
        service_list = core_api.list_namespaced_service(namespace=namespace)
        hpa_list = autoscaling_api.list_namespaced_horizontal_pod_autoscaler(namespace=namespace)

        return NamespaceOverviewRawData(
            namespace_status=ns.status.phase or "Active",
            pods=[_to_pod_status(pod) for pod in pod_list.items],
            deployments=[_to_deployment_status(deployment) for deployment in deployment_list.items],
            services_count=len(service_list.items),
            hpas=[_to_hpa_status(hpa) for hpa in hpa_list.items],
        )

    def xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_orig(self, namespace: str) -> NamespaceOverviewRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            ns = core_api.read_namespace(name=namespace)
        except Exception as exc:
            raise _translate_namespace_error(exc, namespace) from exc

        apps_api = k8s.AppsV1Api()
        autoscaling_api = k8s.AutoscalingV2Api()

        pod_list = core_api.list_namespaced_pod(namespace=namespace)
        deployment_list = apps_api.list_namespaced_deployment(namespace=namespace)
        service_list = core_api.list_namespaced_service(namespace=namespace)
        hpa_list = autoscaling_api.list_namespaced_horizontal_pod_autoscaler(namespace=namespace)

        return NamespaceOverviewRawData(
            namespace_status=ns.status.phase or "Active",
            pods=[_to_pod_status(pod) for pod in pod_list.items],
            deployments=[_to_deployment_status(deployment) for deployment in deployment_list.items],
            services_count=len(service_list.items),
            hpas=[_to_hpa_status(hpa) for hpa in hpa_list.items],
        )

    def xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_1(self, namespace: str) -> NamespaceOverviewRawData:
        from kubernetes import client as k8s

        core_api = None
        try:
            ns = core_api.read_namespace(name=namespace)
        except Exception as exc:
            raise _translate_namespace_error(exc, namespace) from exc

        apps_api = k8s.AppsV1Api()
        autoscaling_api = k8s.AutoscalingV2Api()

        pod_list = core_api.list_namespaced_pod(namespace=namespace)
        deployment_list = apps_api.list_namespaced_deployment(namespace=namespace)
        service_list = core_api.list_namespaced_service(namespace=namespace)
        hpa_list = autoscaling_api.list_namespaced_horizontal_pod_autoscaler(namespace=namespace)

        return NamespaceOverviewRawData(
            namespace_status=ns.status.phase or "Active",
            pods=[_to_pod_status(pod) for pod in pod_list.items],
            deployments=[_to_deployment_status(deployment) for deployment in deployment_list.items],
            services_count=len(service_list.items),
            hpas=[_to_hpa_status(hpa) for hpa in hpa_list.items],
        )

    def xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_2(self, namespace: str) -> NamespaceOverviewRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            ns = None
        except Exception as exc:
            raise _translate_namespace_error(exc, namespace) from exc

        apps_api = k8s.AppsV1Api()
        autoscaling_api = k8s.AutoscalingV2Api()

        pod_list = core_api.list_namespaced_pod(namespace=namespace)
        deployment_list = apps_api.list_namespaced_deployment(namespace=namespace)
        service_list = core_api.list_namespaced_service(namespace=namespace)
        hpa_list = autoscaling_api.list_namespaced_horizontal_pod_autoscaler(namespace=namespace)

        return NamespaceOverviewRawData(
            namespace_status=ns.status.phase or "Active",
            pods=[_to_pod_status(pod) for pod in pod_list.items],
            deployments=[_to_deployment_status(deployment) for deployment in deployment_list.items],
            services_count=len(service_list.items),
            hpas=[_to_hpa_status(hpa) for hpa in hpa_list.items],
        )

    def xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_3(self, namespace: str) -> NamespaceOverviewRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            ns = core_api.read_namespace(name=None)
        except Exception as exc:
            raise _translate_namespace_error(exc, namespace) from exc

        apps_api = k8s.AppsV1Api()
        autoscaling_api = k8s.AutoscalingV2Api()

        pod_list = core_api.list_namespaced_pod(namespace=namespace)
        deployment_list = apps_api.list_namespaced_deployment(namespace=namespace)
        service_list = core_api.list_namespaced_service(namespace=namespace)
        hpa_list = autoscaling_api.list_namespaced_horizontal_pod_autoscaler(namespace=namespace)

        return NamespaceOverviewRawData(
            namespace_status=ns.status.phase or "Active",
            pods=[_to_pod_status(pod) for pod in pod_list.items],
            deployments=[_to_deployment_status(deployment) for deployment in deployment_list.items],
            services_count=len(service_list.items),
            hpas=[_to_hpa_status(hpa) for hpa in hpa_list.items],
        )

    def xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_4(self, namespace: str) -> NamespaceOverviewRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            ns = core_api.read_namespace(name=namespace)
        except Exception as exc:
            raise _translate_namespace_error(None, namespace) from exc

        apps_api = k8s.AppsV1Api()
        autoscaling_api = k8s.AutoscalingV2Api()

        pod_list = core_api.list_namespaced_pod(namespace=namespace)
        deployment_list = apps_api.list_namespaced_deployment(namespace=namespace)
        service_list = core_api.list_namespaced_service(namespace=namespace)
        hpa_list = autoscaling_api.list_namespaced_horizontal_pod_autoscaler(namespace=namespace)

        return NamespaceOverviewRawData(
            namespace_status=ns.status.phase or "Active",
            pods=[_to_pod_status(pod) for pod in pod_list.items],
            deployments=[_to_deployment_status(deployment) for deployment in deployment_list.items],
            services_count=len(service_list.items),
            hpas=[_to_hpa_status(hpa) for hpa in hpa_list.items],
        )

    def xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_5(self, namespace: str) -> NamespaceOverviewRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            ns = core_api.read_namespace(name=namespace)
        except Exception as exc:
            raise _translate_namespace_error(exc, None) from exc

        apps_api = k8s.AppsV1Api()
        autoscaling_api = k8s.AutoscalingV2Api()

        pod_list = core_api.list_namespaced_pod(namespace=namespace)
        deployment_list = apps_api.list_namespaced_deployment(namespace=namespace)
        service_list = core_api.list_namespaced_service(namespace=namespace)
        hpa_list = autoscaling_api.list_namespaced_horizontal_pod_autoscaler(namespace=namespace)

        return NamespaceOverviewRawData(
            namespace_status=ns.status.phase or "Active",
            pods=[_to_pod_status(pod) for pod in pod_list.items],
            deployments=[_to_deployment_status(deployment) for deployment in deployment_list.items],
            services_count=len(service_list.items),
            hpas=[_to_hpa_status(hpa) for hpa in hpa_list.items],
        )

    def xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_6(self, namespace: str) -> NamespaceOverviewRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            ns = core_api.read_namespace(name=namespace)
        except Exception as exc:
            raise _translate_namespace_error(namespace) from exc

        apps_api = k8s.AppsV1Api()
        autoscaling_api = k8s.AutoscalingV2Api()

        pod_list = core_api.list_namespaced_pod(namespace=namespace)
        deployment_list = apps_api.list_namespaced_deployment(namespace=namespace)
        service_list = core_api.list_namespaced_service(namespace=namespace)
        hpa_list = autoscaling_api.list_namespaced_horizontal_pod_autoscaler(namespace=namespace)

        return NamespaceOverviewRawData(
            namespace_status=ns.status.phase or "Active",
            pods=[_to_pod_status(pod) for pod in pod_list.items],
            deployments=[_to_deployment_status(deployment) for deployment in deployment_list.items],
            services_count=len(service_list.items),
            hpas=[_to_hpa_status(hpa) for hpa in hpa_list.items],
        )

    def xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_7(self, namespace: str) -> NamespaceOverviewRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            ns = core_api.read_namespace(name=namespace)
        except Exception as exc:
            raise _translate_namespace_error(exc, ) from exc

        apps_api = k8s.AppsV1Api()
        autoscaling_api = k8s.AutoscalingV2Api()

        pod_list = core_api.list_namespaced_pod(namespace=namespace)
        deployment_list = apps_api.list_namespaced_deployment(namespace=namespace)
        service_list = core_api.list_namespaced_service(namespace=namespace)
        hpa_list = autoscaling_api.list_namespaced_horizontal_pod_autoscaler(namespace=namespace)

        return NamespaceOverviewRawData(
            namespace_status=ns.status.phase or "Active",
            pods=[_to_pod_status(pod) for pod in pod_list.items],
            deployments=[_to_deployment_status(deployment) for deployment in deployment_list.items],
            services_count=len(service_list.items),
            hpas=[_to_hpa_status(hpa) for hpa in hpa_list.items],
        )

    def xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_8(self, namespace: str) -> NamespaceOverviewRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            ns = core_api.read_namespace(name=namespace)
        except Exception as exc:
            raise _translate_namespace_error(exc, namespace) from exc

        apps_api = None
        autoscaling_api = k8s.AutoscalingV2Api()

        pod_list = core_api.list_namespaced_pod(namespace=namespace)
        deployment_list = apps_api.list_namespaced_deployment(namespace=namespace)
        service_list = core_api.list_namespaced_service(namespace=namespace)
        hpa_list = autoscaling_api.list_namespaced_horizontal_pod_autoscaler(namespace=namespace)

        return NamespaceOverviewRawData(
            namespace_status=ns.status.phase or "Active",
            pods=[_to_pod_status(pod) for pod in pod_list.items],
            deployments=[_to_deployment_status(deployment) for deployment in deployment_list.items],
            services_count=len(service_list.items),
            hpas=[_to_hpa_status(hpa) for hpa in hpa_list.items],
        )

    def xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_9(self, namespace: str) -> NamespaceOverviewRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            ns = core_api.read_namespace(name=namespace)
        except Exception as exc:
            raise _translate_namespace_error(exc, namespace) from exc

        apps_api = k8s.AppsV1Api()
        autoscaling_api = None

        pod_list = core_api.list_namespaced_pod(namespace=namespace)
        deployment_list = apps_api.list_namespaced_deployment(namespace=namespace)
        service_list = core_api.list_namespaced_service(namespace=namespace)
        hpa_list = autoscaling_api.list_namespaced_horizontal_pod_autoscaler(namespace=namespace)

        return NamespaceOverviewRawData(
            namespace_status=ns.status.phase or "Active",
            pods=[_to_pod_status(pod) for pod in pod_list.items],
            deployments=[_to_deployment_status(deployment) for deployment in deployment_list.items],
            services_count=len(service_list.items),
            hpas=[_to_hpa_status(hpa) for hpa in hpa_list.items],
        )

    def xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_10(self, namespace: str) -> NamespaceOverviewRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            ns = core_api.read_namespace(name=namespace)
        except Exception as exc:
            raise _translate_namespace_error(exc, namespace) from exc

        apps_api = k8s.AppsV1Api()
        autoscaling_api = k8s.AutoscalingV2Api()

        pod_list = None
        deployment_list = apps_api.list_namespaced_deployment(namespace=namespace)
        service_list = core_api.list_namespaced_service(namespace=namespace)
        hpa_list = autoscaling_api.list_namespaced_horizontal_pod_autoscaler(namespace=namespace)

        return NamespaceOverviewRawData(
            namespace_status=ns.status.phase or "Active",
            pods=[_to_pod_status(pod) for pod in pod_list.items],
            deployments=[_to_deployment_status(deployment) for deployment in deployment_list.items],
            services_count=len(service_list.items),
            hpas=[_to_hpa_status(hpa) for hpa in hpa_list.items],
        )

    def xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_11(self, namespace: str) -> NamespaceOverviewRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            ns = core_api.read_namespace(name=namespace)
        except Exception as exc:
            raise _translate_namespace_error(exc, namespace) from exc

        apps_api = k8s.AppsV1Api()
        autoscaling_api = k8s.AutoscalingV2Api()

        pod_list = core_api.list_namespaced_pod(namespace=None)
        deployment_list = apps_api.list_namespaced_deployment(namespace=namespace)
        service_list = core_api.list_namespaced_service(namespace=namespace)
        hpa_list = autoscaling_api.list_namespaced_horizontal_pod_autoscaler(namespace=namespace)

        return NamespaceOverviewRawData(
            namespace_status=ns.status.phase or "Active",
            pods=[_to_pod_status(pod) for pod in pod_list.items],
            deployments=[_to_deployment_status(deployment) for deployment in deployment_list.items],
            services_count=len(service_list.items),
            hpas=[_to_hpa_status(hpa) for hpa in hpa_list.items],
        )

    def xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_12(self, namespace: str) -> NamespaceOverviewRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            ns = core_api.read_namespace(name=namespace)
        except Exception as exc:
            raise _translate_namespace_error(exc, namespace) from exc

        apps_api = k8s.AppsV1Api()
        autoscaling_api = k8s.AutoscalingV2Api()

        pod_list = core_api.list_namespaced_pod(namespace=namespace)
        deployment_list = None
        service_list = core_api.list_namespaced_service(namespace=namespace)
        hpa_list = autoscaling_api.list_namespaced_horizontal_pod_autoscaler(namespace=namespace)

        return NamespaceOverviewRawData(
            namespace_status=ns.status.phase or "Active",
            pods=[_to_pod_status(pod) for pod in pod_list.items],
            deployments=[_to_deployment_status(deployment) for deployment in deployment_list.items],
            services_count=len(service_list.items),
            hpas=[_to_hpa_status(hpa) for hpa in hpa_list.items],
        )

    def xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_13(self, namespace: str) -> NamespaceOverviewRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            ns = core_api.read_namespace(name=namespace)
        except Exception as exc:
            raise _translate_namespace_error(exc, namespace) from exc

        apps_api = k8s.AppsV1Api()
        autoscaling_api = k8s.AutoscalingV2Api()

        pod_list = core_api.list_namespaced_pod(namespace=namespace)
        deployment_list = apps_api.list_namespaced_deployment(namespace=None)
        service_list = core_api.list_namespaced_service(namespace=namespace)
        hpa_list = autoscaling_api.list_namespaced_horizontal_pod_autoscaler(namespace=namespace)

        return NamespaceOverviewRawData(
            namespace_status=ns.status.phase or "Active",
            pods=[_to_pod_status(pod) for pod in pod_list.items],
            deployments=[_to_deployment_status(deployment) for deployment in deployment_list.items],
            services_count=len(service_list.items),
            hpas=[_to_hpa_status(hpa) for hpa in hpa_list.items],
        )

    def xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_14(self, namespace: str) -> NamespaceOverviewRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            ns = core_api.read_namespace(name=namespace)
        except Exception as exc:
            raise _translate_namespace_error(exc, namespace) from exc

        apps_api = k8s.AppsV1Api()
        autoscaling_api = k8s.AutoscalingV2Api()

        pod_list = core_api.list_namespaced_pod(namespace=namespace)
        deployment_list = apps_api.list_namespaced_deployment(namespace=namespace)
        service_list = None
        hpa_list = autoscaling_api.list_namespaced_horizontal_pod_autoscaler(namespace=namespace)

        return NamespaceOverviewRawData(
            namespace_status=ns.status.phase or "Active",
            pods=[_to_pod_status(pod) for pod in pod_list.items],
            deployments=[_to_deployment_status(deployment) for deployment in deployment_list.items],
            services_count=len(service_list.items),
            hpas=[_to_hpa_status(hpa) for hpa in hpa_list.items],
        )

    def xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_15(self, namespace: str) -> NamespaceOverviewRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            ns = core_api.read_namespace(name=namespace)
        except Exception as exc:
            raise _translate_namespace_error(exc, namespace) from exc

        apps_api = k8s.AppsV1Api()
        autoscaling_api = k8s.AutoscalingV2Api()

        pod_list = core_api.list_namespaced_pod(namespace=namespace)
        deployment_list = apps_api.list_namespaced_deployment(namespace=namespace)
        service_list = core_api.list_namespaced_service(namespace=None)
        hpa_list = autoscaling_api.list_namespaced_horizontal_pod_autoscaler(namespace=namespace)

        return NamespaceOverviewRawData(
            namespace_status=ns.status.phase or "Active",
            pods=[_to_pod_status(pod) for pod in pod_list.items],
            deployments=[_to_deployment_status(deployment) for deployment in deployment_list.items],
            services_count=len(service_list.items),
            hpas=[_to_hpa_status(hpa) for hpa in hpa_list.items],
        )

    def xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_16(self, namespace: str) -> NamespaceOverviewRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            ns = core_api.read_namespace(name=namespace)
        except Exception as exc:
            raise _translate_namespace_error(exc, namespace) from exc

        apps_api = k8s.AppsV1Api()
        autoscaling_api = k8s.AutoscalingV2Api()

        pod_list = core_api.list_namespaced_pod(namespace=namespace)
        deployment_list = apps_api.list_namespaced_deployment(namespace=namespace)
        service_list = core_api.list_namespaced_service(namespace=namespace)
        hpa_list = None

        return NamespaceOverviewRawData(
            namespace_status=ns.status.phase or "Active",
            pods=[_to_pod_status(pod) for pod in pod_list.items],
            deployments=[_to_deployment_status(deployment) for deployment in deployment_list.items],
            services_count=len(service_list.items),
            hpas=[_to_hpa_status(hpa) for hpa in hpa_list.items],
        )

    def xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_17(self, namespace: str) -> NamespaceOverviewRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            ns = core_api.read_namespace(name=namespace)
        except Exception as exc:
            raise _translate_namespace_error(exc, namespace) from exc

        apps_api = k8s.AppsV1Api()
        autoscaling_api = k8s.AutoscalingV2Api()

        pod_list = core_api.list_namespaced_pod(namespace=namespace)
        deployment_list = apps_api.list_namespaced_deployment(namespace=namespace)
        service_list = core_api.list_namespaced_service(namespace=namespace)
        hpa_list = autoscaling_api.list_namespaced_horizontal_pod_autoscaler(namespace=None)

        return NamespaceOverviewRawData(
            namespace_status=ns.status.phase or "Active",
            pods=[_to_pod_status(pod) for pod in pod_list.items],
            deployments=[_to_deployment_status(deployment) for deployment in deployment_list.items],
            services_count=len(service_list.items),
            hpas=[_to_hpa_status(hpa) for hpa in hpa_list.items],
        )

    def xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_18(self, namespace: str) -> NamespaceOverviewRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            ns = core_api.read_namespace(name=namespace)
        except Exception as exc:
            raise _translate_namespace_error(exc, namespace) from exc

        apps_api = k8s.AppsV1Api()
        autoscaling_api = k8s.AutoscalingV2Api()

        pod_list = core_api.list_namespaced_pod(namespace=namespace)
        deployment_list = apps_api.list_namespaced_deployment(namespace=namespace)
        service_list = core_api.list_namespaced_service(namespace=namespace)
        hpa_list = autoscaling_api.list_namespaced_horizontal_pod_autoscaler(namespace=namespace)

        return NamespaceOverviewRawData(
            namespace_status=None,
            pods=[_to_pod_status(pod) for pod in pod_list.items],
            deployments=[_to_deployment_status(deployment) for deployment in deployment_list.items],
            services_count=len(service_list.items),
            hpas=[_to_hpa_status(hpa) for hpa in hpa_list.items],
        )

    def xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_19(self, namespace: str) -> NamespaceOverviewRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            ns = core_api.read_namespace(name=namespace)
        except Exception as exc:
            raise _translate_namespace_error(exc, namespace) from exc

        apps_api = k8s.AppsV1Api()
        autoscaling_api = k8s.AutoscalingV2Api()

        pod_list = core_api.list_namespaced_pod(namespace=namespace)
        deployment_list = apps_api.list_namespaced_deployment(namespace=namespace)
        service_list = core_api.list_namespaced_service(namespace=namespace)
        hpa_list = autoscaling_api.list_namespaced_horizontal_pod_autoscaler(namespace=namespace)

        return NamespaceOverviewRawData(
            namespace_status=ns.status.phase or "Active",
            pods=None,
            deployments=[_to_deployment_status(deployment) for deployment in deployment_list.items],
            services_count=len(service_list.items),
            hpas=[_to_hpa_status(hpa) for hpa in hpa_list.items],
        )

    def xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_20(self, namespace: str) -> NamespaceOverviewRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            ns = core_api.read_namespace(name=namespace)
        except Exception as exc:
            raise _translate_namespace_error(exc, namespace) from exc

        apps_api = k8s.AppsV1Api()
        autoscaling_api = k8s.AutoscalingV2Api()

        pod_list = core_api.list_namespaced_pod(namespace=namespace)
        deployment_list = apps_api.list_namespaced_deployment(namespace=namespace)
        service_list = core_api.list_namespaced_service(namespace=namespace)
        hpa_list = autoscaling_api.list_namespaced_horizontal_pod_autoscaler(namespace=namespace)

        return NamespaceOverviewRawData(
            namespace_status=ns.status.phase or "Active",
            pods=[_to_pod_status(pod) for pod in pod_list.items],
            deployments=None,
            services_count=len(service_list.items),
            hpas=[_to_hpa_status(hpa) for hpa in hpa_list.items],
        )

    def xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_21(self, namespace: str) -> NamespaceOverviewRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            ns = core_api.read_namespace(name=namespace)
        except Exception as exc:
            raise _translate_namespace_error(exc, namespace) from exc

        apps_api = k8s.AppsV1Api()
        autoscaling_api = k8s.AutoscalingV2Api()

        pod_list = core_api.list_namespaced_pod(namespace=namespace)
        deployment_list = apps_api.list_namespaced_deployment(namespace=namespace)
        service_list = core_api.list_namespaced_service(namespace=namespace)
        hpa_list = autoscaling_api.list_namespaced_horizontal_pod_autoscaler(namespace=namespace)

        return NamespaceOverviewRawData(
            namespace_status=ns.status.phase or "Active",
            pods=[_to_pod_status(pod) for pod in pod_list.items],
            deployments=[_to_deployment_status(deployment) for deployment in deployment_list.items],
            services_count=None,
            hpas=[_to_hpa_status(hpa) for hpa in hpa_list.items],
        )

    def xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_22(self, namespace: str) -> NamespaceOverviewRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            ns = core_api.read_namespace(name=namespace)
        except Exception as exc:
            raise _translate_namespace_error(exc, namespace) from exc

        apps_api = k8s.AppsV1Api()
        autoscaling_api = k8s.AutoscalingV2Api()

        pod_list = core_api.list_namespaced_pod(namespace=namespace)
        deployment_list = apps_api.list_namespaced_deployment(namespace=namespace)
        service_list = core_api.list_namespaced_service(namespace=namespace)
        hpa_list = autoscaling_api.list_namespaced_horizontal_pod_autoscaler(namespace=namespace)

        return NamespaceOverviewRawData(
            namespace_status=ns.status.phase or "Active",
            pods=[_to_pod_status(pod) for pod in pod_list.items],
            deployments=[_to_deployment_status(deployment) for deployment in deployment_list.items],
            services_count=len(service_list.items),
            hpas=None,
        )

    def xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_23(self, namespace: str) -> NamespaceOverviewRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            ns = core_api.read_namespace(name=namespace)
        except Exception as exc:
            raise _translate_namespace_error(exc, namespace) from exc

        apps_api = k8s.AppsV1Api()
        autoscaling_api = k8s.AutoscalingV2Api()

        pod_list = core_api.list_namespaced_pod(namespace=namespace)
        deployment_list = apps_api.list_namespaced_deployment(namespace=namespace)
        service_list = core_api.list_namespaced_service(namespace=namespace)
        hpa_list = autoscaling_api.list_namespaced_horizontal_pod_autoscaler(namespace=namespace)

        return NamespaceOverviewRawData(
            pods=[_to_pod_status(pod) for pod in pod_list.items],
            deployments=[_to_deployment_status(deployment) for deployment in deployment_list.items],
            services_count=len(service_list.items),
            hpas=[_to_hpa_status(hpa) for hpa in hpa_list.items],
        )

    def xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_24(self, namespace: str) -> NamespaceOverviewRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            ns = core_api.read_namespace(name=namespace)
        except Exception as exc:
            raise _translate_namespace_error(exc, namespace) from exc

        apps_api = k8s.AppsV1Api()
        autoscaling_api = k8s.AutoscalingV2Api()

        pod_list = core_api.list_namespaced_pod(namespace=namespace)
        deployment_list = apps_api.list_namespaced_deployment(namespace=namespace)
        service_list = core_api.list_namespaced_service(namespace=namespace)
        hpa_list = autoscaling_api.list_namespaced_horizontal_pod_autoscaler(namespace=namespace)

        return NamespaceOverviewRawData(
            namespace_status=ns.status.phase or "Active",
            deployments=[_to_deployment_status(deployment) for deployment in deployment_list.items],
            services_count=len(service_list.items),
            hpas=[_to_hpa_status(hpa) for hpa in hpa_list.items],
        )

    def xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_25(self, namespace: str) -> NamespaceOverviewRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            ns = core_api.read_namespace(name=namespace)
        except Exception as exc:
            raise _translate_namespace_error(exc, namespace) from exc

        apps_api = k8s.AppsV1Api()
        autoscaling_api = k8s.AutoscalingV2Api()

        pod_list = core_api.list_namespaced_pod(namespace=namespace)
        deployment_list = apps_api.list_namespaced_deployment(namespace=namespace)
        service_list = core_api.list_namespaced_service(namespace=namespace)
        hpa_list = autoscaling_api.list_namespaced_horizontal_pod_autoscaler(namespace=namespace)

        return NamespaceOverviewRawData(
            namespace_status=ns.status.phase or "Active",
            pods=[_to_pod_status(pod) for pod in pod_list.items],
            services_count=len(service_list.items),
            hpas=[_to_hpa_status(hpa) for hpa in hpa_list.items],
        )

    def xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_26(self, namespace: str) -> NamespaceOverviewRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            ns = core_api.read_namespace(name=namespace)
        except Exception as exc:
            raise _translate_namespace_error(exc, namespace) from exc

        apps_api = k8s.AppsV1Api()
        autoscaling_api = k8s.AutoscalingV2Api()

        pod_list = core_api.list_namespaced_pod(namespace=namespace)
        deployment_list = apps_api.list_namespaced_deployment(namespace=namespace)
        service_list = core_api.list_namespaced_service(namespace=namespace)
        hpa_list = autoscaling_api.list_namespaced_horizontal_pod_autoscaler(namespace=namespace)

        return NamespaceOverviewRawData(
            namespace_status=ns.status.phase or "Active",
            pods=[_to_pod_status(pod) for pod in pod_list.items],
            deployments=[_to_deployment_status(deployment) for deployment in deployment_list.items],
            hpas=[_to_hpa_status(hpa) for hpa in hpa_list.items],
        )

    def xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_27(self, namespace: str) -> NamespaceOverviewRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            ns = core_api.read_namespace(name=namespace)
        except Exception as exc:
            raise _translate_namespace_error(exc, namespace) from exc

        apps_api = k8s.AppsV1Api()
        autoscaling_api = k8s.AutoscalingV2Api()

        pod_list = core_api.list_namespaced_pod(namespace=namespace)
        deployment_list = apps_api.list_namespaced_deployment(namespace=namespace)
        service_list = core_api.list_namespaced_service(namespace=namespace)
        hpa_list = autoscaling_api.list_namespaced_horizontal_pod_autoscaler(namespace=namespace)

        return NamespaceOverviewRawData(
            namespace_status=ns.status.phase or "Active",
            pods=[_to_pod_status(pod) for pod in pod_list.items],
            deployments=[_to_deployment_status(deployment) for deployment in deployment_list.items],
            services_count=len(service_list.items),
            )

    def xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_28(self, namespace: str) -> NamespaceOverviewRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            ns = core_api.read_namespace(name=namespace)
        except Exception as exc:
            raise _translate_namespace_error(exc, namespace) from exc

        apps_api = k8s.AppsV1Api()
        autoscaling_api = k8s.AutoscalingV2Api()

        pod_list = core_api.list_namespaced_pod(namespace=namespace)
        deployment_list = apps_api.list_namespaced_deployment(namespace=namespace)
        service_list = core_api.list_namespaced_service(namespace=namespace)
        hpa_list = autoscaling_api.list_namespaced_horizontal_pod_autoscaler(namespace=namespace)

        return NamespaceOverviewRawData(
            namespace_status=ns.status.phase and "Active",
            pods=[_to_pod_status(pod) for pod in pod_list.items],
            deployments=[_to_deployment_status(deployment) for deployment in deployment_list.items],
            services_count=len(service_list.items),
            hpas=[_to_hpa_status(hpa) for hpa in hpa_list.items],
        )

    def xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_29(self, namespace: str) -> NamespaceOverviewRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            ns = core_api.read_namespace(name=namespace)
        except Exception as exc:
            raise _translate_namespace_error(exc, namespace) from exc

        apps_api = k8s.AppsV1Api()
        autoscaling_api = k8s.AutoscalingV2Api()

        pod_list = core_api.list_namespaced_pod(namespace=namespace)
        deployment_list = apps_api.list_namespaced_deployment(namespace=namespace)
        service_list = core_api.list_namespaced_service(namespace=namespace)
        hpa_list = autoscaling_api.list_namespaced_horizontal_pod_autoscaler(namespace=namespace)

        return NamespaceOverviewRawData(
            namespace_status=ns.status.phase or "XXActiveXX",
            pods=[_to_pod_status(pod) for pod in pod_list.items],
            deployments=[_to_deployment_status(deployment) for deployment in deployment_list.items],
            services_count=len(service_list.items),
            hpas=[_to_hpa_status(hpa) for hpa in hpa_list.items],
        )

    def xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_30(self, namespace: str) -> NamespaceOverviewRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            ns = core_api.read_namespace(name=namespace)
        except Exception as exc:
            raise _translate_namespace_error(exc, namespace) from exc

        apps_api = k8s.AppsV1Api()
        autoscaling_api = k8s.AutoscalingV2Api()

        pod_list = core_api.list_namespaced_pod(namespace=namespace)
        deployment_list = apps_api.list_namespaced_deployment(namespace=namespace)
        service_list = core_api.list_namespaced_service(namespace=namespace)
        hpa_list = autoscaling_api.list_namespaced_horizontal_pod_autoscaler(namespace=namespace)

        return NamespaceOverviewRawData(
            namespace_status=ns.status.phase or "active",
            pods=[_to_pod_status(pod) for pod in pod_list.items],
            deployments=[_to_deployment_status(deployment) for deployment in deployment_list.items],
            services_count=len(service_list.items),
            hpas=[_to_hpa_status(hpa) for hpa in hpa_list.items],
        )

    def xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_31(self, namespace: str) -> NamespaceOverviewRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            ns = core_api.read_namespace(name=namespace)
        except Exception as exc:
            raise _translate_namespace_error(exc, namespace) from exc

        apps_api = k8s.AppsV1Api()
        autoscaling_api = k8s.AutoscalingV2Api()

        pod_list = core_api.list_namespaced_pod(namespace=namespace)
        deployment_list = apps_api.list_namespaced_deployment(namespace=namespace)
        service_list = core_api.list_namespaced_service(namespace=namespace)
        hpa_list = autoscaling_api.list_namespaced_horizontal_pod_autoscaler(namespace=namespace)

        return NamespaceOverviewRawData(
            namespace_status=ns.status.phase or "ACTIVE",
            pods=[_to_pod_status(pod) for pod in pod_list.items],
            deployments=[_to_deployment_status(deployment) for deployment in deployment_list.items],
            services_count=len(service_list.items),
            hpas=[_to_hpa_status(hpa) for hpa in hpa_list.items],
        )

    def xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_32(self, namespace: str) -> NamespaceOverviewRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            ns = core_api.read_namespace(name=namespace)
        except Exception as exc:
            raise _translate_namespace_error(exc, namespace) from exc

        apps_api = k8s.AppsV1Api()
        autoscaling_api = k8s.AutoscalingV2Api()

        pod_list = core_api.list_namespaced_pod(namespace=namespace)
        deployment_list = apps_api.list_namespaced_deployment(namespace=namespace)
        service_list = core_api.list_namespaced_service(namespace=namespace)
        hpa_list = autoscaling_api.list_namespaced_horizontal_pod_autoscaler(namespace=namespace)

        return NamespaceOverviewRawData(
            namespace_status=ns.status.phase or "Active",
            pods=[_to_pod_status(None) for pod in pod_list.items],
            deployments=[_to_deployment_status(deployment) for deployment in deployment_list.items],
            services_count=len(service_list.items),
            hpas=[_to_hpa_status(hpa) for hpa in hpa_list.items],
        )

    def xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_33(self, namespace: str) -> NamespaceOverviewRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            ns = core_api.read_namespace(name=namespace)
        except Exception as exc:
            raise _translate_namespace_error(exc, namespace) from exc

        apps_api = k8s.AppsV1Api()
        autoscaling_api = k8s.AutoscalingV2Api()

        pod_list = core_api.list_namespaced_pod(namespace=namespace)
        deployment_list = apps_api.list_namespaced_deployment(namespace=namespace)
        service_list = core_api.list_namespaced_service(namespace=namespace)
        hpa_list = autoscaling_api.list_namespaced_horizontal_pod_autoscaler(namespace=namespace)

        return NamespaceOverviewRawData(
            namespace_status=ns.status.phase or "Active",
            pods=[_to_pod_status(pod) for pod in pod_list.items],
            deployments=[_to_deployment_status(None) for deployment in deployment_list.items],
            services_count=len(service_list.items),
            hpas=[_to_hpa_status(hpa) for hpa in hpa_list.items],
        )

    def xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_34(self, namespace: str) -> NamespaceOverviewRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            ns = core_api.read_namespace(name=namespace)
        except Exception as exc:
            raise _translate_namespace_error(exc, namespace) from exc

        apps_api = k8s.AppsV1Api()
        autoscaling_api = k8s.AutoscalingV2Api()

        pod_list = core_api.list_namespaced_pod(namespace=namespace)
        deployment_list = apps_api.list_namespaced_deployment(namespace=namespace)
        service_list = core_api.list_namespaced_service(namespace=namespace)
        hpa_list = autoscaling_api.list_namespaced_horizontal_pod_autoscaler(namespace=namespace)

        return NamespaceOverviewRawData(
            namespace_status=ns.status.phase or "Active",
            pods=[_to_pod_status(pod) for pod in pod_list.items],
            deployments=[_to_deployment_status(deployment) for deployment in deployment_list.items],
            services_count=len(service_list.items),
            hpas=[_to_hpa_status(None) for hpa in hpa_list.items],
        )

mutants_xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut['_mutmut_orig'] = KubernetesNamespaceAdapter.xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut['xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_1'] = KubernetesNamespaceAdapter.xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut['xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_2'] = KubernetesNamespaceAdapter.xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut['xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_3'] = KubernetesNamespaceAdapter.xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut['xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_4'] = KubernetesNamespaceAdapter.xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut['xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_5'] = KubernetesNamespaceAdapter.xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut['xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_6'] = KubernetesNamespaceAdapter.xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut['xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_7'] = KubernetesNamespaceAdapter.xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut['xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_8'] = KubernetesNamespaceAdapter.xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut['xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_9'] = KubernetesNamespaceAdapter.xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut['xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_10'] = KubernetesNamespaceAdapter.xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut['xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_11'] = KubernetesNamespaceAdapter.xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut['xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_12'] = KubernetesNamespaceAdapter.xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut['xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_13'] = KubernetesNamespaceAdapter.xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut['xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_14'] = KubernetesNamespaceAdapter.xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_14 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut['xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_15'] = KubernetesNamespaceAdapter.xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_15 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut['xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_16'] = KubernetesNamespaceAdapter.xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_16 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut['xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_17'] = KubernetesNamespaceAdapter.xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_17 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut['xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_18'] = KubernetesNamespaceAdapter.xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_18 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut['xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_19'] = KubernetesNamespaceAdapter.xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_19 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut['xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_20'] = KubernetesNamespaceAdapter.xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_20 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut['xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_21'] = KubernetesNamespaceAdapter.xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_21 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut['xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_22'] = KubernetesNamespaceAdapter.xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_22 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut['xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_23'] = KubernetesNamespaceAdapter.xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_23 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut['xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_24'] = KubernetesNamespaceAdapter.xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_24 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut['xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_25'] = KubernetesNamespaceAdapter.xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_25 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut['xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_26'] = KubernetesNamespaceAdapter.xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_26 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut['xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_27'] = KubernetesNamespaceAdapter.xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_27 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut['xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_28'] = KubernetesNamespaceAdapter.xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_28 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut['xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_29'] = KubernetesNamespaceAdapter.xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_29 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut['xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_30'] = KubernetesNamespaceAdapter.xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_30 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut['xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_31'] = KubernetesNamespaceAdapter.xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_31 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut['xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_32'] = KubernetesNamespaceAdapter.xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_32 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut['xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_33'] = KubernetesNamespaceAdapter.xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_33 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut['xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_34'] = KubernetesNamespaceAdapter.xǁKubernetesNamespaceAdapterǁget_namespace_overview_data__mutmut_34 # type: ignore # mutmut generated
mutants_x__to_pod_status__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_pod_status__mutmut)
def _to_pod_status(pod: V1Pod) -> PodStatusRaw:
    return PodStatusRaw(name=pod.metadata.name, status=_pod_status(pod))


def x__to_pod_status__mutmut_orig(pod: V1Pod) -> PodStatusRaw:
    return PodStatusRaw(name=pod.metadata.name, status=_pod_status(pod))


def x__to_pod_status__mutmut_1(pod: V1Pod) -> PodStatusRaw:
    return PodStatusRaw(name=None, status=_pod_status(pod))


def x__to_pod_status__mutmut_2(pod: V1Pod) -> PodStatusRaw:
    return PodStatusRaw(name=pod.metadata.name, status=None)


def x__to_pod_status__mutmut_3(pod: V1Pod) -> PodStatusRaw:
    return PodStatusRaw(status=_pod_status(pod))


def x__to_pod_status__mutmut_4(pod: V1Pod) -> PodStatusRaw:
    return PodStatusRaw(name=pod.metadata.name, )


def x__to_pod_status__mutmut_5(pod: V1Pod) -> PodStatusRaw:
    return PodStatusRaw(name=pod.metadata.name, status=_pod_status(None))

mutants_x__to_pod_status__mutmut['_mutmut_orig'] = x__to_pod_status__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_pod_status__mutmut['x__to_pod_status__mutmut_1'] = x__to_pod_status__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_pod_status__mutmut['x__to_pod_status__mutmut_2'] = x__to_pod_status__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_pod_status__mutmut['x__to_pod_status__mutmut_3'] = x__to_pod_status__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_pod_status__mutmut['x__to_pod_status__mutmut_4'] = x__to_pod_status__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_pod_status__mutmut['x__to_pod_status__mutmut_5'] = x__to_pod_status__mutmut_5 # type: ignore # mutmut generated
mutants_x__pod_status__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__pod_status__mutmut)
def _pod_status(pod: V1Pod) -> str:
    waiting_reason = _waiting_reason(pod)
    return waiting_reason or (pod.status.phase or "Unknown")


def x__pod_status__mutmut_orig(pod: V1Pod) -> str:
    waiting_reason = _waiting_reason(pod)
    return waiting_reason or (pod.status.phase or "Unknown")


def x__pod_status__mutmut_1(pod: V1Pod) -> str:
    waiting_reason = None
    return waiting_reason or (pod.status.phase or "Unknown")


def x__pod_status__mutmut_2(pod: V1Pod) -> str:
    waiting_reason = _waiting_reason(None)
    return waiting_reason or (pod.status.phase or "Unknown")


def x__pod_status__mutmut_3(pod: V1Pod) -> str:
    waiting_reason = _waiting_reason(pod)
    return waiting_reason and (pod.status.phase or "Unknown")


def x__pod_status__mutmut_4(pod: V1Pod) -> str:
    waiting_reason = _waiting_reason(pod)
    return waiting_reason or (pod.status.phase and "Unknown")


def x__pod_status__mutmut_5(pod: V1Pod) -> str:
    waiting_reason = _waiting_reason(pod)
    return waiting_reason or (pod.status.phase or "XXUnknownXX")


def x__pod_status__mutmut_6(pod: V1Pod) -> str:
    waiting_reason = _waiting_reason(pod)
    return waiting_reason or (pod.status.phase or "unknown")


def x__pod_status__mutmut_7(pod: V1Pod) -> str:
    waiting_reason = _waiting_reason(pod)
    return waiting_reason or (pod.status.phase or "UNKNOWN")

mutants_x__pod_status__mutmut['_mutmut_orig'] = x__pod_status__mutmut_orig # type: ignore # mutmut generated
mutants_x__pod_status__mutmut['x__pod_status__mutmut_1'] = x__pod_status__mutmut_1 # type: ignore # mutmut generated
mutants_x__pod_status__mutmut['x__pod_status__mutmut_2'] = x__pod_status__mutmut_2 # type: ignore # mutmut generated
mutants_x__pod_status__mutmut['x__pod_status__mutmut_3'] = x__pod_status__mutmut_3 # type: ignore # mutmut generated
mutants_x__pod_status__mutmut['x__pod_status__mutmut_4'] = x__pod_status__mutmut_4 # type: ignore # mutmut generated
mutants_x__pod_status__mutmut['x__pod_status__mutmut_5'] = x__pod_status__mutmut_5 # type: ignore # mutmut generated
mutants_x__pod_status__mutmut['x__pod_status__mutmut_6'] = x__pod_status__mutmut_6 # type: ignore # mutmut generated
mutants_x__pod_status__mutmut['x__pod_status__mutmut_7'] = x__pod_status__mutmut_7 # type: ignore # mutmut generated
mutants_x__waiting_reason__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__waiting_reason__mutmut)
def _waiting_reason(pod: V1Pod) -> str | None:
    for container_status in pod.status.container_statuses or []:
        waiting = container_status.state.waiting
        reason = getattr(waiting, "reason", None) if waiting else None
        if reason:
            return str(reason)
    return None


def x__waiting_reason__mutmut_orig(pod: V1Pod) -> str | None:
    for container_status in pod.status.container_statuses or []:
        waiting = container_status.state.waiting
        reason = getattr(waiting, "reason", None) if waiting else None
        if reason:
            return str(reason)
    return None


def x__waiting_reason__mutmut_1(pod: V1Pod) -> str | None:
    for container_status in pod.status.container_statuses and []:
        waiting = container_status.state.waiting
        reason = getattr(waiting, "reason", None) if waiting else None
        if reason:
            return str(reason)
    return None


def x__waiting_reason__mutmut_2(pod: V1Pod) -> str | None:
    for container_status in pod.status.container_statuses or []:
        waiting = None
        reason = getattr(waiting, "reason", None) if waiting else None
        if reason:
            return str(reason)
    return None


def x__waiting_reason__mutmut_3(pod: V1Pod) -> str | None:
    for container_status in pod.status.container_statuses or []:
        waiting = container_status.state.waiting
        reason = None
        if reason:
            return str(reason)
    return None


def x__waiting_reason__mutmut_4(pod: V1Pod) -> str | None:
    for container_status in pod.status.container_statuses or []:
        waiting = container_status.state.waiting
        reason = getattr(None, "reason", None) if waiting else None
        if reason:
            return str(reason)
    return None


def x__waiting_reason__mutmut_5(pod: V1Pod) -> str | None:
    for container_status in pod.status.container_statuses or []:
        waiting = container_status.state.waiting
        reason = getattr(waiting, None, None) if waiting else None
        if reason:
            return str(reason)
    return None


def x__waiting_reason__mutmut_6(pod: V1Pod) -> str | None:
    for container_status in pod.status.container_statuses or []:
        waiting = container_status.state.waiting
        reason = getattr("reason", None) if waiting else None
        if reason:
            return str(reason)
    return None


def x__waiting_reason__mutmut_7(pod: V1Pod) -> str | None:
    for container_status in pod.status.container_statuses or []:
        waiting = container_status.state.waiting
        reason = getattr(waiting, None) if waiting else None
        if reason:
            return str(reason)
    return None


def x__waiting_reason__mutmut_8(pod: V1Pod) -> str | None:
    for container_status in pod.status.container_statuses or []:
        waiting = container_status.state.waiting
        reason = getattr(waiting, "reason", ) if waiting else None
        if reason:
            return str(reason)
    return None


def x__waiting_reason__mutmut_9(pod: V1Pod) -> str | None:
    for container_status in pod.status.container_statuses or []:
        waiting = container_status.state.waiting
        reason = getattr(waiting, "XXreasonXX", None) if waiting else None
        if reason:
            return str(reason)
    return None


def x__waiting_reason__mutmut_10(pod: V1Pod) -> str | None:
    for container_status in pod.status.container_statuses or []:
        waiting = container_status.state.waiting
        reason = getattr(waiting, "REASON", None) if waiting else None
        if reason:
            return str(reason)
    return None


def x__waiting_reason__mutmut_11(pod: V1Pod) -> str | None:
    for container_status in pod.status.container_statuses or []:
        waiting = container_status.state.waiting
        reason = getattr(waiting, "reason", None) if waiting else None
        if reason:
            return str(None)
    return None

mutants_x__waiting_reason__mutmut['_mutmut_orig'] = x__waiting_reason__mutmut_orig # type: ignore # mutmut generated
mutants_x__waiting_reason__mutmut['x__waiting_reason__mutmut_1'] = x__waiting_reason__mutmut_1 # type: ignore # mutmut generated
mutants_x__waiting_reason__mutmut['x__waiting_reason__mutmut_2'] = x__waiting_reason__mutmut_2 # type: ignore # mutmut generated
mutants_x__waiting_reason__mutmut['x__waiting_reason__mutmut_3'] = x__waiting_reason__mutmut_3 # type: ignore # mutmut generated
mutants_x__waiting_reason__mutmut['x__waiting_reason__mutmut_4'] = x__waiting_reason__mutmut_4 # type: ignore # mutmut generated
mutants_x__waiting_reason__mutmut['x__waiting_reason__mutmut_5'] = x__waiting_reason__mutmut_5 # type: ignore # mutmut generated
mutants_x__waiting_reason__mutmut['x__waiting_reason__mutmut_6'] = x__waiting_reason__mutmut_6 # type: ignore # mutmut generated
mutants_x__waiting_reason__mutmut['x__waiting_reason__mutmut_7'] = x__waiting_reason__mutmut_7 # type: ignore # mutmut generated
mutants_x__waiting_reason__mutmut['x__waiting_reason__mutmut_8'] = x__waiting_reason__mutmut_8 # type: ignore # mutmut generated
mutants_x__waiting_reason__mutmut['x__waiting_reason__mutmut_9'] = x__waiting_reason__mutmut_9 # type: ignore # mutmut generated
mutants_x__waiting_reason__mutmut['x__waiting_reason__mutmut_10'] = x__waiting_reason__mutmut_10 # type: ignore # mutmut generated
mutants_x__waiting_reason__mutmut['x__waiting_reason__mutmut_11'] = x__waiting_reason__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_deployment_status__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_deployment_status__mutmut)
def _to_deployment_status(deployment: V1Deployment) -> DeploymentStatusRaw:
    return DeploymentStatusRaw(
        name=deployment.metadata.name,
        ready_replicas=deployment.status.ready_replicas or 0,
        desired_replicas=deployment.spec.replicas or 0,
    )


def x__to_deployment_status__mutmut_orig(deployment: V1Deployment) -> DeploymentStatusRaw:
    return DeploymentStatusRaw(
        name=deployment.metadata.name,
        ready_replicas=deployment.status.ready_replicas or 0,
        desired_replicas=deployment.spec.replicas or 0,
    )


def x__to_deployment_status__mutmut_1(deployment: V1Deployment) -> DeploymentStatusRaw:
    return DeploymentStatusRaw(
        name=None,
        ready_replicas=deployment.status.ready_replicas or 0,
        desired_replicas=deployment.spec.replicas or 0,
    )


def x__to_deployment_status__mutmut_2(deployment: V1Deployment) -> DeploymentStatusRaw:
    return DeploymentStatusRaw(
        name=deployment.metadata.name,
        ready_replicas=None,
        desired_replicas=deployment.spec.replicas or 0,
    )


def x__to_deployment_status__mutmut_3(deployment: V1Deployment) -> DeploymentStatusRaw:
    return DeploymentStatusRaw(
        name=deployment.metadata.name,
        ready_replicas=deployment.status.ready_replicas or 0,
        desired_replicas=None,
    )


def x__to_deployment_status__mutmut_4(deployment: V1Deployment) -> DeploymentStatusRaw:
    return DeploymentStatusRaw(
        ready_replicas=deployment.status.ready_replicas or 0,
        desired_replicas=deployment.spec.replicas or 0,
    )


def x__to_deployment_status__mutmut_5(deployment: V1Deployment) -> DeploymentStatusRaw:
    return DeploymentStatusRaw(
        name=deployment.metadata.name,
        desired_replicas=deployment.spec.replicas or 0,
    )


def x__to_deployment_status__mutmut_6(deployment: V1Deployment) -> DeploymentStatusRaw:
    return DeploymentStatusRaw(
        name=deployment.metadata.name,
        ready_replicas=deployment.status.ready_replicas or 0,
        )


def x__to_deployment_status__mutmut_7(deployment: V1Deployment) -> DeploymentStatusRaw:
    return DeploymentStatusRaw(
        name=deployment.metadata.name,
        ready_replicas=deployment.status.ready_replicas and 0,
        desired_replicas=deployment.spec.replicas or 0,
    )


def x__to_deployment_status__mutmut_8(deployment: V1Deployment) -> DeploymentStatusRaw:
    return DeploymentStatusRaw(
        name=deployment.metadata.name,
        ready_replicas=deployment.status.ready_replicas or 1,
        desired_replicas=deployment.spec.replicas or 0,
    )


def x__to_deployment_status__mutmut_9(deployment: V1Deployment) -> DeploymentStatusRaw:
    return DeploymentStatusRaw(
        name=deployment.metadata.name,
        ready_replicas=deployment.status.ready_replicas or 0,
        desired_replicas=deployment.spec.replicas and 0,
    )


def x__to_deployment_status__mutmut_10(deployment: V1Deployment) -> DeploymentStatusRaw:
    return DeploymentStatusRaw(
        name=deployment.metadata.name,
        ready_replicas=deployment.status.ready_replicas or 0,
        desired_replicas=deployment.spec.replicas or 1,
    )

mutants_x__to_deployment_status__mutmut['_mutmut_orig'] = x__to_deployment_status__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_deployment_status__mutmut['x__to_deployment_status__mutmut_1'] = x__to_deployment_status__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_deployment_status__mutmut['x__to_deployment_status__mutmut_2'] = x__to_deployment_status__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_deployment_status__mutmut['x__to_deployment_status__mutmut_3'] = x__to_deployment_status__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_deployment_status__mutmut['x__to_deployment_status__mutmut_4'] = x__to_deployment_status__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_deployment_status__mutmut['x__to_deployment_status__mutmut_5'] = x__to_deployment_status__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_deployment_status__mutmut['x__to_deployment_status__mutmut_6'] = x__to_deployment_status__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_deployment_status__mutmut['x__to_deployment_status__mutmut_7'] = x__to_deployment_status__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_deployment_status__mutmut['x__to_deployment_status__mutmut_8'] = x__to_deployment_status__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_deployment_status__mutmut['x__to_deployment_status__mutmut_9'] = x__to_deployment_status__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_deployment_status__mutmut['x__to_deployment_status__mutmut_10'] = x__to_deployment_status__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_hpa_status__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_hpa_status__mutmut)
def _to_hpa_status(hpa: V1HorizontalPodAutoscaler) -> HpaStatusRaw:
    return HpaStatusRaw(
        name=hpa.metadata.name,
        current_replicas=hpa.status.current_replicas or 0,
        max_replicas=hpa.spec.max_replicas or 0,
    )


def x__to_hpa_status__mutmut_orig(hpa: V1HorizontalPodAutoscaler) -> HpaStatusRaw:
    return HpaStatusRaw(
        name=hpa.metadata.name,
        current_replicas=hpa.status.current_replicas or 0,
        max_replicas=hpa.spec.max_replicas or 0,
    )


def x__to_hpa_status__mutmut_1(hpa: V1HorizontalPodAutoscaler) -> HpaStatusRaw:
    return HpaStatusRaw(
        name=None,
        current_replicas=hpa.status.current_replicas or 0,
        max_replicas=hpa.spec.max_replicas or 0,
    )


def x__to_hpa_status__mutmut_2(hpa: V1HorizontalPodAutoscaler) -> HpaStatusRaw:
    return HpaStatusRaw(
        name=hpa.metadata.name,
        current_replicas=None,
        max_replicas=hpa.spec.max_replicas or 0,
    )


def x__to_hpa_status__mutmut_3(hpa: V1HorizontalPodAutoscaler) -> HpaStatusRaw:
    return HpaStatusRaw(
        name=hpa.metadata.name,
        current_replicas=hpa.status.current_replicas or 0,
        max_replicas=None,
    )


def x__to_hpa_status__mutmut_4(hpa: V1HorizontalPodAutoscaler) -> HpaStatusRaw:
    return HpaStatusRaw(
        current_replicas=hpa.status.current_replicas or 0,
        max_replicas=hpa.spec.max_replicas or 0,
    )


def x__to_hpa_status__mutmut_5(hpa: V1HorizontalPodAutoscaler) -> HpaStatusRaw:
    return HpaStatusRaw(
        name=hpa.metadata.name,
        max_replicas=hpa.spec.max_replicas or 0,
    )


def x__to_hpa_status__mutmut_6(hpa: V1HorizontalPodAutoscaler) -> HpaStatusRaw:
    return HpaStatusRaw(
        name=hpa.metadata.name,
        current_replicas=hpa.status.current_replicas or 0,
        )


def x__to_hpa_status__mutmut_7(hpa: V1HorizontalPodAutoscaler) -> HpaStatusRaw:
    return HpaStatusRaw(
        name=hpa.metadata.name,
        current_replicas=hpa.status.current_replicas and 0,
        max_replicas=hpa.spec.max_replicas or 0,
    )


def x__to_hpa_status__mutmut_8(hpa: V1HorizontalPodAutoscaler) -> HpaStatusRaw:
    return HpaStatusRaw(
        name=hpa.metadata.name,
        current_replicas=hpa.status.current_replicas or 1,
        max_replicas=hpa.spec.max_replicas or 0,
    )


def x__to_hpa_status__mutmut_9(hpa: V1HorizontalPodAutoscaler) -> HpaStatusRaw:
    return HpaStatusRaw(
        name=hpa.metadata.name,
        current_replicas=hpa.status.current_replicas or 0,
        max_replicas=hpa.spec.max_replicas and 0,
    )


def x__to_hpa_status__mutmut_10(hpa: V1HorizontalPodAutoscaler) -> HpaStatusRaw:
    return HpaStatusRaw(
        name=hpa.metadata.name,
        current_replicas=hpa.status.current_replicas or 0,
        max_replicas=hpa.spec.max_replicas or 1,
    )

mutants_x__to_hpa_status__mutmut['_mutmut_orig'] = x__to_hpa_status__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_hpa_status__mutmut['x__to_hpa_status__mutmut_1'] = x__to_hpa_status__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_hpa_status__mutmut['x__to_hpa_status__mutmut_2'] = x__to_hpa_status__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_hpa_status__mutmut['x__to_hpa_status__mutmut_3'] = x__to_hpa_status__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_hpa_status__mutmut['x__to_hpa_status__mutmut_4'] = x__to_hpa_status__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_hpa_status__mutmut['x__to_hpa_status__mutmut_5'] = x__to_hpa_status__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_hpa_status__mutmut['x__to_hpa_status__mutmut_6'] = x__to_hpa_status__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_hpa_status__mutmut['x__to_hpa_status__mutmut_7'] = x__to_hpa_status__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_hpa_status__mutmut['x__to_hpa_status__mutmut_8'] = x__to_hpa_status__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_hpa_status__mutmut['x__to_hpa_status__mutmut_9'] = x__to_hpa_status__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_hpa_status__mutmut['x__to_hpa_status__mutmut_10'] = x__to_hpa_status__mutmut_10 # type: ignore # mutmut generated
mutants_x__translate_namespace_error__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__translate_namespace_error__mutmut)
def _translate_namespace_error(exc: Exception, namespace: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {namespace!r} not found", context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot read namespace {namespace!r}: {exc}")


def x__translate_namespace_error__mutmut_orig(exc: Exception, namespace: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {namespace!r} not found", context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot read namespace {namespace!r}: {exc}")


def x__translate_namespace_error__mutmut_1(exc: Exception, namespace: str) -> Exception:
    status = None
    context = {"namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {namespace!r} not found", context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot read namespace {namespace!r}: {exc}")


def x__translate_namespace_error__mutmut_2(exc: Exception, namespace: str) -> Exception:
    status = getattr(None, "status", None)
    context = {"namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {namespace!r} not found", context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot read namespace {namespace!r}: {exc}")


def x__translate_namespace_error__mutmut_3(exc: Exception, namespace: str) -> Exception:
    status = getattr(exc, None, None)
    context = {"namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {namespace!r} not found", context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot read namespace {namespace!r}: {exc}")


def x__translate_namespace_error__mutmut_4(exc: Exception, namespace: str) -> Exception:
    status = getattr("status", None)
    context = {"namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {namespace!r} not found", context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot read namespace {namespace!r}: {exc}")


def x__translate_namespace_error__mutmut_5(exc: Exception, namespace: str) -> Exception:
    status = getattr(exc, None)
    context = {"namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {namespace!r} not found", context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot read namespace {namespace!r}: {exc}")


def x__translate_namespace_error__mutmut_6(exc: Exception, namespace: str) -> Exception:
    status = getattr(exc, "status", )
    context = {"namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {namespace!r} not found", context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot read namespace {namespace!r}: {exc}")


def x__translate_namespace_error__mutmut_7(exc: Exception, namespace: str) -> Exception:
    status = getattr(exc, "XXstatusXX", None)
    context = {"namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {namespace!r} not found", context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot read namespace {namespace!r}: {exc}")


def x__translate_namespace_error__mutmut_8(exc: Exception, namespace: str) -> Exception:
    status = getattr(exc, "STATUS", None)
    context = {"namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {namespace!r} not found", context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot read namespace {namespace!r}: {exc}")


def x__translate_namespace_error__mutmut_9(exc: Exception, namespace: str) -> Exception:
    status = getattr(exc, "status", None)
    context = None
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {namespace!r} not found", context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot read namespace {namespace!r}: {exc}")


def x__translate_namespace_error__mutmut_10(exc: Exception, namespace: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"XXnamespaceXX": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {namespace!r} not found", context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot read namespace {namespace!r}: {exc}")


def x__translate_namespace_error__mutmut_11(exc: Exception, namespace: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"NAMESPACE": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {namespace!r} not found", context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot read namespace {namespace!r}: {exc}")


def x__translate_namespace_error__mutmut_12(exc: Exception, namespace: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": namespace}
    if status != _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {namespace!r} not found", context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot read namespace {namespace!r}: {exc}")


def x__translate_namespace_error__mutmut_13(exc: Exception, namespace: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(None, context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot read namespace {namespace!r}: {exc}")


def x__translate_namespace_error__mutmut_14(exc: Exception, namespace: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {namespace!r} not found", context=None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot read namespace {namespace!r}: {exc}")


def x__translate_namespace_error__mutmut_15(exc: Exception, namespace: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot read namespace {namespace!r}: {exc}")


def x__translate_namespace_error__mutmut_16(exc: Exception, namespace: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {namespace!r} not found", )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot read namespace {namespace!r}: {exc}")


def x__translate_namespace_error__mutmut_17(exc: Exception, namespace: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {namespace!r} not found", context=context)
    if status != _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot read namespace {namespace!r}: {exc}")


def x__translate_namespace_error__mutmut_18(exc: Exception, namespace: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {namespace!r} not found", context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            None, context=context
        )
    return ClusterUnreachableError(f"Cannot read namespace {namespace!r}: {exc}")


def x__translate_namespace_error__mutmut_19(exc: Exception, namespace: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {namespace!r} not found", context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to namespace {namespace!r}", context=None
        )
    return ClusterUnreachableError(f"Cannot read namespace {namespace!r}: {exc}")


def x__translate_namespace_error__mutmut_20(exc: Exception, namespace: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {namespace!r} not found", context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            context=context
        )
    return ClusterUnreachableError(f"Cannot read namespace {namespace!r}: {exc}")


def x__translate_namespace_error__mutmut_21(exc: Exception, namespace: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {namespace!r} not found", context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to namespace {namespace!r}", )
    return ClusterUnreachableError(f"Cannot read namespace {namespace!r}: {exc}")


def x__translate_namespace_error__mutmut_22(exc: Exception, namespace: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {namespace!r} not found", context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(None)

mutants_x__translate_namespace_error__mutmut['_mutmut_orig'] = x__translate_namespace_error__mutmut_orig # type: ignore # mutmut generated
mutants_x__translate_namespace_error__mutmut['x__translate_namespace_error__mutmut_1'] = x__translate_namespace_error__mutmut_1 # type: ignore # mutmut generated
mutants_x__translate_namespace_error__mutmut['x__translate_namespace_error__mutmut_2'] = x__translate_namespace_error__mutmut_2 # type: ignore # mutmut generated
mutants_x__translate_namespace_error__mutmut['x__translate_namespace_error__mutmut_3'] = x__translate_namespace_error__mutmut_3 # type: ignore # mutmut generated
mutants_x__translate_namespace_error__mutmut['x__translate_namespace_error__mutmut_4'] = x__translate_namespace_error__mutmut_4 # type: ignore # mutmut generated
mutants_x__translate_namespace_error__mutmut['x__translate_namespace_error__mutmut_5'] = x__translate_namespace_error__mutmut_5 # type: ignore # mutmut generated
mutants_x__translate_namespace_error__mutmut['x__translate_namespace_error__mutmut_6'] = x__translate_namespace_error__mutmut_6 # type: ignore # mutmut generated
mutants_x__translate_namespace_error__mutmut['x__translate_namespace_error__mutmut_7'] = x__translate_namespace_error__mutmut_7 # type: ignore # mutmut generated
mutants_x__translate_namespace_error__mutmut['x__translate_namespace_error__mutmut_8'] = x__translate_namespace_error__mutmut_8 # type: ignore # mutmut generated
mutants_x__translate_namespace_error__mutmut['x__translate_namespace_error__mutmut_9'] = x__translate_namespace_error__mutmut_9 # type: ignore # mutmut generated
mutants_x__translate_namespace_error__mutmut['x__translate_namespace_error__mutmut_10'] = x__translate_namespace_error__mutmut_10 # type: ignore # mutmut generated
mutants_x__translate_namespace_error__mutmut['x__translate_namespace_error__mutmut_11'] = x__translate_namespace_error__mutmut_11 # type: ignore # mutmut generated
mutants_x__translate_namespace_error__mutmut['x__translate_namespace_error__mutmut_12'] = x__translate_namespace_error__mutmut_12 # type: ignore # mutmut generated
mutants_x__translate_namespace_error__mutmut['x__translate_namespace_error__mutmut_13'] = x__translate_namespace_error__mutmut_13 # type: ignore # mutmut generated
mutants_x__translate_namespace_error__mutmut['x__translate_namespace_error__mutmut_14'] = x__translate_namespace_error__mutmut_14 # type: ignore # mutmut generated
mutants_x__translate_namespace_error__mutmut['x__translate_namespace_error__mutmut_15'] = x__translate_namespace_error__mutmut_15 # type: ignore # mutmut generated
mutants_x__translate_namespace_error__mutmut['x__translate_namespace_error__mutmut_16'] = x__translate_namespace_error__mutmut_16 # type: ignore # mutmut generated
mutants_x__translate_namespace_error__mutmut['x__translate_namespace_error__mutmut_17'] = x__translate_namespace_error__mutmut_17 # type: ignore # mutmut generated
mutants_x__translate_namespace_error__mutmut['x__translate_namespace_error__mutmut_18'] = x__translate_namespace_error__mutmut_18 # type: ignore # mutmut generated
mutants_x__translate_namespace_error__mutmut['x__translate_namespace_error__mutmut_19'] = x__translate_namespace_error__mutmut_19 # type: ignore # mutmut generated
mutants_x__translate_namespace_error__mutmut['x__translate_namespace_error__mutmut_20'] = x__translate_namespace_error__mutmut_20 # type: ignore # mutmut generated
mutants_x__translate_namespace_error__mutmut['x__translate_namespace_error__mutmut_21'] = x__translate_namespace_error__mutmut_21 # type: ignore # mutmut generated
mutants_x__translate_namespace_error__mutmut['x__translate_namespace_error__mutmut_22'] = x__translate_namespace_error__mutmut_22 # type: ignore # mutmut generated
