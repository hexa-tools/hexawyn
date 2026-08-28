"""CalicoK8sAdapter — real Calico detection via the Kubernetes API.

Reads Calico CRDs (``projectcalico.org``), the ``calico-node`` DaemonSet and the
``tigera-operator`` install resource through the Kubernetes client, then hands
the raw signals to the pure domain service. All errors are translated to
``HexawynError`` subclasses — never a raw ``ApiException``.
"""

from __future__ import annotations

from typing import Any, cast

from hexawyn.adapters.secondary.calico.calico_prometheus_adapter import CalicoPrometheusAdapter
from hexawyn.application.ports.driven.calico_port import CalicoPort
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    HexawynError,
    InsufficientPermissionsError,
    ResourceNotFoundError,
)
from hexawyn.domain.models.calico import (
    CalicoBgpConfiguration,
    CalicoBgpPeer,
    CalicoDetectionResult,
    CalicoDetectionSignals,
    CalicoHostEndpoint,
    CalicoIPPool,
    CalicoNetworkPolicy,
    CalicoNodeAgent,
    CalicoWorkload,
)
from hexawyn.domain.services.calico.detection_service import (
    build_agent_phase,
    build_detection_result,
)
from hexawyn.domain.services.calico.network_policy_service import (
    parse_calico_network_policy,
    parse_global_network_policy,
)

_CALICO_GROUP = "projectcalico.org"
_CALICO_VERSION = "v3"
_TIGERA_GROUP = "operator.tigera.io"
_TIGERA_VERSION = "v1"
_CALICO_NODE_LABEL = "k8s-app=calico-node"
_FORBIDDEN = 403
_NOT_FOUND = 404
_IPIP_ENABLED_MODES = {"always", "crosssubnet"}
_VXLAN_ENABLED_MODES = {"always", "crosssubnet"}
_CALICO_ALLOWED_KINDS = {"NetworkPolicy", "GlobalNetworkPolicy"}


class CalicoK8sAdapter(CalicoPort):
    """K8s-backed Calico port. Collaborators are injectable for testability."""

    def __init__(
        self,
        core_api: Any = None,
        apps_api: Any = None,
        crd_api: Any = None,
        metrics_source: CalicoPrometheusAdapter | None = None,
    ) -> None:
        self._core_api = core_api
        self._apps_api = apps_api
        self._crd_api = crd_api
        self._metrics = metrics_source

    # ── Lazy real clients (only imported when injected collaborators missing) ──
    @property
    def _runtime_core_api(self) -> Any:
        if self._core_api is not None:
            return self._core_api
        from kubernetes import client as k8s

        return k8s.CoreV1Api()

    @property
    def _runtime_apps_api(self) -> Any:
        if self._apps_api is not None:
            return self._apps_api
        from kubernetes import client as k8s

        return k8s.AppsV1Api()

    @property
    def _runtime_crd_api(self) -> Any:
        if self._crd_api is not None:
            return self._crd_api
        from kubernetes import client as k8s

        return k8s.CustomObjectsApi()

    # ── detect ────────────────────────────────────────────────────────────
    def detect(self) -> CalicoDetectionResult:
        pool_raw = self._safe_crd_list("ippools")
        installed = pool_raw is not None
        mode_signals = self._pool_mode_signals(pool_raw)

        tigera = self._has_tigera_install()

        namespace: str | None = None
        version: str | None = None
        daemonset = self._calico_node_daemonset()
        if daemonset:
            installed = True
            ds_namespace, ds_version = daemonset
            namespace = namespace or ds_namespace
            version = version or ds_version

        if version is None:
            version = self._version_from_cluster_information()
        if version is None and tigera:
            version = self._version_from_install()

        mode_signals |= self._felix_mode_signals()
        agents = self._list_node_agents() if installed else []

        signals = CalicoDetectionSignals(
            installed=installed,
            version=version,
            namespace=namespace,
            mode_signals=mode_signals,
            tigera_operator=tigera,
            enterprise=tigera,
            agents=agents,
            error=None,
        )
        return build_detection_result(signals)

    def status(self) -> CalicoDetectionResult:
        return self.detect()

    # ── Network policies ──────────────────────────────────────────────────
    def list_network_policies(self, namespace: str | None = None) -> list[CalicoNetworkPolicy]:
        if not self._is_installed():
            return []
        policies: list[CalicoNetworkPolicy] = []
        global_raw = self._safe_crd_list("globalnetworkpolicies")
        policies.extend(parse_global_network_policy(item) for item in raw_items(global_raw))
        namespaces = [namespace] if namespace is not None else self._namespaces()
        for name in namespaces:
            ns_raw = self._safe_namespaced_list("networkpolicies", name)
            policies.extend(parse_calico_network_policy(item) for item in raw_items(ns_raw))
        return policies

    def get_network_policy(self, name: str, namespace: str) -> CalicoNetworkPolicy | None:
        if not self._is_installed():
            return None
        if namespace:
            raw = self._get_policy_raw(name, namespace)
            if raw is None:
                raise ResourceNotFoundError(
                    f"Calico network policy '{name}' not found in namespace '{namespace}'"
                )
            return self._parse_and_guard(raw, namespaced=True)
        raw = self._get_policy_raw_cluster(name)
        if raw is None:
            raise ResourceNotFoundError(f"Calico GlobalNetworkPolicy '{name}' not found")
        return self._parse_and_guard(raw, namespaced=False)

    def _get_policy_raw(self, name: str, namespace: str) -> dict[str, Any] | None:
        try:
            raw = self._runtime_crd_api.get_namespaced_custom_object(
                group=_CALICO_GROUP,
                version=_CALICO_VERSION,
                namespace=namespace,
                plural="networkpolicies",
                name=name,
            )
        except Exception as exc:
            return self._translate_get(exc)
        return cast(dict[str, Any], raw) if isinstance(raw, dict) else None

    def _get_policy_raw_cluster(self, name: str) -> dict[str, Any] | None:
        try:
            raw = self._runtime_crd_api.get_cluster_custom_object(
                group=_CALICO_GROUP,
                version=_CALICO_VERSION,
                plural="globalnetworkpolicies",
                name=name,
            )
        except Exception as exc:
            return self._translate_get(exc)
        return cast(dict[str, Any], raw) if isinstance(raw, dict) else None

    @staticmethod
    def _translate_get(exc: Exception) -> dict[str, Any] | None:
        status = getattr(exc, "status", None)
        if status == _NOT_FOUND:
            return None
        if status == _FORBIDDEN:
            raise InsufficientPermissionsError(
                "RBAC denied read access to Calico network policies"
            ) from exc
        raise ClusterUnreachableError(f"Cannot read Calico network policy: {exc}") from exc

    @staticmethod
    def _parse_and_guard(raw: dict[str, Any], *, namespaced: bool) -> CalicoNetworkPolicy:
        api_version = str(raw.get("apiVersion", ""))
        kind = str(raw.get("kind", ""))
        if api_version and not api_version.startswith("projectcalico.org"):
            raise HexawynError(f"Non-Calico policy kind refused (apiVersion={api_version})")
        if kind and kind not in _CALICO_ALLOWED_KINDS:
            raise HexawynError(f"Non-Calico policy kind refused (kind={kind})")
        if namespaced:
            return parse_calico_network_policy(raw)
        return parse_global_network_policy(raw)

    def audit_policies(self) -> dict[str, object]:
        if not self._is_installed():
            return {"installed": False, "global": 0, "namespaced": 0}
        policies = self.list_network_policies()
        return {
            "installed": True,
            "global": sum(1 for p in policies if p.namespace == ""),
            "namespaced": sum(1 for p in policies if p.namespace != ""),
            "total": len(policies),
        }

    def list_workloads(self, namespace: str | None = None) -> list[CalicoWorkload]:
        try:
            if namespace:
                result = self._runtime_core_api.list_namespaced_pod(
                    namespace=namespace, timeout_seconds=10
                )
            else:
                result = self._runtime_core_api.list_pod_for_all_namespaces()
        except Exception:
            return []
        counts: dict[str, int] = {}
        for pod in getattr(result, "items", []) or []:
            ns = getattr(getattr(pod, "metadata", None), "namespace", None)
            if ns:
                counts[str(ns)] = counts.get(str(ns), 0) + 1
        return [CalicoWorkload(namespace=ns, pod_count=count) for ns, count in counts.items()]

    # ── IP pools / host endpoints ─────────────────────────────────────────
    def list_ip_pools(self) -> list[CalicoIPPool]:
        if not self._is_installed():
            return []
        raw = self._safe_crd_list("ippools")
        return [self._parse_ip_pool(item) for item in raw_items(raw)]

    def list_host_endpoints(self) -> list[CalicoHostEndpoint]:
        if not self._is_installed():
            return []
        raw = self._safe_crd_list("hostendpoints")
        return [self._parse_host_endpoint(item) for item in raw_items(raw)]

    def bgp_audit(self) -> dict[str, object]:
        if not self._is_installed():
            return {}
        raw = self._safe_crd_list("bgpconfigurations")
        configs = raw_items(raw)
        node_to_node = any("nodeToNodeMeshEnabled" in (c.get("spec") or {}) for c in configs)
        return {"bgp_configurations": len(configs), "node_to_node_mesh_configured": node_to_node}

    def list_bgp_configurations(self) -> list[CalicoBgpConfiguration]:
        if not self._is_installed():
            return []
        raw = self._safe_crd_list("bgpconfigurations")
        return [self._parse_bgp_configuration(item) for item in raw_items(raw)]

    def list_bgp_peers(self) -> list[CalicoBgpPeer]:
        if not self._is_installed():
            return []
        raw = self._safe_crd_list("bgppeers")
        return [self._parse_bgp_peer(item) for item in raw_items(raw)]

    def encryption_status(self) -> dict[str, object]:
        if not self._is_installed():
            return {}
        raw = self._safe_crd_list("felixconfigurations")
        items = raw_items(raw)
        default = next(
            (item for item in items if (item.get("metadata") or {}).get("name") == "default"),
            items[0] if items else None,
        )
        wireguard_enabled: bool | None = None
        if default is not None:
            spec = default.get("spec") or {}
            wireguard_raw = spec.get("wireguardEnabled")
            wireguard_enabled = bool(wireguard_raw) if wireguard_raw is not None else None
        per_node: list[dict[str, object]] = []
        for item in items:
            name = str((item.get("metadata") or {}).get("name", ""))
            if name.startswith("node."):
                spec = item.get("spec") or {}
                wireguard_raw = spec.get("wireguardEnabled")
                per_node.append(
                    {
                        "node": name[len("node.") :],
                        "wireguard_enabled": bool(wireguard_raw)
                        if wireguard_raw is not None
                        else False,
                    }
                )
        return {
            "wireguard_enabled": wireguard_enabled,
            "per_node": per_node,
            "enabled": wireguard_enabled,
        }

    # ── Metrics-backed (delegated) ────────────────────────────────────────
    def felix_metrics(self) -> dict[str, object]:
        if self._metrics is None:
            return {"available": False, "metrics": {}, "error": "no metrics source configured"}
        return self._metrics.felix_metrics()

    def felix_policy_counters(self) -> dict[str, object]:
        if self._metrics is None:
            return {
                "available": False,
                "message": "no metrics source configured",
                "samples": [],
            }
        return self._metrics.felix_policy_counters()

    def connectivity_health(self) -> dict[str, object]:
        if self._metrics is None:
            return {
                "available": False,
                "status": "degraded",
                "detail": "no metrics source configured",
            }
        return self._metrics.connectivity_health()

    # ── Helpers ───────────────────────────────────────────────────────────
    def _is_installed(self) -> bool:
        if self._safe_crd_list("ippools") is not None:
            return True
        return self._calico_node_daemonset() is not None

    def _safe_crd_list(
        self, plural: str, group: str = _CALICO_GROUP, version: str = _CALICO_VERSION
    ) -> dict[str, Any] | None:
        try:
            raw = self._runtime_crd_api.list_cluster_custom_object(
                group=group, version=version, plural=plural
            )
        except Exception as exc:
            return self._translate_and_raise(exc)
        return cast(dict[str, Any], raw) if isinstance(raw, dict) else None

    def _safe_namespaced_list(self, plural: str, namespace: str) -> dict[str, Any] | None:
        try:
            raw = self._runtime_crd_api.list_namespaced_custom_object(
                group=_CALICO_GROUP, version=_CALICO_VERSION, namespace=namespace, plural=plural
            )
        except Exception as exc:
            return self._translate_and_raise(exc)
        return cast(dict[str, Any], raw) if isinstance(raw, dict) else None

    def _translate_and_raise(self, exc: Exception) -> dict[str, Any] | None:
        status = getattr(exc, "status", None)
        if status == _NOT_FOUND:
            return None
        if status == _FORBIDDEN:
            raise InsufficientPermissionsError(
                "RBAC denied access to Calico resources; grant read access to "
                "projectcalico.org CRDs"
            ) from exc
        message = f"Cannot reach Kubernetes API for Calico detection: {exc}"
        raise ClusterUnreachableError(message) from exc

    def _has_tigera_install(self) -> bool:
        raw = self._safe_crd_list("installs", group=_TIGERA_GROUP, version=_TIGERA_VERSION)
        return raw is not None

    def _version_from_cluster_information(self) -> str | None:
        raw = self._safe_crd_list("clusterinformations")
        for item in raw_items(raw):
            spec = item.get("spec") or {}
            version = spec.get("version")
            if isinstance(version, str) and version:
                return version
        return None

    def _version_from_install(self) -> str | None:
        raw = self._safe_crd_list("installs", group=_TIGERA_GROUP, version=_TIGERA_VERSION)
        for item in raw_items(raw):
            spec = item.get("spec") or {}
            version = spec.get("version")
            if isinstance(version, str) and version:
                return version
        return None

    def _calico_node_daemonset(self) -> tuple[str, str | None] | None:
        try:
            result = self._runtime_apps_api.list_daemon_set_for_all_namespaces(
                label_selector=_CALICO_NODE_LABEL
            )
        except Exception:
            return None
        for ds in getattr(result, "items", []) or []:
            namespace = getattr(ds.metadata, "namespace", None)
            containers = getattr(ds.spec.template.spec, "containers", None) or []
            image = ""
            if containers:
                image = getattr(containers[0], "image", "") or ""
            return (str(namespace), self._image_version(image))
        return None

    @staticmethod
    def _image_version(image: str) -> str | None:
        if ":" in image:
            return image.rsplit(":", 1)[-1] or None
        return None

    def _felix_mode_signals(self) -> set[str]:
        raw = self._safe_crd_list("felixconfigurations")
        signals: set[str] = set()
        for item in raw_items(raw):
            spec = item.get("spec") or {}
            if spec.get("bpfEnabled"):
                signals.add("ebpf")
                continue
            gates = spec.get("featureGates") or {}
            if isinstance(gates, dict) and gates.get("BPFEnabled"):
                signals.add("ebpf")
        return signals

    def _pool_mode_signals(self, raw: dict[str, Any] | None) -> set[str]:
        signals: set[str] = set()
        for item in raw_items(raw):
            spec = item.get("spec") or {}
            ipip = str(spec.get("ipipMode", "Never")).lower()
            vxlan = str(spec.get("vxlanMode", "Never")).lower()
            if ipip in _IPIP_ENABLED_MODES:
                signals.add("ipip")
            if vxlan in _VXLAN_ENABLED_MODES:
                signals.add("vxlan")
        return signals

    def _list_node_agents(self) -> list[CalicoNodeAgent]:
        per_node: dict[str, CalicoNodeAgent] = {}
        for pod in self._calico_node_pods():
            node = getattr(pod.spec, "node_name", None) or "unknown"
            phase_raw = getattr(pod.status, "phase", "") or ""
            ready_status = self._pod_ready_status(pod)
            ready = ready_status == "True"
            per_node[node] = CalicoNodeAgent(
                node=str(node),
                phase=build_agent_phase(phase_raw, ready_status),
                ready=ready,
                ready_replicas=1 if ready else 0,
                desired_replicas=1,
                available_replicas=1 if ready else 0,
                message=self._pod_message(pod),
            )
        return list(per_node.values())

    def _calico_node_pods(self) -> list[Any]:
        try:
            result = self._runtime_core_api.list_pod_for_all_namespaces(
                label_selector=_CALICO_NODE_LABEL
            )
        except Exception:
            return []
        return getattr(result, "items", []) or []

    def _namespaces(self) -> list[str]:
        try:
            result = self._runtime_core_api.list_namespace()
        except Exception:
            return []
        items = getattr(result, "items", None)
        if not isinstance(items, list):
            return []
        namespaces: list[str] = []
        for item in items:
            name = getattr(getattr(item, "metadata", None), "name", None)
            if name:
                namespaces.append(str(name))
        return namespaces

    @staticmethod
    def _pod_ready_status(pod: Any) -> str:
        for cond in getattr(pod.status, "conditions", []) or []:
            if getattr(cond, "type", "") == "Ready":
                return getattr(cond, "status", "") or ""
        return ""

    @staticmethod
    def _pod_message(pod: Any) -> str | None:
        for container in getattr(pod.status, "container_statuses", []) or []:
            state = getattr(container, "state", None)
            if state is None:
                continue
            waiting = getattr(state, "waiting", None)
            if waiting is not None:
                message = getattr(waiting, "message", None)
                if message:
                    return str(message)
            terminated = getattr(state, "terminated", None)
            if terminated is not None:
                message = getattr(terminated, "message", None)
                if message:
                    return str(message)
        return None

    # ── Parsers ───────────────────────────────────────────────────────────
    @staticmethod
    def _parse_ip_pool(item: dict[str, Any]) -> CalicoIPPool:
        meta = item.get("metadata") or {}
        spec = item.get("spec") or {}
        return CalicoIPPool(
            name=str(meta.get("name", "")),
            cidr=str(spec.get("cidr", "")),
            ipip_mode=str(spec.get("ipipMode", "Never")),
            vxlan_mode=str(spec.get("vxlanMode", "Never")),
            disabled=bool(spec.get("disabled", False)),
            nat_outgoing=bool(spec.get("natOutgoing", False)),
            node_selector=str(spec.get("nodeSelector", "")),
        )

    @staticmethod
    def _parse_host_endpoint(item: dict[str, Any]) -> CalicoHostEndpoint:
        meta = item.get("metadata") or {}
        spec = item.get("spec") or {}
        expected_ips_raw = spec.get("expectedIPs")
        expected_ips = (
            tuple(str(ip) for ip in expected_ips_raw) if isinstance(expected_ips_raw, list) else ()
        )
        expected_ip = expected_ips[0] if expected_ips else ""
        labels = CalicoK8sAdapter._parse_labels(spec.get("labels"))
        profiles = spec.get("profiles")
        applied_policies = (
            tuple(str(profile) for profile in profiles) if isinstance(profiles, list) else ()
        )
        return CalicoHostEndpoint(
            name=str(meta.get("name", "")),
            node=str(spec.get("node", "")),
            interface_name=str(spec.get("interfaceName", "")),
            expected_ip=expected_ip,
            expected_ips=expected_ips,
            labels=labels,
            applied_policies=applied_policies,
        )

    @staticmethod
    def _parse_bgp_configuration(item: dict[str, Any]) -> CalicoBgpConfiguration:
        meta = item.get("metadata") or {}
        spec = item.get("spec") or {}
        mesh_raw = spec.get("nodeToNodeMeshEnabled")
        mesh = spec.get("nodeToNodeMesh")
        if mesh_raw is None and isinstance(mesh, dict):
            mesh_raw = mesh.get("enabled")
        mesh_enabled = bool(mesh_raw) if mesh_raw is not None else None
        ips = spec.get("serviceClusterIPs")
        as_number = spec.get("asNumber")
        return CalicoBgpConfiguration(
            name=str(meta.get("name", "")),
            as_number=str(as_number) if as_number is not None else None,
            node_to_node_mesh_enabled=mesh_enabled,
            service_cluster_ips=tuple(str(ip) for ip in ips) if isinstance(ips, list) else (),
        )

    @staticmethod
    def _parse_bgp_peer(item: dict[str, Any]) -> CalicoBgpPeer:
        meta = item.get("metadata") or {}
        spec = item.get("spec") or {}
        as_number = spec.get("asNumber")
        return CalicoBgpPeer(
            name=str(meta.get("name", "")),
            peer_ip=str(spec.get("peerIP", "")),
            as_number=str(as_number) if as_number is not None else None,
            node_selector=str(spec.get("nodeSelector", "")),
        )

    @staticmethod
    def _parse_labels(raw: object) -> tuple[tuple[str, str], ...]:
        if not isinstance(raw, dict):
            return ()
        return tuple((str(key), str(value)) for key, value in raw.items())


def raw_items(raw: dict[str, Any] | None) -> list[dict[str, Any]]:
    """Extract the ``items`` list from a CRD list payload, tolerating junk."""
    if not isinstance(raw, dict):
        return []
    items = raw.get("items")
    return [item for item in items if isinstance(item, dict)] if isinstance(items, list) else []
