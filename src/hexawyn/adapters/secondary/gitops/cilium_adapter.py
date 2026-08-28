"""CiliumAdapter — detects a Cilium installation via VanillaAdapter."""

from __future__ import annotations

import re
from typing import NoReturn, cast

from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter
from hexawyn.application.ports.driven.cilium_port import CiliumPort
from hexawyn.domain.errors import (
    AdapterTimeoutError,
    ClusterUnreachableError,
    InsufficientPermissionsError,
    ResourceNotFoundError,
)
from hexawyn.domain.models.cilium import (
    CiliumAgentHealth,
    CiliumDetectionResult,
    CiliumNetworkPoliciesResult,
    CiliumNetworkPolicyDetail,
    CiliumNetworkPolicyInfo,
    CiliumStatusResult,
)
from hexawyn.domain.services.cilium.network_policy_summary import (
    build_network_policy,
    build_policies_result,
    not_installed_policies_result,
)
from hexawyn.domain.services.cilium.policy_detail_builder import (
    build_policy_detail,
    not_installed_policy_detail,
)
from hexawyn.domain.services.cilium.status_report_builder import (
    build_status_result,
    crds_only_result,
    not_installed_result,
)

_CILIUM_GROUP = "cilium.io"
_CILIUM_VERSION = "v2"
_CILIUM_PLURAL = "ciliumnodes"
_AGENT_CONTAINER = "cilium-agent"
_CONFIGMAP_NAME = "cilium-config"
_AGENT_LABEL_SELECTOR = "k8s-app=cilium"

_FORBIDDEN_STATUS = 403
_NOT_FOUND_STATUS = 404

_MODE_MAP = {
    "tunnel": "tunnel",
    "native": "native-routing",
    "cluster": "cluster",
    "ipvlan": "ipvlan",
}


def _to_snake(name: str) -> str:
    """camelCase attribute name to snake_case (``nodeName`` -> ``node_name``)."""
    return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()


def _get(obj: object, key: str) -> object:
    """Read ``key`` from a dict (camelCase key) or an object (snake_case attr)."""
    if obj is None:
        return None
    if isinstance(obj, dict):
        return obj.get(key)
    return getattr(obj, _to_snake(key), None)


def _items(response: object) -> list[object]:
    """List of items from a k8s list response (dict or object)."""
    if isinstance(response, dict):
        raw = response.get("items", [])
    elif response is not None:
        raw = getattr(response, "items", [])
    else:
        return []
    return raw if isinstance(raw, list) else []


def _safe_int(value: object) -> int:
    if value is None:
        return 0
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int):
        return value
    try:
        return int(str(value))
    except ValueError:
        return 0


class CiliumAdapter(CiliumPort):
    """Real Cilium adapter using VanillaAdapter's API clients."""

    def __init__(self, vanilla: VanillaAdapter) -> None:
        self._vanilla = vanilla

    def detect(self) -> CiliumDetectionResult:
        try:
            apps_api = self._vanilla._apps_api_client()
            daemonset_list = getattr(apps_api, "list_daemon_set_for_all_namespaces")()
        except Exception as exc:
            self._raise_translated(exc)

        self._raise_if_error_status(daemonset_list)
        daemonset = self._find_daemonset(_items(daemonset_list))
        if daemonset is not None:
            return self._build_installed_result(daemonset)
        return self._crds_only_or_not_installed()

    def status(self) -> CiliumStatusResult:
        try:
            apps_api = self._vanilla._apps_api_client()
            daemonset_list = getattr(apps_api, "list_daemon_set_for_all_namespaces")()
        except Exception as exc:
            self._raise_translated(exc)

        self._raise_if_error_status(daemonset_list)
        daemonset = self._find_daemonset(_items(daemonset_list))
        if daemonset is None:
            return self._crds_only_or_empty_status()
        namespace = _get(_get(daemonset, "metadata"), "namespace")
        return build_status_result(self._list_agents(namespace))

    def _crds_only_or_empty_status(self) -> CiliumStatusResult:
        try:
            crd_api = self._vanilla._crd_api_client()
            crd_list = getattr(crd_api, "list_cluster_custom_object")(
                group=_CILIUM_GROUP,
                version=_CILIUM_VERSION,
                plural=_CILIUM_PLURAL,
            )
        except Exception as exc:
            if getattr(exc, "status", None) == _NOT_FOUND_STATUS:
                return not_installed_result()
            self._raise_translated(exc)

        if _items(crd_list):
            return crds_only_result(
                note="Cilium CRDs are present but no cilium DaemonSet was found"
            )
        return not_installed_result()

    def list_network_policies(self) -> CiliumNetworkPoliciesResult:
        namespaced = self._list_cilium_crd("ciliumnetworkpolicies")
        clusterwide = self._list_cilium_crd("ciliumclusterwidenetworkpolicies")
        if namespaced is None and clusterwide is None:
            return not_installed_policies_result()
        policies: list[CiliumNetworkPolicyInfo] = []
        for item in namespaced or []:
            policies.append(build_network_policy("CiliumNetworkPolicy", item))
        for item in clusterwide or []:
            policies.append(build_network_policy("CiliumClusterwideNetworkPolicy", item))
        return build_policies_result(policies)

    def _list_cilium_crd(self, plural: str) -> list[dict[str, object]] | None:
        try:
            crd_api = self._vanilla._crd_api_client()
            raw = getattr(crd_api, "list_cluster_custom_object")(
                group=_CILIUM_GROUP,
                version=_CILIUM_VERSION,
                plural=plural,
            )
        except Exception as exc:
            if getattr(exc, "status", None) == _NOT_FOUND_STATUS:
                return None
            self._raise_translated(exc)
        return [cast(dict[str, object], item) for item in _items(raw) if isinstance(item, dict)]

    def get_network_policy(self, name: str, namespace: str | None) -> CiliumNetworkPolicyDetail:
        if namespace:
            kind = "CiliumNetworkPolicy"
            plural = "ciliumnetworkpolicies"
        else:
            kind = "CiliumClusterwideNetworkPolicy"
            plural = "ciliumclusterwidenetworkpolicies"
        if self._list_cilium_crd(plural) is None:
            return not_installed_policy_detail()
        try:
            crd_api = self._vanilla._crd_api_client()
            if namespace:
                raw = getattr(crd_api, "get_namespaced_custom_object")(
                    group=_CILIUM_GROUP,
                    version=_CILIUM_VERSION,
                    namespace=namespace,
                    plural=plural,
                    name=name,
                )
            else:
                raw = getattr(crd_api, "get_cluster_custom_object")(
                    group=_CILIUM_GROUP,
                    version=_CILIUM_VERSION,
                    plural=plural,
                    name=name,
                )
        except Exception as exc:
            if getattr(exc, "status", None) == _NOT_FOUND_STATUS:
                raise ResourceNotFoundError(f"Cilium network policy '{name}' not found")
            self._raise_translated(exc)
        return build_policy_detail(kind, namespace, cast(dict[str, object], raw))

    def _raise_if_error_status(self, response: object) -> None:
        """Raise RBAC errors carried on a returned response object."""
        if getattr(response, "status", None) == _FORBIDDEN_STATUS:
            raise InsufficientPermissionsError(str(response))

    def _raise_translated(self, exc: Exception) -> NoReturn:
        """Translate an infra exception to a domain HexawynError."""
        status = getattr(exc, "status", None)
        if status == _FORBIDDEN_STATUS:
            raise InsufficientPermissionsError(str(exc))
        if isinstance(exc, TimeoutError) or "timeout" in str(exc).lower():
            raise AdapterTimeoutError(str(exc))
        raise ClusterUnreachableError(str(exc))

    @staticmethod
    def _find_daemonset(items: list[object]) -> object | None:
        for item in items:
            if _get(_get(item, "metadata"), "name") == "cilium":
                return item
        return None

    def _find_container(self, daemonset: object, name: str) -> object | None:
        spec = _get(daemonset, "spec")
        template = _get(spec, "template")
        pod_spec = _get(template, "spec")
        containers = _get(pod_spec, "containers")
        if not isinstance(containers, list):
            return None
        for container in cast(list[object], containers):
            if _get(container, "name") == name:
                return container
        return None

    def _build_installed_result(self, daemonset: object) -> CiliumDetectionResult:
        container = self._find_container(daemonset, _AGENT_CONTAINER)
        image = _get(container, "image") if container is not None else None
        version = self._parse_image_version(image) if isinstance(image, str) else None
        namespace = _get(_get(daemonset, "metadata"), "namespace")
        mode = self._detect_mode(namespace)
        agents = self._list_agents(namespace)
        if agents:
            total_agents = len(agents)
            ready_agents = sum(1 for agent in agents if agent.ready)
            degraded_summary = (
                f"{ready_agents}/{total_agents} agents ready"
                if ready_agents < total_agents
                else None
            )
            status = "degraded" if degraded_summary is not None else "installed"
        else:
            daemonset_status = _get(daemonset, "status")
            total_agents = _safe_int(_get(daemonset_status, "desiredNumberScheduled"))
            ready_agents = _safe_int(_get(daemonset_status, "numberReady"))
            degraded_summary = (
                f"{ready_agents}/{total_agents} agents ready"
                if ready_agents < total_agents
                else None
            )
            status = "degraded" if degraded_summary is not None else "installed"

        return CiliumDetectionResult(
            installed=True,
            status=status,
            version=version,
            mode=mode,
            namespace=namespace if isinstance(namespace, str) else None,
            total_agents=total_agents,
            ready_agents=ready_agents,
            degraded_summary=degraded_summary,
            agents=agents,
            note=None,
        )

    def _crds_only_or_not_installed(self) -> CiliumDetectionResult:
        try:
            crd_api = self._vanilla._crd_api_client()
            crd_list = getattr(crd_api, "list_cluster_custom_object")(
                group=_CILIUM_GROUP,
                version=_CILIUM_VERSION,
                plural=_CILIUM_PLURAL,
            )
        except Exception as exc:
            if getattr(exc, "status", None) == _NOT_FOUND_STATUS:
                return self._not_installed()
            self._raise_translated(exc)

        if _items(crd_list):
            return CiliumDetectionResult(
                installed=True,
                status="installed",
                version=None,
                mode="UNKNOWN",
                namespace=None,
                total_agents=0,
                ready_agents=0,
                degraded_summary=None,
                agents=[],
                note="Cilium CRDs are present but no cilium DaemonSet was found",
            )
        return self._not_installed()

    @staticmethod
    def _not_installed() -> CiliumDetectionResult:
        return CiliumDetectionResult(
            installed=False,
            status="not_installed",
            version=None,
            mode="UNKNOWN",
            namespace=None,
            total_agents=0,
            ready_agents=0,
            degraded_summary=None,
            agents=[],
            note="Cilium is not installed in this cluster",
        )

    def _detect_mode(self, namespace: object) -> str:
        if not isinstance(namespace, str):
            return "UNKNOWN"
        try:
            core_api = self._vanilla._api_client()
            configmap = getattr(core_api, "read_namespaced_config_map")(
                name=_CONFIGMAP_NAME, namespace=namespace
            )
        except Exception:
            return "UNKNOWN"
        data = _get(configmap, "data")
        if not isinstance(data, dict):
            return "UNKNOWN"
        routing_mode = data.get("routing-mode")
        if isinstance(routing_mode, str) and routing_mode:
            return _MODE_MAP.get(routing_mode, "UNKNOWN")
        tunnel = data.get("tunnel")
        if isinstance(tunnel, str) and tunnel:
            return "tunnel"
        return "UNKNOWN"

    def _list_agents(self, namespace: object) -> list[CiliumAgentHealth]:
        if not isinstance(namespace, str):
            return []
        try:
            core_api = self._vanilla._api_client()
            pods_response = getattr(core_api, "list_namespaced_pod")(
                namespace=namespace, label_selector=_AGENT_LABEL_SELECTOR
            )
        except Exception:
            return []
        return [self._parse_pod(pod) for pod in _items(pods_response)]

    @staticmethod
    def _parse_pod(pod: object) -> CiliumAgentHealth:
        metadata = _get(pod, "metadata")
        spec = _get(pod, "spec")
        status = _get(pod, "status")
        ready = False
        restart_count = 0
        image: str | None = None
        message: str | None = None
        container_statuses = _get(status, "containerStatuses")
        if isinstance(container_statuses, list):
            for container_status in container_statuses:
                if _get(container_status, "name") != _AGENT_CONTAINER:
                    continue
                ready = bool(_get(container_status, "ready"))
                restart_count = _safe_int(_get(container_status, "restartCount"))
                raw_image = _get(container_status, "image")
                if isinstance(raw_image, str):
                    image = raw_image
                state = _get(container_status, "state")
                waiting = _get(state, "waiting") if state is not None else None
                raw_message = _get(waiting, "message") if waiting is not None else None
                if isinstance(raw_message, str):
                    message = raw_message
        return CiliumAgentHealth(
            node=str(_get(spec, "nodeName") or ""),
            pod_name=str(_get(metadata, "name") or ""),
            namespace=str(_get(metadata, "namespace") or "kube-system"),
            ready=ready,
            phase=str(_get(status, "phase") or "Unknown"),
            restart_count=restart_count,
            image=image,
            message=message,
        )

    @staticmethod
    def _parse_image_version(image: str) -> str | None:
        """Preserve the raw image tag (``v1.16.3``), ``None`` if absent/digest."""
        if not image or "@" in image or ":" not in image:
            return None
        _, tag = image.rsplit(":", 1)
        return tag or None
