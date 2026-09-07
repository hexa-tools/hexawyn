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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class CustomObjectsApi(Protocol):
    """Minimal contract for the kubernetes CustomObjectsApi used here."""

    def list_cluster_custom_object(
        self, group: str, version: str, plural: str
    ) -> Mapping[str, object]: ...
mutants_xǁOpenShiftClusterOperatorAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut: MutantDict = {}  # type: ignore
mutants_xǁOpenShiftClusterOperatorAdapterǁ_api_or_create__mutmut: MutantDict = {}  # type: ignore


class OpenShiftClusterOperatorAdapter(ClusterOperatorStatusPort):
    """Reads ClusterOperators from the config.openshift.io/v1 API group.

    Parses the Available / Progressing / Degraded conditions into a flat,
    domain-friendly shape. Infrastructure exceptions never escape: they are
    translated to HexawynError subclasses.
    """

    @_mutmut_mutated(mutants_xǁOpenShiftClusterOperatorAdapterǁ__init____mutmut)
    def __init__(self, custom_objects_api: CustomObjectsApi | None = None) -> None:
        self._api = custom_objects_api

    def xǁOpenShiftClusterOperatorAdapterǁ__init____mutmut_orig(self, custom_objects_api: CustomObjectsApi | None = None) -> None:
        self._api = custom_objects_api

    def xǁOpenShiftClusterOperatorAdapterǁ__init____mutmut_1(self, custom_objects_api: CustomObjectsApi | None = None) -> None:
        self._api = None

    @_mutmut_mutated(mutants_xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut)
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

    def xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut_orig(self) -> list[ClusterOperatorRawData]:
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

    def xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut_1(self) -> list[ClusterOperatorRawData]:
        api = None
        try:
            payload = api.list_cluster_custom_object(
                group=_CONFIG_GROUP,
                version=_API_VERSION,
                plural=_CLUSTER_OPERATORS_PLURAL,
            )
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_raw(item) for item in _items(payload)]

    def xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut_2(self) -> list[ClusterOperatorRawData]:
        api = self._api_or_create()
        try:
            payload = None
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_raw(item) for item in _items(payload)]

    def xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut_3(self) -> list[ClusterOperatorRawData]:
        api = self._api_or_create()
        try:
            payload = api.list_cluster_custom_object(
                group=None,
                version=_API_VERSION,
                plural=_CLUSTER_OPERATORS_PLURAL,
            )
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_raw(item) for item in _items(payload)]

    def xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut_4(self) -> list[ClusterOperatorRawData]:
        api = self._api_or_create()
        try:
            payload = api.list_cluster_custom_object(
                group=_CONFIG_GROUP,
                version=None,
                plural=_CLUSTER_OPERATORS_PLURAL,
            )
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_raw(item) for item in _items(payload)]

    def xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut_5(self) -> list[ClusterOperatorRawData]:
        api = self._api_or_create()
        try:
            payload = api.list_cluster_custom_object(
                group=_CONFIG_GROUP,
                version=_API_VERSION,
                plural=None,
            )
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_raw(item) for item in _items(payload)]

    def xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut_6(self) -> list[ClusterOperatorRawData]:
        api = self._api_or_create()
        try:
            payload = api.list_cluster_custom_object(
                version=_API_VERSION,
                plural=_CLUSTER_OPERATORS_PLURAL,
            )
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_raw(item) for item in _items(payload)]

    def xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut_7(self) -> list[ClusterOperatorRawData]:
        api = self._api_or_create()
        try:
            payload = api.list_cluster_custom_object(
                group=_CONFIG_GROUP,
                plural=_CLUSTER_OPERATORS_PLURAL,
            )
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_raw(item) for item in _items(payload)]

    def xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut_8(self) -> list[ClusterOperatorRawData]:
        api = self._api_or_create()
        try:
            payload = api.list_cluster_custom_object(
                group=_CONFIG_GROUP,
                version=_API_VERSION,
                )
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_raw(item) for item in _items(payload)]

    def xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut_9(self) -> list[ClusterOperatorRawData]:
        api = self._api_or_create()
        try:
            payload = api.list_cluster_custom_object(
                group=_CONFIG_GROUP,
                version=_API_VERSION,
                plural=_CLUSTER_OPERATORS_PLURAL,
            )
        except Exception as exc:
            raise _translate_error(None) from exc

        return [_to_raw(item) for item in _items(payload)]

    def xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut_10(self) -> list[ClusterOperatorRawData]:
        api = self._api_or_create()
        try:
            payload = api.list_cluster_custom_object(
                group=_CONFIG_GROUP,
                version=_API_VERSION,
                plural=_CLUSTER_OPERATORS_PLURAL,
            )
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_raw(None) for item in _items(payload)]

    def xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut_11(self) -> list[ClusterOperatorRawData]:
        api = self._api_or_create()
        try:
            payload = api.list_cluster_custom_object(
                group=_CONFIG_GROUP,
                version=_API_VERSION,
                plural=_CLUSTER_OPERATORS_PLURAL,
            )
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_raw(item) for item in _items(None)]

    @_mutmut_mutated(mutants_xǁOpenShiftClusterOperatorAdapterǁ_api_or_create__mutmut)
    def _api_or_create(self) -> CustomObjectsApi:
        if self._api is None:
            from kubernetes import client as k8s

            self._api = k8s.CustomObjectsApi()
        return self._api

    def xǁOpenShiftClusterOperatorAdapterǁ_api_or_create__mutmut_orig(self) -> CustomObjectsApi:
        if self._api is None:
            from kubernetes import client as k8s

            self._api = k8s.CustomObjectsApi()
        return self._api

    def xǁOpenShiftClusterOperatorAdapterǁ_api_or_create__mutmut_1(self) -> CustomObjectsApi:
        if self._api is not None:
            from kubernetes import client as k8s

            self._api = k8s.CustomObjectsApi()
        return self._api

    def xǁOpenShiftClusterOperatorAdapterǁ_api_or_create__mutmut_2(self) -> CustomObjectsApi:
        if self._api is None:
            from kubernetes import client as k8s

            self._api = None
        return self._api

mutants_xǁOpenShiftClusterOperatorAdapterǁ__init____mutmut['_mutmut_orig'] = OpenShiftClusterOperatorAdapter.xǁOpenShiftClusterOperatorAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenShiftClusterOperatorAdapterǁ__init____mutmut['xǁOpenShiftClusterOperatorAdapterǁ__init____mutmut_1'] = OpenShiftClusterOperatorAdapter.xǁOpenShiftClusterOperatorAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut['_mutmut_orig'] = OpenShiftClusterOperatorAdapter.xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut['xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut_1'] = OpenShiftClusterOperatorAdapter.xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut['xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut_2'] = OpenShiftClusterOperatorAdapter.xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut['xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut_3'] = OpenShiftClusterOperatorAdapter.xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut['xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut_4'] = OpenShiftClusterOperatorAdapter.xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut['xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut_5'] = OpenShiftClusterOperatorAdapter.xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut['xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut_6'] = OpenShiftClusterOperatorAdapter.xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut_6 # type: ignore # mutmut generated
mutants_xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut['xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut_7'] = OpenShiftClusterOperatorAdapter.xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut_7 # type: ignore # mutmut generated
mutants_xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut['xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut_8'] = OpenShiftClusterOperatorAdapter.xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut_8 # type: ignore # mutmut generated
mutants_xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut['xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut_9'] = OpenShiftClusterOperatorAdapter.xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut_9 # type: ignore # mutmut generated
mutants_xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut['xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut_10'] = OpenShiftClusterOperatorAdapter.xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut_10 # type: ignore # mutmut generated
mutants_xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut['xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut_11'] = OpenShiftClusterOperatorAdapter.xǁOpenShiftClusterOperatorAdapterǁlist_cluster_operators__mutmut_11 # type: ignore # mutmut generated

mutants_xǁOpenShiftClusterOperatorAdapterǁ_api_or_create__mutmut['_mutmut_orig'] = OpenShiftClusterOperatorAdapter.xǁOpenShiftClusterOperatorAdapterǁ_api_or_create__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenShiftClusterOperatorAdapterǁ_api_or_create__mutmut['xǁOpenShiftClusterOperatorAdapterǁ_api_or_create__mutmut_1'] = OpenShiftClusterOperatorAdapter.xǁOpenShiftClusterOperatorAdapterǁ_api_or_create__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOpenShiftClusterOperatorAdapterǁ_api_or_create__mutmut['xǁOpenShiftClusterOperatorAdapterǁ_api_or_create__mutmut_2'] = OpenShiftClusterOperatorAdapter.xǁOpenShiftClusterOperatorAdapterǁ_api_or_create__mutmut_2 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__translate_error__mutmut)
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


def x__translate_error__mutmut_orig(exc: Exception) -> Exception:
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


def x__translate_error__mutmut_1(exc: Exception) -> Exception:
    status = None
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


def x__translate_error__mutmut_2(exc: Exception) -> Exception:
    status = getattr(None, "status", None)
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


def x__translate_error__mutmut_3(exc: Exception) -> Exception:
    status = getattr(exc, None, None)
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


def x__translate_error__mutmut_4(exc: Exception) -> Exception:
    status = getattr("status", None)
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


def x__translate_error__mutmut_5(exc: Exception) -> Exception:
    status = getattr(exc, None)
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


def x__translate_error__mutmut_6(exc: Exception) -> Exception:
    status = getattr(exc, "status", )
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


def x__translate_error__mutmut_7(exc: Exception) -> Exception:
    status = getattr(exc, "XXstatusXX", None)
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


def x__translate_error__mutmut_8(exc: Exception) -> Exception:
    status = getattr(exc, "STATUS", None)
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


def x__translate_error__mutmut_9(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status != _NOT_FOUND:
        return ClusterOperatorCRDNotFoundError()
    if status == _FORBIDDEN:
        return InsufficientPermissionsError(
            "RBAC denied access to clusteroperators",
            context={"resource": _CLUSTER_OPERATORS_PLURAL},
        )
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading clusteroperators: {exc}"
    )


def x__translate_error__mutmut_10(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _NOT_FOUND:
        return ClusterOperatorCRDNotFoundError()
    if status != _FORBIDDEN:
        return InsufficientPermissionsError(
            "RBAC denied access to clusteroperators",
            context={"resource": _CLUSTER_OPERATORS_PLURAL},
        )
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading clusteroperators: {exc}"
    )


def x__translate_error__mutmut_11(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _NOT_FOUND:
        return ClusterOperatorCRDNotFoundError()
    if status == _FORBIDDEN:
        return InsufficientPermissionsError(
            None,
            context={"resource": _CLUSTER_OPERATORS_PLURAL},
        )
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading clusteroperators: {exc}"
    )


def x__translate_error__mutmut_12(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _NOT_FOUND:
        return ClusterOperatorCRDNotFoundError()
    if status == _FORBIDDEN:
        return InsufficientPermissionsError(
            "RBAC denied access to clusteroperators",
            context=None,
        )
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading clusteroperators: {exc}"
    )


def x__translate_error__mutmut_13(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _NOT_FOUND:
        return ClusterOperatorCRDNotFoundError()
    if status == _FORBIDDEN:
        return InsufficientPermissionsError(
            context={"resource": _CLUSTER_OPERATORS_PLURAL},
        )
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading clusteroperators: {exc}"
    )


def x__translate_error__mutmut_14(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _NOT_FOUND:
        return ClusterOperatorCRDNotFoundError()
    if status == _FORBIDDEN:
        return InsufficientPermissionsError(
            "RBAC denied access to clusteroperators",
            )
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading clusteroperators: {exc}"
    )


def x__translate_error__mutmut_15(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _NOT_FOUND:
        return ClusterOperatorCRDNotFoundError()
    if status == _FORBIDDEN:
        return InsufficientPermissionsError(
            "XXRBAC denied access to clusteroperatorsXX",
            context={"resource": _CLUSTER_OPERATORS_PLURAL},
        )
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading clusteroperators: {exc}"
    )


def x__translate_error__mutmut_16(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _NOT_FOUND:
        return ClusterOperatorCRDNotFoundError()
    if status == _FORBIDDEN:
        return InsufficientPermissionsError(
            "rbac denied access to clusteroperators",
            context={"resource": _CLUSTER_OPERATORS_PLURAL},
        )
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading clusteroperators: {exc}"
    )


def x__translate_error__mutmut_17(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _NOT_FOUND:
        return ClusterOperatorCRDNotFoundError()
    if status == _FORBIDDEN:
        return InsufficientPermissionsError(
            "RBAC DENIED ACCESS TO CLUSTEROPERATORS",
            context={"resource": _CLUSTER_OPERATORS_PLURAL},
        )
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading clusteroperators: {exc}"
    )


def x__translate_error__mutmut_18(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _NOT_FOUND:
        return ClusterOperatorCRDNotFoundError()
    if status == _FORBIDDEN:
        return InsufficientPermissionsError(
            "RBAC denied access to clusteroperators",
            context={"XXresourceXX": _CLUSTER_OPERATORS_PLURAL},
        )
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading clusteroperators: {exc}"
    )


def x__translate_error__mutmut_19(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _NOT_FOUND:
        return ClusterOperatorCRDNotFoundError()
    if status == _FORBIDDEN:
        return InsufficientPermissionsError(
            "RBAC denied access to clusteroperators",
            context={"RESOURCE": _CLUSTER_OPERATORS_PLURAL},
        )
    return ClusterUnreachableError(
        f"OpenShift API unreachable while reading clusteroperators: {exc}"
    )


def x__translate_error__mutmut_20(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _NOT_FOUND:
        return ClusterOperatorCRDNotFoundError()
    if status == _FORBIDDEN:
        return InsufficientPermissionsError(
            "RBAC denied access to clusteroperators",
            context={"resource": _CLUSTER_OPERATORS_PLURAL},
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


def x__to_raw__mutmut_orig(item: Mapping[str, object]) -> ClusterOperatorRawData:
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


def x__to_raw__mutmut_1(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = None
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


def x__to_raw__mutmut_2(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get(None)
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


def x__to_raw__mutmut_3(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("XXmetadataXX")
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


def x__to_raw__mutmut_4(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("METADATA")
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


def x__to_raw__mutmut_5(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = None
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


def x__to_raw__mutmut_6(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = None

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


def x__to_raw__mutmut_7(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(None)

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


def x__to_raw__mutmut_8(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = None
    return ClusterOperatorRawData(
        name=str(meta.get("name", "")),
        available=available_status == _CONDITION_TRUE,
        progressing=_condition_status(conditions, "Progressing") == _CONDITION_TRUE,
        degraded=_condition_status(conditions, "Degraded") == _CONDITION_TRUE,
        available_unknown=available_status == _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_9(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(None, "Available")
    return ClusterOperatorRawData(
        name=str(meta.get("name", "")),
        available=available_status == _CONDITION_TRUE,
        progressing=_condition_status(conditions, "Progressing") == _CONDITION_TRUE,
        degraded=_condition_status(conditions, "Degraded") == _CONDITION_TRUE,
        available_unknown=available_status == _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_10(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(conditions, None)
    return ClusterOperatorRawData(
        name=str(meta.get("name", "")),
        available=available_status == _CONDITION_TRUE,
        progressing=_condition_status(conditions, "Progressing") == _CONDITION_TRUE,
        degraded=_condition_status(conditions, "Degraded") == _CONDITION_TRUE,
        available_unknown=available_status == _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_11(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status("Available")
    return ClusterOperatorRawData(
        name=str(meta.get("name", "")),
        available=available_status == _CONDITION_TRUE,
        progressing=_condition_status(conditions, "Progressing") == _CONDITION_TRUE,
        degraded=_condition_status(conditions, "Degraded") == _CONDITION_TRUE,
        available_unknown=available_status == _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_12(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(conditions, )
    return ClusterOperatorRawData(
        name=str(meta.get("name", "")),
        available=available_status == _CONDITION_TRUE,
        progressing=_condition_status(conditions, "Progressing") == _CONDITION_TRUE,
        degraded=_condition_status(conditions, "Degraded") == _CONDITION_TRUE,
        available_unknown=available_status == _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_13(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(conditions, "XXAvailableXX")
    return ClusterOperatorRawData(
        name=str(meta.get("name", "")),
        available=available_status == _CONDITION_TRUE,
        progressing=_condition_status(conditions, "Progressing") == _CONDITION_TRUE,
        degraded=_condition_status(conditions, "Degraded") == _CONDITION_TRUE,
        available_unknown=available_status == _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_14(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(conditions, "available")
    return ClusterOperatorRawData(
        name=str(meta.get("name", "")),
        available=available_status == _CONDITION_TRUE,
        progressing=_condition_status(conditions, "Progressing") == _CONDITION_TRUE,
        degraded=_condition_status(conditions, "Degraded") == _CONDITION_TRUE,
        available_unknown=available_status == _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_15(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(conditions, "AVAILABLE")
    return ClusterOperatorRawData(
        name=str(meta.get("name", "")),
        available=available_status == _CONDITION_TRUE,
        progressing=_condition_status(conditions, "Progressing") == _CONDITION_TRUE,
        degraded=_condition_status(conditions, "Degraded") == _CONDITION_TRUE,
        available_unknown=available_status == _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_16(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(conditions, "Available")
    return ClusterOperatorRawData(
        name=None,
        available=available_status == _CONDITION_TRUE,
        progressing=_condition_status(conditions, "Progressing") == _CONDITION_TRUE,
        degraded=_condition_status(conditions, "Degraded") == _CONDITION_TRUE,
        available_unknown=available_status == _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_17(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(conditions, "Available")
    return ClusterOperatorRawData(
        name=str(meta.get("name", "")),
        available=None,
        progressing=_condition_status(conditions, "Progressing") == _CONDITION_TRUE,
        degraded=_condition_status(conditions, "Degraded") == _CONDITION_TRUE,
        available_unknown=available_status == _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_18(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(conditions, "Available")
    return ClusterOperatorRawData(
        name=str(meta.get("name", "")),
        available=available_status == _CONDITION_TRUE,
        progressing=None,
        degraded=_condition_status(conditions, "Degraded") == _CONDITION_TRUE,
        available_unknown=available_status == _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_19(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(conditions, "Available")
    return ClusterOperatorRawData(
        name=str(meta.get("name", "")),
        available=available_status == _CONDITION_TRUE,
        progressing=_condition_status(conditions, "Progressing") == _CONDITION_TRUE,
        degraded=None,
        available_unknown=available_status == _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_20(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(conditions, "Available")
    return ClusterOperatorRawData(
        name=str(meta.get("name", "")),
        available=available_status == _CONDITION_TRUE,
        progressing=_condition_status(conditions, "Progressing") == _CONDITION_TRUE,
        degraded=_condition_status(conditions, "Degraded") == _CONDITION_TRUE,
        available_unknown=None,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_21(item: Mapping[str, object]) -> ClusterOperatorRawData:
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
        message=None,
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_22(item: Mapping[str, object]) -> ClusterOperatorRawData:
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
        degraded_since=None,
    )


def x__to_raw__mutmut_23(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(conditions, "Available")
    return ClusterOperatorRawData(
        available=available_status == _CONDITION_TRUE,
        progressing=_condition_status(conditions, "Progressing") == _CONDITION_TRUE,
        degraded=_condition_status(conditions, "Degraded") == _CONDITION_TRUE,
        available_unknown=available_status == _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_24(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(conditions, "Available")
    return ClusterOperatorRawData(
        name=str(meta.get("name", "")),
        progressing=_condition_status(conditions, "Progressing") == _CONDITION_TRUE,
        degraded=_condition_status(conditions, "Degraded") == _CONDITION_TRUE,
        available_unknown=available_status == _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_25(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(conditions, "Available")
    return ClusterOperatorRawData(
        name=str(meta.get("name", "")),
        available=available_status == _CONDITION_TRUE,
        degraded=_condition_status(conditions, "Degraded") == _CONDITION_TRUE,
        available_unknown=available_status == _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_26(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(conditions, "Available")
    return ClusterOperatorRawData(
        name=str(meta.get("name", "")),
        available=available_status == _CONDITION_TRUE,
        progressing=_condition_status(conditions, "Progressing") == _CONDITION_TRUE,
        available_unknown=available_status == _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_27(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(conditions, "Available")
    return ClusterOperatorRawData(
        name=str(meta.get("name", "")),
        available=available_status == _CONDITION_TRUE,
        progressing=_condition_status(conditions, "Progressing") == _CONDITION_TRUE,
        degraded=_condition_status(conditions, "Degraded") == _CONDITION_TRUE,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_28(item: Mapping[str, object]) -> ClusterOperatorRawData:
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
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_29(item: Mapping[str, object]) -> ClusterOperatorRawData:
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
        )


def x__to_raw__mutmut_30(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(conditions, "Available")
    return ClusterOperatorRawData(
        name=str(None),
        available=available_status == _CONDITION_TRUE,
        progressing=_condition_status(conditions, "Progressing") == _CONDITION_TRUE,
        degraded=_condition_status(conditions, "Degraded") == _CONDITION_TRUE,
        available_unknown=available_status == _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_31(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(conditions, "Available")
    return ClusterOperatorRawData(
        name=str(meta.get(None, "")),
        available=available_status == _CONDITION_TRUE,
        progressing=_condition_status(conditions, "Progressing") == _CONDITION_TRUE,
        degraded=_condition_status(conditions, "Degraded") == _CONDITION_TRUE,
        available_unknown=available_status == _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_32(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(conditions, "Available")
    return ClusterOperatorRawData(
        name=str(meta.get("name", None)),
        available=available_status == _CONDITION_TRUE,
        progressing=_condition_status(conditions, "Progressing") == _CONDITION_TRUE,
        degraded=_condition_status(conditions, "Degraded") == _CONDITION_TRUE,
        available_unknown=available_status == _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_33(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(conditions, "Available")
    return ClusterOperatorRawData(
        name=str(meta.get("")),
        available=available_status == _CONDITION_TRUE,
        progressing=_condition_status(conditions, "Progressing") == _CONDITION_TRUE,
        degraded=_condition_status(conditions, "Degraded") == _CONDITION_TRUE,
        available_unknown=available_status == _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_34(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(conditions, "Available")
    return ClusterOperatorRawData(
        name=str(meta.get("name", )),
        available=available_status == _CONDITION_TRUE,
        progressing=_condition_status(conditions, "Progressing") == _CONDITION_TRUE,
        degraded=_condition_status(conditions, "Degraded") == _CONDITION_TRUE,
        available_unknown=available_status == _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_35(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(conditions, "Available")
    return ClusterOperatorRawData(
        name=str(meta.get("XXnameXX", "")),
        available=available_status == _CONDITION_TRUE,
        progressing=_condition_status(conditions, "Progressing") == _CONDITION_TRUE,
        degraded=_condition_status(conditions, "Degraded") == _CONDITION_TRUE,
        available_unknown=available_status == _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_36(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(conditions, "Available")
    return ClusterOperatorRawData(
        name=str(meta.get("NAME", "")),
        available=available_status == _CONDITION_TRUE,
        progressing=_condition_status(conditions, "Progressing") == _CONDITION_TRUE,
        degraded=_condition_status(conditions, "Degraded") == _CONDITION_TRUE,
        available_unknown=available_status == _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_37(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(conditions, "Available")
    return ClusterOperatorRawData(
        name=str(meta.get("name", "XXXX")),
        available=available_status == _CONDITION_TRUE,
        progressing=_condition_status(conditions, "Progressing") == _CONDITION_TRUE,
        degraded=_condition_status(conditions, "Degraded") == _CONDITION_TRUE,
        available_unknown=available_status == _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_38(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(conditions, "Available")
    return ClusterOperatorRawData(
        name=str(meta.get("name", "")),
        available=available_status != _CONDITION_TRUE,
        progressing=_condition_status(conditions, "Progressing") == _CONDITION_TRUE,
        degraded=_condition_status(conditions, "Degraded") == _CONDITION_TRUE,
        available_unknown=available_status == _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_39(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(conditions, "Available")
    return ClusterOperatorRawData(
        name=str(meta.get("name", "")),
        available=available_status == _CONDITION_TRUE,
        progressing=_condition_status(None, "Progressing") == _CONDITION_TRUE,
        degraded=_condition_status(conditions, "Degraded") == _CONDITION_TRUE,
        available_unknown=available_status == _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_40(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(conditions, "Available")
    return ClusterOperatorRawData(
        name=str(meta.get("name", "")),
        available=available_status == _CONDITION_TRUE,
        progressing=_condition_status(conditions, None) == _CONDITION_TRUE,
        degraded=_condition_status(conditions, "Degraded") == _CONDITION_TRUE,
        available_unknown=available_status == _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_41(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(conditions, "Available")
    return ClusterOperatorRawData(
        name=str(meta.get("name", "")),
        available=available_status == _CONDITION_TRUE,
        progressing=_condition_status("Progressing") == _CONDITION_TRUE,
        degraded=_condition_status(conditions, "Degraded") == _CONDITION_TRUE,
        available_unknown=available_status == _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_42(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(conditions, "Available")
    return ClusterOperatorRawData(
        name=str(meta.get("name", "")),
        available=available_status == _CONDITION_TRUE,
        progressing=_condition_status(conditions, ) == _CONDITION_TRUE,
        degraded=_condition_status(conditions, "Degraded") == _CONDITION_TRUE,
        available_unknown=available_status == _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_43(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(conditions, "Available")
    return ClusterOperatorRawData(
        name=str(meta.get("name", "")),
        available=available_status == _CONDITION_TRUE,
        progressing=_condition_status(conditions, "XXProgressingXX") == _CONDITION_TRUE,
        degraded=_condition_status(conditions, "Degraded") == _CONDITION_TRUE,
        available_unknown=available_status == _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_44(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(conditions, "Available")
    return ClusterOperatorRawData(
        name=str(meta.get("name", "")),
        available=available_status == _CONDITION_TRUE,
        progressing=_condition_status(conditions, "progressing") == _CONDITION_TRUE,
        degraded=_condition_status(conditions, "Degraded") == _CONDITION_TRUE,
        available_unknown=available_status == _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_45(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(conditions, "Available")
    return ClusterOperatorRawData(
        name=str(meta.get("name", "")),
        available=available_status == _CONDITION_TRUE,
        progressing=_condition_status(conditions, "PROGRESSING") == _CONDITION_TRUE,
        degraded=_condition_status(conditions, "Degraded") == _CONDITION_TRUE,
        available_unknown=available_status == _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_46(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(conditions, "Available")
    return ClusterOperatorRawData(
        name=str(meta.get("name", "")),
        available=available_status == _CONDITION_TRUE,
        progressing=_condition_status(conditions, "Progressing") != _CONDITION_TRUE,
        degraded=_condition_status(conditions, "Degraded") == _CONDITION_TRUE,
        available_unknown=available_status == _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_47(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(conditions, "Available")
    return ClusterOperatorRawData(
        name=str(meta.get("name", "")),
        available=available_status == _CONDITION_TRUE,
        progressing=_condition_status(conditions, "Progressing") == _CONDITION_TRUE,
        degraded=_condition_status(None, "Degraded") == _CONDITION_TRUE,
        available_unknown=available_status == _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_48(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(conditions, "Available")
    return ClusterOperatorRawData(
        name=str(meta.get("name", "")),
        available=available_status == _CONDITION_TRUE,
        progressing=_condition_status(conditions, "Progressing") == _CONDITION_TRUE,
        degraded=_condition_status(conditions, None) == _CONDITION_TRUE,
        available_unknown=available_status == _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_49(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(conditions, "Available")
    return ClusterOperatorRawData(
        name=str(meta.get("name", "")),
        available=available_status == _CONDITION_TRUE,
        progressing=_condition_status(conditions, "Progressing") == _CONDITION_TRUE,
        degraded=_condition_status("Degraded") == _CONDITION_TRUE,
        available_unknown=available_status == _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_50(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(conditions, "Available")
    return ClusterOperatorRawData(
        name=str(meta.get("name", "")),
        available=available_status == _CONDITION_TRUE,
        progressing=_condition_status(conditions, "Progressing") == _CONDITION_TRUE,
        degraded=_condition_status(conditions, ) == _CONDITION_TRUE,
        available_unknown=available_status == _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_51(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(conditions, "Available")
    return ClusterOperatorRawData(
        name=str(meta.get("name", "")),
        available=available_status == _CONDITION_TRUE,
        progressing=_condition_status(conditions, "Progressing") == _CONDITION_TRUE,
        degraded=_condition_status(conditions, "XXDegradedXX") == _CONDITION_TRUE,
        available_unknown=available_status == _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_52(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(conditions, "Available")
    return ClusterOperatorRawData(
        name=str(meta.get("name", "")),
        available=available_status == _CONDITION_TRUE,
        progressing=_condition_status(conditions, "Progressing") == _CONDITION_TRUE,
        degraded=_condition_status(conditions, "degraded") == _CONDITION_TRUE,
        available_unknown=available_status == _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_53(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(conditions, "Available")
    return ClusterOperatorRawData(
        name=str(meta.get("name", "")),
        available=available_status == _CONDITION_TRUE,
        progressing=_condition_status(conditions, "Progressing") == _CONDITION_TRUE,
        degraded=_condition_status(conditions, "DEGRADED") == _CONDITION_TRUE,
        available_unknown=available_status == _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_54(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(conditions, "Available")
    return ClusterOperatorRawData(
        name=str(meta.get("name", "")),
        available=available_status == _CONDITION_TRUE,
        progressing=_condition_status(conditions, "Progressing") == _CONDITION_TRUE,
        degraded=_condition_status(conditions, "Degraded") != _CONDITION_TRUE,
        available_unknown=available_status == _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_55(item: Mapping[str, object]) -> ClusterOperatorRawData:
    metadata = item.get("metadata")
    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    conditions = _conditions(item)

    available_status = _condition_status(conditions, "Available")
    return ClusterOperatorRawData(
        name=str(meta.get("name", "")),
        available=available_status == _CONDITION_TRUE,
        progressing=_condition_status(conditions, "Progressing") == _CONDITION_TRUE,
        degraded=_condition_status(conditions, "Degraded") == _CONDITION_TRUE,
        available_unknown=available_status != _CONDITION_UNKNOWN,
        message=_root_cause_message(conditions),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_56(item: Mapping[str, object]) -> ClusterOperatorRawData:
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
        message=_root_cause_message(None),
        degraded_since=_degraded_since(conditions),
    )


def x__to_raw__mutmut_57(item: Mapping[str, object]) -> ClusterOperatorRawData:
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
        degraded_since=_degraded_since(None),
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
mutants_x__conditions__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__conditions__mutmut)
def _conditions(item: Mapping[str, object]) -> list[Mapping[str, object]]:
    status = item.get("status")
    if not isinstance(status, Mapping):
        return []
    raw = status.get("conditions")
    if not isinstance(raw, list):
        return []
    return [condition for condition in raw if isinstance(condition, Mapping)]


def x__conditions__mutmut_orig(item: Mapping[str, object]) -> list[Mapping[str, object]]:
    status = item.get("status")
    if not isinstance(status, Mapping):
        return []
    raw = status.get("conditions")
    if not isinstance(raw, list):
        return []
    return [condition for condition in raw if isinstance(condition, Mapping)]


def x__conditions__mutmut_1(item: Mapping[str, object]) -> list[Mapping[str, object]]:
    status = None
    if not isinstance(status, Mapping):
        return []
    raw = status.get("conditions")
    if not isinstance(raw, list):
        return []
    return [condition for condition in raw if isinstance(condition, Mapping)]


def x__conditions__mutmut_2(item: Mapping[str, object]) -> list[Mapping[str, object]]:
    status = item.get(None)
    if not isinstance(status, Mapping):
        return []
    raw = status.get("conditions")
    if not isinstance(raw, list):
        return []
    return [condition for condition in raw if isinstance(condition, Mapping)]


def x__conditions__mutmut_3(item: Mapping[str, object]) -> list[Mapping[str, object]]:
    status = item.get("XXstatusXX")
    if not isinstance(status, Mapping):
        return []
    raw = status.get("conditions")
    if not isinstance(raw, list):
        return []
    return [condition for condition in raw if isinstance(condition, Mapping)]


def x__conditions__mutmut_4(item: Mapping[str, object]) -> list[Mapping[str, object]]:
    status = item.get("STATUS")
    if not isinstance(status, Mapping):
        return []
    raw = status.get("conditions")
    if not isinstance(raw, list):
        return []
    return [condition for condition in raw if isinstance(condition, Mapping)]


def x__conditions__mutmut_5(item: Mapping[str, object]) -> list[Mapping[str, object]]:
    status = item.get("status")
    if isinstance(status, Mapping):
        return []
    raw = status.get("conditions")
    if not isinstance(raw, list):
        return []
    return [condition for condition in raw if isinstance(condition, Mapping)]


def x__conditions__mutmut_6(item: Mapping[str, object]) -> list[Mapping[str, object]]:
    status = item.get("status")
    if not isinstance(status, Mapping):
        return []
    raw = None
    if not isinstance(raw, list):
        return []
    return [condition for condition in raw if isinstance(condition, Mapping)]


def x__conditions__mutmut_7(item: Mapping[str, object]) -> list[Mapping[str, object]]:
    status = item.get("status")
    if not isinstance(status, Mapping):
        return []
    raw = status.get(None)
    if not isinstance(raw, list):
        return []
    return [condition for condition in raw if isinstance(condition, Mapping)]


def x__conditions__mutmut_8(item: Mapping[str, object]) -> list[Mapping[str, object]]:
    status = item.get("status")
    if not isinstance(status, Mapping):
        return []
    raw = status.get("XXconditionsXX")
    if not isinstance(raw, list):
        return []
    return [condition for condition in raw if isinstance(condition, Mapping)]


def x__conditions__mutmut_9(item: Mapping[str, object]) -> list[Mapping[str, object]]:
    status = item.get("status")
    if not isinstance(status, Mapping):
        return []
    raw = status.get("CONDITIONS")
    if not isinstance(raw, list):
        return []
    return [condition for condition in raw if isinstance(condition, Mapping)]


def x__conditions__mutmut_10(item: Mapping[str, object]) -> list[Mapping[str, object]]:
    status = item.get("status")
    if not isinstance(status, Mapping):
        return []
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
mutants_x__conditions__mutmut['x__conditions__mutmut_6'] = x__conditions__mutmut_6 # type: ignore # mutmut generated
mutants_x__conditions__mutmut['x__conditions__mutmut_7'] = x__conditions__mutmut_7 # type: ignore # mutmut generated
mutants_x__conditions__mutmut['x__conditions__mutmut_8'] = x__conditions__mutmut_8 # type: ignore # mutmut generated
mutants_x__conditions__mutmut['x__conditions__mutmut_9'] = x__conditions__mutmut_9 # type: ignore # mutmut generated
mutants_x__conditions__mutmut['x__conditions__mutmut_10'] = x__conditions__mutmut_10 # type: ignore # mutmut generated
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
mutants_x__condition_status__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__condition_status__mutmut)
def _condition_status(conditions: list[Mapping[str, object]], condition_type: str) -> str:
    condition = _find_condition(conditions, condition_type)
    return str(condition.get("status", "")) if condition is not None else ""


def x__condition_status__mutmut_orig(conditions: list[Mapping[str, object]], condition_type: str) -> str:
    condition = _find_condition(conditions, condition_type)
    return str(condition.get("status", "")) if condition is not None else ""


def x__condition_status__mutmut_1(conditions: list[Mapping[str, object]], condition_type: str) -> str:
    condition = None
    return str(condition.get("status", "")) if condition is not None else ""


def x__condition_status__mutmut_2(conditions: list[Mapping[str, object]], condition_type: str) -> str:
    condition = _find_condition(None, condition_type)
    return str(condition.get("status", "")) if condition is not None else ""


def x__condition_status__mutmut_3(conditions: list[Mapping[str, object]], condition_type: str) -> str:
    condition = _find_condition(conditions, None)
    return str(condition.get("status", "")) if condition is not None else ""


def x__condition_status__mutmut_4(conditions: list[Mapping[str, object]], condition_type: str) -> str:
    condition = _find_condition(condition_type)
    return str(condition.get("status", "")) if condition is not None else ""


def x__condition_status__mutmut_5(conditions: list[Mapping[str, object]], condition_type: str) -> str:
    condition = _find_condition(conditions, )
    return str(condition.get("status", "")) if condition is not None else ""


def x__condition_status__mutmut_6(conditions: list[Mapping[str, object]], condition_type: str) -> str:
    condition = _find_condition(conditions, condition_type)
    return str(None) if condition is not None else ""


def x__condition_status__mutmut_7(conditions: list[Mapping[str, object]], condition_type: str) -> str:
    condition = _find_condition(conditions, condition_type)
    return str(condition.get(None, "")) if condition is not None else ""


def x__condition_status__mutmut_8(conditions: list[Mapping[str, object]], condition_type: str) -> str:
    condition = _find_condition(conditions, condition_type)
    return str(condition.get("status", None)) if condition is not None else ""


def x__condition_status__mutmut_9(conditions: list[Mapping[str, object]], condition_type: str) -> str:
    condition = _find_condition(conditions, condition_type)
    return str(condition.get("")) if condition is not None else ""


def x__condition_status__mutmut_10(conditions: list[Mapping[str, object]], condition_type: str) -> str:
    condition = _find_condition(conditions, condition_type)
    return str(condition.get("status", )) if condition is not None else ""


def x__condition_status__mutmut_11(conditions: list[Mapping[str, object]], condition_type: str) -> str:
    condition = _find_condition(conditions, condition_type)
    return str(condition.get("XXstatusXX", "")) if condition is not None else ""


def x__condition_status__mutmut_12(conditions: list[Mapping[str, object]], condition_type: str) -> str:
    condition = _find_condition(conditions, condition_type)
    return str(condition.get("STATUS", "")) if condition is not None else ""


def x__condition_status__mutmut_13(conditions: list[Mapping[str, object]], condition_type: str) -> str:
    condition = _find_condition(conditions, condition_type)
    return str(condition.get("status", "XXXX")) if condition is not None else ""


def x__condition_status__mutmut_14(conditions: list[Mapping[str, object]], condition_type: str) -> str:
    condition = _find_condition(conditions, condition_type)
    return str(condition.get("status", "")) if condition is None else ""


def x__condition_status__mutmut_15(conditions: list[Mapping[str, object]], condition_type: str) -> str:
    condition = _find_condition(conditions, condition_type)
    return str(condition.get("status", "")) if condition is not None else "XXXX"

mutants_x__condition_status__mutmut['_mutmut_orig'] = x__condition_status__mutmut_orig # type: ignore # mutmut generated
mutants_x__condition_status__mutmut['x__condition_status__mutmut_1'] = x__condition_status__mutmut_1 # type: ignore # mutmut generated
mutants_x__condition_status__mutmut['x__condition_status__mutmut_2'] = x__condition_status__mutmut_2 # type: ignore # mutmut generated
mutants_x__condition_status__mutmut['x__condition_status__mutmut_3'] = x__condition_status__mutmut_3 # type: ignore # mutmut generated
mutants_x__condition_status__mutmut['x__condition_status__mutmut_4'] = x__condition_status__mutmut_4 # type: ignore # mutmut generated
mutants_x__condition_status__mutmut['x__condition_status__mutmut_5'] = x__condition_status__mutmut_5 # type: ignore # mutmut generated
mutants_x__condition_status__mutmut['x__condition_status__mutmut_6'] = x__condition_status__mutmut_6 # type: ignore # mutmut generated
mutants_x__condition_status__mutmut['x__condition_status__mutmut_7'] = x__condition_status__mutmut_7 # type: ignore # mutmut generated
mutants_x__condition_status__mutmut['x__condition_status__mutmut_8'] = x__condition_status__mutmut_8 # type: ignore # mutmut generated
mutants_x__condition_status__mutmut['x__condition_status__mutmut_9'] = x__condition_status__mutmut_9 # type: ignore # mutmut generated
mutants_x__condition_status__mutmut['x__condition_status__mutmut_10'] = x__condition_status__mutmut_10 # type: ignore # mutmut generated
mutants_x__condition_status__mutmut['x__condition_status__mutmut_11'] = x__condition_status__mutmut_11 # type: ignore # mutmut generated
mutants_x__condition_status__mutmut['x__condition_status__mutmut_12'] = x__condition_status__mutmut_12 # type: ignore # mutmut generated
mutants_x__condition_status__mutmut['x__condition_status__mutmut_13'] = x__condition_status__mutmut_13 # type: ignore # mutmut generated
mutants_x__condition_status__mutmut['x__condition_status__mutmut_14'] = x__condition_status__mutmut_14 # type: ignore # mutmut generated
mutants_x__condition_status__mutmut['x__condition_status__mutmut_15'] = x__condition_status__mutmut_15 # type: ignore # mutmut generated
mutants_x__root_cause_message__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__root_cause_message__mutmut)
def _root_cause_message(conditions: list[Mapping[str, object]]) -> str:
    for condition_type in ("Degraded", "Progressing", "Available"):
        condition = _find_condition(conditions, condition_type)
        if condition is None:
            continue
        message = str(condition.get("message", ""))
        if message:
            return message
    return ""


def x__root_cause_message__mutmut_orig(conditions: list[Mapping[str, object]]) -> str:
    for condition_type in ("Degraded", "Progressing", "Available"):
        condition = _find_condition(conditions, condition_type)
        if condition is None:
            continue
        message = str(condition.get("message", ""))
        if message:
            return message
    return ""


def x__root_cause_message__mutmut_1(conditions: list[Mapping[str, object]]) -> str:
    for condition_type in ("XXDegradedXX", "Progressing", "Available"):
        condition = _find_condition(conditions, condition_type)
        if condition is None:
            continue
        message = str(condition.get("message", ""))
        if message:
            return message
    return ""


def x__root_cause_message__mutmut_2(conditions: list[Mapping[str, object]]) -> str:
    for condition_type in ("degraded", "Progressing", "Available"):
        condition = _find_condition(conditions, condition_type)
        if condition is None:
            continue
        message = str(condition.get("message", ""))
        if message:
            return message
    return ""


def x__root_cause_message__mutmut_3(conditions: list[Mapping[str, object]]) -> str:
    for condition_type in ("DEGRADED", "Progressing", "Available"):
        condition = _find_condition(conditions, condition_type)
        if condition is None:
            continue
        message = str(condition.get("message", ""))
        if message:
            return message
    return ""


def x__root_cause_message__mutmut_4(conditions: list[Mapping[str, object]]) -> str:
    for condition_type in ("Degraded", "XXProgressingXX", "Available"):
        condition = _find_condition(conditions, condition_type)
        if condition is None:
            continue
        message = str(condition.get("message", ""))
        if message:
            return message
    return ""


def x__root_cause_message__mutmut_5(conditions: list[Mapping[str, object]]) -> str:
    for condition_type in ("Degraded", "progressing", "Available"):
        condition = _find_condition(conditions, condition_type)
        if condition is None:
            continue
        message = str(condition.get("message", ""))
        if message:
            return message
    return ""


def x__root_cause_message__mutmut_6(conditions: list[Mapping[str, object]]) -> str:
    for condition_type in ("Degraded", "PROGRESSING", "Available"):
        condition = _find_condition(conditions, condition_type)
        if condition is None:
            continue
        message = str(condition.get("message", ""))
        if message:
            return message
    return ""


def x__root_cause_message__mutmut_7(conditions: list[Mapping[str, object]]) -> str:
    for condition_type in ("Degraded", "Progressing", "XXAvailableXX"):
        condition = _find_condition(conditions, condition_type)
        if condition is None:
            continue
        message = str(condition.get("message", ""))
        if message:
            return message
    return ""


def x__root_cause_message__mutmut_8(conditions: list[Mapping[str, object]]) -> str:
    for condition_type in ("Degraded", "Progressing", "available"):
        condition = _find_condition(conditions, condition_type)
        if condition is None:
            continue
        message = str(condition.get("message", ""))
        if message:
            return message
    return ""


def x__root_cause_message__mutmut_9(conditions: list[Mapping[str, object]]) -> str:
    for condition_type in ("Degraded", "Progressing", "AVAILABLE"):
        condition = _find_condition(conditions, condition_type)
        if condition is None:
            continue
        message = str(condition.get("message", ""))
        if message:
            return message
    return ""


def x__root_cause_message__mutmut_10(conditions: list[Mapping[str, object]]) -> str:
    for condition_type in ("Degraded", "Progressing", "Available"):
        condition = None
        if condition is None:
            continue
        message = str(condition.get("message", ""))
        if message:
            return message
    return ""


def x__root_cause_message__mutmut_11(conditions: list[Mapping[str, object]]) -> str:
    for condition_type in ("Degraded", "Progressing", "Available"):
        condition = _find_condition(None, condition_type)
        if condition is None:
            continue
        message = str(condition.get("message", ""))
        if message:
            return message
    return ""


def x__root_cause_message__mutmut_12(conditions: list[Mapping[str, object]]) -> str:
    for condition_type in ("Degraded", "Progressing", "Available"):
        condition = _find_condition(conditions, None)
        if condition is None:
            continue
        message = str(condition.get("message", ""))
        if message:
            return message
    return ""


def x__root_cause_message__mutmut_13(conditions: list[Mapping[str, object]]) -> str:
    for condition_type in ("Degraded", "Progressing", "Available"):
        condition = _find_condition(condition_type)
        if condition is None:
            continue
        message = str(condition.get("message", ""))
        if message:
            return message
    return ""


def x__root_cause_message__mutmut_14(conditions: list[Mapping[str, object]]) -> str:
    for condition_type in ("Degraded", "Progressing", "Available"):
        condition = _find_condition(conditions, )
        if condition is None:
            continue
        message = str(condition.get("message", ""))
        if message:
            return message
    return ""


def x__root_cause_message__mutmut_15(conditions: list[Mapping[str, object]]) -> str:
    for condition_type in ("Degraded", "Progressing", "Available"):
        condition = _find_condition(conditions, condition_type)
        if condition is not None:
            continue
        message = str(condition.get("message", ""))
        if message:
            return message
    return ""


def x__root_cause_message__mutmut_16(conditions: list[Mapping[str, object]]) -> str:
    for condition_type in ("Degraded", "Progressing", "Available"):
        condition = _find_condition(conditions, condition_type)
        if condition is None:
            break
        message = str(condition.get("message", ""))
        if message:
            return message
    return ""


def x__root_cause_message__mutmut_17(conditions: list[Mapping[str, object]]) -> str:
    for condition_type in ("Degraded", "Progressing", "Available"):
        condition = _find_condition(conditions, condition_type)
        if condition is None:
            continue
        message = None
        if message:
            return message
    return ""


def x__root_cause_message__mutmut_18(conditions: list[Mapping[str, object]]) -> str:
    for condition_type in ("Degraded", "Progressing", "Available"):
        condition = _find_condition(conditions, condition_type)
        if condition is None:
            continue
        message = str(None)
        if message:
            return message
    return ""


def x__root_cause_message__mutmut_19(conditions: list[Mapping[str, object]]) -> str:
    for condition_type in ("Degraded", "Progressing", "Available"):
        condition = _find_condition(conditions, condition_type)
        if condition is None:
            continue
        message = str(condition.get(None, ""))
        if message:
            return message
    return ""


def x__root_cause_message__mutmut_20(conditions: list[Mapping[str, object]]) -> str:
    for condition_type in ("Degraded", "Progressing", "Available"):
        condition = _find_condition(conditions, condition_type)
        if condition is None:
            continue
        message = str(condition.get("message", None))
        if message:
            return message
    return ""


def x__root_cause_message__mutmut_21(conditions: list[Mapping[str, object]]) -> str:
    for condition_type in ("Degraded", "Progressing", "Available"):
        condition = _find_condition(conditions, condition_type)
        if condition is None:
            continue
        message = str(condition.get(""))
        if message:
            return message
    return ""


def x__root_cause_message__mutmut_22(conditions: list[Mapping[str, object]]) -> str:
    for condition_type in ("Degraded", "Progressing", "Available"):
        condition = _find_condition(conditions, condition_type)
        if condition is None:
            continue
        message = str(condition.get("message", ))
        if message:
            return message
    return ""


def x__root_cause_message__mutmut_23(conditions: list[Mapping[str, object]]) -> str:
    for condition_type in ("Degraded", "Progressing", "Available"):
        condition = _find_condition(conditions, condition_type)
        if condition is None:
            continue
        message = str(condition.get("XXmessageXX", ""))
        if message:
            return message
    return ""


def x__root_cause_message__mutmut_24(conditions: list[Mapping[str, object]]) -> str:
    for condition_type in ("Degraded", "Progressing", "Available"):
        condition = _find_condition(conditions, condition_type)
        if condition is None:
            continue
        message = str(condition.get("MESSAGE", ""))
        if message:
            return message
    return ""


def x__root_cause_message__mutmut_25(conditions: list[Mapping[str, object]]) -> str:
    for condition_type in ("Degraded", "Progressing", "Available"):
        condition = _find_condition(conditions, condition_type)
        if condition is None:
            continue
        message = str(condition.get("message", "XXXX"))
        if message:
            return message
    return ""


def x__root_cause_message__mutmut_26(conditions: list[Mapping[str, object]]) -> str:
    for condition_type in ("Degraded", "Progressing", "Available"):
        condition = _find_condition(conditions, condition_type)
        if condition is None:
            continue
        message = str(condition.get("message", ""))
        if message:
            return message
    return "XXXX"

mutants_x__root_cause_message__mutmut['_mutmut_orig'] = x__root_cause_message__mutmut_orig # type: ignore # mutmut generated
mutants_x__root_cause_message__mutmut['x__root_cause_message__mutmut_1'] = x__root_cause_message__mutmut_1 # type: ignore # mutmut generated
mutants_x__root_cause_message__mutmut['x__root_cause_message__mutmut_2'] = x__root_cause_message__mutmut_2 # type: ignore # mutmut generated
mutants_x__root_cause_message__mutmut['x__root_cause_message__mutmut_3'] = x__root_cause_message__mutmut_3 # type: ignore # mutmut generated
mutants_x__root_cause_message__mutmut['x__root_cause_message__mutmut_4'] = x__root_cause_message__mutmut_4 # type: ignore # mutmut generated
mutants_x__root_cause_message__mutmut['x__root_cause_message__mutmut_5'] = x__root_cause_message__mutmut_5 # type: ignore # mutmut generated
mutants_x__root_cause_message__mutmut['x__root_cause_message__mutmut_6'] = x__root_cause_message__mutmut_6 # type: ignore # mutmut generated
mutants_x__root_cause_message__mutmut['x__root_cause_message__mutmut_7'] = x__root_cause_message__mutmut_7 # type: ignore # mutmut generated
mutants_x__root_cause_message__mutmut['x__root_cause_message__mutmut_8'] = x__root_cause_message__mutmut_8 # type: ignore # mutmut generated
mutants_x__root_cause_message__mutmut['x__root_cause_message__mutmut_9'] = x__root_cause_message__mutmut_9 # type: ignore # mutmut generated
mutants_x__root_cause_message__mutmut['x__root_cause_message__mutmut_10'] = x__root_cause_message__mutmut_10 # type: ignore # mutmut generated
mutants_x__root_cause_message__mutmut['x__root_cause_message__mutmut_11'] = x__root_cause_message__mutmut_11 # type: ignore # mutmut generated
mutants_x__root_cause_message__mutmut['x__root_cause_message__mutmut_12'] = x__root_cause_message__mutmut_12 # type: ignore # mutmut generated
mutants_x__root_cause_message__mutmut['x__root_cause_message__mutmut_13'] = x__root_cause_message__mutmut_13 # type: ignore # mutmut generated
mutants_x__root_cause_message__mutmut['x__root_cause_message__mutmut_14'] = x__root_cause_message__mutmut_14 # type: ignore # mutmut generated
mutants_x__root_cause_message__mutmut['x__root_cause_message__mutmut_15'] = x__root_cause_message__mutmut_15 # type: ignore # mutmut generated
mutants_x__root_cause_message__mutmut['x__root_cause_message__mutmut_16'] = x__root_cause_message__mutmut_16 # type: ignore # mutmut generated
mutants_x__root_cause_message__mutmut['x__root_cause_message__mutmut_17'] = x__root_cause_message__mutmut_17 # type: ignore # mutmut generated
mutants_x__root_cause_message__mutmut['x__root_cause_message__mutmut_18'] = x__root_cause_message__mutmut_18 # type: ignore # mutmut generated
mutants_x__root_cause_message__mutmut['x__root_cause_message__mutmut_19'] = x__root_cause_message__mutmut_19 # type: ignore # mutmut generated
mutants_x__root_cause_message__mutmut['x__root_cause_message__mutmut_20'] = x__root_cause_message__mutmut_20 # type: ignore # mutmut generated
mutants_x__root_cause_message__mutmut['x__root_cause_message__mutmut_21'] = x__root_cause_message__mutmut_21 # type: ignore # mutmut generated
mutants_x__root_cause_message__mutmut['x__root_cause_message__mutmut_22'] = x__root_cause_message__mutmut_22 # type: ignore # mutmut generated
mutants_x__root_cause_message__mutmut['x__root_cause_message__mutmut_23'] = x__root_cause_message__mutmut_23 # type: ignore # mutmut generated
mutants_x__root_cause_message__mutmut['x__root_cause_message__mutmut_24'] = x__root_cause_message__mutmut_24 # type: ignore # mutmut generated
mutants_x__root_cause_message__mutmut['x__root_cause_message__mutmut_25'] = x__root_cause_message__mutmut_25 # type: ignore # mutmut generated
mutants_x__root_cause_message__mutmut['x__root_cause_message__mutmut_26'] = x__root_cause_message__mutmut_26 # type: ignore # mutmut generated
mutants_x__degraded_since__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__degraded_since__mutmut)
def _degraded_since(conditions: list[Mapping[str, object]]) -> str | None:
    condition = _find_condition(conditions, "Degraded")
    if condition is None or str(condition.get("status", "")) != _CONDITION_TRUE:
        return None
    last_transition = condition.get("lastTransitionTime")
    return str(last_transition) if last_transition else None


def x__degraded_since__mutmut_orig(conditions: list[Mapping[str, object]]) -> str | None:
    condition = _find_condition(conditions, "Degraded")
    if condition is None or str(condition.get("status", "")) != _CONDITION_TRUE:
        return None
    last_transition = condition.get("lastTransitionTime")
    return str(last_transition) if last_transition else None


def x__degraded_since__mutmut_1(conditions: list[Mapping[str, object]]) -> str | None:
    condition = None
    if condition is None or str(condition.get("status", "")) != _CONDITION_TRUE:
        return None
    last_transition = condition.get("lastTransitionTime")
    return str(last_transition) if last_transition else None


def x__degraded_since__mutmut_2(conditions: list[Mapping[str, object]]) -> str | None:
    condition = _find_condition(None, "Degraded")
    if condition is None or str(condition.get("status", "")) != _CONDITION_TRUE:
        return None
    last_transition = condition.get("lastTransitionTime")
    return str(last_transition) if last_transition else None


def x__degraded_since__mutmut_3(conditions: list[Mapping[str, object]]) -> str | None:
    condition = _find_condition(conditions, None)
    if condition is None or str(condition.get("status", "")) != _CONDITION_TRUE:
        return None
    last_transition = condition.get("lastTransitionTime")
    return str(last_transition) if last_transition else None


def x__degraded_since__mutmut_4(conditions: list[Mapping[str, object]]) -> str | None:
    condition = _find_condition("Degraded")
    if condition is None or str(condition.get("status", "")) != _CONDITION_TRUE:
        return None
    last_transition = condition.get("lastTransitionTime")
    return str(last_transition) if last_transition else None


def x__degraded_since__mutmut_5(conditions: list[Mapping[str, object]]) -> str | None:
    condition = _find_condition(conditions, )
    if condition is None or str(condition.get("status", "")) != _CONDITION_TRUE:
        return None
    last_transition = condition.get("lastTransitionTime")
    return str(last_transition) if last_transition else None


def x__degraded_since__mutmut_6(conditions: list[Mapping[str, object]]) -> str | None:
    condition = _find_condition(conditions, "XXDegradedXX")
    if condition is None or str(condition.get("status", "")) != _CONDITION_TRUE:
        return None
    last_transition = condition.get("lastTransitionTime")
    return str(last_transition) if last_transition else None


def x__degraded_since__mutmut_7(conditions: list[Mapping[str, object]]) -> str | None:
    condition = _find_condition(conditions, "degraded")
    if condition is None or str(condition.get("status", "")) != _CONDITION_TRUE:
        return None
    last_transition = condition.get("lastTransitionTime")
    return str(last_transition) if last_transition else None


def x__degraded_since__mutmut_8(conditions: list[Mapping[str, object]]) -> str | None:
    condition = _find_condition(conditions, "DEGRADED")
    if condition is None or str(condition.get("status", "")) != _CONDITION_TRUE:
        return None
    last_transition = condition.get("lastTransitionTime")
    return str(last_transition) if last_transition else None


def x__degraded_since__mutmut_9(conditions: list[Mapping[str, object]]) -> str | None:
    condition = _find_condition(conditions, "Degraded")
    if condition is None and str(condition.get("status", "")) != _CONDITION_TRUE:
        return None
    last_transition = condition.get("lastTransitionTime")
    return str(last_transition) if last_transition else None


def x__degraded_since__mutmut_10(conditions: list[Mapping[str, object]]) -> str | None:
    condition = _find_condition(conditions, "Degraded")
    if condition is not None or str(condition.get("status", "")) != _CONDITION_TRUE:
        return None
    last_transition = condition.get("lastTransitionTime")
    return str(last_transition) if last_transition else None


def x__degraded_since__mutmut_11(conditions: list[Mapping[str, object]]) -> str | None:
    condition = _find_condition(conditions, "Degraded")
    if condition is None or str(None) != _CONDITION_TRUE:
        return None
    last_transition = condition.get("lastTransitionTime")
    return str(last_transition) if last_transition else None


def x__degraded_since__mutmut_12(conditions: list[Mapping[str, object]]) -> str | None:
    condition = _find_condition(conditions, "Degraded")
    if condition is None or str(condition.get(None, "")) != _CONDITION_TRUE:
        return None
    last_transition = condition.get("lastTransitionTime")
    return str(last_transition) if last_transition else None


def x__degraded_since__mutmut_13(conditions: list[Mapping[str, object]]) -> str | None:
    condition = _find_condition(conditions, "Degraded")
    if condition is None or str(condition.get("status", None)) != _CONDITION_TRUE:
        return None
    last_transition = condition.get("lastTransitionTime")
    return str(last_transition) if last_transition else None


def x__degraded_since__mutmut_14(conditions: list[Mapping[str, object]]) -> str | None:
    condition = _find_condition(conditions, "Degraded")
    if condition is None or str(condition.get("")) != _CONDITION_TRUE:
        return None
    last_transition = condition.get("lastTransitionTime")
    return str(last_transition) if last_transition else None


def x__degraded_since__mutmut_15(conditions: list[Mapping[str, object]]) -> str | None:
    condition = _find_condition(conditions, "Degraded")
    if condition is None or str(condition.get("status", )) != _CONDITION_TRUE:
        return None
    last_transition = condition.get("lastTransitionTime")
    return str(last_transition) if last_transition else None


def x__degraded_since__mutmut_16(conditions: list[Mapping[str, object]]) -> str | None:
    condition = _find_condition(conditions, "Degraded")
    if condition is None or str(condition.get("XXstatusXX", "")) != _CONDITION_TRUE:
        return None
    last_transition = condition.get("lastTransitionTime")
    return str(last_transition) if last_transition else None


def x__degraded_since__mutmut_17(conditions: list[Mapping[str, object]]) -> str | None:
    condition = _find_condition(conditions, "Degraded")
    if condition is None or str(condition.get("STATUS", "")) != _CONDITION_TRUE:
        return None
    last_transition = condition.get("lastTransitionTime")
    return str(last_transition) if last_transition else None


def x__degraded_since__mutmut_18(conditions: list[Mapping[str, object]]) -> str | None:
    condition = _find_condition(conditions, "Degraded")
    if condition is None or str(condition.get("status", "XXXX")) != _CONDITION_TRUE:
        return None
    last_transition = condition.get("lastTransitionTime")
    return str(last_transition) if last_transition else None


def x__degraded_since__mutmut_19(conditions: list[Mapping[str, object]]) -> str | None:
    condition = _find_condition(conditions, "Degraded")
    if condition is None or str(condition.get("status", "")) == _CONDITION_TRUE:
        return None
    last_transition = condition.get("lastTransitionTime")
    return str(last_transition) if last_transition else None


def x__degraded_since__mutmut_20(conditions: list[Mapping[str, object]]) -> str | None:
    condition = _find_condition(conditions, "Degraded")
    if condition is None or str(condition.get("status", "")) != _CONDITION_TRUE:
        return None
    last_transition = None
    return str(last_transition) if last_transition else None


def x__degraded_since__mutmut_21(conditions: list[Mapping[str, object]]) -> str | None:
    condition = _find_condition(conditions, "Degraded")
    if condition is None or str(condition.get("status", "")) != _CONDITION_TRUE:
        return None
    last_transition = condition.get(None)
    return str(last_transition) if last_transition else None


def x__degraded_since__mutmut_22(conditions: list[Mapping[str, object]]) -> str | None:
    condition = _find_condition(conditions, "Degraded")
    if condition is None or str(condition.get("status", "")) != _CONDITION_TRUE:
        return None
    last_transition = condition.get("XXlastTransitionTimeXX")
    return str(last_transition) if last_transition else None


def x__degraded_since__mutmut_23(conditions: list[Mapping[str, object]]) -> str | None:
    condition = _find_condition(conditions, "Degraded")
    if condition is None or str(condition.get("status", "")) != _CONDITION_TRUE:
        return None
    last_transition = condition.get("lasttransitiontime")
    return str(last_transition) if last_transition else None


def x__degraded_since__mutmut_24(conditions: list[Mapping[str, object]]) -> str | None:
    condition = _find_condition(conditions, "Degraded")
    if condition is None or str(condition.get("status", "")) != _CONDITION_TRUE:
        return None
    last_transition = condition.get("LASTTRANSITIONTIME")
    return str(last_transition) if last_transition else None


def x__degraded_since__mutmut_25(conditions: list[Mapping[str, object]]) -> str | None:
    condition = _find_condition(conditions, "Degraded")
    if condition is None or str(condition.get("status", "")) != _CONDITION_TRUE:
        return None
    last_transition = condition.get("lastTransitionTime")
    return str(None) if last_transition else None

mutants_x__degraded_since__mutmut['_mutmut_orig'] = x__degraded_since__mutmut_orig # type: ignore # mutmut generated
mutants_x__degraded_since__mutmut['x__degraded_since__mutmut_1'] = x__degraded_since__mutmut_1 # type: ignore # mutmut generated
mutants_x__degraded_since__mutmut['x__degraded_since__mutmut_2'] = x__degraded_since__mutmut_2 # type: ignore # mutmut generated
mutants_x__degraded_since__mutmut['x__degraded_since__mutmut_3'] = x__degraded_since__mutmut_3 # type: ignore # mutmut generated
mutants_x__degraded_since__mutmut['x__degraded_since__mutmut_4'] = x__degraded_since__mutmut_4 # type: ignore # mutmut generated
mutants_x__degraded_since__mutmut['x__degraded_since__mutmut_5'] = x__degraded_since__mutmut_5 # type: ignore # mutmut generated
mutants_x__degraded_since__mutmut['x__degraded_since__mutmut_6'] = x__degraded_since__mutmut_6 # type: ignore # mutmut generated
mutants_x__degraded_since__mutmut['x__degraded_since__mutmut_7'] = x__degraded_since__mutmut_7 # type: ignore # mutmut generated
mutants_x__degraded_since__mutmut['x__degraded_since__mutmut_8'] = x__degraded_since__mutmut_8 # type: ignore # mutmut generated
mutants_x__degraded_since__mutmut['x__degraded_since__mutmut_9'] = x__degraded_since__mutmut_9 # type: ignore # mutmut generated
mutants_x__degraded_since__mutmut['x__degraded_since__mutmut_10'] = x__degraded_since__mutmut_10 # type: ignore # mutmut generated
mutants_x__degraded_since__mutmut['x__degraded_since__mutmut_11'] = x__degraded_since__mutmut_11 # type: ignore # mutmut generated
mutants_x__degraded_since__mutmut['x__degraded_since__mutmut_12'] = x__degraded_since__mutmut_12 # type: ignore # mutmut generated
mutants_x__degraded_since__mutmut['x__degraded_since__mutmut_13'] = x__degraded_since__mutmut_13 # type: ignore # mutmut generated
mutants_x__degraded_since__mutmut['x__degraded_since__mutmut_14'] = x__degraded_since__mutmut_14 # type: ignore # mutmut generated
mutants_x__degraded_since__mutmut['x__degraded_since__mutmut_15'] = x__degraded_since__mutmut_15 # type: ignore # mutmut generated
mutants_x__degraded_since__mutmut['x__degraded_since__mutmut_16'] = x__degraded_since__mutmut_16 # type: ignore # mutmut generated
mutants_x__degraded_since__mutmut['x__degraded_since__mutmut_17'] = x__degraded_since__mutmut_17 # type: ignore # mutmut generated
mutants_x__degraded_since__mutmut['x__degraded_since__mutmut_18'] = x__degraded_since__mutmut_18 # type: ignore # mutmut generated
mutants_x__degraded_since__mutmut['x__degraded_since__mutmut_19'] = x__degraded_since__mutmut_19 # type: ignore # mutmut generated
mutants_x__degraded_since__mutmut['x__degraded_since__mutmut_20'] = x__degraded_since__mutmut_20 # type: ignore # mutmut generated
mutants_x__degraded_since__mutmut['x__degraded_since__mutmut_21'] = x__degraded_since__mutmut_21 # type: ignore # mutmut generated
mutants_x__degraded_since__mutmut['x__degraded_since__mutmut_22'] = x__degraded_since__mutmut_22 # type: ignore # mutmut generated
mutants_x__degraded_since__mutmut['x__degraded_since__mutmut_23'] = x__degraded_since__mutmut_23 # type: ignore # mutmut generated
mutants_x__degraded_since__mutmut['x__degraded_since__mutmut_24'] = x__degraded_since__mutmut_24 # type: ignore # mutmut generated
mutants_x__degraded_since__mutmut['x__degraded_since__mutmut_25'] = x__degraded_since__mutmut_25 # type: ignore # mutmut generated
