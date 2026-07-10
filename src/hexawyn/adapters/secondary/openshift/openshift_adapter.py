from __future__ import annotations

from collections.abc import Mapping
from typing import Protocol

from hexawyn.application.ports.driven.k8s_port import (
    ClusterContext,
    ClusterMetrics,
    K8sPort,
    NamespaceInfo,
    PodInfo,
)
from hexawyn.application.ports.driven.openshift_resource_port import (
    ImageStreamInfo,
    OpenShiftResourcePort,
    ProjectInfo,
    RouteInfo,
    SecurityContextConstraintInfo,
)
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    InsufficientPermissionsError,
)

_PROJECT_GROUP = "project.openshift.io"
_ROUTE_GROUP = "route.openshift.io"
_SECURITY_GROUP = "security.openshift.io"
_IMAGE_GROUP = "image.openshift.io"
_API_VERSION = "v1"
_PROJECTS_PLURAL = "projects"
_ROUTES_PLURAL = "routes"
_SCCS_PLURAL = "securitycontextconstraints"
_IMAGE_STREAMS_PLURAL = "imagestreams"
_FORBIDDEN = 403


class OpenShiftDynamicClient(Protocol):
    """Minimal contract for the kubernetes CustomObjectsApi used by this adapter."""

    def list_cluster_custom_object(
        self, group: str, version: str, plural: str
    ) -> Mapping[str, object]: ...

    def list_namespaced_custom_object(
        self, group: str, version: str, namespace: str, plural: str
    ) -> Mapping[str, object]: ...


class OpenShiftAdapter(K8sPort, OpenShiftResourcePort):
    """OpenShift adapter — understands Projects, Routes, SCCs and ImageStreams.

    Standard Kubernetes reads (pods, namespaces, metrics) are delegated to an
    injected K8sPort; the kubeconfig already carries OpenShift auth after
    `oc login`. OpenShift-native resources are read through the CustomObjectsApi.
    """

    def __init__(
        self,
        context: ClusterContext,
        k8s_delegate: K8sPort | None = None,
        dynamic_client: OpenShiftDynamicClient | None = None,
    ) -> None:
        self._context = context
        self._k8s_delegate = k8s_delegate
        self._dynamic_client = dynamic_client

    # ── K8sPort ───────────────────────────────────────────────

    def list_pods(self, namespace: str | None = None) -> list[PodInfo]:
        return self._delegate().list_pods(namespace)

    def list_namespaces(self) -> list[NamespaceInfo]:
        return self._delegate().list_namespaces()

    def get_cluster_metrics(self) -> ClusterMetrics:
        return self._delegate().get_cluster_metrics()

    def get_cluster_context(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "openshift",
            "namespace": self._context.get("namespace", "default"),
        }

    # ── OpenShiftResourcePort ─────────────────────────────────

    def list_projects(self) -> list[ProjectInfo]:
        payload = self._list_cluster(_PROJECT_GROUP, _PROJECTS_PLURAL)
        return [_to_project(item) for item in _items(payload)]

    def list_routes(self, namespace: str) -> list[RouteInfo]:
        payload = self._list_namespaced(_ROUTE_GROUP, _ROUTES_PLURAL, namespace)
        return [_to_route(item) for item in _items(payload)]

    def list_security_context_constraints(self) -> list[SecurityContextConstraintInfo]:
        payload = self._list_cluster(_SECURITY_GROUP, _SCCS_PLURAL)
        return [_to_scc(item) for item in _items(payload)]

    def list_image_streams(self, namespace: str) -> list[ImageStreamInfo]:
        payload = self._list_namespaced(_IMAGE_GROUP, _IMAGE_STREAMS_PLURAL, namespace)
        return [_to_image_stream(item) for item in _items(payload)]

    # ── Helpers ───────────────────────────────────────────────

    def _list_cluster(self, group: str, plural: str) -> Mapping[str, object]:
        client = self._client_or_create()
        try:
            return client.list_cluster_custom_object(
                group=group, version=_API_VERSION, plural=plural
            )
        except Exception as exc:
            raise _translate_error(exc, plural) from exc

    def _list_namespaced(self, group: str, plural: str, namespace: str) -> Mapping[str, object]:
        client = self._client_or_create()
        try:
            return client.list_namespaced_custom_object(
                group=group, version=_API_VERSION, namespace=namespace, plural=plural
            )
        except Exception as exc:
            raise _translate_error(exc, plural, namespace) from exc

    def _delegate(self) -> K8sPort:
        if self._k8s_delegate is None:
            from hexawyn.adapters.secondary.vanilla.vanilla_adapter import (
                VanillaAdapter,
            )

            self._k8s_delegate = VanillaAdapter(self._context["name"])
        return self._k8s_delegate

    def _client_or_create(self) -> OpenShiftDynamicClient:
        if self._dynamic_client is None:
            from kubernetes import client as k8s

            self._dynamic_client = k8s.CustomObjectsApi()
        return self._dynamic_client

    def _cluster_short_name(self) -> str:
        return self._context.get("cluster") or self._context["name"]


def _translate_error(exc: Exception, plural: str, namespace: str | None = None) -> Exception:
    context = {"resource": plural}
    if namespace is not None:
        context["namespace"] = namespace
    if getattr(exc, "status", None) == _FORBIDDEN:
        return InsufficientPermissionsError(f"RBAC denied access to {plural}", context=context)
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading {plural}: {exc}", context=context
    )


def _items(payload: Mapping[str, object]) -> list[Mapping[str, object]]:
    raw = payload.get("items")
    if not isinstance(raw, list):
        return []
    return [item for item in raw if isinstance(item, Mapping)]


def _metadata(item: Mapping[str, object]) -> Mapping[str, object]:
    meta = item.get("metadata")
    return meta if isinstance(meta, Mapping) else {}


def _mapping(item: Mapping[str, object], key: str) -> Mapping[str, object]:
    value = item.get(key)
    return value if isinstance(value, Mapping) else {}


def _to_project(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(meta.get("name", "")),
        status=str(status.get("phase", "Unknown")),
        display_name=str(spec.get("displayName", "")),
    )


def _to_route(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def _to_scc(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(item)
    run_as_user = _mapping(item, "runAsUser")
    return SecurityContextConstraintInfo(
        name=str(meta.get("name", "")),
        allow_privileged_container=bool(item.get("allowPrivilegedContainer", False)),
        run_as_user_type=str(run_as_user.get("type", "")),
    )


def _to_image_stream(item: Mapping[str, object]) -> ImageStreamInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    tags = status.get("tags")
    tag_count = len(tags) if isinstance(tags, list) else 0
    return ImageStreamInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        tag_count=tag_count,
    )
