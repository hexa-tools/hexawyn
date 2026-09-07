from __future__ import annotations

from collections.abc import Mapping
from typing import Protocol

from hexawyn.application.ports.driven.cluster_operator_status_port import (
    ClusterOperatorRawData,
    ClusterOperatorStatusPort,
)
from hexawyn.domain.errors import (
    ClusterOperatorCRDNotFoundError,
    ClusterUnreachableError,
    InsufficientPermissionsError,
)

_CONFIG_GROUP = "config.openshift.io"
_API_VERSION = "v1"
_CLUSTER_OPERATORS_PLURAL = "clusteroperators"
_FORBIDDEN = 403
_NOT_FOUND = 404
_CONDITION_TRUE = "True"
_CONDITION_UNKNOWN = "Unknown"


class CustomObjectsApi(Protocol):
    """Minimal contract for the kubernetes CustomObjectsApi used here."""

    def list_cluster_custom_object(
        self, group: str, version: str, plural: str
    ) -> Mapping[str, object]: ...


class OpenShiftClusterOperatorAdapter(ClusterOperatorStatusPort):
    """Reads ClusterOperators from the config.openshift.io/v1 API group.

    Parses the Available / Progressing / Degraded conditions into a flat,
    domain-friendly shape. Infrastructure exceptions never escape: they are
    translated to HexawynError subclasses.
    """

    def __init__(self, custom_objects_api: CustomObjectsApi | None = None) -> None:
        self._api = custom_objects_api

    def list_cluster_operators(self) -> list[ClusterOperatorRawData]:
        api = self._api_or_create()
        try:
            payload = api.list_cluster_custom_object(
                group=_CONFIG_GROUP,
                version=_API_VERSION,
                plural=_CLUSTER_OPERATORS_PLURAL,
            )
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_raw(item) for item in _items(payload)]

    def _api_or_create(self) -> CustomObjectsApi:
        if self._api is None:
            from kubernetes import client as k8s

            self._api = k8s.CustomObjectsApi()
        return self._api


def _translate_error(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _NOT_FOUND:
        return ClusterOperatorCRDNotFoundError()
    if status == _FORBIDDEN:
        return InsufficientPermissionsError(
            "RBAC denied access to clusteroperators",
            context={"resource": _CLUSTER_OPERATORS_PLURAL},
        )
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading clusteroperators: {exc}"
    )


def _items(payload: Mapping[str, object]) -> list[Mapping[str, object]]:
    raw = payload.get("items")
    if not isinstance(raw, list):
        return []
    return [item for item in raw if isinstance(item, Mapping)]


def _to_raw(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(conditions, "Available")
    return ClusterOperatorRawData(
        name=str(meta.get("name", "")),
        available=available_status == _CONDITION_TRUE,
        progressing=_condition_status(conditions, "Progressing") == _CONDITION_TRUE,
        degraded=_condition_status(conditions, "Degraded") == _CONDITION_TRUE,
        available_unknown=available_status == _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def _conditions(item: Mapping[str, object]) -> list[Mapping[str, object]]:
    status = item.get("status")
    if not isinstance(status, Mapping):
        return []
    raw = status.get("conditions")
    if not isinstance(raw, list):
        return []
    return [condition for condition in raw if isinstance(condition, Mapping)]


def _find_condition(
    conditions: list[Mapping[str, object]], condition_type: str
) -> Mapping[str, object] | None:
    for condition in conditions:
        if str(condition.get("type", "")) == condition_type:
            return condition
    return None


def _condition_status(conditions: list[Mapping[str, object]], condition_type: str) -> str:
    condition = _find_condition(conditions, condition_type)
    return str(condition.get("status", "")) if condition is not None else ""


def _root_cause_message(conditions: list[Mapping[str, object]]) -> str:
    for condition_type in ("Degraded", "Progressing", "Available"):
        condition = _find_condition(conditions, condition_type)
        if condition is None:
            continue
        message = str(condition.get("message", ""))
        if message:
            return message
    return ""


def _degraded_since(conditions: list[Mapping[str, object]]) -> str | None:
    condition = _find_condition(conditions, "Degraded")
    if condition is None or str(condition.get("status", "")) != _CONDITION_TRUE:
        return None
    last_transition = condition.get("lastTransitionTime")
    return str(last_transition) if last_transition else None
