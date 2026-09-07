from __future__ import annotations

from typing import Any

from hexawyn.application.ports.driven.image_drift_port import (
    ImageDriftPort,
    ResolvedContainerImageRaw,
)
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError

_K8S_FORBIDDEN = 403


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut: MutantDict = {}  # type: ignore


class KubernetesImageDriftAdapter(ImageDriftPort):
    """Secondary adapter — resolves each running container's actually-pulled
    image digest (`pod.status.containerStatuses[].imageID`, populated by the
    kubelet after every successful pull, no registry auth needed to read it)
    by joining Pods to their owning Deployment via label-selector match."""

    @_mutmut_mutated(mutants_xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut)
    def list_resolved_container_images(self, namespace: str) -> list[ResolvedContainerImageRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
            pods = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        results: list[ResolvedContainerImageRaw] = []
        for deployment in deployments.items:
            deployment_name = deployment.metadata.name
            selector = _match_labels(deployment)
            for pod in pods.items:
                if not _matches_selector(pod.metadata.labels or {}, selector):
                    continue
                for status in pod.status.container_statuses or []:
                    if not status.image_id:
                        continue
                    results.append(
                        ResolvedContainerImageRaw(
                            deployment=deployment_name,
                            namespace=namespace,
                            container=status.name,
                            image_id=status.image_id,
                        )
                    )
        return results

    def xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_orig(self, namespace: str) -> list[ResolvedContainerImageRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
            pods = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        results: list[ResolvedContainerImageRaw] = []
        for deployment in deployments.items:
            deployment_name = deployment.metadata.name
            selector = _match_labels(deployment)
            for pod in pods.items:
                if not _matches_selector(pod.metadata.labels or {}, selector):
                    continue
                for status in pod.status.container_statuses or []:
                    if not status.image_id:
                        continue
                    results.append(
                        ResolvedContainerImageRaw(
                            deployment=deployment_name,
                            namespace=namespace,
                            container=status.name,
                            image_id=status.image_id,
                        )
                    )
        return results

    def xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_1(self, namespace: str) -> list[ResolvedContainerImageRaw]:
        from kubernetes import client as k8s

        apps_api = None
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
            pods = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        results: list[ResolvedContainerImageRaw] = []
        for deployment in deployments.items:
            deployment_name = deployment.metadata.name
            selector = _match_labels(deployment)
            for pod in pods.items:
                if not _matches_selector(pod.metadata.labels or {}, selector):
                    continue
                for status in pod.status.container_statuses or []:
                    if not status.image_id:
                        continue
                    results.append(
                        ResolvedContainerImageRaw(
                            deployment=deployment_name,
                            namespace=namespace,
                            container=status.name,
                            image_id=status.image_id,
                        )
                    )
        return results

    def xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_2(self, namespace: str) -> list[ResolvedContainerImageRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = None

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
            pods = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        results: list[ResolvedContainerImageRaw] = []
        for deployment in deployments.items:
            deployment_name = deployment.metadata.name
            selector = _match_labels(deployment)
            for pod in pods.items:
                if not _matches_selector(pod.metadata.labels or {}, selector):
                    continue
                for status in pod.status.container_statuses or []:
                    if not status.image_id:
                        continue
                    results.append(
                        ResolvedContainerImageRaw(
                            deployment=deployment_name,
                            namespace=namespace,
                            container=status.name,
                            image_id=status.image_id,
                        )
                    )
        return results

    def xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_3(self, namespace: str) -> list[ResolvedContainerImageRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = None
            pods = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        results: list[ResolvedContainerImageRaw] = []
        for deployment in deployments.items:
            deployment_name = deployment.metadata.name
            selector = _match_labels(deployment)
            for pod in pods.items:
                if not _matches_selector(pod.metadata.labels or {}, selector):
                    continue
                for status in pod.status.container_statuses or []:
                    if not status.image_id:
                        continue
                    results.append(
                        ResolvedContainerImageRaw(
                            deployment=deployment_name,
                            namespace=namespace,
                            container=status.name,
                            image_id=status.image_id,
                        )
                    )
        return results

    def xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_4(self, namespace: str) -> list[ResolvedContainerImageRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=None)
            pods = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        results: list[ResolvedContainerImageRaw] = []
        for deployment in deployments.items:
            deployment_name = deployment.metadata.name
            selector = _match_labels(deployment)
            for pod in pods.items:
                if not _matches_selector(pod.metadata.labels or {}, selector):
                    continue
                for status in pod.status.container_statuses or []:
                    if not status.image_id:
                        continue
                    results.append(
                        ResolvedContainerImageRaw(
                            deployment=deployment_name,
                            namespace=namespace,
                            container=status.name,
                            image_id=status.image_id,
                        )
                    )
        return results

    def xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_5(self, namespace: str) -> list[ResolvedContainerImageRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
            pods = None
        except Exception as exc:
            raise _translate_error(exc) from exc

        results: list[ResolvedContainerImageRaw] = []
        for deployment in deployments.items:
            deployment_name = deployment.metadata.name
            selector = _match_labels(deployment)
            for pod in pods.items:
                if not _matches_selector(pod.metadata.labels or {}, selector):
                    continue
                for status in pod.status.container_statuses or []:
                    if not status.image_id:
                        continue
                    results.append(
                        ResolvedContainerImageRaw(
                            deployment=deployment_name,
                            namespace=namespace,
                            container=status.name,
                            image_id=status.image_id,
                        )
                    )
        return results

    def xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_6(self, namespace: str) -> list[ResolvedContainerImageRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
            pods = core_api.list_namespaced_pod(namespace=None)
        except Exception as exc:
            raise _translate_error(exc) from exc

        results: list[ResolvedContainerImageRaw] = []
        for deployment in deployments.items:
            deployment_name = deployment.metadata.name
            selector = _match_labels(deployment)
            for pod in pods.items:
                if not _matches_selector(pod.metadata.labels or {}, selector):
                    continue
                for status in pod.status.container_statuses or []:
                    if not status.image_id:
                        continue
                    results.append(
                        ResolvedContainerImageRaw(
                            deployment=deployment_name,
                            namespace=namespace,
                            container=status.name,
                            image_id=status.image_id,
                        )
                    )
        return results

    def xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_7(self, namespace: str) -> list[ResolvedContainerImageRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
            pods = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            raise _translate_error(None) from exc

        results: list[ResolvedContainerImageRaw] = []
        for deployment in deployments.items:
            deployment_name = deployment.metadata.name
            selector = _match_labels(deployment)
            for pod in pods.items:
                if not _matches_selector(pod.metadata.labels or {}, selector):
                    continue
                for status in pod.status.container_statuses or []:
                    if not status.image_id:
                        continue
                    results.append(
                        ResolvedContainerImageRaw(
                            deployment=deployment_name,
                            namespace=namespace,
                            container=status.name,
                            image_id=status.image_id,
                        )
                    )
        return results

    def xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_8(self, namespace: str) -> list[ResolvedContainerImageRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
            pods = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        results: list[ResolvedContainerImageRaw] = None
        for deployment in deployments.items:
            deployment_name = deployment.metadata.name
            selector = _match_labels(deployment)
            for pod in pods.items:
                if not _matches_selector(pod.metadata.labels or {}, selector):
                    continue
                for status in pod.status.container_statuses or []:
                    if not status.image_id:
                        continue
                    results.append(
                        ResolvedContainerImageRaw(
                            deployment=deployment_name,
                            namespace=namespace,
                            container=status.name,
                            image_id=status.image_id,
                        )
                    )
        return results

    def xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_9(self, namespace: str) -> list[ResolvedContainerImageRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
            pods = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        results: list[ResolvedContainerImageRaw] = []
        for deployment in deployments.items:
            deployment_name = None
            selector = _match_labels(deployment)
            for pod in pods.items:
                if not _matches_selector(pod.metadata.labels or {}, selector):
                    continue
                for status in pod.status.container_statuses or []:
                    if not status.image_id:
                        continue
                    results.append(
                        ResolvedContainerImageRaw(
                            deployment=deployment_name,
                            namespace=namespace,
                            container=status.name,
                            image_id=status.image_id,
                        )
                    )
        return results

    def xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_10(self, namespace: str) -> list[ResolvedContainerImageRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
            pods = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        results: list[ResolvedContainerImageRaw] = []
        for deployment in deployments.items:
            deployment_name = deployment.metadata.name
            selector = None
            for pod in pods.items:
                if not _matches_selector(pod.metadata.labels or {}, selector):
                    continue
                for status in pod.status.container_statuses or []:
                    if not status.image_id:
                        continue
                    results.append(
                        ResolvedContainerImageRaw(
                            deployment=deployment_name,
                            namespace=namespace,
                            container=status.name,
                            image_id=status.image_id,
                        )
                    )
        return results

    def xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_11(self, namespace: str) -> list[ResolvedContainerImageRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
            pods = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        results: list[ResolvedContainerImageRaw] = []
        for deployment in deployments.items:
            deployment_name = deployment.metadata.name
            selector = _match_labels(None)
            for pod in pods.items:
                if not _matches_selector(pod.metadata.labels or {}, selector):
                    continue
                for status in pod.status.container_statuses or []:
                    if not status.image_id:
                        continue
                    results.append(
                        ResolvedContainerImageRaw(
                            deployment=deployment_name,
                            namespace=namespace,
                            container=status.name,
                            image_id=status.image_id,
                        )
                    )
        return results

    def xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_12(self, namespace: str) -> list[ResolvedContainerImageRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
            pods = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        results: list[ResolvedContainerImageRaw] = []
        for deployment in deployments.items:
            deployment_name = deployment.metadata.name
            selector = _match_labels(deployment)
            for pod in pods.items:
                if _matches_selector(pod.metadata.labels or {}, selector):
                    continue
                for status in pod.status.container_statuses or []:
                    if not status.image_id:
                        continue
                    results.append(
                        ResolvedContainerImageRaw(
                            deployment=deployment_name,
                            namespace=namespace,
                            container=status.name,
                            image_id=status.image_id,
                        )
                    )
        return results

    def xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_13(self, namespace: str) -> list[ResolvedContainerImageRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
            pods = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        results: list[ResolvedContainerImageRaw] = []
        for deployment in deployments.items:
            deployment_name = deployment.metadata.name
            selector = _match_labels(deployment)
            for pod in pods.items:
                if not _matches_selector(None, selector):
                    continue
                for status in pod.status.container_statuses or []:
                    if not status.image_id:
                        continue
                    results.append(
                        ResolvedContainerImageRaw(
                            deployment=deployment_name,
                            namespace=namespace,
                            container=status.name,
                            image_id=status.image_id,
                        )
                    )
        return results

    def xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_14(self, namespace: str) -> list[ResolvedContainerImageRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
            pods = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        results: list[ResolvedContainerImageRaw] = []
        for deployment in deployments.items:
            deployment_name = deployment.metadata.name
            selector = _match_labels(deployment)
            for pod in pods.items:
                if not _matches_selector(pod.metadata.labels or {}, None):
                    continue
                for status in pod.status.container_statuses or []:
                    if not status.image_id:
                        continue
                    results.append(
                        ResolvedContainerImageRaw(
                            deployment=deployment_name,
                            namespace=namespace,
                            container=status.name,
                            image_id=status.image_id,
                        )
                    )
        return results

    def xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_15(self, namespace: str) -> list[ResolvedContainerImageRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
            pods = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        results: list[ResolvedContainerImageRaw] = []
        for deployment in deployments.items:
            deployment_name = deployment.metadata.name
            selector = _match_labels(deployment)
            for pod in pods.items:
                if not _matches_selector(selector):
                    continue
                for status in pod.status.container_statuses or []:
                    if not status.image_id:
                        continue
                    results.append(
                        ResolvedContainerImageRaw(
                            deployment=deployment_name,
                            namespace=namespace,
                            container=status.name,
                            image_id=status.image_id,
                        )
                    )
        return results

    def xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_16(self, namespace: str) -> list[ResolvedContainerImageRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
            pods = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        results: list[ResolvedContainerImageRaw] = []
        for deployment in deployments.items:
            deployment_name = deployment.metadata.name
            selector = _match_labels(deployment)
            for pod in pods.items:
                if not _matches_selector(pod.metadata.labels or {}, ):
                    continue
                for status in pod.status.container_statuses or []:
                    if not status.image_id:
                        continue
                    results.append(
                        ResolvedContainerImageRaw(
                            deployment=deployment_name,
                            namespace=namespace,
                            container=status.name,
                            image_id=status.image_id,
                        )
                    )
        return results

    def xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_17(self, namespace: str) -> list[ResolvedContainerImageRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
            pods = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        results: list[ResolvedContainerImageRaw] = []
        for deployment in deployments.items:
            deployment_name = deployment.metadata.name
            selector = _match_labels(deployment)
            for pod in pods.items:
                if not _matches_selector(pod.metadata.labels and {}, selector):
                    continue
                for status in pod.status.container_statuses or []:
                    if not status.image_id:
                        continue
                    results.append(
                        ResolvedContainerImageRaw(
                            deployment=deployment_name,
                            namespace=namespace,
                            container=status.name,
                            image_id=status.image_id,
                        )
                    )
        return results

    def xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_18(self, namespace: str) -> list[ResolvedContainerImageRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
            pods = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        results: list[ResolvedContainerImageRaw] = []
        for deployment in deployments.items:
            deployment_name = deployment.metadata.name
            selector = _match_labels(deployment)
            for pod in pods.items:
                if not _matches_selector(pod.metadata.labels or {}, selector):
                    break
                for status in pod.status.container_statuses or []:
                    if not status.image_id:
                        continue
                    results.append(
                        ResolvedContainerImageRaw(
                            deployment=deployment_name,
                            namespace=namespace,
                            container=status.name,
                            image_id=status.image_id,
                        )
                    )
        return results

    def xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_19(self, namespace: str) -> list[ResolvedContainerImageRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
            pods = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        results: list[ResolvedContainerImageRaw] = []
        for deployment in deployments.items:
            deployment_name = deployment.metadata.name
            selector = _match_labels(deployment)
            for pod in pods.items:
                if not _matches_selector(pod.metadata.labels or {}, selector):
                    continue
                for status in pod.status.container_statuses and []:
                    if not status.image_id:
                        continue
                    results.append(
                        ResolvedContainerImageRaw(
                            deployment=deployment_name,
                            namespace=namespace,
                            container=status.name,
                            image_id=status.image_id,
                        )
                    )
        return results

    def xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_20(self, namespace: str) -> list[ResolvedContainerImageRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
            pods = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        results: list[ResolvedContainerImageRaw] = []
        for deployment in deployments.items:
            deployment_name = deployment.metadata.name
            selector = _match_labels(deployment)
            for pod in pods.items:
                if not _matches_selector(pod.metadata.labels or {}, selector):
                    continue
                for status in pod.status.container_statuses or []:
                    if status.image_id:
                        continue
                    results.append(
                        ResolvedContainerImageRaw(
                            deployment=deployment_name,
                            namespace=namespace,
                            container=status.name,
                            image_id=status.image_id,
                        )
                    )
        return results

    def xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_21(self, namespace: str) -> list[ResolvedContainerImageRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
            pods = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        results: list[ResolvedContainerImageRaw] = []
        for deployment in deployments.items:
            deployment_name = deployment.metadata.name
            selector = _match_labels(deployment)
            for pod in pods.items:
                if not _matches_selector(pod.metadata.labels or {}, selector):
                    continue
                for status in pod.status.container_statuses or []:
                    if not status.image_id:
                        break
                    results.append(
                        ResolvedContainerImageRaw(
                            deployment=deployment_name,
                            namespace=namespace,
                            container=status.name,
                            image_id=status.image_id,
                        )
                    )
        return results

    def xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_22(self, namespace: str) -> list[ResolvedContainerImageRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
            pods = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        results: list[ResolvedContainerImageRaw] = []
        for deployment in deployments.items:
            deployment_name = deployment.metadata.name
            selector = _match_labels(deployment)
            for pod in pods.items:
                if not _matches_selector(pod.metadata.labels or {}, selector):
                    continue
                for status in pod.status.container_statuses or []:
                    if not status.image_id:
                        continue
                    results.append(
                        None
                    )
        return results

    def xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_23(self, namespace: str) -> list[ResolvedContainerImageRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
            pods = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        results: list[ResolvedContainerImageRaw] = []
        for deployment in deployments.items:
            deployment_name = deployment.metadata.name
            selector = _match_labels(deployment)
            for pod in pods.items:
                if not _matches_selector(pod.metadata.labels or {}, selector):
                    continue
                for status in pod.status.container_statuses or []:
                    if not status.image_id:
                        continue
                    results.append(
                        ResolvedContainerImageRaw(
                            deployment=None,
                            namespace=namespace,
                            container=status.name,
                            image_id=status.image_id,
                        )
                    )
        return results

    def xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_24(self, namespace: str) -> list[ResolvedContainerImageRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
            pods = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        results: list[ResolvedContainerImageRaw] = []
        for deployment in deployments.items:
            deployment_name = deployment.metadata.name
            selector = _match_labels(deployment)
            for pod in pods.items:
                if not _matches_selector(pod.metadata.labels or {}, selector):
                    continue
                for status in pod.status.container_statuses or []:
                    if not status.image_id:
                        continue
                    results.append(
                        ResolvedContainerImageRaw(
                            deployment=deployment_name,
                            namespace=None,
                            container=status.name,
                            image_id=status.image_id,
                        )
                    )
        return results

    def xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_25(self, namespace: str) -> list[ResolvedContainerImageRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
            pods = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        results: list[ResolvedContainerImageRaw] = []
        for deployment in deployments.items:
            deployment_name = deployment.metadata.name
            selector = _match_labels(deployment)
            for pod in pods.items:
                if not _matches_selector(pod.metadata.labels or {}, selector):
                    continue
                for status in pod.status.container_statuses or []:
                    if not status.image_id:
                        continue
                    results.append(
                        ResolvedContainerImageRaw(
                            deployment=deployment_name,
                            namespace=namespace,
                            container=None,
                            image_id=status.image_id,
                        )
                    )
        return results

    def xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_26(self, namespace: str) -> list[ResolvedContainerImageRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
            pods = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        results: list[ResolvedContainerImageRaw] = []
        for deployment in deployments.items:
            deployment_name = deployment.metadata.name
            selector = _match_labels(deployment)
            for pod in pods.items:
                if not _matches_selector(pod.metadata.labels or {}, selector):
                    continue
                for status in pod.status.container_statuses or []:
                    if not status.image_id:
                        continue
                    results.append(
                        ResolvedContainerImageRaw(
                            deployment=deployment_name,
                            namespace=namespace,
                            container=status.name,
                            image_id=None,
                        )
                    )
        return results

    def xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_27(self, namespace: str) -> list[ResolvedContainerImageRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
            pods = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        results: list[ResolvedContainerImageRaw] = []
        for deployment in deployments.items:
            deployment_name = deployment.metadata.name
            selector = _match_labels(deployment)
            for pod in pods.items:
                if not _matches_selector(pod.metadata.labels or {}, selector):
                    continue
                for status in pod.status.container_statuses or []:
                    if not status.image_id:
                        continue
                    results.append(
                        ResolvedContainerImageRaw(
                            namespace=namespace,
                            container=status.name,
                            image_id=status.image_id,
                        )
                    )
        return results

    def xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_28(self, namespace: str) -> list[ResolvedContainerImageRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
            pods = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        results: list[ResolvedContainerImageRaw] = []
        for deployment in deployments.items:
            deployment_name = deployment.metadata.name
            selector = _match_labels(deployment)
            for pod in pods.items:
                if not _matches_selector(pod.metadata.labels or {}, selector):
                    continue
                for status in pod.status.container_statuses or []:
                    if not status.image_id:
                        continue
                    results.append(
                        ResolvedContainerImageRaw(
                            deployment=deployment_name,
                            container=status.name,
                            image_id=status.image_id,
                        )
                    )
        return results

    def xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_29(self, namespace: str) -> list[ResolvedContainerImageRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
            pods = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        results: list[ResolvedContainerImageRaw] = []
        for deployment in deployments.items:
            deployment_name = deployment.metadata.name
            selector = _match_labels(deployment)
            for pod in pods.items:
                if not _matches_selector(pod.metadata.labels or {}, selector):
                    continue
                for status in pod.status.container_statuses or []:
                    if not status.image_id:
                        continue
                    results.append(
                        ResolvedContainerImageRaw(
                            deployment=deployment_name,
                            namespace=namespace,
                            image_id=status.image_id,
                        )
                    )
        return results

    def xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_30(self, namespace: str) -> list[ResolvedContainerImageRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()

        try:
            deployments = apps_api.list_namespaced_deployment(namespace=namespace)
            pods = core_api.list_namespaced_pod(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        results: list[ResolvedContainerImageRaw] = []
        for deployment in deployments.items:
            deployment_name = deployment.metadata.name
            selector = _match_labels(deployment)
            for pod in pods.items:
                if not _matches_selector(pod.metadata.labels or {}, selector):
                    continue
                for status in pod.status.container_statuses or []:
                    if not status.image_id:
                        continue
                    results.append(
                        ResolvedContainerImageRaw(
                            deployment=deployment_name,
                            namespace=namespace,
                            container=status.name,
                            )
                    )
        return results

mutants_xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut['_mutmut_orig'] = KubernetesImageDriftAdapter.xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut['xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_1'] = KubernetesImageDriftAdapter.xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut['xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_2'] = KubernetesImageDriftAdapter.xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut['xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_3'] = KubernetesImageDriftAdapter.xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut['xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_4'] = KubernetesImageDriftAdapter.xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut['xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_5'] = KubernetesImageDriftAdapter.xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut['xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_6'] = KubernetesImageDriftAdapter.xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut['xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_7'] = KubernetesImageDriftAdapter.xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut['xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_8'] = KubernetesImageDriftAdapter.xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut['xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_9'] = KubernetesImageDriftAdapter.xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut['xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_10'] = KubernetesImageDriftAdapter.xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut['xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_11'] = KubernetesImageDriftAdapter.xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut['xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_12'] = KubernetesImageDriftAdapter.xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut['xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_13'] = KubernetesImageDriftAdapter.xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut['xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_14'] = KubernetesImageDriftAdapter.xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_14 # type: ignore # mutmut generated
mutants_xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut['xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_15'] = KubernetesImageDriftAdapter.xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_15 # type: ignore # mutmut generated
mutants_xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut['xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_16'] = KubernetesImageDriftAdapter.xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_16 # type: ignore # mutmut generated
mutants_xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut['xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_17'] = KubernetesImageDriftAdapter.xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_17 # type: ignore # mutmut generated
mutants_xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut['xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_18'] = KubernetesImageDriftAdapter.xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_18 # type: ignore # mutmut generated
mutants_xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut['xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_19'] = KubernetesImageDriftAdapter.xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_19 # type: ignore # mutmut generated
mutants_xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut['xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_20'] = KubernetesImageDriftAdapter.xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_20 # type: ignore # mutmut generated
mutants_xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut['xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_21'] = KubernetesImageDriftAdapter.xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_21 # type: ignore # mutmut generated
mutants_xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut['xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_22'] = KubernetesImageDriftAdapter.xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_22 # type: ignore # mutmut generated
mutants_xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut['xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_23'] = KubernetesImageDriftAdapter.xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_23 # type: ignore # mutmut generated
mutants_xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut['xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_24'] = KubernetesImageDriftAdapter.xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_24 # type: ignore # mutmut generated
mutants_xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut['xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_25'] = KubernetesImageDriftAdapter.xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_25 # type: ignore # mutmut generated
mutants_xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut['xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_26'] = KubernetesImageDriftAdapter.xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_26 # type: ignore # mutmut generated
mutants_xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut['xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_27'] = KubernetesImageDriftAdapter.xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_27 # type: ignore # mutmut generated
mutants_xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut['xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_28'] = KubernetesImageDriftAdapter.xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_28 # type: ignore # mutmut generated
mutants_xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut['xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_29'] = KubernetesImageDriftAdapter.xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_29 # type: ignore # mutmut generated
mutants_xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut['xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_30'] = KubernetesImageDriftAdapter.xǁKubernetesImageDriftAdapterǁlist_resolved_container_images__mutmut_30 # type: ignore # mutmut generated
mutants_x__match_labels__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__match_labels__mutmut)
def _match_labels(deployment: Any) -> dict[str, str]:
    selector = getattr(deployment.spec, "selector", None)
    match_labels = getattr(selector, "match_labels", None)
    return dict(match_labels or {})


def x__match_labels__mutmut_orig(deployment: Any) -> dict[str, str]:
    selector = getattr(deployment.spec, "selector", None)
    match_labels = getattr(selector, "match_labels", None)
    return dict(match_labels or {})


def x__match_labels__mutmut_1(deployment: Any) -> dict[str, str]:
    selector = None
    match_labels = getattr(selector, "match_labels", None)
    return dict(match_labels or {})


def x__match_labels__mutmut_2(deployment: Any) -> dict[str, str]:
    selector = getattr(None, "selector", None)
    match_labels = getattr(selector, "match_labels", None)
    return dict(match_labels or {})


def x__match_labels__mutmut_3(deployment: Any) -> dict[str, str]:
    selector = getattr(deployment.spec, None, None)
    match_labels = getattr(selector, "match_labels", None)
    return dict(match_labels or {})


def x__match_labels__mutmut_4(deployment: Any) -> dict[str, str]:
    selector = getattr("selector", None)
    match_labels = getattr(selector, "match_labels", None)
    return dict(match_labels or {})


def x__match_labels__mutmut_5(deployment: Any) -> dict[str, str]:
    selector = getattr(deployment.spec, None)
    match_labels = getattr(selector, "match_labels", None)
    return dict(match_labels or {})


def x__match_labels__mutmut_6(deployment: Any) -> dict[str, str]:
    selector = getattr(deployment.spec, "selector", )
    match_labels = getattr(selector, "match_labels", None)
    return dict(match_labels or {})


def x__match_labels__mutmut_7(deployment: Any) -> dict[str, str]:
    selector = getattr(deployment.spec, "XXselectorXX", None)
    match_labels = getattr(selector, "match_labels", None)
    return dict(match_labels or {})


def x__match_labels__mutmut_8(deployment: Any) -> dict[str, str]:
    selector = getattr(deployment.spec, "SELECTOR", None)
    match_labels = getattr(selector, "match_labels", None)
    return dict(match_labels or {})


def x__match_labels__mutmut_9(deployment: Any) -> dict[str, str]:
    selector = getattr(deployment.spec, "selector", None)
    match_labels = None
    return dict(match_labels or {})


def x__match_labels__mutmut_10(deployment: Any) -> dict[str, str]:
    selector = getattr(deployment.spec, "selector", None)
    match_labels = getattr(None, "match_labels", None)
    return dict(match_labels or {})


def x__match_labels__mutmut_11(deployment: Any) -> dict[str, str]:
    selector = getattr(deployment.spec, "selector", None)
    match_labels = getattr(selector, None, None)
    return dict(match_labels or {})


def x__match_labels__mutmut_12(deployment: Any) -> dict[str, str]:
    selector = getattr(deployment.spec, "selector", None)
    match_labels = getattr("match_labels", None)
    return dict(match_labels or {})


def x__match_labels__mutmut_13(deployment: Any) -> dict[str, str]:
    selector = getattr(deployment.spec, "selector", None)
    match_labels = getattr(selector, None)
    return dict(match_labels or {})


def x__match_labels__mutmut_14(deployment: Any) -> dict[str, str]:
    selector = getattr(deployment.spec, "selector", None)
    match_labels = getattr(selector, "match_labels", )
    return dict(match_labels or {})


def x__match_labels__mutmut_15(deployment: Any) -> dict[str, str]:
    selector = getattr(deployment.spec, "selector", None)
    match_labels = getattr(selector, "XXmatch_labelsXX", None)
    return dict(match_labels or {})


def x__match_labels__mutmut_16(deployment: Any) -> dict[str, str]:
    selector = getattr(deployment.spec, "selector", None)
    match_labels = getattr(selector, "MATCH_LABELS", None)
    return dict(match_labels or {})


def x__match_labels__mutmut_17(deployment: Any) -> dict[str, str]:
    selector = getattr(deployment.spec, "selector", None)
    match_labels = getattr(selector, "match_labels", None)
    return dict(None)


def x__match_labels__mutmut_18(deployment: Any) -> dict[str, str]:
    selector = getattr(deployment.spec, "selector", None)
    match_labels = getattr(selector, "match_labels", None)
    return dict(match_labels and {})

mutants_x__match_labels__mutmut['_mutmut_orig'] = x__match_labels__mutmut_orig # type: ignore # mutmut generated
mutants_x__match_labels__mutmut['x__match_labels__mutmut_1'] = x__match_labels__mutmut_1 # type: ignore # mutmut generated
mutants_x__match_labels__mutmut['x__match_labels__mutmut_2'] = x__match_labels__mutmut_2 # type: ignore # mutmut generated
mutants_x__match_labels__mutmut['x__match_labels__mutmut_3'] = x__match_labels__mutmut_3 # type: ignore # mutmut generated
mutants_x__match_labels__mutmut['x__match_labels__mutmut_4'] = x__match_labels__mutmut_4 # type: ignore # mutmut generated
mutants_x__match_labels__mutmut['x__match_labels__mutmut_5'] = x__match_labels__mutmut_5 # type: ignore # mutmut generated
mutants_x__match_labels__mutmut['x__match_labels__mutmut_6'] = x__match_labels__mutmut_6 # type: ignore # mutmut generated
mutants_x__match_labels__mutmut['x__match_labels__mutmut_7'] = x__match_labels__mutmut_7 # type: ignore # mutmut generated
mutants_x__match_labels__mutmut['x__match_labels__mutmut_8'] = x__match_labels__mutmut_8 # type: ignore # mutmut generated
mutants_x__match_labels__mutmut['x__match_labels__mutmut_9'] = x__match_labels__mutmut_9 # type: ignore # mutmut generated
mutants_x__match_labels__mutmut['x__match_labels__mutmut_10'] = x__match_labels__mutmut_10 # type: ignore # mutmut generated
mutants_x__match_labels__mutmut['x__match_labels__mutmut_11'] = x__match_labels__mutmut_11 # type: ignore # mutmut generated
mutants_x__match_labels__mutmut['x__match_labels__mutmut_12'] = x__match_labels__mutmut_12 # type: ignore # mutmut generated
mutants_x__match_labels__mutmut['x__match_labels__mutmut_13'] = x__match_labels__mutmut_13 # type: ignore # mutmut generated
mutants_x__match_labels__mutmut['x__match_labels__mutmut_14'] = x__match_labels__mutmut_14 # type: ignore # mutmut generated
mutants_x__match_labels__mutmut['x__match_labels__mutmut_15'] = x__match_labels__mutmut_15 # type: ignore # mutmut generated
mutants_x__match_labels__mutmut['x__match_labels__mutmut_16'] = x__match_labels__mutmut_16 # type: ignore # mutmut generated
mutants_x__match_labels__mutmut['x__match_labels__mutmut_17'] = x__match_labels__mutmut_17 # type: ignore # mutmut generated
mutants_x__match_labels__mutmut['x__match_labels__mutmut_18'] = x__match_labels__mutmut_18 # type: ignore # mutmut generated
mutants_x__matches_selector__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__matches_selector__mutmut)
def _matches_selector(labels: dict[str, str], selector: dict[str, str]) -> bool:
    return all(labels.get(key) == value for key, value in selector.items())


def x__matches_selector__mutmut_orig(labels: dict[str, str], selector: dict[str, str]) -> bool:
    return all(labels.get(key) == value for key, value in selector.items())


def x__matches_selector__mutmut_1(labels: dict[str, str], selector: dict[str, str]) -> bool:
    return all(None)


def x__matches_selector__mutmut_2(labels: dict[str, str], selector: dict[str, str]) -> bool:
    return all(labels.get(None) == value for key, value in selector.items())


def x__matches_selector__mutmut_3(labels: dict[str, str], selector: dict[str, str]) -> bool:
    return all(labels.get(key) != value for key, value in selector.items())

mutants_x__matches_selector__mutmut['_mutmut_orig'] = x__matches_selector__mutmut_orig # type: ignore # mutmut generated
mutants_x__matches_selector__mutmut['x__matches_selector__mutmut_1'] = x__matches_selector__mutmut_1 # type: ignore # mutmut generated
mutants_x__matches_selector__mutmut['x__matches_selector__mutmut_2'] = x__matches_selector__mutmut_2 # type: ignore # mutmut generated
mutants_x__matches_selector__mutmut['x__matches_selector__mutmut_3'] = x__matches_selector__mutmut_3 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__translate_error__mutmut)
def _translate_error(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list deployments/pods")
    return ClusterUnreachableError(f"Cannot list deployments/pods: {exc}")


def x__translate_error__mutmut_orig(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list deployments/pods")
    return ClusterUnreachableError(f"Cannot list deployments/pods: {exc}")


def x__translate_error__mutmut_1(exc: Exception) -> Exception:
    status = None
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list deployments/pods")
    return ClusterUnreachableError(f"Cannot list deployments/pods: {exc}")


def x__translate_error__mutmut_2(exc: Exception) -> Exception:
    status = getattr(None, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list deployments/pods")
    return ClusterUnreachableError(f"Cannot list deployments/pods: {exc}")


def x__translate_error__mutmut_3(exc: Exception) -> Exception:
    status = getattr(exc, None, None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list deployments/pods")
    return ClusterUnreachableError(f"Cannot list deployments/pods: {exc}")


def x__translate_error__mutmut_4(exc: Exception) -> Exception:
    status = getattr("status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list deployments/pods")
    return ClusterUnreachableError(f"Cannot list deployments/pods: {exc}")


def x__translate_error__mutmut_5(exc: Exception) -> Exception:
    status = getattr(exc, None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list deployments/pods")
    return ClusterUnreachableError(f"Cannot list deployments/pods: {exc}")


def x__translate_error__mutmut_6(exc: Exception) -> Exception:
    status = getattr(exc, "status", )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list deployments/pods")
    return ClusterUnreachableError(f"Cannot list deployments/pods: {exc}")


def x__translate_error__mutmut_7(exc: Exception) -> Exception:
    status = getattr(exc, "XXstatusXX", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list deployments/pods")
    return ClusterUnreachableError(f"Cannot list deployments/pods: {exc}")


def x__translate_error__mutmut_8(exc: Exception) -> Exception:
    status = getattr(exc, "STATUS", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list deployments/pods")
    return ClusterUnreachableError(f"Cannot list deployments/pods: {exc}")


def x__translate_error__mutmut_9(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status != _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list deployments/pods")
    return ClusterUnreachableError(f"Cannot list deployments/pods: {exc}")


def x__translate_error__mutmut_10(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(None)
    return ClusterUnreachableError(f"Cannot list deployments/pods: {exc}")


def x__translate_error__mutmut_11(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("XXRBAC denied access to list deployments/podsXX")
    return ClusterUnreachableError(f"Cannot list deployments/pods: {exc}")


def x__translate_error__mutmut_12(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("rbac denied access to list deployments/pods")
    return ClusterUnreachableError(f"Cannot list deployments/pods: {exc}")


def x__translate_error__mutmut_13(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC DENIED ACCESS TO LIST DEPLOYMENTS/PODS")
    return ClusterUnreachableError(f"Cannot list deployments/pods: {exc}")


def x__translate_error__mutmut_14(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list deployments/pods")
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
