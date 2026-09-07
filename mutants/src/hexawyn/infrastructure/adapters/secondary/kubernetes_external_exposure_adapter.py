from __future__ import annotations

from typing import Any

from hexawyn.application.ports.driven.external_exposure_audit_port import (
    ExternalExposureAuditPort,
    ServiceRaw,
)
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError

_K8S_FORBIDDEN = 403


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁKubernetesExternalExposureAdapterǁlist_external_services__mutmut: MutantDict = {}  # type: ignore


class KubernetesExternalExposureAdapter(ExternalExposureAuditPort):
    """Secondary adapter — enumerates every Service across all namespaces via
    the K8s API and maps each to a ServiceRaw TypedDict. The LoadBalancer /
    NodePort type filter is applied in the application service, keeping that
    decision testable in the domain layer."""

    @_mutmut_mutated(mutants_xǁKubernetesExternalExposureAdapterǁlist_external_services__mutmut)
    def list_external_services(self) -> list[ServiceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_service_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_service_raw(item) for item in result.items]

    def xǁKubernetesExternalExposureAdapterǁlist_external_services__mutmut_orig(self) -> list[ServiceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_service_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_service_raw(item) for item in result.items]

    def xǁKubernetesExternalExposureAdapterǁlist_external_services__mutmut_1(self) -> list[ServiceRaw]:
        from kubernetes import client as k8s

        core_api = None
        try:
            result = core_api.list_service_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_service_raw(item) for item in result.items]

    def xǁKubernetesExternalExposureAdapterǁlist_external_services__mutmut_2(self) -> list[ServiceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = None
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_service_raw(item) for item in result.items]

    def xǁKubernetesExternalExposureAdapterǁlist_external_services__mutmut_3(self) -> list[ServiceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_service_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(None) from exc

        return [_to_service_raw(item) for item in result.items]

    def xǁKubernetesExternalExposureAdapterǁlist_external_services__mutmut_4(self) -> list[ServiceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_service_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        return [_to_service_raw(None) for item in result.items]

mutants_xǁKubernetesExternalExposureAdapterǁlist_external_services__mutmut['_mutmut_orig'] = KubernetesExternalExposureAdapter.xǁKubernetesExternalExposureAdapterǁlist_external_services__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesExternalExposureAdapterǁlist_external_services__mutmut['xǁKubernetesExternalExposureAdapterǁlist_external_services__mutmut_1'] = KubernetesExternalExposureAdapter.xǁKubernetesExternalExposureAdapterǁlist_external_services__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesExternalExposureAdapterǁlist_external_services__mutmut['xǁKubernetesExternalExposureAdapterǁlist_external_services__mutmut_2'] = KubernetesExternalExposureAdapter.xǁKubernetesExternalExposureAdapterǁlist_external_services__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesExternalExposureAdapterǁlist_external_services__mutmut['xǁKubernetesExternalExposureAdapterǁlist_external_services__mutmut_3'] = KubernetesExternalExposureAdapter.xǁKubernetesExternalExposureAdapterǁlist_external_services__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesExternalExposureAdapterǁlist_external_services__mutmut['xǁKubernetesExternalExposureAdapterǁlist_external_services__mutmut_4'] = KubernetesExternalExposureAdapter.xǁKubernetesExternalExposureAdapterǁlist_external_services__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_service_raw__mutmut)
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


def x__to_service_raw__mutmut_orig(item: Any) -> ServiceRaw:
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


def x__to_service_raw__mutmut_1(item: Any) -> ServiceRaw:
    metadata = None
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


def x__to_service_raw__mutmut_2(item: Any) -> ServiceRaw:
    metadata = item.metadata
    spec = None
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


def x__to_service_raw__mutmut_3(item: Any) -> ServiceRaw:
    metadata = item.metadata
    spec = item.spec
    status = None

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


def x__to_service_raw__mutmut_4(item: Any) -> ServiceRaw:
    metadata = item.metadata
    spec = item.spec
    status = item.status

    ports: list[int] = None
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


def x__to_service_raw__mutmut_5(item: Any) -> ServiceRaw:
    metadata = item.metadata
    spec = item.spec
    status = item.status

    ports: list[int] = []
    node_port: int | None = ""
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


def x__to_service_raw__mutmut_6(item: Any) -> ServiceRaw:
    metadata = item.metadata
    spec = item.spec
    status = item.status

    ports: list[int] = []
    node_port: int | None = None
    for port in spec.ports and []:
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


def x__to_service_raw__mutmut_7(item: Any) -> ServiceRaw:
    metadata = item.metadata
    spec = item.spec
    status = item.status

    ports: list[int] = []
    node_port: int | None = None
    for port in spec.ports or []:
        ports.append(None)
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


def x__to_service_raw__mutmut_8(item: Any) -> ServiceRaw:
    metadata = item.metadata
    spec = item.spec
    status = item.status

    ports: list[int] = []
    node_port: int | None = None
    for port in spec.ports or []:
        ports.append(port.port)
        if node_port is None or port.node_port is not None:
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


def x__to_service_raw__mutmut_9(item: Any) -> ServiceRaw:
    metadata = item.metadata
    spec = item.spec
    status = item.status

    ports: list[int] = []
    node_port: int | None = None
    for port in spec.ports or []:
        ports.append(port.port)
        if node_port is not None and port.node_port is not None:
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


def x__to_service_raw__mutmut_10(item: Any) -> ServiceRaw:
    metadata = item.metadata
    spec = item.spec
    status = item.status

    ports: list[int] = []
    node_port: int | None = None
    for port in spec.ports or []:
        ports.append(port.port)
        if node_port is None and port.node_port is None:
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


def x__to_service_raw__mutmut_11(item: Any) -> ServiceRaw:
    metadata = item.metadata
    spec = item.spec
    status = item.status

    ports: list[int] = []
    node_port: int | None = None
    for port in spec.ports or []:
        ports.append(port.port)
        if node_port is None and port.node_port is not None:
            node_port = None

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


def x__to_service_raw__mutmut_12(item: Any) -> ServiceRaw:
    metadata = item.metadata
    spec = item.spec
    status = item.status

    ports: list[int] = []
    node_port: int | None = None
    for port in spec.ports or []:
        ports.append(port.port)
        if node_port is None and port.node_port is not None:
            node_port = port.node_port

    external_ip: str | None = ""
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


def x__to_service_raw__mutmut_13(item: Any) -> ServiceRaw:
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
    external_hostname: str | None = ""
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


def x__to_service_raw__mutmut_14(item: Any) -> ServiceRaw:
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
    lb_status = None
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


def x__to_service_raw__mutmut_15(item: Any) -> ServiceRaw:
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
        ingresses = None
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


def x__to_service_raw__mutmut_16(item: Any) -> ServiceRaw:
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
        ingresses = lb_status.ingress and []
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


def x__to_service_raw__mutmut_17(item: Any) -> ServiceRaw:
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
            if external_ip is None or ingress.ip:
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


def x__to_service_raw__mutmut_18(item: Any) -> ServiceRaw:
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
            if external_ip is not None and ingress.ip:
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


def x__to_service_raw__mutmut_19(item: Any) -> ServiceRaw:
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
                external_ip = None
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


def x__to_service_raw__mutmut_20(item: Any) -> ServiceRaw:
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
            if external_hostname is None or ingress.hostname:
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


def x__to_service_raw__mutmut_21(item: Any) -> ServiceRaw:
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
            if external_hostname is not None and ingress.hostname:
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


def x__to_service_raw__mutmut_22(item: Any) -> ServiceRaw:
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
                external_hostname = None

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


def x__to_service_raw__mutmut_23(item: Any) -> ServiceRaw:
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

    has_source_ranges = None

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


def x__to_service_raw__mutmut_24(item: Any) -> ServiceRaw:
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

    has_source_ranges = bool(None)

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


def x__to_service_raw__mutmut_25(item: Any) -> ServiceRaw:
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

    annotations: dict[str, str] = None
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


def x__to_service_raw__mutmut_26(item: Any) -> ServiceRaw:
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
        annotations = None

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


def x__to_service_raw__mutmut_27(item: Any) -> ServiceRaw:
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
        annotations = dict(None)

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


def x__to_service_raw__mutmut_28(item: Any) -> ServiceRaw:
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
        name=None,
        namespace=metadata.namespace,
        service_type=spec.type or "ClusterIP",
        ports=ports,
        node_port=node_port,
        external_ip=external_ip,
        external_hostname=external_hostname,
        has_source_ranges=has_source_ranges,
        annotations=annotations,
    )


def x__to_service_raw__mutmut_29(item: Any) -> ServiceRaw:
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
        namespace=None,
        service_type=spec.type or "ClusterIP",
        ports=ports,
        node_port=node_port,
        external_ip=external_ip,
        external_hostname=external_hostname,
        has_source_ranges=has_source_ranges,
        annotations=annotations,
    )


def x__to_service_raw__mutmut_30(item: Any) -> ServiceRaw:
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
        service_type=None,
        ports=ports,
        node_port=node_port,
        external_ip=external_ip,
        external_hostname=external_hostname,
        has_source_ranges=has_source_ranges,
        annotations=annotations,
    )


def x__to_service_raw__mutmut_31(item: Any) -> ServiceRaw:
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
        ports=None,
        node_port=node_port,
        external_ip=external_ip,
        external_hostname=external_hostname,
        has_source_ranges=has_source_ranges,
        annotations=annotations,
    )


def x__to_service_raw__mutmut_32(item: Any) -> ServiceRaw:
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
        node_port=None,
        external_ip=external_ip,
        external_hostname=external_hostname,
        has_source_ranges=has_source_ranges,
        annotations=annotations,
    )


def x__to_service_raw__mutmut_33(item: Any) -> ServiceRaw:
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
        external_ip=None,
        external_hostname=external_hostname,
        has_source_ranges=has_source_ranges,
        annotations=annotations,
    )


def x__to_service_raw__mutmut_34(item: Any) -> ServiceRaw:
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
        external_hostname=None,
        has_source_ranges=has_source_ranges,
        annotations=annotations,
    )


def x__to_service_raw__mutmut_35(item: Any) -> ServiceRaw:
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
        has_source_ranges=None,
        annotations=annotations,
    )


def x__to_service_raw__mutmut_36(item: Any) -> ServiceRaw:
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
        annotations=None,
    )


def x__to_service_raw__mutmut_37(item: Any) -> ServiceRaw:
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
        namespace=metadata.namespace,
        service_type=spec.type or "ClusterIP",
        ports=ports,
        node_port=node_port,
        external_ip=external_ip,
        external_hostname=external_hostname,
        has_source_ranges=has_source_ranges,
        annotations=annotations,
    )


def x__to_service_raw__mutmut_38(item: Any) -> ServiceRaw:
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
        service_type=spec.type or "ClusterIP",
        ports=ports,
        node_port=node_port,
        external_ip=external_ip,
        external_hostname=external_hostname,
        has_source_ranges=has_source_ranges,
        annotations=annotations,
    )


def x__to_service_raw__mutmut_39(item: Any) -> ServiceRaw:
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
        ports=ports,
        node_port=node_port,
        external_ip=external_ip,
        external_hostname=external_hostname,
        has_source_ranges=has_source_ranges,
        annotations=annotations,
    )


def x__to_service_raw__mutmut_40(item: Any) -> ServiceRaw:
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
        node_port=node_port,
        external_ip=external_ip,
        external_hostname=external_hostname,
        has_source_ranges=has_source_ranges,
        annotations=annotations,
    )


def x__to_service_raw__mutmut_41(item: Any) -> ServiceRaw:
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
        external_ip=external_ip,
        external_hostname=external_hostname,
        has_source_ranges=has_source_ranges,
        annotations=annotations,
    )


def x__to_service_raw__mutmut_42(item: Any) -> ServiceRaw:
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
        external_hostname=external_hostname,
        has_source_ranges=has_source_ranges,
        annotations=annotations,
    )


def x__to_service_raw__mutmut_43(item: Any) -> ServiceRaw:
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
        has_source_ranges=has_source_ranges,
        annotations=annotations,
    )


def x__to_service_raw__mutmut_44(item: Any) -> ServiceRaw:
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
        annotations=annotations,
    )


def x__to_service_raw__mutmut_45(item: Any) -> ServiceRaw:
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
        )


def x__to_service_raw__mutmut_46(item: Any) -> ServiceRaw:
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
        service_type=spec.type and "ClusterIP",
        ports=ports,
        node_port=node_port,
        external_ip=external_ip,
        external_hostname=external_hostname,
        has_source_ranges=has_source_ranges,
        annotations=annotations,
    )


def x__to_service_raw__mutmut_47(item: Any) -> ServiceRaw:
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
        service_type=spec.type or "XXClusterIPXX",
        ports=ports,
        node_port=node_port,
        external_ip=external_ip,
        external_hostname=external_hostname,
        has_source_ranges=has_source_ranges,
        annotations=annotations,
    )


def x__to_service_raw__mutmut_48(item: Any) -> ServiceRaw:
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
        service_type=spec.type or "clusterip",
        ports=ports,
        node_port=node_port,
        external_ip=external_ip,
        external_hostname=external_hostname,
        has_source_ranges=has_source_ranges,
        annotations=annotations,
    )


def x__to_service_raw__mutmut_49(item: Any) -> ServiceRaw:
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
        service_type=spec.type or "CLUSTERIP",
        ports=ports,
        node_port=node_port,
        external_ip=external_ip,
        external_hostname=external_hostname,
        has_source_ranges=has_source_ranges,
        annotations=annotations,
    )

mutants_x__to_service_raw__mutmut['_mutmut_orig'] = x__to_service_raw__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_1'] = x__to_service_raw__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_2'] = x__to_service_raw__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_3'] = x__to_service_raw__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_4'] = x__to_service_raw__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_5'] = x__to_service_raw__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_6'] = x__to_service_raw__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_7'] = x__to_service_raw__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_8'] = x__to_service_raw__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_9'] = x__to_service_raw__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_10'] = x__to_service_raw__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_11'] = x__to_service_raw__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_12'] = x__to_service_raw__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_13'] = x__to_service_raw__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_14'] = x__to_service_raw__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_15'] = x__to_service_raw__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_16'] = x__to_service_raw__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_17'] = x__to_service_raw__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_18'] = x__to_service_raw__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_19'] = x__to_service_raw__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_20'] = x__to_service_raw__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_21'] = x__to_service_raw__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_22'] = x__to_service_raw__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_23'] = x__to_service_raw__mutmut_23 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_24'] = x__to_service_raw__mutmut_24 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_25'] = x__to_service_raw__mutmut_25 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_26'] = x__to_service_raw__mutmut_26 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_27'] = x__to_service_raw__mutmut_27 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_28'] = x__to_service_raw__mutmut_28 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_29'] = x__to_service_raw__mutmut_29 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_30'] = x__to_service_raw__mutmut_30 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_31'] = x__to_service_raw__mutmut_31 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_32'] = x__to_service_raw__mutmut_32 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_33'] = x__to_service_raw__mutmut_33 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_34'] = x__to_service_raw__mutmut_34 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_35'] = x__to_service_raw__mutmut_35 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_36'] = x__to_service_raw__mutmut_36 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_37'] = x__to_service_raw__mutmut_37 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_38'] = x__to_service_raw__mutmut_38 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_39'] = x__to_service_raw__mutmut_39 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_40'] = x__to_service_raw__mutmut_40 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_41'] = x__to_service_raw__mutmut_41 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_42'] = x__to_service_raw__mutmut_42 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_43'] = x__to_service_raw__mutmut_43 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_44'] = x__to_service_raw__mutmut_44 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_45'] = x__to_service_raw__mutmut_45 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_46'] = x__to_service_raw__mutmut_46 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_47'] = x__to_service_raw__mutmut_47 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_48'] = x__to_service_raw__mutmut_48 # type: ignore # mutmut generated
mutants_x__to_service_raw__mutmut['x__to_service_raw__mutmut_49'] = x__to_service_raw__mutmut_49 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__translate_error__mutmut)
def _translate_error(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list Services")
    return ClusterUnreachableError(f"Cannot list Services: {exc}")


def x__translate_error__mutmut_orig(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list Services")
    return ClusterUnreachableError(f"Cannot list Services: {exc}")


def x__translate_error__mutmut_1(exc: Exception) -> Exception:
    status = None
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list Services")
    return ClusterUnreachableError(f"Cannot list Services: {exc}")


def x__translate_error__mutmut_2(exc: Exception) -> Exception:
    status = getattr(None, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list Services")
    return ClusterUnreachableError(f"Cannot list Services: {exc}")


def x__translate_error__mutmut_3(exc: Exception) -> Exception:
    status = getattr(exc, None, None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list Services")
    return ClusterUnreachableError(f"Cannot list Services: {exc}")


def x__translate_error__mutmut_4(exc: Exception) -> Exception:
    status = getattr("status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list Services")
    return ClusterUnreachableError(f"Cannot list Services: {exc}")


def x__translate_error__mutmut_5(exc: Exception) -> Exception:
    status = getattr(exc, None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list Services")
    return ClusterUnreachableError(f"Cannot list Services: {exc}")


def x__translate_error__mutmut_6(exc: Exception) -> Exception:
    status = getattr(exc, "status", )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list Services")
    return ClusterUnreachableError(f"Cannot list Services: {exc}")


def x__translate_error__mutmut_7(exc: Exception) -> Exception:
    status = getattr(exc, "XXstatusXX", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list Services")
    return ClusterUnreachableError(f"Cannot list Services: {exc}")


def x__translate_error__mutmut_8(exc: Exception) -> Exception:
    status = getattr(exc, "STATUS", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list Services")
    return ClusterUnreachableError(f"Cannot list Services: {exc}")


def x__translate_error__mutmut_9(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status != _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list Services")
    return ClusterUnreachableError(f"Cannot list Services: {exc}")


def x__translate_error__mutmut_10(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(None)
    return ClusterUnreachableError(f"Cannot list Services: {exc}")


def x__translate_error__mutmut_11(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("XXRBAC denied access to list ServicesXX")
    return ClusterUnreachableError(f"Cannot list Services: {exc}")


def x__translate_error__mutmut_12(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("rbac denied access to list services")
    return ClusterUnreachableError(f"Cannot list Services: {exc}")


def x__translate_error__mutmut_13(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC DENIED ACCESS TO LIST SERVICES")
    return ClusterUnreachableError(f"Cannot list Services: {exc}")


def x__translate_error__mutmut_14(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to list Services")
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
