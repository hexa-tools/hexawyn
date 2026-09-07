from __future__ import annotations

from collections.abc import Mapping
from typing import Protocol

from hexawyn.application.ports.driven.machine_config_pool_port import (
    MachineConfigPoolPort,
    MachineConfigPoolRawData,
)
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    InsufficientPermissionsError,
    MachineConfigPoolCRDNotFoundError,
)

_MCO_GROUP = "machineconfiguration.openshift.io"
_API_VERSION = "v1"
_MCP_PLURAL = "machineconfigpools"
_FORBIDDEN = 403
_NOT_FOUND = 404
_CONDITION_TRUE = "True"


class CustomObjectsApi(Protocol):
    """Minimal contract for the kubernetes CustomObjectsApi used here."""

    def list_cluster_custom_object(
        self, group: str, version: str, plural: str
    ) -> Mapping[str, object]: ...


class OpenShiftMachineConfigAdapter(MachineConfigPoolPort):
    """Reads MachineConfigPools from the machineconfiguration.openshift.io/v1 API.

    Parses machine counts, the current/desired rendered MachineConfig, the
    spec.paused flag, and the Updating / Degraded conditions (with reason and
    lastTransitionTime) into a flat, domain-friendly shape. Infrastructure
    exceptions never escape: they are translated to HexawynError subclasses.
    """

    def __init__(self, custom_objects_api: CustomObjectsApi | None = None) -> None:
        self._api = custom_objects_api

    def list_machine_config_pools(self) -> list[MachineConfigPoolRawData]:
        api = self._api_or_create()
        try:
            payload = api.list_cluster_custom_object(
                group=_MCO_GROUP,
                version=_API_VERSION,
                plural=_MCP_PLURAL,
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
        return MachineConfigPoolCRDNotFoundError()
    if status == _FORBIDDEN:
        return InsufficientPermissionsError(
            "RBAC denied access to machineconfigpools",
            context={"resource": _MCP_PLURAL},
        )
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading machineconfigpools: {exc}"
    )


def _items(payload: Mapping[str, object]) -> list[Mapping[str, object]]:
    raw = payload.get("items")
    if not isinstance(raw, list):
        return []
    return [item for item in raw if isinstance(item, Mapping)]


def _to_raw(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = _conditions(status)

    updating_condition = _find_condition(conditions, "Updating")
    degraded_condition = _find_condition(conditions, "Degraded")

    return MachineConfigPoolRawData(
        name=str(metadata.get("name", "")),
        machine_count=_as_int(status.get("machineCount")),
        ready_machine_count=_as_int(status.get("readyMachineCount")),
        updated_machine_count=_as_int(status.get("updatedMachineCount")),
        degraded_machine_count=_as_int(status.get("degradedMachineCount")),
        updating=_is_true(updating_condition),
        degraded=_is_true(degraded_condition),
        paused=bool(spec.get("paused", False)),
        current_config=str(_mapping(status, "configuration").get("name", "")),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def _mapping(item: Mapping[str, object], key: str) -> Mapping[str, object]:
    value = item.get(key)
    return value if isinstance(value, Mapping) else {}


def _conditions(status: Mapping[str, object]) -> list[Mapping[str, object]]:
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


def _is_true(condition: Mapping[str, object] | None) -> bool:
    return condition is not None and str(condition.get("status", "")) == _CONDITION_TRUE


def _reason(condition: Mapping[str, object] | None) -> str:
    return str(condition.get("reason", "")) if condition is not None else ""


def _transition_time(condition: Mapping[str, object] | None) -> str | None:
    if condition is None or not _is_true(condition):
        return None
    last_transition = condition.get("lastTransitionTime")
    return str(last_transition) if last_transition else None


def _as_int(value: object) -> int:
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value)
    return 0
