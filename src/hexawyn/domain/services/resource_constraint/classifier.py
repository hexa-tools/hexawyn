from __future__ import annotations

from hexawyn.application.ports.driven.pod_resource_metrics_port import ContainerMetricsRecord
from hexawyn.domain.models.resource_constraint import ContainerResourceEntry, RiskLevel

_RISK_ORDER: dict[RiskLevel, int] = {
    RiskLevel.CRITICAL: 0,
    RiskLevel.NO_LIMITS: 1,
    RiskLevel.OK: 2,
}


def sort_key(risk_level: RiskLevel) -> int:
    return _RISK_ORDER.get(risk_level, 99)


def classify_container(
    record: ContainerMetricsRecord,
    cpu_thr: float,
    mem_thr: float,
) -> ContainerResourceEntry:
    cpu_limit = record["cpu_limit_millicores"]
    mem_limit = record["memory_limit_bytes"]

    cpu_unlimited = cpu_limit == 0
    mem_unlimited = mem_limit == 0

    cpu_pct: float | None = None
    if cpu_limit and not cpu_unlimited:
        cpu_pct = record["cpu_usage_millicores"] / cpu_limit * 100

    mem_pct: float | None = None
    if mem_limit and not mem_unlimited:
        mem_pct = record["memory_usage_bytes"] / mem_limit * 100

    tags: list[str] = []
    if record["is_init_container"]:
        tags.append("init_container")
    if cpu_unlimited:
        tags.append("cpu_unlimited")
    if mem_unlimited:
        tags.append("memory_unlimited")

    if cpu_limit is None or mem_limit is None:
        risk_level = RiskLevel.NO_LIMITS
        tags.append("no_limits")
    elif (cpu_pct is not None and cpu_pct > cpu_thr) or (mem_pct is not None and mem_pct > mem_thr):
        risk_level = RiskLevel.CRITICAL
        if cpu_pct is not None and cpu_pct > cpu_thr:
            tags.append("throttled")
        if mem_pct is not None and mem_pct > mem_thr:
            tags.append("oomkill_risk")
    else:
        risk_level = RiskLevel.OK

    return ContainerResourceEntry(
        container_name=record["container_name"],
        pod_name=record["pod_name"],
        namespace=record["namespace"],
        cpu_usage_millicores=record["cpu_usage_millicores"],
        cpu_limit_millicores=cpu_limit,
        memory_usage_bytes=record["memory_usage_bytes"],
        memory_limit_bytes=mem_limit,
        cpu_pct=cpu_pct,
        memory_pct=mem_pct,
        risk_level=risk_level,
        is_init_container=record["is_init_container"],
        tags=tags,
    )
