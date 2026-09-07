"""IstioTopologyAdapter — infers edges from Istio VirtualService CRDs (best-effort)."""

from __future__ import annotations

from typing import Protocol, cast

from hexawyn.application.ports.driven.istio_topology_port import IstioTopologyPort
from hexawyn.application.ports.driven.kubernetes_topology_port import EdgeRecordData

_ISTIO_GROUP = "networking.istio.io"
_ISTIO_VERSION = "v1beta1"
_VIRTUAL_SERVICES_PLURAL = "virtualservices"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class _CustomObjectsApi(Protocol):
    def list_cluster_custom_object(self, group: str, version: str, plural: str) -> object:
        """List cluster-scoped custom objects."""

    def list_namespaced_custom_object(
        self, group: str, version: str, namespace: str, plural: str
    ) -> object:
        """List namespace-scoped custom objects."""
mutants_xǁIstioTopologyAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁIstioTopologyAdapterǁget_virtual_service_edges__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIstioTopologyAdapterǁ_crd_api_client__mutmut: MutantDict = {}  # type: ignore


class IstioTopologyAdapter(IstioTopologyPort):
    @_mutmut_mutated(mutants_xǁIstioTopologyAdapterǁ__init____mutmut)
    def __init__(self, crd_api: _CustomObjectsApi | None = None) -> None:
        self._crd_api = crd_api
    def xǁIstioTopologyAdapterǁ__init____mutmut_orig(self, crd_api: _CustomObjectsApi | None = None) -> None:
        self._crd_api = crd_api
    def xǁIstioTopologyAdapterǁ__init____mutmut_1(self, crd_api: _CustomObjectsApi | None = None) -> None:
        self._crd_api = None

    # ── IstioTopologyPort ─────────────────────────────────────

    @_mutmut_mutated(mutants_xǁIstioTopologyAdapterǁget_virtual_service_edges__mutmut)
    def get_virtual_service_edges(self, namespace: str | None) -> list[EdgeRecordData] | None:
        try:
            raw = self._fetch_virtual_services(namespace)
        except Exception:
            return None
        return _build_edges_from_virtual_services(_items(raw))

    # ── IstioTopologyPort ─────────────────────────────────────

    def xǁIstioTopologyAdapterǁget_virtual_service_edges__mutmut_orig(self, namespace: str | None) -> list[EdgeRecordData] | None:
        try:
            raw = self._fetch_virtual_services(namespace)
        except Exception:
            return None
        return _build_edges_from_virtual_services(_items(raw))

    # ── IstioTopologyPort ─────────────────────────────────────

    def xǁIstioTopologyAdapterǁget_virtual_service_edges__mutmut_1(self, namespace: str | None) -> list[EdgeRecordData] | None:
        try:
            raw = None
        except Exception:
            return None
        return _build_edges_from_virtual_services(_items(raw))

    # ── IstioTopologyPort ─────────────────────────────────────

    def xǁIstioTopologyAdapterǁget_virtual_service_edges__mutmut_2(self, namespace: str | None) -> list[EdgeRecordData] | None:
        try:
            raw = self._fetch_virtual_services(None)
        except Exception:
            return None
        return _build_edges_from_virtual_services(_items(raw))

    # ── IstioTopologyPort ─────────────────────────────────────

    def xǁIstioTopologyAdapterǁget_virtual_service_edges__mutmut_3(self, namespace: str | None) -> list[EdgeRecordData] | None:
        try:
            raw = self._fetch_virtual_services(namespace)
        except Exception:
            return None
        return _build_edges_from_virtual_services(None)

    # ── IstioTopologyPort ─────────────────────────────────────

    def xǁIstioTopologyAdapterǁget_virtual_service_edges__mutmut_4(self, namespace: str | None) -> list[EdgeRecordData] | None:
        try:
            raw = self._fetch_virtual_services(namespace)
        except Exception:
            return None
        return _build_edges_from_virtual_services(_items(None))

    # ── Internal ───────────────────────────────────────────────

    @_mutmut_mutated(mutants_xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut)
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

    # ── Internal ───────────────────────────────────────────────

    def xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_orig(self, namespace: str | None) -> object:
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

    # ── Internal ───────────────────────────────────────────────

    def xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_1(self, namespace: str | None) -> object:
        api = None
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

    # ── Internal ───────────────────────────────────────────────

    def xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_2(self, namespace: str | None) -> object:
        api = self._crd_api_client()
        if namespace:
            return api.list_namespaced_custom_object(
                group=None,
                version=_ISTIO_VERSION,
                namespace=namespace,
                plural=_VIRTUAL_SERVICES_PLURAL,
            )
        return api.list_cluster_custom_object(
            group=_ISTIO_GROUP,
            version=_ISTIO_VERSION,
            plural=_VIRTUAL_SERVICES_PLURAL,
        )

    # ── Internal ───────────────────────────────────────────────

    def xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_3(self, namespace: str | None) -> object:
        api = self._crd_api_client()
        if namespace:
            return api.list_namespaced_custom_object(
                group=_ISTIO_GROUP,
                version=None,
                namespace=namespace,
                plural=_VIRTUAL_SERVICES_PLURAL,
            )
        return api.list_cluster_custom_object(
            group=_ISTIO_GROUP,
            version=_ISTIO_VERSION,
            plural=_VIRTUAL_SERVICES_PLURAL,
        )

    # ── Internal ───────────────────────────────────────────────

    def xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_4(self, namespace: str | None) -> object:
        api = self._crd_api_client()
        if namespace:
            return api.list_namespaced_custom_object(
                group=_ISTIO_GROUP,
                version=_ISTIO_VERSION,
                namespace=None,
                plural=_VIRTUAL_SERVICES_PLURAL,
            )
        return api.list_cluster_custom_object(
            group=_ISTIO_GROUP,
            version=_ISTIO_VERSION,
            plural=_VIRTUAL_SERVICES_PLURAL,
        )

    # ── Internal ───────────────────────────────────────────────

    def xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_5(self, namespace: str | None) -> object:
        api = self._crd_api_client()
        if namespace:
            return api.list_namespaced_custom_object(
                group=_ISTIO_GROUP,
                version=_ISTIO_VERSION,
                namespace=namespace,
                plural=None,
            )
        return api.list_cluster_custom_object(
            group=_ISTIO_GROUP,
            version=_ISTIO_VERSION,
            plural=_VIRTUAL_SERVICES_PLURAL,
        )

    # ── Internal ───────────────────────────────────────────────

    def xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_6(self, namespace: str | None) -> object:
        api = self._crd_api_client()
        if namespace:
            return api.list_namespaced_custom_object(
                version=_ISTIO_VERSION,
                namespace=namespace,
                plural=_VIRTUAL_SERVICES_PLURAL,
            )
        return api.list_cluster_custom_object(
            group=_ISTIO_GROUP,
            version=_ISTIO_VERSION,
            plural=_VIRTUAL_SERVICES_PLURAL,
        )

    # ── Internal ───────────────────────────────────────────────

    def xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_7(self, namespace: str | None) -> object:
        api = self._crd_api_client()
        if namespace:
            return api.list_namespaced_custom_object(
                group=_ISTIO_GROUP,
                namespace=namespace,
                plural=_VIRTUAL_SERVICES_PLURAL,
            )
        return api.list_cluster_custom_object(
            group=_ISTIO_GROUP,
            version=_ISTIO_VERSION,
            plural=_VIRTUAL_SERVICES_PLURAL,
        )

    # ── Internal ───────────────────────────────────────────────

    def xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_8(self, namespace: str | None) -> object:
        api = self._crd_api_client()
        if namespace:
            return api.list_namespaced_custom_object(
                group=_ISTIO_GROUP,
                version=_ISTIO_VERSION,
                plural=_VIRTUAL_SERVICES_PLURAL,
            )
        return api.list_cluster_custom_object(
            group=_ISTIO_GROUP,
            version=_ISTIO_VERSION,
            plural=_VIRTUAL_SERVICES_PLURAL,
        )

    # ── Internal ───────────────────────────────────────────────

    def xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_9(self, namespace: str | None) -> object:
        api = self._crd_api_client()
        if namespace:
            return api.list_namespaced_custom_object(
                group=_ISTIO_GROUP,
                version=_ISTIO_VERSION,
                namespace=namespace,
                )
        return api.list_cluster_custom_object(
            group=_ISTIO_GROUP,
            version=_ISTIO_VERSION,
            plural=_VIRTUAL_SERVICES_PLURAL,
        )

    # ── Internal ───────────────────────────────────────────────

    def xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_10(self, namespace: str | None) -> object:
        api = self._crd_api_client()
        if namespace:
            return api.list_namespaced_custom_object(
                group=_ISTIO_GROUP,
                version=_ISTIO_VERSION,
                namespace=namespace,
                plural=_VIRTUAL_SERVICES_PLURAL,
            )
        return api.list_cluster_custom_object(
            group=None,
            version=_ISTIO_VERSION,
            plural=_VIRTUAL_SERVICES_PLURAL,
        )

    # ── Internal ───────────────────────────────────────────────

    def xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_11(self, namespace: str | None) -> object:
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
            version=None,
            plural=_VIRTUAL_SERVICES_PLURAL,
        )

    # ── Internal ───────────────────────────────────────────────

    def xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_12(self, namespace: str | None) -> object:
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
            plural=None,
        )

    # ── Internal ───────────────────────────────────────────────

    def xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_13(self, namespace: str | None) -> object:
        api = self._crd_api_client()
        if namespace:
            return api.list_namespaced_custom_object(
                group=_ISTIO_GROUP,
                version=_ISTIO_VERSION,
                namespace=namespace,
                plural=_VIRTUAL_SERVICES_PLURAL,
            )
        return api.list_cluster_custom_object(
            version=_ISTIO_VERSION,
            plural=_VIRTUAL_SERVICES_PLURAL,
        )

    # ── Internal ───────────────────────────────────────────────

    def xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_14(self, namespace: str | None) -> object:
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
            plural=_VIRTUAL_SERVICES_PLURAL,
        )

    # ── Internal ───────────────────────────────────────────────

    def xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_15(self, namespace: str | None) -> object:
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
            )

    @_mutmut_mutated(mutants_xǁIstioTopologyAdapterǁ_crd_api_client__mutmut)
    def _crd_api_client(self) -> _CustomObjectsApi:
        if self._crd_api is None:
            from kubernetes import client

            self._crd_api = cast(_CustomObjectsApi, client.CustomObjectsApi())
        return self._crd_api

    def xǁIstioTopologyAdapterǁ_crd_api_client__mutmut_orig(self) -> _CustomObjectsApi:
        if self._crd_api is None:
            from kubernetes import client

            self._crd_api = cast(_CustomObjectsApi, client.CustomObjectsApi())
        return self._crd_api

    def xǁIstioTopologyAdapterǁ_crd_api_client__mutmut_1(self) -> _CustomObjectsApi:
        if self._crd_api is not None:
            from kubernetes import client

            self._crd_api = cast(_CustomObjectsApi, client.CustomObjectsApi())
        return self._crd_api

    def xǁIstioTopologyAdapterǁ_crd_api_client__mutmut_2(self) -> _CustomObjectsApi:
        if self._crd_api is None:
            from kubernetes import client

            self._crd_api = None
        return self._crd_api

    def xǁIstioTopologyAdapterǁ_crd_api_client__mutmut_3(self) -> _CustomObjectsApi:
        if self._crd_api is None:
            from kubernetes import client

            self._crd_api = cast(None, client.CustomObjectsApi())
        return self._crd_api

    def xǁIstioTopologyAdapterǁ_crd_api_client__mutmut_4(self) -> _CustomObjectsApi:
        if self._crd_api is None:
            from kubernetes import client

            self._crd_api = cast(_CustomObjectsApi, None)
        return self._crd_api

    def xǁIstioTopologyAdapterǁ_crd_api_client__mutmut_5(self) -> _CustomObjectsApi:
        if self._crd_api is None:
            from kubernetes import client

            self._crd_api = cast(client.CustomObjectsApi())
        return self._crd_api

    def xǁIstioTopologyAdapterǁ_crd_api_client__mutmut_6(self) -> _CustomObjectsApi:
        if self._crd_api is None:
            from kubernetes import client

            self._crd_api = cast(_CustomObjectsApi, )
        return self._crd_api

mutants_xǁIstioTopologyAdapterǁ__init____mutmut['_mutmut_orig'] = IstioTopologyAdapter.xǁIstioTopologyAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁIstioTopologyAdapterǁ__init____mutmut['xǁIstioTopologyAdapterǁ__init____mutmut_1'] = IstioTopologyAdapter.xǁIstioTopologyAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁIstioTopologyAdapterǁget_virtual_service_edges__mutmut['_mutmut_orig'] = IstioTopologyAdapter.xǁIstioTopologyAdapterǁget_virtual_service_edges__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIstioTopologyAdapterǁget_virtual_service_edges__mutmut['xǁIstioTopologyAdapterǁget_virtual_service_edges__mutmut_1'] = IstioTopologyAdapter.xǁIstioTopologyAdapterǁget_virtual_service_edges__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIstioTopologyAdapterǁget_virtual_service_edges__mutmut['xǁIstioTopologyAdapterǁget_virtual_service_edges__mutmut_2'] = IstioTopologyAdapter.xǁIstioTopologyAdapterǁget_virtual_service_edges__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIstioTopologyAdapterǁget_virtual_service_edges__mutmut['xǁIstioTopologyAdapterǁget_virtual_service_edges__mutmut_3'] = IstioTopologyAdapter.xǁIstioTopologyAdapterǁget_virtual_service_edges__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIstioTopologyAdapterǁget_virtual_service_edges__mutmut['xǁIstioTopologyAdapterǁget_virtual_service_edges__mutmut_4'] = IstioTopologyAdapter.xǁIstioTopologyAdapterǁget_virtual_service_edges__mutmut_4 # type: ignore # mutmut generated

mutants_xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut['_mutmut_orig'] = IstioTopologyAdapter.xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut['xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_1'] = IstioTopologyAdapter.xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut['xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_2'] = IstioTopologyAdapter.xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut['xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_3'] = IstioTopologyAdapter.xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut['xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_4'] = IstioTopologyAdapter.xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut['xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_5'] = IstioTopologyAdapter.xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut['xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_6'] = IstioTopologyAdapter.xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut['xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_7'] = IstioTopologyAdapter.xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut['xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_8'] = IstioTopologyAdapter.xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut['xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_9'] = IstioTopologyAdapter.xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut['xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_10'] = IstioTopologyAdapter.xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut['xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_11'] = IstioTopologyAdapter.xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_11 # type: ignore # mutmut generated
mutants_xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut['xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_12'] = IstioTopologyAdapter.xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_12 # type: ignore # mutmut generated
mutants_xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut['xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_13'] = IstioTopologyAdapter.xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_13 # type: ignore # mutmut generated
mutants_xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut['xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_14'] = IstioTopologyAdapter.xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_14 # type: ignore # mutmut generated
mutants_xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut['xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_15'] = IstioTopologyAdapter.xǁIstioTopologyAdapterǁ_fetch_virtual_services__mutmut_15 # type: ignore # mutmut generated

mutants_xǁIstioTopologyAdapterǁ_crd_api_client__mutmut['_mutmut_orig'] = IstioTopologyAdapter.xǁIstioTopologyAdapterǁ_crd_api_client__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIstioTopologyAdapterǁ_crd_api_client__mutmut['xǁIstioTopologyAdapterǁ_crd_api_client__mutmut_1'] = IstioTopologyAdapter.xǁIstioTopologyAdapterǁ_crd_api_client__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIstioTopologyAdapterǁ_crd_api_client__mutmut['xǁIstioTopologyAdapterǁ_crd_api_client__mutmut_2'] = IstioTopologyAdapter.xǁIstioTopologyAdapterǁ_crd_api_client__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIstioTopologyAdapterǁ_crd_api_client__mutmut['xǁIstioTopologyAdapterǁ_crd_api_client__mutmut_3'] = IstioTopologyAdapter.xǁIstioTopologyAdapterǁ_crd_api_client__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIstioTopologyAdapterǁ_crd_api_client__mutmut['xǁIstioTopologyAdapterǁ_crd_api_client__mutmut_4'] = IstioTopologyAdapter.xǁIstioTopologyAdapterǁ_crd_api_client__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIstioTopologyAdapterǁ_crd_api_client__mutmut['xǁIstioTopologyAdapterǁ_crd_api_client__mutmut_5'] = IstioTopologyAdapter.xǁIstioTopologyAdapterǁ_crd_api_client__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIstioTopologyAdapterǁ_crd_api_client__mutmut['xǁIstioTopologyAdapterǁ_crd_api_client__mutmut_6'] = IstioTopologyAdapter.xǁIstioTopologyAdapterǁ_crd_api_client__mutmut_6 # type: ignore # mutmut generated
mutants_x__items__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__items__mutmut)
def _items(raw: object) -> list[dict[str, object]]:
    if not isinstance(raw, dict):
        return []
    items = raw.get("items", [])
    if not isinstance(items, list):
        return []
    return [item for item in items if isinstance(item, dict)]


def x__items__mutmut_orig(raw: object) -> list[dict[str, object]]:
    if not isinstance(raw, dict):
        return []
    items = raw.get("items", [])
    if not isinstance(items, list):
        return []
    return [item for item in items if isinstance(item, dict)]


def x__items__mutmut_1(raw: object) -> list[dict[str, object]]:
    if isinstance(raw, dict):
        return []
    items = raw.get("items", [])
    if not isinstance(items, list):
        return []
    return [item for item in items if isinstance(item, dict)]


def x__items__mutmut_2(raw: object) -> list[dict[str, object]]:
    if not isinstance(raw, dict):
        return []
    items = None
    if not isinstance(items, list):
        return []
    return [item for item in items if isinstance(item, dict)]


def x__items__mutmut_3(raw: object) -> list[dict[str, object]]:
    if not isinstance(raw, dict):
        return []
    items = raw.get(None, [])
    if not isinstance(items, list):
        return []
    return [item for item in items if isinstance(item, dict)]


def x__items__mutmut_4(raw: object) -> list[dict[str, object]]:
    if not isinstance(raw, dict):
        return []
    items = raw.get("items", None)
    if not isinstance(items, list):
        return []
    return [item for item in items if isinstance(item, dict)]


def x__items__mutmut_5(raw: object) -> list[dict[str, object]]:
    if not isinstance(raw, dict):
        return []
    items = raw.get([])
    if not isinstance(items, list):
        return []
    return [item for item in items if isinstance(item, dict)]


def x__items__mutmut_6(raw: object) -> list[dict[str, object]]:
    if not isinstance(raw, dict):
        return []
    items = raw.get("items", )
    if not isinstance(items, list):
        return []
    return [item for item in items if isinstance(item, dict)]


def x__items__mutmut_7(raw: object) -> list[dict[str, object]]:
    if not isinstance(raw, dict):
        return []
    items = raw.get("XXitemsXX", [])
    if not isinstance(items, list):
        return []
    return [item for item in items if isinstance(item, dict)]


def x__items__mutmut_8(raw: object) -> list[dict[str, object]]:
    if not isinstance(raw, dict):
        return []
    items = raw.get("ITEMS", [])
    if not isinstance(items, list):
        return []
    return [item for item in items if isinstance(item, dict)]


def x__items__mutmut_9(raw: object) -> list[dict[str, object]]:
    if not isinstance(raw, dict):
        return []
    items = raw.get("items", [])
    if isinstance(items, list):
        return []
    return [item for item in items if isinstance(item, dict)]

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
mutants_x__build_edges_from_virtual_services__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__build_edges_from_virtual_services__mutmut)
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


def x__build_edges_from_virtual_services__mutmut_orig(
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


def x__build_edges_from_virtual_services__mutmut_1(
    virtual_services: list[dict[str, object]],
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = None
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


def x__build_edges_from_virtual_services__mutmut_2(
    virtual_services: list[dict[str, object]],
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = None

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


def x__build_edges_from_virtual_services__mutmut_3(
    virtual_services: list[dict[str, object]],
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for virtual_service in virtual_services:
        callee = None
        if callee is None:
            continue
        for caller in _source_apps(virtual_service):
            if caller == callee or (caller, callee) in seen:
                continue
            seen.add((caller, callee))
            edges.append(EdgeRecordData(caller=caller, callee=callee))

    return edges


def x__build_edges_from_virtual_services__mutmut_4(
    virtual_services: list[dict[str, object]],
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for virtual_service in virtual_services:
        callee = _primary_host(None)
        if callee is None:
            continue
        for caller in _source_apps(virtual_service):
            if caller == callee or (caller, callee) in seen:
                continue
            seen.add((caller, callee))
            edges.append(EdgeRecordData(caller=caller, callee=callee))

    return edges


def x__build_edges_from_virtual_services__mutmut_5(
    virtual_services: list[dict[str, object]],
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for virtual_service in virtual_services:
        callee = _primary_host(virtual_service)
        if callee is not None:
            continue
        for caller in _source_apps(virtual_service):
            if caller == callee or (caller, callee) in seen:
                continue
            seen.add((caller, callee))
            edges.append(EdgeRecordData(caller=caller, callee=callee))

    return edges


def x__build_edges_from_virtual_services__mutmut_6(
    virtual_services: list[dict[str, object]],
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for virtual_service in virtual_services:
        callee = _primary_host(virtual_service)
        if callee is None:
            break
        for caller in _source_apps(virtual_service):
            if caller == callee or (caller, callee) in seen:
                continue
            seen.add((caller, callee))
            edges.append(EdgeRecordData(caller=caller, callee=callee))

    return edges


def x__build_edges_from_virtual_services__mutmut_7(
    virtual_services: list[dict[str, object]],
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for virtual_service in virtual_services:
        callee = _primary_host(virtual_service)
        if callee is None:
            continue
        for caller in _source_apps(None):
            if caller == callee or (caller, callee) in seen:
                continue
            seen.add((caller, callee))
            edges.append(EdgeRecordData(caller=caller, callee=callee))

    return edges


def x__build_edges_from_virtual_services__mutmut_8(
    virtual_services: list[dict[str, object]],
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for virtual_service in virtual_services:
        callee = _primary_host(virtual_service)
        if callee is None:
            continue
        for caller in _source_apps(virtual_service):
            if caller == callee and (caller, callee) in seen:
                continue
            seen.add((caller, callee))
            edges.append(EdgeRecordData(caller=caller, callee=callee))

    return edges


def x__build_edges_from_virtual_services__mutmut_9(
    virtual_services: list[dict[str, object]],
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for virtual_service in virtual_services:
        callee = _primary_host(virtual_service)
        if callee is None:
            continue
        for caller in _source_apps(virtual_service):
            if caller != callee or (caller, callee) in seen:
                continue
            seen.add((caller, callee))
            edges.append(EdgeRecordData(caller=caller, callee=callee))

    return edges


def x__build_edges_from_virtual_services__mutmut_10(
    virtual_services: list[dict[str, object]],
) -> list[EdgeRecordData]:
    edges: list[EdgeRecordData] = []
    seen: set[tuple[str, str]] = set()

    for virtual_service in virtual_services:
        callee = _primary_host(virtual_service)
        if callee is None:
            continue
        for caller in _source_apps(virtual_service):
            if caller == callee or (caller, callee) not in seen:
                continue
            seen.add((caller, callee))
            edges.append(EdgeRecordData(caller=caller, callee=callee))

    return edges


def x__build_edges_from_virtual_services__mutmut_11(
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
                break
            seen.add((caller, callee))
            edges.append(EdgeRecordData(caller=caller, callee=callee))

    return edges


def x__build_edges_from_virtual_services__mutmut_12(
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
            seen.add(None)
            edges.append(EdgeRecordData(caller=caller, callee=callee))

    return edges


def x__build_edges_from_virtual_services__mutmut_13(
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
            edges.append(None)

    return edges


def x__build_edges_from_virtual_services__mutmut_14(
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
            edges.append(EdgeRecordData(caller=None, callee=callee))

    return edges


def x__build_edges_from_virtual_services__mutmut_15(
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
            edges.append(EdgeRecordData(caller=caller, callee=None))

    return edges


def x__build_edges_from_virtual_services__mutmut_16(
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
            edges.append(EdgeRecordData(callee=callee))

    return edges


def x__build_edges_from_virtual_services__mutmut_17(
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
            edges.append(EdgeRecordData(caller=caller, ))

    return edges

mutants_x__build_edges_from_virtual_services__mutmut['_mutmut_orig'] = x__build_edges_from_virtual_services__mutmut_orig # type: ignore # mutmut generated
mutants_x__build_edges_from_virtual_services__mutmut['x__build_edges_from_virtual_services__mutmut_1'] = x__build_edges_from_virtual_services__mutmut_1 # type: ignore # mutmut generated
mutants_x__build_edges_from_virtual_services__mutmut['x__build_edges_from_virtual_services__mutmut_2'] = x__build_edges_from_virtual_services__mutmut_2 # type: ignore # mutmut generated
mutants_x__build_edges_from_virtual_services__mutmut['x__build_edges_from_virtual_services__mutmut_3'] = x__build_edges_from_virtual_services__mutmut_3 # type: ignore # mutmut generated
mutants_x__build_edges_from_virtual_services__mutmut['x__build_edges_from_virtual_services__mutmut_4'] = x__build_edges_from_virtual_services__mutmut_4 # type: ignore # mutmut generated
mutants_x__build_edges_from_virtual_services__mutmut['x__build_edges_from_virtual_services__mutmut_5'] = x__build_edges_from_virtual_services__mutmut_5 # type: ignore # mutmut generated
mutants_x__build_edges_from_virtual_services__mutmut['x__build_edges_from_virtual_services__mutmut_6'] = x__build_edges_from_virtual_services__mutmut_6 # type: ignore # mutmut generated
mutants_x__build_edges_from_virtual_services__mutmut['x__build_edges_from_virtual_services__mutmut_7'] = x__build_edges_from_virtual_services__mutmut_7 # type: ignore # mutmut generated
mutants_x__build_edges_from_virtual_services__mutmut['x__build_edges_from_virtual_services__mutmut_8'] = x__build_edges_from_virtual_services__mutmut_8 # type: ignore # mutmut generated
mutants_x__build_edges_from_virtual_services__mutmut['x__build_edges_from_virtual_services__mutmut_9'] = x__build_edges_from_virtual_services__mutmut_9 # type: ignore # mutmut generated
mutants_x__build_edges_from_virtual_services__mutmut['x__build_edges_from_virtual_services__mutmut_10'] = x__build_edges_from_virtual_services__mutmut_10 # type: ignore # mutmut generated
mutants_x__build_edges_from_virtual_services__mutmut['x__build_edges_from_virtual_services__mutmut_11'] = x__build_edges_from_virtual_services__mutmut_11 # type: ignore # mutmut generated
mutants_x__build_edges_from_virtual_services__mutmut['x__build_edges_from_virtual_services__mutmut_12'] = x__build_edges_from_virtual_services__mutmut_12 # type: ignore # mutmut generated
mutants_x__build_edges_from_virtual_services__mutmut['x__build_edges_from_virtual_services__mutmut_13'] = x__build_edges_from_virtual_services__mutmut_13 # type: ignore # mutmut generated
mutants_x__build_edges_from_virtual_services__mutmut['x__build_edges_from_virtual_services__mutmut_14'] = x__build_edges_from_virtual_services__mutmut_14 # type: ignore # mutmut generated
mutants_x__build_edges_from_virtual_services__mutmut['x__build_edges_from_virtual_services__mutmut_15'] = x__build_edges_from_virtual_services__mutmut_15 # type: ignore # mutmut generated
mutants_x__build_edges_from_virtual_services__mutmut['x__build_edges_from_virtual_services__mutmut_16'] = x__build_edges_from_virtual_services__mutmut_16 # type: ignore # mutmut generated
mutants_x__build_edges_from_virtual_services__mutmut['x__build_edges_from_virtual_services__mutmut_17'] = x__build_edges_from_virtual_services__mutmut_17 # type: ignore # mutmut generated
mutants_x__primary_host__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__primary_host__mutmut)
def _primary_host(virtual_service: dict[str, object]) -> str | None:
    spec = virtual_service.get("spec")
    if not isinstance(spec, dict):
        return None
    hosts = spec.get("hosts")
    if not isinstance(hosts, list) or not hosts:
        return None
    return str(hosts[0]).split(".")[0]


def x__primary_host__mutmut_orig(virtual_service: dict[str, object]) -> str | None:
    spec = virtual_service.get("spec")
    if not isinstance(spec, dict):
        return None
    hosts = spec.get("hosts")
    if not isinstance(hosts, list) or not hosts:
        return None
    return str(hosts[0]).split(".")[0]


def x__primary_host__mutmut_1(virtual_service: dict[str, object]) -> str | None:
    spec = None
    if not isinstance(spec, dict):
        return None
    hosts = spec.get("hosts")
    if not isinstance(hosts, list) or not hosts:
        return None
    return str(hosts[0]).split(".")[0]


def x__primary_host__mutmut_2(virtual_service: dict[str, object]) -> str | None:
    spec = virtual_service.get(None)
    if not isinstance(spec, dict):
        return None
    hosts = spec.get("hosts")
    if not isinstance(hosts, list) or not hosts:
        return None
    return str(hosts[0]).split(".")[0]


def x__primary_host__mutmut_3(virtual_service: dict[str, object]) -> str | None:
    spec = virtual_service.get("XXspecXX")
    if not isinstance(spec, dict):
        return None
    hosts = spec.get("hosts")
    if not isinstance(hosts, list) or not hosts:
        return None
    return str(hosts[0]).split(".")[0]


def x__primary_host__mutmut_4(virtual_service: dict[str, object]) -> str | None:
    spec = virtual_service.get("SPEC")
    if not isinstance(spec, dict):
        return None
    hosts = spec.get("hosts")
    if not isinstance(hosts, list) or not hosts:
        return None
    return str(hosts[0]).split(".")[0]


def x__primary_host__mutmut_5(virtual_service: dict[str, object]) -> str | None:
    spec = virtual_service.get("spec")
    if isinstance(spec, dict):
        return None
    hosts = spec.get("hosts")
    if not isinstance(hosts, list) or not hosts:
        return None
    return str(hosts[0]).split(".")[0]


def x__primary_host__mutmut_6(virtual_service: dict[str, object]) -> str | None:
    spec = virtual_service.get("spec")
    if not isinstance(spec, dict):
        return None
    hosts = None
    if not isinstance(hosts, list) or not hosts:
        return None
    return str(hosts[0]).split(".")[0]


def x__primary_host__mutmut_7(virtual_service: dict[str, object]) -> str | None:
    spec = virtual_service.get("spec")
    if not isinstance(spec, dict):
        return None
    hosts = spec.get(None)
    if not isinstance(hosts, list) or not hosts:
        return None
    return str(hosts[0]).split(".")[0]


def x__primary_host__mutmut_8(virtual_service: dict[str, object]) -> str | None:
    spec = virtual_service.get("spec")
    if not isinstance(spec, dict):
        return None
    hosts = spec.get("XXhostsXX")
    if not isinstance(hosts, list) or not hosts:
        return None
    return str(hosts[0]).split(".")[0]


def x__primary_host__mutmut_9(virtual_service: dict[str, object]) -> str | None:
    spec = virtual_service.get("spec")
    if not isinstance(spec, dict):
        return None
    hosts = spec.get("HOSTS")
    if not isinstance(hosts, list) or not hosts:
        return None
    return str(hosts[0]).split(".")[0]


def x__primary_host__mutmut_10(virtual_service: dict[str, object]) -> str | None:
    spec = virtual_service.get("spec")
    if not isinstance(spec, dict):
        return None
    hosts = spec.get("hosts")
    if not isinstance(hosts, list) and not hosts:
        return None
    return str(hosts[0]).split(".")[0]


def x__primary_host__mutmut_11(virtual_service: dict[str, object]) -> str | None:
    spec = virtual_service.get("spec")
    if not isinstance(spec, dict):
        return None
    hosts = spec.get("hosts")
    if isinstance(hosts, list) or not hosts:
        return None
    return str(hosts[0]).split(".")[0]


def x__primary_host__mutmut_12(virtual_service: dict[str, object]) -> str | None:
    spec = virtual_service.get("spec")
    if not isinstance(spec, dict):
        return None
    hosts = spec.get("hosts")
    if not isinstance(hosts, list) or hosts:
        return None
    return str(hosts[0]).split(".")[0]


def x__primary_host__mutmut_13(virtual_service: dict[str, object]) -> str | None:
    spec = virtual_service.get("spec")
    if not isinstance(spec, dict):
        return None
    hosts = spec.get("hosts")
    if not isinstance(hosts, list) or not hosts:
        return None
    return str(hosts[0]).split(None)[0]


def x__primary_host__mutmut_14(virtual_service: dict[str, object]) -> str | None:
    spec = virtual_service.get("spec")
    if not isinstance(spec, dict):
        return None
    hosts = spec.get("hosts")
    if not isinstance(hosts, list) or not hosts:
        return None
    return str(None).split(".")[0]


def x__primary_host__mutmut_15(virtual_service: dict[str, object]) -> str | None:
    spec = virtual_service.get("spec")
    if not isinstance(spec, dict):
        return None
    hosts = spec.get("hosts")
    if not isinstance(hosts, list) or not hosts:
        return None
    return str(hosts[1]).split(".")[0]


def x__primary_host__mutmut_16(virtual_service: dict[str, object]) -> str | None:
    spec = virtual_service.get("spec")
    if not isinstance(spec, dict):
        return None
    hosts = spec.get("hosts")
    if not isinstance(hosts, list) or not hosts:
        return None
    return str(hosts[0]).split("XX.XX")[0]


def x__primary_host__mutmut_17(virtual_service: dict[str, object]) -> str | None:
    spec = virtual_service.get("spec")
    if not isinstance(spec, dict):
        return None
    hosts = spec.get("hosts")
    if not isinstance(hosts, list) or not hosts:
        return None
    return str(hosts[0]).split(".")[1]

mutants_x__primary_host__mutmut['_mutmut_orig'] = x__primary_host__mutmut_orig # type: ignore # mutmut generated
mutants_x__primary_host__mutmut['x__primary_host__mutmut_1'] = x__primary_host__mutmut_1 # type: ignore # mutmut generated
mutants_x__primary_host__mutmut['x__primary_host__mutmut_2'] = x__primary_host__mutmut_2 # type: ignore # mutmut generated
mutants_x__primary_host__mutmut['x__primary_host__mutmut_3'] = x__primary_host__mutmut_3 # type: ignore # mutmut generated
mutants_x__primary_host__mutmut['x__primary_host__mutmut_4'] = x__primary_host__mutmut_4 # type: ignore # mutmut generated
mutants_x__primary_host__mutmut['x__primary_host__mutmut_5'] = x__primary_host__mutmut_5 # type: ignore # mutmut generated
mutants_x__primary_host__mutmut['x__primary_host__mutmut_6'] = x__primary_host__mutmut_6 # type: ignore # mutmut generated
mutants_x__primary_host__mutmut['x__primary_host__mutmut_7'] = x__primary_host__mutmut_7 # type: ignore # mutmut generated
mutants_x__primary_host__mutmut['x__primary_host__mutmut_8'] = x__primary_host__mutmut_8 # type: ignore # mutmut generated
mutants_x__primary_host__mutmut['x__primary_host__mutmut_9'] = x__primary_host__mutmut_9 # type: ignore # mutmut generated
mutants_x__primary_host__mutmut['x__primary_host__mutmut_10'] = x__primary_host__mutmut_10 # type: ignore # mutmut generated
mutants_x__primary_host__mutmut['x__primary_host__mutmut_11'] = x__primary_host__mutmut_11 # type: ignore # mutmut generated
mutants_x__primary_host__mutmut['x__primary_host__mutmut_12'] = x__primary_host__mutmut_12 # type: ignore # mutmut generated
mutants_x__primary_host__mutmut['x__primary_host__mutmut_13'] = x__primary_host__mutmut_13 # type: ignore # mutmut generated
mutants_x__primary_host__mutmut['x__primary_host__mutmut_14'] = x__primary_host__mutmut_14 # type: ignore # mutmut generated
mutants_x__primary_host__mutmut['x__primary_host__mutmut_15'] = x__primary_host__mutmut_15 # type: ignore # mutmut generated
mutants_x__primary_host__mutmut['x__primary_host__mutmut_16'] = x__primary_host__mutmut_16 # type: ignore # mutmut generated
mutants_x__primary_host__mutmut['x__primary_host__mutmut_17'] = x__primary_host__mutmut_17 # type: ignore # mutmut generated
mutants_x__source_apps__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__source_apps__mutmut)
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


def x__source_apps__mutmut_orig(virtual_service: dict[str, object]) -> list[str]:
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


def x__source_apps__mutmut_1(virtual_service: dict[str, object]) -> list[str]:
    spec = None
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


def x__source_apps__mutmut_2(virtual_service: dict[str, object]) -> list[str]:
    spec = virtual_service.get(None)
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


def x__source_apps__mutmut_3(virtual_service: dict[str, object]) -> list[str]:
    spec = virtual_service.get("XXspecXX")
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


def x__source_apps__mutmut_4(virtual_service: dict[str, object]) -> list[str]:
    spec = virtual_service.get("SPEC")
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


def x__source_apps__mutmut_5(virtual_service: dict[str, object]) -> list[str]:
    spec = virtual_service.get("spec")
    if isinstance(spec, dict):
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


def x__source_apps__mutmut_6(virtual_service: dict[str, object]) -> list[str]:
    spec = virtual_service.get("spec")
    if not isinstance(spec, dict):
        return []
    http_rules = None
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


def x__source_apps__mutmut_7(virtual_service: dict[str, object]) -> list[str]:
    spec = virtual_service.get("spec")
    if not isinstance(spec, dict):
        return []
    http_rules = spec.get(None)
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


def x__source_apps__mutmut_8(virtual_service: dict[str, object]) -> list[str]:
    spec = virtual_service.get("spec")
    if not isinstance(spec, dict):
        return []
    http_rules = spec.get("XXhttpXX")
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


def x__source_apps__mutmut_9(virtual_service: dict[str, object]) -> list[str]:
    spec = virtual_service.get("spec")
    if not isinstance(spec, dict):
        return []
    http_rules = spec.get("HTTP")
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


def x__source_apps__mutmut_10(virtual_service: dict[str, object]) -> list[str]:
    spec = virtual_service.get("spec")
    if not isinstance(spec, dict):
        return []
    http_rules = spec.get("http")
    if isinstance(http_rules, list):
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


def x__source_apps__mutmut_11(virtual_service: dict[str, object]) -> list[str]:
    spec = virtual_service.get("spec")
    if not isinstance(spec, dict):
        return []
    http_rules = spec.get("http")
    if not isinstance(http_rules, list):
        return []

    apps: list[str] = None
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


def x__source_apps__mutmut_12(virtual_service: dict[str, object]) -> list[str]:
    spec = virtual_service.get("spec")
    if not isinstance(spec, dict):
        return []
    http_rules = spec.get("http")
    if not isinstance(http_rules, list):
        return []

    apps: list[str] = []
    for rule in http_rules:
        if isinstance(rule, dict):
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


def x__source_apps__mutmut_13(virtual_service: dict[str, object]) -> list[str]:
    spec = virtual_service.get("spec")
    if not isinstance(spec, dict):
        return []
    http_rules = spec.get("http")
    if not isinstance(http_rules, list):
        return []

    apps: list[str] = []
    for rule in http_rules:
        if not isinstance(rule, dict):
            break
        for match in rule.get("match", []) or []:
            if not isinstance(match, dict):
                continue
            source_labels = match.get("sourceLabels")
            if isinstance(source_labels, dict):
                app = source_labels.get("app")
                if app:
                    apps.append(str(app))
    return apps


def x__source_apps__mutmut_14(virtual_service: dict[str, object]) -> list[str]:
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
        for match in rule.get("match", []) and []:
            if not isinstance(match, dict):
                continue
            source_labels = match.get("sourceLabels")
            if isinstance(source_labels, dict):
                app = source_labels.get("app")
                if app:
                    apps.append(str(app))
    return apps


def x__source_apps__mutmut_15(virtual_service: dict[str, object]) -> list[str]:
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
        for match in rule.get(None, []) or []:
            if not isinstance(match, dict):
                continue
            source_labels = match.get("sourceLabels")
            if isinstance(source_labels, dict):
                app = source_labels.get("app")
                if app:
                    apps.append(str(app))
    return apps


def x__source_apps__mutmut_16(virtual_service: dict[str, object]) -> list[str]:
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
        for match in rule.get("match", None) or []:
            if not isinstance(match, dict):
                continue
            source_labels = match.get("sourceLabels")
            if isinstance(source_labels, dict):
                app = source_labels.get("app")
                if app:
                    apps.append(str(app))
    return apps


def x__source_apps__mutmut_17(virtual_service: dict[str, object]) -> list[str]:
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
        for match in rule.get([]) or []:
            if not isinstance(match, dict):
                continue
            source_labels = match.get("sourceLabels")
            if isinstance(source_labels, dict):
                app = source_labels.get("app")
                if app:
                    apps.append(str(app))
    return apps


def x__source_apps__mutmut_18(virtual_service: dict[str, object]) -> list[str]:
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
        for match in rule.get("match", ) or []:
            if not isinstance(match, dict):
                continue
            source_labels = match.get("sourceLabels")
            if isinstance(source_labels, dict):
                app = source_labels.get("app")
                if app:
                    apps.append(str(app))
    return apps


def x__source_apps__mutmut_19(virtual_service: dict[str, object]) -> list[str]:
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
        for match in rule.get("XXmatchXX", []) or []:
            if not isinstance(match, dict):
                continue
            source_labels = match.get("sourceLabels")
            if isinstance(source_labels, dict):
                app = source_labels.get("app")
                if app:
                    apps.append(str(app))
    return apps


def x__source_apps__mutmut_20(virtual_service: dict[str, object]) -> list[str]:
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
        for match in rule.get("MATCH", []) or []:
            if not isinstance(match, dict):
                continue
            source_labels = match.get("sourceLabels")
            if isinstance(source_labels, dict):
                app = source_labels.get("app")
                if app:
                    apps.append(str(app))
    return apps


def x__source_apps__mutmut_21(virtual_service: dict[str, object]) -> list[str]:
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
            if isinstance(match, dict):
                continue
            source_labels = match.get("sourceLabels")
            if isinstance(source_labels, dict):
                app = source_labels.get("app")
                if app:
                    apps.append(str(app))
    return apps


def x__source_apps__mutmut_22(virtual_service: dict[str, object]) -> list[str]:
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
                break
            source_labels = match.get("sourceLabels")
            if isinstance(source_labels, dict):
                app = source_labels.get("app")
                if app:
                    apps.append(str(app))
    return apps


def x__source_apps__mutmut_23(virtual_service: dict[str, object]) -> list[str]:
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
            source_labels = None
            if isinstance(source_labels, dict):
                app = source_labels.get("app")
                if app:
                    apps.append(str(app))
    return apps


def x__source_apps__mutmut_24(virtual_service: dict[str, object]) -> list[str]:
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
            source_labels = match.get(None)
            if isinstance(source_labels, dict):
                app = source_labels.get("app")
                if app:
                    apps.append(str(app))
    return apps


def x__source_apps__mutmut_25(virtual_service: dict[str, object]) -> list[str]:
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
            source_labels = match.get("XXsourceLabelsXX")
            if isinstance(source_labels, dict):
                app = source_labels.get("app")
                if app:
                    apps.append(str(app))
    return apps


def x__source_apps__mutmut_26(virtual_service: dict[str, object]) -> list[str]:
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
            source_labels = match.get("sourcelabels")
            if isinstance(source_labels, dict):
                app = source_labels.get("app")
                if app:
                    apps.append(str(app))
    return apps


def x__source_apps__mutmut_27(virtual_service: dict[str, object]) -> list[str]:
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
            source_labels = match.get("SOURCELABELS")
            if isinstance(source_labels, dict):
                app = source_labels.get("app")
                if app:
                    apps.append(str(app))
    return apps


def x__source_apps__mutmut_28(virtual_service: dict[str, object]) -> list[str]:
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
                app = None
                if app:
                    apps.append(str(app))
    return apps


def x__source_apps__mutmut_29(virtual_service: dict[str, object]) -> list[str]:
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
                app = source_labels.get(None)
                if app:
                    apps.append(str(app))
    return apps


def x__source_apps__mutmut_30(virtual_service: dict[str, object]) -> list[str]:
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
                app = source_labels.get("XXappXX")
                if app:
                    apps.append(str(app))
    return apps


def x__source_apps__mutmut_31(virtual_service: dict[str, object]) -> list[str]:
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
                app = source_labels.get("APP")
                if app:
                    apps.append(str(app))
    return apps


def x__source_apps__mutmut_32(virtual_service: dict[str, object]) -> list[str]:
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
                    apps.append(None)
    return apps


def x__source_apps__mutmut_33(virtual_service: dict[str, object]) -> list[str]:
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
                    apps.append(str(None))
    return apps

mutants_x__source_apps__mutmut['_mutmut_orig'] = x__source_apps__mutmut_orig # type: ignore # mutmut generated
mutants_x__source_apps__mutmut['x__source_apps__mutmut_1'] = x__source_apps__mutmut_1 # type: ignore # mutmut generated
mutants_x__source_apps__mutmut['x__source_apps__mutmut_2'] = x__source_apps__mutmut_2 # type: ignore # mutmut generated
mutants_x__source_apps__mutmut['x__source_apps__mutmut_3'] = x__source_apps__mutmut_3 # type: ignore # mutmut generated
mutants_x__source_apps__mutmut['x__source_apps__mutmut_4'] = x__source_apps__mutmut_4 # type: ignore # mutmut generated
mutants_x__source_apps__mutmut['x__source_apps__mutmut_5'] = x__source_apps__mutmut_5 # type: ignore # mutmut generated
mutants_x__source_apps__mutmut['x__source_apps__mutmut_6'] = x__source_apps__mutmut_6 # type: ignore # mutmut generated
mutants_x__source_apps__mutmut['x__source_apps__mutmut_7'] = x__source_apps__mutmut_7 # type: ignore # mutmut generated
mutants_x__source_apps__mutmut['x__source_apps__mutmut_8'] = x__source_apps__mutmut_8 # type: ignore # mutmut generated
mutants_x__source_apps__mutmut['x__source_apps__mutmut_9'] = x__source_apps__mutmut_9 # type: ignore # mutmut generated
mutants_x__source_apps__mutmut['x__source_apps__mutmut_10'] = x__source_apps__mutmut_10 # type: ignore # mutmut generated
mutants_x__source_apps__mutmut['x__source_apps__mutmut_11'] = x__source_apps__mutmut_11 # type: ignore # mutmut generated
mutants_x__source_apps__mutmut['x__source_apps__mutmut_12'] = x__source_apps__mutmut_12 # type: ignore # mutmut generated
mutants_x__source_apps__mutmut['x__source_apps__mutmut_13'] = x__source_apps__mutmut_13 # type: ignore # mutmut generated
mutants_x__source_apps__mutmut['x__source_apps__mutmut_14'] = x__source_apps__mutmut_14 # type: ignore # mutmut generated
mutants_x__source_apps__mutmut['x__source_apps__mutmut_15'] = x__source_apps__mutmut_15 # type: ignore # mutmut generated
mutants_x__source_apps__mutmut['x__source_apps__mutmut_16'] = x__source_apps__mutmut_16 # type: ignore # mutmut generated
mutants_x__source_apps__mutmut['x__source_apps__mutmut_17'] = x__source_apps__mutmut_17 # type: ignore # mutmut generated
mutants_x__source_apps__mutmut['x__source_apps__mutmut_18'] = x__source_apps__mutmut_18 # type: ignore # mutmut generated
mutants_x__source_apps__mutmut['x__source_apps__mutmut_19'] = x__source_apps__mutmut_19 # type: ignore # mutmut generated
mutants_x__source_apps__mutmut['x__source_apps__mutmut_20'] = x__source_apps__mutmut_20 # type: ignore # mutmut generated
mutants_x__source_apps__mutmut['x__source_apps__mutmut_21'] = x__source_apps__mutmut_21 # type: ignore # mutmut generated
mutants_x__source_apps__mutmut['x__source_apps__mutmut_22'] = x__source_apps__mutmut_22 # type: ignore # mutmut generated
mutants_x__source_apps__mutmut['x__source_apps__mutmut_23'] = x__source_apps__mutmut_23 # type: ignore # mutmut generated
mutants_x__source_apps__mutmut['x__source_apps__mutmut_24'] = x__source_apps__mutmut_24 # type: ignore # mutmut generated
mutants_x__source_apps__mutmut['x__source_apps__mutmut_25'] = x__source_apps__mutmut_25 # type: ignore # mutmut generated
mutants_x__source_apps__mutmut['x__source_apps__mutmut_26'] = x__source_apps__mutmut_26 # type: ignore # mutmut generated
mutants_x__source_apps__mutmut['x__source_apps__mutmut_27'] = x__source_apps__mutmut_27 # type: ignore # mutmut generated
mutants_x__source_apps__mutmut['x__source_apps__mutmut_28'] = x__source_apps__mutmut_28 # type: ignore # mutmut generated
mutants_x__source_apps__mutmut['x__source_apps__mutmut_29'] = x__source_apps__mutmut_29 # type: ignore # mutmut generated
mutants_x__source_apps__mutmut['x__source_apps__mutmut_30'] = x__source_apps__mutmut_30 # type: ignore # mutmut generated
mutants_x__source_apps__mutmut['x__source_apps__mutmut_31'] = x__source_apps__mutmut_31 # type: ignore # mutmut generated
mutants_x__source_apps__mutmut['x__source_apps__mutmut_32'] = x__source_apps__mutmut_32 # type: ignore # mutmut generated
mutants_x__source_apps__mutmut['x__source_apps__mutmut_33'] = x__source_apps__mutmut_33 # type: ignore # mutmut generated
