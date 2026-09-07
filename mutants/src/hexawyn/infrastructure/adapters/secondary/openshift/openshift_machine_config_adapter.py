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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class CustomObjectsApi(Protocol):
    """Minimal contract for the kubernetes CustomObjectsApi used here."""

    def list_cluster_custom_object(
        self, group: str, version: str, plural: str
    ) -> Mapping[str, object]: ...
mutants_xǁOpenShiftMachineConfigAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut: MutantDict = {}  # type: ignore
mutants_xǁOpenShiftMachineConfigAdapterǁ_api_or_create__mutmut: MutantDict = {}  # type: ignore


class OpenShiftMachineConfigAdapter(MachineConfigPoolPort):
    """Reads MachineConfigPools from the machineconfiguration.openshift.io/v1 API.

    Parses machine counts, the current/desired rendered MachineConfig, the
    spec.paused flag, and the Updating / Degraded conditions (with reason and
    lastTransitionTime) into a flat, domain-friendly shape. Infrastructure
    exceptions never escape: they are translated to HexawynError subclasses.
    """

    @_mutmut_mutated(mutants_xǁOpenShiftMachineConfigAdapterǁ__init____mutmut)
    def __init__(self, custom_objects_api: CustomObjectsApi | None = None) -> None:
        self._api = custom_objects_api

    def xǁOpenShiftMachineConfigAdapterǁ__init____mutmut_orig(self, custom_objects_api: CustomObjectsApi | None = None) -> None:
        self._api = custom_objects_api

    def xǁOpenShiftMachineConfigAdapterǁ__init____mutmut_1(self, custom_objects_api: CustomObjectsApi | None = None) -> None:
        self._api = None

    @_mutmut_mutated(mutants_xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut)
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

    def xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut_orig(self) -> list[MachineConfigPoolRawData]:
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

    def xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut_1(self) -> list[MachineConfigPoolRawData]:
        api = None
        try:
            payload = api.list_cluster_custom_object(
                group=_MCO_GROUP,
                version=_API_VERSION,
                plural=_MCP_PLURAL,
            )
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_raw(item) for item in _items(payload)]

    def xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut_2(self) -> list[MachineConfigPoolRawData]:
        api = self._api_or_create()
        try:
            payload = None
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_raw(item) for item in _items(payload)]

    def xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut_3(self) -> list[MachineConfigPoolRawData]:
        api = self._api_or_create()
        try:
            payload = api.list_cluster_custom_object(
                group=None,
                version=_API_VERSION,
                plural=_MCP_PLURAL,
            )
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_raw(item) for item in _items(payload)]

    def xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut_4(self) -> list[MachineConfigPoolRawData]:
        api = self._api_or_create()
        try:
            payload = api.list_cluster_custom_object(
                group=_MCO_GROUP,
                version=None,
                plural=_MCP_PLURAL,
            )
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_raw(item) for item in _items(payload)]

    def xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut_5(self) -> list[MachineConfigPoolRawData]:
        api = self._api_or_create()
        try:
            payload = api.list_cluster_custom_object(
                group=_MCO_GROUP,
                version=_API_VERSION,
                plural=None,
            )
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_raw(item) for item in _items(payload)]

    def xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut_6(self) -> list[MachineConfigPoolRawData]:
        api = self._api_or_create()
        try:
            payload = api.list_cluster_custom_object(
                version=_API_VERSION,
                plural=_MCP_PLURAL,
            )
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_raw(item) for item in _items(payload)]

    def xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut_7(self) -> list[MachineConfigPoolRawData]:
        api = self._api_or_create()
        try:
            payload = api.list_cluster_custom_object(
                group=_MCO_GROUP,
                plural=_MCP_PLURAL,
            )
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_raw(item) for item in _items(payload)]

    def xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut_8(self) -> list[MachineConfigPoolRawData]:
        api = self._api_or_create()
        try:
            payload = api.list_cluster_custom_object(
                group=_MCO_GROUP,
                version=_API_VERSION,
                )
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_raw(item) for item in _items(payload)]

    def xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut_9(self) -> list[MachineConfigPoolRawData]:
        api = self._api_or_create()
        try:
            payload = api.list_cluster_custom_object(
                group=_MCO_GROUP,
                version=_API_VERSION,
                plural=_MCP_PLURAL,
            )
        except Exception as exc:
            raise _translate_error(None) from exc

        return [_to_raw(item) for item in _items(payload)]

    def xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut_10(self) -> list[MachineConfigPoolRawData]:
        api = self._api_or_create()
        try:
            payload = api.list_cluster_custom_object(
                group=_MCO_GROUP,
                version=_API_VERSION,
                plural=_MCP_PLURAL,
            )
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_raw(None) for item in _items(payload)]

    def xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut_11(self) -> list[MachineConfigPoolRawData]:
        api = self._api_or_create()
        try:
            payload = api.list_cluster_custom_object(
                group=_MCO_GROUP,
                version=_API_VERSION,
                plural=_MCP_PLURAL,
            )
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_raw(item) for item in _items(None)]

    @_mutmut_mutated(mutants_xǁOpenShiftMachineConfigAdapterǁ_api_or_create__mutmut)
    def _api_or_create(self) -> CustomObjectsApi:
        if self._api is None:
            from kubernetes import client as k8s

            self._api = k8s.CustomObjectsApi()
        return self._api

    def xǁOpenShiftMachineConfigAdapterǁ_api_or_create__mutmut_orig(self) -> CustomObjectsApi:
        if self._api is None:
            from kubernetes import client as k8s

            self._api = k8s.CustomObjectsApi()
        return self._api

    def xǁOpenShiftMachineConfigAdapterǁ_api_or_create__mutmut_1(self) -> CustomObjectsApi:
        if self._api is not None:
            from kubernetes import client as k8s

            self._api = k8s.CustomObjectsApi()
        return self._api

    def xǁOpenShiftMachineConfigAdapterǁ_api_or_create__mutmut_2(self) -> CustomObjectsApi:
        if self._api is None:
            from kubernetes import client as k8s

            self._api = None
        return self._api

mutants_xǁOpenShiftMachineConfigAdapterǁ__init____mutmut['_mutmut_orig'] = OpenShiftMachineConfigAdapter.xǁOpenShiftMachineConfigAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenShiftMachineConfigAdapterǁ__init____mutmut['xǁOpenShiftMachineConfigAdapterǁ__init____mutmut_1'] = OpenShiftMachineConfigAdapter.xǁOpenShiftMachineConfigAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut['_mutmut_orig'] = OpenShiftMachineConfigAdapter.xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut['xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut_1'] = OpenShiftMachineConfigAdapter.xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut['xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut_2'] = OpenShiftMachineConfigAdapter.xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut['xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut_3'] = OpenShiftMachineConfigAdapter.xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut['xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut_4'] = OpenShiftMachineConfigAdapter.xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut['xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut_5'] = OpenShiftMachineConfigAdapter.xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut['xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut_6'] = OpenShiftMachineConfigAdapter.xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut_6 # type: ignore # mutmut generated
mutants_xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut['xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut_7'] = OpenShiftMachineConfigAdapter.xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut_7 # type: ignore # mutmut generated
mutants_xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut['xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut_8'] = OpenShiftMachineConfigAdapter.xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut_8 # type: ignore # mutmut generated
mutants_xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut['xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut_9'] = OpenShiftMachineConfigAdapter.xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut_9 # type: ignore # mutmut generated
mutants_xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut['xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut_10'] = OpenShiftMachineConfigAdapter.xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut_10 # type: ignore # mutmut generated
mutants_xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut['xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut_11'] = OpenShiftMachineConfigAdapter.xǁOpenShiftMachineConfigAdapterǁlist_machine_config_pools__mutmut_11 # type: ignore # mutmut generated

mutants_xǁOpenShiftMachineConfigAdapterǁ_api_or_create__mutmut['_mutmut_orig'] = OpenShiftMachineConfigAdapter.xǁOpenShiftMachineConfigAdapterǁ_api_or_create__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenShiftMachineConfigAdapterǁ_api_or_create__mutmut['xǁOpenShiftMachineConfigAdapterǁ_api_or_create__mutmut_1'] = OpenShiftMachineConfigAdapter.xǁOpenShiftMachineConfigAdapterǁ_api_or_create__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOpenShiftMachineConfigAdapterǁ_api_or_create__mutmut['xǁOpenShiftMachineConfigAdapterǁ_api_or_create__mutmut_2'] = OpenShiftMachineConfigAdapter.xǁOpenShiftMachineConfigAdapterǁ_api_or_create__mutmut_2 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__translate_error__mutmut)
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


def x__translate_error__mutmut_orig(exc: Exception) -> Exception:
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


def x__translate_error__mutmut_1(exc: Exception) -> Exception:
    status = None
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


def x__translate_error__mutmut_2(exc: Exception) -> Exception:
    status = getattr(None, "status", None)
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


def x__translate_error__mutmut_3(exc: Exception) -> Exception:
    status = getattr(exc, None, None)
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


def x__translate_error__mutmut_4(exc: Exception) -> Exception:
    status = getattr("status", None)
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


def x__translate_error__mutmut_5(exc: Exception) -> Exception:
    status = getattr(exc, None)
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


def x__translate_error__mutmut_6(exc: Exception) -> Exception:
    status = getattr(exc, "status", )
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


def x__translate_error__mutmut_7(exc: Exception) -> Exception:
    status = getattr(exc, "XXstatusXX", None)
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


def x__translate_error__mutmut_8(exc: Exception) -> Exception:
    status = getattr(exc, "STATUS", None)
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


def x__translate_error__mutmut_9(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status != _NOT_FOUND:
        return MachineConfigPoolCRDNotFoundError()
    if status == _FORBIDDEN:
        return InsufficientPermissionsError(
            "RBAC denied access to machineconfigpools",
            context={"resource": _MCP_PLURAL},
        )
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading machineconfigpools: {exc}"
    )


def x__translate_error__mutmut_10(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _NOT_FOUND:
        return MachineConfigPoolCRDNotFoundError()
    if status != _FORBIDDEN:
        return InsufficientPermissionsError(
            "RBAC denied access to machineconfigpools",
            context={"resource": _MCP_PLURAL},
        )
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading machineconfigpools: {exc}"
    )


def x__translate_error__mutmut_11(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _NOT_FOUND:
        return MachineConfigPoolCRDNotFoundError()
    if status == _FORBIDDEN:
        return InsufficientPermissionsError(
            None,
            context={"resource": _MCP_PLURAL},
        )
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading machineconfigpools: {exc}"
    )


def x__translate_error__mutmut_12(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _NOT_FOUND:
        return MachineConfigPoolCRDNotFoundError()
    if status == _FORBIDDEN:
        return InsufficientPermissionsError(
            "RBAC denied access to machineconfigpools",
            context=None,
        )
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading machineconfigpools: {exc}"
    )


def x__translate_error__mutmut_13(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _NOT_FOUND:
        return MachineConfigPoolCRDNotFoundError()
    if status == _FORBIDDEN:
        return InsufficientPermissionsError(
            context={"resource": _MCP_PLURAL},
        )
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading machineconfigpools: {exc}"
    )


def x__translate_error__mutmut_14(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _NOT_FOUND:
        return MachineConfigPoolCRDNotFoundError()
    if status == _FORBIDDEN:
        return InsufficientPermissionsError(
            "RBAC denied access to machineconfigpools",
            )
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading machineconfigpools: {exc}"
    )


def x__translate_error__mutmut_15(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _NOT_FOUND:
        return MachineConfigPoolCRDNotFoundError()
    if status == _FORBIDDEN:
        return InsufficientPermissionsError(
            "XXRBAC denied access to machineconfigpoolsXX",
            context={"resource": _MCP_PLURAL},
        )
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading machineconfigpools: {exc}"
    )


def x__translate_error__mutmut_16(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _NOT_FOUND:
        return MachineConfigPoolCRDNotFoundError()
    if status == _FORBIDDEN:
        return InsufficientPermissionsError(
            "rbac denied access to machineconfigpools",
            context={"resource": _MCP_PLURAL},
        )
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading machineconfigpools: {exc}"
    )


def x__translate_error__mutmut_17(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _NOT_FOUND:
        return MachineConfigPoolCRDNotFoundError()
    if status == _FORBIDDEN:
        return InsufficientPermissionsError(
            "RBAC DENIED ACCESS TO MACHINECONFIGPOOLS",
            context={"resource": _MCP_PLURAL},
        )
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading machineconfigpools: {exc}"
    )


def x__translate_error__mutmut_18(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _NOT_FOUND:
        return MachineConfigPoolCRDNotFoundError()
    if status == _FORBIDDEN:
        return InsufficientPermissionsError(
            "RBAC denied access to machineconfigpools",
            context={"XXresourceXX": _MCP_PLURAL},
        )
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading machineconfigpools: {exc}"
    )


def x__translate_error__mutmut_19(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _NOT_FOUND:
        return MachineConfigPoolCRDNotFoundError()
    if status == _FORBIDDEN:
        return InsufficientPermissionsError(
            "RBAC denied access to machineconfigpools",
            context={"RESOURCE": _MCP_PLURAL},
        )
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading machineconfigpools: {exc}"
    )


def x__translate_error__mutmut_20(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _NOT_FOUND:
        return MachineConfigPoolCRDNotFoundError()
    if status == _FORBIDDEN:
        return InsufficientPermissionsError(
            "RBAC denied access to machineconfigpools",
            context={"resource": _MCP_PLURAL},
        )
    return ClusterUnreachableError(
        None
    )

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
mutants_x__to_raw__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_raw__mutmut)
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


def x__to_raw__mutmut_orig(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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


def x__to_raw__mutmut_1(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = None
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


def x__to_raw__mutmut_2(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(None, "metadata")
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


def x__to_raw__mutmut_3(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, None)
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


def x__to_raw__mutmut_4(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping("metadata")
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


def x__to_raw__mutmut_5(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, )
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


def x__to_raw__mutmut_6(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "XXmetadataXX")
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


def x__to_raw__mutmut_7(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "METADATA")
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


def x__to_raw__mutmut_8(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = None
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


def x__to_raw__mutmut_9(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(None, "spec")
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


def x__to_raw__mutmut_10(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, None)
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


def x__to_raw__mutmut_11(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping("spec")
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


def x__to_raw__mutmut_12(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, )
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


def x__to_raw__mutmut_13(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "XXspecXX")
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


def x__to_raw__mutmut_14(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "SPEC")
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


def x__to_raw__mutmut_15(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = None
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


def x__to_raw__mutmut_16(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(None, "status")
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


def x__to_raw__mutmut_17(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, None)
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


def x__to_raw__mutmut_18(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping("status")
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


def x__to_raw__mutmut_19(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, )
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


def x__to_raw__mutmut_20(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "XXstatusXX")
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


def x__to_raw__mutmut_21(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "STATUS")
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


def x__to_raw__mutmut_22(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = None

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


def x__to_raw__mutmut_23(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = _conditions(None)

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


def x__to_raw__mutmut_24(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = _conditions(status)

    updating_condition = None
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


def x__to_raw__mutmut_25(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = _conditions(status)

    updating_condition = _find_condition(None, "Updating")
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


def x__to_raw__mutmut_26(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = _conditions(status)

    updating_condition = _find_condition(conditions, None)
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


def x__to_raw__mutmut_27(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = _conditions(status)

    updating_condition = _find_condition("Updating")
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


def x__to_raw__mutmut_28(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = _conditions(status)

    updating_condition = _find_condition(conditions, )
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


def x__to_raw__mutmut_29(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = _conditions(status)

    updating_condition = _find_condition(conditions, "XXUpdatingXX")
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


def x__to_raw__mutmut_30(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = _conditions(status)

    updating_condition = _find_condition(conditions, "updating")
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


def x__to_raw__mutmut_31(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = _conditions(status)

    updating_condition = _find_condition(conditions, "UPDATING")
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


def x__to_raw__mutmut_32(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = _conditions(status)

    updating_condition = _find_condition(conditions, "Updating")
    degraded_condition = None

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


def x__to_raw__mutmut_33(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = _conditions(status)

    updating_condition = _find_condition(conditions, "Updating")
    degraded_condition = _find_condition(None, "Degraded")

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


def x__to_raw__mutmut_34(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = _conditions(status)

    updating_condition = _find_condition(conditions, "Updating")
    degraded_condition = _find_condition(conditions, None)

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


def x__to_raw__mutmut_35(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = _conditions(status)

    updating_condition = _find_condition(conditions, "Updating")
    degraded_condition = _find_condition("Degraded")

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


def x__to_raw__mutmut_36(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = _conditions(status)

    updating_condition = _find_condition(conditions, "Updating")
    degraded_condition = _find_condition(conditions, )

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


def x__to_raw__mutmut_37(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = _conditions(status)

    updating_condition = _find_condition(conditions, "Updating")
    degraded_condition = _find_condition(conditions, "XXDegradedXX")

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


def x__to_raw__mutmut_38(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = _conditions(status)

    updating_condition = _find_condition(conditions, "Updating")
    degraded_condition = _find_condition(conditions, "degraded")

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


def x__to_raw__mutmut_39(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = _conditions(status)

    updating_condition = _find_condition(conditions, "Updating")
    degraded_condition = _find_condition(conditions, "DEGRADED")

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


def x__to_raw__mutmut_40(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = _conditions(status)

    updating_condition = _find_condition(conditions, "Updating")
    degraded_condition = _find_condition(conditions, "Degraded")

    return MachineConfigPoolRawData(
        name=None,
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


def x__to_raw__mutmut_41(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = _conditions(status)

    updating_condition = _find_condition(conditions, "Updating")
    degraded_condition = _find_condition(conditions, "Degraded")

    return MachineConfigPoolRawData(
        name=str(metadata.get("name", "")),
        machine_count=None,
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


def x__to_raw__mutmut_42(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = _conditions(status)

    updating_condition = _find_condition(conditions, "Updating")
    degraded_condition = _find_condition(conditions, "Degraded")

    return MachineConfigPoolRawData(
        name=str(metadata.get("name", "")),
        machine_count=_as_int(status.get("machineCount")),
        ready_machine_count=None,
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


def x__to_raw__mutmut_43(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        updated_machine_count=None,
        degraded_machine_count=_as_int(status.get("degradedMachineCount")),
        updating=_is_true(updating_condition),
        degraded=_is_true(degraded_condition),
        paused=bool(spec.get("paused", False)),
        current_config=str(_mapping(status, "configuration").get("name", "")),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_44(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        degraded_machine_count=None,
        updating=_is_true(updating_condition),
        degraded=_is_true(degraded_condition),
        paused=bool(spec.get("paused", False)),
        current_config=str(_mapping(status, "configuration").get("name", "")),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_45(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        updating=None,
        degraded=_is_true(degraded_condition),
        paused=bool(spec.get("paused", False)),
        current_config=str(_mapping(status, "configuration").get("name", "")),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_46(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        degraded=None,
        paused=bool(spec.get("paused", False)),
        current_config=str(_mapping(status, "configuration").get("name", "")),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_47(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        paused=None,
        current_config=str(_mapping(status, "configuration").get("name", "")),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_48(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        current_config=None,
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_49(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        desired_config=None,
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_50(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        reason=None,
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_51(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        updating_since=None,
    )


def x__to_raw__mutmut_52(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = _conditions(status)

    updating_condition = _find_condition(conditions, "Updating")
    degraded_condition = _find_condition(conditions, "Degraded")

    return MachineConfigPoolRawData(
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


def x__to_raw__mutmut_53(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = _conditions(status)

    updating_condition = _find_condition(conditions, "Updating")
    degraded_condition = _find_condition(conditions, "Degraded")

    return MachineConfigPoolRawData(
        name=str(metadata.get("name", "")),
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


def x__to_raw__mutmut_54(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = _conditions(status)

    updating_condition = _find_condition(conditions, "Updating")
    degraded_condition = _find_condition(conditions, "Degraded")

    return MachineConfigPoolRawData(
        name=str(metadata.get("name", "")),
        machine_count=_as_int(status.get("machineCount")),
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


def x__to_raw__mutmut_55(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        degraded_machine_count=_as_int(status.get("degradedMachineCount")),
        updating=_is_true(updating_condition),
        degraded=_is_true(degraded_condition),
        paused=bool(spec.get("paused", False)),
        current_config=str(_mapping(status, "configuration").get("name", "")),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_56(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        updating=_is_true(updating_condition),
        degraded=_is_true(degraded_condition),
        paused=bool(spec.get("paused", False)),
        current_config=str(_mapping(status, "configuration").get("name", "")),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_57(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        degraded=_is_true(degraded_condition),
        paused=bool(spec.get("paused", False)),
        current_config=str(_mapping(status, "configuration").get("name", "")),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_58(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        paused=bool(spec.get("paused", False)),
        current_config=str(_mapping(status, "configuration").get("name", "")),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_59(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        current_config=str(_mapping(status, "configuration").get("name", "")),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_60(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_61(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_62(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_63(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        )


def x__to_raw__mutmut_64(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = _conditions(status)

    updating_condition = _find_condition(conditions, "Updating")
    degraded_condition = _find_condition(conditions, "Degraded")

    return MachineConfigPoolRawData(
        name=str(None),
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


def x__to_raw__mutmut_65(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = _conditions(status)

    updating_condition = _find_condition(conditions, "Updating")
    degraded_condition = _find_condition(conditions, "Degraded")

    return MachineConfigPoolRawData(
        name=str(metadata.get(None, "")),
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


def x__to_raw__mutmut_66(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = _conditions(status)

    updating_condition = _find_condition(conditions, "Updating")
    degraded_condition = _find_condition(conditions, "Degraded")

    return MachineConfigPoolRawData(
        name=str(metadata.get("name", None)),
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


def x__to_raw__mutmut_67(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = _conditions(status)

    updating_condition = _find_condition(conditions, "Updating")
    degraded_condition = _find_condition(conditions, "Degraded")

    return MachineConfigPoolRawData(
        name=str(metadata.get("")),
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


def x__to_raw__mutmut_68(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = _conditions(status)

    updating_condition = _find_condition(conditions, "Updating")
    degraded_condition = _find_condition(conditions, "Degraded")

    return MachineConfigPoolRawData(
        name=str(metadata.get("name", )),
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


def x__to_raw__mutmut_69(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = _conditions(status)

    updating_condition = _find_condition(conditions, "Updating")
    degraded_condition = _find_condition(conditions, "Degraded")

    return MachineConfigPoolRawData(
        name=str(metadata.get("XXnameXX", "")),
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


def x__to_raw__mutmut_70(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = _conditions(status)

    updating_condition = _find_condition(conditions, "Updating")
    degraded_condition = _find_condition(conditions, "Degraded")

    return MachineConfigPoolRawData(
        name=str(metadata.get("NAME", "")),
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


def x__to_raw__mutmut_71(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = _conditions(status)

    updating_condition = _find_condition(conditions, "Updating")
    degraded_condition = _find_condition(conditions, "Degraded")

    return MachineConfigPoolRawData(
        name=str(metadata.get("name", "XXXX")),
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


def x__to_raw__mutmut_72(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = _conditions(status)

    updating_condition = _find_condition(conditions, "Updating")
    degraded_condition = _find_condition(conditions, "Degraded")

    return MachineConfigPoolRawData(
        name=str(metadata.get("name", "")),
        machine_count=_as_int(None),
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


def x__to_raw__mutmut_73(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = _conditions(status)

    updating_condition = _find_condition(conditions, "Updating")
    degraded_condition = _find_condition(conditions, "Degraded")

    return MachineConfigPoolRawData(
        name=str(metadata.get("name", "")),
        machine_count=_as_int(status.get(None)),
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


def x__to_raw__mutmut_74(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = _conditions(status)

    updating_condition = _find_condition(conditions, "Updating")
    degraded_condition = _find_condition(conditions, "Degraded")

    return MachineConfigPoolRawData(
        name=str(metadata.get("name", "")),
        machine_count=_as_int(status.get("XXmachineCountXX")),
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


def x__to_raw__mutmut_75(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = _conditions(status)

    updating_condition = _find_condition(conditions, "Updating")
    degraded_condition = _find_condition(conditions, "Degraded")

    return MachineConfigPoolRawData(
        name=str(metadata.get("name", "")),
        machine_count=_as_int(status.get("machinecount")),
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


def x__to_raw__mutmut_76(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = _conditions(status)

    updating_condition = _find_condition(conditions, "Updating")
    degraded_condition = _find_condition(conditions, "Degraded")

    return MachineConfigPoolRawData(
        name=str(metadata.get("name", "")),
        machine_count=_as_int(status.get("MACHINECOUNT")),
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


def x__to_raw__mutmut_77(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = _conditions(status)

    updating_condition = _find_condition(conditions, "Updating")
    degraded_condition = _find_condition(conditions, "Degraded")

    return MachineConfigPoolRawData(
        name=str(metadata.get("name", "")),
        machine_count=_as_int(status.get("machineCount")),
        ready_machine_count=_as_int(None),
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


def x__to_raw__mutmut_78(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = _conditions(status)

    updating_condition = _find_condition(conditions, "Updating")
    degraded_condition = _find_condition(conditions, "Degraded")

    return MachineConfigPoolRawData(
        name=str(metadata.get("name", "")),
        machine_count=_as_int(status.get("machineCount")),
        ready_machine_count=_as_int(status.get(None)),
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


def x__to_raw__mutmut_79(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = _conditions(status)

    updating_condition = _find_condition(conditions, "Updating")
    degraded_condition = _find_condition(conditions, "Degraded")

    return MachineConfigPoolRawData(
        name=str(metadata.get("name", "")),
        machine_count=_as_int(status.get("machineCount")),
        ready_machine_count=_as_int(status.get("XXreadyMachineCountXX")),
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


def x__to_raw__mutmut_80(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = _conditions(status)

    updating_condition = _find_condition(conditions, "Updating")
    degraded_condition = _find_condition(conditions, "Degraded")

    return MachineConfigPoolRawData(
        name=str(metadata.get("name", "")),
        machine_count=_as_int(status.get("machineCount")),
        ready_machine_count=_as_int(status.get("readymachinecount")),
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


def x__to_raw__mutmut_81(item: Mapping[str, object]) -> MachineConfigPoolRawData:
    metadata = _mapping(item, "metadata")
    spec = _mapping(item, "spec")
    status = _mapping(item, "status")
    conditions = _conditions(status)

    updating_condition = _find_condition(conditions, "Updating")
    degraded_condition = _find_condition(conditions, "Degraded")

    return MachineConfigPoolRawData(
        name=str(metadata.get("name", "")),
        machine_count=_as_int(status.get("machineCount")),
        ready_machine_count=_as_int(status.get("READYMACHINECOUNT")),
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


def x__to_raw__mutmut_82(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        updated_machine_count=_as_int(None),
        degraded_machine_count=_as_int(status.get("degradedMachineCount")),
        updating=_is_true(updating_condition),
        degraded=_is_true(degraded_condition),
        paused=bool(spec.get("paused", False)),
        current_config=str(_mapping(status, "configuration").get("name", "")),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_83(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        updated_machine_count=_as_int(status.get(None)),
        degraded_machine_count=_as_int(status.get("degradedMachineCount")),
        updating=_is_true(updating_condition),
        degraded=_is_true(degraded_condition),
        paused=bool(spec.get("paused", False)),
        current_config=str(_mapping(status, "configuration").get("name", "")),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_84(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        updated_machine_count=_as_int(status.get("XXupdatedMachineCountXX")),
        degraded_machine_count=_as_int(status.get("degradedMachineCount")),
        updating=_is_true(updating_condition),
        degraded=_is_true(degraded_condition),
        paused=bool(spec.get("paused", False)),
        current_config=str(_mapping(status, "configuration").get("name", "")),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_85(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        updated_machine_count=_as_int(status.get("updatedmachinecount")),
        degraded_machine_count=_as_int(status.get("degradedMachineCount")),
        updating=_is_true(updating_condition),
        degraded=_is_true(degraded_condition),
        paused=bool(spec.get("paused", False)),
        current_config=str(_mapping(status, "configuration").get("name", "")),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_86(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        updated_machine_count=_as_int(status.get("UPDATEDMACHINECOUNT")),
        degraded_machine_count=_as_int(status.get("degradedMachineCount")),
        updating=_is_true(updating_condition),
        degraded=_is_true(degraded_condition),
        paused=bool(spec.get("paused", False)),
        current_config=str(_mapping(status, "configuration").get("name", "")),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_87(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        degraded_machine_count=_as_int(None),
        updating=_is_true(updating_condition),
        degraded=_is_true(degraded_condition),
        paused=bool(spec.get("paused", False)),
        current_config=str(_mapping(status, "configuration").get("name", "")),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_88(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        degraded_machine_count=_as_int(status.get(None)),
        updating=_is_true(updating_condition),
        degraded=_is_true(degraded_condition),
        paused=bool(spec.get("paused", False)),
        current_config=str(_mapping(status, "configuration").get("name", "")),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_89(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        degraded_machine_count=_as_int(status.get("XXdegradedMachineCountXX")),
        updating=_is_true(updating_condition),
        degraded=_is_true(degraded_condition),
        paused=bool(spec.get("paused", False)),
        current_config=str(_mapping(status, "configuration").get("name", "")),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_90(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        degraded_machine_count=_as_int(status.get("degradedmachinecount")),
        updating=_is_true(updating_condition),
        degraded=_is_true(degraded_condition),
        paused=bool(spec.get("paused", False)),
        current_config=str(_mapping(status, "configuration").get("name", "")),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_91(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        degraded_machine_count=_as_int(status.get("DEGRADEDMACHINECOUNT")),
        updating=_is_true(updating_condition),
        degraded=_is_true(degraded_condition),
        paused=bool(spec.get("paused", False)),
        current_config=str(_mapping(status, "configuration").get("name", "")),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_92(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        updating=_is_true(None),
        degraded=_is_true(degraded_condition),
        paused=bool(spec.get("paused", False)),
        current_config=str(_mapping(status, "configuration").get("name", "")),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_93(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        degraded=_is_true(None),
        paused=bool(spec.get("paused", False)),
        current_config=str(_mapping(status, "configuration").get("name", "")),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_94(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        paused=bool(None),
        current_config=str(_mapping(status, "configuration").get("name", "")),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_95(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        paused=bool(spec.get(None, False)),
        current_config=str(_mapping(status, "configuration").get("name", "")),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_96(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        paused=bool(spec.get("paused", None)),
        current_config=str(_mapping(status, "configuration").get("name", "")),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_97(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        paused=bool(spec.get(False)),
        current_config=str(_mapping(status, "configuration").get("name", "")),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_98(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        paused=bool(spec.get("paused", )),
        current_config=str(_mapping(status, "configuration").get("name", "")),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_99(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        paused=bool(spec.get("XXpausedXX", False)),
        current_config=str(_mapping(status, "configuration").get("name", "")),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_100(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        paused=bool(spec.get("PAUSED", False)),
        current_config=str(_mapping(status, "configuration").get("name", "")),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_101(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        paused=bool(spec.get("paused", True)),
        current_config=str(_mapping(status, "configuration").get("name", "")),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_102(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        current_config=str(None),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_103(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        current_config=str(_mapping(status, "configuration").get(None, "")),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_104(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        current_config=str(_mapping(status, "configuration").get("name", None)),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_105(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        current_config=str(_mapping(status, "configuration").get("")),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_106(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        current_config=str(_mapping(status, "configuration").get("name", )),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_107(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        current_config=str(_mapping(None, "configuration").get("name", "")),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_108(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        current_config=str(_mapping(status, None).get("name", "")),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_109(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        current_config=str(_mapping("configuration").get("name", "")),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_110(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        current_config=str(_mapping(status, ).get("name", "")),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_111(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        current_config=str(_mapping(status, "XXconfigurationXX").get("name", "")),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_112(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        current_config=str(_mapping(status, "CONFIGURATION").get("name", "")),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_113(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        current_config=str(_mapping(status, "configuration").get("XXnameXX", "")),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_114(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        current_config=str(_mapping(status, "configuration").get("NAME", "")),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_115(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        current_config=str(_mapping(status, "configuration").get("name", "XXXX")),
        desired_config=str(_mapping(spec, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_116(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        desired_config=str(None),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_117(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        desired_config=str(_mapping(spec, "configuration").get(None, "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_118(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        desired_config=str(_mapping(spec, "configuration").get("name", None)),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_119(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        desired_config=str(_mapping(spec, "configuration").get("")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_120(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        desired_config=str(_mapping(spec, "configuration").get("name", )),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_121(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        desired_config=str(_mapping(None, "configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_122(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        desired_config=str(_mapping(spec, None).get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_123(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        desired_config=str(_mapping("configuration").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_124(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        desired_config=str(_mapping(spec, ).get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_125(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        desired_config=str(_mapping(spec, "XXconfigurationXX").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_126(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        desired_config=str(_mapping(spec, "CONFIGURATION").get("name", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_127(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        desired_config=str(_mapping(spec, "configuration").get("XXnameXX", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_128(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        desired_config=str(_mapping(spec, "configuration").get("NAME", "")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_129(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        desired_config=str(_mapping(spec, "configuration").get("name", "XXXX")),
        reason=_reason(degraded_condition),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_130(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        reason=_reason(None),
        updating_since=_transition_time(updating_condition),
    )


def x__to_raw__mutmut_131(item: Mapping[str, object]) -> MachineConfigPoolRawData:
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
        updating_since=_transition_time(None),
    )

mutants_x__to_raw__mutmut['_mutmut_orig'] = x__to_raw__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_1'] = x__to_raw__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_2'] = x__to_raw__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_3'] = x__to_raw__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_4'] = x__to_raw__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_5'] = x__to_raw__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_6'] = x__to_raw__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_7'] = x__to_raw__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_8'] = x__to_raw__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_9'] = x__to_raw__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_10'] = x__to_raw__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_11'] = x__to_raw__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_12'] = x__to_raw__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_13'] = x__to_raw__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_14'] = x__to_raw__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_15'] = x__to_raw__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_16'] = x__to_raw__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_17'] = x__to_raw__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_18'] = x__to_raw__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_19'] = x__to_raw__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_20'] = x__to_raw__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_21'] = x__to_raw__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_22'] = x__to_raw__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_23'] = x__to_raw__mutmut_23 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_24'] = x__to_raw__mutmut_24 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_25'] = x__to_raw__mutmut_25 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_26'] = x__to_raw__mutmut_26 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_27'] = x__to_raw__mutmut_27 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_28'] = x__to_raw__mutmut_28 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_29'] = x__to_raw__mutmut_29 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_30'] = x__to_raw__mutmut_30 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_31'] = x__to_raw__mutmut_31 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_32'] = x__to_raw__mutmut_32 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_33'] = x__to_raw__mutmut_33 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_34'] = x__to_raw__mutmut_34 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_35'] = x__to_raw__mutmut_35 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_36'] = x__to_raw__mutmut_36 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_37'] = x__to_raw__mutmut_37 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_38'] = x__to_raw__mutmut_38 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_39'] = x__to_raw__mutmut_39 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_40'] = x__to_raw__mutmut_40 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_41'] = x__to_raw__mutmut_41 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_42'] = x__to_raw__mutmut_42 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_43'] = x__to_raw__mutmut_43 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_44'] = x__to_raw__mutmut_44 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_45'] = x__to_raw__mutmut_45 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_46'] = x__to_raw__mutmut_46 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_47'] = x__to_raw__mutmut_47 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_48'] = x__to_raw__mutmut_48 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_49'] = x__to_raw__mutmut_49 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_50'] = x__to_raw__mutmut_50 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_51'] = x__to_raw__mutmut_51 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_52'] = x__to_raw__mutmut_52 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_53'] = x__to_raw__mutmut_53 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_54'] = x__to_raw__mutmut_54 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_55'] = x__to_raw__mutmut_55 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_56'] = x__to_raw__mutmut_56 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_57'] = x__to_raw__mutmut_57 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_58'] = x__to_raw__mutmut_58 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_59'] = x__to_raw__mutmut_59 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_60'] = x__to_raw__mutmut_60 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_61'] = x__to_raw__mutmut_61 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_62'] = x__to_raw__mutmut_62 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_63'] = x__to_raw__mutmut_63 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_64'] = x__to_raw__mutmut_64 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_65'] = x__to_raw__mutmut_65 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_66'] = x__to_raw__mutmut_66 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_67'] = x__to_raw__mutmut_67 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_68'] = x__to_raw__mutmut_68 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_69'] = x__to_raw__mutmut_69 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_70'] = x__to_raw__mutmut_70 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_71'] = x__to_raw__mutmut_71 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_72'] = x__to_raw__mutmut_72 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_73'] = x__to_raw__mutmut_73 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_74'] = x__to_raw__mutmut_74 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_75'] = x__to_raw__mutmut_75 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_76'] = x__to_raw__mutmut_76 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_77'] = x__to_raw__mutmut_77 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_78'] = x__to_raw__mutmut_78 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_79'] = x__to_raw__mutmut_79 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_80'] = x__to_raw__mutmut_80 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_81'] = x__to_raw__mutmut_81 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_82'] = x__to_raw__mutmut_82 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_83'] = x__to_raw__mutmut_83 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_84'] = x__to_raw__mutmut_84 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_85'] = x__to_raw__mutmut_85 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_86'] = x__to_raw__mutmut_86 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_87'] = x__to_raw__mutmut_87 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_88'] = x__to_raw__mutmut_88 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_89'] = x__to_raw__mutmut_89 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_90'] = x__to_raw__mutmut_90 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_91'] = x__to_raw__mutmut_91 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_92'] = x__to_raw__mutmut_92 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_93'] = x__to_raw__mutmut_93 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_94'] = x__to_raw__mutmut_94 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_95'] = x__to_raw__mutmut_95 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_96'] = x__to_raw__mutmut_96 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_97'] = x__to_raw__mutmut_97 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_98'] = x__to_raw__mutmut_98 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_99'] = x__to_raw__mutmut_99 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_100'] = x__to_raw__mutmut_100 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_101'] = x__to_raw__mutmut_101 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_102'] = x__to_raw__mutmut_102 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_103'] = x__to_raw__mutmut_103 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_104'] = x__to_raw__mutmut_104 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_105'] = x__to_raw__mutmut_105 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_106'] = x__to_raw__mutmut_106 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_107'] = x__to_raw__mutmut_107 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_108'] = x__to_raw__mutmut_108 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_109'] = x__to_raw__mutmut_109 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_110'] = x__to_raw__mutmut_110 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_111'] = x__to_raw__mutmut_111 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_112'] = x__to_raw__mutmut_112 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_113'] = x__to_raw__mutmut_113 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_114'] = x__to_raw__mutmut_114 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_115'] = x__to_raw__mutmut_115 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_116'] = x__to_raw__mutmut_116 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_117'] = x__to_raw__mutmut_117 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_118'] = x__to_raw__mutmut_118 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_119'] = x__to_raw__mutmut_119 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_120'] = x__to_raw__mutmut_120 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_121'] = x__to_raw__mutmut_121 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_122'] = x__to_raw__mutmut_122 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_123'] = x__to_raw__mutmut_123 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_124'] = x__to_raw__mutmut_124 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_125'] = x__to_raw__mutmut_125 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_126'] = x__to_raw__mutmut_126 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_127'] = x__to_raw__mutmut_127 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_128'] = x__to_raw__mutmut_128 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_129'] = x__to_raw__mutmut_129 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_130'] = x__to_raw__mutmut_130 # type: ignore # mutmut generated
mutants_x__to_raw__mutmut['x__to_raw__mutmut_131'] = x__to_raw__mutmut_131 # type: ignore # mutmut generated
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
mutants_x__conditions__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__conditions__mutmut)
def _conditions(status: Mapping[str, object]) -> list[Mapping[str, object]]:
    raw = status.get("conditions")
    if not isinstance(raw, list):
        return []
    return [condition for condition in raw if isinstance(condition, Mapping)]


def x__conditions__mutmut_orig(status: Mapping[str, object]) -> list[Mapping[str, object]]:
    raw = status.get("conditions")
    if not isinstance(raw, list):
        return []
    return [condition for condition in raw if isinstance(condition, Mapping)]


def x__conditions__mutmut_1(status: Mapping[str, object]) -> list[Mapping[str, object]]:
    raw = None
    if not isinstance(raw, list):
        return []
    return [condition for condition in raw if isinstance(condition, Mapping)]


def x__conditions__mutmut_2(status: Mapping[str, object]) -> list[Mapping[str, object]]:
    raw = status.get(None)
    if not isinstance(raw, list):
        return []
    return [condition for condition in raw if isinstance(condition, Mapping)]


def x__conditions__mutmut_3(status: Mapping[str, object]) -> list[Mapping[str, object]]:
    raw = status.get("XXconditionsXX")
    if not isinstance(raw, list):
        return []
    return [condition for condition in raw if isinstance(condition, Mapping)]


def x__conditions__mutmut_4(status: Mapping[str, object]) -> list[Mapping[str, object]]:
    raw = status.get("CONDITIONS")
    if not isinstance(raw, list):
        return []
    return [condition for condition in raw if isinstance(condition, Mapping)]


def x__conditions__mutmut_5(status: Mapping[str, object]) -> list[Mapping[str, object]]:
    raw = status.get("conditions")
    if isinstance(raw, list):
        return []
    return [condition for condition in raw if isinstance(condition, Mapping)]

mutants_x__conditions__mutmut['_mutmut_orig'] = x__conditions__mutmut_orig # type: ignore # mutmut generated
mutants_x__conditions__mutmut['x__conditions__mutmut_1'] = x__conditions__mutmut_1 # type: ignore # mutmut generated
mutants_x__conditions__mutmut['x__conditions__mutmut_2'] = x__conditions__mutmut_2 # type: ignore # mutmut generated
mutants_x__conditions__mutmut['x__conditions__mutmut_3'] = x__conditions__mutmut_3 # type: ignore # mutmut generated
mutants_x__conditions__mutmut['x__conditions__mutmut_4'] = x__conditions__mutmut_4 # type: ignore # mutmut generated
mutants_x__conditions__mutmut['x__conditions__mutmut_5'] = x__conditions__mutmut_5 # type: ignore # mutmut generated
mutants_x__find_condition__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__find_condition__mutmut)
def _find_condition(
    conditions: list[Mapping[str, object]], condition_type: str
) -> Mapping[str, object] | None:
    for condition in conditions:
        if str(condition.get("type", "")) == condition_type:
            return condition
    return None


def x__find_condition__mutmut_orig(
    conditions: list[Mapping[str, object]], condition_type: str
) -> Mapping[str, object] | None:
    for condition in conditions:
        if str(condition.get("type", "")) == condition_type:
            return condition
    return None


def x__find_condition__mutmut_1(
    conditions: list[Mapping[str, object]], condition_type: str
) -> Mapping[str, object] | None:
    for condition in conditions:
        if str(None) == condition_type:
            return condition
    return None


def x__find_condition__mutmut_2(
    conditions: list[Mapping[str, object]], condition_type: str
) -> Mapping[str, object] | None:
    for condition in conditions:
        if str(condition.get(None, "")) == condition_type:
            return condition
    return None


def x__find_condition__mutmut_3(
    conditions: list[Mapping[str, object]], condition_type: str
) -> Mapping[str, object] | None:
    for condition in conditions:
        if str(condition.get("type", None)) == condition_type:
            return condition
    return None


def x__find_condition__mutmut_4(
    conditions: list[Mapping[str, object]], condition_type: str
) -> Mapping[str, object] | None:
    for condition in conditions:
        if str(condition.get("")) == condition_type:
            return condition
    return None


def x__find_condition__mutmut_5(
    conditions: list[Mapping[str, object]], condition_type: str
) -> Mapping[str, object] | None:
    for condition in conditions:
        if str(condition.get("type", )) == condition_type:
            return condition
    return None


def x__find_condition__mutmut_6(
    conditions: list[Mapping[str, object]], condition_type: str
) -> Mapping[str, object] | None:
    for condition in conditions:
        if str(condition.get("XXtypeXX", "")) == condition_type:
            return condition
    return None


def x__find_condition__mutmut_7(
    conditions: list[Mapping[str, object]], condition_type: str
) -> Mapping[str, object] | None:
    for condition in conditions:
        if str(condition.get("TYPE", "")) == condition_type:
            return condition
    return None


def x__find_condition__mutmut_8(
    conditions: list[Mapping[str, object]], condition_type: str
) -> Mapping[str, object] | None:
    for condition in conditions:
        if str(condition.get("type", "XXXX")) == condition_type:
            return condition
    return None


def x__find_condition__mutmut_9(
    conditions: list[Mapping[str, object]], condition_type: str
) -> Mapping[str, object] | None:
    for condition in conditions:
        if str(condition.get("type", "")) != condition_type:
            return condition
    return None

mutants_x__find_condition__mutmut['_mutmut_orig'] = x__find_condition__mutmut_orig # type: ignore # mutmut generated
mutants_x__find_condition__mutmut['x__find_condition__mutmut_1'] = x__find_condition__mutmut_1 # type: ignore # mutmut generated
mutants_x__find_condition__mutmut['x__find_condition__mutmut_2'] = x__find_condition__mutmut_2 # type: ignore # mutmut generated
mutants_x__find_condition__mutmut['x__find_condition__mutmut_3'] = x__find_condition__mutmut_3 # type: ignore # mutmut generated
mutants_x__find_condition__mutmut['x__find_condition__mutmut_4'] = x__find_condition__mutmut_4 # type: ignore # mutmut generated
mutants_x__find_condition__mutmut['x__find_condition__mutmut_5'] = x__find_condition__mutmut_5 # type: ignore # mutmut generated
mutants_x__find_condition__mutmut['x__find_condition__mutmut_6'] = x__find_condition__mutmut_6 # type: ignore # mutmut generated
mutants_x__find_condition__mutmut['x__find_condition__mutmut_7'] = x__find_condition__mutmut_7 # type: ignore # mutmut generated
mutants_x__find_condition__mutmut['x__find_condition__mutmut_8'] = x__find_condition__mutmut_8 # type: ignore # mutmut generated
mutants_x__find_condition__mutmut['x__find_condition__mutmut_9'] = x__find_condition__mutmut_9 # type: ignore # mutmut generated
mutants_x__is_true__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__is_true__mutmut)
def _is_true(condition: Mapping[str, object] | None) -> bool:
    return condition is not None and str(condition.get("status", "")) == _CONDITION_TRUE


def x__is_true__mutmut_orig(condition: Mapping[str, object] | None) -> bool:
    return condition is not None and str(condition.get("status", "")) == _CONDITION_TRUE


def x__is_true__mutmut_1(condition: Mapping[str, object] | None) -> bool:
    return condition is not None or str(condition.get("status", "")) == _CONDITION_TRUE


def x__is_true__mutmut_2(condition: Mapping[str, object] | None) -> bool:
    return condition is None and str(condition.get("status", "")) == _CONDITION_TRUE


def x__is_true__mutmut_3(condition: Mapping[str, object] | None) -> bool:
    return condition is not None and str(None) == _CONDITION_TRUE


def x__is_true__mutmut_4(condition: Mapping[str, object] | None) -> bool:
    return condition is not None and str(condition.get(None, "")) == _CONDITION_TRUE


def x__is_true__mutmut_5(condition: Mapping[str, object] | None) -> bool:
    return condition is not None and str(condition.get("status", None)) == _CONDITION_TRUE


def x__is_true__mutmut_6(condition: Mapping[str, object] | None) -> bool:
    return condition is not None and str(condition.get("")) == _CONDITION_TRUE


def x__is_true__mutmut_7(condition: Mapping[str, object] | None) -> bool:
    return condition is not None and str(condition.get("status", )) == _CONDITION_TRUE


def x__is_true__mutmut_8(condition: Mapping[str, object] | None) -> bool:
    return condition is not None and str(condition.get("XXstatusXX", "")) == _CONDITION_TRUE


def x__is_true__mutmut_9(condition: Mapping[str, object] | None) -> bool:
    return condition is not None and str(condition.get("STATUS", "")) == _CONDITION_TRUE


def x__is_true__mutmut_10(condition: Mapping[str, object] | None) -> bool:
    return condition is not None and str(condition.get("status", "XXXX")) == _CONDITION_TRUE


def x__is_true__mutmut_11(condition: Mapping[str, object] | None) -> bool:
    return condition is not None and str(condition.get("status", "")) != _CONDITION_TRUE

mutants_x__is_true__mutmut['_mutmut_orig'] = x__is_true__mutmut_orig # type: ignore # mutmut generated
mutants_x__is_true__mutmut['x__is_true__mutmut_1'] = x__is_true__mutmut_1 # type: ignore # mutmut generated
mutants_x__is_true__mutmut['x__is_true__mutmut_2'] = x__is_true__mutmut_2 # type: ignore # mutmut generated
mutants_x__is_true__mutmut['x__is_true__mutmut_3'] = x__is_true__mutmut_3 # type: ignore # mutmut generated
mutants_x__is_true__mutmut['x__is_true__mutmut_4'] = x__is_true__mutmut_4 # type: ignore # mutmut generated
mutants_x__is_true__mutmut['x__is_true__mutmut_5'] = x__is_true__mutmut_5 # type: ignore # mutmut generated
mutants_x__is_true__mutmut['x__is_true__mutmut_6'] = x__is_true__mutmut_6 # type: ignore # mutmut generated
mutants_x__is_true__mutmut['x__is_true__mutmut_7'] = x__is_true__mutmut_7 # type: ignore # mutmut generated
mutants_x__is_true__mutmut['x__is_true__mutmut_8'] = x__is_true__mutmut_8 # type: ignore # mutmut generated
mutants_x__is_true__mutmut['x__is_true__mutmut_9'] = x__is_true__mutmut_9 # type: ignore # mutmut generated
mutants_x__is_true__mutmut['x__is_true__mutmut_10'] = x__is_true__mutmut_10 # type: ignore # mutmut generated
mutants_x__is_true__mutmut['x__is_true__mutmut_11'] = x__is_true__mutmut_11 # type: ignore # mutmut generated
mutants_x__reason__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__reason__mutmut)
def _reason(condition: Mapping[str, object] | None) -> str:
    return str(condition.get("reason", "")) if condition is not None else ""


def x__reason__mutmut_orig(condition: Mapping[str, object] | None) -> str:
    return str(condition.get("reason", "")) if condition is not None else ""


def x__reason__mutmut_1(condition: Mapping[str, object] | None) -> str:
    return str(None) if condition is not None else ""


def x__reason__mutmut_2(condition: Mapping[str, object] | None) -> str:
    return str(condition.get(None, "")) if condition is not None else ""


def x__reason__mutmut_3(condition: Mapping[str, object] | None) -> str:
    return str(condition.get("reason", None)) if condition is not None else ""


def x__reason__mutmut_4(condition: Mapping[str, object] | None) -> str:
    return str(condition.get("")) if condition is not None else ""


def x__reason__mutmut_5(condition: Mapping[str, object] | None) -> str:
    return str(condition.get("reason", )) if condition is not None else ""


def x__reason__mutmut_6(condition: Mapping[str, object] | None) -> str:
    return str(condition.get("XXreasonXX", "")) if condition is not None else ""


def x__reason__mutmut_7(condition: Mapping[str, object] | None) -> str:
    return str(condition.get("REASON", "")) if condition is not None else ""


def x__reason__mutmut_8(condition: Mapping[str, object] | None) -> str:
    return str(condition.get("reason", "XXXX")) if condition is not None else ""


def x__reason__mutmut_9(condition: Mapping[str, object] | None) -> str:
    return str(condition.get("reason", "")) if condition is None else ""


def x__reason__mutmut_10(condition: Mapping[str, object] | None) -> str:
    return str(condition.get("reason", "")) if condition is not None else "XXXX"

mutants_x__reason__mutmut['_mutmut_orig'] = x__reason__mutmut_orig # type: ignore # mutmut generated
mutants_x__reason__mutmut['x__reason__mutmut_1'] = x__reason__mutmut_1 # type: ignore # mutmut generated
mutants_x__reason__mutmut['x__reason__mutmut_2'] = x__reason__mutmut_2 # type: ignore # mutmut generated
mutants_x__reason__mutmut['x__reason__mutmut_3'] = x__reason__mutmut_3 # type: ignore # mutmut generated
mutants_x__reason__mutmut['x__reason__mutmut_4'] = x__reason__mutmut_4 # type: ignore # mutmut generated
mutants_x__reason__mutmut['x__reason__mutmut_5'] = x__reason__mutmut_5 # type: ignore # mutmut generated
mutants_x__reason__mutmut['x__reason__mutmut_6'] = x__reason__mutmut_6 # type: ignore # mutmut generated
mutants_x__reason__mutmut['x__reason__mutmut_7'] = x__reason__mutmut_7 # type: ignore # mutmut generated
mutants_x__reason__mutmut['x__reason__mutmut_8'] = x__reason__mutmut_8 # type: ignore # mutmut generated
mutants_x__reason__mutmut['x__reason__mutmut_9'] = x__reason__mutmut_9 # type: ignore # mutmut generated
mutants_x__reason__mutmut['x__reason__mutmut_10'] = x__reason__mutmut_10 # type: ignore # mutmut generated
mutants_x__transition_time__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__transition_time__mutmut)
def _transition_time(condition: Mapping[str, object] | None) -> str | None:
    if condition is None or not _is_true(condition):
        return None
    last_transition = condition.get("lastTransitionTime")
    return str(last_transition) if last_transition else None


def x__transition_time__mutmut_orig(condition: Mapping[str, object] | None) -> str | None:
    if condition is None or not _is_true(condition):
        return None
    last_transition = condition.get("lastTransitionTime")
    return str(last_transition) if last_transition else None


def x__transition_time__mutmut_1(condition: Mapping[str, object] | None) -> str | None:
    if condition is None and not _is_true(condition):
        return None
    last_transition = condition.get("lastTransitionTime")
    return str(last_transition) if last_transition else None


def x__transition_time__mutmut_2(condition: Mapping[str, object] | None) -> str | None:
    if condition is not None or not _is_true(condition):
        return None
    last_transition = condition.get("lastTransitionTime")
    return str(last_transition) if last_transition else None


def x__transition_time__mutmut_3(condition: Mapping[str, object] | None) -> str | None:
    if condition is None or _is_true(condition):
        return None
    last_transition = condition.get("lastTransitionTime")
    return str(last_transition) if last_transition else None


def x__transition_time__mutmut_4(condition: Mapping[str, object] | None) -> str | None:
    if condition is None or not _is_true(None):
        return None
    last_transition = condition.get("lastTransitionTime")
    return str(last_transition) if last_transition else None


def x__transition_time__mutmut_5(condition: Mapping[str, object] | None) -> str | None:
    if condition is None or not _is_true(condition):
        return None
    last_transition = None
    return str(last_transition) if last_transition else None


def x__transition_time__mutmut_6(condition: Mapping[str, object] | None) -> str | None:
    if condition is None or not _is_true(condition):
        return None
    last_transition = condition.get(None)
    return str(last_transition) if last_transition else None


def x__transition_time__mutmut_7(condition: Mapping[str, object] | None) -> str | None:
    if condition is None or not _is_true(condition):
        return None
    last_transition = condition.get("XXlastTransitionTimeXX")
    return str(last_transition) if last_transition else None


def x__transition_time__mutmut_8(condition: Mapping[str, object] | None) -> str | None:
    if condition is None or not _is_true(condition):
        return None
    last_transition = condition.get("lasttransitiontime")
    return str(last_transition) if last_transition else None


def x__transition_time__mutmut_9(condition: Mapping[str, object] | None) -> str | None:
    if condition is None or not _is_true(condition):
        return None
    last_transition = condition.get("LASTTRANSITIONTIME")
    return str(last_transition) if last_transition else None


def x__transition_time__mutmut_10(condition: Mapping[str, object] | None) -> str | None:
    if condition is None or not _is_true(condition):
        return None
    last_transition = condition.get("lastTransitionTime")
    return str(None) if last_transition else None

mutants_x__transition_time__mutmut['_mutmut_orig'] = x__transition_time__mutmut_orig # type: ignore # mutmut generated
mutants_x__transition_time__mutmut['x__transition_time__mutmut_1'] = x__transition_time__mutmut_1 # type: ignore # mutmut generated
mutants_x__transition_time__mutmut['x__transition_time__mutmut_2'] = x__transition_time__mutmut_2 # type: ignore # mutmut generated
mutants_x__transition_time__mutmut['x__transition_time__mutmut_3'] = x__transition_time__mutmut_3 # type: ignore # mutmut generated
mutants_x__transition_time__mutmut['x__transition_time__mutmut_4'] = x__transition_time__mutmut_4 # type: ignore # mutmut generated
mutants_x__transition_time__mutmut['x__transition_time__mutmut_5'] = x__transition_time__mutmut_5 # type: ignore # mutmut generated
mutants_x__transition_time__mutmut['x__transition_time__mutmut_6'] = x__transition_time__mutmut_6 # type: ignore # mutmut generated
mutants_x__transition_time__mutmut['x__transition_time__mutmut_7'] = x__transition_time__mutmut_7 # type: ignore # mutmut generated
mutants_x__transition_time__mutmut['x__transition_time__mutmut_8'] = x__transition_time__mutmut_8 # type: ignore # mutmut generated
mutants_x__transition_time__mutmut['x__transition_time__mutmut_9'] = x__transition_time__mutmut_9 # type: ignore # mutmut generated
mutants_x__transition_time__mutmut['x__transition_time__mutmut_10'] = x__transition_time__mutmut_10 # type: ignore # mutmut generated
mutants_x__as_int__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__as_int__mutmut)
def _as_int(value: object) -> int:
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value)
    return 0


def x__as_int__mutmut_orig(value: object) -> int:
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value)
    return 0


def x__as_int__mutmut_1(value: object) -> int:
    if isinstance(value, bool):
        return int(None)
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value)
    return 0


def x__as_int__mutmut_2(value: object) -> int:
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(None)
    return 0


def x__as_int__mutmut_3(value: object) -> int:
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value)
    return 1

mutants_x__as_int__mutmut['_mutmut_orig'] = x__as_int__mutmut_orig # type: ignore # mutmut generated
mutants_x__as_int__mutmut['x__as_int__mutmut_1'] = x__as_int__mutmut_1 # type: ignore # mutmut generated
mutants_x__as_int__mutmut['x__as_int__mutmut_2'] = x__as_int__mutmut_2 # type: ignore # mutmut generated
mutants_x__as_int__mutmut['x__as_int__mutmut_3'] = x__as_int__mutmut_3 # type: ignore # mutmut generated
