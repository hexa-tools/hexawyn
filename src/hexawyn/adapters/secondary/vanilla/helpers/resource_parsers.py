from __future__ import annotations

from hexawyn.application.ports.driven.cost_forecast_port import DailyCostData, NamespaceCostData
from hexawyn.application.ports.driven.probe_audit_port import ProbeContainerRawData

_CPU_MILLI_FACTOR = 1000.0
_NANOCORES_FACTOR = 1_000_000_000.0
_MEM_GIB_FACTOR = 1024**3
_BYTES_TO_MI = 1024.0 * 1024.0
_CPU_COST_PER_CORE_DAY = 21.6 / 30.0
_MEM_COST_PER_GIB_DAY = 2.88 / 30.0


def _compute_pod_resources(containers: list[object]) -> tuple[float, float]:
    cpu_total = 0.0
    mem_total_gb = 0.0
    for container in containers:
        resources = getattr(container, "resources", None)
        requests = getattr(resources, "requests", {}) if resources else {}
        if isinstance(requests, dict):
            cpu_raw = requests.get("cpu")
            mem_raw = requests.get("memory")
            if cpu_raw is not None:
                cpu_total += _parse_cpu(str(cpu_raw))
            if mem_raw is not None:
                mem_total_gb += _parse_memory(str(mem_raw))
    return cpu_total, mem_total_gb


def _compute_namespace_daily_costs(deployments: list[object]) -> dict[str, float]:
    ns_costs: dict[str, float] = {}
    for dep in deployments:
        meta = getattr(dep, "metadata", None)
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_cores, mem_mi = _workload_resource_requests(dep)
        mem_gib = mem_mi / 1024.0
        daily = cpu_cores * _CPU_COST_PER_CORE_DAY + mem_gib * _MEM_COST_PER_GIB_DAY
        ns_costs[namespace] = ns_costs.get(namespace, 0.0) + daily
    return ns_costs


def _build_daily_cost_entries(
    ns_costs: dict[str, float],
    total_daily: float,
    days: int,
) -> list[DailyCostData]:
    from datetime import date, timedelta

    today = date.today()
    ns_list: list[NamespaceCostData] = [
        NamespaceCostData(name=ns, cost_usd=round(cost, 4))
        for ns, cost in sorted(ns_costs.items(), key=lambda x: x[1], reverse=True)
    ]
    return [
        DailyCostData(
            date=(today - timedelta(days=days - 1 - i)).strftime("%Y-%m-%d"),
            total_usd=round(total_daily, 4),
            namespace_costs=ns_list,
        )
        for i in range(days)
    ]


def _workload_resource_requests(workload: object) -> tuple[float, float]:
    spec = getattr(workload, "spec", None)
    template = getattr(spec, "template", None) if spec else None
    pod_spec = getattr(template, "spec", None) if template else None
    containers = list(getattr(pod_spec, "containers", None) or []) if pod_spec else []
    cpu_total = 0.0
    mem_total_mi = 0.0
    for container in containers:
        cpu = _container_request(container, "cpu")
        mem_gib = _container_request(container, "memory")
        if cpu is not None:
            cpu_total += cpu
        if mem_gib is not None:
            mem_total_mi += mem_gib * 1024.0
    return cpu_total, mem_total_mi


def _sum_container_metrics(containers: object) -> tuple[float, float]:
    if not isinstance(containers, list):
        return 0.0, 0.0
    cpu_total = 0.0
    mem_total_mi = 0.0
    for container in containers:
        if not isinstance(container, dict):
            continue
        usage = container.get("usage", {})
        if not isinstance(usage, dict):
            continue
        cpu_raw = str(usage.get("cpu", "0"))
        mem_raw = str(usage.get("memory", "0"))
        cpu_total += _parse_nanocores(cpu_raw)
        mem_total_mi += _parse_memory_to_mi(mem_raw)
    return cpu_total, mem_total_mi


def _parse_nanocores(value: str) -> float:
    if value.endswith("n"):
        return float(value[:-1]) / _NANOCORES_FACTOR
    if value.endswith("m"):
        return float(value[:-1]) / _CPU_MILLI_FACTOR
    return float(value)


def _parse_memory_to_mi(value: str) -> float:
    for suffix, factor in (
        ("Ki", 1.0 / 1024.0),
        ("Mi", 1.0),
        ("Gi", 1024.0),
        ("Ti", 1024.0 * 1024.0),
        ("K", 1000.0 / (1024.0 * 1024.0)),
        ("M", 1000.0 * 1000.0 / (1024.0 * 1024.0)),
        ("G", 1000.0 * 1000.0 * 1000.0 / (1024.0 * 1024.0)),
    ):
        if value.endswith(suffix):
            return float(value[: -len(suffix)]) * factor
    return float(value) / _BYTES_TO_MI


def _workload_key_from_pod_name(pod_name: str, namespace: str) -> str | None:
    parts = pod_name.rsplit("-", 2)
    if len(parts) >= 3:  # noqa: PLR2004
        workload_name = parts[0]
        return f"{namespace}/{workload_name}"
    if len(parts) == 2:  # noqa: PLR2004
        return f"{namespace}/{parts[0]}"
    return None


def _pod_namespace(pod: object) -> str:
    meta = getattr(pod, "metadata", None)
    return str(getattr(meta, "namespace", "") or "") if meta else ""


def _pod_containers(pod: object) -> list[object]:
    spec = getattr(pod, "spec", None)
    if spec is None:
        return []
    return list(getattr(spec, "containers", None) or [])


def _container_request(container: object, resource: str) -> float | None:
    resources = getattr(container, "resources", None)
    if resources is None:
        return None
    requests = getattr(resources, "requests", None)
    if not isinstance(requests, dict) or resource not in requests:
        return None
    raw = requests[resource]
    if resource == "cpu":
        return _parse_cpu(str(raw))
    if resource == "memory":
        return _parse_memory(str(raw))
    return None


def _parse_cpu(value: str) -> float:
    if value.endswith("m"):
        return float(value[:-1]) / _CPU_MILLI_FACTOR
    return float(value)


def _parse_memory(value: str) -> float:
    for suffix, factor in (
        ("Gi", 1.0),
        ("Mi", 1.0 / 1024),
        ("Ki", 1.0 / (1024**2)),
        ("G", 1.0 / 1.073741824),
        ("M", 1.0 / (1.073741824 * 1024)),
        ("K", 1.0 / (1.073741824 * 1024**2)),
    ):
        if value.endswith(suffix):
            return float(value[: -len(suffix)]) * factor
    return float(value) / _MEM_GIB_FACTOR


def _parse_prometheus_vector(payload: dict[str, object]) -> dict[str, float]:
    result: dict[str, float] = {}
    data = payload.get("data") if isinstance(payload, dict) else None
    if not isinstance(data, dict):
        return result
    result_list = data.get("result")
    if not isinstance(result_list, list):
        return result
    for entry in result_list:
        if not isinstance(entry, dict):
            continue
        metric = entry.get("metric")
        value_pair = entry.get("value")
        if not isinstance(metric, dict) or not isinstance(value_pair, list):
            continue
        namespace = metric.get("namespace")
        if not isinstance(namespace, str) or len(value_pair) < 2:  # noqa: PLR2004
            continue
        try:
            result[namespace] = float(str(value_pair[1]))
        except (ValueError, TypeError):
            continue
    return result


def _parse_prometheus_pod_vector(payload: dict[str, object]) -> dict[str, float]:
    result: dict[str, float] = {}
    data = payload.get("data") if isinstance(payload, dict) else None
    if not isinstance(data, dict):
        return result
    result_list = data.get("result")
    if not isinstance(result_list, list):
        return result
    for entry in result_list:
        if not isinstance(entry, dict):
            continue
        metric = entry.get("metric")
        value_pair = entry.get("value")
        if not isinstance(metric, dict) or not isinstance(value_pair, list) or len(value_pair) < 2:  # noqa: PLR2004
            continue
        pod = metric.get("pod")
        namespace = metric.get("namespace")
        if not isinstance(pod, str) or not isinstance(namespace, str):
            continue
        try:
            result[f"{namespace}/{pod}"] = float(str(value_pair[1]))
        except (ValueError, TypeError):
            continue
    return result


def _pod_requests_and_limits(
    containers: list[object],
) -> tuple[float | None, float | None, float | None, float | None]:
    cpu_req: float | None = None
    mem_req_mi: float | None = None
    cpu_lim: float | None = None
    mem_lim_mi: float | None = None
    for container in containers:
        resources = getattr(container, "resources", None)
        if resources is None:
            continue
        requests = getattr(resources, "requests", None)
        limits = getattr(resources, "limits", None)
        if isinstance(requests, dict):
            if "cpu" in requests:
                cpu_req = (cpu_req or 0.0) + _parse_cpu(str(requests["cpu"]))
            if "memory" in requests:
                mem_req_mi = (mem_req_mi or 0.0) + _parse_memory(str(requests["memory"])) * 1024.0
        if isinstance(limits, dict):
            if "cpu" in limits:
                cpu_lim = (cpu_lim or 0.0) + _parse_cpu(str(limits["cpu"]))
            if "memory" in limits:
                mem_lim_mi = (mem_lim_mi or 0.0) + _parse_memory(str(limits["memory"])) * 1024.0
    return cpu_req, mem_req_mi, cpu_lim, mem_lim_mi


def _deployment_key_from_pod(pod_name: str, namespace: str) -> str | None:
    parts = pod_name.rsplit("-", 2)
    if len(parts) >= 3:  # noqa: PLR2004
        return f"{namespace}/{parts[0]}"
    if len(parts) == 2:  # noqa: PLR2004
        return f"{namespace}/{parts[0]}"
    return None


def _get_workload_type(owner_references: object) -> str:
    if not isinstance(owner_references, list):
        return "Deployment"
    for ref in owner_references:
        if not isinstance(ref, object) or not hasattr(ref, "kind"):
            continue
        kind = str(getattr(ref, "kind", ""))
        if kind in ("StatefulSet", "DaemonSet", "Job", "CronJob"):
            return kind
    return "Deployment"


def _extract_container_data(container: object) -> ProbeContainerRawData:
    name = str(getattr(container, "name", ""))
    ports = getattr(container, "ports", None)
    exposed_ports: list[int] = []
    if isinstance(ports, list):
        for port in ports:
            container_port = getattr(port, "container_port", None)
            if container_port is not None:
                exposed_ports.append(int(container_port))
    liveness = getattr(container, "liveness_probe", None)
    readiness = getattr(container, "readiness_probe", None)
    has_liveness = liveness is not None
    has_readiness = readiness is not None
    liveness_type = str(getattr(liveness, "_exec", None) and "exec" or "")
    if liveness is not None and hasattr(liveness, "http_get") and liveness.http_get:
        liveness_type = "httpGet"
    elif liveness is not None and hasattr(liveness, "tcp_socket") and liveness.tcp_socket:
        liveness_type = "tcpSocket"
    readiness_type = str(getattr(readiness, "_exec", None) and "exec" or "")
    if readiness is not None and hasattr(readiness, "http_get") and readiness.http_get:
        readiness_type = "httpGet"
    elif readiness is not None and hasattr(readiness, "tcp_socket") and readiness.tcp_socket:
        readiness_type = "tcpSocket"
    liveness_http_path = str(
        getattr(getattr(liveness, "http_get", None), "path", "") if liveness else ""
    )
    readiness_http_path = str(
        getattr(getattr(readiness, "http_get", None), "path", "") if readiness else ""
    )
    liveness_port = (
        int(
            getattr(getattr(liveness, "http_get", None), "port", 0)
            or getattr(getattr(liveness, "tcp_socket", None), "port", 0)
            or 0
        )
        if liveness
        else 0
    )
    readiness_port = (
        int(
            getattr(getattr(readiness, "http_get", None), "port", 0)
            or getattr(getattr(readiness, "tcp_socket", None), "port", 0)
            or 0
        )
        if readiness
        else 0
    )
    return ProbeContainerRawData(
        container_name=name,
        is_init_container=False,
        exposed_ports=exposed_ports,
        has_liveness_probe=has_liveness,
        has_readiness_probe=has_readiness,
        liveness_probe_type=liveness_type,
        readiness_probe_type=readiness_type,
        liveness_http_path=liveness_http_path,
        readiness_http_path=readiness_http_path,
        liveness_port=liveness_port,
        readiness_port=readiness_port,
    )


def _extract_init_container_data(container: object) -> ProbeContainerRawData:
    name = str(getattr(container, "name", ""))
    ports = getattr(container, "ports", None)
    exposed_ports: list[int] = []
    if isinstance(ports, list):
        for port in ports:
            container_port = getattr(port, "container_port", None)
            if container_port is not None:
                exposed_ports.append(int(container_port))
    liveness = getattr(container, "liveness_probe", None)
    readiness = getattr(container, "readiness_probe", None)
    has_liveness = liveness is not None
    has_readiness = readiness is not None
    liveness_type = str(getattr(liveness, "_exec", None) and "exec" or "")
    if liveness is not None and hasattr(liveness, "http_get") and liveness.http_get:
        liveness_type = "httpGet"
    elif liveness is not None and hasattr(liveness, "tcp_socket") and liveness.tcp_socket:
        liveness_type = "tcpSocket"
    readiness_type = str(getattr(readiness, "_exec", None) and "exec" or "")
    if readiness is not None and hasattr(readiness, "http_get") and readiness.http_get:
        readiness_type = "httpGet"
    elif readiness is not None and hasattr(readiness, "tcp_socket") and readiness.tcp_socket:
        readiness_type = "tcpSocket"
    liveness_http_path = str(
        getattr(getattr(liveness, "http_get", None), "path", "") if liveness else ""
    )
    readiness_http_path = str(
        getattr(getattr(readiness, "http_get", None), "path", "") if readiness else ""
    )
    liveness_port = (
        int(
            getattr(getattr(liveness, "http_get", None), "port", 0)
            or getattr(getattr(liveness, "tcp_socket", None), "port", 0)
            or 0
        )
        if liveness
        else 0
    )
    readiness_port = (
        int(
            getattr(getattr(readiness, "http_get", None), "port", 0)
            or getattr(getattr(readiness, "tcp_socket", None), "port", 0)
            or 0
        )
        if readiness
        else 0
    )
    return ProbeContainerRawData(
        container_name=name,
        is_init_container=True,
        exposed_ports=exposed_ports,
        has_liveness_probe=has_liveness,
        has_readiness_probe=has_readiness,
        liveness_probe_type=liveness_type,
        readiness_probe_type=readiness_type,
        liveness_http_path=liveness_http_path,
        readiness_http_path=readiness_http_path,
        liveness_port=liveness_port,
        readiness_port=readiness_port,
    )
