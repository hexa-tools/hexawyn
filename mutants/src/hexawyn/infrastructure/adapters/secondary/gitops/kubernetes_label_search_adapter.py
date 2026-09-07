from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driven.resource_search_port import (
    MatchedResourceRaw,
    ResourceSearchPort,
)

if TYPE_CHECKING:
    from kubernetes.client import V1ConfigMap, V1Deployment, V1Pod, V1Service


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁKubernetesLabelSearchAdapterǁsearch_pods__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut: MutantDict = {}  # type: ignore


class KubernetesLabelSearchAdapter(ResourceSearchPort):
    """Secondary adapter — searches pods/deployments/services/configmaps by
    label selector, one `kubernetes` client call per resource kind."""

    @_mutmut_mutated(mutants_xǁKubernetesLabelSearchAdapterǁsearch_pods__mutmut)
    def search_pods(self, label_selector: str, namespace: str | None) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            pod_list = core_api.list_namespaced_pod(
                namespace=namespace, label_selector=label_selector
            )
        else:
            pod_list = core_api.list_pod_for_all_namespaces(label_selector=label_selector)
        return [_to_pod_raw(item) for item in pod_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_pods__mutmut_orig(self, label_selector: str, namespace: str | None) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            pod_list = core_api.list_namespaced_pod(
                namespace=namespace, label_selector=label_selector
            )
        else:
            pod_list = core_api.list_pod_for_all_namespaces(label_selector=label_selector)
        return [_to_pod_raw(item) for item in pod_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_pods__mutmut_1(self, label_selector: str, namespace: str | None) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = None
        if namespace:
            pod_list = core_api.list_namespaced_pod(
                namespace=namespace, label_selector=label_selector
            )
        else:
            pod_list = core_api.list_pod_for_all_namespaces(label_selector=label_selector)
        return [_to_pod_raw(item) for item in pod_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_pods__mutmut_2(self, label_selector: str, namespace: str | None) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            pod_list = None
        else:
            pod_list = core_api.list_pod_for_all_namespaces(label_selector=label_selector)
        return [_to_pod_raw(item) for item in pod_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_pods__mutmut_3(self, label_selector: str, namespace: str | None) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            pod_list = core_api.list_namespaced_pod(
                namespace=None, label_selector=label_selector
            )
        else:
            pod_list = core_api.list_pod_for_all_namespaces(label_selector=label_selector)
        return [_to_pod_raw(item) for item in pod_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_pods__mutmut_4(self, label_selector: str, namespace: str | None) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            pod_list = core_api.list_namespaced_pod(
                namespace=namespace, label_selector=None
            )
        else:
            pod_list = core_api.list_pod_for_all_namespaces(label_selector=label_selector)
        return [_to_pod_raw(item) for item in pod_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_pods__mutmut_5(self, label_selector: str, namespace: str | None) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            pod_list = core_api.list_namespaced_pod(
                label_selector=label_selector
            )
        else:
            pod_list = core_api.list_pod_for_all_namespaces(label_selector=label_selector)
        return [_to_pod_raw(item) for item in pod_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_pods__mutmut_6(self, label_selector: str, namespace: str | None) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            pod_list = core_api.list_namespaced_pod(
                namespace=namespace, )
        else:
            pod_list = core_api.list_pod_for_all_namespaces(label_selector=label_selector)
        return [_to_pod_raw(item) for item in pod_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_pods__mutmut_7(self, label_selector: str, namespace: str | None) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            pod_list = core_api.list_namespaced_pod(
                namespace=namespace, label_selector=label_selector
            )
        else:
            pod_list = None
        return [_to_pod_raw(item) for item in pod_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_pods__mutmut_8(self, label_selector: str, namespace: str | None) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            pod_list = core_api.list_namespaced_pod(
                namespace=namespace, label_selector=label_selector
            )
        else:
            pod_list = core_api.list_pod_for_all_namespaces(label_selector=None)
        return [_to_pod_raw(item) for item in pod_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_pods__mutmut_9(self, label_selector: str, namespace: str | None) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            pod_list = core_api.list_namespaced_pod(
                namespace=namespace, label_selector=label_selector
            )
        else:
            pod_list = core_api.list_pod_for_all_namespaces(label_selector=label_selector)
        return [_to_pod_raw(None) for item in pod_list.items]

    @_mutmut_mutated(mutants_xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut)
    def search_deployments(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        if namespace:
            deployment_list = apps_api.list_namespaced_deployment(
                namespace=namespace, label_selector=label_selector
            )
        else:
            deployment_list = apps_api.list_deployment_for_all_namespaces(
                label_selector=label_selector
            )
        return [_to_non_pod_raw(item, kind="deployment") for item in deployment_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_orig(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        if namespace:
            deployment_list = apps_api.list_namespaced_deployment(
                namespace=namespace, label_selector=label_selector
            )
        else:
            deployment_list = apps_api.list_deployment_for_all_namespaces(
                label_selector=label_selector
            )
        return [_to_non_pod_raw(item, kind="deployment") for item in deployment_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_1(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        apps_api = None
        if namespace:
            deployment_list = apps_api.list_namespaced_deployment(
                namespace=namespace, label_selector=label_selector
            )
        else:
            deployment_list = apps_api.list_deployment_for_all_namespaces(
                label_selector=label_selector
            )
        return [_to_non_pod_raw(item, kind="deployment") for item in deployment_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_2(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        if namespace:
            deployment_list = None
        else:
            deployment_list = apps_api.list_deployment_for_all_namespaces(
                label_selector=label_selector
            )
        return [_to_non_pod_raw(item, kind="deployment") for item in deployment_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_3(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        if namespace:
            deployment_list = apps_api.list_namespaced_deployment(
                namespace=None, label_selector=label_selector
            )
        else:
            deployment_list = apps_api.list_deployment_for_all_namespaces(
                label_selector=label_selector
            )
        return [_to_non_pod_raw(item, kind="deployment") for item in deployment_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_4(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        if namespace:
            deployment_list = apps_api.list_namespaced_deployment(
                namespace=namespace, label_selector=None
            )
        else:
            deployment_list = apps_api.list_deployment_for_all_namespaces(
                label_selector=label_selector
            )
        return [_to_non_pod_raw(item, kind="deployment") for item in deployment_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_5(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        if namespace:
            deployment_list = apps_api.list_namespaced_deployment(
                label_selector=label_selector
            )
        else:
            deployment_list = apps_api.list_deployment_for_all_namespaces(
                label_selector=label_selector
            )
        return [_to_non_pod_raw(item, kind="deployment") for item in deployment_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_6(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        if namespace:
            deployment_list = apps_api.list_namespaced_deployment(
                namespace=namespace, )
        else:
            deployment_list = apps_api.list_deployment_for_all_namespaces(
                label_selector=label_selector
            )
        return [_to_non_pod_raw(item, kind="deployment") for item in deployment_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_7(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        if namespace:
            deployment_list = apps_api.list_namespaced_deployment(
                namespace=namespace, label_selector=label_selector
            )
        else:
            deployment_list = None
        return [_to_non_pod_raw(item, kind="deployment") for item in deployment_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_8(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        if namespace:
            deployment_list = apps_api.list_namespaced_deployment(
                namespace=namespace, label_selector=label_selector
            )
        else:
            deployment_list = apps_api.list_deployment_for_all_namespaces(
                label_selector=None
            )
        return [_to_non_pod_raw(item, kind="deployment") for item in deployment_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_9(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        if namespace:
            deployment_list = apps_api.list_namespaced_deployment(
                namespace=namespace, label_selector=label_selector
            )
        else:
            deployment_list = apps_api.list_deployment_for_all_namespaces(
                label_selector=label_selector
            )
        return [_to_non_pod_raw(None, kind="deployment") for item in deployment_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_10(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        if namespace:
            deployment_list = apps_api.list_namespaced_deployment(
                namespace=namespace, label_selector=label_selector
            )
        else:
            deployment_list = apps_api.list_deployment_for_all_namespaces(
                label_selector=label_selector
            )
        return [_to_non_pod_raw(item, kind=None) for item in deployment_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_11(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        if namespace:
            deployment_list = apps_api.list_namespaced_deployment(
                namespace=namespace, label_selector=label_selector
            )
        else:
            deployment_list = apps_api.list_deployment_for_all_namespaces(
                label_selector=label_selector
            )
        return [_to_non_pod_raw(kind="deployment") for item in deployment_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_12(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        if namespace:
            deployment_list = apps_api.list_namespaced_deployment(
                namespace=namespace, label_selector=label_selector
            )
        else:
            deployment_list = apps_api.list_deployment_for_all_namespaces(
                label_selector=label_selector
            )
        return [_to_non_pod_raw(item, ) for item in deployment_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_13(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        if namespace:
            deployment_list = apps_api.list_namespaced_deployment(
                namespace=namespace, label_selector=label_selector
            )
        else:
            deployment_list = apps_api.list_deployment_for_all_namespaces(
                label_selector=label_selector
            )
        return [_to_non_pod_raw(item, kind="XXdeploymentXX") for item in deployment_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_14(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        if namespace:
            deployment_list = apps_api.list_namespaced_deployment(
                namespace=namespace, label_selector=label_selector
            )
        else:
            deployment_list = apps_api.list_deployment_for_all_namespaces(
                label_selector=label_selector
            )
        return [_to_non_pod_raw(item, kind="DEPLOYMENT") for item in deployment_list.items]

    @_mutmut_mutated(mutants_xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut)
    def search_services(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            service_list = core_api.list_namespaced_service(
                namespace=namespace, label_selector=label_selector
            )
        else:
            service_list = core_api.list_service_for_all_namespaces(label_selector=label_selector)
        return [_to_non_pod_raw(item, kind="service") for item in service_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_orig(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            service_list = core_api.list_namespaced_service(
                namespace=namespace, label_selector=label_selector
            )
        else:
            service_list = core_api.list_service_for_all_namespaces(label_selector=label_selector)
        return [_to_non_pod_raw(item, kind="service") for item in service_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_1(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = None
        if namespace:
            service_list = core_api.list_namespaced_service(
                namespace=namespace, label_selector=label_selector
            )
        else:
            service_list = core_api.list_service_for_all_namespaces(label_selector=label_selector)
        return [_to_non_pod_raw(item, kind="service") for item in service_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_2(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            service_list = None
        else:
            service_list = core_api.list_service_for_all_namespaces(label_selector=label_selector)
        return [_to_non_pod_raw(item, kind="service") for item in service_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_3(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            service_list = core_api.list_namespaced_service(
                namespace=None, label_selector=label_selector
            )
        else:
            service_list = core_api.list_service_for_all_namespaces(label_selector=label_selector)
        return [_to_non_pod_raw(item, kind="service") for item in service_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_4(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            service_list = core_api.list_namespaced_service(
                namespace=namespace, label_selector=None
            )
        else:
            service_list = core_api.list_service_for_all_namespaces(label_selector=label_selector)
        return [_to_non_pod_raw(item, kind="service") for item in service_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_5(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            service_list = core_api.list_namespaced_service(
                label_selector=label_selector
            )
        else:
            service_list = core_api.list_service_for_all_namespaces(label_selector=label_selector)
        return [_to_non_pod_raw(item, kind="service") for item in service_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_6(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            service_list = core_api.list_namespaced_service(
                namespace=namespace, )
        else:
            service_list = core_api.list_service_for_all_namespaces(label_selector=label_selector)
        return [_to_non_pod_raw(item, kind="service") for item in service_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_7(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            service_list = core_api.list_namespaced_service(
                namespace=namespace, label_selector=label_selector
            )
        else:
            service_list = None
        return [_to_non_pod_raw(item, kind="service") for item in service_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_8(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            service_list = core_api.list_namespaced_service(
                namespace=namespace, label_selector=label_selector
            )
        else:
            service_list = core_api.list_service_for_all_namespaces(label_selector=None)
        return [_to_non_pod_raw(item, kind="service") for item in service_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_9(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            service_list = core_api.list_namespaced_service(
                namespace=namespace, label_selector=label_selector
            )
        else:
            service_list = core_api.list_service_for_all_namespaces(label_selector=label_selector)
        return [_to_non_pod_raw(None, kind="service") for item in service_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_10(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            service_list = core_api.list_namespaced_service(
                namespace=namespace, label_selector=label_selector
            )
        else:
            service_list = core_api.list_service_for_all_namespaces(label_selector=label_selector)
        return [_to_non_pod_raw(item, kind=None) for item in service_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_11(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            service_list = core_api.list_namespaced_service(
                namespace=namespace, label_selector=label_selector
            )
        else:
            service_list = core_api.list_service_for_all_namespaces(label_selector=label_selector)
        return [_to_non_pod_raw(kind="service") for item in service_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_12(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            service_list = core_api.list_namespaced_service(
                namespace=namespace, label_selector=label_selector
            )
        else:
            service_list = core_api.list_service_for_all_namespaces(label_selector=label_selector)
        return [_to_non_pod_raw(item, ) for item in service_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_13(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            service_list = core_api.list_namespaced_service(
                namespace=namespace, label_selector=label_selector
            )
        else:
            service_list = core_api.list_service_for_all_namespaces(label_selector=label_selector)
        return [_to_non_pod_raw(item, kind="XXserviceXX") for item in service_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_14(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            service_list = core_api.list_namespaced_service(
                namespace=namespace, label_selector=label_selector
            )
        else:
            service_list = core_api.list_service_for_all_namespaces(label_selector=label_selector)
        return [_to_non_pod_raw(item, kind="SERVICE") for item in service_list.items]

    @_mutmut_mutated(mutants_xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut)
    def search_configmaps(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            configmap_list = core_api.list_namespaced_config_map(
                namespace=namespace, label_selector=label_selector
            )
        else:
            configmap_list = core_api.list_config_map_for_all_namespaces(
                label_selector=label_selector
            )
        return [_to_non_pod_raw(item, kind="configmap") for item in configmap_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_orig(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            configmap_list = core_api.list_namespaced_config_map(
                namespace=namespace, label_selector=label_selector
            )
        else:
            configmap_list = core_api.list_config_map_for_all_namespaces(
                label_selector=label_selector
            )
        return [_to_non_pod_raw(item, kind="configmap") for item in configmap_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_1(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = None
        if namespace:
            configmap_list = core_api.list_namespaced_config_map(
                namespace=namespace, label_selector=label_selector
            )
        else:
            configmap_list = core_api.list_config_map_for_all_namespaces(
                label_selector=label_selector
            )
        return [_to_non_pod_raw(item, kind="configmap") for item in configmap_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_2(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            configmap_list = None
        else:
            configmap_list = core_api.list_config_map_for_all_namespaces(
                label_selector=label_selector
            )
        return [_to_non_pod_raw(item, kind="configmap") for item in configmap_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_3(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            configmap_list = core_api.list_namespaced_config_map(
                namespace=None, label_selector=label_selector
            )
        else:
            configmap_list = core_api.list_config_map_for_all_namespaces(
                label_selector=label_selector
            )
        return [_to_non_pod_raw(item, kind="configmap") for item in configmap_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_4(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            configmap_list = core_api.list_namespaced_config_map(
                namespace=namespace, label_selector=None
            )
        else:
            configmap_list = core_api.list_config_map_for_all_namespaces(
                label_selector=label_selector
            )
        return [_to_non_pod_raw(item, kind="configmap") for item in configmap_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_5(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            configmap_list = core_api.list_namespaced_config_map(
                label_selector=label_selector
            )
        else:
            configmap_list = core_api.list_config_map_for_all_namespaces(
                label_selector=label_selector
            )
        return [_to_non_pod_raw(item, kind="configmap") for item in configmap_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_6(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            configmap_list = core_api.list_namespaced_config_map(
                namespace=namespace, )
        else:
            configmap_list = core_api.list_config_map_for_all_namespaces(
                label_selector=label_selector
            )
        return [_to_non_pod_raw(item, kind="configmap") for item in configmap_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_7(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            configmap_list = core_api.list_namespaced_config_map(
                namespace=namespace, label_selector=label_selector
            )
        else:
            configmap_list = None
        return [_to_non_pod_raw(item, kind="configmap") for item in configmap_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_8(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            configmap_list = core_api.list_namespaced_config_map(
                namespace=namespace, label_selector=label_selector
            )
        else:
            configmap_list = core_api.list_config_map_for_all_namespaces(
                label_selector=None
            )
        return [_to_non_pod_raw(item, kind="configmap") for item in configmap_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_9(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            configmap_list = core_api.list_namespaced_config_map(
                namespace=namespace, label_selector=label_selector
            )
        else:
            configmap_list = core_api.list_config_map_for_all_namespaces(
                label_selector=label_selector
            )
        return [_to_non_pod_raw(None, kind="configmap") for item in configmap_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_10(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            configmap_list = core_api.list_namespaced_config_map(
                namespace=namespace, label_selector=label_selector
            )
        else:
            configmap_list = core_api.list_config_map_for_all_namespaces(
                label_selector=label_selector
            )
        return [_to_non_pod_raw(item, kind=None) for item in configmap_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_11(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            configmap_list = core_api.list_namespaced_config_map(
                namespace=namespace, label_selector=label_selector
            )
        else:
            configmap_list = core_api.list_config_map_for_all_namespaces(
                label_selector=label_selector
            )
        return [_to_non_pod_raw(kind="configmap") for item in configmap_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_12(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            configmap_list = core_api.list_namespaced_config_map(
                namespace=namespace, label_selector=label_selector
            )
        else:
            configmap_list = core_api.list_config_map_for_all_namespaces(
                label_selector=label_selector
            )
        return [_to_non_pod_raw(item, ) for item in configmap_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_13(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            configmap_list = core_api.list_namespaced_config_map(
                namespace=namespace, label_selector=label_selector
            )
        else:
            configmap_list = core_api.list_config_map_for_all_namespaces(
                label_selector=label_selector
            )
        return [_to_non_pod_raw(item, kind="XXconfigmapXX") for item in configmap_list.items]

    def xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_14(
        self, label_selector: str, namespace: str | None
    ) -> list[MatchedResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        if namespace:
            configmap_list = core_api.list_namespaced_config_map(
                namespace=namespace, label_selector=label_selector
            )
        else:
            configmap_list = core_api.list_config_map_for_all_namespaces(
                label_selector=label_selector
            )
        return [_to_non_pod_raw(item, kind="CONFIGMAP") for item in configmap_list.items]

mutants_xǁKubernetesLabelSearchAdapterǁsearch_pods__mutmut['_mutmut_orig'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_pods__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_pods__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_pods__mutmut_1'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_pods__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_pods__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_pods__mutmut_2'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_pods__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_pods__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_pods__mutmut_3'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_pods__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_pods__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_pods__mutmut_4'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_pods__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_pods__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_pods__mutmut_5'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_pods__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_pods__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_pods__mutmut_6'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_pods__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_pods__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_pods__mutmut_7'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_pods__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_pods__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_pods__mutmut_8'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_pods__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_pods__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_pods__mutmut_9'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_pods__mutmut_9 # type: ignore # mutmut generated

mutants_xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut['_mutmut_orig'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_1'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_2'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_3'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_4'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_5'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_6'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_7'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_8'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_9'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_10'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_11'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_12'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_13'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_14'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_deployments__mutmut_14 # type: ignore # mutmut generated

mutants_xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut['_mutmut_orig'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_1'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_2'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_3'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_4'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_5'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_6'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_7'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_8'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_9'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_10'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_11'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_12'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_13'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_14'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_services__mutmut_14 # type: ignore # mutmut generated

mutants_xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut['_mutmut_orig'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_1'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_2'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_3'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_4'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_5'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_6'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_7'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_8'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_9'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_10'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_11'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_12'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_13'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut['xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_14'] = KubernetesLabelSearchAdapter.xǁKubernetesLabelSearchAdapterǁsearch_configmaps__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_pod_raw__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_pod_raw__mutmut)
def _to_pod_raw(item: V1Pod) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        kind="pod",
        node=item.spec.node_name,
        phase=item.status.phase or "Unknown",
        ready=_pod_ready(item),
        labels=dict(item.metadata.labels or {}),
    )


def x__to_pod_raw__mutmut_orig(item: V1Pod) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        kind="pod",
        node=item.spec.node_name,
        phase=item.status.phase or "Unknown",
        ready=_pod_ready(item),
        labels=dict(item.metadata.labels or {}),
    )


def x__to_pod_raw__mutmut_1(item: V1Pod) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        name=None,
        namespace=item.metadata.namespace,
        kind="pod",
        node=item.spec.node_name,
        phase=item.status.phase or "Unknown",
        ready=_pod_ready(item),
        labels=dict(item.metadata.labels or {}),
    )


def x__to_pod_raw__mutmut_2(item: V1Pod) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        name=item.metadata.name,
        namespace=None,
        kind="pod",
        node=item.spec.node_name,
        phase=item.status.phase or "Unknown",
        ready=_pod_ready(item),
        labels=dict(item.metadata.labels or {}),
    )


def x__to_pod_raw__mutmut_3(item: V1Pod) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        kind=None,
        node=item.spec.node_name,
        phase=item.status.phase or "Unknown",
        ready=_pod_ready(item),
        labels=dict(item.metadata.labels or {}),
    )


def x__to_pod_raw__mutmut_4(item: V1Pod) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        kind="pod",
        node=None,
        phase=item.status.phase or "Unknown",
        ready=_pod_ready(item),
        labels=dict(item.metadata.labels or {}),
    )


def x__to_pod_raw__mutmut_5(item: V1Pod) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        kind="pod",
        node=item.spec.node_name,
        phase=None,
        ready=_pod_ready(item),
        labels=dict(item.metadata.labels or {}),
    )


def x__to_pod_raw__mutmut_6(item: V1Pod) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        kind="pod",
        node=item.spec.node_name,
        phase=item.status.phase or "Unknown",
        ready=None,
        labels=dict(item.metadata.labels or {}),
    )


def x__to_pod_raw__mutmut_7(item: V1Pod) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        kind="pod",
        node=item.spec.node_name,
        phase=item.status.phase or "Unknown",
        ready=_pod_ready(item),
        labels=None,
    )


def x__to_pod_raw__mutmut_8(item: V1Pod) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        namespace=item.metadata.namespace,
        kind="pod",
        node=item.spec.node_name,
        phase=item.status.phase or "Unknown",
        ready=_pod_ready(item),
        labels=dict(item.metadata.labels or {}),
    )


def x__to_pod_raw__mutmut_9(item: V1Pod) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        name=item.metadata.name,
        kind="pod",
        node=item.spec.node_name,
        phase=item.status.phase or "Unknown",
        ready=_pod_ready(item),
        labels=dict(item.metadata.labels or {}),
    )


def x__to_pod_raw__mutmut_10(item: V1Pod) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        node=item.spec.node_name,
        phase=item.status.phase or "Unknown",
        ready=_pod_ready(item),
        labels=dict(item.metadata.labels or {}),
    )


def x__to_pod_raw__mutmut_11(item: V1Pod) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        kind="pod",
        phase=item.status.phase or "Unknown",
        ready=_pod_ready(item),
        labels=dict(item.metadata.labels or {}),
    )


def x__to_pod_raw__mutmut_12(item: V1Pod) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        kind="pod",
        node=item.spec.node_name,
        ready=_pod_ready(item),
        labels=dict(item.metadata.labels or {}),
    )


def x__to_pod_raw__mutmut_13(item: V1Pod) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        kind="pod",
        node=item.spec.node_name,
        phase=item.status.phase or "Unknown",
        labels=dict(item.metadata.labels or {}),
    )


def x__to_pod_raw__mutmut_14(item: V1Pod) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        kind="pod",
        node=item.spec.node_name,
        phase=item.status.phase or "Unknown",
        ready=_pod_ready(item),
        )


def x__to_pod_raw__mutmut_15(item: V1Pod) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        kind="XXpodXX",
        node=item.spec.node_name,
        phase=item.status.phase or "Unknown",
        ready=_pod_ready(item),
        labels=dict(item.metadata.labels or {}),
    )


def x__to_pod_raw__mutmut_16(item: V1Pod) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        kind="POD",
        node=item.spec.node_name,
        phase=item.status.phase or "Unknown",
        ready=_pod_ready(item),
        labels=dict(item.metadata.labels or {}),
    )


def x__to_pod_raw__mutmut_17(item: V1Pod) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        kind="pod",
        node=item.spec.node_name,
        phase=item.status.phase and "Unknown",
        ready=_pod_ready(item),
        labels=dict(item.metadata.labels or {}),
    )


def x__to_pod_raw__mutmut_18(item: V1Pod) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        kind="pod",
        node=item.spec.node_name,
        phase=item.status.phase or "XXUnknownXX",
        ready=_pod_ready(item),
        labels=dict(item.metadata.labels or {}),
    )


def x__to_pod_raw__mutmut_19(item: V1Pod) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        kind="pod",
        node=item.spec.node_name,
        phase=item.status.phase or "unknown",
        ready=_pod_ready(item),
        labels=dict(item.metadata.labels or {}),
    )


def x__to_pod_raw__mutmut_20(item: V1Pod) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        kind="pod",
        node=item.spec.node_name,
        phase=item.status.phase or "UNKNOWN",
        ready=_pod_ready(item),
        labels=dict(item.metadata.labels or {}),
    )


def x__to_pod_raw__mutmut_21(item: V1Pod) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        kind="pod",
        node=item.spec.node_name,
        phase=item.status.phase or "Unknown",
        ready=_pod_ready(None),
        labels=dict(item.metadata.labels or {}),
    )


def x__to_pod_raw__mutmut_22(item: V1Pod) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        kind="pod",
        node=item.spec.node_name,
        phase=item.status.phase or "Unknown",
        ready=_pod_ready(item),
        labels=dict(None),
    )


def x__to_pod_raw__mutmut_23(item: V1Pod) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        kind="pod",
        node=item.spec.node_name,
        phase=item.status.phase or "Unknown",
        ready=_pod_ready(item),
        labels=dict(item.metadata.labels and {}),
    )

mutants_x__to_pod_raw__mutmut['_mutmut_orig'] = x__to_pod_raw__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_pod_raw__mutmut['x__to_pod_raw__mutmut_1'] = x__to_pod_raw__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_pod_raw__mutmut['x__to_pod_raw__mutmut_2'] = x__to_pod_raw__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_pod_raw__mutmut['x__to_pod_raw__mutmut_3'] = x__to_pod_raw__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_pod_raw__mutmut['x__to_pod_raw__mutmut_4'] = x__to_pod_raw__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_pod_raw__mutmut['x__to_pod_raw__mutmut_5'] = x__to_pod_raw__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_pod_raw__mutmut['x__to_pod_raw__mutmut_6'] = x__to_pod_raw__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_pod_raw__mutmut['x__to_pod_raw__mutmut_7'] = x__to_pod_raw__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_pod_raw__mutmut['x__to_pod_raw__mutmut_8'] = x__to_pod_raw__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_pod_raw__mutmut['x__to_pod_raw__mutmut_9'] = x__to_pod_raw__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_pod_raw__mutmut['x__to_pod_raw__mutmut_10'] = x__to_pod_raw__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_pod_raw__mutmut['x__to_pod_raw__mutmut_11'] = x__to_pod_raw__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_pod_raw__mutmut['x__to_pod_raw__mutmut_12'] = x__to_pod_raw__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_pod_raw__mutmut['x__to_pod_raw__mutmut_13'] = x__to_pod_raw__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_pod_raw__mutmut['x__to_pod_raw__mutmut_14'] = x__to_pod_raw__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_pod_raw__mutmut['x__to_pod_raw__mutmut_15'] = x__to_pod_raw__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_pod_raw__mutmut['x__to_pod_raw__mutmut_16'] = x__to_pod_raw__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_pod_raw__mutmut['x__to_pod_raw__mutmut_17'] = x__to_pod_raw__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_pod_raw__mutmut['x__to_pod_raw__mutmut_18'] = x__to_pod_raw__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_pod_raw__mutmut['x__to_pod_raw__mutmut_19'] = x__to_pod_raw__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_pod_raw__mutmut['x__to_pod_raw__mutmut_20'] = x__to_pod_raw__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_pod_raw__mutmut['x__to_pod_raw__mutmut_21'] = x__to_pod_raw__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_pod_raw__mutmut['x__to_pod_raw__mutmut_22'] = x__to_pod_raw__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_pod_raw__mutmut['x__to_pod_raw__mutmut_23'] = x__to_pod_raw__mutmut_23 # type: ignore # mutmut generated
mutants_x__pod_ready__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__pod_ready__mutmut)
def _pod_ready(item: V1Pod) -> bool:
    statuses = item.status.container_statuses or []
    if not statuses:
        return False
    return all(status.ready for status in statuses)


def x__pod_ready__mutmut_orig(item: V1Pod) -> bool:
    statuses = item.status.container_statuses or []
    if not statuses:
        return False
    return all(status.ready for status in statuses)


def x__pod_ready__mutmut_1(item: V1Pod) -> bool:
    statuses = None
    if not statuses:
        return False
    return all(status.ready for status in statuses)


def x__pod_ready__mutmut_2(item: V1Pod) -> bool:
    statuses = item.status.container_statuses and []
    if not statuses:
        return False
    return all(status.ready for status in statuses)


def x__pod_ready__mutmut_3(item: V1Pod) -> bool:
    statuses = item.status.container_statuses or []
    if statuses:
        return False
    return all(status.ready for status in statuses)


def x__pod_ready__mutmut_4(item: V1Pod) -> bool:
    statuses = item.status.container_statuses or []
    if not statuses:
        return True
    return all(status.ready for status in statuses)


def x__pod_ready__mutmut_5(item: V1Pod) -> bool:
    statuses = item.status.container_statuses or []
    if not statuses:
        return False
    return all(None)

mutants_x__pod_ready__mutmut['_mutmut_orig'] = x__pod_ready__mutmut_orig # type: ignore # mutmut generated
mutants_x__pod_ready__mutmut['x__pod_ready__mutmut_1'] = x__pod_ready__mutmut_1 # type: ignore # mutmut generated
mutants_x__pod_ready__mutmut['x__pod_ready__mutmut_2'] = x__pod_ready__mutmut_2 # type: ignore # mutmut generated
mutants_x__pod_ready__mutmut['x__pod_ready__mutmut_3'] = x__pod_ready__mutmut_3 # type: ignore # mutmut generated
mutants_x__pod_ready__mutmut['x__pod_ready__mutmut_4'] = x__pod_ready__mutmut_4 # type: ignore # mutmut generated
mutants_x__pod_ready__mutmut['x__pod_ready__mutmut_5'] = x__pod_ready__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_non_pod_raw__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_non_pod_raw__mutmut)
def _to_non_pod_raw(item: V1Deployment | V1Service | V1ConfigMap, kind: str) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        kind=kind,
        node=None,
        phase=None,
        ready=None,
        labels=dict(item.metadata.labels or {}),
    )


def x__to_non_pod_raw__mutmut_orig(item: V1Deployment | V1Service | V1ConfigMap, kind: str) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        kind=kind,
        node=None,
        phase=None,
        ready=None,
        labels=dict(item.metadata.labels or {}),
    )


def x__to_non_pod_raw__mutmut_1(item: V1Deployment | V1Service | V1ConfigMap, kind: str) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        name=None,
        namespace=item.metadata.namespace,
        kind=kind,
        node=None,
        phase=None,
        ready=None,
        labels=dict(item.metadata.labels or {}),
    )


def x__to_non_pod_raw__mutmut_2(item: V1Deployment | V1Service | V1ConfigMap, kind: str) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        name=item.metadata.name,
        namespace=None,
        kind=kind,
        node=None,
        phase=None,
        ready=None,
        labels=dict(item.metadata.labels or {}),
    )


def x__to_non_pod_raw__mutmut_3(item: V1Deployment | V1Service | V1ConfigMap, kind: str) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        kind=None,
        node=None,
        phase=None,
        ready=None,
        labels=dict(item.metadata.labels or {}),
    )


def x__to_non_pod_raw__mutmut_4(item: V1Deployment | V1Service | V1ConfigMap, kind: str) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        kind=kind,
        node=None,
        phase=None,
        ready=None,
        labels=None,
    )


def x__to_non_pod_raw__mutmut_5(item: V1Deployment | V1Service | V1ConfigMap, kind: str) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        namespace=item.metadata.namespace,
        kind=kind,
        node=None,
        phase=None,
        ready=None,
        labels=dict(item.metadata.labels or {}),
    )


def x__to_non_pod_raw__mutmut_6(item: V1Deployment | V1Service | V1ConfigMap, kind: str) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        name=item.metadata.name,
        kind=kind,
        node=None,
        phase=None,
        ready=None,
        labels=dict(item.metadata.labels or {}),
    )


def x__to_non_pod_raw__mutmut_7(item: V1Deployment | V1Service | V1ConfigMap, kind: str) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        node=None,
        phase=None,
        ready=None,
        labels=dict(item.metadata.labels or {}),
    )


def x__to_non_pod_raw__mutmut_8(item: V1Deployment | V1Service | V1ConfigMap, kind: str) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        kind=kind,
        phase=None,
        ready=None,
        labels=dict(item.metadata.labels or {}),
    )


def x__to_non_pod_raw__mutmut_9(item: V1Deployment | V1Service | V1ConfigMap, kind: str) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        kind=kind,
        node=None,
        ready=None,
        labels=dict(item.metadata.labels or {}),
    )


def x__to_non_pod_raw__mutmut_10(item: V1Deployment | V1Service | V1ConfigMap, kind: str) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        kind=kind,
        node=None,
        phase=None,
        labels=dict(item.metadata.labels or {}),
    )


def x__to_non_pod_raw__mutmut_11(item: V1Deployment | V1Service | V1ConfigMap, kind: str) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        kind=kind,
        node=None,
        phase=None,
        ready=None,
        )


def x__to_non_pod_raw__mutmut_12(item: V1Deployment | V1Service | V1ConfigMap, kind: str) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        kind=kind,
        node=None,
        phase=None,
        ready=None,
        labels=dict(None),
    )


def x__to_non_pod_raw__mutmut_13(item: V1Deployment | V1Service | V1ConfigMap, kind: str) -> MatchedResourceRaw:
    return MatchedResourceRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        kind=kind,
        node=None,
        phase=None,
        ready=None,
        labels=dict(item.metadata.labels and {}),
    )

mutants_x__to_non_pod_raw__mutmut['_mutmut_orig'] = x__to_non_pod_raw__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_non_pod_raw__mutmut['x__to_non_pod_raw__mutmut_1'] = x__to_non_pod_raw__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_non_pod_raw__mutmut['x__to_non_pod_raw__mutmut_2'] = x__to_non_pod_raw__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_non_pod_raw__mutmut['x__to_non_pod_raw__mutmut_3'] = x__to_non_pod_raw__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_non_pod_raw__mutmut['x__to_non_pod_raw__mutmut_4'] = x__to_non_pod_raw__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_non_pod_raw__mutmut['x__to_non_pod_raw__mutmut_5'] = x__to_non_pod_raw__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_non_pod_raw__mutmut['x__to_non_pod_raw__mutmut_6'] = x__to_non_pod_raw__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_non_pod_raw__mutmut['x__to_non_pod_raw__mutmut_7'] = x__to_non_pod_raw__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_non_pod_raw__mutmut['x__to_non_pod_raw__mutmut_8'] = x__to_non_pod_raw__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_non_pod_raw__mutmut['x__to_non_pod_raw__mutmut_9'] = x__to_non_pod_raw__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_non_pod_raw__mutmut['x__to_non_pod_raw__mutmut_10'] = x__to_non_pod_raw__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_non_pod_raw__mutmut['x__to_non_pod_raw__mutmut_11'] = x__to_non_pod_raw__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_non_pod_raw__mutmut['x__to_non_pod_raw__mutmut_12'] = x__to_non_pod_raw__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_non_pod_raw__mutmut['x__to_non_pod_raw__mutmut_13'] = x__to_non_pod_raw__mutmut_13 # type: ignore # mutmut generated
