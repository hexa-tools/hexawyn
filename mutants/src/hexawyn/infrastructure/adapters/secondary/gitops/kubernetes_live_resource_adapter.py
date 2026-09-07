from __future__ import annotations

from hexawyn.application.ports.driven.live_resource_port import LiveResourcePort, LiveResourceRaw
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError

_K8S_FORBIDDEN = 403


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut: MutantDict = {}  # type: ignore


class KubernetesLiveResourceAdapter(LiveResourcePort):
    """Secondary adapter — lists live Deployments and ConfigMaps, extracting
    labels and annotations. `to_dict()`'s output is directly compatible
    with field_comparison.py's extractors — none of the specific paths this
    feature reads (image/env/replicas/limits/labels/data) differ between
    raw K8s YAML and the client's snake_case conversion."""

    @_mutmut_mutated(mutants_xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut)
    def list_live_resources(self, namespace: str) -> list[LiveResourceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        try:
            configmaps = core_api.list_namespaced_config_map(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_live_resource("Deployment", item) for item in deployments.items] + [
            _to_live_resource("ConfigMap", item) for item in configmaps.items
        ]

    def xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_orig(self, namespace: str) -> list[LiveResourceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        try:
            configmaps = core_api.list_namespaced_config_map(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_live_resource("Deployment", item) for item in deployments.items] + [
            _to_live_resource("ConfigMap", item) for item in configmaps.items
        ]

    def xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_1(self, namespace: str) -> list[LiveResourceRaw]:
        from kubernetes import client as k8s

        apps_api = None
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        try:
            configmaps = core_api.list_namespaced_config_map(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_live_resource("Deployment", item) for item in deployments.items] + [
            _to_live_resource("ConfigMap", item) for item in configmaps.items
        ]

    def xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_2(self, namespace: str) -> list[LiveResourceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = None

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        try:
            configmaps = core_api.list_namespaced_config_map(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_live_resource("Deployment", item) for item in deployments.items] + [
            _to_live_resource("ConfigMap", item) for item in configmaps.items
        ]

    def xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_3(self, namespace: str) -> list[LiveResourceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = None
        except Exception as exc:
            raise _translate_error(exc) from exc

        try:
            configmaps = core_api.list_namespaced_config_map(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_live_resource("Deployment", item) for item in deployments.items] + [
            _to_live_resource("ConfigMap", item) for item in configmaps.items
        ]

    def xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_4(self, namespace: str) -> list[LiveResourceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=None)
        except Exception as exc:
            raise _translate_error(exc) from exc

        try:
            configmaps = core_api.list_namespaced_config_map(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_live_resource("Deployment", item) for item in deployments.items] + [
            _to_live_resource("ConfigMap", item) for item in configmaps.items
        ]

    def xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_5(self, namespace: str) -> list[LiveResourceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
        except Exception as exc:
            raise _translate_error(None) from exc

        try:
            configmaps = core_api.list_namespaced_config_map(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_live_resource("Deployment", item) for item in deployments.items] + [
            _to_live_resource("ConfigMap", item) for item in configmaps.items
        ]

    def xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_6(self, namespace: str) -> list[LiveResourceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        try:
            configmaps = None
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_live_resource("Deployment", item) for item in deployments.items] + [
            _to_live_resource("ConfigMap", item) for item in configmaps.items
        ]

    def xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_7(self, namespace: str) -> list[LiveResourceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        try:
            configmaps = core_api.list_namespaced_config_map(namespace=None)
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_live_resource("Deployment", item) for item in deployments.items] + [
            _to_live_resource("ConfigMap", item) for item in configmaps.items
        ]

    def xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_8(self, namespace: str) -> list[LiveResourceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        try:
            configmaps = core_api.list_namespaced_config_map(namespace=namespace)
        except Exception as exc:
            raise _translate_error(None) from exc

        return [_to_live_resource("Deployment", item) for item in deployments.items] + [
            _to_live_resource("ConfigMap", item) for item in configmaps.items
        ]

    def xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_9(self, namespace: str) -> list[LiveResourceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        try:
            configmaps = core_api.list_namespaced_config_map(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_live_resource("Deployment", item) for item in deployments.items] - [
            _to_live_resource("ConfigMap", item) for item in configmaps.items
        ]

    def xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_10(self, namespace: str) -> list[LiveResourceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        try:
            configmaps = core_api.list_namespaced_config_map(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_live_resource(None, item) for item in deployments.items] + [
            _to_live_resource("ConfigMap", item) for item in configmaps.items
        ]

    def xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_11(self, namespace: str) -> list[LiveResourceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        try:
            configmaps = core_api.list_namespaced_config_map(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_live_resource("Deployment", None) for item in deployments.items] + [
            _to_live_resource("ConfigMap", item) for item in configmaps.items
        ]

    def xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_12(self, namespace: str) -> list[LiveResourceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        try:
            configmaps = core_api.list_namespaced_config_map(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_live_resource(item) for item in deployments.items] + [
            _to_live_resource("ConfigMap", item) for item in configmaps.items
        ]

    def xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_13(self, namespace: str) -> list[LiveResourceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        try:
            configmaps = core_api.list_namespaced_config_map(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_live_resource("Deployment", ) for item in deployments.items] + [
            _to_live_resource("ConfigMap", item) for item in configmaps.items
        ]

    def xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_14(self, namespace: str) -> list[LiveResourceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        try:
            configmaps = core_api.list_namespaced_config_map(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_live_resource("XXDeploymentXX", item) for item in deployments.items] + [
            _to_live_resource("ConfigMap", item) for item in configmaps.items
        ]

    def xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_15(self, namespace: str) -> list[LiveResourceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        try:
            configmaps = core_api.list_namespaced_config_map(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_live_resource("deployment", item) for item in deployments.items] + [
            _to_live_resource("ConfigMap", item) for item in configmaps.items
        ]

    def xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_16(self, namespace: str) -> list[LiveResourceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        try:
            configmaps = core_api.list_namespaced_config_map(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_live_resource("DEPLOYMENT", item) for item in deployments.items] + [
            _to_live_resource("ConfigMap", item) for item in configmaps.items
        ]

    def xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_17(self, namespace: str) -> list[LiveResourceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        try:
            configmaps = core_api.list_namespaced_config_map(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_live_resource("Deployment", item) for item in deployments.items] + [
            _to_live_resource(None, item) for item in configmaps.items
        ]

    def xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_18(self, namespace: str) -> list[LiveResourceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        try:
            configmaps = core_api.list_namespaced_config_map(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_live_resource("Deployment", item) for item in deployments.items] + [
            _to_live_resource("ConfigMap", None) for item in configmaps.items
        ]

    def xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_19(self, namespace: str) -> list[LiveResourceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        try:
            configmaps = core_api.list_namespaced_config_map(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_live_resource("Deployment", item) for item in deployments.items] + [
            _to_live_resource(item) for item in configmaps.items
        ]

    def xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_20(self, namespace: str) -> list[LiveResourceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        try:
            configmaps = core_api.list_namespaced_config_map(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_live_resource("Deployment", item) for item in deployments.items] + [
            _to_live_resource("ConfigMap", ) for item in configmaps.items
        ]

    def xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_21(self, namespace: str) -> list[LiveResourceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        try:
            configmaps = core_api.list_namespaced_config_map(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_live_resource("Deployment", item) for item in deployments.items] + [
            _to_live_resource("XXConfigMapXX", item) for item in configmaps.items
        ]

    def xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_22(self, namespace: str) -> list[LiveResourceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        try:
            configmaps = core_api.list_namespaced_config_map(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_live_resource("Deployment", item) for item in deployments.items] + [
            _to_live_resource("configmap", item) for item in configmaps.items
        ]

    def xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_23(self, namespace: str) -> list[LiveResourceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        try:
            configmaps = core_api.list_namespaced_config_map(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_live_resource("Deployment", item) for item in deployments.items] + [
            _to_live_resource("CONFIGMAP", item) for item in configmaps.items
        ]

mutants_xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut['_mutmut_orig'] = KubernetesLiveResourceAdapter.xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut['xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_1'] = KubernetesLiveResourceAdapter.xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut['xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_2'] = KubernetesLiveResourceAdapter.xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut['xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_3'] = KubernetesLiveResourceAdapter.xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut['xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_4'] = KubernetesLiveResourceAdapter.xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut['xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_5'] = KubernetesLiveResourceAdapter.xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut['xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_6'] = KubernetesLiveResourceAdapter.xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut['xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_7'] = KubernetesLiveResourceAdapter.xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut['xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_8'] = KubernetesLiveResourceAdapter.xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut['xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_9'] = KubernetesLiveResourceAdapter.xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut['xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_10'] = KubernetesLiveResourceAdapter.xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut['xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_11'] = KubernetesLiveResourceAdapter.xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut['xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_12'] = KubernetesLiveResourceAdapter.xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut['xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_13'] = KubernetesLiveResourceAdapter.xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut['xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_14'] = KubernetesLiveResourceAdapter.xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_14 # type: ignore # mutmut generated
mutants_xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut['xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_15'] = KubernetesLiveResourceAdapter.xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_15 # type: ignore # mutmut generated
mutants_xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut['xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_16'] = KubernetesLiveResourceAdapter.xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_16 # type: ignore # mutmut generated
mutants_xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut['xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_17'] = KubernetesLiveResourceAdapter.xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_17 # type: ignore # mutmut generated
mutants_xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut['xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_18'] = KubernetesLiveResourceAdapter.xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_18 # type: ignore # mutmut generated
mutants_xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut['xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_19'] = KubernetesLiveResourceAdapter.xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_19 # type: ignore # mutmut generated
mutants_xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut['xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_20'] = KubernetesLiveResourceAdapter.xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_20 # type: ignore # mutmut generated
mutants_xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut['xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_21'] = KubernetesLiveResourceAdapter.xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_21 # type: ignore # mutmut generated
mutants_xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut['xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_22'] = KubernetesLiveResourceAdapter.xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_22 # type: ignore # mutmut generated
mutants_xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut['xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_23'] = KubernetesLiveResourceAdapter.xǁKubernetesLiveResourceAdapterǁlist_live_resources__mutmut_23 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_live_resource__mutmut)
def _to_live_resource(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_orig(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_1(kind: str, item: object) -> LiveResourceRaw:
    metadata = None
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_2(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(None, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_3(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, None, None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_4(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr("metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_5(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_6(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", )
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_7(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "XXmetadataXX", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_8(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "METADATA", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_9(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = None
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_10(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(None, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_11(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, None, None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_12(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr("to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_13(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_14(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", )
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_15(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "XXto_dictXX", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_16(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "TO_DICT", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_17(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=None,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_18(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=None,
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_19(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=None,
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_20(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=None,
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_21(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=None,
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_22(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=None,
    )


def x__to_live_resource__mutmut_23(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_24(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_25(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_26(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_27(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_28(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        )


def x__to_live_resource__mutmut_29(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(None, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_30(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, None, ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_31(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", None),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_32(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr("name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_33(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_34(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_35(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "XXnameXX", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_36(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "NAME", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_37(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", "XXXX"),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_38(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(None, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_39(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, None, ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_40(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", None),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_41(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr("namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_42(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_43(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_44(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "XXnamespaceXX", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_45(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "NAMESPACE", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_46(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", "XXXX"),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_47(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(None),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_48(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) and {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_49(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(None, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_50(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, None, None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_51(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr("labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_52(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_53(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", ) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_54(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "XXlabelsXX", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_55(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "LABELS", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_56(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(None),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_57(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) and {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_58(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(None, "annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_59(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, None, None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_60(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr("annotations", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_61(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_62(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", ) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_63(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "XXannotationsXX", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_64(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "ANNOTATIONS", None) or {}),
        data=to_dict() if callable(to_dict) else {},
    )


def x__to_live_resource__mutmut_65(kind: str, item: object) -> LiveResourceRaw:
    metadata = getattr(item, "metadata", None)
    to_dict = getattr(item, "to_dict", None)
    return LiveResourceRaw(
        kind=kind,
        name=getattr(metadata, "name", ""),
        namespace=getattr(metadata, "namespace", ""),
        labels=dict(getattr(metadata, "labels", None) or {}),
        annotations=dict(getattr(metadata, "annotations", None) or {}),
        data=to_dict() if callable(None) else {},
    )

mutants_x__to_live_resource__mutmut['_mutmut_orig'] = x__to_live_resource__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_1'] = x__to_live_resource__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_2'] = x__to_live_resource__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_3'] = x__to_live_resource__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_4'] = x__to_live_resource__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_5'] = x__to_live_resource__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_6'] = x__to_live_resource__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_7'] = x__to_live_resource__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_8'] = x__to_live_resource__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_9'] = x__to_live_resource__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_10'] = x__to_live_resource__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_11'] = x__to_live_resource__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_12'] = x__to_live_resource__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_13'] = x__to_live_resource__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_14'] = x__to_live_resource__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_15'] = x__to_live_resource__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_16'] = x__to_live_resource__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_17'] = x__to_live_resource__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_18'] = x__to_live_resource__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_19'] = x__to_live_resource__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_20'] = x__to_live_resource__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_21'] = x__to_live_resource__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_22'] = x__to_live_resource__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_23'] = x__to_live_resource__mutmut_23 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_24'] = x__to_live_resource__mutmut_24 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_25'] = x__to_live_resource__mutmut_25 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_26'] = x__to_live_resource__mutmut_26 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_27'] = x__to_live_resource__mutmut_27 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_28'] = x__to_live_resource__mutmut_28 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_29'] = x__to_live_resource__mutmut_29 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_30'] = x__to_live_resource__mutmut_30 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_31'] = x__to_live_resource__mutmut_31 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_32'] = x__to_live_resource__mutmut_32 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_33'] = x__to_live_resource__mutmut_33 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_34'] = x__to_live_resource__mutmut_34 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_35'] = x__to_live_resource__mutmut_35 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_36'] = x__to_live_resource__mutmut_36 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_37'] = x__to_live_resource__mutmut_37 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_38'] = x__to_live_resource__mutmut_38 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_39'] = x__to_live_resource__mutmut_39 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_40'] = x__to_live_resource__mutmut_40 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_41'] = x__to_live_resource__mutmut_41 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_42'] = x__to_live_resource__mutmut_42 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_43'] = x__to_live_resource__mutmut_43 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_44'] = x__to_live_resource__mutmut_44 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_45'] = x__to_live_resource__mutmut_45 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_46'] = x__to_live_resource__mutmut_46 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_47'] = x__to_live_resource__mutmut_47 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_48'] = x__to_live_resource__mutmut_48 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_49'] = x__to_live_resource__mutmut_49 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_50'] = x__to_live_resource__mutmut_50 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_51'] = x__to_live_resource__mutmut_51 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_52'] = x__to_live_resource__mutmut_52 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_53'] = x__to_live_resource__mutmut_53 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_54'] = x__to_live_resource__mutmut_54 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_55'] = x__to_live_resource__mutmut_55 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_56'] = x__to_live_resource__mutmut_56 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_57'] = x__to_live_resource__mutmut_57 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_58'] = x__to_live_resource__mutmut_58 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_59'] = x__to_live_resource__mutmut_59 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_60'] = x__to_live_resource__mutmut_60 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_61'] = x__to_live_resource__mutmut_61 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_62'] = x__to_live_resource__mutmut_62 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_63'] = x__to_live_resource__mutmut_63 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_64'] = x__to_live_resource__mutmut_64 # type: ignore # mutmut generated
mutants_x__to_live_resource__mutmut['x__to_live_resource__mutmut_65'] = x__to_live_resource__mutmut_65 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__translate_error__mutmut)
def _translate_error(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list cluster resources")
    return ClusterUnreachableError(f"Cannot list cluster resources: {exc}")


def x__translate_error__mutmut_orig(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list cluster resources")
    return ClusterUnreachableError(f"Cannot list cluster resources: {exc}")


def x__translate_error__mutmut_1(exc: Exception) -> Exception:
    status = None
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list cluster resources")
    return ClusterUnreachableError(f"Cannot list cluster resources: {exc}")


def x__translate_error__mutmut_2(exc: Exception) -> Exception:
    status = getattr(None, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list cluster resources")
    return ClusterUnreachableError(f"Cannot list cluster resources: {exc}")


def x__translate_error__mutmut_3(exc: Exception) -> Exception:
    status = getattr(exc, None, None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list cluster resources")
    return ClusterUnreachableError(f"Cannot list cluster resources: {exc}")


def x__translate_error__mutmut_4(exc: Exception) -> Exception:
    status = getattr("status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list cluster resources")
    return ClusterUnreachableError(f"Cannot list cluster resources: {exc}")


def x__translate_error__mutmut_5(exc: Exception) -> Exception:
    status = getattr(exc, None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list cluster resources")
    return ClusterUnreachableError(f"Cannot list cluster resources: {exc}")


def x__translate_error__mutmut_6(exc: Exception) -> Exception:
    status = getattr(exc, "status", )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list cluster resources")
    return ClusterUnreachableError(f"Cannot list cluster resources: {exc}")


def x__translate_error__mutmut_7(exc: Exception) -> Exception:
    status = getattr(exc, "XXstatusXX", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list cluster resources")
    return ClusterUnreachableError(f"Cannot list cluster resources: {exc}")


def x__translate_error__mutmut_8(exc: Exception) -> Exception:
    status = getattr(exc, "STATUS", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list cluster resources")
    return ClusterUnreachableError(f"Cannot list cluster resources: {exc}")


def x__translate_error__mutmut_9(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status != _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list cluster resources")
    return ClusterUnreachableError(f"Cannot list cluster resources: {exc}")


def x__translate_error__mutmut_10(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(None)
    return ClusterUnreachableError(f"Cannot list cluster resources: {exc}")


def x__translate_error__mutmut_11(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("XXRBAC denied access to list cluster resourcesXX")
    return ClusterUnreachableError(f"Cannot list cluster resources: {exc}")


def x__translate_error__mutmut_12(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("rbac denied access to list cluster resources")
    return ClusterUnreachableError(f"Cannot list cluster resources: {exc}")


def x__translate_error__mutmut_13(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC DENIED ACCESS TO LIST CLUSTER RESOURCES")
    return ClusterUnreachableError(f"Cannot list cluster resources: {exc}")


def x__translate_error__mutmut_14(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list cluster resources")
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
