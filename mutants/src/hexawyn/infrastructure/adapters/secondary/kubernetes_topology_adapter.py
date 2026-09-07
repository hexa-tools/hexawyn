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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


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
mutants_xǁKubernetesTopologyAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁKubernetesTopologyAdapterǁlist_services__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKubernetesTopologyAdapterǁ_fetch_raw_services__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKubernetesTopologyAdapterǁ_fetch_raw_network_policies__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKubernetesTopologyAdapterǁ_core_api_client__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKubernetesTopologyAdapterǁ_context_name__mutmut: MutantDict = {}  # type: ignore


class KubernetesTopologyAdapter(KubernetesTopologyPort):
    @_mutmut_mutated(mutants_xǁKubernetesTopologyAdapterǁ__init____mutmut)
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
    def xǁKubernetesTopologyAdapterǁ__init____mutmut_orig(
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
    def xǁKubernetesTopologyAdapterǁ__init____mutmut_1(
        self,
        cluster_name: str,
        core_api: _CoreServiceApi | None = None,
        apps_api: _AppsApi | None = None,
        networking_api: _NetworkingApi | None = None,
    ) -> None:
        self._cluster_name = None
        self._core_api = core_api
        self._apps_api = apps_api
        self._networking_api = networking_api
    def xǁKubernetesTopologyAdapterǁ__init____mutmut_2(
        self,
        cluster_name: str,
        core_api: _CoreServiceApi | None = None,
        apps_api: _AppsApi | None = None,
        networking_api: _NetworkingApi | None = None,
    ) -> None:
        self._cluster_name = cluster_name
        self._core_api = None
        self._apps_api = apps_api
        self._networking_api = networking_api
    def xǁKubernetesTopologyAdapterǁ__init____mutmut_3(
        self,
        cluster_name: str,
        core_api: _CoreServiceApi | None = None,
        apps_api: _AppsApi | None = None,
        networking_api: _NetworkingApi | None = None,
    ) -> None:
        self._cluster_name = cluster_name
        self._core_api = core_api
        self._apps_api = None
        self._networking_api = networking_api
    def xǁKubernetesTopologyAdapterǁ__init____mutmut_4(
        self,
        cluster_name: str,
        core_api: _CoreServiceApi | None = None,
        apps_api: _AppsApi | None = None,
        networking_api: _NetworkingApi | None = None,
    ) -> None:
        self._cluster_name = cluster_name
        self._core_api = core_api
        self._apps_api = apps_api
        self._networking_api = None

    # ── KubernetesTopologyPort ────────────────────────────────

    @_mutmut_mutated(mutants_xǁKubernetesTopologyAdapterǁlist_services__mutmut)
    def list_services(self, namespace: str | None) -> list[ServiceRecordData]:
        try:
            raw_services = self._fetch_raw_services(namespace)
        except Exception:
            return []
        replica_by_name = self._replica_counts_by_name(namespace)
        return [self._to_service_record(svc, replica_by_name) for svc in _items(raw_services)]

    # ── KubernetesTopologyPort ────────────────────────────────

    def xǁKubernetesTopologyAdapterǁlist_services__mutmut_orig(self, namespace: str | None) -> list[ServiceRecordData]:
        try:
            raw_services = self._fetch_raw_services(namespace)
        except Exception:
            return []
        replica_by_name = self._replica_counts_by_name(namespace)
        return [self._to_service_record(svc, replica_by_name) for svc in _items(raw_services)]

    # ── KubernetesTopologyPort ────────────────────────────────

    def xǁKubernetesTopologyAdapterǁlist_services__mutmut_1(self, namespace: str | None) -> list[ServiceRecordData]:
        try:
            raw_services = None
        except Exception:
            return []
        replica_by_name = self._replica_counts_by_name(namespace)
        return [self._to_service_record(svc, replica_by_name) for svc in _items(raw_services)]

    # ── KubernetesTopologyPort ────────────────────────────────

    def xǁKubernetesTopologyAdapterǁlist_services__mutmut_2(self, namespace: str | None) -> list[ServiceRecordData]:
        try:
            raw_services = self._fetch_raw_services(None)
        except Exception:
            return []
        replica_by_name = self._replica_counts_by_name(namespace)
        return [self._to_service_record(svc, replica_by_name) for svc in _items(raw_services)]

    # ── KubernetesTopologyPort ────────────────────────────────

    def xǁKubernetesTopologyAdapterǁlist_services__mutmut_3(self, namespace: str | None) -> list[ServiceRecordData]:
        try:
            raw_services = self._fetch_raw_services(namespace)
        except Exception:
            return []
        replica_by_name = None
        return [self._to_service_record(svc, replica_by_name) for svc in _items(raw_services)]

    # ── KubernetesTopologyPort ────────────────────────────────

    def xǁKubernetesTopologyAdapterǁlist_services__mutmut_4(self, namespace: str | None) -> list[ServiceRecordData]:
        try:
            raw_services = self._fetch_raw_services(namespace)
        except Exception:
            return []
        replica_by_name = self._replica_counts_by_name(None)
        return [self._to_service_record(svc, replica_by_name) for svc in _items(raw_services)]

    # ── KubernetesTopologyPort ────────────────────────────────

    def xǁKubernetesTopologyAdapterǁlist_services__mutmut_5(self, namespace: str | None) -> list[ServiceRecordData]:
        try:
            raw_services = self._fetch_raw_services(namespace)
        except Exception:
            return []
        replica_by_name = self._replica_counts_by_name(namespace)
        return [self._to_service_record(None, replica_by_name) for svc in _items(raw_services)]

    # ── KubernetesTopologyPort ────────────────────────────────

    def xǁKubernetesTopologyAdapterǁlist_services__mutmut_6(self, namespace: str | None) -> list[ServiceRecordData]:
        try:
            raw_services = self._fetch_raw_services(namespace)
        except Exception:
            return []
        replica_by_name = self._replica_counts_by_name(namespace)
        return [self._to_service_record(svc, None) for svc in _items(raw_services)]

    # ── KubernetesTopologyPort ────────────────────────────────

    def xǁKubernetesTopologyAdapterǁlist_services__mutmut_7(self, namespace: str | None) -> list[ServiceRecordData]:
        try:
            raw_services = self._fetch_raw_services(namespace)
        except Exception:
            return []
        replica_by_name = self._replica_counts_by_name(namespace)
        return [self._to_service_record(replica_by_name) for svc in _items(raw_services)]

    # ── KubernetesTopologyPort ────────────────────────────────

    def xǁKubernetesTopologyAdapterǁlist_services__mutmut_8(self, namespace: str | None) -> list[ServiceRecordData]:
        try:
            raw_services = self._fetch_raw_services(namespace)
        except Exception:
            return []
        replica_by_name = self._replica_counts_by_name(namespace)
        return [self._to_service_record(svc, ) for svc in _items(raw_services)]

    # ── KubernetesTopologyPort ────────────────────────────────

    def xǁKubernetesTopologyAdapterǁlist_services__mutmut_9(self, namespace: str | None) -> list[ServiceRecordData]:
        try:
            raw_services = self._fetch_raw_services(namespace)
        except Exception:
            return []
        replica_by_name = self._replica_counts_by_name(namespace)
        return [self._to_service_record(svc, replica_by_name) for svc in _items(None)]

    @_mutmut_mutated(mutants_xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut)
    def get_network_policy_edges(self, namespace: str | None) -> list[EdgeRecordData]:
        try:
            raw_services = self._fetch_raw_services(namespace)
            raw_policies = self._fetch_raw_network_policies(namespace)
        except Exception:
            return []
        selectors = [_to_service_selector(svc) for svc in _items(raw_services)]
        return _build_edges_from_policies(_items(raw_policies), selectors)

    def xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut_orig(self, namespace: str | None) -> list[EdgeRecordData]:
        try:
            raw_services = self._fetch_raw_services(namespace)
            raw_policies = self._fetch_raw_network_policies(namespace)
        except Exception:
            return []
        selectors = [_to_service_selector(svc) for svc in _items(raw_services)]
        return _build_edges_from_policies(_items(raw_policies), selectors)

    def xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut_1(self, namespace: str | None) -> list[EdgeRecordData]:
        try:
            raw_services = None
            raw_policies = self._fetch_raw_network_policies(namespace)
        except Exception:
            return []
        selectors = [_to_service_selector(svc) for svc in _items(raw_services)]
        return _build_edges_from_policies(_items(raw_policies), selectors)

    def xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut_2(self, namespace: str | None) -> list[EdgeRecordData]:
        try:
            raw_services = self._fetch_raw_services(None)
            raw_policies = self._fetch_raw_network_policies(namespace)
        except Exception:
            return []
        selectors = [_to_service_selector(svc) for svc in _items(raw_services)]
        return _build_edges_from_policies(_items(raw_policies), selectors)

    def xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut_3(self, namespace: str | None) -> list[EdgeRecordData]:
        try:
            raw_services = self._fetch_raw_services(namespace)
            raw_policies = None
        except Exception:
            return []
        selectors = [_to_service_selector(svc) for svc in _items(raw_services)]
        return _build_edges_from_policies(_items(raw_policies), selectors)

    def xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut_4(self, namespace: str | None) -> list[EdgeRecordData]:
        try:
            raw_services = self._fetch_raw_services(namespace)
            raw_policies = self._fetch_raw_network_policies(None)
        except Exception:
            return []
        selectors = [_to_service_selector(svc) for svc in _items(raw_services)]
        return _build_edges_from_policies(_items(raw_policies), selectors)

    def xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut_5(self, namespace: str | None) -> list[EdgeRecordData]:
        try:
            raw_services = self._fetch_raw_services(namespace)
            raw_policies = self._fetch_raw_network_policies(namespace)
        except Exception:
            return []
        selectors = None
        return _build_edges_from_policies(_items(raw_policies), selectors)

    def xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut_6(self, namespace: str | None) -> list[EdgeRecordData]:
        try:
            raw_services = self._fetch_raw_services(namespace)
            raw_policies = self._fetch_raw_network_policies(namespace)
        except Exception:
            return []
        selectors = [_to_service_selector(None) for svc in _items(raw_services)]
        return _build_edges_from_policies(_items(raw_policies), selectors)

    def xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut_7(self, namespace: str | None) -> list[EdgeRecordData]:
        try:
            raw_services = self._fetch_raw_services(namespace)
            raw_policies = self._fetch_raw_network_policies(namespace)
        except Exception:
            return []
        selectors = [_to_service_selector(svc) for svc in _items(None)]
        return _build_edges_from_policies(_items(raw_policies), selectors)

    def xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut_8(self, namespace: str | None) -> list[EdgeRecordData]:
        try:
            raw_services = self._fetch_raw_services(namespace)
            raw_policies = self._fetch_raw_network_policies(namespace)
        except Exception:
            return []
        selectors = [_to_service_selector(svc) for svc in _items(raw_services)]
        return _build_edges_from_policies(None, selectors)

    def xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut_9(self, namespace: str | None) -> list[EdgeRecordData]:
        try:
            raw_services = self._fetch_raw_services(namespace)
            raw_policies = self._fetch_raw_network_policies(namespace)
        except Exception:
            return []
        selectors = [_to_service_selector(svc) for svc in _items(raw_services)]
        return _build_edges_from_policies(_items(raw_policies), None)

    def xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut_10(self, namespace: str | None) -> list[EdgeRecordData]:
        try:
            raw_services = self._fetch_raw_services(namespace)
            raw_policies = self._fetch_raw_network_policies(namespace)
        except Exception:
            return []
        selectors = [_to_service_selector(svc) for svc in _items(raw_services)]
        return _build_edges_from_policies(selectors)

    def xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut_11(self, namespace: str | None) -> list[EdgeRecordData]:
        try:
            raw_services = self._fetch_raw_services(namespace)
            raw_policies = self._fetch_raw_network_policies(namespace)
        except Exception:
            return []
        selectors = [_to_service_selector(svc) for svc in _items(raw_services)]
        return _build_edges_from_policies(_items(raw_policies), )

    def xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut_12(self, namespace: str | None) -> list[EdgeRecordData]:
        try:
            raw_services = self._fetch_raw_services(namespace)
            raw_policies = self._fetch_raw_network_policies(namespace)
        except Exception:
            return []
        selectors = [_to_service_selector(svc) for svc in _items(raw_services)]
        return _build_edges_from_policies(_items(None), selectors)

    # ── Internal ───────────────────────────────────────────────

    @_mutmut_mutated(mutants_xǁKubernetesTopologyAdapterǁ_fetch_raw_services__mutmut)
    def _fetch_raw_services(self, namespace: str | None) -> object:
        api = self._core_api_client()
        if namespace:
            return api.list_namespaced_service(namespace, timeout_seconds=_K8S_TIMEOUT)
        return api.list_service_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)

    # ── Internal ───────────────────────────────────────────────

    def xǁKubernetesTopologyAdapterǁ_fetch_raw_services__mutmut_orig(self, namespace: str | None) -> object:
        api = self._core_api_client()
        if namespace:
            return api.list_namespaced_service(namespace, timeout_seconds=_K8S_TIMEOUT)
        return api.list_service_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)

    # ── Internal ───────────────────────────────────────────────

    def xǁKubernetesTopologyAdapterǁ_fetch_raw_services__mutmut_1(self, namespace: str | None) -> object:
        api = None
        if namespace:
            return api.list_namespaced_service(namespace, timeout_seconds=_K8S_TIMEOUT)
        return api.list_service_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)

    # ── Internal ───────────────────────────────────────────────

    def xǁKubernetesTopologyAdapterǁ_fetch_raw_services__mutmut_2(self, namespace: str | None) -> object:
        api = self._core_api_client()
        if namespace:
            return api.list_namespaced_service(None, timeout_seconds=_K8S_TIMEOUT)
        return api.list_service_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)

    # ── Internal ───────────────────────────────────────────────

    def xǁKubernetesTopologyAdapterǁ_fetch_raw_services__mutmut_3(self, namespace: str | None) -> object:
        api = self._core_api_client()
        if namespace:
            return api.list_namespaced_service(namespace, timeout_seconds=None)
        return api.list_service_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)

    # ── Internal ───────────────────────────────────────────────

    def xǁKubernetesTopologyAdapterǁ_fetch_raw_services__mutmut_4(self, namespace: str | None) -> object:
        api = self._core_api_client()
        if namespace:
            return api.list_namespaced_service(timeout_seconds=_K8S_TIMEOUT)
        return api.list_service_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)

    # ── Internal ───────────────────────────────────────────────

    def xǁKubernetesTopologyAdapterǁ_fetch_raw_services__mutmut_5(self, namespace: str | None) -> object:
        api = self._core_api_client()
        if namespace:
            return api.list_namespaced_service(namespace, )
        return api.list_service_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)

    # ── Internal ───────────────────────────────────────────────

    def xǁKubernetesTopologyAdapterǁ_fetch_raw_services__mutmut_6(self, namespace: str | None) -> object:
        api = self._core_api_client()
        if namespace:
            return api.list_namespaced_service(namespace, timeout_seconds=_K8S_TIMEOUT)
        return api.list_service_for_all_namespaces(timeout_seconds=None)

    @_mutmut_mutated(mutants_xǁKubernetesTopologyAdapterǁ_fetch_raw_network_policies__mutmut)
    def _fetch_raw_network_policies(self, namespace: str | None) -> object:
        api = self._networking_api_client()
        if namespace:
            return api.list_namespaced_network_policy(namespace, timeout_seconds=_K8S_TIMEOUT)
        return api.list_network_policy_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)

    def xǁKubernetesTopologyAdapterǁ_fetch_raw_network_policies__mutmut_orig(self, namespace: str | None) -> object:
        api = self._networking_api_client()
        if namespace:
            return api.list_namespaced_network_policy(namespace, timeout_seconds=_K8S_TIMEOUT)
        return api.list_network_policy_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)

    def xǁKubernetesTopologyAdapterǁ_fetch_raw_network_policies__mutmut_1(self, namespace: str | None) -> object:
        api = None
        if namespace:
            return api.list_namespaced_network_policy(namespace, timeout_seconds=_K8S_TIMEOUT)
        return api.list_network_policy_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)

    def xǁKubernetesTopologyAdapterǁ_fetch_raw_network_policies__mutmut_2(self, namespace: str | None) -> object:
        api = self._networking_api_client()
        if namespace:
            return api.list_namespaced_network_policy(None, timeout_seconds=_K8S_TIMEOUT)
        return api.list_network_policy_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)

    def xǁKubernetesTopologyAdapterǁ_fetch_raw_network_policies__mutmut_3(self, namespace: str | None) -> object:
        api = self._networking_api_client()
        if namespace:
            return api.list_namespaced_network_policy(namespace, timeout_seconds=None)
        return api.list_network_policy_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)

    def xǁKubernetesTopologyAdapterǁ_fetch_raw_network_policies__mutmut_4(self, namespace: str | None) -> object:
        api = self._networking_api_client()
        if namespace:
            return api.list_namespaced_network_policy(timeout_seconds=_K8S_TIMEOUT)
        return api.list_network_policy_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)

    def xǁKubernetesTopologyAdapterǁ_fetch_raw_network_policies__mutmut_5(self, namespace: str | None) -> object:
        api = self._networking_api_client()
        if namespace:
            return api.list_namespaced_network_policy(namespace, )
        return api.list_network_policy_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)

    def xǁKubernetesTopologyAdapterǁ_fetch_raw_network_policies__mutmut_6(self, namespace: str | None) -> object:
        api = self._networking_api_client()
        if namespace:
            return api.list_namespaced_network_policy(namespace, timeout_seconds=_K8S_TIMEOUT)
        return api.list_network_policy_for_all_namespaces(timeout_seconds=None)

    @_mutmut_mutated(mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut)
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

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_orig(self, namespace: str | None) -> dict[str, int]:
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

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_1(self, namespace: str | None) -> dict[str, int]:
        try:
            api = None
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

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_2(self, namespace: str | None) -> dict[str, int]:
        try:
            api = self._apps_api_client()
            raw = None
        except Exception:
            return {}
        counts: dict[str, int] = {}
        for dep in _items(raw):
            name = str(getattr(getattr(dep, "metadata", None), "name", ""))
            spec = getattr(dep, "spec", None)
            counts[name] = int(getattr(spec, "replicas", 0) or 0)
        return counts

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_3(self, namespace: str | None) -> dict[str, int]:
        try:
            api = self._apps_api_client()
            raw = (
                api.list_namespaced_deployment(None, timeout_seconds=_K8S_TIMEOUT)
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

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_4(self, namespace: str | None) -> dict[str, int]:
        try:
            api = self._apps_api_client()
            raw = (
                api.list_namespaced_deployment(namespace, timeout_seconds=None)
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

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_5(self, namespace: str | None) -> dict[str, int]:
        try:
            api = self._apps_api_client()
            raw = (
                api.list_namespaced_deployment(timeout_seconds=_K8S_TIMEOUT)
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

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_6(self, namespace: str | None) -> dict[str, int]:
        try:
            api = self._apps_api_client()
            raw = (
                api.list_namespaced_deployment(namespace, )
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

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_7(self, namespace: str | None) -> dict[str, int]:
        try:
            api = self._apps_api_client()
            raw = (
                api.list_namespaced_deployment(namespace, timeout_seconds=_K8S_TIMEOUT)
                if namespace
                else api.list_deployment_for_all_namespaces(timeout_seconds=None)
            )
        except Exception:
            return {}
        counts: dict[str, int] = {}
        for dep in _items(raw):
            name = str(getattr(getattr(dep, "metadata", None), "name", ""))
            spec = getattr(dep, "spec", None)
            counts[name] = int(getattr(spec, "replicas", 0) or 0)
        return counts

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_8(self, namespace: str | None) -> dict[str, int]:
        try:
            api = self._apps_api_client()
            raw = (
                api.list_namespaced_deployment(namespace, timeout_seconds=_K8S_TIMEOUT)
                if namespace
                else api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
            )
        except Exception:
            return {}
        counts: dict[str, int] = None
        for dep in _items(raw):
            name = str(getattr(getattr(dep, "metadata", None), "name", ""))
            spec = getattr(dep, "spec", None)
            counts[name] = int(getattr(spec, "replicas", 0) or 0)
        return counts

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_9(self, namespace: str | None) -> dict[str, int]:
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
        for dep in _items(None):
            name = str(getattr(getattr(dep, "metadata", None), "name", ""))
            spec = getattr(dep, "spec", None)
            counts[name] = int(getattr(spec, "replicas", 0) or 0)
        return counts

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_10(self, namespace: str | None) -> dict[str, int]:
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
            name = None
            spec = getattr(dep, "spec", None)
            counts[name] = int(getattr(spec, "replicas", 0) or 0)
        return counts

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_11(self, namespace: str | None) -> dict[str, int]:
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
            name = str(None)
            spec = getattr(dep, "spec", None)
            counts[name] = int(getattr(spec, "replicas", 0) or 0)
        return counts

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_12(self, namespace: str | None) -> dict[str, int]:
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
            name = str(getattr(None, "name", ""))
            spec = getattr(dep, "spec", None)
            counts[name] = int(getattr(spec, "replicas", 0) or 0)
        return counts

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_13(self, namespace: str | None) -> dict[str, int]:
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
            name = str(getattr(getattr(dep, "metadata", None), None, ""))
            spec = getattr(dep, "spec", None)
            counts[name] = int(getattr(spec, "replicas", 0) or 0)
        return counts

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_14(self, namespace: str | None) -> dict[str, int]:
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
            name = str(getattr(getattr(dep, "metadata", None), "name", None))
            spec = getattr(dep, "spec", None)
            counts[name] = int(getattr(spec, "replicas", 0) or 0)
        return counts

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_15(self, namespace: str | None) -> dict[str, int]:
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
            name = str(getattr("name", ""))
            spec = getattr(dep, "spec", None)
            counts[name] = int(getattr(spec, "replicas", 0) or 0)
        return counts

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_16(self, namespace: str | None) -> dict[str, int]:
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
            name = str(getattr(getattr(dep, "metadata", None), ""))
            spec = getattr(dep, "spec", None)
            counts[name] = int(getattr(spec, "replicas", 0) or 0)
        return counts

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_17(self, namespace: str | None) -> dict[str, int]:
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
            name = str(getattr(getattr(dep, "metadata", None), "name", ))
            spec = getattr(dep, "spec", None)
            counts[name] = int(getattr(spec, "replicas", 0) or 0)
        return counts

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_18(self, namespace: str | None) -> dict[str, int]:
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
            name = str(getattr(getattr(None, "metadata", None), "name", ""))
            spec = getattr(dep, "spec", None)
            counts[name] = int(getattr(spec, "replicas", 0) or 0)
        return counts

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_19(self, namespace: str | None) -> dict[str, int]:
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
            name = str(getattr(getattr(dep, None, None), "name", ""))
            spec = getattr(dep, "spec", None)
            counts[name] = int(getattr(spec, "replicas", 0) or 0)
        return counts

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_20(self, namespace: str | None) -> dict[str, int]:
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
            name = str(getattr(getattr("metadata", None), "name", ""))
            spec = getattr(dep, "spec", None)
            counts[name] = int(getattr(spec, "replicas", 0) or 0)
        return counts

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_21(self, namespace: str | None) -> dict[str, int]:
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
            name = str(getattr(getattr(dep, None), "name", ""))
            spec = getattr(dep, "spec", None)
            counts[name] = int(getattr(spec, "replicas", 0) or 0)
        return counts

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_22(self, namespace: str | None) -> dict[str, int]:
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
            name = str(getattr(getattr(dep, "metadata", ), "name", ""))
            spec = getattr(dep, "spec", None)
            counts[name] = int(getattr(spec, "replicas", 0) or 0)
        return counts

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_23(self, namespace: str | None) -> dict[str, int]:
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
            name = str(getattr(getattr(dep, "XXmetadataXX", None), "name", ""))
            spec = getattr(dep, "spec", None)
            counts[name] = int(getattr(spec, "replicas", 0) or 0)
        return counts

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_24(self, namespace: str | None) -> dict[str, int]:
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
            name = str(getattr(getattr(dep, "METADATA", None), "name", ""))
            spec = getattr(dep, "spec", None)
            counts[name] = int(getattr(spec, "replicas", 0) or 0)
        return counts

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_25(self, namespace: str | None) -> dict[str, int]:
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
            name = str(getattr(getattr(dep, "metadata", None), "XXnameXX", ""))
            spec = getattr(dep, "spec", None)
            counts[name] = int(getattr(spec, "replicas", 0) or 0)
        return counts

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_26(self, namespace: str | None) -> dict[str, int]:
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
            name = str(getattr(getattr(dep, "metadata", None), "NAME", ""))
            spec = getattr(dep, "spec", None)
            counts[name] = int(getattr(spec, "replicas", 0) or 0)
        return counts

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_27(self, namespace: str | None) -> dict[str, int]:
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
            name = str(getattr(getattr(dep, "metadata", None), "name", "XXXX"))
            spec = getattr(dep, "spec", None)
            counts[name] = int(getattr(spec, "replicas", 0) or 0)
        return counts

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_28(self, namespace: str | None) -> dict[str, int]:
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
            spec = None
            counts[name] = int(getattr(spec, "replicas", 0) or 0)
        return counts

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_29(self, namespace: str | None) -> dict[str, int]:
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
            spec = getattr(None, "spec", None)
            counts[name] = int(getattr(spec, "replicas", 0) or 0)
        return counts

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_30(self, namespace: str | None) -> dict[str, int]:
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
            spec = getattr(dep, None, None)
            counts[name] = int(getattr(spec, "replicas", 0) or 0)
        return counts

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_31(self, namespace: str | None) -> dict[str, int]:
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
            spec = getattr("spec", None)
            counts[name] = int(getattr(spec, "replicas", 0) or 0)
        return counts

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_32(self, namespace: str | None) -> dict[str, int]:
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
            spec = getattr(dep, None)
            counts[name] = int(getattr(spec, "replicas", 0) or 0)
        return counts

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_33(self, namespace: str | None) -> dict[str, int]:
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
            spec = getattr(dep, "spec", )
            counts[name] = int(getattr(spec, "replicas", 0) or 0)
        return counts

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_34(self, namespace: str | None) -> dict[str, int]:
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
            spec = getattr(dep, "XXspecXX", None)
            counts[name] = int(getattr(spec, "replicas", 0) or 0)
        return counts

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_35(self, namespace: str | None) -> dict[str, int]:
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
            spec = getattr(dep, "SPEC", None)
            counts[name] = int(getattr(spec, "replicas", 0) or 0)
        return counts

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_36(self, namespace: str | None) -> dict[str, int]:
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
            counts[name] = None
        return counts

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_37(self, namespace: str | None) -> dict[str, int]:
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
            counts[name] = int(None)
        return counts

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_38(self, namespace: str | None) -> dict[str, int]:
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
            counts[name] = int(getattr(spec, "replicas", 0) and 0)
        return counts

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_39(self, namespace: str | None) -> dict[str, int]:
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
            counts[name] = int(getattr(None, "replicas", 0) or 0)
        return counts

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_40(self, namespace: str | None) -> dict[str, int]:
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
            counts[name] = int(getattr(spec, None, 0) or 0)
        return counts

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_41(self, namespace: str | None) -> dict[str, int]:
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
            counts[name] = int(getattr(spec, "replicas", None) or 0)
        return counts

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_42(self, namespace: str | None) -> dict[str, int]:
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
            counts[name] = int(getattr("replicas", 0) or 0)
        return counts

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_43(self, namespace: str | None) -> dict[str, int]:
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
            counts[name] = int(getattr(spec, 0) or 0)
        return counts

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_44(self, namespace: str | None) -> dict[str, int]:
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
            counts[name] = int(getattr(spec, "replicas", ) or 0)
        return counts

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_45(self, namespace: str | None) -> dict[str, int]:
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
            counts[name] = int(getattr(spec, "XXreplicasXX", 0) or 0)
        return counts

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_46(self, namespace: str | None) -> dict[str, int]:
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
            counts[name] = int(getattr(spec, "REPLICAS", 0) or 0)
        return counts

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_47(self, namespace: str | None) -> dict[str, int]:
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
            counts[name] = int(getattr(spec, "replicas", 1) or 0)
        return counts

    def xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_48(self, namespace: str | None) -> dict[str, int]:
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
            counts[name] = int(getattr(spec, "replicas", 0) or 1)
        return counts

    @_mutmut_mutated(mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut)
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

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_orig(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
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

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_1(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = None
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

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_2(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(None, "metadata", None)
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

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_3(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, None, None)
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

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_4(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr("metadata", None)
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

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_5(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, None)
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

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_6(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", )
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

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_7(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "XXmetadataXX", None)
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

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_8(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "METADATA", None)
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

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_9(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = None
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_10(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(None, "spec", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_11(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, None, None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_12(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr("spec", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_13(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_14(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", )
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_15(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "XXspecXX", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_16(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "SPEC", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_17(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = None
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_18(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(None)
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_19(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(None, "name", "unknown"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_20(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, None, "unknown"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_21(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", None))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_22(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr("name", "unknown"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_23(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "unknown"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_24(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", ))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_25(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "XXnameXX", "unknown"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_26(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "NAME", "unknown"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_27(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", "XXunknownXX"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_28(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", "UNKNOWN"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_29(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = None
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_30(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(None)
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_31(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(None, "namespace", "default"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_32(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, None, "default"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_33(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "namespace", None))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_34(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr("namespace", "default"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_35(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "default"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_36(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "namespace", ))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_37(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "XXnamespaceXX", "default"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_38(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "NAMESPACE", "default"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_39(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "namespace", "XXdefaultXX"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_40(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "namespace", "DEFAULT"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_41(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = None
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_42(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(None)
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_43(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "type", "") and "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_44(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(None, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_45(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, None, "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_46(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "type", None) or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_47(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr("type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_48(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_49(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "type", ) or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_50(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "XXtypeXX", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_51(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "TYPE", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_52(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "type", "XXXX") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_53(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "type", "") or "XXXX")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_54(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=None,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_55(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=None,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_56(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=None,
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_57(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=None,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_58(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_59(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_60(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_61(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_62(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(None, 0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_63(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, None),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_64(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(0),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_65(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, ),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_66(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 1),
            is_external=service_type == _EXTERNAL_NAME_TYPE,
        )

    def xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_67(self, svc: object, replica_by_name: dict[str, int]) -> ServiceRecordData:
        metadata = getattr(svc, "metadata", None)
        spec = getattr(svc, "spec", None)
        name = str(getattr(metadata, "name", "unknown"))
        namespace = str(getattr(metadata, "namespace", "default"))
        service_type = str(getattr(spec, "type", "") or "")
        return ServiceRecordData(
            name=name,
            namespace=namespace,
            replicas=replica_by_name.get(name, 0),
            is_external=service_type != _EXTERNAL_NAME_TYPE,
        )

    @_mutmut_mutated(mutants_xǁKubernetesTopologyAdapterǁ_core_api_client__mutmut)
    def _core_api_client(self) -> _CoreServiceApi:
        if self._core_api is None:
            self._core_api = cast(_CoreServiceApi, load_kubeconfig(context=self._context_name()))
        return self._core_api

    def xǁKubernetesTopologyAdapterǁ_core_api_client__mutmut_orig(self) -> _CoreServiceApi:
        if self._core_api is None:
            self._core_api = cast(_CoreServiceApi, load_kubeconfig(context=self._context_name()))
        return self._core_api

    def xǁKubernetesTopologyAdapterǁ_core_api_client__mutmut_1(self) -> _CoreServiceApi:
        if self._core_api is not None:
            self._core_api = cast(_CoreServiceApi, load_kubeconfig(context=self._context_name()))
        return self._core_api

    def xǁKubernetesTopologyAdapterǁ_core_api_client__mutmut_2(self) -> _CoreServiceApi:
        if self._core_api is None:
            self._core_api = None
        return self._core_api

    def xǁKubernetesTopologyAdapterǁ_core_api_client__mutmut_3(self) -> _CoreServiceApi:
        if self._core_api is None:
            self._core_api = cast(None, load_kubeconfig(context=self._context_name()))
        return self._core_api

    def xǁKubernetesTopologyAdapterǁ_core_api_client__mutmut_4(self) -> _CoreServiceApi:
        if self._core_api is None:
            self._core_api = cast(_CoreServiceApi, None)
        return self._core_api

    def xǁKubernetesTopologyAdapterǁ_core_api_client__mutmut_5(self) -> _CoreServiceApi:
        if self._core_api is None:
            self._core_api = cast(load_kubeconfig(context=self._context_name()))
        return self._core_api

    def xǁKubernetesTopologyAdapterǁ_core_api_client__mutmut_6(self) -> _CoreServiceApi:
        if self._core_api is None:
            self._core_api = cast(_CoreServiceApi, )
        return self._core_api

    def xǁKubernetesTopologyAdapterǁ_core_api_client__mutmut_7(self) -> _CoreServiceApi:
        if self._core_api is None:
            self._core_api = cast(_CoreServiceApi, load_kubeconfig(context=None))
        return self._core_api

    @_mutmut_mutated(mutants_xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut)
    def _apps_api_client(self) -> _AppsApi:
        if self._apps_api is None:
            from kubernetes import client

            core_api = cast(client.CoreV1Api, self._core_api_client())
            self._apps_api = cast(_AppsApi, client.AppsV1Api(api_client=core_api.api_client))
        return self._apps_api

    def xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut_orig(self) -> _AppsApi:
        if self._apps_api is None:
            from kubernetes import client

            core_api = cast(client.CoreV1Api, self._core_api_client())
            self._apps_api = cast(_AppsApi, client.AppsV1Api(api_client=core_api.api_client))
        return self._apps_api

    def xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut_1(self) -> _AppsApi:
        if self._apps_api is not None:
            from kubernetes import client

            core_api = cast(client.CoreV1Api, self._core_api_client())
            self._apps_api = cast(_AppsApi, client.AppsV1Api(api_client=core_api.api_client))
        return self._apps_api

    def xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut_2(self) -> _AppsApi:
        if self._apps_api is None:
            from kubernetes import client

            core_api = None
            self._apps_api = cast(_AppsApi, client.AppsV1Api(api_client=core_api.api_client))
        return self._apps_api

    def xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut_3(self) -> _AppsApi:
        if self._apps_api is None:
            from kubernetes import client

            core_api = cast(None, self._core_api_client())
            self._apps_api = cast(_AppsApi, client.AppsV1Api(api_client=core_api.api_client))
        return self._apps_api

    def xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut_4(self) -> _AppsApi:
        if self._apps_api is None:
            from kubernetes import client

            core_api = cast(client.CoreV1Api, None)
            self._apps_api = cast(_AppsApi, client.AppsV1Api(api_client=core_api.api_client))
        return self._apps_api

    def xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut_5(self) -> _AppsApi:
        if self._apps_api is None:
            from kubernetes import client

            core_api = cast(self._core_api_client())
            self._apps_api = cast(_AppsApi, client.AppsV1Api(api_client=core_api.api_client))
        return self._apps_api

    def xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut_6(self) -> _AppsApi:
        if self._apps_api is None:
            from kubernetes import client

            core_api = cast(client.CoreV1Api, )
            self._apps_api = cast(_AppsApi, client.AppsV1Api(api_client=core_api.api_client))
        return self._apps_api

    def xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut_7(self) -> _AppsApi:
        if self._apps_api is None:
            from kubernetes import client

            core_api = cast(client.CoreV1Api, self._core_api_client())
            self._apps_api = None
        return self._apps_api

    def xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut_8(self) -> _AppsApi:
        if self._apps_api is None:
            from kubernetes import client

            core_api = cast(client.CoreV1Api, self._core_api_client())
            self._apps_api = cast(None, client.AppsV1Api(api_client=core_api.api_client))
        return self._apps_api

    def xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut_9(self) -> _AppsApi:
        if self._apps_api is None:
            from kubernetes import client

            core_api = cast(client.CoreV1Api, self._core_api_client())
            self._apps_api = cast(_AppsApi, None)
        return self._apps_api

    def xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut_10(self) -> _AppsApi:
        if self._apps_api is None:
            from kubernetes import client

            core_api = cast(client.CoreV1Api, self._core_api_client())
            self._apps_api = cast(client.AppsV1Api(api_client=core_api.api_client))
        return self._apps_api

    def xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut_11(self) -> _AppsApi:
        if self._apps_api is None:
            from kubernetes import client

            core_api = cast(client.CoreV1Api, self._core_api_client())
            self._apps_api = cast(_AppsApi, )
        return self._apps_api

    def xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut_12(self) -> _AppsApi:
        if self._apps_api is None:
            from kubernetes import client

            core_api = cast(client.CoreV1Api, self._core_api_client())
            self._apps_api = cast(_AppsApi, client.AppsV1Api(api_client=None))
        return self._apps_api

    @_mutmut_mutated(mutants_xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut)
    def _networking_api_client(self) -> _NetworkingApi:
        if self._networking_api is None:
            from kubernetes import client

            core_api = cast(client.CoreV1Api, self._core_api_client())
            self._networking_api = cast(
                _NetworkingApi, client.NetworkingV1Api(api_client=core_api.api_client)
            )
        return self._networking_api

    def xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut_orig(self) -> _NetworkingApi:
        if self._networking_api is None:
            from kubernetes import client

            core_api = cast(client.CoreV1Api, self._core_api_client())
            self._networking_api = cast(
                _NetworkingApi, client.NetworkingV1Api(api_client=core_api.api_client)
            )
        return self._networking_api

    def xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut_1(self) -> _NetworkingApi:
        if self._networking_api is not None:
            from kubernetes import client

            core_api = cast(client.CoreV1Api, self._core_api_client())
            self._networking_api = cast(
                _NetworkingApi, client.NetworkingV1Api(api_client=core_api.api_client)
            )
        return self._networking_api

    def xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut_2(self) -> _NetworkingApi:
        if self._networking_api is None:
            from kubernetes import client

            core_api = None
            self._networking_api = cast(
                _NetworkingApi, client.NetworkingV1Api(api_client=core_api.api_client)
            )
        return self._networking_api

    def xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut_3(self) -> _NetworkingApi:
        if self._networking_api is None:
            from kubernetes import client

            core_api = cast(None, self._core_api_client())
            self._networking_api = cast(
                _NetworkingApi, client.NetworkingV1Api(api_client=core_api.api_client)
            )
        return self._networking_api

    def xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut_4(self) -> _NetworkingApi:
        if self._networking_api is None:
            from kubernetes import client

            core_api = cast(client.CoreV1Api, None)
            self._networking_api = cast(
                _NetworkingApi, client.NetworkingV1Api(api_client=core_api.api_client)
            )
        return self._networking_api

    def xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut_5(self) -> _NetworkingApi:
        if self._networking_api is None:
            from kubernetes import client

            core_api = cast(self._core_api_client())
            self._networking_api = cast(
                _NetworkingApi, client.NetworkingV1Api(api_client=core_api.api_client)
            )
        return self._networking_api

    def xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut_6(self) -> _NetworkingApi:
        if self._networking_api is None:
            from kubernetes import client

            core_api = cast(client.CoreV1Api, )
            self._networking_api = cast(
                _NetworkingApi, client.NetworkingV1Api(api_client=core_api.api_client)
            )
        return self._networking_api

    def xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut_7(self) -> _NetworkingApi:
        if self._networking_api is None:
            from kubernetes import client

            core_api = cast(client.CoreV1Api, self._core_api_client())
            self._networking_api = None
        return self._networking_api

    def xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut_8(self) -> _NetworkingApi:
        if self._networking_api is None:
            from kubernetes import client

            core_api = cast(client.CoreV1Api, self._core_api_client())
            self._networking_api = cast(
                None, client.NetworkingV1Api(api_client=core_api.api_client)
            )
        return self._networking_api

    def xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut_9(self) -> _NetworkingApi:
        if self._networking_api is None:
            from kubernetes import client

            core_api = cast(client.CoreV1Api, self._core_api_client())
            self._networking_api = cast(
                _NetworkingApi, None
            )
        return self._networking_api

    def xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut_10(self) -> _NetworkingApi:
        if self._networking_api is None:
            from kubernetes import client

            core_api = cast(client.CoreV1Api, self._core_api_client())
            self._networking_api = cast(
                client.NetworkingV1Api(api_client=core_api.api_client)
            )
        return self._networking_api

    def xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut_11(self) -> _NetworkingApi:
        if self._networking_api is None:
            from kubernetes import client

            core_api = cast(client.CoreV1Api, self._core_api_client())
            self._networking_api = cast(
                _NetworkingApi, )
        return self._networking_api

    def xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut_12(self) -> _NetworkingApi:
        if self._networking_api is None:
            from kubernetes import client

            core_api = cast(client.CoreV1Api, self._core_api_client())
            self._networking_api = cast(
                _NetworkingApi, client.NetworkingV1Api(api_client=None)
            )
        return self._networking_api

    @_mutmut_mutated(mutants_xǁKubernetesTopologyAdapterǁ_context_name__mutmut)
    def _context_name(self) -> str | None:
        return None if self._cluster_name == "unknown" else self._cluster_name

    def xǁKubernetesTopologyAdapterǁ_context_name__mutmut_orig(self) -> str | None:
        return None if self._cluster_name == "unknown" else self._cluster_name

    def xǁKubernetesTopologyAdapterǁ_context_name__mutmut_1(self) -> str | None:
        return None if self._cluster_name != "unknown" else self._cluster_name

    def xǁKubernetesTopologyAdapterǁ_context_name__mutmut_2(self) -> str | None:
        return None if self._cluster_name == "XXunknownXX" else self._cluster_name

    def xǁKubernetesTopologyAdapterǁ_context_name__mutmut_3(self) -> str | None:
        return None if self._cluster_name == "UNKNOWN" else self._cluster_name

mutants_xǁKubernetesTopologyAdapterǁ__init____mutmut['_mutmut_orig'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ__init____mutmut['xǁKubernetesTopologyAdapterǁ__init____mutmut_1'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ__init____mutmut['xǁKubernetesTopologyAdapterǁ__init____mutmut_2'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ__init____mutmut['xǁKubernetesTopologyAdapterǁ__init____mutmut_3'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ__init____mutmut['xǁKubernetesTopologyAdapterǁ__init____mutmut_4'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ__init____mutmut_4 # type: ignore # mutmut generated

mutants_xǁKubernetesTopologyAdapterǁlist_services__mutmut['_mutmut_orig'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁlist_services__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁlist_services__mutmut['xǁKubernetesTopologyAdapterǁlist_services__mutmut_1'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁlist_services__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁlist_services__mutmut['xǁKubernetesTopologyAdapterǁlist_services__mutmut_2'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁlist_services__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁlist_services__mutmut['xǁKubernetesTopologyAdapterǁlist_services__mutmut_3'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁlist_services__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁlist_services__mutmut['xǁKubernetesTopologyAdapterǁlist_services__mutmut_4'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁlist_services__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁlist_services__mutmut['xǁKubernetesTopologyAdapterǁlist_services__mutmut_5'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁlist_services__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁlist_services__mutmut['xǁKubernetesTopologyAdapterǁlist_services__mutmut_6'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁlist_services__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁlist_services__mutmut['xǁKubernetesTopologyAdapterǁlist_services__mutmut_7'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁlist_services__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁlist_services__mutmut['xǁKubernetesTopologyAdapterǁlist_services__mutmut_8'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁlist_services__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁlist_services__mutmut['xǁKubernetesTopologyAdapterǁlist_services__mutmut_9'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁlist_services__mutmut_9 # type: ignore # mutmut generated

mutants_xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut['_mutmut_orig'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut['xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut_1'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut['xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut_2'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut['xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut_3'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut['xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut_4'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut['xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut_5'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut['xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut_6'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut['xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut_7'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut['xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut_8'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut['xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut_9'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut['xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut_10'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut['xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut_11'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut['xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut_12'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁget_network_policy_edges__mutmut_12 # type: ignore # mutmut generated

mutants_xǁKubernetesTopologyAdapterǁ_fetch_raw_services__mutmut['_mutmut_orig'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_fetch_raw_services__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_fetch_raw_services__mutmut['xǁKubernetesTopologyAdapterǁ_fetch_raw_services__mutmut_1'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_fetch_raw_services__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_fetch_raw_services__mutmut['xǁKubernetesTopologyAdapterǁ_fetch_raw_services__mutmut_2'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_fetch_raw_services__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_fetch_raw_services__mutmut['xǁKubernetesTopologyAdapterǁ_fetch_raw_services__mutmut_3'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_fetch_raw_services__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_fetch_raw_services__mutmut['xǁKubernetesTopologyAdapterǁ_fetch_raw_services__mutmut_4'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_fetch_raw_services__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_fetch_raw_services__mutmut['xǁKubernetesTopologyAdapterǁ_fetch_raw_services__mutmut_5'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_fetch_raw_services__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_fetch_raw_services__mutmut['xǁKubernetesTopologyAdapterǁ_fetch_raw_services__mutmut_6'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_fetch_raw_services__mutmut_6 # type: ignore # mutmut generated

mutants_xǁKubernetesTopologyAdapterǁ_fetch_raw_network_policies__mutmut['_mutmut_orig'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_fetch_raw_network_policies__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_fetch_raw_network_policies__mutmut['xǁKubernetesTopologyAdapterǁ_fetch_raw_network_policies__mutmut_1'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_fetch_raw_network_policies__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_fetch_raw_network_policies__mutmut['xǁKubernetesTopologyAdapterǁ_fetch_raw_network_policies__mutmut_2'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_fetch_raw_network_policies__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_fetch_raw_network_policies__mutmut['xǁKubernetesTopologyAdapterǁ_fetch_raw_network_policies__mutmut_3'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_fetch_raw_network_policies__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_fetch_raw_network_policies__mutmut['xǁKubernetesTopologyAdapterǁ_fetch_raw_network_policies__mutmut_4'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_fetch_raw_network_policies__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_fetch_raw_network_policies__mutmut['xǁKubernetesTopologyAdapterǁ_fetch_raw_network_policies__mutmut_5'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_fetch_raw_network_policies__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_fetch_raw_network_policies__mutmut['xǁKubernetesTopologyAdapterǁ_fetch_raw_network_policies__mutmut_6'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_fetch_raw_network_policies__mutmut_6 # type: ignore # mutmut generated

mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['_mutmut_orig'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_1'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_2'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_3'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_4'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_5'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_6'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_7'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_8'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_9'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_10'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_11'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_12'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_13'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_14'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_14 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_15'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_15 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_16'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_16 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_17'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_17 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_18'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_18 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_19'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_19 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_20'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_20 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_21'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_21 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_22'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_22 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_23'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_23 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_24'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_24 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_25'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_25 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_26'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_26 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_27'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_27 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_28'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_28 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_29'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_29 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_30'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_30 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_31'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_31 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_32'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_32 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_33'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_33 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_34'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_34 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_35'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_35 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_36'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_36 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_37'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_37 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_38'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_38 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_39'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_39 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_40'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_40 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_41'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_41 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_42'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_42 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_43'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_43 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_44'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_44 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_45'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_45 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_46'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_46 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_47'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_47 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut['xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_48'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_replica_counts_by_name__mutmut_48 # type: ignore # mutmut generated

mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['_mutmut_orig'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_1'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_2'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_3'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_4'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_5'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_6'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_7'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_8'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_9'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_10'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_11'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_12'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_13'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_14'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_14 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_15'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_15 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_16'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_16 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_17'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_17 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_18'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_18 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_19'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_19 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_20'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_20 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_21'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_21 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_22'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_22 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_23'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_23 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_24'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_24 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_25'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_25 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_26'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_26 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_27'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_27 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_28'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_28 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_29'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_29 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_30'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_30 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_31'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_31 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_32'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_32 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_33'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_33 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_34'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_34 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_35'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_35 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_36'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_36 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_37'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_37 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_38'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_38 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_39'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_39 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_40'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_40 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_41'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_41 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_42'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_42 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_43'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_43 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_44'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_44 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_45'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_45 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_46'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_46 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_47'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_47 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_48'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_48 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_49'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_49 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_50'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_50 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_51'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_51 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_52'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_52 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_53'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_53 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_54'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_54 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_55'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_55 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_56'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_56 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_57'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_57 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_58'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_58 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_59'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_59 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_60'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_60 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_61'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_61 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_62'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_62 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_63'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_63 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_64'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_64 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_65'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_65 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_66'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_66 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut['xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_67'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_to_service_record__mutmut_67 # type: ignore # mutmut generated

mutants_xǁKubernetesTopologyAdapterǁ_core_api_client__mutmut['_mutmut_orig'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_core_api_client__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_core_api_client__mutmut['xǁKubernetesTopologyAdapterǁ_core_api_client__mutmut_1'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_core_api_client__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_core_api_client__mutmut['xǁKubernetesTopologyAdapterǁ_core_api_client__mutmut_2'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_core_api_client__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_core_api_client__mutmut['xǁKubernetesTopologyAdapterǁ_core_api_client__mutmut_3'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_core_api_client__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_core_api_client__mutmut['xǁKubernetesTopologyAdapterǁ_core_api_client__mutmut_4'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_core_api_client__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_core_api_client__mutmut['xǁKubernetesTopologyAdapterǁ_core_api_client__mutmut_5'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_core_api_client__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_core_api_client__mutmut['xǁKubernetesTopologyAdapterǁ_core_api_client__mutmut_6'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_core_api_client__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_core_api_client__mutmut['xǁKubernetesTopologyAdapterǁ_core_api_client__mutmut_7'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_core_api_client__mutmut_7 # type: ignore # mutmut generated

mutants_xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut['_mutmut_orig'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut['xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut_1'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut['xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut_2'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut['xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut_3'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut['xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut_4'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut['xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut_5'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut['xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut_6'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut['xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut_7'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut['xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut_8'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut['xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut_9'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut['xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut_10'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut['xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut_11'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut['xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut_12'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_apps_api_client__mutmut_12 # type: ignore # mutmut generated

mutants_xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut['_mutmut_orig'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut['xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut_1'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut['xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut_2'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut['xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut_3'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut['xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut_4'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut['xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut_5'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut['xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut_6'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut['xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut_7'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut['xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut_8'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut['xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut_9'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut['xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut_10'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut['xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut_11'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut['xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut_12'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_networking_api_client__mutmut_12 # type: ignore # mutmut generated

mutants_xǁKubernetesTopologyAdapterǁ_context_name__mutmut['_mutmut_orig'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_context_name__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_context_name__mutmut['xǁKubernetesTopologyAdapterǁ_context_name__mutmut_1'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_context_name__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_context_name__mutmut['xǁKubernetesTopologyAdapterǁ_context_name__mutmut_2'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_context_name__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesTopologyAdapterǁ_context_name__mutmut['xǁKubernetesTopologyAdapterǁ_context_name__mutmut_3'] = KubernetesTopologyAdapter.xǁKubernetesTopologyAdapterǁ_context_name__mutmut_3 # type: ignore # mutmut generated
mutants_x__items__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__items__mutmut)
def _items(api_response: object) -> list[object]:
    return list(getattr(api_response, "items", None) or [])


def x__items__mutmut_orig(api_response: object) -> list[object]:
    return list(getattr(api_response, "items", None) or [])


def x__items__mutmut_1(api_response: object) -> list[object]:
    return list(None)


def x__items__mutmut_2(api_response: object) -> list[object]:
    return list(getattr(api_response, "items", None) and [])


def x__items__mutmut_3(api_response: object) -> list[object]:
    return list(getattr(None, "items", None) or [])


def x__items__mutmut_4(api_response: object) -> list[object]:
    return list(getattr(api_response, None, None) or [])


def x__items__mutmut_5(api_response: object) -> list[object]:
    return list(getattr("items", None) or [])


def x__items__mutmut_6(api_response: object) -> list[object]:
    return list(getattr(api_response, None) or [])


def x__items__mutmut_7(api_response: object) -> list[object]:
    return list(getattr(api_response, "items", ) or [])


def x__items__mutmut_8(api_response: object) -> list[object]:
    return list(getattr(api_response, "XXitemsXX", None) or [])


def x__items__mutmut_9(api_response: object) -> list[object]:
    return list(getattr(api_response, "ITEMS", None) or [])

mutants_x__items__mutmut['_mutmut_orig'] = x__items__mutmut_orig # type: ignore # mutmut generated
mutants_x__items__mutmut['x__items__mutmut_1'] = x__items__mutmut_1 # type: ignore # mutmut generated
mutants_x__items__mutmut['x__items__mutmut_2'] = x__items__mutmut_2 # type: ignore # mutmut generated
mutants_x__items__mutmut['x__items__mutmut_3'] = x__items__mutmut_3 # type: ignore # mutmut generated
mutants_x__items__mutmut['x__items__mutmut_4'] = x__items__mutmut_4 # type: ignore # mutmut generated
mutants_x__items__mutmut['x__items__mutmut_5'] = x__items__mutmut_5 # type: ignore # mutmut generated
mutants_x__items__mutmut['x__items__mutmut_6'] = x__items__mutmut_6 # type: ignore # mutmut generated
mutants_x__items__mutmut['x__items__mutmut_7'] = x__items__mutmut_7 # type: ignore # mutmut generated
mutants_x__items__mutmut['x__items__mutmut_8'] = x__items__mutmut_8 # type: ignore # mutmut generated
mutants_x__items__mutmut['x__items__mutmut_9'] = x__items__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_service_selector__mutmut)
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


def x__to_service_selector__mutmut_orig(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_1(svc: object) -> _ServiceSelector:
    metadata = None
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_2(svc: object) -> _ServiceSelector:
    metadata = getattr(None, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_3(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, None, None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_4(svc: object) -> _ServiceSelector:
    metadata = getattr("metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_5(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_6(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", )
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_7(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "XXmetadataXX", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_8(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "METADATA", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_9(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = None
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_10(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(None, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_11(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, None, None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_12(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr("spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_13(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_14(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", )
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_15(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "XXspecXX", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_16(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "SPEC", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_17(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = None
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_18(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) and {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_19(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(None, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_20(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, None, None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_21(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr("selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_22(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_23(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", ) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_24(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "XXselectorXX", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_25(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "SELECTOR", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_26(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_27(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get(None) if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_28(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("XXappXX") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_29(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("APP") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_30(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=None,
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_31(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=None,
        app_label=app_label,
    )


def x__to_service_selector__mutmut_32(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=None,
    )


def x__to_service_selector__mutmut_33(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_34(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_35(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr(metadata, "namespace", "default")),
        )


def x__to_service_selector__mutmut_36(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(None),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_37(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(None, "name", "unknown")),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_38(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, None, "unknown")),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_39(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", None)),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_40(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr("name", "unknown")),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_41(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "unknown")),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_42(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", )),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_43(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "XXnameXX", "unknown")),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_44(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "NAME", "unknown")),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_45(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "XXunknownXX")),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_46(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "UNKNOWN")),
        namespace=str(getattr(metadata, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_47(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(None),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_48(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr(None, "namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_49(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr(metadata, None, "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_50(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr(metadata, "namespace", None)),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_51(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr("namespace", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_52(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr(metadata, "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_53(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr(metadata, "namespace", )),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_54(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr(metadata, "XXnamespaceXX", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_55(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr(metadata, "NAMESPACE", "default")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_56(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr(metadata, "namespace", "XXdefaultXX")),
        app_label=app_label,
    )


def x__to_service_selector__mutmut_57(svc: object) -> _ServiceSelector:
    metadata = getattr(svc, "metadata", None)
    spec = getattr(svc, "spec", None)
    selector = getattr(spec, "selector", None) or {}
    app_label = selector.get("app") if isinstance(selector, dict) else None
    return _ServiceSelector(
        name=str(getattr(metadata, "name", "unknown")),
        namespace=str(getattr(metadata, "namespace", "DEFAULT")),
        app_label=app_label,
    )

mutants_x__to_service_selector__mutmut['_mutmut_orig'] = x__to_service_selector__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_1'] = x__to_service_selector__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_2'] = x__to_service_selector__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_3'] = x__to_service_selector__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_4'] = x__to_service_selector__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_5'] = x__to_service_selector__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_6'] = x__to_service_selector__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_7'] = x__to_service_selector__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_8'] = x__to_service_selector__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_9'] = x__to_service_selector__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_10'] = x__to_service_selector__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_11'] = x__to_service_selector__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_12'] = x__to_service_selector__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_13'] = x__to_service_selector__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_14'] = x__to_service_selector__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_15'] = x__to_service_selector__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_16'] = x__to_service_selector__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_17'] = x__to_service_selector__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_18'] = x__to_service_selector__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_19'] = x__to_service_selector__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_20'] = x__to_service_selector__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_21'] = x__to_service_selector__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_22'] = x__to_service_selector__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_23'] = x__to_service_selector__mutmut_23 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_24'] = x__to_service_selector__mutmut_24 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_25'] = x__to_service_selector__mutmut_25 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_26'] = x__to_service_selector__mutmut_26 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_27'] = x__to_service_selector__mutmut_27 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_28'] = x__to_service_selector__mutmut_28 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_29'] = x__to_service_selector__mutmut_29 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_30'] = x__to_service_selector__mutmut_30 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_31'] = x__to_service_selector__mutmut_31 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_32'] = x__to_service_selector__mutmut_32 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_33'] = x__to_service_selector__mutmut_33 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_34'] = x__to_service_selector__mutmut_34 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_35'] = x__to_service_selector__mutmut_35 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_36'] = x__to_service_selector__mutmut_36 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_37'] = x__to_service_selector__mutmut_37 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_38'] = x__to_service_selector__mutmut_38 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_39'] = x__to_service_selector__mutmut_39 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_40'] = x__to_service_selector__mutmut_40 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_41'] = x__to_service_selector__mutmut_41 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_42'] = x__to_service_selector__mutmut_42 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_43'] = x__to_service_selector__mutmut_43 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_44'] = x__to_service_selector__mutmut_44 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_45'] = x__to_service_selector__mutmut_45 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_46'] = x__to_service_selector__mutmut_46 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_47'] = x__to_service_selector__mutmut_47 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_48'] = x__to_service_selector__mutmut_48 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_49'] = x__to_service_selector__mutmut_49 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_50'] = x__to_service_selector__mutmut_50 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_51'] = x__to_service_selector__mutmut_51 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_52'] = x__to_service_selector__mutmut_52 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_53'] = x__to_service_selector__mutmut_53 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_54'] = x__to_service_selector__mutmut_54 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_55'] = x__to_service_selector__mutmut_55 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_56'] = x__to_service_selector__mutmut_56 # type: ignore # mutmut generated
mutants_x__to_service_selector__mutmut['x__to_service_selector__mutmut_57'] = x__to_service_selector__mutmut_57 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__build_edges_from_policies__mutmut)
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


def x__build_edges_from_policies__mutmut_orig(
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


def x__build_edges_from_policies__mutmut_1(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = None
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


def x__build_edges_from_policies__mutmut_2(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = None

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


def x__build_edges_from_policies__mutmut_3(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = None
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


def x__build_edges_from_policies__mutmut_4(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(None, "metadata", None)
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


def x__build_edges_from_policies__mutmut_5(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, None, None)
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


def x__build_edges_from_policies__mutmut_6(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr("metadata", None)
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


def x__build_edges_from_policies__mutmut_7(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, None)
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


def x__build_edges_from_policies__mutmut_8(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", )
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


def x__build_edges_from_policies__mutmut_9(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "XXmetadataXX", None)
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


def x__build_edges_from_policies__mutmut_10(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "METADATA", None)
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


def x__build_edges_from_policies__mutmut_11(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = None
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


def x__build_edges_from_policies__mutmut_12(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = str(None)
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


def x__build_edges_from_policies__mutmut_13(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = str(getattr(None, "namespace", "default"))
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


def x__build_edges_from_policies__mutmut_14(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = str(getattr(metadata, None, "default"))
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


def x__build_edges_from_policies__mutmut_15(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = str(getattr(metadata, "namespace", None))
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


def x__build_edges_from_policies__mutmut_16(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = str(getattr("namespace", "default"))
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


def x__build_edges_from_policies__mutmut_17(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = str(getattr(metadata, "default"))
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


def x__build_edges_from_policies__mutmut_18(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = str(getattr(metadata, "namespace", ))
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


def x__build_edges_from_policies__mutmut_19(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = str(getattr(metadata, "XXnamespaceXX", "default"))
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


def x__build_edges_from_policies__mutmut_20(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = str(getattr(metadata, "NAMESPACE", "default"))
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


def x__build_edges_from_policies__mutmut_21(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = str(getattr(metadata, "namespace", "XXdefaultXX"))
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


def x__build_edges_from_policies__mutmut_22(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = str(getattr(metadata, "namespace", "DEFAULT"))
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


def x__build_edges_from_policies__mutmut_23(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = str(getattr(metadata, "namespace", "default"))
        spec = None
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


def x__build_edges_from_policies__mutmut_24(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = str(getattr(metadata, "namespace", "default"))
        spec = getattr(None, "spec", None)
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


def x__build_edges_from_policies__mutmut_25(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = str(getattr(metadata, "namespace", "default"))
        spec = getattr(policy, None, None)
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


def x__build_edges_from_policies__mutmut_26(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = str(getattr(metadata, "namespace", "default"))
        spec = getattr("spec", None)
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


def x__build_edges_from_policies__mutmut_27(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = str(getattr(metadata, "namespace", "default"))
        spec = getattr(policy, None)
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


def x__build_edges_from_policies__mutmut_28(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = str(getattr(metadata, "namespace", "default"))
        spec = getattr(policy, "spec", )
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


def x__build_edges_from_policies__mutmut_29(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = str(getattr(metadata, "namespace", "default"))
        spec = getattr(policy, "XXspecXX", None)
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


def x__build_edges_from_policies__mutmut_30(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = str(getattr(metadata, "namespace", "default"))
        spec = getattr(policy, "SPEC", None)
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


def x__build_edges_from_policies__mutmut_31(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = str(getattr(metadata, "namespace", "default"))
        spec = getattr(policy, "spec", None)
        callees = None

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


def x__build_edges_from_policies__mutmut_32(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = str(getattr(metadata, "namespace", "default"))
        spec = getattr(policy, "spec", None)
        callees = _match_services(None, policy_namespace, selectors)

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


def x__build_edges_from_policies__mutmut_33(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = str(getattr(metadata, "namespace", "default"))
        spec = getattr(policy, "spec", None)
        callees = _match_services(getattr(spec, "pod_selector", None), None, selectors)

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


def x__build_edges_from_policies__mutmut_34(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = str(getattr(metadata, "namespace", "default"))
        spec = getattr(policy, "spec", None)
        callees = _match_services(getattr(spec, "pod_selector", None), policy_namespace, None)

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


def x__build_edges_from_policies__mutmut_35(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = str(getattr(metadata, "namespace", "default"))
        spec = getattr(policy, "spec", None)
        callees = _match_services(policy_namespace, selectors)

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


def x__build_edges_from_policies__mutmut_36(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = str(getattr(metadata, "namespace", "default"))
        spec = getattr(policy, "spec", None)
        callees = _match_services(getattr(spec, "pod_selector", None), selectors)

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


def x__build_edges_from_policies__mutmut_37(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = str(getattr(metadata, "namespace", "default"))
        spec = getattr(policy, "spec", None)
        callees = _match_services(getattr(spec, "pod_selector", None), policy_namespace, )

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


def x__build_edges_from_policies__mutmut_38(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = str(getattr(metadata, "namespace", "default"))
        spec = getattr(policy, "spec", None)
        callees = _match_services(getattr(None, "pod_selector", None), policy_namespace, selectors)

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


def x__build_edges_from_policies__mutmut_39(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = str(getattr(metadata, "namespace", "default"))
        spec = getattr(policy, "spec", None)
        callees = _match_services(getattr(spec, None, None), policy_namespace, selectors)

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


def x__build_edges_from_policies__mutmut_40(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = str(getattr(metadata, "namespace", "default"))
        spec = getattr(policy, "spec", None)
        callees = _match_services(getattr("pod_selector", None), policy_namespace, selectors)

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


def x__build_edges_from_policies__mutmut_41(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = str(getattr(metadata, "namespace", "default"))
        spec = getattr(policy, "spec", None)
        callees = _match_services(getattr(spec, None), policy_namespace, selectors)

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


def x__build_edges_from_policies__mutmut_42(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = str(getattr(metadata, "namespace", "default"))
        spec = getattr(policy, "spec", None)
        callees = _match_services(getattr(spec, "pod_selector", ), policy_namespace, selectors)

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


def x__build_edges_from_policies__mutmut_43(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = str(getattr(metadata, "namespace", "default"))
        spec = getattr(policy, "spec", None)
        callees = _match_services(getattr(spec, "XXpod_selectorXX", None), policy_namespace, selectors)

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


def x__build_edges_from_policies__mutmut_44(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = str(getattr(metadata, "namespace", "default"))
        spec = getattr(policy, "spec", None)
        callees = _match_services(getattr(spec, "POD_SELECTOR", None), policy_namespace, selectors)

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


def x__build_edges_from_policies__mutmut_45(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = str(getattr(metadata, "namespace", "default"))
        spec = getattr(policy, "spec", None)
        callees = _match_services(getattr(spec, "pod_selector", None), policy_namespace, selectors)

        for ingress in getattr(spec, "ingress", None) and []:
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


def x__build_edges_from_policies__mutmut_46(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = str(getattr(metadata, "namespace", "default"))
        spec = getattr(policy, "spec", None)
        callees = _match_services(getattr(spec, "pod_selector", None), policy_namespace, selectors)

        for ingress in getattr(None, "ingress", None) or []:
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


def x__build_edges_from_policies__mutmut_47(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = str(getattr(metadata, "namespace", "default"))
        spec = getattr(policy, "spec", None)
        callees = _match_services(getattr(spec, "pod_selector", None), policy_namespace, selectors)

        for ingress in getattr(spec, None, None) or []:
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


def x__build_edges_from_policies__mutmut_48(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = str(getattr(metadata, "namespace", "default"))
        spec = getattr(policy, "spec", None)
        callees = _match_services(getattr(spec, "pod_selector", None), policy_namespace, selectors)

        for ingress in getattr("ingress", None) or []:
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


def x__build_edges_from_policies__mutmut_49(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = str(getattr(metadata, "namespace", "default"))
        spec = getattr(policy, "spec", None)
        callees = _match_services(getattr(spec, "pod_selector", None), policy_namespace, selectors)

        for ingress in getattr(spec, None) or []:
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


def x__build_edges_from_policies__mutmut_50(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = str(getattr(metadata, "namespace", "default"))
        spec = getattr(policy, "spec", None)
        callees = _match_services(getattr(spec, "pod_selector", None), policy_namespace, selectors)

        for ingress in getattr(spec, "ingress", ) or []:
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


def x__build_edges_from_policies__mutmut_51(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = str(getattr(metadata, "namespace", "default"))
        spec = getattr(policy, "spec", None)
        callees = _match_services(getattr(spec, "pod_selector", None), policy_namespace, selectors)

        for ingress in getattr(spec, "XXingressXX", None) or []:
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


def x__build_edges_from_policies__mutmut_52(
    policies: list[object], selectors: list[_ServiceSelector]
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for policy in policies:
        metadata = getattr(policy, "metadata", None)
        policy_namespace = str(getattr(metadata, "namespace", "default"))
        spec = getattr(policy, "spec", None)
        callees = _match_services(getattr(spec, "pod_selector", None), policy_namespace, selectors)

        for ingress in getattr(spec, "INGRESS", None) or []:
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


def x__build_edges_from_policies__mutmut_53(
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
            for peer in getattr(ingress, "_from", None) and []:
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


def x__build_edges_from_policies__mutmut_54(
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
            for peer in getattr(None, "_from", None) or []:
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


def x__build_edges_from_policies__mutmut_55(
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
            for peer in getattr(ingress, None, None) or []:
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


def x__build_edges_from_policies__mutmut_56(
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
            for peer in getattr("_from", None) or []:
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


def x__build_edges_from_policies__mutmut_57(
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
            for peer in getattr(ingress, None) or []:
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


def x__build_edges_from_policies__mutmut_58(
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
            for peer in getattr(ingress, "_from", ) or []:
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


def x__build_edges_from_policies__mutmut_59(
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
            for peer in getattr(ingress, "XX_fromXX", None) or []:
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


def x__build_edges_from_policies__mutmut_60(
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
            for peer in getattr(ingress, "_FROM", None) or []:
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


def x__build_edges_from_policies__mutmut_61(
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
                callers = None
                for caller in callers:
                    for callee in callees:
                        if caller == callee or (caller, callee) in seen:
                            continue
                        seen.add((caller, callee))
                        edges.append(EdgeRecordData(caller=caller, callee=callee))

    return edges


def x__build_edges_from_policies__mutmut_62(
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
                    None, policy_namespace, selectors
                )
                for caller in callers:
                    for callee in callees:
                        if caller == callee or (caller, callee) in seen:
                            continue
                        seen.add((caller, callee))
                        edges.append(EdgeRecordData(caller=caller, callee=callee))

    return edges


def x__build_edges_from_policies__mutmut_63(
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
                    getattr(peer, "pod_selector", None), None, selectors
                )
                for caller in callers:
                    for callee in callees:
                        if caller == callee or (caller, callee) in seen:
                            continue
                        seen.add((caller, callee))
                        edges.append(EdgeRecordData(caller=caller, callee=callee))

    return edges


def x__build_edges_from_policies__mutmut_64(
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
                    getattr(peer, "pod_selector", None), policy_namespace, None
                )
                for caller in callers:
                    for callee in callees:
                        if caller == callee or (caller, callee) in seen:
                            continue
                        seen.add((caller, callee))
                        edges.append(EdgeRecordData(caller=caller, callee=callee))

    return edges


def x__build_edges_from_policies__mutmut_65(
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
                    policy_namespace, selectors
                )
                for caller in callers:
                    for callee in callees:
                        if caller == callee or (caller, callee) in seen:
                            continue
                        seen.add((caller, callee))
                        edges.append(EdgeRecordData(caller=caller, callee=callee))

    return edges


def x__build_edges_from_policies__mutmut_66(
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
                    getattr(peer, "pod_selector", None), selectors
                )
                for caller in callers:
                    for callee in callees:
                        if caller == callee or (caller, callee) in seen:
                            continue
                        seen.add((caller, callee))
                        edges.append(EdgeRecordData(caller=caller, callee=callee))

    return edges


def x__build_edges_from_policies__mutmut_67(
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
                    getattr(peer, "pod_selector", None), policy_namespace, )
                for caller in callers:
                    for callee in callees:
                        if caller == callee or (caller, callee) in seen:
                            continue
                        seen.add((caller, callee))
                        edges.append(EdgeRecordData(caller=caller, callee=callee))

    return edges


def x__build_edges_from_policies__mutmut_68(
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
                    getattr(None, "pod_selector", None), policy_namespace, selectors
                )
                for caller in callers:
                    for callee in callees:
                        if caller == callee or (caller, callee) in seen:
                            continue
                        seen.add((caller, callee))
                        edges.append(EdgeRecordData(caller=caller, callee=callee))

    return edges


def x__build_edges_from_policies__mutmut_69(
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
                    getattr(peer, None, None), policy_namespace, selectors
                )
                for caller in callers:
                    for callee in callees:
                        if caller == callee or (caller, callee) in seen:
                            continue
                        seen.add((caller, callee))
                        edges.append(EdgeRecordData(caller=caller, callee=callee))

    return edges


def x__build_edges_from_policies__mutmut_70(
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
                    getattr("pod_selector", None), policy_namespace, selectors
                )
                for caller in callers:
                    for callee in callees:
                        if caller == callee or (caller, callee) in seen:
                            continue
                        seen.add((caller, callee))
                        edges.append(EdgeRecordData(caller=caller, callee=callee))

    return edges


def x__build_edges_from_policies__mutmut_71(
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
                    getattr(peer, None), policy_namespace, selectors
                )
                for caller in callers:
                    for callee in callees:
                        if caller == callee or (caller, callee) in seen:
                            continue
                        seen.add((caller, callee))
                        edges.append(EdgeRecordData(caller=caller, callee=callee))

    return edges


def x__build_edges_from_policies__mutmut_72(
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
                    getattr(peer, "pod_selector", ), policy_namespace, selectors
                )
                for caller in callers:
                    for callee in callees:
                        if caller == callee or (caller, callee) in seen:
                            continue
                        seen.add((caller, callee))
                        edges.append(EdgeRecordData(caller=caller, callee=callee))

    return edges


def x__build_edges_from_policies__mutmut_73(
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
                    getattr(peer, "XXpod_selectorXX", None), policy_namespace, selectors
                )
                for caller in callers:
                    for callee in callees:
                        if caller == callee or (caller, callee) in seen:
                            continue
                        seen.add((caller, callee))
                        edges.append(EdgeRecordData(caller=caller, callee=callee))

    return edges


def x__build_edges_from_policies__mutmut_74(
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
                    getattr(peer, "POD_SELECTOR", None), policy_namespace, selectors
                )
                for caller in callers:
                    for callee in callees:
                        if caller == callee or (caller, callee) in seen:
                            continue
                        seen.add((caller, callee))
                        edges.append(EdgeRecordData(caller=caller, callee=callee))

    return edges


def x__build_edges_from_policies__mutmut_75(
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
                        if caller == callee and (caller, callee) in seen:
                            continue
                        seen.add((caller, callee))
                        edges.append(EdgeRecordData(caller=caller, callee=callee))

    return edges


def x__build_edges_from_policies__mutmut_76(
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
                        if caller != callee or (caller, callee) in seen:
                            continue
                        seen.add((caller, callee))
                        edges.append(EdgeRecordData(caller=caller, callee=callee))

    return edges


def x__build_edges_from_policies__mutmut_77(
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
                        if caller == callee or (caller, callee) not in seen:
                            continue
                        seen.add((caller, callee))
                        edges.append(EdgeRecordData(caller=caller, callee=callee))

    return edges


def x__build_edges_from_policies__mutmut_78(
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
                            break
                        seen.add((caller, callee))
                        edges.append(EdgeRecordData(caller=caller, callee=callee))

    return edges


def x__build_edges_from_policies__mutmut_79(
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
                        seen.add(None)
                        edges.append(EdgeRecordData(caller=caller, callee=callee))

    return edges


def x__build_edges_from_policies__mutmut_80(
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
                        edges.append(None)

    return edges


def x__build_edges_from_policies__mutmut_81(
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
                        edges.append(EdgeRecordData(caller=None, callee=callee))

    return edges


def x__build_edges_from_policies__mutmut_82(
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
                        edges.append(EdgeRecordData(caller=caller, callee=None))

    return edges


def x__build_edges_from_policies__mutmut_83(
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
                        edges.append(EdgeRecordData(callee=callee))

    return edges


def x__build_edges_from_policies__mutmut_84(
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
                        edges.append(EdgeRecordData(caller=caller, ))

    return edges

mutants_x__build_edges_from_policies__mutmut['_mutmut_orig'] = x__build_edges_from_policies__mutmut_orig # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_1'] = x__build_edges_from_policies__mutmut_1 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_2'] = x__build_edges_from_policies__mutmut_2 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_3'] = x__build_edges_from_policies__mutmut_3 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_4'] = x__build_edges_from_policies__mutmut_4 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_5'] = x__build_edges_from_policies__mutmut_5 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_6'] = x__build_edges_from_policies__mutmut_6 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_7'] = x__build_edges_from_policies__mutmut_7 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_8'] = x__build_edges_from_policies__mutmut_8 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_9'] = x__build_edges_from_policies__mutmut_9 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_10'] = x__build_edges_from_policies__mutmut_10 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_11'] = x__build_edges_from_policies__mutmut_11 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_12'] = x__build_edges_from_policies__mutmut_12 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_13'] = x__build_edges_from_policies__mutmut_13 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_14'] = x__build_edges_from_policies__mutmut_14 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_15'] = x__build_edges_from_policies__mutmut_15 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_16'] = x__build_edges_from_policies__mutmut_16 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_17'] = x__build_edges_from_policies__mutmut_17 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_18'] = x__build_edges_from_policies__mutmut_18 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_19'] = x__build_edges_from_policies__mutmut_19 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_20'] = x__build_edges_from_policies__mutmut_20 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_21'] = x__build_edges_from_policies__mutmut_21 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_22'] = x__build_edges_from_policies__mutmut_22 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_23'] = x__build_edges_from_policies__mutmut_23 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_24'] = x__build_edges_from_policies__mutmut_24 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_25'] = x__build_edges_from_policies__mutmut_25 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_26'] = x__build_edges_from_policies__mutmut_26 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_27'] = x__build_edges_from_policies__mutmut_27 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_28'] = x__build_edges_from_policies__mutmut_28 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_29'] = x__build_edges_from_policies__mutmut_29 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_30'] = x__build_edges_from_policies__mutmut_30 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_31'] = x__build_edges_from_policies__mutmut_31 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_32'] = x__build_edges_from_policies__mutmut_32 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_33'] = x__build_edges_from_policies__mutmut_33 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_34'] = x__build_edges_from_policies__mutmut_34 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_35'] = x__build_edges_from_policies__mutmut_35 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_36'] = x__build_edges_from_policies__mutmut_36 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_37'] = x__build_edges_from_policies__mutmut_37 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_38'] = x__build_edges_from_policies__mutmut_38 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_39'] = x__build_edges_from_policies__mutmut_39 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_40'] = x__build_edges_from_policies__mutmut_40 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_41'] = x__build_edges_from_policies__mutmut_41 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_42'] = x__build_edges_from_policies__mutmut_42 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_43'] = x__build_edges_from_policies__mutmut_43 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_44'] = x__build_edges_from_policies__mutmut_44 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_45'] = x__build_edges_from_policies__mutmut_45 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_46'] = x__build_edges_from_policies__mutmut_46 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_47'] = x__build_edges_from_policies__mutmut_47 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_48'] = x__build_edges_from_policies__mutmut_48 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_49'] = x__build_edges_from_policies__mutmut_49 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_50'] = x__build_edges_from_policies__mutmut_50 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_51'] = x__build_edges_from_policies__mutmut_51 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_52'] = x__build_edges_from_policies__mutmut_52 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_53'] = x__build_edges_from_policies__mutmut_53 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_54'] = x__build_edges_from_policies__mutmut_54 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_55'] = x__build_edges_from_policies__mutmut_55 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_56'] = x__build_edges_from_policies__mutmut_56 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_57'] = x__build_edges_from_policies__mutmut_57 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_58'] = x__build_edges_from_policies__mutmut_58 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_59'] = x__build_edges_from_policies__mutmut_59 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_60'] = x__build_edges_from_policies__mutmut_60 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_61'] = x__build_edges_from_policies__mutmut_61 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_62'] = x__build_edges_from_policies__mutmut_62 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_63'] = x__build_edges_from_policies__mutmut_63 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_64'] = x__build_edges_from_policies__mutmut_64 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_65'] = x__build_edges_from_policies__mutmut_65 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_66'] = x__build_edges_from_policies__mutmut_66 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_67'] = x__build_edges_from_policies__mutmut_67 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_68'] = x__build_edges_from_policies__mutmut_68 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_69'] = x__build_edges_from_policies__mutmut_69 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_70'] = x__build_edges_from_policies__mutmut_70 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_71'] = x__build_edges_from_policies__mutmut_71 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_72'] = x__build_edges_from_policies__mutmut_72 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_73'] = x__build_edges_from_policies__mutmut_73 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_74'] = x__build_edges_from_policies__mutmut_74 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_75'] = x__build_edges_from_policies__mutmut_75 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_76'] = x__build_edges_from_policies__mutmut_76 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_77'] = x__build_edges_from_policies__mutmut_77 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_78'] = x__build_edges_from_policies__mutmut_78 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_79'] = x__build_edges_from_policies__mutmut_79 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_80'] = x__build_edges_from_policies__mutmut_80 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_81'] = x__build_edges_from_policies__mutmut_81 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_82'] = x__build_edges_from_policies__mutmut_82 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_83'] = x__build_edges_from_policies__mutmut_83 # type: ignore # mutmut generated
mutants_x__build_edges_from_policies__mutmut['x__build_edges_from_policies__mutmut_84'] = x__build_edges_from_policies__mutmut_84 # type: ignore # mutmut generated
mutants_x__match_services__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__match_services__mutmut)
def _match_services(
    pod_selector: object, namespace: str, selectors: list[_ServiceSelector]
) -> list[str]:
    match_labels = getattr(pod_selector, "match_labels", None) or {}
    app_label = match_labels.get("app") if isinstance(match_labels, dict) else None
    if not app_label:
        return []
    return [s.name for s in selectors if s.namespace == namespace and s.app_label == app_label]


def x__match_services__mutmut_orig(
    pod_selector: object, namespace: str, selectors: list[_ServiceSelector]
) -> list[str]:
    match_labels = getattr(pod_selector, "match_labels", None) or {}
    app_label = match_labels.get("app") if isinstance(match_labels, dict) else None
    if not app_label:
        return []
    return [s.name for s in selectors if s.namespace == namespace and s.app_label == app_label]


def x__match_services__mutmut_1(
    pod_selector: object, namespace: str, selectors: list[_ServiceSelector]
) -> list[str]:
    match_labels = None
    app_label = match_labels.get("app") if isinstance(match_labels, dict) else None
    if not app_label:
        return []
    return [s.name for s in selectors if s.namespace == namespace and s.app_label == app_label]


def x__match_services__mutmut_2(
    pod_selector: object, namespace: str, selectors: list[_ServiceSelector]
) -> list[str]:
    match_labels = getattr(pod_selector, "match_labels", None) and {}
    app_label = match_labels.get("app") if isinstance(match_labels, dict) else None
    if not app_label:
        return []
    return [s.name for s in selectors if s.namespace == namespace and s.app_label == app_label]


def x__match_services__mutmut_3(
    pod_selector: object, namespace: str, selectors: list[_ServiceSelector]
) -> list[str]:
    match_labels = getattr(None, "match_labels", None) or {}
    app_label = match_labels.get("app") if isinstance(match_labels, dict) else None
    if not app_label:
        return []
    return [s.name for s in selectors if s.namespace == namespace and s.app_label == app_label]


def x__match_services__mutmut_4(
    pod_selector: object, namespace: str, selectors: list[_ServiceSelector]
) -> list[str]:
    match_labels = getattr(pod_selector, None, None) or {}
    app_label = match_labels.get("app") if isinstance(match_labels, dict) else None
    if not app_label:
        return []
    return [s.name for s in selectors if s.namespace == namespace and s.app_label == app_label]


def x__match_services__mutmut_5(
    pod_selector: object, namespace: str, selectors: list[_ServiceSelector]
) -> list[str]:
    match_labels = getattr("match_labels", None) or {}
    app_label = match_labels.get("app") if isinstance(match_labels, dict) else None
    if not app_label:
        return []
    return [s.name for s in selectors if s.namespace == namespace and s.app_label == app_label]


def x__match_services__mutmut_6(
    pod_selector: object, namespace: str, selectors: list[_ServiceSelector]
) -> list[str]:
    match_labels = getattr(pod_selector, None) or {}
    app_label = match_labels.get("app") if isinstance(match_labels, dict) else None
    if not app_label:
        return []
    return [s.name for s in selectors if s.namespace == namespace and s.app_label == app_label]


def x__match_services__mutmut_7(
    pod_selector: object, namespace: str, selectors: list[_ServiceSelector]
) -> list[str]:
    match_labels = getattr(pod_selector, "match_labels", ) or {}
    app_label = match_labels.get("app") if isinstance(match_labels, dict) else None
    if not app_label:
        return []
    return [s.name for s in selectors if s.namespace == namespace and s.app_label == app_label]


def x__match_services__mutmut_8(
    pod_selector: object, namespace: str, selectors: list[_ServiceSelector]
) -> list[str]:
    match_labels = getattr(pod_selector, "XXmatch_labelsXX", None) or {}
    app_label = match_labels.get("app") if isinstance(match_labels, dict) else None
    if not app_label:
        return []
    return [s.name for s in selectors if s.namespace == namespace and s.app_label == app_label]


def x__match_services__mutmut_9(
    pod_selector: object, namespace: str, selectors: list[_ServiceSelector]
) -> list[str]:
    match_labels = getattr(pod_selector, "MATCH_LABELS", None) or {}
    app_label = match_labels.get("app") if isinstance(match_labels, dict) else None
    if not app_label:
        return []
    return [s.name for s in selectors if s.namespace == namespace and s.app_label == app_label]


def x__match_services__mutmut_10(
    pod_selector: object, namespace: str, selectors: list[_ServiceSelector]
) -> list[str]:
    match_labels = getattr(pod_selector, "match_labels", None) or {}
    app_label = None
    if not app_label:
        return []
    return [s.name for s in selectors if s.namespace == namespace and s.app_label == app_label]


def x__match_services__mutmut_11(
    pod_selector: object, namespace: str, selectors: list[_ServiceSelector]
) -> list[str]:
    match_labels = getattr(pod_selector, "match_labels", None) or {}
    app_label = match_labels.get(None) if isinstance(match_labels, dict) else None
    if not app_label:
        return []
    return [s.name for s in selectors if s.namespace == namespace and s.app_label == app_label]


def x__match_services__mutmut_12(
    pod_selector: object, namespace: str, selectors: list[_ServiceSelector]
) -> list[str]:
    match_labels = getattr(pod_selector, "match_labels", None) or {}
    app_label = match_labels.get("XXappXX") if isinstance(match_labels, dict) else None
    if not app_label:
        return []
    return [s.name for s in selectors if s.namespace == namespace and s.app_label == app_label]


def x__match_services__mutmut_13(
    pod_selector: object, namespace: str, selectors: list[_ServiceSelector]
) -> list[str]:
    match_labels = getattr(pod_selector, "match_labels", None) or {}
    app_label = match_labels.get("APP") if isinstance(match_labels, dict) else None
    if not app_label:
        return []
    return [s.name for s in selectors if s.namespace == namespace and s.app_label == app_label]


def x__match_services__mutmut_14(
    pod_selector: object, namespace: str, selectors: list[_ServiceSelector]
) -> list[str]:
    match_labels = getattr(pod_selector, "match_labels", None) or {}
    app_label = match_labels.get("app") if isinstance(match_labels, dict) else None
    if app_label:
        return []
    return [s.name for s in selectors if s.namespace == namespace and s.app_label == app_label]


def x__match_services__mutmut_15(
    pod_selector: object, namespace: str, selectors: list[_ServiceSelector]
) -> list[str]:
    match_labels = getattr(pod_selector, "match_labels", None) or {}
    app_label = match_labels.get("app") if isinstance(match_labels, dict) else None
    if not app_label:
        return []
    return [s.name for s in selectors if s.namespace == namespace or s.app_label == app_label]


def x__match_services__mutmut_16(
    pod_selector: object, namespace: str, selectors: list[_ServiceSelector]
) -> list[str]:
    match_labels = getattr(pod_selector, "match_labels", None) or {}
    app_label = match_labels.get("app") if isinstance(match_labels, dict) else None
    if not app_label:
        return []
    return [s.name for s in selectors if s.namespace != namespace and s.app_label == app_label]


def x__match_services__mutmut_17(
    pod_selector: object, namespace: str, selectors: list[_ServiceSelector]
) -> list[str]:
    match_labels = getattr(pod_selector, "match_labels", None) or {}
    app_label = match_labels.get("app") if isinstance(match_labels, dict) else None
    if not app_label:
        return []
    return [s.name for s in selectors if s.namespace == namespace and s.app_label != app_label]

mutants_x__match_services__mutmut['_mutmut_orig'] = x__match_services__mutmut_orig # type: ignore # mutmut generated
mutants_x__match_services__mutmut['x__match_services__mutmut_1'] = x__match_services__mutmut_1 # type: ignore # mutmut generated
mutants_x__match_services__mutmut['x__match_services__mutmut_2'] = x__match_services__mutmut_2 # type: ignore # mutmut generated
mutants_x__match_services__mutmut['x__match_services__mutmut_3'] = x__match_services__mutmut_3 # type: ignore # mutmut generated
mutants_x__match_services__mutmut['x__match_services__mutmut_4'] = x__match_services__mutmut_4 # type: ignore # mutmut generated
mutants_x__match_services__mutmut['x__match_services__mutmut_5'] = x__match_services__mutmut_5 # type: ignore # mutmut generated
mutants_x__match_services__mutmut['x__match_services__mutmut_6'] = x__match_services__mutmut_6 # type: ignore # mutmut generated
mutants_x__match_services__mutmut['x__match_services__mutmut_7'] = x__match_services__mutmut_7 # type: ignore # mutmut generated
mutants_x__match_services__mutmut['x__match_services__mutmut_8'] = x__match_services__mutmut_8 # type: ignore # mutmut generated
mutants_x__match_services__mutmut['x__match_services__mutmut_9'] = x__match_services__mutmut_9 # type: ignore # mutmut generated
mutants_x__match_services__mutmut['x__match_services__mutmut_10'] = x__match_services__mutmut_10 # type: ignore # mutmut generated
mutants_x__match_services__mutmut['x__match_services__mutmut_11'] = x__match_services__mutmut_11 # type: ignore # mutmut generated
mutants_x__match_services__mutmut['x__match_services__mutmut_12'] = x__match_services__mutmut_12 # type: ignore # mutmut generated
mutants_x__match_services__mutmut['x__match_services__mutmut_13'] = x__match_services__mutmut_13 # type: ignore # mutmut generated
mutants_x__match_services__mutmut['x__match_services__mutmut_14'] = x__match_services__mutmut_14 # type: ignore # mutmut generated
mutants_x__match_services__mutmut['x__match_services__mutmut_15'] = x__match_services__mutmut_15 # type: ignore # mutmut generated
mutants_x__match_services__mutmut['x__match_services__mutmut_16'] = x__match_services__mutmut_16 # type: ignore # mutmut generated
mutants_x__match_services__mutmut['x__match_services__mutmut_17'] = x__match_services__mutmut_17 # type: ignore # mutmut generated
