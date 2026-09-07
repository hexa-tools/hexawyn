from __future__ import annotations

from typing import Any

from hexawyn.application.ports.driven.image_inventory_port import (
    ImageInventoryPort,
    RunningImageRaw,
)
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError

_K8S_FORBIDDEN = 403


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁKubernetesImageInventoryAdapterǁlist_running_images__mutmut: MutantDict = {}  # type: ignore


class KubernetesImageInventoryAdapter(ImageInventoryPort):
    """Secondary adapter — enumerates every unique container image currently
    running in the cluster, covering init, regular, and ephemeral containers."""

    @_mutmut_mutated(mutants_xǁKubernetesImageInventoryAdapterǁlist_running_images__mutmut)
    def list_running_images(self) -> list[RunningImageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        images: list[RunningImageRaw] = []
        for pod in result.items:
            images.extend(_to_running_images(pod))
        return images

    def xǁKubernetesImageInventoryAdapterǁlist_running_images__mutmut_orig(self) -> list[RunningImageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        images: list[RunningImageRaw] = []
        for pod in result.items:
            images.extend(_to_running_images(pod))
        return images

    def xǁKubernetesImageInventoryAdapterǁlist_running_images__mutmut_1(self) -> list[RunningImageRaw]:
        from kubernetes import client as k8s

        core_api = None
        try:
            result = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        images: list[RunningImageRaw] = []
        for pod in result.items:
            images.extend(_to_running_images(pod))
        return images

    def xǁKubernetesImageInventoryAdapterǁlist_running_images__mutmut_2(self) -> list[RunningImageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = None
        except Exception as exc:
            raise _translate_error(exc) from exc

        images: list[RunningImageRaw] = []
        for pod in result.items:
            images.extend(_to_running_images(pod))
        return images

    def xǁKubernetesImageInventoryAdapterǁlist_running_images__mutmut_3(self) -> list[RunningImageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(None) from exc

        images: list[RunningImageRaw] = []
        for pod in result.items:
            images.extend(_to_running_images(pod))
        return images

    def xǁKubernetesImageInventoryAdapterǁlist_running_images__mutmut_4(self) -> list[RunningImageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        images: list[RunningImageRaw] = None
        for pod in result.items:
            images.extend(_to_running_images(pod))
        return images

    def xǁKubernetesImageInventoryAdapterǁlist_running_images__mutmut_5(self) -> list[RunningImageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        images: list[RunningImageRaw] = []
        for pod in result.items:
            images.extend(None)
        return images

    def xǁKubernetesImageInventoryAdapterǁlist_running_images__mutmut_6(self) -> list[RunningImageRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        images: list[RunningImageRaw] = []
        for pod in result.items:
            images.extend(_to_running_images(None))
        return images

mutants_xǁKubernetesImageInventoryAdapterǁlist_running_images__mutmut['_mutmut_orig'] = KubernetesImageInventoryAdapter.xǁKubernetesImageInventoryAdapterǁlist_running_images__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesImageInventoryAdapterǁlist_running_images__mutmut['xǁKubernetesImageInventoryAdapterǁlist_running_images__mutmut_1'] = KubernetesImageInventoryAdapter.xǁKubernetesImageInventoryAdapterǁlist_running_images__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesImageInventoryAdapterǁlist_running_images__mutmut['xǁKubernetesImageInventoryAdapterǁlist_running_images__mutmut_2'] = KubernetesImageInventoryAdapter.xǁKubernetesImageInventoryAdapterǁlist_running_images__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesImageInventoryAdapterǁlist_running_images__mutmut['xǁKubernetesImageInventoryAdapterǁlist_running_images__mutmut_3'] = KubernetesImageInventoryAdapter.xǁKubernetesImageInventoryAdapterǁlist_running_images__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesImageInventoryAdapterǁlist_running_images__mutmut['xǁKubernetesImageInventoryAdapterǁlist_running_images__mutmut_4'] = KubernetesImageInventoryAdapter.xǁKubernetesImageInventoryAdapterǁlist_running_images__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesImageInventoryAdapterǁlist_running_images__mutmut['xǁKubernetesImageInventoryAdapterǁlist_running_images__mutmut_5'] = KubernetesImageInventoryAdapter.xǁKubernetesImageInventoryAdapterǁlist_running_images__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesImageInventoryAdapterǁlist_running_images__mutmut['xǁKubernetesImageInventoryAdapterǁlist_running_images__mutmut_6'] = KubernetesImageInventoryAdapter.xǁKubernetesImageInventoryAdapterǁlist_running_images__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_running_images__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_running_images__mutmut)
def _to_running_images(pod: Any) -> list[RunningImageRaw]:
    namespace = pod.metadata.namespace
    pod_name = pod.metadata.name
    containers = (
        list(pod.spec.init_containers or [])
        + list(pod.spec.containers or [])
        + list(pod.spec.ephemeral_containers or [])
    )
    return [
        RunningImageRaw(image=container.image, namespace=namespace, pod_name=pod_name)
        for container in containers
    ]


def x__to_running_images__mutmut_orig(pod: Any) -> list[RunningImageRaw]:
    namespace = pod.metadata.namespace
    pod_name = pod.metadata.name
    containers = (
        list(pod.spec.init_containers or [])
        + list(pod.spec.containers or [])
        + list(pod.spec.ephemeral_containers or [])
    )
    return [
        RunningImageRaw(image=container.image, namespace=namespace, pod_name=pod_name)
        for container in containers
    ]


def x__to_running_images__mutmut_1(pod: Any) -> list[RunningImageRaw]:
    namespace = None
    pod_name = pod.metadata.name
    containers = (
        list(pod.spec.init_containers or [])
        + list(pod.spec.containers or [])
        + list(pod.spec.ephemeral_containers or [])
    )
    return [
        RunningImageRaw(image=container.image, namespace=namespace, pod_name=pod_name)
        for container in containers
    ]


def x__to_running_images__mutmut_2(pod: Any) -> list[RunningImageRaw]:
    namespace = pod.metadata.namespace
    pod_name = None
    containers = (
        list(pod.spec.init_containers or [])
        + list(pod.spec.containers or [])
        + list(pod.spec.ephemeral_containers or [])
    )
    return [
        RunningImageRaw(image=container.image, namespace=namespace, pod_name=pod_name)
        for container in containers
    ]


def x__to_running_images__mutmut_3(pod: Any) -> list[RunningImageRaw]:
    namespace = pod.metadata.namespace
    pod_name = pod.metadata.name
    containers = None
    return [
        RunningImageRaw(image=container.image, namespace=namespace, pod_name=pod_name)
        for container in containers
    ]


def x__to_running_images__mutmut_4(pod: Any) -> list[RunningImageRaw]:
    namespace = pod.metadata.namespace
    pod_name = pod.metadata.name
    containers = (
        list(pod.spec.init_containers or [])
        + list(pod.spec.containers or []) - list(pod.spec.ephemeral_containers or [])
    )
    return [
        RunningImageRaw(image=container.image, namespace=namespace, pod_name=pod_name)
        for container in containers
    ]


def x__to_running_images__mutmut_5(pod: Any) -> list[RunningImageRaw]:
    namespace = pod.metadata.namespace
    pod_name = pod.metadata.name
    containers = (
        list(pod.spec.init_containers or []) - list(pod.spec.containers or [])
        + list(pod.spec.ephemeral_containers or [])
    )
    return [
        RunningImageRaw(image=container.image, namespace=namespace, pod_name=pod_name)
        for container in containers
    ]


def x__to_running_images__mutmut_6(pod: Any) -> list[RunningImageRaw]:
    namespace = pod.metadata.namespace
    pod_name = pod.metadata.name
    containers = (
        list(None)
        + list(pod.spec.containers or [])
        + list(pod.spec.ephemeral_containers or [])
    )
    return [
        RunningImageRaw(image=container.image, namespace=namespace, pod_name=pod_name)
        for container in containers
    ]


def x__to_running_images__mutmut_7(pod: Any) -> list[RunningImageRaw]:
    namespace = pod.metadata.namespace
    pod_name = pod.metadata.name
    containers = (
        list(pod.spec.init_containers and [])
        + list(pod.spec.containers or [])
        + list(pod.spec.ephemeral_containers or [])
    )
    return [
        RunningImageRaw(image=container.image, namespace=namespace, pod_name=pod_name)
        for container in containers
    ]


def x__to_running_images__mutmut_8(pod: Any) -> list[RunningImageRaw]:
    namespace = pod.metadata.namespace
    pod_name = pod.metadata.name
    containers = (
        list(pod.spec.init_containers or [])
        + list(None)
        + list(pod.spec.ephemeral_containers or [])
    )
    return [
        RunningImageRaw(image=container.image, namespace=namespace, pod_name=pod_name)
        for container in containers
    ]


def x__to_running_images__mutmut_9(pod: Any) -> list[RunningImageRaw]:
    namespace = pod.metadata.namespace
    pod_name = pod.metadata.name
    containers = (
        list(pod.spec.init_containers or [])
        + list(pod.spec.containers and [])
        + list(pod.spec.ephemeral_containers or [])
    )
    return [
        RunningImageRaw(image=container.image, namespace=namespace, pod_name=pod_name)
        for container in containers
    ]


def x__to_running_images__mutmut_10(pod: Any) -> list[RunningImageRaw]:
    namespace = pod.metadata.namespace
    pod_name = pod.metadata.name
    containers = (
        list(pod.spec.init_containers or [])
        + list(pod.spec.containers or [])
        + list(None)
    )
    return [
        RunningImageRaw(image=container.image, namespace=namespace, pod_name=pod_name)
        for container in containers
    ]


def x__to_running_images__mutmut_11(pod: Any) -> list[RunningImageRaw]:
    namespace = pod.metadata.namespace
    pod_name = pod.metadata.name
    containers = (
        list(pod.spec.init_containers or [])
        + list(pod.spec.containers or [])
        + list(pod.spec.ephemeral_containers and [])
    )
    return [
        RunningImageRaw(image=container.image, namespace=namespace, pod_name=pod_name)
        for container in containers
    ]


def x__to_running_images__mutmut_12(pod: Any) -> list[RunningImageRaw]:
    namespace = pod.metadata.namespace
    pod_name = pod.metadata.name
    containers = (
        list(pod.spec.init_containers or [])
        + list(pod.spec.containers or [])
        + list(pod.spec.ephemeral_containers or [])
    )
    return [
        RunningImageRaw(image=None, namespace=namespace, pod_name=pod_name)
        for container in containers
    ]


def x__to_running_images__mutmut_13(pod: Any) -> list[RunningImageRaw]:
    namespace = pod.metadata.namespace
    pod_name = pod.metadata.name
    containers = (
        list(pod.spec.init_containers or [])
        + list(pod.spec.containers or [])
        + list(pod.spec.ephemeral_containers or [])
    )
    return [
        RunningImageRaw(image=container.image, namespace=None, pod_name=pod_name)
        for container in containers
    ]


def x__to_running_images__mutmut_14(pod: Any) -> list[RunningImageRaw]:
    namespace = pod.metadata.namespace
    pod_name = pod.metadata.name
    containers = (
        list(pod.spec.init_containers or [])
        + list(pod.spec.containers or [])
        + list(pod.spec.ephemeral_containers or [])
    )
    return [
        RunningImageRaw(image=container.image, namespace=namespace, pod_name=None)
        for container in containers
    ]


def x__to_running_images__mutmut_15(pod: Any) -> list[RunningImageRaw]:
    namespace = pod.metadata.namespace
    pod_name = pod.metadata.name
    containers = (
        list(pod.spec.init_containers or [])
        + list(pod.spec.containers or [])
        + list(pod.spec.ephemeral_containers or [])
    )
    return [
        RunningImageRaw(namespace=namespace, pod_name=pod_name)
        for container in containers
    ]


def x__to_running_images__mutmut_16(pod: Any) -> list[RunningImageRaw]:
    namespace = pod.metadata.namespace
    pod_name = pod.metadata.name
    containers = (
        list(pod.spec.init_containers or [])
        + list(pod.spec.containers or [])
        + list(pod.spec.ephemeral_containers or [])
    )
    return [
        RunningImageRaw(image=container.image, pod_name=pod_name)
        for container in containers
    ]


def x__to_running_images__mutmut_17(pod: Any) -> list[RunningImageRaw]:
    namespace = pod.metadata.namespace
    pod_name = pod.metadata.name
    containers = (
        list(pod.spec.init_containers or [])
        + list(pod.spec.containers or [])
        + list(pod.spec.ephemeral_containers or [])
    )
    return [
        RunningImageRaw(image=container.image, namespace=namespace, )
        for container in containers
    ]

mutants_x__to_running_images__mutmut['_mutmut_orig'] = x__to_running_images__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_running_images__mutmut['x__to_running_images__mutmut_1'] = x__to_running_images__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_running_images__mutmut['x__to_running_images__mutmut_2'] = x__to_running_images__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_running_images__mutmut['x__to_running_images__mutmut_3'] = x__to_running_images__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_running_images__mutmut['x__to_running_images__mutmut_4'] = x__to_running_images__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_running_images__mutmut['x__to_running_images__mutmut_5'] = x__to_running_images__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_running_images__mutmut['x__to_running_images__mutmut_6'] = x__to_running_images__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_running_images__mutmut['x__to_running_images__mutmut_7'] = x__to_running_images__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_running_images__mutmut['x__to_running_images__mutmut_8'] = x__to_running_images__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_running_images__mutmut['x__to_running_images__mutmut_9'] = x__to_running_images__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_running_images__mutmut['x__to_running_images__mutmut_10'] = x__to_running_images__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_running_images__mutmut['x__to_running_images__mutmut_11'] = x__to_running_images__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_running_images__mutmut['x__to_running_images__mutmut_12'] = x__to_running_images__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_running_images__mutmut['x__to_running_images__mutmut_13'] = x__to_running_images__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_running_images__mutmut['x__to_running_images__mutmut_14'] = x__to_running_images__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_running_images__mutmut['x__to_running_images__mutmut_15'] = x__to_running_images__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_running_images__mutmut['x__to_running_images__mutmut_16'] = x__to_running_images__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_running_images__mutmut['x__to_running_images__mutmut_17'] = x__to_running_images__mutmut_17 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__translate_error__mutmut)
def _translate_error(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Pod image info")
    return ClusterUnreachableError(f"Cannot list Pod image info: {exc}")


def x__translate_error__mutmut_orig(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Pod image info")
    return ClusterUnreachableError(f"Cannot list Pod image info: {exc}")


def x__translate_error__mutmut_1(exc: Exception) -> Exception:
    status = None
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Pod image info")
    return ClusterUnreachableError(f"Cannot list Pod image info: {exc}")


def x__translate_error__mutmut_2(exc: Exception) -> Exception:
    status = getattr(None, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Pod image info")
    return ClusterUnreachableError(f"Cannot list Pod image info: {exc}")


def x__translate_error__mutmut_3(exc: Exception) -> Exception:
    status = getattr(exc, None, None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Pod image info")
    return ClusterUnreachableError(f"Cannot list Pod image info: {exc}")


def x__translate_error__mutmut_4(exc: Exception) -> Exception:
    status = getattr("status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Pod image info")
    return ClusterUnreachableError(f"Cannot list Pod image info: {exc}")


def x__translate_error__mutmut_5(exc: Exception) -> Exception:
    status = getattr(exc, None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Pod image info")
    return ClusterUnreachableError(f"Cannot list Pod image info: {exc}")


def x__translate_error__mutmut_6(exc: Exception) -> Exception:
    status = getattr(exc, "status", )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Pod image info")
    return ClusterUnreachableError(f"Cannot list Pod image info: {exc}")


def x__translate_error__mutmut_7(exc: Exception) -> Exception:
    status = getattr(exc, "XXstatusXX", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Pod image info")
    return ClusterUnreachableError(f"Cannot list Pod image info: {exc}")


def x__translate_error__mutmut_8(exc: Exception) -> Exception:
    status = getattr(exc, "STATUS", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Pod image info")
    return ClusterUnreachableError(f"Cannot list Pod image info: {exc}")


def x__translate_error__mutmut_9(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status != _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Pod image info")
    return ClusterUnreachableError(f"Cannot list Pod image info: {exc}")


def x__translate_error__mutmut_10(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(None)
    return ClusterUnreachableError(f"Cannot list Pod image info: {exc}")


def x__translate_error__mutmut_11(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("XXRBAC denied access to Pod image infoXX")
    return ClusterUnreachableError(f"Cannot list Pod image info: {exc}")


def x__translate_error__mutmut_12(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("rbac denied access to pod image info")
    return ClusterUnreachableError(f"Cannot list Pod image info: {exc}")


def x__translate_error__mutmut_13(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC DENIED ACCESS TO POD IMAGE INFO")
    return ClusterUnreachableError(f"Cannot list Pod image info: {exc}")


def x__translate_error__mutmut_14(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Pod image info")
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
