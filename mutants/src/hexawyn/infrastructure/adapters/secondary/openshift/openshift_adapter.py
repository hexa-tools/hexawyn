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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class OpenShiftDynamicClient(Protocol):
    """Minimal contract for the kubernetes CustomObjectsApi used by this adapter."""

    def list_cluster_custom_object(
        self, group: str, version: str, plural: str
    ) -> Mapping[str, object]: ...

    def list_namespaced_custom_object(
        self, group: str, version: str, namespace: str, plural: str
    ) -> Mapping[str, object]: ...
mutants_xǁOpenShiftAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁOpenShiftAdapterǁlist_pods__mutmut: MutantDict = {}  # type: ignore
mutants_xǁOpenShiftAdapterǁget_cluster_context__mutmut: MutantDict = {}  # type: ignore
mutants_xǁOpenShiftAdapterǁlist_projects__mutmut: MutantDict = {}  # type: ignore
mutants_xǁOpenShiftAdapterǁlist_routes__mutmut: MutantDict = {}  # type: ignore
mutants_xǁOpenShiftAdapterǁlist_security_context_constraints__mutmut: MutantDict = {}  # type: ignore
mutants_xǁOpenShiftAdapterǁlist_image_streams__mutmut: MutantDict = {}  # type: ignore
mutants_xǁOpenShiftAdapterǁ_list_cluster__mutmut: MutantDict = {}  # type: ignore
mutants_xǁOpenShiftAdapterǁ_list_namespaced__mutmut: MutantDict = {}  # type: ignore
mutants_xǁOpenShiftAdapterǁ_delegate__mutmut: MutantDict = {}  # type: ignore
mutants_xǁOpenShiftAdapterǁ_client_or_create__mutmut: MutantDict = {}  # type: ignore
mutants_xǁOpenShiftAdapterǁ_cluster_short_name__mutmut: MutantDict = {}  # type: ignore


class OpenShiftAdapter(K8sPort, OpenShiftResourcePort):
    """OpenShift adapter — understands Projects, Routes, SCCs and ImageStreams.

    Standard Kubernetes reads (pods, namespaces, metrics) are delegated to an
    injected K8sPort; the kubeconfig already carries OpenShift auth after
    `oc login`. OpenShift-native resources are read through the CustomObjectsApi.
    """

    @_mutmut_mutated(mutants_xǁOpenShiftAdapterǁ__init____mutmut)
    def __init__(
        self,
        context: ClusterContext,
        k8s_delegate: K8sPort | None = None,
        dynamic_client: OpenShiftDynamicClient | None = None,
    ) -> None:
        self._context = context
        self._k8s_delegate = k8s_delegate
        self._dynamic_client = dynamic_client

    def xǁOpenShiftAdapterǁ__init____mutmut_orig(
        self,
        context: ClusterContext,
        k8s_delegate: K8sPort | None = None,
        dynamic_client: OpenShiftDynamicClient | None = None,
    ) -> None:
        self._context = context
        self._k8s_delegate = k8s_delegate
        self._dynamic_client = dynamic_client

    def xǁOpenShiftAdapterǁ__init____mutmut_1(
        self,
        context: ClusterContext,
        k8s_delegate: K8sPort | None = None,
        dynamic_client: OpenShiftDynamicClient | None = None,
    ) -> None:
        self._context = None
        self._k8s_delegate = k8s_delegate
        self._dynamic_client = dynamic_client

    def xǁOpenShiftAdapterǁ__init____mutmut_2(
        self,
        context: ClusterContext,
        k8s_delegate: K8sPort | None = None,
        dynamic_client: OpenShiftDynamicClient | None = None,
    ) -> None:
        self._context = context
        self._k8s_delegate = None
        self._dynamic_client = dynamic_client

    def xǁOpenShiftAdapterǁ__init____mutmut_3(
        self,
        context: ClusterContext,
        k8s_delegate: K8sPort | None = None,
        dynamic_client: OpenShiftDynamicClient | None = None,
    ) -> None:
        self._context = context
        self._k8s_delegate = k8s_delegate
        self._dynamic_client = None

    # ── K8sPort ───────────────────────────────────────────────

    @_mutmut_mutated(mutants_xǁOpenShiftAdapterǁlist_pods__mutmut)
    def list_pods(self, namespace: str | None = None) -> list[PodInfo]:
        return self._delegate().list_pods(namespace)

    # ── K8sPort ───────────────────────────────────────────────

    def xǁOpenShiftAdapterǁlist_pods__mutmut_orig(self, namespace: str | None = None) -> list[PodInfo]:
        return self._delegate().list_pods(namespace)

    # ── K8sPort ───────────────────────────────────────────────

    def xǁOpenShiftAdapterǁlist_pods__mutmut_1(self, namespace: str | None = None) -> list[PodInfo]:
        return self._delegate().list_pods(None)

    def list_namespaces(self) -> list[NamespaceInfo]:
        return self._delegate().list_namespaces()

    def get_cluster_metrics(self) -> ClusterMetrics:
        return self._delegate().get_cluster_metrics()

    @_mutmut_mutated(mutants_xǁOpenShiftAdapterǁget_cluster_context__mutmut)
    def get_cluster_context(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "openshift",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁOpenShiftAdapterǁget_cluster_context__mutmut_orig(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "openshift",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁOpenShiftAdapterǁget_cluster_context__mutmut_1(self) -> ClusterContext:
        return {
            "XXnameXX": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "openshift",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁOpenShiftAdapterǁget_cluster_context__mutmut_2(self) -> ClusterContext:
        return {
            "NAME": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "openshift",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁOpenShiftAdapterǁget_cluster_context__mutmut_3(self) -> ClusterContext:
        return {
            "name": self._context["XXnameXX"],
            "cluster": self._cluster_short_name(),
            "provider": "openshift",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁOpenShiftAdapterǁget_cluster_context__mutmut_4(self) -> ClusterContext:
        return {
            "name": self._context["NAME"],
            "cluster": self._cluster_short_name(),
            "provider": "openshift",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁOpenShiftAdapterǁget_cluster_context__mutmut_5(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "XXclusterXX": self._cluster_short_name(),
            "provider": "openshift",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁOpenShiftAdapterǁget_cluster_context__mutmut_6(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "CLUSTER": self._cluster_short_name(),
            "provider": "openshift",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁOpenShiftAdapterǁget_cluster_context__mutmut_7(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "XXproviderXX": "openshift",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁOpenShiftAdapterǁget_cluster_context__mutmut_8(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "PROVIDER": "openshift",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁOpenShiftAdapterǁget_cluster_context__mutmut_9(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "XXopenshiftXX",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁOpenShiftAdapterǁget_cluster_context__mutmut_10(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "OPENSHIFT",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁOpenShiftAdapterǁget_cluster_context__mutmut_11(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "openshift",
            "XXnamespaceXX": self._context.get("namespace", "default"),
        }

    def xǁOpenShiftAdapterǁget_cluster_context__mutmut_12(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "openshift",
            "NAMESPACE": self._context.get("namespace", "default"),
        }

    def xǁOpenShiftAdapterǁget_cluster_context__mutmut_13(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "openshift",
            "namespace": self._context.get(None, "default"),
        }

    def xǁOpenShiftAdapterǁget_cluster_context__mutmut_14(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "openshift",
            "namespace": self._context.get("namespace", None),
        }

    def xǁOpenShiftAdapterǁget_cluster_context__mutmut_15(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "openshift",
            "namespace": self._context.get("default"),
        }

    def xǁOpenShiftAdapterǁget_cluster_context__mutmut_16(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "openshift",
            "namespace": self._context.get("namespace", ),
        }

    def xǁOpenShiftAdapterǁget_cluster_context__mutmut_17(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "openshift",
            "namespace": self._context.get("XXnamespaceXX", "default"),
        }

    def xǁOpenShiftAdapterǁget_cluster_context__mutmut_18(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "openshift",
            "namespace": self._context.get("NAMESPACE", "default"),
        }

    def xǁOpenShiftAdapterǁget_cluster_context__mutmut_19(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "openshift",
            "namespace": self._context.get("namespace", "XXdefaultXX"),
        }

    def xǁOpenShiftAdapterǁget_cluster_context__mutmut_20(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "openshift",
            "namespace": self._context.get("namespace", "DEFAULT"),
        }

    # ── OpenShiftResourcePort ─────────────────────────────────

    @_mutmut_mutated(mutants_xǁOpenShiftAdapterǁlist_projects__mutmut)
    def list_projects(self) -> list[ProjectInfo]:
        payload = self._list_cluster(_PROJECT_GROUP, _PROJECTS_PLURAL)
        return [_to_project(item) for item in _items(payload)]

    # ── OpenShiftResourcePort ─────────────────────────────────

    def xǁOpenShiftAdapterǁlist_projects__mutmut_orig(self) -> list[ProjectInfo]:
        payload = self._list_cluster(_PROJECT_GROUP, _PROJECTS_PLURAL)
        return [_to_project(item) for item in _items(payload)]

    # ── OpenShiftResourcePort ─────────────────────────────────

    def xǁOpenShiftAdapterǁlist_projects__mutmut_1(self) -> list[ProjectInfo]:
        payload = None
        return [_to_project(item) for item in _items(payload)]

    # ── OpenShiftResourcePort ─────────────────────────────────

    def xǁOpenShiftAdapterǁlist_projects__mutmut_2(self) -> list[ProjectInfo]:
        payload = self._list_cluster(None, _PROJECTS_PLURAL)
        return [_to_project(item) for item in _items(payload)]

    # ── OpenShiftResourcePort ─────────────────────────────────

    def xǁOpenShiftAdapterǁlist_projects__mutmut_3(self) -> list[ProjectInfo]:
        payload = self._list_cluster(_PROJECT_GROUP, None)
        return [_to_project(item) for item in _items(payload)]

    # ── OpenShiftResourcePort ─────────────────────────────────

    def xǁOpenShiftAdapterǁlist_projects__mutmut_4(self) -> list[ProjectInfo]:
        payload = self._list_cluster(_PROJECTS_PLURAL)
        return [_to_project(item) for item in _items(payload)]

    # ── OpenShiftResourcePort ─────────────────────────────────

    def xǁOpenShiftAdapterǁlist_projects__mutmut_5(self) -> list[ProjectInfo]:
        payload = self._list_cluster(_PROJECT_GROUP, )
        return [_to_project(item) for item in _items(payload)]

    # ── OpenShiftResourcePort ─────────────────────────────────

    def xǁOpenShiftAdapterǁlist_projects__mutmut_6(self) -> list[ProjectInfo]:
        payload = self._list_cluster(_PROJECT_GROUP, _PROJECTS_PLURAL)
        return [_to_project(None) for item in _items(payload)]

    # ── OpenShiftResourcePort ─────────────────────────────────

    def xǁOpenShiftAdapterǁlist_projects__mutmut_7(self) -> list[ProjectInfo]:
        payload = self._list_cluster(_PROJECT_GROUP, _PROJECTS_PLURAL)
        return [_to_project(item) for item in _items(None)]

    @_mutmut_mutated(mutants_xǁOpenShiftAdapterǁlist_routes__mutmut)
    def list_routes(self, namespace: str) -> list[RouteInfo]:
        payload = self._list_namespaced(_ROUTE_GROUP, _ROUTES_PLURAL, namespace)
        return [_to_route(item) for item in _items(payload)]

    def xǁOpenShiftAdapterǁlist_routes__mutmut_orig(self, namespace: str) -> list[RouteInfo]:
        payload = self._list_namespaced(_ROUTE_GROUP, _ROUTES_PLURAL, namespace)
        return [_to_route(item) for item in _items(payload)]

    def xǁOpenShiftAdapterǁlist_routes__mutmut_1(self, namespace: str) -> list[RouteInfo]:
        payload = None
        return [_to_route(item) for item in _items(payload)]

    def xǁOpenShiftAdapterǁlist_routes__mutmut_2(self, namespace: str) -> list[RouteInfo]:
        payload = self._list_namespaced(None, _ROUTES_PLURAL, namespace)
        return [_to_route(item) for item in _items(payload)]

    def xǁOpenShiftAdapterǁlist_routes__mutmut_3(self, namespace: str) -> list[RouteInfo]:
        payload = self._list_namespaced(_ROUTE_GROUP, None, namespace)
        return [_to_route(item) for item in _items(payload)]

    def xǁOpenShiftAdapterǁlist_routes__mutmut_4(self, namespace: str) -> list[RouteInfo]:
        payload = self._list_namespaced(_ROUTE_GROUP, _ROUTES_PLURAL, None)
        return [_to_route(item) for item in _items(payload)]

    def xǁOpenShiftAdapterǁlist_routes__mutmut_5(self, namespace: str) -> list[RouteInfo]:
        payload = self._list_namespaced(_ROUTES_PLURAL, namespace)
        return [_to_route(item) for item in _items(payload)]

    def xǁOpenShiftAdapterǁlist_routes__mutmut_6(self, namespace: str) -> list[RouteInfo]:
        payload = self._list_namespaced(_ROUTE_GROUP, namespace)
        return [_to_route(item) for item in _items(payload)]

    def xǁOpenShiftAdapterǁlist_routes__mutmut_7(self, namespace: str) -> list[RouteInfo]:
        payload = self._list_namespaced(_ROUTE_GROUP, _ROUTES_PLURAL, )
        return [_to_route(item) for item in _items(payload)]

    def xǁOpenShiftAdapterǁlist_routes__mutmut_8(self, namespace: str) -> list[RouteInfo]:
        payload = self._list_namespaced(_ROUTE_GROUP, _ROUTES_PLURAL, namespace)
        return [_to_route(None) for item in _items(payload)]

    def xǁOpenShiftAdapterǁlist_routes__mutmut_9(self, namespace: str) -> list[RouteInfo]:
        payload = self._list_namespaced(_ROUTE_GROUP, _ROUTES_PLURAL, namespace)
        return [_to_route(item) for item in _items(None)]

    @_mutmut_mutated(mutants_xǁOpenShiftAdapterǁlist_security_context_constraints__mutmut)
    def list_security_context_constraints(self) -> list[SecurityContextConstraintInfo]:
        payload = self._list_cluster(_SECURITY_GROUP, _SCCS_PLURAL)
        return [_to_scc(item) for item in _items(payload)]

    def xǁOpenShiftAdapterǁlist_security_context_constraints__mutmut_orig(self) -> list[SecurityContextConstraintInfo]:
        payload = self._list_cluster(_SECURITY_GROUP, _SCCS_PLURAL)
        return [_to_scc(item) for item in _items(payload)]

    def xǁOpenShiftAdapterǁlist_security_context_constraints__mutmut_1(self) -> list[SecurityContextConstraintInfo]:
        payload = None
        return [_to_scc(item) for item in _items(payload)]

    def xǁOpenShiftAdapterǁlist_security_context_constraints__mutmut_2(self) -> list[SecurityContextConstraintInfo]:
        payload = self._list_cluster(None, _SCCS_PLURAL)
        return [_to_scc(item) for item in _items(payload)]

    def xǁOpenShiftAdapterǁlist_security_context_constraints__mutmut_3(self) -> list[SecurityContextConstraintInfo]:
        payload = self._list_cluster(_SECURITY_GROUP, None)
        return [_to_scc(item) for item in _items(payload)]

    def xǁOpenShiftAdapterǁlist_security_context_constraints__mutmut_4(self) -> list[SecurityContextConstraintInfo]:
        payload = self._list_cluster(_SCCS_PLURAL)
        return [_to_scc(item) for item in _items(payload)]

    def xǁOpenShiftAdapterǁlist_security_context_constraints__mutmut_5(self) -> list[SecurityContextConstraintInfo]:
        payload = self._list_cluster(_SECURITY_GROUP, )
        return [_to_scc(item) for item in _items(payload)]

    def xǁOpenShiftAdapterǁlist_security_context_constraints__mutmut_6(self) -> list[SecurityContextConstraintInfo]:
        payload = self._list_cluster(_SECURITY_GROUP, _SCCS_PLURAL)
        return [_to_scc(None) for item in _items(payload)]

    def xǁOpenShiftAdapterǁlist_security_context_constraints__mutmut_7(self) -> list[SecurityContextConstraintInfo]:
        payload = self._list_cluster(_SECURITY_GROUP, _SCCS_PLURAL)
        return [_to_scc(item) for item in _items(None)]

    @_mutmut_mutated(mutants_xǁOpenShiftAdapterǁlist_image_streams__mutmut)
    def list_image_streams(self, namespace: str) -> list[ImageStreamInfo]:
        payload = self._list_namespaced(_IMAGE_GROUP, _IMAGE_STREAMS_PLURAL, namespace)
        return [_to_image_stream(item) for item in _items(payload)]

    def xǁOpenShiftAdapterǁlist_image_streams__mutmut_orig(self, namespace: str) -> list[ImageStreamInfo]:
        payload = self._list_namespaced(_IMAGE_GROUP, _IMAGE_STREAMS_PLURAL, namespace)
        return [_to_image_stream(item) for item in _items(payload)]

    def xǁOpenShiftAdapterǁlist_image_streams__mutmut_1(self, namespace: str) -> list[ImageStreamInfo]:
        payload = None
        return [_to_image_stream(item) for item in _items(payload)]

    def xǁOpenShiftAdapterǁlist_image_streams__mutmut_2(self, namespace: str) -> list[ImageStreamInfo]:
        payload = self._list_namespaced(None, _IMAGE_STREAMS_PLURAL, namespace)
        return [_to_image_stream(item) for item in _items(payload)]

    def xǁOpenShiftAdapterǁlist_image_streams__mutmut_3(self, namespace: str) -> list[ImageStreamInfo]:
        payload = self._list_namespaced(_IMAGE_GROUP, None, namespace)
        return [_to_image_stream(item) for item in _items(payload)]

    def xǁOpenShiftAdapterǁlist_image_streams__mutmut_4(self, namespace: str) -> list[ImageStreamInfo]:
        payload = self._list_namespaced(_IMAGE_GROUP, _IMAGE_STREAMS_PLURAL, None)
        return [_to_image_stream(item) for item in _items(payload)]

    def xǁOpenShiftAdapterǁlist_image_streams__mutmut_5(self, namespace: str) -> list[ImageStreamInfo]:
        payload = self._list_namespaced(_IMAGE_STREAMS_PLURAL, namespace)
        return [_to_image_stream(item) for item in _items(payload)]

    def xǁOpenShiftAdapterǁlist_image_streams__mutmut_6(self, namespace: str) -> list[ImageStreamInfo]:
        payload = self._list_namespaced(_IMAGE_GROUP, namespace)
        return [_to_image_stream(item) for item in _items(payload)]

    def xǁOpenShiftAdapterǁlist_image_streams__mutmut_7(self, namespace: str) -> list[ImageStreamInfo]:
        payload = self._list_namespaced(_IMAGE_GROUP, _IMAGE_STREAMS_PLURAL, )
        return [_to_image_stream(item) for item in _items(payload)]

    def xǁOpenShiftAdapterǁlist_image_streams__mutmut_8(self, namespace: str) -> list[ImageStreamInfo]:
        payload = self._list_namespaced(_IMAGE_GROUP, _IMAGE_STREAMS_PLURAL, namespace)
        return [_to_image_stream(None) for item in _items(payload)]

    def xǁOpenShiftAdapterǁlist_image_streams__mutmut_9(self, namespace: str) -> list[ImageStreamInfo]:
        payload = self._list_namespaced(_IMAGE_GROUP, _IMAGE_STREAMS_PLURAL, namespace)
        return [_to_image_stream(item) for item in _items(None)]

    # ── Helpers ───────────────────────────────────────────────

    @_mutmut_mutated(mutants_xǁOpenShiftAdapterǁ_list_cluster__mutmut)
    def _list_cluster(self, group: str, plural: str) -> Mapping[str, object]:
        client = self._client_or_create()
        try:
            return client.list_cluster_custom_object(
                group=group, version=_API_VERSION, plural=plural
            )
        except Exception as exc:
            raise _translate_error(exc, plural) from exc

    # ── Helpers ───────────────────────────────────────────────

    def xǁOpenShiftAdapterǁ_list_cluster__mutmut_orig(self, group: str, plural: str) -> Mapping[str, object]:
        client = self._client_or_create()
        try:
            return client.list_cluster_custom_object(
                group=group, version=_API_VERSION, plural=plural
            )
        except Exception as exc:
            raise _translate_error(exc, plural) from exc

    # ── Helpers ───────────────────────────────────────────────

    def xǁOpenShiftAdapterǁ_list_cluster__mutmut_1(self, group: str, plural: str) -> Mapping[str, object]:
        client = None
        try:
            return client.list_cluster_custom_object(
                group=group, version=_API_VERSION, plural=plural
            )
        except Exception as exc:
            raise _translate_error(exc, plural) from exc

    # ── Helpers ───────────────────────────────────────────────

    def xǁOpenShiftAdapterǁ_list_cluster__mutmut_2(self, group: str, plural: str) -> Mapping[str, object]:
        client = self._client_or_create()
        try:
            return client.list_cluster_custom_object(
                group=None, version=_API_VERSION, plural=plural
            )
        except Exception as exc:
            raise _translate_error(exc, plural) from exc

    # ── Helpers ───────────────────────────────────────────────

    def xǁOpenShiftAdapterǁ_list_cluster__mutmut_3(self, group: str, plural: str) -> Mapping[str, object]:
        client = self._client_or_create()
        try:
            return client.list_cluster_custom_object(
                group=group, version=None, plural=plural
            )
        except Exception as exc:
            raise _translate_error(exc, plural) from exc

    # ── Helpers ───────────────────────────────────────────────

    def xǁOpenShiftAdapterǁ_list_cluster__mutmut_4(self, group: str, plural: str) -> Mapping[str, object]:
        client = self._client_or_create()
        try:
            return client.list_cluster_custom_object(
                group=group, version=_API_VERSION, plural=None
            )
        except Exception as exc:
            raise _translate_error(exc, plural) from exc

    # ── Helpers ───────────────────────────────────────────────

    def xǁOpenShiftAdapterǁ_list_cluster__mutmut_5(self, group: str, plural: str) -> Mapping[str, object]:
        client = self._client_or_create()
        try:
            return client.list_cluster_custom_object(
                version=_API_VERSION, plural=plural
            )
        except Exception as exc:
            raise _translate_error(exc, plural) from exc

    # ── Helpers ───────────────────────────────────────────────

    def xǁOpenShiftAdapterǁ_list_cluster__mutmut_6(self, group: str, plural: str) -> Mapping[str, object]:
        client = self._client_or_create()
        try:
            return client.list_cluster_custom_object(
                group=group, plural=plural
            )
        except Exception as exc:
            raise _translate_error(exc, plural) from exc

    # ── Helpers ───────────────────────────────────────────────

    def xǁOpenShiftAdapterǁ_list_cluster__mutmut_7(self, group: str, plural: str) -> Mapping[str, object]:
        client = self._client_or_create()
        try:
            return client.list_cluster_custom_object(
                group=group, version=_API_VERSION, )
        except Exception as exc:
            raise _translate_error(exc, plural) from exc

    # ── Helpers ───────────────────────────────────────────────

    def xǁOpenShiftAdapterǁ_list_cluster__mutmut_8(self, group: str, plural: str) -> Mapping[str, object]:
        client = self._client_or_create()
        try:
            return client.list_cluster_custom_object(
                group=group, version=_API_VERSION, plural=plural
            )
        except Exception as exc:
            raise _translate_error(None, plural) from exc

    # ── Helpers ───────────────────────────────────────────────

    def xǁOpenShiftAdapterǁ_list_cluster__mutmut_9(self, group: str, plural: str) -> Mapping[str, object]:
        client = self._client_or_create()
        try:
            return client.list_cluster_custom_object(
                group=group, version=_API_VERSION, plural=plural
            )
        except Exception as exc:
            raise _translate_error(exc, None) from exc

    # ── Helpers ───────────────────────────────────────────────

    def xǁOpenShiftAdapterǁ_list_cluster__mutmut_10(self, group: str, plural: str) -> Mapping[str, object]:
        client = self._client_or_create()
        try:
            return client.list_cluster_custom_object(
                group=group, version=_API_VERSION, plural=plural
            )
        except Exception as exc:
            raise _translate_error(plural) from exc

    # ── Helpers ───────────────────────────────────────────────

    def xǁOpenShiftAdapterǁ_list_cluster__mutmut_11(self, group: str, plural: str) -> Mapping[str, object]:
        client = self._client_or_create()
        try:
            return client.list_cluster_custom_object(
                group=group, version=_API_VERSION, plural=plural
            )
        except Exception as exc:
            raise _translate_error(exc, ) from exc

    @_mutmut_mutated(mutants_xǁOpenShiftAdapterǁ_list_namespaced__mutmut)
    def _list_namespaced(self, group: str, plural: str, namespace: str) -> Mapping[str, object]:
        client = self._client_or_create()
        try:
            return client.list_namespaced_custom_object(
                group=group, version=_API_VERSION, namespace=namespace, plural=plural
            )
        except Exception as exc:
            raise _translate_error(exc, plural, namespace) from exc

    def xǁOpenShiftAdapterǁ_list_namespaced__mutmut_orig(self, group: str, plural: str, namespace: str) -> Mapping[str, object]:
        client = self._client_or_create()
        try:
            return client.list_namespaced_custom_object(
                group=group, version=_API_VERSION, namespace=namespace, plural=plural
            )
        except Exception as exc:
            raise _translate_error(exc, plural, namespace) from exc

    def xǁOpenShiftAdapterǁ_list_namespaced__mutmut_1(self, group: str, plural: str, namespace: str) -> Mapping[str, object]:
        client = None
        try:
            return client.list_namespaced_custom_object(
                group=group, version=_API_VERSION, namespace=namespace, plural=plural
            )
        except Exception as exc:
            raise _translate_error(exc, plural, namespace) from exc

    def xǁOpenShiftAdapterǁ_list_namespaced__mutmut_2(self, group: str, plural: str, namespace: str) -> Mapping[str, object]:
        client = self._client_or_create()
        try:
            return client.list_namespaced_custom_object(
                group=None, version=_API_VERSION, namespace=namespace, plural=plural
            )
        except Exception as exc:
            raise _translate_error(exc, plural, namespace) from exc

    def xǁOpenShiftAdapterǁ_list_namespaced__mutmut_3(self, group: str, plural: str, namespace: str) -> Mapping[str, object]:
        client = self._client_or_create()
        try:
            return client.list_namespaced_custom_object(
                group=group, version=None, namespace=namespace, plural=plural
            )
        except Exception as exc:
            raise _translate_error(exc, plural, namespace) from exc

    def xǁOpenShiftAdapterǁ_list_namespaced__mutmut_4(self, group: str, plural: str, namespace: str) -> Mapping[str, object]:
        client = self._client_or_create()
        try:
            return client.list_namespaced_custom_object(
                group=group, version=_API_VERSION, namespace=None, plural=plural
            )
        except Exception as exc:
            raise _translate_error(exc, plural, namespace) from exc

    def xǁOpenShiftAdapterǁ_list_namespaced__mutmut_5(self, group: str, plural: str, namespace: str) -> Mapping[str, object]:
        client = self._client_or_create()
        try:
            return client.list_namespaced_custom_object(
                group=group, version=_API_VERSION, namespace=namespace, plural=None
            )
        except Exception as exc:
            raise _translate_error(exc, plural, namespace) from exc

    def xǁOpenShiftAdapterǁ_list_namespaced__mutmut_6(self, group: str, plural: str, namespace: str) -> Mapping[str, object]:
        client = self._client_or_create()
        try:
            return client.list_namespaced_custom_object(
                version=_API_VERSION, namespace=namespace, plural=plural
            )
        except Exception as exc:
            raise _translate_error(exc, plural, namespace) from exc

    def xǁOpenShiftAdapterǁ_list_namespaced__mutmut_7(self, group: str, plural: str, namespace: str) -> Mapping[str, object]:
        client = self._client_or_create()
        try:
            return client.list_namespaced_custom_object(
                group=group, namespace=namespace, plural=plural
            )
        except Exception as exc:
            raise _translate_error(exc, plural, namespace) from exc

    def xǁOpenShiftAdapterǁ_list_namespaced__mutmut_8(self, group: str, plural: str, namespace: str) -> Mapping[str, object]:
        client = self._client_or_create()
        try:
            return client.list_namespaced_custom_object(
                group=group, version=_API_VERSION, plural=plural
            )
        except Exception as exc:
            raise _translate_error(exc, plural, namespace) from exc

    def xǁOpenShiftAdapterǁ_list_namespaced__mutmut_9(self, group: str, plural: str, namespace: str) -> Mapping[str, object]:
        client = self._client_or_create()
        try:
            return client.list_namespaced_custom_object(
                group=group, version=_API_VERSION, namespace=namespace, )
        except Exception as exc:
            raise _translate_error(exc, plural, namespace) from exc

    def xǁOpenShiftAdapterǁ_list_namespaced__mutmut_10(self, group: str, plural: str, namespace: str) -> Mapping[str, object]:
        client = self._client_or_create()
        try:
            return client.list_namespaced_custom_object(
                group=group, version=_API_VERSION, namespace=namespace, plural=plural
            )
        except Exception as exc:
            raise _translate_error(None, plural, namespace) from exc

    def xǁOpenShiftAdapterǁ_list_namespaced__mutmut_11(self, group: str, plural: str, namespace: str) -> Mapping[str, object]:
        client = self._client_or_create()
        try:
            return client.list_namespaced_custom_object(
                group=group, version=_API_VERSION, namespace=namespace, plural=plural
            )
        except Exception as exc:
            raise _translate_error(exc, None, namespace) from exc

    def xǁOpenShiftAdapterǁ_list_namespaced__mutmut_12(self, group: str, plural: str, namespace: str) -> Mapping[str, object]:
        client = self._client_or_create()
        try:
            return client.list_namespaced_custom_object(
                group=group, version=_API_VERSION, namespace=namespace, plural=plural
            )
        except Exception as exc:
            raise _translate_error(exc, plural, None) from exc

    def xǁOpenShiftAdapterǁ_list_namespaced__mutmut_13(self, group: str, plural: str, namespace: str) -> Mapping[str, object]:
        client = self._client_or_create()
        try:
            return client.list_namespaced_custom_object(
                group=group, version=_API_VERSION, namespace=namespace, plural=plural
            )
        except Exception as exc:
            raise _translate_error(plural, namespace) from exc

    def xǁOpenShiftAdapterǁ_list_namespaced__mutmut_14(self, group: str, plural: str, namespace: str) -> Mapping[str, object]:
        client = self._client_or_create()
        try:
            return client.list_namespaced_custom_object(
                group=group, version=_API_VERSION, namespace=namespace, plural=plural
            )
        except Exception as exc:
            raise _translate_error(exc, namespace) from exc

    def xǁOpenShiftAdapterǁ_list_namespaced__mutmut_15(self, group: str, plural: str, namespace: str) -> Mapping[str, object]:
        client = self._client_or_create()
        try:
            return client.list_namespaced_custom_object(
                group=group, version=_API_VERSION, namespace=namespace, plural=plural
            )
        except Exception as exc:
            raise _translate_error(exc, plural, ) from exc

    @_mutmut_mutated(mutants_xǁOpenShiftAdapterǁ_delegate__mutmut)
    def _delegate(self) -> K8sPort:
        if self._k8s_delegate is None:
            from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
                VanillaAdapter,
            )

            self._k8s_delegate = VanillaAdapter(self._context["name"])
        return self._k8s_delegate

    def xǁOpenShiftAdapterǁ_delegate__mutmut_orig(self) -> K8sPort:
        if self._k8s_delegate is None:
            from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
                VanillaAdapter,
            )

            self._k8s_delegate = VanillaAdapter(self._context["name"])
        return self._k8s_delegate

    def xǁOpenShiftAdapterǁ_delegate__mutmut_1(self) -> K8sPort:
        if self._k8s_delegate is not None:
            from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
                VanillaAdapter,
            )

            self._k8s_delegate = VanillaAdapter(self._context["name"])
        return self._k8s_delegate

    def xǁOpenShiftAdapterǁ_delegate__mutmut_2(self) -> K8sPort:
        if self._k8s_delegate is None:
            from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
                VanillaAdapter,
            )

            self._k8s_delegate = None
        return self._k8s_delegate

    def xǁOpenShiftAdapterǁ_delegate__mutmut_3(self) -> K8sPort:
        if self._k8s_delegate is None:
            from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
                VanillaAdapter,
            )

            self._k8s_delegate = VanillaAdapter(None)
        return self._k8s_delegate

    def xǁOpenShiftAdapterǁ_delegate__mutmut_4(self) -> K8sPort:
        if self._k8s_delegate is None:
            from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
                VanillaAdapter,
            )

            self._k8s_delegate = VanillaAdapter(self._context["XXnameXX"])
        return self._k8s_delegate

    def xǁOpenShiftAdapterǁ_delegate__mutmut_5(self) -> K8sPort:
        if self._k8s_delegate is None:
            from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
                VanillaAdapter,
            )

            self._k8s_delegate = VanillaAdapter(self._context["NAME"])
        return self._k8s_delegate

    @_mutmut_mutated(mutants_xǁOpenShiftAdapterǁ_client_or_create__mutmut)
    def _client_or_create(self) -> OpenShiftDynamicClient:
        if self._dynamic_client is None:
            from kubernetes import client as k8s

            self._dynamic_client = k8s.CustomObjectsApi()
        return self._dynamic_client

    def xǁOpenShiftAdapterǁ_client_or_create__mutmut_orig(self) -> OpenShiftDynamicClient:
        if self._dynamic_client is None:
            from kubernetes import client as k8s

            self._dynamic_client = k8s.CustomObjectsApi()
        return self._dynamic_client

    def xǁOpenShiftAdapterǁ_client_or_create__mutmut_1(self) -> OpenShiftDynamicClient:
        if self._dynamic_client is not None:
            from kubernetes import client as k8s

            self._dynamic_client = k8s.CustomObjectsApi()
        return self._dynamic_client

    def xǁOpenShiftAdapterǁ_client_or_create__mutmut_2(self) -> OpenShiftDynamicClient:
        if self._dynamic_client is None:
            from kubernetes import client as k8s

            self._dynamic_client = None
        return self._dynamic_client

    @_mutmut_mutated(mutants_xǁOpenShiftAdapterǁ_cluster_short_name__mutmut)
    def _cluster_short_name(self) -> str:
        return self._context.get("cluster") or self._context["name"]

    def xǁOpenShiftAdapterǁ_cluster_short_name__mutmut_orig(self) -> str:
        return self._context.get("cluster") or self._context["name"]

    def xǁOpenShiftAdapterǁ_cluster_short_name__mutmut_1(self) -> str:
        return self._context.get("cluster") and self._context["name"]

    def xǁOpenShiftAdapterǁ_cluster_short_name__mutmut_2(self) -> str:
        return self._context.get(None) or self._context["name"]

    def xǁOpenShiftAdapterǁ_cluster_short_name__mutmut_3(self) -> str:
        return self._context.get("XXclusterXX") or self._context["name"]

    def xǁOpenShiftAdapterǁ_cluster_short_name__mutmut_4(self) -> str:
        return self._context.get("CLUSTER") or self._context["name"]

    def xǁOpenShiftAdapterǁ_cluster_short_name__mutmut_5(self) -> str:
        return self._context.get("cluster") or self._context["XXnameXX"]

    def xǁOpenShiftAdapterǁ_cluster_short_name__mutmut_6(self) -> str:
        return self._context.get("cluster") or self._context["NAME"]

mutants_xǁOpenShiftAdapterǁ__init____mutmut['_mutmut_orig'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁ__init____mutmut['xǁOpenShiftAdapterǁ__init____mutmut_1'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁ__init____mutmut['xǁOpenShiftAdapterǁ__init____mutmut_2'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁ__init____mutmut['xǁOpenShiftAdapterǁ__init____mutmut_3'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ__init____mutmut_3 # type: ignore # mutmut generated

mutants_xǁOpenShiftAdapterǁlist_pods__mutmut['_mutmut_orig'] = OpenShiftAdapter.xǁOpenShiftAdapterǁlist_pods__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁlist_pods__mutmut['xǁOpenShiftAdapterǁlist_pods__mutmut_1'] = OpenShiftAdapter.xǁOpenShiftAdapterǁlist_pods__mutmut_1 # type: ignore # mutmut generated

mutants_xǁOpenShiftAdapterǁget_cluster_context__mutmut['_mutmut_orig'] = OpenShiftAdapter.xǁOpenShiftAdapterǁget_cluster_context__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁget_cluster_context__mutmut['xǁOpenShiftAdapterǁget_cluster_context__mutmut_1'] = OpenShiftAdapter.xǁOpenShiftAdapterǁget_cluster_context__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁget_cluster_context__mutmut['xǁOpenShiftAdapterǁget_cluster_context__mutmut_2'] = OpenShiftAdapter.xǁOpenShiftAdapterǁget_cluster_context__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁget_cluster_context__mutmut['xǁOpenShiftAdapterǁget_cluster_context__mutmut_3'] = OpenShiftAdapter.xǁOpenShiftAdapterǁget_cluster_context__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁget_cluster_context__mutmut['xǁOpenShiftAdapterǁget_cluster_context__mutmut_4'] = OpenShiftAdapter.xǁOpenShiftAdapterǁget_cluster_context__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁget_cluster_context__mutmut['xǁOpenShiftAdapterǁget_cluster_context__mutmut_5'] = OpenShiftAdapter.xǁOpenShiftAdapterǁget_cluster_context__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁget_cluster_context__mutmut['xǁOpenShiftAdapterǁget_cluster_context__mutmut_6'] = OpenShiftAdapter.xǁOpenShiftAdapterǁget_cluster_context__mutmut_6 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁget_cluster_context__mutmut['xǁOpenShiftAdapterǁget_cluster_context__mutmut_7'] = OpenShiftAdapter.xǁOpenShiftAdapterǁget_cluster_context__mutmut_7 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁget_cluster_context__mutmut['xǁOpenShiftAdapterǁget_cluster_context__mutmut_8'] = OpenShiftAdapter.xǁOpenShiftAdapterǁget_cluster_context__mutmut_8 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁget_cluster_context__mutmut['xǁOpenShiftAdapterǁget_cluster_context__mutmut_9'] = OpenShiftAdapter.xǁOpenShiftAdapterǁget_cluster_context__mutmut_9 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁget_cluster_context__mutmut['xǁOpenShiftAdapterǁget_cluster_context__mutmut_10'] = OpenShiftAdapter.xǁOpenShiftAdapterǁget_cluster_context__mutmut_10 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁget_cluster_context__mutmut['xǁOpenShiftAdapterǁget_cluster_context__mutmut_11'] = OpenShiftAdapter.xǁOpenShiftAdapterǁget_cluster_context__mutmut_11 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁget_cluster_context__mutmut['xǁOpenShiftAdapterǁget_cluster_context__mutmut_12'] = OpenShiftAdapter.xǁOpenShiftAdapterǁget_cluster_context__mutmut_12 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁget_cluster_context__mutmut['xǁOpenShiftAdapterǁget_cluster_context__mutmut_13'] = OpenShiftAdapter.xǁOpenShiftAdapterǁget_cluster_context__mutmut_13 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁget_cluster_context__mutmut['xǁOpenShiftAdapterǁget_cluster_context__mutmut_14'] = OpenShiftAdapter.xǁOpenShiftAdapterǁget_cluster_context__mutmut_14 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁget_cluster_context__mutmut['xǁOpenShiftAdapterǁget_cluster_context__mutmut_15'] = OpenShiftAdapter.xǁOpenShiftAdapterǁget_cluster_context__mutmut_15 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁget_cluster_context__mutmut['xǁOpenShiftAdapterǁget_cluster_context__mutmut_16'] = OpenShiftAdapter.xǁOpenShiftAdapterǁget_cluster_context__mutmut_16 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁget_cluster_context__mutmut['xǁOpenShiftAdapterǁget_cluster_context__mutmut_17'] = OpenShiftAdapter.xǁOpenShiftAdapterǁget_cluster_context__mutmut_17 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁget_cluster_context__mutmut['xǁOpenShiftAdapterǁget_cluster_context__mutmut_18'] = OpenShiftAdapter.xǁOpenShiftAdapterǁget_cluster_context__mutmut_18 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁget_cluster_context__mutmut['xǁOpenShiftAdapterǁget_cluster_context__mutmut_19'] = OpenShiftAdapter.xǁOpenShiftAdapterǁget_cluster_context__mutmut_19 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁget_cluster_context__mutmut['xǁOpenShiftAdapterǁget_cluster_context__mutmut_20'] = OpenShiftAdapter.xǁOpenShiftAdapterǁget_cluster_context__mutmut_20 # type: ignore # mutmut generated

mutants_xǁOpenShiftAdapterǁlist_projects__mutmut['_mutmut_orig'] = OpenShiftAdapter.xǁOpenShiftAdapterǁlist_projects__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁlist_projects__mutmut['xǁOpenShiftAdapterǁlist_projects__mutmut_1'] = OpenShiftAdapter.xǁOpenShiftAdapterǁlist_projects__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁlist_projects__mutmut['xǁOpenShiftAdapterǁlist_projects__mutmut_2'] = OpenShiftAdapter.xǁOpenShiftAdapterǁlist_projects__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁlist_projects__mutmut['xǁOpenShiftAdapterǁlist_projects__mutmut_3'] = OpenShiftAdapter.xǁOpenShiftAdapterǁlist_projects__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁlist_projects__mutmut['xǁOpenShiftAdapterǁlist_projects__mutmut_4'] = OpenShiftAdapter.xǁOpenShiftAdapterǁlist_projects__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁlist_projects__mutmut['xǁOpenShiftAdapterǁlist_projects__mutmut_5'] = OpenShiftAdapter.xǁOpenShiftAdapterǁlist_projects__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁlist_projects__mutmut['xǁOpenShiftAdapterǁlist_projects__mutmut_6'] = OpenShiftAdapter.xǁOpenShiftAdapterǁlist_projects__mutmut_6 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁlist_projects__mutmut['xǁOpenShiftAdapterǁlist_projects__mutmut_7'] = OpenShiftAdapter.xǁOpenShiftAdapterǁlist_projects__mutmut_7 # type: ignore # mutmut generated

mutants_xǁOpenShiftAdapterǁlist_routes__mutmut['_mutmut_orig'] = OpenShiftAdapter.xǁOpenShiftAdapterǁlist_routes__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁlist_routes__mutmut['xǁOpenShiftAdapterǁlist_routes__mutmut_1'] = OpenShiftAdapter.xǁOpenShiftAdapterǁlist_routes__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁlist_routes__mutmut['xǁOpenShiftAdapterǁlist_routes__mutmut_2'] = OpenShiftAdapter.xǁOpenShiftAdapterǁlist_routes__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁlist_routes__mutmut['xǁOpenShiftAdapterǁlist_routes__mutmut_3'] = OpenShiftAdapter.xǁOpenShiftAdapterǁlist_routes__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁlist_routes__mutmut['xǁOpenShiftAdapterǁlist_routes__mutmut_4'] = OpenShiftAdapter.xǁOpenShiftAdapterǁlist_routes__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁlist_routes__mutmut['xǁOpenShiftAdapterǁlist_routes__mutmut_5'] = OpenShiftAdapter.xǁOpenShiftAdapterǁlist_routes__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁlist_routes__mutmut['xǁOpenShiftAdapterǁlist_routes__mutmut_6'] = OpenShiftAdapter.xǁOpenShiftAdapterǁlist_routes__mutmut_6 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁlist_routes__mutmut['xǁOpenShiftAdapterǁlist_routes__mutmut_7'] = OpenShiftAdapter.xǁOpenShiftAdapterǁlist_routes__mutmut_7 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁlist_routes__mutmut['xǁOpenShiftAdapterǁlist_routes__mutmut_8'] = OpenShiftAdapter.xǁOpenShiftAdapterǁlist_routes__mutmut_8 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁlist_routes__mutmut['xǁOpenShiftAdapterǁlist_routes__mutmut_9'] = OpenShiftAdapter.xǁOpenShiftAdapterǁlist_routes__mutmut_9 # type: ignore # mutmut generated

mutants_xǁOpenShiftAdapterǁlist_security_context_constraints__mutmut['_mutmut_orig'] = OpenShiftAdapter.xǁOpenShiftAdapterǁlist_security_context_constraints__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁlist_security_context_constraints__mutmut['xǁOpenShiftAdapterǁlist_security_context_constraints__mutmut_1'] = OpenShiftAdapter.xǁOpenShiftAdapterǁlist_security_context_constraints__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁlist_security_context_constraints__mutmut['xǁOpenShiftAdapterǁlist_security_context_constraints__mutmut_2'] = OpenShiftAdapter.xǁOpenShiftAdapterǁlist_security_context_constraints__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁlist_security_context_constraints__mutmut['xǁOpenShiftAdapterǁlist_security_context_constraints__mutmut_3'] = OpenShiftAdapter.xǁOpenShiftAdapterǁlist_security_context_constraints__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁlist_security_context_constraints__mutmut['xǁOpenShiftAdapterǁlist_security_context_constraints__mutmut_4'] = OpenShiftAdapter.xǁOpenShiftAdapterǁlist_security_context_constraints__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁlist_security_context_constraints__mutmut['xǁOpenShiftAdapterǁlist_security_context_constraints__mutmut_5'] = OpenShiftAdapter.xǁOpenShiftAdapterǁlist_security_context_constraints__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁlist_security_context_constraints__mutmut['xǁOpenShiftAdapterǁlist_security_context_constraints__mutmut_6'] = OpenShiftAdapter.xǁOpenShiftAdapterǁlist_security_context_constraints__mutmut_6 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁlist_security_context_constraints__mutmut['xǁOpenShiftAdapterǁlist_security_context_constraints__mutmut_7'] = OpenShiftAdapter.xǁOpenShiftAdapterǁlist_security_context_constraints__mutmut_7 # type: ignore # mutmut generated

mutants_xǁOpenShiftAdapterǁlist_image_streams__mutmut['_mutmut_orig'] = OpenShiftAdapter.xǁOpenShiftAdapterǁlist_image_streams__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁlist_image_streams__mutmut['xǁOpenShiftAdapterǁlist_image_streams__mutmut_1'] = OpenShiftAdapter.xǁOpenShiftAdapterǁlist_image_streams__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁlist_image_streams__mutmut['xǁOpenShiftAdapterǁlist_image_streams__mutmut_2'] = OpenShiftAdapter.xǁOpenShiftAdapterǁlist_image_streams__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁlist_image_streams__mutmut['xǁOpenShiftAdapterǁlist_image_streams__mutmut_3'] = OpenShiftAdapter.xǁOpenShiftAdapterǁlist_image_streams__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁlist_image_streams__mutmut['xǁOpenShiftAdapterǁlist_image_streams__mutmut_4'] = OpenShiftAdapter.xǁOpenShiftAdapterǁlist_image_streams__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁlist_image_streams__mutmut['xǁOpenShiftAdapterǁlist_image_streams__mutmut_5'] = OpenShiftAdapter.xǁOpenShiftAdapterǁlist_image_streams__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁlist_image_streams__mutmut['xǁOpenShiftAdapterǁlist_image_streams__mutmut_6'] = OpenShiftAdapter.xǁOpenShiftAdapterǁlist_image_streams__mutmut_6 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁlist_image_streams__mutmut['xǁOpenShiftAdapterǁlist_image_streams__mutmut_7'] = OpenShiftAdapter.xǁOpenShiftAdapterǁlist_image_streams__mutmut_7 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁlist_image_streams__mutmut['xǁOpenShiftAdapterǁlist_image_streams__mutmut_8'] = OpenShiftAdapter.xǁOpenShiftAdapterǁlist_image_streams__mutmut_8 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁlist_image_streams__mutmut['xǁOpenShiftAdapterǁlist_image_streams__mutmut_9'] = OpenShiftAdapter.xǁOpenShiftAdapterǁlist_image_streams__mutmut_9 # type: ignore # mutmut generated

mutants_xǁOpenShiftAdapterǁ_list_cluster__mutmut['_mutmut_orig'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_list_cluster__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁ_list_cluster__mutmut['xǁOpenShiftAdapterǁ_list_cluster__mutmut_1'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_list_cluster__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁ_list_cluster__mutmut['xǁOpenShiftAdapterǁ_list_cluster__mutmut_2'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_list_cluster__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁ_list_cluster__mutmut['xǁOpenShiftAdapterǁ_list_cluster__mutmut_3'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_list_cluster__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁ_list_cluster__mutmut['xǁOpenShiftAdapterǁ_list_cluster__mutmut_4'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_list_cluster__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁ_list_cluster__mutmut['xǁOpenShiftAdapterǁ_list_cluster__mutmut_5'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_list_cluster__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁ_list_cluster__mutmut['xǁOpenShiftAdapterǁ_list_cluster__mutmut_6'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_list_cluster__mutmut_6 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁ_list_cluster__mutmut['xǁOpenShiftAdapterǁ_list_cluster__mutmut_7'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_list_cluster__mutmut_7 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁ_list_cluster__mutmut['xǁOpenShiftAdapterǁ_list_cluster__mutmut_8'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_list_cluster__mutmut_8 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁ_list_cluster__mutmut['xǁOpenShiftAdapterǁ_list_cluster__mutmut_9'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_list_cluster__mutmut_9 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁ_list_cluster__mutmut['xǁOpenShiftAdapterǁ_list_cluster__mutmut_10'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_list_cluster__mutmut_10 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁ_list_cluster__mutmut['xǁOpenShiftAdapterǁ_list_cluster__mutmut_11'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_list_cluster__mutmut_11 # type: ignore # mutmut generated

mutants_xǁOpenShiftAdapterǁ_list_namespaced__mutmut['_mutmut_orig'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_list_namespaced__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁ_list_namespaced__mutmut['xǁOpenShiftAdapterǁ_list_namespaced__mutmut_1'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_list_namespaced__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁ_list_namespaced__mutmut['xǁOpenShiftAdapterǁ_list_namespaced__mutmut_2'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_list_namespaced__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁ_list_namespaced__mutmut['xǁOpenShiftAdapterǁ_list_namespaced__mutmut_3'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_list_namespaced__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁ_list_namespaced__mutmut['xǁOpenShiftAdapterǁ_list_namespaced__mutmut_4'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_list_namespaced__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁ_list_namespaced__mutmut['xǁOpenShiftAdapterǁ_list_namespaced__mutmut_5'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_list_namespaced__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁ_list_namespaced__mutmut['xǁOpenShiftAdapterǁ_list_namespaced__mutmut_6'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_list_namespaced__mutmut_6 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁ_list_namespaced__mutmut['xǁOpenShiftAdapterǁ_list_namespaced__mutmut_7'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_list_namespaced__mutmut_7 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁ_list_namespaced__mutmut['xǁOpenShiftAdapterǁ_list_namespaced__mutmut_8'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_list_namespaced__mutmut_8 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁ_list_namespaced__mutmut['xǁOpenShiftAdapterǁ_list_namespaced__mutmut_9'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_list_namespaced__mutmut_9 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁ_list_namespaced__mutmut['xǁOpenShiftAdapterǁ_list_namespaced__mutmut_10'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_list_namespaced__mutmut_10 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁ_list_namespaced__mutmut['xǁOpenShiftAdapterǁ_list_namespaced__mutmut_11'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_list_namespaced__mutmut_11 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁ_list_namespaced__mutmut['xǁOpenShiftAdapterǁ_list_namespaced__mutmut_12'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_list_namespaced__mutmut_12 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁ_list_namespaced__mutmut['xǁOpenShiftAdapterǁ_list_namespaced__mutmut_13'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_list_namespaced__mutmut_13 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁ_list_namespaced__mutmut['xǁOpenShiftAdapterǁ_list_namespaced__mutmut_14'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_list_namespaced__mutmut_14 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁ_list_namespaced__mutmut['xǁOpenShiftAdapterǁ_list_namespaced__mutmut_15'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_list_namespaced__mutmut_15 # type: ignore # mutmut generated

mutants_xǁOpenShiftAdapterǁ_delegate__mutmut['_mutmut_orig'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_delegate__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁ_delegate__mutmut['xǁOpenShiftAdapterǁ_delegate__mutmut_1'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_delegate__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁ_delegate__mutmut['xǁOpenShiftAdapterǁ_delegate__mutmut_2'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_delegate__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁ_delegate__mutmut['xǁOpenShiftAdapterǁ_delegate__mutmut_3'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_delegate__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁ_delegate__mutmut['xǁOpenShiftAdapterǁ_delegate__mutmut_4'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_delegate__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁ_delegate__mutmut['xǁOpenShiftAdapterǁ_delegate__mutmut_5'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_delegate__mutmut_5 # type: ignore # mutmut generated

mutants_xǁOpenShiftAdapterǁ_client_or_create__mutmut['_mutmut_orig'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_client_or_create__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁ_client_or_create__mutmut['xǁOpenShiftAdapterǁ_client_or_create__mutmut_1'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_client_or_create__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁ_client_or_create__mutmut['xǁOpenShiftAdapterǁ_client_or_create__mutmut_2'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_client_or_create__mutmut_2 # type: ignore # mutmut generated

mutants_xǁOpenShiftAdapterǁ_cluster_short_name__mutmut['_mutmut_orig'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_cluster_short_name__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁ_cluster_short_name__mutmut['xǁOpenShiftAdapterǁ_cluster_short_name__mutmut_1'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_cluster_short_name__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁ_cluster_short_name__mutmut['xǁOpenShiftAdapterǁ_cluster_short_name__mutmut_2'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_cluster_short_name__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁ_cluster_short_name__mutmut['xǁOpenShiftAdapterǁ_cluster_short_name__mutmut_3'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_cluster_short_name__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁ_cluster_short_name__mutmut['xǁOpenShiftAdapterǁ_cluster_short_name__mutmut_4'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_cluster_short_name__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁ_cluster_short_name__mutmut['xǁOpenShiftAdapterǁ_cluster_short_name__mutmut_5'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_cluster_short_name__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOpenShiftAdapterǁ_cluster_short_name__mutmut['xǁOpenShiftAdapterǁ_cluster_short_name__mutmut_6'] = OpenShiftAdapter.xǁOpenShiftAdapterǁ_cluster_short_name__mutmut_6 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__translate_error__mutmut)
def _translate_error(exc: Exception, plural: str, namespace: str | None = None) -> Exception:
    context = {"resource": plural}
    if namespace is not None:
        context["namespace"] = namespace
    if getattr(exc, "status", None) == _FORBIDDEN:
        return InsufficientPermissionsError(f"RBAC denied access to {plural}", context=context)
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading {plural}: {exc}", context=context
    )


def x__translate_error__mutmut_orig(exc: Exception, plural: str, namespace: str | None = None) -> Exception:
    context = {"resource": plural}
    if namespace is not None:
        context["namespace"] = namespace
    if getattr(exc, "status", None) == _FORBIDDEN:
        return InsufficientPermissionsError(f"RBAC denied access to {plural}", context=context)
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading {plural}: {exc}", context=context
    )


def x__translate_error__mutmut_1(exc: Exception, plural: str, namespace: str | None = None) -> Exception:
    context = None
    if namespace is not None:
        context["namespace"] = namespace
    if getattr(exc, "status", None) == _FORBIDDEN:
        return InsufficientPermissionsError(f"RBAC denied access to {plural}", context=context)
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading {plural}: {exc}", context=context
    )


def x__translate_error__mutmut_2(exc: Exception, plural: str, namespace: str | None = None) -> Exception:
    context = {"XXresourceXX": plural}
    if namespace is not None:
        context["namespace"] = namespace
    if getattr(exc, "status", None) == _FORBIDDEN:
        return InsufficientPermissionsError(f"RBAC denied access to {plural}", context=context)
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading {plural}: {exc}", context=context
    )


def x__translate_error__mutmut_3(exc: Exception, plural: str, namespace: str | None = None) -> Exception:
    context = {"RESOURCE": plural}
    if namespace is not None:
        context["namespace"] = namespace
    if getattr(exc, "status", None) == _FORBIDDEN:
        return InsufficientPermissionsError(f"RBAC denied access to {plural}", context=context)
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading {plural}: {exc}", context=context
    )


def x__translate_error__mutmut_4(exc: Exception, plural: str, namespace: str | None = None) -> Exception:
    context = {"resource": plural}
    if namespace is None:
        context["namespace"] = namespace
    if getattr(exc, "status", None) == _FORBIDDEN:
        return InsufficientPermissionsError(f"RBAC denied access to {plural}", context=context)
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading {plural}: {exc}", context=context
    )


def x__translate_error__mutmut_5(exc: Exception, plural: str, namespace: str | None = None) -> Exception:
    context = {"resource": plural}
    if namespace is not None:
        context["namespace"] = None
    if getattr(exc, "status", None) == _FORBIDDEN:
        return InsufficientPermissionsError(f"RBAC denied access to {plural}", context=context)
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading {plural}: {exc}", context=context
    )


def x__translate_error__mutmut_6(exc: Exception, plural: str, namespace: str | None = None) -> Exception:
    context = {"resource": plural}
    if namespace is not None:
        context["XXnamespaceXX"] = namespace
    if getattr(exc, "status", None) == _FORBIDDEN:
        return InsufficientPermissionsError(f"RBAC denied access to {plural}", context=context)
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading {plural}: {exc}", context=context
    )


def x__translate_error__mutmut_7(exc: Exception, plural: str, namespace: str | None = None) -> Exception:
    context = {"resource": plural}
    if namespace is not None:
        context["NAMESPACE"] = namespace
    if getattr(exc, "status", None) == _FORBIDDEN:
        return InsufficientPermissionsError(f"RBAC denied access to {plural}", context=context)
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading {plural}: {exc}", context=context
    )


def x__translate_error__mutmut_8(exc: Exception, plural: str, namespace: str | None = None) -> Exception:
    context = {"resource": plural}
    if namespace is not None:
        context["namespace"] = namespace
    if getattr(None, "status", None) == _FORBIDDEN:
        return InsufficientPermissionsError(f"RBAC denied access to {plural}", context=context)
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading {plural}: {exc}", context=context
    )


def x__translate_error__mutmut_9(exc: Exception, plural: str, namespace: str | None = None) -> Exception:
    context = {"resource": plural}
    if namespace is not None:
        context["namespace"] = namespace
    if getattr(exc, None, None) == _FORBIDDEN:
        return InsufficientPermissionsError(f"RBAC denied access to {plural}", context=context)
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading {plural}: {exc}", context=context
    )


def x__translate_error__mutmut_10(exc: Exception, plural: str, namespace: str | None = None) -> Exception:
    context = {"resource": plural}
    if namespace is not None:
        context["namespace"] = namespace
    if getattr("status", None) == _FORBIDDEN:
        return InsufficientPermissionsError(f"RBAC denied access to {plural}", context=context)
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading {plural}: {exc}", context=context
    )


def x__translate_error__mutmut_11(exc: Exception, plural: str, namespace: str | None = None) -> Exception:
    context = {"resource": plural}
    if namespace is not None:
        context["namespace"] = namespace
    if getattr(exc, None) == _FORBIDDEN:
        return InsufficientPermissionsError(f"RBAC denied access to {plural}", context=context)
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading {plural}: {exc}", context=context
    )


def x__translate_error__mutmut_12(exc: Exception, plural: str, namespace: str | None = None) -> Exception:
    context = {"resource": plural}
    if namespace is not None:
        context["namespace"] = namespace
    if getattr(exc, "status", ) == _FORBIDDEN:
        return InsufficientPermissionsError(f"RBAC denied access to {plural}", context=context)
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading {plural}: {exc}", context=context
    )


def x__translate_error__mutmut_13(exc: Exception, plural: str, namespace: str | None = None) -> Exception:
    context = {"resource": plural}
    if namespace is not None:
        context["namespace"] = namespace
    if getattr(exc, "XXstatusXX", None) == _FORBIDDEN:
        return InsufficientPermissionsError(f"RBAC denied access to {plural}", context=context)
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading {plural}: {exc}", context=context
    )


def x__translate_error__mutmut_14(exc: Exception, plural: str, namespace: str | None = None) -> Exception:
    context = {"resource": plural}
    if namespace is not None:
        context["namespace"] = namespace
    if getattr(exc, "STATUS", None) == _FORBIDDEN:
        return InsufficientPermissionsError(f"RBAC denied access to {plural}", context=context)
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading {plural}: {exc}", context=context
    )


def x__translate_error__mutmut_15(exc: Exception, plural: str, namespace: str | None = None) -> Exception:
    context = {"resource": plural}
    if namespace is not None:
        context["namespace"] = namespace
    if getattr(exc, "status", None) != _FORBIDDEN:
        return InsufficientPermissionsError(f"RBAC denied access to {plural}", context=context)
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading {plural}: {exc}", context=context
    )


def x__translate_error__mutmut_16(exc: Exception, plural: str, namespace: str | None = None) -> Exception:
    context = {"resource": plural}
    if namespace is not None:
        context["namespace"] = namespace
    if getattr(exc, "status", None) == _FORBIDDEN:
        return InsufficientPermissionsError(None, context=context)
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading {plural}: {exc}", context=context
    )


def x__translate_error__mutmut_17(exc: Exception, plural: str, namespace: str | None = None) -> Exception:
    context = {"resource": plural}
    if namespace is not None:
        context["namespace"] = namespace
    if getattr(exc, "status", None) == _FORBIDDEN:
        return InsufficientPermissionsError(f"RBAC denied access to {plural}", context=None)
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading {plural}: {exc}", context=context
    )


def x__translate_error__mutmut_18(exc: Exception, plural: str, namespace: str | None = None) -> Exception:
    context = {"resource": plural}
    if namespace is not None:
        context["namespace"] = namespace
    if getattr(exc, "status", None) == _FORBIDDEN:
        return InsufficientPermissionsError(context=context)
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading {plural}: {exc}", context=context
    )


def x__translate_error__mutmut_19(exc: Exception, plural: str, namespace: str | None = None) -> Exception:
    context = {"resource": plural}
    if namespace is not None:
        context["namespace"] = namespace
    if getattr(exc, "status", None) == _FORBIDDEN:
        return InsufficientPermissionsError(f"RBAC denied access to {plural}", )
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading {plural}: {exc}", context=context
    )


def x__translate_error__mutmut_20(exc: Exception, plural: str, namespace: str | None = None) -> Exception:
    context = {"resource": plural}
    if namespace is not None:
        context["namespace"] = namespace
    if getattr(exc, "status", None) == _FORBIDDEN:
        return InsufficientPermissionsError(f"RBAC denied access to {plural}", context=context)
    return ClusterUnreachableError(
        None, context=context
    )


def x__translate_error__mutmut_21(exc: Exception, plural: str, namespace: str | None = None) -> Exception:
    context = {"resource": plural}
    if namespace is not None:
        context["namespace"] = namespace
    if getattr(exc, "status", None) == _FORBIDDEN:
        return InsufficientPermissionsError(f"RBAC denied access to {plural}", context=context)
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading {plural}: {exc}", context=None
    )


def x__translate_error__mutmut_22(exc: Exception, plural: str, namespace: str | None = None) -> Exception:
    context = {"resource": plural}
    if namespace is not None:
        context["namespace"] = namespace
    if getattr(exc, "status", None) == _FORBIDDEN:
        return InsufficientPermissionsError(f"RBAC denied access to {plural}", context=context)
    return ClusterUnreachableError(
        context=context
    )


def x__translate_error__mutmut_23(exc: Exception, plural: str, namespace: str | None = None) -> Exception:
    context = {"resource": plural}
    if namespace is not None:
        context["namespace"] = namespace
    if getattr(exc, "status", None) == _FORBIDDEN:
        return InsufficientPermissionsError(f"RBAC denied access to {plural}", context=context)
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading {plural}: {exc}", )

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
mutants_x__translate_error__mutmut['x__translate_error__mutmut_15'] = x__translate_error__mutmut_15 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_16'] = x__translate_error__mutmut_16 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_17'] = x__translate_error__mutmut_17 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_18'] = x__translate_error__mutmut_18 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_19'] = x__translate_error__mutmut_19 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_20'] = x__translate_error__mutmut_20 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_21'] = x__translate_error__mutmut_21 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_22'] = x__translate_error__mutmut_22 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_23'] = x__translate_error__mutmut_23 # type: ignore # mutmut generated
mutants_x__items__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__items__mutmut)
def _items(payload: Mapping[str, object]) -> list[Mapping[str, object]]:
    raw = payload.get("items")
    if not isinstance(raw, list):
        return []
    return [item for item in raw if isinstance(item, Mapping)]


def x__items__mutmut_orig(payload: Mapping[str, object]) -> list[Mapping[str, object]]:
    raw = payload.get("items")
    if not isinstance(raw, list):
        return []
    return [item for item in raw if isinstance(item, Mapping)]


def x__items__mutmut_1(payload: Mapping[str, object]) -> list[Mapping[str, object]]:
    raw = None
    if not isinstance(raw, list):
        return []
    return [item for item in raw if isinstance(item, Mapping)]


def x__items__mutmut_2(payload: Mapping[str, object]) -> list[Mapping[str, object]]:
    raw = payload.get(None)
    if not isinstance(raw, list):
        return []
    return [item for item in raw if isinstance(item, Mapping)]


def x__items__mutmut_3(payload: Mapping[str, object]) -> list[Mapping[str, object]]:
    raw = payload.get("XXitemsXX")
    if not isinstance(raw, list):
        return []
    return [item for item in raw if isinstance(item, Mapping)]


def x__items__mutmut_4(payload: Mapping[str, object]) -> list[Mapping[str, object]]:
    raw = payload.get("ITEMS")
    if not isinstance(raw, list):
        return []
    return [item for item in raw if isinstance(item, Mapping)]


def x__items__mutmut_5(payload: Mapping[str, object]) -> list[Mapping[str, object]]:
    raw = payload.get("items")
    if isinstance(raw, list):
        return []
    return [item for item in raw if isinstance(item, Mapping)]

mutants_x__items__mutmut['_mutmut_orig'] = x__items__mutmut_orig # type: ignore # mutmut generated
mutants_x__items__mutmut['x__items__mutmut_1'] = x__items__mutmut_1 # type: ignore # mutmut generated
mutants_x__items__mutmut['x__items__mutmut_2'] = x__items__mutmut_2 # type: ignore # mutmut generated
mutants_x__items__mutmut['x__items__mutmut_3'] = x__items__mutmut_3 # type: ignore # mutmut generated
mutants_x__items__mutmut['x__items__mutmut_4'] = x__items__mutmut_4 # type: ignore # mutmut generated
mutants_x__items__mutmut['x__items__mutmut_5'] = x__items__mutmut_5 # type: ignore # mutmut generated
mutants_x__metadata__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__metadata__mutmut)
def _metadata(item: Mapping[str, object]) -> Mapping[str, object]:
    meta = item.get("metadata")
    return meta if isinstance(meta, Mapping) else {}


def x__metadata__mutmut_orig(item: Mapping[str, object]) -> Mapping[str, object]:
    meta = item.get("metadata")
    return meta if isinstance(meta, Mapping) else {}


def x__metadata__mutmut_1(item: Mapping[str, object]) -> Mapping[str, object]:
    meta = None
    return meta if isinstance(meta, Mapping) else {}


def x__metadata__mutmut_2(item: Mapping[str, object]) -> Mapping[str, object]:
    meta = item.get(None)
    return meta if isinstance(meta, Mapping) else {}


def x__metadata__mutmut_3(item: Mapping[str, object]) -> Mapping[str, object]:
    meta = item.get("XXmetadataXX")
    return meta if isinstance(meta, Mapping) else {}


def x__metadata__mutmut_4(item: Mapping[str, object]) -> Mapping[str, object]:
    meta = item.get("METADATA")
    return meta if isinstance(meta, Mapping) else {}

mutants_x__metadata__mutmut['_mutmut_orig'] = x__metadata__mutmut_orig # type: ignore # mutmut generated
mutants_x__metadata__mutmut['x__metadata__mutmut_1'] = x__metadata__mutmut_1 # type: ignore # mutmut generated
mutants_x__metadata__mutmut['x__metadata__mutmut_2'] = x__metadata__mutmut_2 # type: ignore # mutmut generated
mutants_x__metadata__mutmut['x__metadata__mutmut_3'] = x__metadata__mutmut_3 # type: ignore # mutmut generated
mutants_x__metadata__mutmut['x__metadata__mutmut_4'] = x__metadata__mutmut_4 # type: ignore # mutmut generated
mutants_x__mapping__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__mapping__mutmut)
def _mapping(item: Mapping[str, object], key: str) -> Mapping[str, object]:
    value = item.get(key)
    return value if isinstance(value, Mapping) else {}


def x__mapping__mutmut_orig(item: Mapping[str, object], key: str) -> Mapping[str, object]:
    value = item.get(key)
    return value if isinstance(value, Mapping) else {}


def x__mapping__mutmut_1(item: Mapping[str, object], key: str) -> Mapping[str, object]:
    value = None
    return value if isinstance(value, Mapping) else {}


def x__mapping__mutmut_2(item: Mapping[str, object], key: str) -> Mapping[str, object]:
    value = item.get(None)
    return value if isinstance(value, Mapping) else {}

mutants_x__mapping__mutmut['_mutmut_orig'] = x__mapping__mutmut_orig # type: ignore # mutmut generated
mutants_x__mapping__mutmut['x__mapping__mutmut_1'] = x__mapping__mutmut_1 # type: ignore # mutmut generated
mutants_x__mapping__mutmut['x__mapping__mutmut_2'] = x__mapping__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_project__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_project__mutmut)
def _to_project(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(meta.get("name", "")),
        status=str(status.get("phase", "Unknown")),
        display_name=str(spec.get("displayName", "")),
    )


def x__to_project__mutmut_orig(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(meta.get("name", "")),
        status=str(status.get("phase", "Unknown")),
        display_name=str(spec.get("displayName", "")),
    )


def x__to_project__mutmut_1(item: Mapping[str, object]) -> ProjectInfo:
    meta = None
    status = _mapping(item, "status")
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(meta.get("name", "")),
        status=str(status.get("phase", "Unknown")),
        display_name=str(spec.get("displayName", "")),
    )


def x__to_project__mutmut_2(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(None)
    status = _mapping(item, "status")
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(meta.get("name", "")),
        status=str(status.get("phase", "Unknown")),
        display_name=str(spec.get("displayName", "")),
    )


def x__to_project__mutmut_3(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = None
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(meta.get("name", "")),
        status=str(status.get("phase", "Unknown")),
        display_name=str(spec.get("displayName", "")),
    )


def x__to_project__mutmut_4(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(None, "status")
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(meta.get("name", "")),
        status=str(status.get("phase", "Unknown")),
        display_name=str(spec.get("displayName", "")),
    )


def x__to_project__mutmut_5(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, None)
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(meta.get("name", "")),
        status=str(status.get("phase", "Unknown")),
        display_name=str(spec.get("displayName", "")),
    )


def x__to_project__mutmut_6(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping("status")
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(meta.get("name", "")),
        status=str(status.get("phase", "Unknown")),
        display_name=str(spec.get("displayName", "")),
    )


def x__to_project__mutmut_7(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, )
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(meta.get("name", "")),
        status=str(status.get("phase", "Unknown")),
        display_name=str(spec.get("displayName", "")),
    )


def x__to_project__mutmut_8(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "XXstatusXX")
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(meta.get("name", "")),
        status=str(status.get("phase", "Unknown")),
        display_name=str(spec.get("displayName", "")),
    )


def x__to_project__mutmut_9(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "STATUS")
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(meta.get("name", "")),
        status=str(status.get("phase", "Unknown")),
        display_name=str(spec.get("displayName", "")),
    )


def x__to_project__mutmut_10(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = None
    return ProjectInfo(
        name=str(meta.get("name", "")),
        status=str(status.get("phase", "Unknown")),
        display_name=str(spec.get("displayName", "")),
    )


def x__to_project__mutmut_11(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = _mapping(None, "spec")
    return ProjectInfo(
        name=str(meta.get("name", "")),
        status=str(status.get("phase", "Unknown")),
        display_name=str(spec.get("displayName", "")),
    )


def x__to_project__mutmut_12(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = _mapping(item, None)
    return ProjectInfo(
        name=str(meta.get("name", "")),
        status=str(status.get("phase", "Unknown")),
        display_name=str(spec.get("displayName", "")),
    )


def x__to_project__mutmut_13(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = _mapping("spec")
    return ProjectInfo(
        name=str(meta.get("name", "")),
        status=str(status.get("phase", "Unknown")),
        display_name=str(spec.get("displayName", "")),
    )


def x__to_project__mutmut_14(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = _mapping(item, )
    return ProjectInfo(
        name=str(meta.get("name", "")),
        status=str(status.get("phase", "Unknown")),
        display_name=str(spec.get("displayName", "")),
    )


def x__to_project__mutmut_15(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = _mapping(item, "XXspecXX")
    return ProjectInfo(
        name=str(meta.get("name", "")),
        status=str(status.get("phase", "Unknown")),
        display_name=str(spec.get("displayName", "")),
    )


def x__to_project__mutmut_16(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = _mapping(item, "SPEC")
    return ProjectInfo(
        name=str(meta.get("name", "")),
        status=str(status.get("phase", "Unknown")),
        display_name=str(spec.get("displayName", "")),
    )


def x__to_project__mutmut_17(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=None,
        status=str(status.get("phase", "Unknown")),
        display_name=str(spec.get("displayName", "")),
    )


def x__to_project__mutmut_18(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(meta.get("name", "")),
        status=None,
        display_name=str(spec.get("displayName", "")),
    )


def x__to_project__mutmut_19(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(meta.get("name", "")),
        status=str(status.get("phase", "Unknown")),
        display_name=None,
    )


def x__to_project__mutmut_20(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = _mapping(item, "spec")
    return ProjectInfo(
        status=str(status.get("phase", "Unknown")),
        display_name=str(spec.get("displayName", "")),
    )


def x__to_project__mutmut_21(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(meta.get("name", "")),
        display_name=str(spec.get("displayName", "")),
    )


def x__to_project__mutmut_22(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(meta.get("name", "")),
        status=str(status.get("phase", "Unknown")),
        )


def x__to_project__mutmut_23(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(None),
        status=str(status.get("phase", "Unknown")),
        display_name=str(spec.get("displayName", "")),
    )


def x__to_project__mutmut_24(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(meta.get(None, "")),
        status=str(status.get("phase", "Unknown")),
        display_name=str(spec.get("displayName", "")),
    )


def x__to_project__mutmut_25(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(meta.get("name", None)),
        status=str(status.get("phase", "Unknown")),
        display_name=str(spec.get("displayName", "")),
    )


def x__to_project__mutmut_26(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(meta.get("")),
        status=str(status.get("phase", "Unknown")),
        display_name=str(spec.get("displayName", "")),
    )


def x__to_project__mutmut_27(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(meta.get("name", )),
        status=str(status.get("phase", "Unknown")),
        display_name=str(spec.get("displayName", "")),
    )


def x__to_project__mutmut_28(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(meta.get("XXnameXX", "")),
        status=str(status.get("phase", "Unknown")),
        display_name=str(spec.get("displayName", "")),
    )


def x__to_project__mutmut_29(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(meta.get("NAME", "")),
        status=str(status.get("phase", "Unknown")),
        display_name=str(spec.get("displayName", "")),
    )


def x__to_project__mutmut_30(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(meta.get("name", "XXXX")),
        status=str(status.get("phase", "Unknown")),
        display_name=str(spec.get("displayName", "")),
    )


def x__to_project__mutmut_31(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(meta.get("name", "")),
        status=str(None),
        display_name=str(spec.get("displayName", "")),
    )


def x__to_project__mutmut_32(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(meta.get("name", "")),
        status=str(status.get(None, "Unknown")),
        display_name=str(spec.get("displayName", "")),
    )


def x__to_project__mutmut_33(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(meta.get("name", "")),
        status=str(status.get("phase", None)),
        display_name=str(spec.get("displayName", "")),
    )


def x__to_project__mutmut_34(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(meta.get("name", "")),
        status=str(status.get("Unknown")),
        display_name=str(spec.get("displayName", "")),
    )


def x__to_project__mutmut_35(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(meta.get("name", "")),
        status=str(status.get("phase", )),
        display_name=str(spec.get("displayName", "")),
    )


def x__to_project__mutmut_36(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(meta.get("name", "")),
        status=str(status.get("XXphaseXX", "Unknown")),
        display_name=str(spec.get("displayName", "")),
    )


def x__to_project__mutmut_37(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(meta.get("name", "")),
        status=str(status.get("PHASE", "Unknown")),
        display_name=str(spec.get("displayName", "")),
    )


def x__to_project__mutmut_38(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(meta.get("name", "")),
        status=str(status.get("phase", "XXUnknownXX")),
        display_name=str(spec.get("displayName", "")),
    )


def x__to_project__mutmut_39(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(meta.get("name", "")),
        status=str(status.get("phase", "unknown")),
        display_name=str(spec.get("displayName", "")),
    )


def x__to_project__mutmut_40(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(meta.get("name", "")),
        status=str(status.get("phase", "UNKNOWN")),
        display_name=str(spec.get("displayName", "")),
    )


def x__to_project__mutmut_41(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(meta.get("name", "")),
        status=str(status.get("phase", "Unknown")),
        display_name=str(None),
    )


def x__to_project__mutmut_42(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(meta.get("name", "")),
        status=str(status.get("phase", "Unknown")),
        display_name=str(spec.get(None, "")),
    )


def x__to_project__mutmut_43(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(meta.get("name", "")),
        status=str(status.get("phase", "Unknown")),
        display_name=str(spec.get("displayName", None)),
    )


def x__to_project__mutmut_44(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(meta.get("name", "")),
        status=str(status.get("phase", "Unknown")),
        display_name=str(spec.get("")),
    )


def x__to_project__mutmut_45(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(meta.get("name", "")),
        status=str(status.get("phase", "Unknown")),
        display_name=str(spec.get("displayName", )),
    )


def x__to_project__mutmut_46(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(meta.get("name", "")),
        status=str(status.get("phase", "Unknown")),
        display_name=str(spec.get("XXdisplayNameXX", "")),
    )


def x__to_project__mutmut_47(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(meta.get("name", "")),
        status=str(status.get("phase", "Unknown")),
        display_name=str(spec.get("displayname", "")),
    )


def x__to_project__mutmut_48(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(meta.get("name", "")),
        status=str(status.get("phase", "Unknown")),
        display_name=str(spec.get("DISPLAYNAME", "")),
    )


def x__to_project__mutmut_49(item: Mapping[str, object]) -> ProjectInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    spec = _mapping(item, "spec")
    return ProjectInfo(
        name=str(meta.get("name", "")),
        status=str(status.get("phase", "Unknown")),
        display_name=str(spec.get("displayName", "XXXX")),
    )

mutants_x__to_project__mutmut['_mutmut_orig'] = x__to_project__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_1'] = x__to_project__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_2'] = x__to_project__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_3'] = x__to_project__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_4'] = x__to_project__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_5'] = x__to_project__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_6'] = x__to_project__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_7'] = x__to_project__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_8'] = x__to_project__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_9'] = x__to_project__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_10'] = x__to_project__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_11'] = x__to_project__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_12'] = x__to_project__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_13'] = x__to_project__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_14'] = x__to_project__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_15'] = x__to_project__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_16'] = x__to_project__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_17'] = x__to_project__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_18'] = x__to_project__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_19'] = x__to_project__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_20'] = x__to_project__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_21'] = x__to_project__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_22'] = x__to_project__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_23'] = x__to_project__mutmut_23 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_24'] = x__to_project__mutmut_24 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_25'] = x__to_project__mutmut_25 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_26'] = x__to_project__mutmut_26 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_27'] = x__to_project__mutmut_27 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_28'] = x__to_project__mutmut_28 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_29'] = x__to_project__mutmut_29 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_30'] = x__to_project__mutmut_30 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_31'] = x__to_project__mutmut_31 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_32'] = x__to_project__mutmut_32 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_33'] = x__to_project__mutmut_33 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_34'] = x__to_project__mutmut_34 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_35'] = x__to_project__mutmut_35 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_36'] = x__to_project__mutmut_36 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_37'] = x__to_project__mutmut_37 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_38'] = x__to_project__mutmut_38 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_39'] = x__to_project__mutmut_39 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_40'] = x__to_project__mutmut_40 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_41'] = x__to_project__mutmut_41 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_42'] = x__to_project__mutmut_42 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_43'] = x__to_project__mutmut_43 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_44'] = x__to_project__mutmut_44 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_45'] = x__to_project__mutmut_45 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_46'] = x__to_project__mutmut_46 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_47'] = x__to_project__mutmut_47 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_48'] = x__to_project__mutmut_48 # type: ignore # mutmut generated
mutants_x__to_project__mutmut['x__to_project__mutmut_49'] = x__to_project__mutmut_49 # type: ignore # mutmut generated
mutants_x__to_route__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_route__mutmut)
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


def x__to_route__mutmut_orig(item: Mapping[str, object]) -> RouteInfo:
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


def x__to_route__mutmut_1(item: Mapping[str, object]) -> RouteInfo:
    meta = None
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_2(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(None)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_3(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = None
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_4(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(None, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_5(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, None)
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_6(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping("spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_7(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, )
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_8(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "XXspecXX")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_9(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "SPEC")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_10(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = None
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_11(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(None, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_12(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, None)
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_13(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping("to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_14(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, )
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_15(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "XXtoXX")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_16(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "TO")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_17(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=None,
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_18(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=None,
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_19(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        host=None,
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_20(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "")),
        target_service=None,
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_21(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled=None,
    )


def x__to_route__mutmut_22(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_23(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_24(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_25(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_26(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "")),
        )


def x__to_route__mutmut_27(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(None),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_28(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get(None, "")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_29(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", None)),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_30(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_31(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", )),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_32(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("XXnameXX", "")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_33(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("NAME", "")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_34(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "XXXX")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_35(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(None),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_36(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get(None, "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_37(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", None)),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_38(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_39(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", )),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_40(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("XXnamespaceXX", "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_41(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("NAMESPACE", "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_42(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "XXXX")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_43(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        host=str(None),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_44(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get(None, "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_45(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", None)),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_46(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_47(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", )),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_48(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("XXhostXX", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_49(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("HOST", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_50(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "XXXX")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_51(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "")),
        target_service=str(None),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_52(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get(None, "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_53(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", None)),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_54(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_55(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", )),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_56(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("XXnameXX", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_57(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("NAME", "")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_58(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "XXXX")),
        tls_enabled="tls" in spec,
    )


def x__to_route__mutmut_59(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="XXtlsXX" in spec,
    )


def x__to_route__mutmut_60(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="TLS" in spec,
    )


def x__to_route__mutmut_61(item: Mapping[str, object]) -> RouteInfo:
    meta = _metadata(item)
    spec = _mapping(item, "spec")
    to_target = _mapping(spec, "to")
    return RouteInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        host=str(spec.get("host", "")),
        target_service=str(to_target.get("name", "")),
        tls_enabled="tls" not in spec,
    )

mutants_x__to_route__mutmut['_mutmut_orig'] = x__to_route__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_1'] = x__to_route__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_2'] = x__to_route__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_3'] = x__to_route__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_4'] = x__to_route__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_5'] = x__to_route__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_6'] = x__to_route__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_7'] = x__to_route__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_8'] = x__to_route__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_9'] = x__to_route__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_10'] = x__to_route__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_11'] = x__to_route__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_12'] = x__to_route__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_13'] = x__to_route__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_14'] = x__to_route__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_15'] = x__to_route__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_16'] = x__to_route__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_17'] = x__to_route__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_18'] = x__to_route__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_19'] = x__to_route__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_20'] = x__to_route__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_21'] = x__to_route__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_22'] = x__to_route__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_23'] = x__to_route__mutmut_23 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_24'] = x__to_route__mutmut_24 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_25'] = x__to_route__mutmut_25 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_26'] = x__to_route__mutmut_26 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_27'] = x__to_route__mutmut_27 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_28'] = x__to_route__mutmut_28 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_29'] = x__to_route__mutmut_29 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_30'] = x__to_route__mutmut_30 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_31'] = x__to_route__mutmut_31 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_32'] = x__to_route__mutmut_32 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_33'] = x__to_route__mutmut_33 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_34'] = x__to_route__mutmut_34 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_35'] = x__to_route__mutmut_35 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_36'] = x__to_route__mutmut_36 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_37'] = x__to_route__mutmut_37 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_38'] = x__to_route__mutmut_38 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_39'] = x__to_route__mutmut_39 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_40'] = x__to_route__mutmut_40 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_41'] = x__to_route__mutmut_41 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_42'] = x__to_route__mutmut_42 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_43'] = x__to_route__mutmut_43 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_44'] = x__to_route__mutmut_44 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_45'] = x__to_route__mutmut_45 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_46'] = x__to_route__mutmut_46 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_47'] = x__to_route__mutmut_47 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_48'] = x__to_route__mutmut_48 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_49'] = x__to_route__mutmut_49 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_50'] = x__to_route__mutmut_50 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_51'] = x__to_route__mutmut_51 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_52'] = x__to_route__mutmut_52 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_53'] = x__to_route__mutmut_53 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_54'] = x__to_route__mutmut_54 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_55'] = x__to_route__mutmut_55 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_56'] = x__to_route__mutmut_56 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_57'] = x__to_route__mutmut_57 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_58'] = x__to_route__mutmut_58 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_59'] = x__to_route__mutmut_59 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_60'] = x__to_route__mutmut_60 # type: ignore # mutmut generated
mutants_x__to_route__mutmut['x__to_route__mutmut_61'] = x__to_route__mutmut_61 # type: ignore # mutmut generated
mutants_x__to_scc__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_scc__mutmut)
def _to_scc(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(item)
    run_as_user = _mapping(item, "runAsUser")
    return SecurityContextConstraintInfo(
        name=str(meta.get("name", "")),
        allow_privileged_container=bool(item.get("allowPrivilegedContainer", False)),
        run_as_user_type=str(run_as_user.get("type", "")),
    )


def x__to_scc__mutmut_orig(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(item)
    run_as_user = _mapping(item, "runAsUser")
    return SecurityContextConstraintInfo(
        name=str(meta.get("name", "")),
        allow_privileged_container=bool(item.get("allowPrivilegedContainer", False)),
        run_as_user_type=str(run_as_user.get("type", "")),
    )


def x__to_scc__mutmut_1(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = None
    run_as_user = _mapping(item, "runAsUser")
    return SecurityContextConstraintInfo(
        name=str(meta.get("name", "")),
        allow_privileged_container=bool(item.get("allowPrivilegedContainer", False)),
        run_as_user_type=str(run_as_user.get("type", "")),
    )


def x__to_scc__mutmut_2(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(None)
    run_as_user = _mapping(item, "runAsUser")
    return SecurityContextConstraintInfo(
        name=str(meta.get("name", "")),
        allow_privileged_container=bool(item.get("allowPrivilegedContainer", False)),
        run_as_user_type=str(run_as_user.get("type", "")),
    )


def x__to_scc__mutmut_3(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(item)
    run_as_user = None
    return SecurityContextConstraintInfo(
        name=str(meta.get("name", "")),
        allow_privileged_container=bool(item.get("allowPrivilegedContainer", False)),
        run_as_user_type=str(run_as_user.get("type", "")),
    )


def x__to_scc__mutmut_4(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(item)
    run_as_user = _mapping(None, "runAsUser")
    return SecurityContextConstraintInfo(
        name=str(meta.get("name", "")),
        allow_privileged_container=bool(item.get("allowPrivilegedContainer", False)),
        run_as_user_type=str(run_as_user.get("type", "")),
    )


def x__to_scc__mutmut_5(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(item)
    run_as_user = _mapping(item, None)
    return SecurityContextConstraintInfo(
        name=str(meta.get("name", "")),
        allow_privileged_container=bool(item.get("allowPrivilegedContainer", False)),
        run_as_user_type=str(run_as_user.get("type", "")),
    )


def x__to_scc__mutmut_6(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(item)
    run_as_user = _mapping("runAsUser")
    return SecurityContextConstraintInfo(
        name=str(meta.get("name", "")),
        allow_privileged_container=bool(item.get("allowPrivilegedContainer", False)),
        run_as_user_type=str(run_as_user.get("type", "")),
    )


def x__to_scc__mutmut_7(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(item)
    run_as_user = _mapping(item, )
    return SecurityContextConstraintInfo(
        name=str(meta.get("name", "")),
        allow_privileged_container=bool(item.get("allowPrivilegedContainer", False)),
        run_as_user_type=str(run_as_user.get("type", "")),
    )


def x__to_scc__mutmut_8(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(item)
    run_as_user = _mapping(item, "XXrunAsUserXX")
    return SecurityContextConstraintInfo(
        name=str(meta.get("name", "")),
        allow_privileged_container=bool(item.get("allowPrivilegedContainer", False)),
        run_as_user_type=str(run_as_user.get("type", "")),
    )


def x__to_scc__mutmut_9(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(item)
    run_as_user = _mapping(item, "runasuser")
    return SecurityContextConstraintInfo(
        name=str(meta.get("name", "")),
        allow_privileged_container=bool(item.get("allowPrivilegedContainer", False)),
        run_as_user_type=str(run_as_user.get("type", "")),
    )


def x__to_scc__mutmut_10(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(item)
    run_as_user = _mapping(item, "RUNASUSER")
    return SecurityContextConstraintInfo(
        name=str(meta.get("name", "")),
        allow_privileged_container=bool(item.get("allowPrivilegedContainer", False)),
        run_as_user_type=str(run_as_user.get("type", "")),
    )


def x__to_scc__mutmut_11(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(item)
    run_as_user = _mapping(item, "runAsUser")
    return SecurityContextConstraintInfo(
        name=None,
        allow_privileged_container=bool(item.get("allowPrivilegedContainer", False)),
        run_as_user_type=str(run_as_user.get("type", "")),
    )


def x__to_scc__mutmut_12(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(item)
    run_as_user = _mapping(item, "runAsUser")
    return SecurityContextConstraintInfo(
        name=str(meta.get("name", "")),
        allow_privileged_container=None,
        run_as_user_type=str(run_as_user.get("type", "")),
    )


def x__to_scc__mutmut_13(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(item)
    run_as_user = _mapping(item, "runAsUser")
    return SecurityContextConstraintInfo(
        name=str(meta.get("name", "")),
        allow_privileged_container=bool(item.get("allowPrivilegedContainer", False)),
        run_as_user_type=None,
    )


def x__to_scc__mutmut_14(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(item)
    run_as_user = _mapping(item, "runAsUser")
    return SecurityContextConstraintInfo(
        allow_privileged_container=bool(item.get("allowPrivilegedContainer", False)),
        run_as_user_type=str(run_as_user.get("type", "")),
    )


def x__to_scc__mutmut_15(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(item)
    run_as_user = _mapping(item, "runAsUser")
    return SecurityContextConstraintInfo(
        name=str(meta.get("name", "")),
        run_as_user_type=str(run_as_user.get("type", "")),
    )


def x__to_scc__mutmut_16(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(item)
    run_as_user = _mapping(item, "runAsUser")
    return SecurityContextConstraintInfo(
        name=str(meta.get("name", "")),
        allow_privileged_container=bool(item.get("allowPrivilegedContainer", False)),
        )


def x__to_scc__mutmut_17(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(item)
    run_as_user = _mapping(item, "runAsUser")
    return SecurityContextConstraintInfo(
        name=str(None),
        allow_privileged_container=bool(item.get("allowPrivilegedContainer", False)),
        run_as_user_type=str(run_as_user.get("type", "")),
    )


def x__to_scc__mutmut_18(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(item)
    run_as_user = _mapping(item, "runAsUser")
    return SecurityContextConstraintInfo(
        name=str(meta.get(None, "")),
        allow_privileged_container=bool(item.get("allowPrivilegedContainer", False)),
        run_as_user_type=str(run_as_user.get("type", "")),
    )


def x__to_scc__mutmut_19(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(item)
    run_as_user = _mapping(item, "runAsUser")
    return SecurityContextConstraintInfo(
        name=str(meta.get("name", None)),
        allow_privileged_container=bool(item.get("allowPrivilegedContainer", False)),
        run_as_user_type=str(run_as_user.get("type", "")),
    )


def x__to_scc__mutmut_20(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(item)
    run_as_user = _mapping(item, "runAsUser")
    return SecurityContextConstraintInfo(
        name=str(meta.get("")),
        allow_privileged_container=bool(item.get("allowPrivilegedContainer", False)),
        run_as_user_type=str(run_as_user.get("type", "")),
    )


def x__to_scc__mutmut_21(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(item)
    run_as_user = _mapping(item, "runAsUser")
    return SecurityContextConstraintInfo(
        name=str(meta.get("name", )),
        allow_privileged_container=bool(item.get("allowPrivilegedContainer", False)),
        run_as_user_type=str(run_as_user.get("type", "")),
    )


def x__to_scc__mutmut_22(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(item)
    run_as_user = _mapping(item, "runAsUser")
    return SecurityContextConstraintInfo(
        name=str(meta.get("XXnameXX", "")),
        allow_privileged_container=bool(item.get("allowPrivilegedContainer", False)),
        run_as_user_type=str(run_as_user.get("type", "")),
    )


def x__to_scc__mutmut_23(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(item)
    run_as_user = _mapping(item, "runAsUser")
    return SecurityContextConstraintInfo(
        name=str(meta.get("NAME", "")),
        allow_privileged_container=bool(item.get("allowPrivilegedContainer", False)),
        run_as_user_type=str(run_as_user.get("type", "")),
    )


def x__to_scc__mutmut_24(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(item)
    run_as_user = _mapping(item, "runAsUser")
    return SecurityContextConstraintInfo(
        name=str(meta.get("name", "XXXX")),
        allow_privileged_container=bool(item.get("allowPrivilegedContainer", False)),
        run_as_user_type=str(run_as_user.get("type", "")),
    )


def x__to_scc__mutmut_25(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(item)
    run_as_user = _mapping(item, "runAsUser")
    return SecurityContextConstraintInfo(
        name=str(meta.get("name", "")),
        allow_privileged_container=bool(None),
        run_as_user_type=str(run_as_user.get("type", "")),
    )


def x__to_scc__mutmut_26(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(item)
    run_as_user = _mapping(item, "runAsUser")
    return SecurityContextConstraintInfo(
        name=str(meta.get("name", "")),
        allow_privileged_container=bool(item.get(None, False)),
        run_as_user_type=str(run_as_user.get("type", "")),
    )


def x__to_scc__mutmut_27(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(item)
    run_as_user = _mapping(item, "runAsUser")
    return SecurityContextConstraintInfo(
        name=str(meta.get("name", "")),
        allow_privileged_container=bool(item.get("allowPrivilegedContainer", None)),
        run_as_user_type=str(run_as_user.get("type", "")),
    )


def x__to_scc__mutmut_28(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(item)
    run_as_user = _mapping(item, "runAsUser")
    return SecurityContextConstraintInfo(
        name=str(meta.get("name", "")),
        allow_privileged_container=bool(item.get(False)),
        run_as_user_type=str(run_as_user.get("type", "")),
    )


def x__to_scc__mutmut_29(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(item)
    run_as_user = _mapping(item, "runAsUser")
    return SecurityContextConstraintInfo(
        name=str(meta.get("name", "")),
        allow_privileged_container=bool(item.get("allowPrivilegedContainer", )),
        run_as_user_type=str(run_as_user.get("type", "")),
    )


def x__to_scc__mutmut_30(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(item)
    run_as_user = _mapping(item, "runAsUser")
    return SecurityContextConstraintInfo(
        name=str(meta.get("name", "")),
        allow_privileged_container=bool(item.get("XXallowPrivilegedContainerXX", False)),
        run_as_user_type=str(run_as_user.get("type", "")),
    )


def x__to_scc__mutmut_31(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(item)
    run_as_user = _mapping(item, "runAsUser")
    return SecurityContextConstraintInfo(
        name=str(meta.get("name", "")),
        allow_privileged_container=bool(item.get("allowprivilegedcontainer", False)),
        run_as_user_type=str(run_as_user.get("type", "")),
    )


def x__to_scc__mutmut_32(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(item)
    run_as_user = _mapping(item, "runAsUser")
    return SecurityContextConstraintInfo(
        name=str(meta.get("name", "")),
        allow_privileged_container=bool(item.get("ALLOWPRIVILEGEDCONTAINER", False)),
        run_as_user_type=str(run_as_user.get("type", "")),
    )


def x__to_scc__mutmut_33(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(item)
    run_as_user = _mapping(item, "runAsUser")
    return SecurityContextConstraintInfo(
        name=str(meta.get("name", "")),
        allow_privileged_container=bool(item.get("allowPrivilegedContainer", True)),
        run_as_user_type=str(run_as_user.get("type", "")),
    )


def x__to_scc__mutmut_34(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(item)
    run_as_user = _mapping(item, "runAsUser")
    return SecurityContextConstraintInfo(
        name=str(meta.get("name", "")),
        allow_privileged_container=bool(item.get("allowPrivilegedContainer", False)),
        run_as_user_type=str(None),
    )


def x__to_scc__mutmut_35(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(item)
    run_as_user = _mapping(item, "runAsUser")
    return SecurityContextConstraintInfo(
        name=str(meta.get("name", "")),
        allow_privileged_container=bool(item.get("allowPrivilegedContainer", False)),
        run_as_user_type=str(run_as_user.get(None, "")),
    )


def x__to_scc__mutmut_36(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(item)
    run_as_user = _mapping(item, "runAsUser")
    return SecurityContextConstraintInfo(
        name=str(meta.get("name", "")),
        allow_privileged_container=bool(item.get("allowPrivilegedContainer", False)),
        run_as_user_type=str(run_as_user.get("type", None)),
    )


def x__to_scc__mutmut_37(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(item)
    run_as_user = _mapping(item, "runAsUser")
    return SecurityContextConstraintInfo(
        name=str(meta.get("name", "")),
        allow_privileged_container=bool(item.get("allowPrivilegedContainer", False)),
        run_as_user_type=str(run_as_user.get("")),
    )


def x__to_scc__mutmut_38(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(item)
    run_as_user = _mapping(item, "runAsUser")
    return SecurityContextConstraintInfo(
        name=str(meta.get("name", "")),
        allow_privileged_container=bool(item.get("allowPrivilegedContainer", False)),
        run_as_user_type=str(run_as_user.get("type", )),
    )


def x__to_scc__mutmut_39(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(item)
    run_as_user = _mapping(item, "runAsUser")
    return SecurityContextConstraintInfo(
        name=str(meta.get("name", "")),
        allow_privileged_container=bool(item.get("allowPrivilegedContainer", False)),
        run_as_user_type=str(run_as_user.get("XXtypeXX", "")),
    )


def x__to_scc__mutmut_40(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(item)
    run_as_user = _mapping(item, "runAsUser")
    return SecurityContextConstraintInfo(
        name=str(meta.get("name", "")),
        allow_privileged_container=bool(item.get("allowPrivilegedContainer", False)),
        run_as_user_type=str(run_as_user.get("TYPE", "")),
    )


def x__to_scc__mutmut_41(item: Mapping[str, object]) -> SecurityContextConstraintInfo:
    meta = _metadata(item)
    run_as_user = _mapping(item, "runAsUser")
    return SecurityContextConstraintInfo(
        name=str(meta.get("name", "")),
        allow_privileged_container=bool(item.get("allowPrivilegedContainer", False)),
        run_as_user_type=str(run_as_user.get("type", "XXXX")),
    )

mutants_x__to_scc__mutmut['_mutmut_orig'] = x__to_scc__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_scc__mutmut['x__to_scc__mutmut_1'] = x__to_scc__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_scc__mutmut['x__to_scc__mutmut_2'] = x__to_scc__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_scc__mutmut['x__to_scc__mutmut_3'] = x__to_scc__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_scc__mutmut['x__to_scc__mutmut_4'] = x__to_scc__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_scc__mutmut['x__to_scc__mutmut_5'] = x__to_scc__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_scc__mutmut['x__to_scc__mutmut_6'] = x__to_scc__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_scc__mutmut['x__to_scc__mutmut_7'] = x__to_scc__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_scc__mutmut['x__to_scc__mutmut_8'] = x__to_scc__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_scc__mutmut['x__to_scc__mutmut_9'] = x__to_scc__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_scc__mutmut['x__to_scc__mutmut_10'] = x__to_scc__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_scc__mutmut['x__to_scc__mutmut_11'] = x__to_scc__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_scc__mutmut['x__to_scc__mutmut_12'] = x__to_scc__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_scc__mutmut['x__to_scc__mutmut_13'] = x__to_scc__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_scc__mutmut['x__to_scc__mutmut_14'] = x__to_scc__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_scc__mutmut['x__to_scc__mutmut_15'] = x__to_scc__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_scc__mutmut['x__to_scc__mutmut_16'] = x__to_scc__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_scc__mutmut['x__to_scc__mutmut_17'] = x__to_scc__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_scc__mutmut['x__to_scc__mutmut_18'] = x__to_scc__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_scc__mutmut['x__to_scc__mutmut_19'] = x__to_scc__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_scc__mutmut['x__to_scc__mutmut_20'] = x__to_scc__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_scc__mutmut['x__to_scc__mutmut_21'] = x__to_scc__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_scc__mutmut['x__to_scc__mutmut_22'] = x__to_scc__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_scc__mutmut['x__to_scc__mutmut_23'] = x__to_scc__mutmut_23 # type: ignore # mutmut generated
mutants_x__to_scc__mutmut['x__to_scc__mutmut_24'] = x__to_scc__mutmut_24 # type: ignore # mutmut generated
mutants_x__to_scc__mutmut['x__to_scc__mutmut_25'] = x__to_scc__mutmut_25 # type: ignore # mutmut generated
mutants_x__to_scc__mutmut['x__to_scc__mutmut_26'] = x__to_scc__mutmut_26 # type: ignore # mutmut generated
mutants_x__to_scc__mutmut['x__to_scc__mutmut_27'] = x__to_scc__mutmut_27 # type: ignore # mutmut generated
mutants_x__to_scc__mutmut['x__to_scc__mutmut_28'] = x__to_scc__mutmut_28 # type: ignore # mutmut generated
mutants_x__to_scc__mutmut['x__to_scc__mutmut_29'] = x__to_scc__mutmut_29 # type: ignore # mutmut generated
mutants_x__to_scc__mutmut['x__to_scc__mutmut_30'] = x__to_scc__mutmut_30 # type: ignore # mutmut generated
mutants_x__to_scc__mutmut['x__to_scc__mutmut_31'] = x__to_scc__mutmut_31 # type: ignore # mutmut generated
mutants_x__to_scc__mutmut['x__to_scc__mutmut_32'] = x__to_scc__mutmut_32 # type: ignore # mutmut generated
mutants_x__to_scc__mutmut['x__to_scc__mutmut_33'] = x__to_scc__mutmut_33 # type: ignore # mutmut generated
mutants_x__to_scc__mutmut['x__to_scc__mutmut_34'] = x__to_scc__mutmut_34 # type: ignore # mutmut generated
mutants_x__to_scc__mutmut['x__to_scc__mutmut_35'] = x__to_scc__mutmut_35 # type: ignore # mutmut generated
mutants_x__to_scc__mutmut['x__to_scc__mutmut_36'] = x__to_scc__mutmut_36 # type: ignore # mutmut generated
mutants_x__to_scc__mutmut['x__to_scc__mutmut_37'] = x__to_scc__mutmut_37 # type: ignore # mutmut generated
mutants_x__to_scc__mutmut['x__to_scc__mutmut_38'] = x__to_scc__mutmut_38 # type: ignore # mutmut generated
mutants_x__to_scc__mutmut['x__to_scc__mutmut_39'] = x__to_scc__mutmut_39 # type: ignore # mutmut generated
mutants_x__to_scc__mutmut['x__to_scc__mutmut_40'] = x__to_scc__mutmut_40 # type: ignore # mutmut generated
mutants_x__to_scc__mutmut['x__to_scc__mutmut_41'] = x__to_scc__mutmut_41 # type: ignore # mutmut generated
mutants_x__to_image_stream__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_image_stream__mutmut)
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


def x__to_image_stream__mutmut_orig(item: Mapping[str, object]) -> ImageStreamInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    tags = status.get("tags")
    tag_count = len(tags) if isinstance(tags, list) else 0
    return ImageStreamInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        tag_count=tag_count,
    )


def x__to_image_stream__mutmut_1(item: Mapping[str, object]) -> ImageStreamInfo:
    meta = None
    status = _mapping(item, "status")
    tags = status.get("tags")
    tag_count = len(tags) if isinstance(tags, list) else 0
    return ImageStreamInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        tag_count=tag_count,
    )


def x__to_image_stream__mutmut_2(item: Mapping[str, object]) -> ImageStreamInfo:
    meta = _metadata(None)
    status = _mapping(item, "status")
    tags = status.get("tags")
    tag_count = len(tags) if isinstance(tags, list) else 0
    return ImageStreamInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        tag_count=tag_count,
    )


def x__to_image_stream__mutmut_3(item: Mapping[str, object]) -> ImageStreamInfo:
    meta = _metadata(item)
    status = None
    tags = status.get("tags")
    tag_count = len(tags) if isinstance(tags, list) else 0
    return ImageStreamInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        tag_count=tag_count,
    )


def x__to_image_stream__mutmut_4(item: Mapping[str, object]) -> ImageStreamInfo:
    meta = _metadata(item)
    status = _mapping(None, "status")
    tags = status.get("tags")
    tag_count = len(tags) if isinstance(tags, list) else 0
    return ImageStreamInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        tag_count=tag_count,
    )


def x__to_image_stream__mutmut_5(item: Mapping[str, object]) -> ImageStreamInfo:
    meta = _metadata(item)
    status = _mapping(item, None)
    tags = status.get("tags")
    tag_count = len(tags) if isinstance(tags, list) else 0
    return ImageStreamInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        tag_count=tag_count,
    )


def x__to_image_stream__mutmut_6(item: Mapping[str, object]) -> ImageStreamInfo:
    meta = _metadata(item)
    status = _mapping("status")
    tags = status.get("tags")
    tag_count = len(tags) if isinstance(tags, list) else 0
    return ImageStreamInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        tag_count=tag_count,
    )


def x__to_image_stream__mutmut_7(item: Mapping[str, object]) -> ImageStreamInfo:
    meta = _metadata(item)
    status = _mapping(item, )
    tags = status.get("tags")
    tag_count = len(tags) if isinstance(tags, list) else 0
    return ImageStreamInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        tag_count=tag_count,
    )


def x__to_image_stream__mutmut_8(item: Mapping[str, object]) -> ImageStreamInfo:
    meta = _metadata(item)
    status = _mapping(item, "XXstatusXX")
    tags = status.get("tags")
    tag_count = len(tags) if isinstance(tags, list) else 0
    return ImageStreamInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        tag_count=tag_count,
    )


def x__to_image_stream__mutmut_9(item: Mapping[str, object]) -> ImageStreamInfo:
    meta = _metadata(item)
    status = _mapping(item, "STATUS")
    tags = status.get("tags")
    tag_count = len(tags) if isinstance(tags, list) else 0
    return ImageStreamInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        tag_count=tag_count,
    )


def x__to_image_stream__mutmut_10(item: Mapping[str, object]) -> ImageStreamInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    tags = None
    tag_count = len(tags) if isinstance(tags, list) else 0
    return ImageStreamInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        tag_count=tag_count,
    )


def x__to_image_stream__mutmut_11(item: Mapping[str, object]) -> ImageStreamInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    tags = status.get(None)
    tag_count = len(tags) if isinstance(tags, list) else 0
    return ImageStreamInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        tag_count=tag_count,
    )


def x__to_image_stream__mutmut_12(item: Mapping[str, object]) -> ImageStreamInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    tags = status.get("XXtagsXX")
    tag_count = len(tags) if isinstance(tags, list) else 0
    return ImageStreamInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        tag_count=tag_count,
    )


def x__to_image_stream__mutmut_13(item: Mapping[str, object]) -> ImageStreamInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    tags = status.get("TAGS")
    tag_count = len(tags) if isinstance(tags, list) else 0
    return ImageStreamInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        tag_count=tag_count,
    )


def x__to_image_stream__mutmut_14(item: Mapping[str, object]) -> ImageStreamInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    tags = status.get("tags")
    tag_count = None
    return ImageStreamInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        tag_count=tag_count,
    )


def x__to_image_stream__mutmut_15(item: Mapping[str, object]) -> ImageStreamInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    tags = status.get("tags")
    tag_count = len(tags) if isinstance(tags, list) else 1
    return ImageStreamInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        tag_count=tag_count,
    )


def x__to_image_stream__mutmut_16(item: Mapping[str, object]) -> ImageStreamInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    tags = status.get("tags")
    tag_count = len(tags) if isinstance(tags, list) else 0
    return ImageStreamInfo(
        name=None,
        namespace=str(meta.get("namespace", "")),
        tag_count=tag_count,
    )


def x__to_image_stream__mutmut_17(item: Mapping[str, object]) -> ImageStreamInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    tags = status.get("tags")
    tag_count = len(tags) if isinstance(tags, list) else 0
    return ImageStreamInfo(
        name=str(meta.get("name", "")),
        namespace=None,
        tag_count=tag_count,
    )


def x__to_image_stream__mutmut_18(item: Mapping[str, object]) -> ImageStreamInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    tags = status.get("tags")
    tag_count = len(tags) if isinstance(tags, list) else 0
    return ImageStreamInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        tag_count=None,
    )


def x__to_image_stream__mutmut_19(item: Mapping[str, object]) -> ImageStreamInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    tags = status.get("tags")
    tag_count = len(tags) if isinstance(tags, list) else 0
    return ImageStreamInfo(
        namespace=str(meta.get("namespace", "")),
        tag_count=tag_count,
    )


def x__to_image_stream__mutmut_20(item: Mapping[str, object]) -> ImageStreamInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    tags = status.get("tags")
    tag_count = len(tags) if isinstance(tags, list) else 0
    return ImageStreamInfo(
        name=str(meta.get("name", "")),
        tag_count=tag_count,
    )


def x__to_image_stream__mutmut_21(item: Mapping[str, object]) -> ImageStreamInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    tags = status.get("tags")
    tag_count = len(tags) if isinstance(tags, list) else 0
    return ImageStreamInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        )


def x__to_image_stream__mutmut_22(item: Mapping[str, object]) -> ImageStreamInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    tags = status.get("tags")
    tag_count = len(tags) if isinstance(tags, list) else 0
    return ImageStreamInfo(
        name=str(None),
        namespace=str(meta.get("namespace", "")),
        tag_count=tag_count,
    )


def x__to_image_stream__mutmut_23(item: Mapping[str, object]) -> ImageStreamInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    tags = status.get("tags")
    tag_count = len(tags) if isinstance(tags, list) else 0
    return ImageStreamInfo(
        name=str(meta.get(None, "")),
        namespace=str(meta.get("namespace", "")),
        tag_count=tag_count,
    )


def x__to_image_stream__mutmut_24(item: Mapping[str, object]) -> ImageStreamInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    tags = status.get("tags")
    tag_count = len(tags) if isinstance(tags, list) else 0
    return ImageStreamInfo(
        name=str(meta.get("name", None)),
        namespace=str(meta.get("namespace", "")),
        tag_count=tag_count,
    )


def x__to_image_stream__mutmut_25(item: Mapping[str, object]) -> ImageStreamInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    tags = status.get("tags")
    tag_count = len(tags) if isinstance(tags, list) else 0
    return ImageStreamInfo(
        name=str(meta.get("")),
        namespace=str(meta.get("namespace", "")),
        tag_count=tag_count,
    )


def x__to_image_stream__mutmut_26(item: Mapping[str, object]) -> ImageStreamInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    tags = status.get("tags")
    tag_count = len(tags) if isinstance(tags, list) else 0
    return ImageStreamInfo(
        name=str(meta.get("name", )),
        namespace=str(meta.get("namespace", "")),
        tag_count=tag_count,
    )


def x__to_image_stream__mutmut_27(item: Mapping[str, object]) -> ImageStreamInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    tags = status.get("tags")
    tag_count = len(tags) if isinstance(tags, list) else 0
    return ImageStreamInfo(
        name=str(meta.get("XXnameXX", "")),
        namespace=str(meta.get("namespace", "")),
        tag_count=tag_count,
    )


def x__to_image_stream__mutmut_28(item: Mapping[str, object]) -> ImageStreamInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    tags = status.get("tags")
    tag_count = len(tags) if isinstance(tags, list) else 0
    return ImageStreamInfo(
        name=str(meta.get("NAME", "")),
        namespace=str(meta.get("namespace", "")),
        tag_count=tag_count,
    )


def x__to_image_stream__mutmut_29(item: Mapping[str, object]) -> ImageStreamInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    tags = status.get("tags")
    tag_count = len(tags) if isinstance(tags, list) else 0
    return ImageStreamInfo(
        name=str(meta.get("name", "XXXX")),
        namespace=str(meta.get("namespace", "")),
        tag_count=tag_count,
    )


def x__to_image_stream__mutmut_30(item: Mapping[str, object]) -> ImageStreamInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    tags = status.get("tags")
    tag_count = len(tags) if isinstance(tags, list) else 0
    return ImageStreamInfo(
        name=str(meta.get("name", "")),
        namespace=str(None),
        tag_count=tag_count,
    )


def x__to_image_stream__mutmut_31(item: Mapping[str, object]) -> ImageStreamInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    tags = status.get("tags")
    tag_count = len(tags) if isinstance(tags, list) else 0
    return ImageStreamInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get(None, "")),
        tag_count=tag_count,
    )


def x__to_image_stream__mutmut_32(item: Mapping[str, object]) -> ImageStreamInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    tags = status.get("tags")
    tag_count = len(tags) if isinstance(tags, list) else 0
    return ImageStreamInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", None)),
        tag_count=tag_count,
    )


def x__to_image_stream__mutmut_33(item: Mapping[str, object]) -> ImageStreamInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    tags = status.get("tags")
    tag_count = len(tags) if isinstance(tags, list) else 0
    return ImageStreamInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("")),
        tag_count=tag_count,
    )


def x__to_image_stream__mutmut_34(item: Mapping[str, object]) -> ImageStreamInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    tags = status.get("tags")
    tag_count = len(tags) if isinstance(tags, list) else 0
    return ImageStreamInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", )),
        tag_count=tag_count,
    )


def x__to_image_stream__mutmut_35(item: Mapping[str, object]) -> ImageStreamInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    tags = status.get("tags")
    tag_count = len(tags) if isinstance(tags, list) else 0
    return ImageStreamInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("XXnamespaceXX", "")),
        tag_count=tag_count,
    )


def x__to_image_stream__mutmut_36(item: Mapping[str, object]) -> ImageStreamInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    tags = status.get("tags")
    tag_count = len(tags) if isinstance(tags, list) else 0
    return ImageStreamInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("NAMESPACE", "")),
        tag_count=tag_count,
    )


def x__to_image_stream__mutmut_37(item: Mapping[str, object]) -> ImageStreamInfo:
    meta = _metadata(item)
    status = _mapping(item, "status")
    tags = status.get("tags")
    tag_count = len(tags) if isinstance(tags, list) else 0
    return ImageStreamInfo(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "XXXX")),
        tag_count=tag_count,
    )

mutants_x__to_image_stream__mutmut['_mutmut_orig'] = x__to_image_stream__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_image_stream__mutmut['x__to_image_stream__mutmut_1'] = x__to_image_stream__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_image_stream__mutmut['x__to_image_stream__mutmut_2'] = x__to_image_stream__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_image_stream__mutmut['x__to_image_stream__mutmut_3'] = x__to_image_stream__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_image_stream__mutmut['x__to_image_stream__mutmut_4'] = x__to_image_stream__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_image_stream__mutmut['x__to_image_stream__mutmut_5'] = x__to_image_stream__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_image_stream__mutmut['x__to_image_stream__mutmut_6'] = x__to_image_stream__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_image_stream__mutmut['x__to_image_stream__mutmut_7'] = x__to_image_stream__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_image_stream__mutmut['x__to_image_stream__mutmut_8'] = x__to_image_stream__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_image_stream__mutmut['x__to_image_stream__mutmut_9'] = x__to_image_stream__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_image_stream__mutmut['x__to_image_stream__mutmut_10'] = x__to_image_stream__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_image_stream__mutmut['x__to_image_stream__mutmut_11'] = x__to_image_stream__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_image_stream__mutmut['x__to_image_stream__mutmut_12'] = x__to_image_stream__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_image_stream__mutmut['x__to_image_stream__mutmut_13'] = x__to_image_stream__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_image_stream__mutmut['x__to_image_stream__mutmut_14'] = x__to_image_stream__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_image_stream__mutmut['x__to_image_stream__mutmut_15'] = x__to_image_stream__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_image_stream__mutmut['x__to_image_stream__mutmut_16'] = x__to_image_stream__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_image_stream__mutmut['x__to_image_stream__mutmut_17'] = x__to_image_stream__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_image_stream__mutmut['x__to_image_stream__mutmut_18'] = x__to_image_stream__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_image_stream__mutmut['x__to_image_stream__mutmut_19'] = x__to_image_stream__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_image_stream__mutmut['x__to_image_stream__mutmut_20'] = x__to_image_stream__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_image_stream__mutmut['x__to_image_stream__mutmut_21'] = x__to_image_stream__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_image_stream__mutmut['x__to_image_stream__mutmut_22'] = x__to_image_stream__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_image_stream__mutmut['x__to_image_stream__mutmut_23'] = x__to_image_stream__mutmut_23 # type: ignore # mutmut generated
mutants_x__to_image_stream__mutmut['x__to_image_stream__mutmut_24'] = x__to_image_stream__mutmut_24 # type: ignore # mutmut generated
mutants_x__to_image_stream__mutmut['x__to_image_stream__mutmut_25'] = x__to_image_stream__mutmut_25 # type: ignore # mutmut generated
mutants_x__to_image_stream__mutmut['x__to_image_stream__mutmut_26'] = x__to_image_stream__mutmut_26 # type: ignore # mutmut generated
mutants_x__to_image_stream__mutmut['x__to_image_stream__mutmut_27'] = x__to_image_stream__mutmut_27 # type: ignore # mutmut generated
mutants_x__to_image_stream__mutmut['x__to_image_stream__mutmut_28'] = x__to_image_stream__mutmut_28 # type: ignore # mutmut generated
mutants_x__to_image_stream__mutmut['x__to_image_stream__mutmut_29'] = x__to_image_stream__mutmut_29 # type: ignore # mutmut generated
mutants_x__to_image_stream__mutmut['x__to_image_stream__mutmut_30'] = x__to_image_stream__mutmut_30 # type: ignore # mutmut generated
mutants_x__to_image_stream__mutmut['x__to_image_stream__mutmut_31'] = x__to_image_stream__mutmut_31 # type: ignore # mutmut generated
mutants_x__to_image_stream__mutmut['x__to_image_stream__mutmut_32'] = x__to_image_stream__mutmut_32 # type: ignore # mutmut generated
mutants_x__to_image_stream__mutmut['x__to_image_stream__mutmut_33'] = x__to_image_stream__mutmut_33 # type: ignore # mutmut generated
mutants_x__to_image_stream__mutmut['x__to_image_stream__mutmut_34'] = x__to_image_stream__mutmut_34 # type: ignore # mutmut generated
mutants_x__to_image_stream__mutmut['x__to_image_stream__mutmut_35'] = x__to_image_stream__mutmut_35 # type: ignore # mutmut generated
mutants_x__to_image_stream__mutmut['x__to_image_stream__mutmut_36'] = x__to_image_stream__mutmut_36 # type: ignore # mutmut generated
mutants_x__to_image_stream__mutmut['x__to_image_stream__mutmut_37'] = x__to_image_stream__mutmut_37 # type: ignore # mutmut generated
