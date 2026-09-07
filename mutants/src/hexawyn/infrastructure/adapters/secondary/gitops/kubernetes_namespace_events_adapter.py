from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driven.namespace_events_port import NamespaceEventsPort
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    InsufficientPermissionsError,
    ResourceNotFoundError,
)
from hexawyn.domain.models.namespace_event import GetNamespaceEventsRequest, NamespaceEvent

if TYPE_CHECKING:
    from kubernetes.client import CoreV1Api

_K8S_FORBIDDEN = 403
_K8S_NOT_FOUND = 404


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut: MutantDict = {}  # type: ignore


class KubernetesNamespaceEventsAdapter(NamespaceEventsPort):
    """Secondary adapter — reads namespace-wide events from the Kubernetes API
    (core_v1.list_namespaced_event)."""

    @_mutmut_mutated(mutants_xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut)
    def list_events(self, request: GetNamespaceEventsRequest) -> list[NamespaceEvent]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            event_list = core_api.list_namespaced_event(namespace=request.namespace)
        except Exception as exc:
            raise _translate_error(exc, request) from exc

        return [
            self._to_namespace_event(item, core_api, request.namespace) for item in event_list.items
        ]

    def xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut_orig(self, request: GetNamespaceEventsRequest) -> list[NamespaceEvent]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            event_list = core_api.list_namespaced_event(namespace=request.namespace)
        except Exception as exc:
            raise _translate_error(exc, request) from exc

        return [
            self._to_namespace_event(item, core_api, request.namespace) for item in event_list.items
        ]

    def xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut_1(self, request: GetNamespaceEventsRequest) -> list[NamespaceEvent]:
        from kubernetes import client as k8s

        core_api = None
        try:
            event_list = core_api.list_namespaced_event(namespace=request.namespace)
        except Exception as exc:
            raise _translate_error(exc, request) from exc

        return [
            self._to_namespace_event(item, core_api, request.namespace) for item in event_list.items
        ]

    def xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut_2(self, request: GetNamespaceEventsRequest) -> list[NamespaceEvent]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            event_list = None
        except Exception as exc:
            raise _translate_error(exc, request) from exc

        return [
            self._to_namespace_event(item, core_api, request.namespace) for item in event_list.items
        ]

    def xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut_3(self, request: GetNamespaceEventsRequest) -> list[NamespaceEvent]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            event_list = core_api.list_namespaced_event(namespace=None)
        except Exception as exc:
            raise _translate_error(exc, request) from exc

        return [
            self._to_namespace_event(item, core_api, request.namespace) for item in event_list.items
        ]

    def xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut_4(self, request: GetNamespaceEventsRequest) -> list[NamespaceEvent]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            event_list = core_api.list_namespaced_event(namespace=request.namespace)
        except Exception as exc:
            raise _translate_error(None, request) from exc

        return [
            self._to_namespace_event(item, core_api, request.namespace) for item in event_list.items
        ]

    def xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut_5(self, request: GetNamespaceEventsRequest) -> list[NamespaceEvent]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            event_list = core_api.list_namespaced_event(namespace=request.namespace)
        except Exception as exc:
            raise _translate_error(exc, None) from exc

        return [
            self._to_namespace_event(item, core_api, request.namespace) for item in event_list.items
        ]

    def xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut_6(self, request: GetNamespaceEventsRequest) -> list[NamespaceEvent]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            event_list = core_api.list_namespaced_event(namespace=request.namespace)
        except Exception as exc:
            raise _translate_error(request) from exc

        return [
            self._to_namespace_event(item, core_api, request.namespace) for item in event_list.items
        ]

    def xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut_7(self, request: GetNamespaceEventsRequest) -> list[NamespaceEvent]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            event_list = core_api.list_namespaced_event(namespace=request.namespace)
        except Exception as exc:
            raise _translate_error(exc, ) from exc

        return [
            self._to_namespace_event(item, core_api, request.namespace) for item in event_list.items
        ]

    def xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut_8(self, request: GetNamespaceEventsRequest) -> list[NamespaceEvent]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            event_list = core_api.list_namespaced_event(namespace=request.namespace)
        except Exception as exc:
            raise _translate_error(exc, request) from exc

        return [
            self._to_namespace_event(None, core_api, request.namespace) for item in event_list.items
        ]

    def xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut_9(self, request: GetNamespaceEventsRequest) -> list[NamespaceEvent]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            event_list = core_api.list_namespaced_event(namespace=request.namespace)
        except Exception as exc:
            raise _translate_error(exc, request) from exc

        return [
            self._to_namespace_event(item, None, request.namespace) for item in event_list.items
        ]

    def xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut_10(self, request: GetNamespaceEventsRequest) -> list[NamespaceEvent]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            event_list = core_api.list_namespaced_event(namespace=request.namespace)
        except Exception as exc:
            raise _translate_error(exc, request) from exc

        return [
            self._to_namespace_event(item, core_api, None) for item in event_list.items
        ]

    def xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut_11(self, request: GetNamespaceEventsRequest) -> list[NamespaceEvent]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            event_list = core_api.list_namespaced_event(namespace=request.namespace)
        except Exception as exc:
            raise _translate_error(exc, request) from exc

        return [
            self._to_namespace_event(core_api, request.namespace) for item in event_list.items
        ]

    def xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut_12(self, request: GetNamespaceEventsRequest) -> list[NamespaceEvent]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            event_list = core_api.list_namespaced_event(namespace=request.namespace)
        except Exception as exc:
            raise _translate_error(exc, request) from exc

        return [
            self._to_namespace_event(item, request.namespace) for item in event_list.items
        ]

    def xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut_13(self, request: GetNamespaceEventsRequest) -> list[NamespaceEvent]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            event_list = core_api.list_namespaced_event(namespace=request.namespace)
        except Exception as exc:
            raise _translate_error(exc, request) from exc

        return [
            self._to_namespace_event(item, core_api, ) for item in event_list.items
        ]

    @_mutmut_mutated(mutants_xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut)
    def _to_namespace_event(
        self, item: object, core_api: CoreV1Api, namespace: str
    ) -> NamespaceEvent:
        involved = item.involved_object  # type: ignore[attr-defined]
        object_ref = f"{involved.kind.lower()}/{involved.name}"
        last_seen = (
            item.last_timestamp or item.event_time or item.first_timestamp  # type: ignore[attr-defined]
        )
        return NamespaceEvent(
            event_type=item.type or "Normal",  # type: ignore[attr-defined]
            reason=item.reason or "",  # type: ignore[attr-defined]
            message=item.message or "",  # type: ignore[attr-defined]
            object=object_ref,
            count=item.count or 1,  # type: ignore[attr-defined]
            last_seen=last_seen.isoformat() if last_seen else "",
            object_exists=_object_exists(core_api, involved, namespace),
        )

    def xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_orig(
        self, item: object, core_api: CoreV1Api, namespace: str
    ) -> NamespaceEvent:
        involved = item.involved_object  # type: ignore[attr-defined]
        object_ref = f"{involved.kind.lower()}/{involved.name}"
        last_seen = (
            item.last_timestamp or item.event_time or item.first_timestamp  # type: ignore[attr-defined]
        )
        return NamespaceEvent(
            event_type=item.type or "Normal",  # type: ignore[attr-defined]
            reason=item.reason or "",  # type: ignore[attr-defined]
            message=item.message or "",  # type: ignore[attr-defined]
            object=object_ref,
            count=item.count or 1,  # type: ignore[attr-defined]
            last_seen=last_seen.isoformat() if last_seen else "",
            object_exists=_object_exists(core_api, involved, namespace),
        )

    def xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_1(
        self, item: object, core_api: CoreV1Api, namespace: str
    ) -> NamespaceEvent:
        involved = None  # type: ignore[attr-defined]
        object_ref = f"{involved.kind.lower()}/{involved.name}"
        last_seen = (
            item.last_timestamp or item.event_time or item.first_timestamp  # type: ignore[attr-defined]
        )
        return NamespaceEvent(
            event_type=item.type or "Normal",  # type: ignore[attr-defined]
            reason=item.reason or "",  # type: ignore[attr-defined]
            message=item.message or "",  # type: ignore[attr-defined]
            object=object_ref,
            count=item.count or 1,  # type: ignore[attr-defined]
            last_seen=last_seen.isoformat() if last_seen else "",
            object_exists=_object_exists(core_api, involved, namespace),
        )

    def xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_2(
        self, item: object, core_api: CoreV1Api, namespace: str
    ) -> NamespaceEvent:
        involved = item.involved_object  # type: ignore[attr-defined]
        object_ref = None
        last_seen = (
            item.last_timestamp or item.event_time or item.first_timestamp  # type: ignore[attr-defined]
        )
        return NamespaceEvent(
            event_type=item.type or "Normal",  # type: ignore[attr-defined]
            reason=item.reason or "",  # type: ignore[attr-defined]
            message=item.message or "",  # type: ignore[attr-defined]
            object=object_ref,
            count=item.count or 1,  # type: ignore[attr-defined]
            last_seen=last_seen.isoformat() if last_seen else "",
            object_exists=_object_exists(core_api, involved, namespace),
        )

    def xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_3(
        self, item: object, core_api: CoreV1Api, namespace: str
    ) -> NamespaceEvent:
        involved = item.involved_object  # type: ignore[attr-defined]
        object_ref = f"{involved.kind.upper()}/{involved.name}"
        last_seen = (
            item.last_timestamp or item.event_time or item.first_timestamp  # type: ignore[attr-defined]
        )
        return NamespaceEvent(
            event_type=item.type or "Normal",  # type: ignore[attr-defined]
            reason=item.reason or "",  # type: ignore[attr-defined]
            message=item.message or "",  # type: ignore[attr-defined]
            object=object_ref,
            count=item.count or 1,  # type: ignore[attr-defined]
            last_seen=last_seen.isoformat() if last_seen else "",
            object_exists=_object_exists(core_api, involved, namespace),
        )

    def xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_4(
        self, item: object, core_api: CoreV1Api, namespace: str
    ) -> NamespaceEvent:
        involved = item.involved_object  # type: ignore[attr-defined]
        object_ref = f"{involved.kind.lower()}/{involved.name}"
        last_seen = None
        return NamespaceEvent(
            event_type=item.type or "Normal",  # type: ignore[attr-defined]
            reason=item.reason or "",  # type: ignore[attr-defined]
            message=item.message or "",  # type: ignore[attr-defined]
            object=object_ref,
            count=item.count or 1,  # type: ignore[attr-defined]
            last_seen=last_seen.isoformat() if last_seen else "",
            object_exists=_object_exists(core_api, involved, namespace),
        )

    def xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_5(
        self, item: object, core_api: CoreV1Api, namespace: str
    ) -> NamespaceEvent:
        involved = item.involved_object  # type: ignore[attr-defined]
        object_ref = f"{involved.kind.lower()}/{involved.name}"
        last_seen = (
            item.last_timestamp or item.event_time and item.first_timestamp  # type: ignore[attr-defined]
        )
        return NamespaceEvent(
            event_type=item.type or "Normal",  # type: ignore[attr-defined]
            reason=item.reason or "",  # type: ignore[attr-defined]
            message=item.message or "",  # type: ignore[attr-defined]
            object=object_ref,
            count=item.count or 1,  # type: ignore[attr-defined]
            last_seen=last_seen.isoformat() if last_seen else "",
            object_exists=_object_exists(core_api, involved, namespace),
        )

    def xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_6(
        self, item: object, core_api: CoreV1Api, namespace: str
    ) -> NamespaceEvent:
        involved = item.involved_object  # type: ignore[attr-defined]
        object_ref = f"{involved.kind.lower()}/{involved.name}"
        last_seen = (
            item.last_timestamp and item.event_time or item.first_timestamp  # type: ignore[attr-defined]
        )
        return NamespaceEvent(
            event_type=item.type or "Normal",  # type: ignore[attr-defined]
            reason=item.reason or "",  # type: ignore[attr-defined]
            message=item.message or "",  # type: ignore[attr-defined]
            object=object_ref,
            count=item.count or 1,  # type: ignore[attr-defined]
            last_seen=last_seen.isoformat() if last_seen else "",
            object_exists=_object_exists(core_api, involved, namespace),
        )

    def xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_7(
        self, item: object, core_api: CoreV1Api, namespace: str
    ) -> NamespaceEvent:
        involved = item.involved_object  # type: ignore[attr-defined]
        object_ref = f"{involved.kind.lower()}/{involved.name}"
        last_seen = (
            item.last_timestamp or item.event_time or item.first_timestamp  # type: ignore[attr-defined]
        )
        return NamespaceEvent(
            event_type=None,  # type: ignore[attr-defined]
            reason=item.reason or "",  # type: ignore[attr-defined]
            message=item.message or "",  # type: ignore[attr-defined]
            object=object_ref,
            count=item.count or 1,  # type: ignore[attr-defined]
            last_seen=last_seen.isoformat() if last_seen else "",
            object_exists=_object_exists(core_api, involved, namespace),
        )

    def xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_8(
        self, item: object, core_api: CoreV1Api, namespace: str
    ) -> NamespaceEvent:
        involved = item.involved_object  # type: ignore[attr-defined]
        object_ref = f"{involved.kind.lower()}/{involved.name}"
        last_seen = (
            item.last_timestamp or item.event_time or item.first_timestamp  # type: ignore[attr-defined]
        )
        return NamespaceEvent(
            event_type=item.type or "Normal",  # type: ignore[attr-defined]
            reason=None,  # type: ignore[attr-defined]
            message=item.message or "",  # type: ignore[attr-defined]
            object=object_ref,
            count=item.count or 1,  # type: ignore[attr-defined]
            last_seen=last_seen.isoformat() if last_seen else "",
            object_exists=_object_exists(core_api, involved, namespace),
        )

    def xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_9(
        self, item: object, core_api: CoreV1Api, namespace: str
    ) -> NamespaceEvent:
        involved = item.involved_object  # type: ignore[attr-defined]
        object_ref = f"{involved.kind.lower()}/{involved.name}"
        last_seen = (
            item.last_timestamp or item.event_time or item.first_timestamp  # type: ignore[attr-defined]
        )
        return NamespaceEvent(
            event_type=item.type or "Normal",  # type: ignore[attr-defined]
            reason=item.reason or "",  # type: ignore[attr-defined]
            message=None,  # type: ignore[attr-defined]
            object=object_ref,
            count=item.count or 1,  # type: ignore[attr-defined]
            last_seen=last_seen.isoformat() if last_seen else "",
            object_exists=_object_exists(core_api, involved, namespace),
        )

    def xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_10(
        self, item: object, core_api: CoreV1Api, namespace: str
    ) -> NamespaceEvent:
        involved = item.involved_object  # type: ignore[attr-defined]
        object_ref = f"{involved.kind.lower()}/{involved.name}"
        last_seen = (
            item.last_timestamp or item.event_time or item.first_timestamp  # type: ignore[attr-defined]
        )
        return NamespaceEvent(
            event_type=item.type or "Normal",  # type: ignore[attr-defined]
            reason=item.reason or "",  # type: ignore[attr-defined]
            message=item.message or "",  # type: ignore[attr-defined]
            object=None,
            count=item.count or 1,  # type: ignore[attr-defined]
            last_seen=last_seen.isoformat() if last_seen else "",
            object_exists=_object_exists(core_api, involved, namespace),
        )

    def xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_11(
        self, item: object, core_api: CoreV1Api, namespace: str
    ) -> NamespaceEvent:
        involved = item.involved_object  # type: ignore[attr-defined]
        object_ref = f"{involved.kind.lower()}/{involved.name}"
        last_seen = (
            item.last_timestamp or item.event_time or item.first_timestamp  # type: ignore[attr-defined]
        )
        return NamespaceEvent(
            event_type=item.type or "Normal",  # type: ignore[attr-defined]
            reason=item.reason or "",  # type: ignore[attr-defined]
            message=item.message or "",  # type: ignore[attr-defined]
            object=object_ref,
            count=None,  # type: ignore[attr-defined]
            last_seen=last_seen.isoformat() if last_seen else "",
            object_exists=_object_exists(core_api, involved, namespace),
        )

    def xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_12(
        self, item: object, core_api: CoreV1Api, namespace: str
    ) -> NamespaceEvent:
        involved = item.involved_object  # type: ignore[attr-defined]
        object_ref = f"{involved.kind.lower()}/{involved.name}"
        last_seen = (
            item.last_timestamp or item.event_time or item.first_timestamp  # type: ignore[attr-defined]
        )
        return NamespaceEvent(
            event_type=item.type or "Normal",  # type: ignore[attr-defined]
            reason=item.reason or "",  # type: ignore[attr-defined]
            message=item.message or "",  # type: ignore[attr-defined]
            object=object_ref,
            count=item.count or 1,  # type: ignore[attr-defined]
            last_seen=None,
            object_exists=_object_exists(core_api, involved, namespace),
        )

    def xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_13(
        self, item: object, core_api: CoreV1Api, namespace: str
    ) -> NamespaceEvent:
        involved = item.involved_object  # type: ignore[attr-defined]
        object_ref = f"{involved.kind.lower()}/{involved.name}"
        last_seen = (
            item.last_timestamp or item.event_time or item.first_timestamp  # type: ignore[attr-defined]
        )
        return NamespaceEvent(
            event_type=item.type or "Normal",  # type: ignore[attr-defined]
            reason=item.reason or "",  # type: ignore[attr-defined]
            message=item.message or "",  # type: ignore[attr-defined]
            object=object_ref,
            count=item.count or 1,  # type: ignore[attr-defined]
            last_seen=last_seen.isoformat() if last_seen else "",
            object_exists=None,
        )

    def xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_14(
        self, item: object, core_api: CoreV1Api, namespace: str
    ) -> NamespaceEvent:
        involved = item.involved_object  # type: ignore[attr-defined]
        object_ref = f"{involved.kind.lower()}/{involved.name}"
        last_seen = (
            item.last_timestamp or item.event_time or item.first_timestamp  # type: ignore[attr-defined]
        )
        return NamespaceEvent(
            reason=item.reason or "",  # type: ignore[attr-defined]
            message=item.message or "",  # type: ignore[attr-defined]
            object=object_ref,
            count=item.count or 1,  # type: ignore[attr-defined]
            last_seen=last_seen.isoformat() if last_seen else "",
            object_exists=_object_exists(core_api, involved, namespace),
        )

    def xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_15(
        self, item: object, core_api: CoreV1Api, namespace: str
    ) -> NamespaceEvent:
        involved = item.involved_object  # type: ignore[attr-defined]
        object_ref = f"{involved.kind.lower()}/{involved.name}"
        last_seen = (
            item.last_timestamp or item.event_time or item.first_timestamp  # type: ignore[attr-defined]
        )
        return NamespaceEvent(
            event_type=item.type or "Normal",  # type: ignore[attr-defined]
            message=item.message or "",  # type: ignore[attr-defined]
            object=object_ref,
            count=item.count or 1,  # type: ignore[attr-defined]
            last_seen=last_seen.isoformat() if last_seen else "",
            object_exists=_object_exists(core_api, involved, namespace),
        )

    def xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_16(
        self, item: object, core_api: CoreV1Api, namespace: str
    ) -> NamespaceEvent:
        involved = item.involved_object  # type: ignore[attr-defined]
        object_ref = f"{involved.kind.lower()}/{involved.name}"
        last_seen = (
            item.last_timestamp or item.event_time or item.first_timestamp  # type: ignore[attr-defined]
        )
        return NamespaceEvent(
            event_type=item.type or "Normal",  # type: ignore[attr-defined]
            reason=item.reason or "",  # type: ignore[attr-defined]
            object=object_ref,
            count=item.count or 1,  # type: ignore[attr-defined]
            last_seen=last_seen.isoformat() if last_seen else "",
            object_exists=_object_exists(core_api, involved, namespace),
        )

    def xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_17(
        self, item: object, core_api: CoreV1Api, namespace: str
    ) -> NamespaceEvent:
        involved = item.involved_object  # type: ignore[attr-defined]
        object_ref = f"{involved.kind.lower()}/{involved.name}"
        last_seen = (
            item.last_timestamp or item.event_time or item.first_timestamp  # type: ignore[attr-defined]
        )
        return NamespaceEvent(
            event_type=item.type or "Normal",  # type: ignore[attr-defined]
            reason=item.reason or "",  # type: ignore[attr-defined]
            message=item.message or "",  # type: ignore[attr-defined]
            count=item.count or 1,  # type: ignore[attr-defined]
            last_seen=last_seen.isoformat() if last_seen else "",
            object_exists=_object_exists(core_api, involved, namespace),
        )

    def xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_18(
        self, item: object, core_api: CoreV1Api, namespace: str
    ) -> NamespaceEvent:
        involved = item.involved_object  # type: ignore[attr-defined]
        object_ref = f"{involved.kind.lower()}/{involved.name}"
        last_seen = (
            item.last_timestamp or item.event_time or item.first_timestamp  # type: ignore[attr-defined]
        )
        return NamespaceEvent(
            event_type=item.type or "Normal",  # type: ignore[attr-defined]
            reason=item.reason or "",  # type: ignore[attr-defined]
            message=item.message or "",  # type: ignore[attr-defined]
            object=object_ref,
            last_seen=last_seen.isoformat() if last_seen else "",
            object_exists=_object_exists(core_api, involved, namespace),
        )

    def xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_19(
        self, item: object, core_api: CoreV1Api, namespace: str
    ) -> NamespaceEvent:
        involved = item.involved_object  # type: ignore[attr-defined]
        object_ref = f"{involved.kind.lower()}/{involved.name}"
        last_seen = (
            item.last_timestamp or item.event_time or item.first_timestamp  # type: ignore[attr-defined]
        )
        return NamespaceEvent(
            event_type=item.type or "Normal",  # type: ignore[attr-defined]
            reason=item.reason or "",  # type: ignore[attr-defined]
            message=item.message or "",  # type: ignore[attr-defined]
            object=object_ref,
            count=item.count or 1,  # type: ignore[attr-defined]
            object_exists=_object_exists(core_api, involved, namespace),
        )

    def xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_20(
        self, item: object, core_api: CoreV1Api, namespace: str
    ) -> NamespaceEvent:
        involved = item.involved_object  # type: ignore[attr-defined]
        object_ref = f"{involved.kind.lower()}/{involved.name}"
        last_seen = (
            item.last_timestamp or item.event_time or item.first_timestamp  # type: ignore[attr-defined]
        )
        return NamespaceEvent(
            event_type=item.type or "Normal",  # type: ignore[attr-defined]
            reason=item.reason or "",  # type: ignore[attr-defined]
            message=item.message or "",  # type: ignore[attr-defined]
            object=object_ref,
            count=item.count or 1,  # type: ignore[attr-defined]
            last_seen=last_seen.isoformat() if last_seen else "",
            )

    def xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_21(
        self, item: object, core_api: CoreV1Api, namespace: str
    ) -> NamespaceEvent:
        involved = item.involved_object  # type: ignore[attr-defined]
        object_ref = f"{involved.kind.lower()}/{involved.name}"
        last_seen = (
            item.last_timestamp or item.event_time or item.first_timestamp  # type: ignore[attr-defined]
        )
        return NamespaceEvent(
            event_type=item.type and "Normal",  # type: ignore[attr-defined]
            reason=item.reason or "",  # type: ignore[attr-defined]
            message=item.message or "",  # type: ignore[attr-defined]
            object=object_ref,
            count=item.count or 1,  # type: ignore[attr-defined]
            last_seen=last_seen.isoformat() if last_seen else "",
            object_exists=_object_exists(core_api, involved, namespace),
        )

    def xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_22(
        self, item: object, core_api: CoreV1Api, namespace: str
    ) -> NamespaceEvent:
        involved = item.involved_object  # type: ignore[attr-defined]
        object_ref = f"{involved.kind.lower()}/{involved.name}"
        last_seen = (
            item.last_timestamp or item.event_time or item.first_timestamp  # type: ignore[attr-defined]
        )
        return NamespaceEvent(
            event_type=item.type or "XXNormalXX",  # type: ignore[attr-defined]
            reason=item.reason or "",  # type: ignore[attr-defined]
            message=item.message or "",  # type: ignore[attr-defined]
            object=object_ref,
            count=item.count or 1,  # type: ignore[attr-defined]
            last_seen=last_seen.isoformat() if last_seen else "",
            object_exists=_object_exists(core_api, involved, namespace),
        )

    def xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_23(
        self, item: object, core_api: CoreV1Api, namespace: str
    ) -> NamespaceEvent:
        involved = item.involved_object  # type: ignore[attr-defined]
        object_ref = f"{involved.kind.lower()}/{involved.name}"
        last_seen = (
            item.last_timestamp or item.event_time or item.first_timestamp  # type: ignore[attr-defined]
        )
        return NamespaceEvent(
            event_type=item.type or "normal",  # type: ignore[attr-defined]
            reason=item.reason or "",  # type: ignore[attr-defined]
            message=item.message or "",  # type: ignore[attr-defined]
            object=object_ref,
            count=item.count or 1,  # type: ignore[attr-defined]
            last_seen=last_seen.isoformat() if last_seen else "",
            object_exists=_object_exists(core_api, involved, namespace),
        )

    def xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_24(
        self, item: object, core_api: CoreV1Api, namespace: str
    ) -> NamespaceEvent:
        involved = item.involved_object  # type: ignore[attr-defined]
        object_ref = f"{involved.kind.lower()}/{involved.name}"
        last_seen = (
            item.last_timestamp or item.event_time or item.first_timestamp  # type: ignore[attr-defined]
        )
        return NamespaceEvent(
            event_type=item.type or "NORMAL",  # type: ignore[attr-defined]
            reason=item.reason or "",  # type: ignore[attr-defined]
            message=item.message or "",  # type: ignore[attr-defined]
            object=object_ref,
            count=item.count or 1,  # type: ignore[attr-defined]
            last_seen=last_seen.isoformat() if last_seen else "",
            object_exists=_object_exists(core_api, involved, namespace),
        )

    def xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_25(
        self, item: object, core_api: CoreV1Api, namespace: str
    ) -> NamespaceEvent:
        involved = item.involved_object  # type: ignore[attr-defined]
        object_ref = f"{involved.kind.lower()}/{involved.name}"
        last_seen = (
            item.last_timestamp or item.event_time or item.first_timestamp  # type: ignore[attr-defined]
        )
        return NamespaceEvent(
            event_type=item.type or "Normal",  # type: ignore[attr-defined]
            reason=item.reason and "",  # type: ignore[attr-defined]
            message=item.message or "",  # type: ignore[attr-defined]
            object=object_ref,
            count=item.count or 1,  # type: ignore[attr-defined]
            last_seen=last_seen.isoformat() if last_seen else "",
            object_exists=_object_exists(core_api, involved, namespace),
        )

    def xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_26(
        self, item: object, core_api: CoreV1Api, namespace: str
    ) -> NamespaceEvent:
        involved = item.involved_object  # type: ignore[attr-defined]
        object_ref = f"{involved.kind.lower()}/{involved.name}"
        last_seen = (
            item.last_timestamp or item.event_time or item.first_timestamp  # type: ignore[attr-defined]
        )
        return NamespaceEvent(
            event_type=item.type or "Normal",  # type: ignore[attr-defined]
            reason=item.reason or "XXXX",  # type: ignore[attr-defined]
            message=item.message or "",  # type: ignore[attr-defined]
            object=object_ref,
            count=item.count or 1,  # type: ignore[attr-defined]
            last_seen=last_seen.isoformat() if last_seen else "",
            object_exists=_object_exists(core_api, involved, namespace),
        )

    def xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_27(
        self, item: object, core_api: CoreV1Api, namespace: str
    ) -> NamespaceEvent:
        involved = item.involved_object  # type: ignore[attr-defined]
        object_ref = f"{involved.kind.lower()}/{involved.name}"
        last_seen = (
            item.last_timestamp or item.event_time or item.first_timestamp  # type: ignore[attr-defined]
        )
        return NamespaceEvent(
            event_type=item.type or "Normal",  # type: ignore[attr-defined]
            reason=item.reason or "",  # type: ignore[attr-defined]
            message=item.message and "",  # type: ignore[attr-defined]
            object=object_ref,
            count=item.count or 1,  # type: ignore[attr-defined]
            last_seen=last_seen.isoformat() if last_seen else "",
            object_exists=_object_exists(core_api, involved, namespace),
        )

    def xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_28(
        self, item: object, core_api: CoreV1Api, namespace: str
    ) -> NamespaceEvent:
        involved = item.involved_object  # type: ignore[attr-defined]
        object_ref = f"{involved.kind.lower()}/{involved.name}"
        last_seen = (
            item.last_timestamp or item.event_time or item.first_timestamp  # type: ignore[attr-defined]
        )
        return NamespaceEvent(
            event_type=item.type or "Normal",  # type: ignore[attr-defined]
            reason=item.reason or "",  # type: ignore[attr-defined]
            message=item.message or "XXXX",  # type: ignore[attr-defined]
            object=object_ref,
            count=item.count or 1,  # type: ignore[attr-defined]
            last_seen=last_seen.isoformat() if last_seen else "",
            object_exists=_object_exists(core_api, involved, namespace),
        )

    def xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_29(
        self, item: object, core_api: CoreV1Api, namespace: str
    ) -> NamespaceEvent:
        involved = item.involved_object  # type: ignore[attr-defined]
        object_ref = f"{involved.kind.lower()}/{involved.name}"
        last_seen = (
            item.last_timestamp or item.event_time or item.first_timestamp  # type: ignore[attr-defined]
        )
        return NamespaceEvent(
            event_type=item.type or "Normal",  # type: ignore[attr-defined]
            reason=item.reason or "",  # type: ignore[attr-defined]
            message=item.message or "",  # type: ignore[attr-defined]
            object=object_ref,
            count=item.count and 1,  # type: ignore[attr-defined]
            last_seen=last_seen.isoformat() if last_seen else "",
            object_exists=_object_exists(core_api, involved, namespace),
        )

    def xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_30(
        self, item: object, core_api: CoreV1Api, namespace: str
    ) -> NamespaceEvent:
        involved = item.involved_object  # type: ignore[attr-defined]
        object_ref = f"{involved.kind.lower()}/{involved.name}"
        last_seen = (
            item.last_timestamp or item.event_time or item.first_timestamp  # type: ignore[attr-defined]
        )
        return NamespaceEvent(
            event_type=item.type or "Normal",  # type: ignore[attr-defined]
            reason=item.reason or "",  # type: ignore[attr-defined]
            message=item.message or "",  # type: ignore[attr-defined]
            object=object_ref,
            count=item.count or 2,  # type: ignore[attr-defined]
            last_seen=last_seen.isoformat() if last_seen else "",
            object_exists=_object_exists(core_api, involved, namespace),
        )

    def xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_31(
        self, item: object, core_api: CoreV1Api, namespace: str
    ) -> NamespaceEvent:
        involved = item.involved_object  # type: ignore[attr-defined]
        object_ref = f"{involved.kind.lower()}/{involved.name}"
        last_seen = (
            item.last_timestamp or item.event_time or item.first_timestamp  # type: ignore[attr-defined]
        )
        return NamespaceEvent(
            event_type=item.type or "Normal",  # type: ignore[attr-defined]
            reason=item.reason or "",  # type: ignore[attr-defined]
            message=item.message or "",  # type: ignore[attr-defined]
            object=object_ref,
            count=item.count or 1,  # type: ignore[attr-defined]
            last_seen=last_seen.isoformat() if last_seen else "XXXX",
            object_exists=_object_exists(core_api, involved, namespace),
        )

    def xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_32(
        self, item: object, core_api: CoreV1Api, namespace: str
    ) -> NamespaceEvent:
        involved = item.involved_object  # type: ignore[attr-defined]
        object_ref = f"{involved.kind.lower()}/{involved.name}"
        last_seen = (
            item.last_timestamp or item.event_time or item.first_timestamp  # type: ignore[attr-defined]
        )
        return NamespaceEvent(
            event_type=item.type or "Normal",  # type: ignore[attr-defined]
            reason=item.reason or "",  # type: ignore[attr-defined]
            message=item.message or "",  # type: ignore[attr-defined]
            object=object_ref,
            count=item.count or 1,  # type: ignore[attr-defined]
            last_seen=last_seen.isoformat() if last_seen else "",
            object_exists=_object_exists(None, involved, namespace),
        )

    def xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_33(
        self, item: object, core_api: CoreV1Api, namespace: str
    ) -> NamespaceEvent:
        involved = item.involved_object  # type: ignore[attr-defined]
        object_ref = f"{involved.kind.lower()}/{involved.name}"
        last_seen = (
            item.last_timestamp or item.event_time or item.first_timestamp  # type: ignore[attr-defined]
        )
        return NamespaceEvent(
            event_type=item.type or "Normal",  # type: ignore[attr-defined]
            reason=item.reason or "",  # type: ignore[attr-defined]
            message=item.message or "",  # type: ignore[attr-defined]
            object=object_ref,
            count=item.count or 1,  # type: ignore[attr-defined]
            last_seen=last_seen.isoformat() if last_seen else "",
            object_exists=_object_exists(core_api, None, namespace),
        )

    def xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_34(
        self, item: object, core_api: CoreV1Api, namespace: str
    ) -> NamespaceEvent:
        involved = item.involved_object  # type: ignore[attr-defined]
        object_ref = f"{involved.kind.lower()}/{involved.name}"
        last_seen = (
            item.last_timestamp or item.event_time or item.first_timestamp  # type: ignore[attr-defined]
        )
        return NamespaceEvent(
            event_type=item.type or "Normal",  # type: ignore[attr-defined]
            reason=item.reason or "",  # type: ignore[attr-defined]
            message=item.message or "",  # type: ignore[attr-defined]
            object=object_ref,
            count=item.count or 1,  # type: ignore[attr-defined]
            last_seen=last_seen.isoformat() if last_seen else "",
            object_exists=_object_exists(core_api, involved, None),
        )

    def xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_35(
        self, item: object, core_api: CoreV1Api, namespace: str
    ) -> NamespaceEvent:
        involved = item.involved_object  # type: ignore[attr-defined]
        object_ref = f"{involved.kind.lower()}/{involved.name}"
        last_seen = (
            item.last_timestamp or item.event_time or item.first_timestamp  # type: ignore[attr-defined]
        )
        return NamespaceEvent(
            event_type=item.type or "Normal",  # type: ignore[attr-defined]
            reason=item.reason or "",  # type: ignore[attr-defined]
            message=item.message or "",  # type: ignore[attr-defined]
            object=object_ref,
            count=item.count or 1,  # type: ignore[attr-defined]
            last_seen=last_seen.isoformat() if last_seen else "",
            object_exists=_object_exists(involved, namespace),
        )

    def xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_36(
        self, item: object, core_api: CoreV1Api, namespace: str
    ) -> NamespaceEvent:
        involved = item.involved_object  # type: ignore[attr-defined]
        object_ref = f"{involved.kind.lower()}/{involved.name}"
        last_seen = (
            item.last_timestamp or item.event_time or item.first_timestamp  # type: ignore[attr-defined]
        )
        return NamespaceEvent(
            event_type=item.type or "Normal",  # type: ignore[attr-defined]
            reason=item.reason or "",  # type: ignore[attr-defined]
            message=item.message or "",  # type: ignore[attr-defined]
            object=object_ref,
            count=item.count or 1,  # type: ignore[attr-defined]
            last_seen=last_seen.isoformat() if last_seen else "",
            object_exists=_object_exists(core_api, namespace),
        )

    def xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_37(
        self, item: object, core_api: CoreV1Api, namespace: str
    ) -> NamespaceEvent:
        involved = item.involved_object  # type: ignore[attr-defined]
        object_ref = f"{involved.kind.lower()}/{involved.name}"
        last_seen = (
            item.last_timestamp or item.event_time or item.first_timestamp  # type: ignore[attr-defined]
        )
        return NamespaceEvent(
            event_type=item.type or "Normal",  # type: ignore[attr-defined]
            reason=item.reason or "",  # type: ignore[attr-defined]
            message=item.message or "",  # type: ignore[attr-defined]
            object=object_ref,
            count=item.count or 1,  # type: ignore[attr-defined]
            last_seen=last_seen.isoformat() if last_seen else "",
            object_exists=_object_exists(core_api, involved, ),
        )

mutants_xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut['_mutmut_orig'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut['xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut_1'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut['xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut_2'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut['xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut_3'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut['xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut_4'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut['xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut_5'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut['xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut_6'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut['xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut_7'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut['xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut_8'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut['xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut_9'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut['xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut_10'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut['xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut_11'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut['xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut_12'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut['xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut_13'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁlist_events__mutmut_13 # type: ignore # mutmut generated

mutants_xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut['_mutmut_orig'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut['xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_1'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut['xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_2'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut['xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_3'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut['xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_4'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut['xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_5'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut['xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_6'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut['xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_7'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut['xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_8'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut['xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_9'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut['xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_10'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut['xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_11'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut['xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_12'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut['xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_13'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut['xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_14'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_14 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut['xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_15'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_15 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut['xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_16'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_16 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut['xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_17'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_17 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut['xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_18'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_18 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut['xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_19'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_19 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut['xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_20'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_20 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut['xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_21'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_21 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut['xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_22'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_22 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut['xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_23'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_23 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut['xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_24'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_24 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut['xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_25'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_25 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut['xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_26'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_26 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut['xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_27'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_27 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut['xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_28'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_28 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut['xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_29'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_29 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut['xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_30'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_30 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut['xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_31'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_31 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut['xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_32'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_32 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut['xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_33'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_33 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut['xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_34'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_34 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut['xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_35'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_35 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut['xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_36'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_36 # type: ignore # mutmut generated
mutants_xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut['xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_37'] = KubernetesNamespaceEventsAdapter.xǁKubernetesNamespaceEventsAdapterǁ_to_namespace_event__mutmut_37 # type: ignore # mutmut generated
mutants_x__object_exists__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__object_exists__mutmut)
def _object_exists(core_api: CoreV1Api, involved: object, namespace: str) -> bool:
    """Best-effort check — only Pods are worth a lookup (cheap, common case
    for the "object no longer exists" edge case); other kinds are assumed
    to still exist rather than paying for an extra API call per event."""
    if involved.kind != "Pod":  # type: ignore[attr-defined]
        return True
    try:
        core_api.read_namespaced_pod(name=involved.name, namespace=namespace)  # type: ignore[attr-defined]
    except Exception as exc:
        return getattr(exc, "status", None) != _K8S_NOT_FOUND
    return True


def x__object_exists__mutmut_orig(core_api: CoreV1Api, involved: object, namespace: str) -> bool:
    """Best-effort check — only Pods are worth a lookup (cheap, common case
    for the "object no longer exists" edge case); other kinds are assumed
    to still exist rather than paying for an extra API call per event."""
    if involved.kind != "Pod":  # type: ignore[attr-defined]
        return True
    try:
        core_api.read_namespaced_pod(name=involved.name, namespace=namespace)  # type: ignore[attr-defined]
    except Exception as exc:
        return getattr(exc, "status", None) != _K8S_NOT_FOUND
    return True


def x__object_exists__mutmut_1(core_api: CoreV1Api, involved: object, namespace: str) -> bool:
    """Best-effort check — only Pods are worth a lookup (cheap, common case
    for the "object no longer exists" edge case); other kinds are assumed
    to still exist rather than paying for an extra API call per event."""
    if involved.kind == "Pod":  # type: ignore[attr-defined]
        return True
    try:
        core_api.read_namespaced_pod(name=involved.name, namespace=namespace)  # type: ignore[attr-defined]
    except Exception as exc:
        return getattr(exc, "status", None) != _K8S_NOT_FOUND
    return True


def x__object_exists__mutmut_2(core_api: CoreV1Api, involved: object, namespace: str) -> bool:
    """Best-effort check — only Pods are worth a lookup (cheap, common case
    for the "object no longer exists" edge case); other kinds are assumed
    to still exist rather than paying for an extra API call per event."""
    if involved.kind != "XXPodXX":  # type: ignore[attr-defined]
        return True
    try:
        core_api.read_namespaced_pod(name=involved.name, namespace=namespace)  # type: ignore[attr-defined]
    except Exception as exc:
        return getattr(exc, "status", None) != _K8S_NOT_FOUND
    return True


def x__object_exists__mutmut_3(core_api: CoreV1Api, involved: object, namespace: str) -> bool:
    """Best-effort check — only Pods are worth a lookup (cheap, common case
    for the "object no longer exists" edge case); other kinds are assumed
    to still exist rather than paying for an extra API call per event."""
    if involved.kind != "pod":  # type: ignore[attr-defined]
        return True
    try:
        core_api.read_namespaced_pod(name=involved.name, namespace=namespace)  # type: ignore[attr-defined]
    except Exception as exc:
        return getattr(exc, "status", None) != _K8S_NOT_FOUND
    return True


def x__object_exists__mutmut_4(core_api: CoreV1Api, involved: object, namespace: str) -> bool:
    """Best-effort check — only Pods are worth a lookup (cheap, common case
    for the "object no longer exists" edge case); other kinds are assumed
    to still exist rather than paying for an extra API call per event."""
    if involved.kind != "POD":  # type: ignore[attr-defined]
        return True
    try:
        core_api.read_namespaced_pod(name=involved.name, namespace=namespace)  # type: ignore[attr-defined]
    except Exception as exc:
        return getattr(exc, "status", None) != _K8S_NOT_FOUND
    return True


def x__object_exists__mutmut_5(core_api: CoreV1Api, involved: object, namespace: str) -> bool:
    """Best-effort check — only Pods are worth a lookup (cheap, common case
    for the "object no longer exists" edge case); other kinds are assumed
    to still exist rather than paying for an extra API call per event."""
    if involved.kind != "Pod":  # type: ignore[attr-defined]
        return False
    try:
        core_api.read_namespaced_pod(name=involved.name, namespace=namespace)  # type: ignore[attr-defined]
    except Exception as exc:
        return getattr(exc, "status", None) != _K8S_NOT_FOUND
    return True


def x__object_exists__mutmut_6(core_api: CoreV1Api, involved: object, namespace: str) -> bool:
    """Best-effort check — only Pods are worth a lookup (cheap, common case
    for the "object no longer exists" edge case); other kinds are assumed
    to still exist rather than paying for an extra API call per event."""
    if involved.kind != "Pod":  # type: ignore[attr-defined]
        return True
    try:
        core_api.read_namespaced_pod(name=None, namespace=namespace)  # type: ignore[attr-defined]
    except Exception as exc:
        return getattr(exc, "status", None) != _K8S_NOT_FOUND
    return True


def x__object_exists__mutmut_7(core_api: CoreV1Api, involved: object, namespace: str) -> bool:
    """Best-effort check — only Pods are worth a lookup (cheap, common case
    for the "object no longer exists" edge case); other kinds are assumed
    to still exist rather than paying for an extra API call per event."""
    if involved.kind != "Pod":  # type: ignore[attr-defined]
        return True
    try:
        core_api.read_namespaced_pod(name=involved.name, namespace=None)  # type: ignore[attr-defined]
    except Exception as exc:
        return getattr(exc, "status", None) != _K8S_NOT_FOUND
    return True


def x__object_exists__mutmut_8(core_api: CoreV1Api, involved: object, namespace: str) -> bool:
    """Best-effort check — only Pods are worth a lookup (cheap, common case
    for the "object no longer exists" edge case); other kinds are assumed
    to still exist rather than paying for an extra API call per event."""
    if involved.kind != "Pod":  # type: ignore[attr-defined]
        return True
    try:
        core_api.read_namespaced_pod(namespace=namespace)  # type: ignore[attr-defined]
    except Exception as exc:
        return getattr(exc, "status", None) != _K8S_NOT_FOUND
    return True


def x__object_exists__mutmut_9(core_api: CoreV1Api, involved: object, namespace: str) -> bool:
    """Best-effort check — only Pods are worth a lookup (cheap, common case
    for the "object no longer exists" edge case); other kinds are assumed
    to still exist rather than paying for an extra API call per event."""
    if involved.kind != "Pod":  # type: ignore[attr-defined]
        return True
    try:
        core_api.read_namespaced_pod(name=involved.name, )  # type: ignore[attr-defined]
    except Exception as exc:
        return getattr(exc, "status", None) != _K8S_NOT_FOUND
    return True


def x__object_exists__mutmut_10(core_api: CoreV1Api, involved: object, namespace: str) -> bool:
    """Best-effort check — only Pods are worth a lookup (cheap, common case
    for the "object no longer exists" edge case); other kinds are assumed
    to still exist rather than paying for an extra API call per event."""
    if involved.kind != "Pod":  # type: ignore[attr-defined]
        return True
    try:
        core_api.read_namespaced_pod(name=involved.name, namespace=namespace)  # type: ignore[attr-defined]
    except Exception as exc:
        return getattr(None, "status", None) != _K8S_NOT_FOUND
    return True


def x__object_exists__mutmut_11(core_api: CoreV1Api, involved: object, namespace: str) -> bool:
    """Best-effort check — only Pods are worth a lookup (cheap, common case
    for the "object no longer exists" edge case); other kinds are assumed
    to still exist rather than paying for an extra API call per event."""
    if involved.kind != "Pod":  # type: ignore[attr-defined]
        return True
    try:
        core_api.read_namespaced_pod(name=involved.name, namespace=namespace)  # type: ignore[attr-defined]
    except Exception as exc:
        return getattr(exc, None, None) != _K8S_NOT_FOUND
    return True


def x__object_exists__mutmut_12(core_api: CoreV1Api, involved: object, namespace: str) -> bool:
    """Best-effort check — only Pods are worth a lookup (cheap, common case
    for the "object no longer exists" edge case); other kinds are assumed
    to still exist rather than paying for an extra API call per event."""
    if involved.kind != "Pod":  # type: ignore[attr-defined]
        return True
    try:
        core_api.read_namespaced_pod(name=involved.name, namespace=namespace)  # type: ignore[attr-defined]
    except Exception as exc:
        return getattr("status", None) != _K8S_NOT_FOUND
    return True


def x__object_exists__mutmut_13(core_api: CoreV1Api, involved: object, namespace: str) -> bool:
    """Best-effort check — only Pods are worth a lookup (cheap, common case
    for the "object no longer exists" edge case); other kinds are assumed
    to still exist rather than paying for an extra API call per event."""
    if involved.kind != "Pod":  # type: ignore[attr-defined]
        return True
    try:
        core_api.read_namespaced_pod(name=involved.name, namespace=namespace)  # type: ignore[attr-defined]
    except Exception as exc:
        return getattr(exc, None) != _K8S_NOT_FOUND
    return True


def x__object_exists__mutmut_14(core_api: CoreV1Api, involved: object, namespace: str) -> bool:
    """Best-effort check — only Pods are worth a lookup (cheap, common case
    for the "object no longer exists" edge case); other kinds are assumed
    to still exist rather than paying for an extra API call per event."""
    if involved.kind != "Pod":  # type: ignore[attr-defined]
        return True
    try:
        core_api.read_namespaced_pod(name=involved.name, namespace=namespace)  # type: ignore[attr-defined]
    except Exception as exc:
        return getattr(exc, "status", ) != _K8S_NOT_FOUND
    return True


def x__object_exists__mutmut_15(core_api: CoreV1Api, involved: object, namespace: str) -> bool:
    """Best-effort check — only Pods are worth a lookup (cheap, common case
    for the "object no longer exists" edge case); other kinds are assumed
    to still exist rather than paying for an extra API call per event."""
    if involved.kind != "Pod":  # type: ignore[attr-defined]
        return True
    try:
        core_api.read_namespaced_pod(name=involved.name, namespace=namespace)  # type: ignore[attr-defined]
    except Exception as exc:
        return getattr(exc, "XXstatusXX", None) != _K8S_NOT_FOUND
    return True


def x__object_exists__mutmut_16(core_api: CoreV1Api, involved: object, namespace: str) -> bool:
    """Best-effort check — only Pods are worth a lookup (cheap, common case
    for the "object no longer exists" edge case); other kinds are assumed
    to still exist rather than paying for an extra API call per event."""
    if involved.kind != "Pod":  # type: ignore[attr-defined]
        return True
    try:
        core_api.read_namespaced_pod(name=involved.name, namespace=namespace)  # type: ignore[attr-defined]
    except Exception as exc:
        return getattr(exc, "STATUS", None) != _K8S_NOT_FOUND
    return True


def x__object_exists__mutmut_17(core_api: CoreV1Api, involved: object, namespace: str) -> bool:
    """Best-effort check — only Pods are worth a lookup (cheap, common case
    for the "object no longer exists" edge case); other kinds are assumed
    to still exist rather than paying for an extra API call per event."""
    if involved.kind != "Pod":  # type: ignore[attr-defined]
        return True
    try:
        core_api.read_namespaced_pod(name=involved.name, namespace=namespace)  # type: ignore[attr-defined]
    except Exception as exc:
        return getattr(exc, "status", None) == _K8S_NOT_FOUND
    return True


def x__object_exists__mutmut_18(core_api: CoreV1Api, involved: object, namespace: str) -> bool:
    """Best-effort check — only Pods are worth a lookup (cheap, common case
    for the "object no longer exists" edge case); other kinds are assumed
    to still exist rather than paying for an extra API call per event."""
    if involved.kind != "Pod":  # type: ignore[attr-defined]
        return True
    try:
        core_api.read_namespaced_pod(name=involved.name, namespace=namespace)  # type: ignore[attr-defined]
    except Exception as exc:
        return getattr(exc, "status", None) != _K8S_NOT_FOUND
    return False

mutants_x__object_exists__mutmut['_mutmut_orig'] = x__object_exists__mutmut_orig # type: ignore # mutmut generated
mutants_x__object_exists__mutmut['x__object_exists__mutmut_1'] = x__object_exists__mutmut_1 # type: ignore # mutmut generated
mutants_x__object_exists__mutmut['x__object_exists__mutmut_2'] = x__object_exists__mutmut_2 # type: ignore # mutmut generated
mutants_x__object_exists__mutmut['x__object_exists__mutmut_3'] = x__object_exists__mutmut_3 # type: ignore # mutmut generated
mutants_x__object_exists__mutmut['x__object_exists__mutmut_4'] = x__object_exists__mutmut_4 # type: ignore # mutmut generated
mutants_x__object_exists__mutmut['x__object_exists__mutmut_5'] = x__object_exists__mutmut_5 # type: ignore # mutmut generated
mutants_x__object_exists__mutmut['x__object_exists__mutmut_6'] = x__object_exists__mutmut_6 # type: ignore # mutmut generated
mutants_x__object_exists__mutmut['x__object_exists__mutmut_7'] = x__object_exists__mutmut_7 # type: ignore # mutmut generated
mutants_x__object_exists__mutmut['x__object_exists__mutmut_8'] = x__object_exists__mutmut_8 # type: ignore # mutmut generated
mutants_x__object_exists__mutmut['x__object_exists__mutmut_9'] = x__object_exists__mutmut_9 # type: ignore # mutmut generated
mutants_x__object_exists__mutmut['x__object_exists__mutmut_10'] = x__object_exists__mutmut_10 # type: ignore # mutmut generated
mutants_x__object_exists__mutmut['x__object_exists__mutmut_11'] = x__object_exists__mutmut_11 # type: ignore # mutmut generated
mutants_x__object_exists__mutmut['x__object_exists__mutmut_12'] = x__object_exists__mutmut_12 # type: ignore # mutmut generated
mutants_x__object_exists__mutmut['x__object_exists__mutmut_13'] = x__object_exists__mutmut_13 # type: ignore # mutmut generated
mutants_x__object_exists__mutmut['x__object_exists__mutmut_14'] = x__object_exists__mutmut_14 # type: ignore # mutmut generated
mutants_x__object_exists__mutmut['x__object_exists__mutmut_15'] = x__object_exists__mutmut_15 # type: ignore # mutmut generated
mutants_x__object_exists__mutmut['x__object_exists__mutmut_16'] = x__object_exists__mutmut_16 # type: ignore # mutmut generated
mutants_x__object_exists__mutmut['x__object_exists__mutmut_17'] = x__object_exists__mutmut_17 # type: ignore # mutmut generated
mutants_x__object_exists__mutmut['x__object_exists__mutmut_18'] = x__object_exists__mutmut_18 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__translate_error__mutmut)
def _translate_error(exc: Exception, request: GetNamespaceEventsRequest) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {request.namespace!r} not found", context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to events in namespace {request.namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot list events in namespace {request.namespace!r}: {exc}")


def x__translate_error__mutmut_orig(exc: Exception, request: GetNamespaceEventsRequest) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {request.namespace!r} not found", context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to events in namespace {request.namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot list events in namespace {request.namespace!r}: {exc}")


def x__translate_error__mutmut_1(exc: Exception, request: GetNamespaceEventsRequest) -> Exception:
    status = None
    context = {"namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {request.namespace!r} not found", context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to events in namespace {request.namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot list events in namespace {request.namespace!r}: {exc}")


def x__translate_error__mutmut_2(exc: Exception, request: GetNamespaceEventsRequest) -> Exception:
    status = getattr(None, "status", None)
    context = {"namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {request.namespace!r} not found", context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to events in namespace {request.namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot list events in namespace {request.namespace!r}: {exc}")


def x__translate_error__mutmut_3(exc: Exception, request: GetNamespaceEventsRequest) -> Exception:
    status = getattr(exc, None, None)
    context = {"namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {request.namespace!r} not found", context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to events in namespace {request.namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot list events in namespace {request.namespace!r}: {exc}")


def x__translate_error__mutmut_4(exc: Exception, request: GetNamespaceEventsRequest) -> Exception:
    status = getattr("status", None)
    context = {"namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {request.namespace!r} not found", context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to events in namespace {request.namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot list events in namespace {request.namespace!r}: {exc}")


def x__translate_error__mutmut_5(exc: Exception, request: GetNamespaceEventsRequest) -> Exception:
    status = getattr(exc, None)
    context = {"namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {request.namespace!r} not found", context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to events in namespace {request.namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot list events in namespace {request.namespace!r}: {exc}")


def x__translate_error__mutmut_6(exc: Exception, request: GetNamespaceEventsRequest) -> Exception:
    status = getattr(exc, "status", )
    context = {"namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {request.namespace!r} not found", context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to events in namespace {request.namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot list events in namespace {request.namespace!r}: {exc}")


def x__translate_error__mutmut_7(exc: Exception, request: GetNamespaceEventsRequest) -> Exception:
    status = getattr(exc, "XXstatusXX", None)
    context = {"namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {request.namespace!r} not found", context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to events in namespace {request.namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot list events in namespace {request.namespace!r}: {exc}")


def x__translate_error__mutmut_8(exc: Exception, request: GetNamespaceEventsRequest) -> Exception:
    status = getattr(exc, "STATUS", None)
    context = {"namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {request.namespace!r} not found", context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to events in namespace {request.namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot list events in namespace {request.namespace!r}: {exc}")


def x__translate_error__mutmut_9(exc: Exception, request: GetNamespaceEventsRequest) -> Exception:
    status = getattr(exc, "status", None)
    context = None
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {request.namespace!r} not found", context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to events in namespace {request.namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot list events in namespace {request.namespace!r}: {exc}")


def x__translate_error__mutmut_10(exc: Exception, request: GetNamespaceEventsRequest) -> Exception:
    status = getattr(exc, "status", None)
    context = {"XXnamespaceXX": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {request.namespace!r} not found", context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to events in namespace {request.namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot list events in namespace {request.namespace!r}: {exc}")


def x__translate_error__mutmut_11(exc: Exception, request: GetNamespaceEventsRequest) -> Exception:
    status = getattr(exc, "status", None)
    context = {"NAMESPACE": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {request.namespace!r} not found", context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to events in namespace {request.namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot list events in namespace {request.namespace!r}: {exc}")


def x__translate_error__mutmut_12(exc: Exception, request: GetNamespaceEventsRequest) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": request.namespace}
    if status != _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {request.namespace!r} not found", context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to events in namespace {request.namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot list events in namespace {request.namespace!r}: {exc}")


def x__translate_error__mutmut_13(exc: Exception, request: GetNamespaceEventsRequest) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(None, context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to events in namespace {request.namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot list events in namespace {request.namespace!r}: {exc}")


def x__translate_error__mutmut_14(exc: Exception, request: GetNamespaceEventsRequest) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {request.namespace!r} not found", context=None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to events in namespace {request.namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot list events in namespace {request.namespace!r}: {exc}")


def x__translate_error__mutmut_15(exc: Exception, request: GetNamespaceEventsRequest) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to events in namespace {request.namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot list events in namespace {request.namespace!r}: {exc}")


def x__translate_error__mutmut_16(exc: Exception, request: GetNamespaceEventsRequest) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {request.namespace!r} not found", )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to events in namespace {request.namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot list events in namespace {request.namespace!r}: {exc}")


def x__translate_error__mutmut_17(exc: Exception, request: GetNamespaceEventsRequest) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {request.namespace!r} not found", context=context)
    if status != _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to events in namespace {request.namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot list events in namespace {request.namespace!r}: {exc}")


def x__translate_error__mutmut_18(exc: Exception, request: GetNamespaceEventsRequest) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {request.namespace!r} not found", context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            None, context=context
        )
    return ClusterUnreachableError(f"Cannot list events in namespace {request.namespace!r}: {exc}")


def x__translate_error__mutmut_19(exc: Exception, request: GetNamespaceEventsRequest) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {request.namespace!r} not found", context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to events in namespace {request.namespace!r}", context=None
        )
    return ClusterUnreachableError(f"Cannot list events in namespace {request.namespace!r}: {exc}")


def x__translate_error__mutmut_20(exc: Exception, request: GetNamespaceEventsRequest) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {request.namespace!r} not found", context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            context=context
        )
    return ClusterUnreachableError(f"Cannot list events in namespace {request.namespace!r}: {exc}")


def x__translate_error__mutmut_21(exc: Exception, request: GetNamespaceEventsRequest) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {request.namespace!r} not found", context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to events in namespace {request.namespace!r}", )
    return ClusterUnreachableError(f"Cannot list events in namespace {request.namespace!r}: {exc}")


def x__translate_error__mutmut_22(exc: Exception, request: GetNamespaceEventsRequest) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(f"Namespace {request.namespace!r} not found", context=context)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to events in namespace {request.namespace!r}", context=context
        )
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
mutants_x__translate_error__mutmut['x__translate_error__mutmut_15'] = x__translate_error__mutmut_15 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_16'] = x__translate_error__mutmut_16 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_17'] = x__translate_error__mutmut_17 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_18'] = x__translate_error__mutmut_18 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_19'] = x__translate_error__mutmut_19 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_20'] = x__translate_error__mutmut_20 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_21'] = x__translate_error__mutmut_21 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_22'] = x__translate_error__mutmut_22 # type: ignore # mutmut generated
