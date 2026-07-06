from __future__ import annotations

from typing import Any

from hexawyn.application.ports.driven.external_exposure_audit_port import (
    ExternalExposureAuditPort,
    ServiceRaw,
)
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError

_K8S_FORBIDDEN = 403


class KubernetesExternalExposureAdapter(ExternalExposureAuditPort):
    """Secondary adapter — enumerates every Service across all namespaces via
    the K8s API and maps each to a ServiceRaw TypedDict. The LoadBalancer /
    NodePort type filter is applied in the application service, keeping that
    decision testable in the domain layer."""

    def list_external_services(self) -> list[ServiceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_service_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_service_raw(item) for item in result.items]


def _to_service_raw(item: Any) -> ServiceRaw:
    metadata = item.metadata
    spec = item.spec
    status = item.status

    ports: list[int] = []
    node_port: int | None = None
    for port in spec.ports or []:
        ports.append(port.port)
        if node_port is None and port.node_port is not None:
            node_port = port.node_port

    external_ip: str | None = None
    external_hostname: str | None = None
    lb_status = status.load_balancer if status else None
    if lb_status:
        ingresses = lb_status.ingress or []
        for ingress in ingresses:
            if external_ip is None and ingress.ip:
                external_ip = ingress.ip
            if external_hostname is None and ingress.hostname:
                external_hostname = ingress.hostname

    has_source_ranges = bool(spec.load_balancer_source_ranges)

    annotations: dict[str, str] = {}
    if metadata.annotations:
        annotations = dict(metadata.annotations)

    return ServiceRaw(
        name=metadata.name,
        namespace=metadata.namespace,
        service_type=spec.type or "ClusterIP",
        ports=ports,
        node_port=node_port,
        external_ip=external_ip,
        external_hostname=external_hostname,
        has_source_ranges=has_source_ranges,
        annotations=annotations,
    )


def _translate_error(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list Services")
    return ClusterUnreachableError(f"Cannot list Services: {exc}")
