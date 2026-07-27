from __future__ import annotations

from hexawyn.application.ports.driven.pod_resource_metrics_port import (
    ContainerMetricsRecord,
    PodResourceMetricsPort,
)
from hexawyn.application.use_case.cluster.check_resource_constraints.command import (
    CheckResourceConstraintsCommand,
)
from hexawyn.application.use_case.cluster.check_resource_constraints.response import (
    CheckResourceConstraintsResponse,
)
from hexawyn.application.use_case.cluster.resource_constraint.command import (
    ResourceConstraintCommand,
)
from hexawyn.application.use_case.cluster.resource_constraint.response import (
    ResourceConstraintResponse,
)
from hexawyn.domain.models.resource_constraint import (
    ContainerResourceEntry,
    ResourceConstraintReport,
    RiskLevel,
)

_RISK_ORDER: dict[RiskLevel, int] = {
    RiskLevel.CRITICAL: 0,
    RiskLevel.NO_LIMITS: 1,
    RiskLevel.OK: 2,
}


def _sort_key(risk_level: RiskLevel) -> int:
    return _RISK_ORDER.get(risk_level, 99)


def _classify_container(
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


class ResourceConstraintUseCase:
    def __init__(self, port: PodResourceMetricsPort) -> None:
        self._port = port

    def execute(
        self,
        command: ResourceConstraintCommand,
    ) -> ResourceConstraintResponse:
        from hexawyn.application.use_case.cluster.check_resource_constraints.command import (
            CheckResourceConstraintsCommand,
        )

        # Default to check_resource_constraints with standard params
        result = self.check_resource_constraints(
            CheckResourceConstraintsCommand(),
        )
        return ResourceConstraintResponse(
            namespace=command.namespace or "",
            total_pods=result.report.total_pods_scanned if result.report else 0,
            total_containers=result.report.total_containers if result.report else 0,
            critical_count=result.report.critical_count if result.report else 0,
        )

    def check_resource_constraints(
        self, command: CheckResourceConstraintsCommand
    ) -> CheckResourceConstraintsResponse:
        raw_records = self._port.list_container_resources(namespace=command.namespace)

        entries = [
            _classify_container(r, command.cpu_threshold_pct, command.memory_threshold_pct)
            for r in raw_records
        ]
        entries.sort(key=lambda e: _sort_key(e.risk_level))

        critical_count = sum(1 for e in entries if e.risk_level == RiskLevel.CRITICAL)
        no_limits_count = sum(1 for e in entries if e.risk_level == RiskLevel.NO_LIMITS)
        ok_count = sum(1 for e in entries if e.risk_level == RiskLevel.OK)

        pod_names = {r["pod_name"] for r in raw_records}

        report = ResourceConstraintReport(
            namespace=command.namespace,
            total_pods_scanned=len(pod_names),
            total_containers=len(entries),
            critical_count=critical_count,
            no_limits_count=no_limits_count,
            ok_count=ok_count,
            containers=entries,
        )
        return CheckResourceConstraintsResponse(report=report)
