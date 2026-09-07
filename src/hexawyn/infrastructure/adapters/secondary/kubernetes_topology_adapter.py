"""KubernetesTopologyAdapter — discovers Services and infers edges from NetworkPolicies."""

from __future__ import annotations

from typing import NamedTuple, Protocol, cast

from hexawyn.application.ports.driven.kubernetes_topology_port import (
    EdgeRecordData,
    KubernetesTopologyPort,
    ServiceRecordData,
)
from hexawyn.infrastructure.config.kubeconfig_reader import load_kubeconfig

_K8S_TIMEOUT = 5
_EXTERNAL_NAME_TYPE = "ExternalName"


class _CoreServiceApi(Protocol):
    def list_service_for_all_namespaces(self, timeout_seconds: int) -> object:
        """List services across all namespaces."""

    def list_namespaced_service(self, namespace: str, timeout_seconds: int) -> object:
        """List services in a namespace."""


class _AppsApi(Protocol):
    def list_deployment_for_all_namespaces(self, timeout_seconds: int) -> object:
        """List deployments across all namespaces."""

    def list_namespaced_deployment(self, namespace: str, timeout_seconds: int) -> object:
        """List deployments in a namespace."""


class _NetworkingApi(Protocol):
    def list_network_policy_for_all_namespaces(self, timeout_seconds: int) -> object:
        """List NetworkPolicies across all namespaces."""

    def list_namespaced_network_policy(self, namespace: str, timeout_seconds: int) -> object:
        """List NetworkPolicies in a namespace."""


class _ServiceSelector(NamedTuple):
    name: str
    namespace: str
    app_label: str | None


class KubernetesTopologyAdapter(KubernetesTopologyPort):
    def __init__(
        self,
        cluster_name: str,
        core_api: _CoreServiceApi | None = None,
        apps_api: _AppsApi | None = None,
        networking_api: _NetworkingApi | None = None,
    ) -> None:
        self._cluster_name = cluster_name
        self._core_api = core_api
        self._apps_api = apps_api
        self._networking_api = networking_api

    # ── KubernetesTopologyPort ────────────────────────────────

    def list_services(self, namespace: str | None) -> list[ServiceRecordData]:
        try:
            raw_services = self._fetch_raw_services(namespace)
        except Exception:
            return []
        replica_by_name = self._replica_counts_by_name(namespace)
        return [self._to_service_record(svc, replica_by_name) for svc in _items(raw_services)]

    def get_network_policy_edges(self, namespace: str | None) -> list[EdgeRecordData]:
        try:
            raw_services = self._fetch_raw_services(namespace)
            raw_policies = self._fetch_raw_network_policies(namespace)
        except Exception:
            return []
        selectors = [_to_service_selector(svc) for svc in _items(raw_services)]
        return _build_edges_from_policies(_items(raw_policies), selectors)

    # ── Internal ───────────────────────────────────────────────

    def _fetch_raw_services(self, namespace: str | None) -> object:
        api = self._core_api_client()
        if namespace:
            return api.list_namespaced_service(namespace, timeout_seconds=_K8S_TIMEOUT)
        return api.list_service_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)

    def _fetch_raw_network_policies(self, namespace: str | None) -> object:
        api = self._networking_api_client()
        if namespace:
            return api.list_namespaced_network_policy(namespace, timeout_seconds=_K8S_TIMEOUT)
        return api.list_network_policy_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)

    def _replica_counts_by_name(self, namespace: str | None) -> dict[str, int]:
        try:
            api = self._apps_api_client()
            raw = (
                api.list_namespaced_deployment(namespace, timeout_seconds=_K8S_TIMEOUT)
                if namespace
                else api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
            )
        except Exception:
            return {}
        counts: dict[str, int] = {}
        for dep in _items(raw):
            name = str(getattr(getattr(dep, "metadata", None), "name", ""))
            spec = getattr(dep, "spec", None)
            counts[name] = int(getattr(spec, "replicas", 0) or 0)
        return counts

    def _to_service_record(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def _core_api_client(self) -> _CoreServiceApi:
        if self._core_api is None:
            self._core_api = cast(_CoreServiceApi, load_kubeconfig(context=self._context_name()))
        return self._core_api

    def _apps_api_client(self) -> _AppsApi:
        if self._apps_api is None:
            from kubernetes import client

            core_api = cast(client.CoreV1Api, self._core_api_client())
            self._apps_api = cast(_AppsApi, client.AppsV1Api(api_client=core_api.api_client))
        return self._apps_api

    def _networking_api_client(self) -> _NetworkingApi:
        if self._networking_api is None:
            from kubernetes import client

            core_api = cast(client.CoreV1Api, self._core_api_client())
            self._networking_api = cast(
                _NetworkingApi, client.NetworkingV1Api(api_client=core_api.api_client)
            )
        return self._networking_api

    def _context_name(self) -> str | None:
        return None if self._cluster_name == "unknown" else self._cluster_name


def _items(api_response: object) -> list[object]:
    return list(getattr(api_response, "items", None) or [])


def _to_service_selector(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def _build_edges_from_policies(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = str(getattr(metadata, "namespace", "default"))
        spec = getattr(policy, "spec", None)
        callees = _match_services(getattr(spec, "pod_selector", None), policy_namespace, selectors)

        for ingress in getattr(spec, "ingress", None) or []:
            for peer in getattr(ingress, "_from", None) or []:
                callers = _match_services(
                    getattr(peer, "pod_selector", None), policy_namespace, selectors
                )
                for caller in callers:
                    for callee in callees:
                        if caller == callee or (caller, callee) in seen:
                            continue
                        seen.add((caller, callee))
                        edges.append(EdgeRecordData(caller=caller, callee=callee))

    return edges


def _match_services(
    pod_selector: object, namespace: str, selectors: list[_ServiceSelector]
) -> list[str]:
    match_labels = getattr(pod_selector, "match_labels", None) or {}
    app_label = match_labels.get("app") if isinstance(match_labels, dict) else None
    if not app_label:
        return []
    return [s.name for s in selectors if s.namespace == namespace and s.app_label == app_label]
