"""IstioTopologyAdapter — infers edges from Istio VirtualService CRDs (best-effort)."""

from __future__ import annotations

from typing import Protocol, cast

from hexawyn.application.ports.driven.istio_topology_port import IstioTopologyPort
from hexawyn.application.ports.driven.kubernetes_topology_port import EdgeRecordData

_ISTIO_GROUP = "networking.istio.io"
_ISTIO_VERSION = "v1beta1"
_VIRTUAL_SERVICES_PLURAL = "virtualservices"


class _CustomObjectsApi(Protocol):
    def list_cluster_custom_object(self, group: str, version: str, plural: str) -> object:
        """List cluster-scoped custom objects."""

    def list_namespaced_custom_object(
        self, group: str, version: str, namespace: str, plural: str
    ) -> object:
        """List namespace-scoped custom objects."""


class IstioTopologyAdapter(IstioTopologyPort):
    def __init__(self, crd_api: _CustomObjectsApi | None = None) -> None:
        self._crd_api = crd_api

    # ── IstioTopologyPort ─────────────────────────────────────

    def get_virtual_service_edges(self, namespace: str | None) -> list[EdgeRecordData] | None:
        try:
            raw = self._fetch_virtual_services(namespace)
        except Exception:
            return None
        return _build_edges_from_virtual_services(_items(raw))

    # ── Internal ───────────────────────────────────────────────

    def _fetch_virtual_services(self, namespace: str | None) -> object:
        api = self._crd_api_client()
        if namespace:
            return api.list_namespaced_custom_object(
                group=_ISTIO_GROUP,
                version=_ISTIO_VERSION,
                namespace=namespace,
                plural=_VIRTUAL_SERVICES_PLURAL,
            )
        return api.list_cluster_custom_object(
            group=_ISTIO_GROUP,
            version=_ISTIO_VERSION,
            plural=_VIRTUAL_SERVICES_PLURAL,
        )

    def _crd_api_client(self) -> _CustomObjectsApi:
        if self._crd_api is None:
            from kubernetes import client

            self._crd_api = cast(_CustomObjectsApi, client.CustomObjectsApi())
        return self._crd_api


def _items(raw: object) -> list[dict[str, object]]:
    if not isinstance(raw, dict):
        return []
    items = raw.get("items", [])
    if not isinstance(items, list):
        return []
    return [item for item in items if isinstance(item, dict)]


def _build_edges_from_virtual_services(
    virtual_services: list[dict[str, object]],
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for virtual_service in virtual_services:
        callee = _primary_host(virtual_service)
        if callee is None:
            continue
        for caller in _source_apps(virtual_service):
            if caller == callee or (caller, callee) in seen:
                continue
            seen.add((caller, callee))
            edges.append(EdgeRecordData(caller=caller, callee=callee))

    return edges


def _primary_host(virtual_service: dict[str, object]) -> str | None:
    spec = virtual_service.get("spec")
    if not isinstance(spec, dict):
        return None
    hosts = spec.get("hosts")
    if not isinstance(hosts, list) or not hosts:
        return None
    return str(hosts[0]).split(".")[0]


def _source_apps(virtual_service: dict[str, object]) -> list[str]:
    spec = virtual_service.get("spec")
    if not isinstance(spec, dict):
        return []
    http_rules = spec.get("http")
    if not isinstance(http_rules, list):
        return []

    apps: list[str] = []
    for rule in http_rules:
        if not isinstance(rule, dict):
            continue
        for match in rule.get("match", []) or []:
            if not isinstance(match, dict):
                continue
            source_labels = match.get("sourceLabels")
            if isinstance(source_labels, dict):
                app = source_labels.get("app")
                if app:
                    apps.append(str(app))
    return apps
