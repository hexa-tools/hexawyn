from __future__ import annotations

from collections.abc import Sequence
from typing import cast

from kubernetes import client

from hexawyn.adapters.secondary.vanilla.helpers.k8s_client import (
    KubernetesAppsApi,
    KubernetesCoreApi,
)
from hexawyn.adapters.secondary.vanilla.helpers.resource_parsers import (
    _deployment_key_from_pod,
    _extract_container_data,
    _extract_init_container_data,
    _get_workload_type,
)
from hexawyn.application.ports.driven.probe_audit_port import (
    ProbeAuditPort,
    ProbeContainerRawData,
    ProbeDeploymentRawData,
)
from hexawyn.application.ports.driven.what_if_simulation_port import (
    DependentServiceData,
    HPAData,
    PDBData,
    WhatIfSimulationPort,
)
from hexawyn.domain.errors import ClusterUnreachableError

_K8S_TIMEOUT = 10
_PROMETHEUS_QUERY_TIMEOUT = 15.0


def _items_from(item_list: object) -> list[object]:
    items = getattr(item_list, "items", [])
    return _object_sequence(items)


def _object_sequence(value: object) -> list[object]:
    if isinstance(value, Sequence) and not isinstance(value, str | bytes):
        return list(cast(Sequence[object], value))
    return []


class VanillaWhatIfSimulationAdapter(WhatIfSimulationPort, ProbeAuditPort):
    def __init__(
        self,
        api: KubernetesCoreApi,
        apps_api: KubernetesAppsApi,
        prometheus_url: str = "",
    ) -> None:
        self._api = api
        self._apps_api = apps_api
        self._prometheus_url = prometheus_url

    def get_current_replicas(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def get_current_cpu_utilization(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 0.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
            data = resp.json()
            results = data.get("data", {}).get("result", [])
            if results and isinstance(results, list):
                value = results[0].get("value", [None, "0"])
                if len(value) >= 2:  # noqa: PLR2004
                    return float(value[1])
        except Exception:
            pass
        return 0.0

    def get_pdb_info(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def get_hpa_info(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def get_service_topology(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[DependentServiceData]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                deps: list[DependentServiceData] = []
                for pod in pods.items:  # type: ignore
                    if pod.metadata:
                        deps.append(
                            DependentServiceData(  # type: ignore
                                name=pod.metadata.name or "",
                                namespace=namespace,
                                status=pod.status.phase or "Unknown",
                            )
                        )
                result[svc_name] = deps
            return result
        except Exception:
            return {}

    def get_dependency_graph(self, namespace: str) -> dict[str, list[str]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[str]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                pod_names = []
                for p in _items_from(pods):
                    meta = getattr(p, "metadata", None)
                    name = getattr(meta, "name", None) if meta else None
                    if name:
                        pod_names.append(name)
                result[svc_name] = pod_names
            return result
        except Exception:
            return {}

    def get_probe_audit_data(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result
