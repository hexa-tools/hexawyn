from __future__ import annotations

from hexawyn.application.ports.driven.pod_resource_metrics_port import ContainerMetricsRecord
from hexawyn.domain.models.resource_constraint import ContainerResourceEntry, RiskLevel

_RISK_ORDER: dict[RiskLevel, int] = {
    RiskLevel.CRITICAL: 0,
    RiskLevel.NO_LIMITS: 1,
    RiskLevel.OK: 2,
}


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_sort_key__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_sort_key__mutmut)
def sort_key(risk_level: RiskLevel) -> int:
    return _RISK_ORDER.get(risk_level, 99)


def x_sort_key__mutmut_orig(risk_level: RiskLevel) -> int:
    return _RISK_ORDER.get(risk_level, 99)


def x_sort_key__mutmut_1(risk_level: RiskLevel) -> int:
    return _RISK_ORDER.get(None, 99)


def x_sort_key__mutmut_2(risk_level: RiskLevel) -> int:
    return _RISK_ORDER.get(risk_level, None)


def x_sort_key__mutmut_3(risk_level: RiskLevel) -> int:
    return _RISK_ORDER.get(99)


def x_sort_key__mutmut_4(risk_level: RiskLevel) -> int:
    return _RISK_ORDER.get(risk_level, )


def x_sort_key__mutmut_5(risk_level: RiskLevel) -> int:
    return _RISK_ORDER.get(risk_level, 100)

mutants_x_sort_key__mutmut['_mutmut_orig'] = x_sort_key__mutmut_orig # type: ignore # mutmut generated
mutants_x_sort_key__mutmut['x_sort_key__mutmut_1'] = x_sort_key__mutmut_1 # type: ignore # mutmut generated
mutants_x_sort_key__mutmut['x_sort_key__mutmut_2'] = x_sort_key__mutmut_2 # type: ignore # mutmut generated
mutants_x_sort_key__mutmut['x_sort_key__mutmut_3'] = x_sort_key__mutmut_3 # type: ignore # mutmut generated
mutants_x_sort_key__mutmut['x_sort_key__mutmut_4'] = x_sort_key__mutmut_4 # type: ignore # mutmut generated
mutants_x_sort_key__mutmut['x_sort_key__mutmut_5'] = x_sort_key__mutmut_5 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_classify_container__mutmut)
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


def x_classify_container__mutmut_orig(
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


def x_classify_container__mutmut_1(
    record: ContainerMetricsRecord,
    cpu_thr: float,
    mem_thr: float,
) -> ContainerResourceEntry:
    cpu_limit = None
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


def x_classify_container__mutmut_2(
    record: ContainerMetricsRecord,
    cpu_thr: float,
    mem_thr: float,
) -> ContainerResourceEntry:
    cpu_limit = record["XXcpu_limit_millicoresXX"]
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


def x_classify_container__mutmut_3(
    record: ContainerMetricsRecord,
    cpu_thr: float,
    mem_thr: float,
) -> ContainerResourceEntry:
    cpu_limit = record["CPU_LIMIT_MILLICORES"]
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


def x_classify_container__mutmut_4(
    record: ContainerMetricsRecord,
    cpu_thr: float,
    mem_thr: float,
) -> ContainerResourceEntry:
    cpu_limit = record["cpu_limit_millicores"]
    mem_limit = None

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


def x_classify_container__mutmut_5(
    record: ContainerMetricsRecord,
    cpu_thr: float,
    mem_thr: float,
) -> ContainerResourceEntry:
    cpu_limit = record["cpu_limit_millicores"]
    mem_limit = record["XXmemory_limit_bytesXX"]

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


def x_classify_container__mutmut_6(
    record: ContainerMetricsRecord,
    cpu_thr: float,
    mem_thr: float,
) -> ContainerResourceEntry:
    cpu_limit = record["cpu_limit_millicores"]
    mem_limit = record["MEMORY_LIMIT_BYTES"]

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


def x_classify_container__mutmut_7(
    record: ContainerMetricsRecord,
    cpu_thr: float,
    mem_thr: float,
) -> ContainerResourceEntry:
    cpu_limit = record["cpu_limit_millicores"]
    mem_limit = record["memory_limit_bytes"]

    cpu_unlimited = None
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


def x_classify_container__mutmut_8(
    record: ContainerMetricsRecord,
    cpu_thr: float,
    mem_thr: float,
) -> ContainerResourceEntry:
    cpu_limit = record["cpu_limit_millicores"]
    mem_limit = record["memory_limit_bytes"]

    cpu_unlimited = cpu_limit != 0
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


def x_classify_container__mutmut_9(
    record: ContainerMetricsRecord,
    cpu_thr: float,
    mem_thr: float,
) -> ContainerResourceEntry:
    cpu_limit = record["cpu_limit_millicores"]
    mem_limit = record["memory_limit_bytes"]

    cpu_unlimited = cpu_limit == 1
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


def x_classify_container__mutmut_10(
    record: ContainerMetricsRecord,
    cpu_thr: float,
    mem_thr: float,
) -> ContainerResourceEntry:
    cpu_limit = record["cpu_limit_millicores"]
    mem_limit = record["memory_limit_bytes"]

    cpu_unlimited = cpu_limit == 0
    mem_unlimited = None

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


def x_classify_container__mutmut_11(
    record: ContainerMetricsRecord,
    cpu_thr: float,
    mem_thr: float,
) -> ContainerResourceEntry:
    cpu_limit = record["cpu_limit_millicores"]
    mem_limit = record["memory_limit_bytes"]

    cpu_unlimited = cpu_limit == 0
    mem_unlimited = mem_limit != 0

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


def x_classify_container__mutmut_12(
    record: ContainerMetricsRecord,
    cpu_thr: float,
    mem_thr: float,
) -> ContainerResourceEntry:
    cpu_limit = record["cpu_limit_millicores"]
    mem_limit = record["memory_limit_bytes"]

    cpu_unlimited = cpu_limit == 0
    mem_unlimited = mem_limit == 1

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


def x_classify_container__mutmut_13(
    record: ContainerMetricsRecord,
    cpu_thr: float,
    mem_thr: float,
) -> ContainerResourceEntry:
    cpu_limit = record["cpu_limit_millicores"]
    mem_limit = record["memory_limit_bytes"]

    cpu_unlimited = cpu_limit == 0
    mem_unlimited = mem_limit == 0

    cpu_pct: float | None = ""
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


def x_classify_container__mutmut_14(
    record: ContainerMetricsRecord,
    cpu_thr: float,
    mem_thr: float,
) -> ContainerResourceEntry:
    cpu_limit = record["cpu_limit_millicores"]
    mem_limit = record["memory_limit_bytes"]

    cpu_unlimited = cpu_limit == 0
    mem_unlimited = mem_limit == 0

    cpu_pct: float | None = None
    if cpu_limit or not cpu_unlimited:
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


def x_classify_container__mutmut_15(
    record: ContainerMetricsRecord,
    cpu_thr: float,
    mem_thr: float,
) -> ContainerResourceEntry:
    cpu_limit = record["cpu_limit_millicores"]
    mem_limit = record["memory_limit_bytes"]

    cpu_unlimited = cpu_limit == 0
    mem_unlimited = mem_limit == 0

    cpu_pct: float | None = None
    if cpu_limit and cpu_unlimited:
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


def x_classify_container__mutmut_16(
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
        cpu_pct = None

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


def x_classify_container__mutmut_17(
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
        cpu_pct = record["cpu_usage_millicores"] / cpu_limit / 100

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


def x_classify_container__mutmut_18(
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
        cpu_pct = record["cpu_usage_millicores"] * cpu_limit * 100

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


def x_classify_container__mutmut_19(
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
        cpu_pct = record["XXcpu_usage_millicoresXX"] / cpu_limit * 100

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


def x_classify_container__mutmut_20(
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
        cpu_pct = record["CPU_USAGE_MILLICORES"] / cpu_limit * 100

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


def x_classify_container__mutmut_21(
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
        cpu_pct = record["cpu_usage_millicores"] / cpu_limit * 101

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


def x_classify_container__mutmut_22(
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

    mem_pct: float | None = ""
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


def x_classify_container__mutmut_23(
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
    if mem_limit or not mem_unlimited:
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


def x_classify_container__mutmut_24(
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
    if mem_limit and mem_unlimited:
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


def x_classify_container__mutmut_25(
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
        mem_pct = None

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


def x_classify_container__mutmut_26(
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
        mem_pct = record["memory_usage_bytes"] / mem_limit / 100

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


def x_classify_container__mutmut_27(
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
        mem_pct = record["memory_usage_bytes"] * mem_limit * 100

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


def x_classify_container__mutmut_28(
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
        mem_pct = record["XXmemory_usage_bytesXX"] / mem_limit * 100

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


def x_classify_container__mutmut_29(
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
        mem_pct = record["MEMORY_USAGE_BYTES"] / mem_limit * 100

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


def x_classify_container__mutmut_30(
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
        mem_pct = record["memory_usage_bytes"] / mem_limit * 101

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


def x_classify_container__mutmut_31(
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

    tags: list[str] = None
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


def x_classify_container__mutmut_32(
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
    if record["XXis_init_containerXX"]:
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


def x_classify_container__mutmut_33(
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
    if record["IS_INIT_CONTAINER"]:
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


def x_classify_container__mutmut_34(
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
        tags.append(None)
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


def x_classify_container__mutmut_35(
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
        tags.append("XXinit_containerXX")
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


def x_classify_container__mutmut_36(
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
        tags.append("INIT_CONTAINER")
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


def x_classify_container__mutmut_37(
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
        tags.append(None)
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


def x_classify_container__mutmut_38(
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
        tags.append("XXcpu_unlimitedXX")
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


def x_classify_container__mutmut_39(
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
        tags.append("CPU_UNLIMITED")
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


def x_classify_container__mutmut_40(
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
        tags.append(None)

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


def x_classify_container__mutmut_41(
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
        tags.append("XXmemory_unlimitedXX")

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


def x_classify_container__mutmut_42(
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
        tags.append("MEMORY_UNLIMITED")

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


def x_classify_container__mutmut_43(
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

    if cpu_limit is None and mem_limit is None:
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


def x_classify_container__mutmut_44(
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

    if cpu_limit is not None or mem_limit is None:
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


def x_classify_container__mutmut_45(
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

    if cpu_limit is None or mem_limit is not None:
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


def x_classify_container__mutmut_46(
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
        risk_level = None
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


def x_classify_container__mutmut_47(
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
        tags.append(None)
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


def x_classify_container__mutmut_48(
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
        tags.append("XXno_limitsXX")
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


def x_classify_container__mutmut_49(
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
        tags.append("NO_LIMITS")
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


def x_classify_container__mutmut_50(
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
    elif (cpu_pct is not None and cpu_pct > cpu_thr) and (mem_pct is not None and mem_pct > mem_thr):
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


def x_classify_container__mutmut_51(
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
    elif (cpu_pct is not None or cpu_pct > cpu_thr) or (mem_pct is not None and mem_pct > mem_thr):
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


def x_classify_container__mutmut_52(
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
    elif (cpu_pct is None and cpu_pct > cpu_thr) or (mem_pct is not None and mem_pct > mem_thr):
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


def x_classify_container__mutmut_53(
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
    elif (cpu_pct is not None and cpu_pct >= cpu_thr) or (mem_pct is not None and mem_pct > mem_thr):
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


def x_classify_container__mutmut_54(
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
    elif (cpu_pct is not None and cpu_pct > cpu_thr) or (mem_pct is not None or mem_pct > mem_thr):
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


def x_classify_container__mutmut_55(
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
    elif (cpu_pct is not None and cpu_pct > cpu_thr) or (mem_pct is None and mem_pct > mem_thr):
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


def x_classify_container__mutmut_56(
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
    elif (cpu_pct is not None and cpu_pct > cpu_thr) or (mem_pct is not None and mem_pct >= mem_thr):
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


def x_classify_container__mutmut_57(
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
        risk_level = None
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


def x_classify_container__mutmut_58(
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
        if cpu_pct is not None or cpu_pct > cpu_thr:
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


def x_classify_container__mutmut_59(
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
        if cpu_pct is None and cpu_pct > cpu_thr:
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


def x_classify_container__mutmut_60(
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
        if cpu_pct is not None and cpu_pct >= cpu_thr:
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


def x_classify_container__mutmut_61(
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
            tags.append(None)
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


def x_classify_container__mutmut_62(
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
            tags.append("XXthrottledXX")
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


def x_classify_container__mutmut_63(
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
            tags.append("THROTTLED")
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


def x_classify_container__mutmut_64(
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
        if mem_pct is not None or mem_pct > mem_thr:
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


def x_classify_container__mutmut_65(
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
        if mem_pct is None and mem_pct > mem_thr:
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


def x_classify_container__mutmut_66(
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
        if mem_pct is not None and mem_pct >= mem_thr:
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


def x_classify_container__mutmut_67(
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
            tags.append(None)
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


def x_classify_container__mutmut_68(
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
            tags.append("XXoomkill_riskXX")
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


def x_classify_container__mutmut_69(
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
            tags.append("OOMKILL_RISK")
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


def x_classify_container__mutmut_70(
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
        risk_level = None

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


def x_classify_container__mutmut_71(
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
        container_name=None,
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


def x_classify_container__mutmut_72(
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
        pod_name=None,
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


def x_classify_container__mutmut_73(
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
        namespace=None,
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


def x_classify_container__mutmut_74(
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
        cpu_usage_millicores=None,
        cpu_limit_millicores=cpu_limit,
        memory_usage_bytes=record["memory_usage_bytes"],
        memory_limit_bytes=mem_limit,
        cpu_pct=cpu_pct,
        memory_pct=mem_pct,
        risk_level=risk_level,
        is_init_container=record["is_init_container"],
        tags=tags,
    )


def x_classify_container__mutmut_75(
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
        cpu_limit_millicores=None,
        memory_usage_bytes=record["memory_usage_bytes"],
        memory_limit_bytes=mem_limit,
        cpu_pct=cpu_pct,
        memory_pct=mem_pct,
        risk_level=risk_level,
        is_init_container=record["is_init_container"],
        tags=tags,
    )


def x_classify_container__mutmut_76(
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
        memory_usage_bytes=None,
        memory_limit_bytes=mem_limit,
        cpu_pct=cpu_pct,
        memory_pct=mem_pct,
        risk_level=risk_level,
        is_init_container=record["is_init_container"],
        tags=tags,
    )


def x_classify_container__mutmut_77(
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
        memory_limit_bytes=None,
        cpu_pct=cpu_pct,
        memory_pct=mem_pct,
        risk_level=risk_level,
        is_init_container=record["is_init_container"],
        tags=tags,
    )


def x_classify_container__mutmut_78(
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
        cpu_pct=None,
        memory_pct=mem_pct,
        risk_level=risk_level,
        is_init_container=record["is_init_container"],
        tags=tags,
    )


def x_classify_container__mutmut_79(
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
        memory_pct=None,
        risk_level=risk_level,
        is_init_container=record["is_init_container"],
        tags=tags,
    )


def x_classify_container__mutmut_80(
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
        risk_level=None,
        is_init_container=record["is_init_container"],
        tags=tags,
    )


def x_classify_container__mutmut_81(
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
        is_init_container=None,
        tags=tags,
    )


def x_classify_container__mutmut_82(
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
        tags=None,
    )


def x_classify_container__mutmut_83(
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


def x_classify_container__mutmut_84(
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


def x_classify_container__mutmut_85(
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


def x_classify_container__mutmut_86(
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
        cpu_limit_millicores=cpu_limit,
        memory_usage_bytes=record["memory_usage_bytes"],
        memory_limit_bytes=mem_limit,
        cpu_pct=cpu_pct,
        memory_pct=mem_pct,
        risk_level=risk_level,
        is_init_container=record["is_init_container"],
        tags=tags,
    )


def x_classify_container__mutmut_87(
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
        memory_usage_bytes=record["memory_usage_bytes"],
        memory_limit_bytes=mem_limit,
        cpu_pct=cpu_pct,
        memory_pct=mem_pct,
        risk_level=risk_level,
        is_init_container=record["is_init_container"],
        tags=tags,
    )


def x_classify_container__mutmut_88(
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
        memory_limit_bytes=mem_limit,
        cpu_pct=cpu_pct,
        memory_pct=mem_pct,
        risk_level=risk_level,
        is_init_container=record["is_init_container"],
        tags=tags,
    )


def x_classify_container__mutmut_89(
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
        cpu_pct=cpu_pct,
        memory_pct=mem_pct,
        risk_level=risk_level,
        is_init_container=record["is_init_container"],
        tags=tags,
    )


def x_classify_container__mutmut_90(
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
        memory_pct=mem_pct,
        risk_level=risk_level,
        is_init_container=record["is_init_container"],
        tags=tags,
    )


def x_classify_container__mutmut_91(
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
        risk_level=risk_level,
        is_init_container=record["is_init_container"],
        tags=tags,
    )


def x_classify_container__mutmut_92(
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
        is_init_container=record["is_init_container"],
        tags=tags,
    )


def x_classify_container__mutmut_93(
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
        tags=tags,
    )


def x_classify_container__mutmut_94(
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
        )


def x_classify_container__mutmut_95(
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
        container_name=record["XXcontainer_nameXX"],
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


def x_classify_container__mutmut_96(
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
        container_name=record["CONTAINER_NAME"],
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


def x_classify_container__mutmut_97(
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
        pod_name=record["XXpod_nameXX"],
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


def x_classify_container__mutmut_98(
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
        pod_name=record["POD_NAME"],
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


def x_classify_container__mutmut_99(
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
        namespace=record["XXnamespaceXX"],
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


def x_classify_container__mutmut_100(
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
        namespace=record["NAMESPACE"],
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


def x_classify_container__mutmut_101(
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
        cpu_usage_millicores=record["XXcpu_usage_millicoresXX"],
        cpu_limit_millicores=cpu_limit,
        memory_usage_bytes=record["memory_usage_bytes"],
        memory_limit_bytes=mem_limit,
        cpu_pct=cpu_pct,
        memory_pct=mem_pct,
        risk_level=risk_level,
        is_init_container=record["is_init_container"],
        tags=tags,
    )


def x_classify_container__mutmut_102(
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
        cpu_usage_millicores=record["CPU_USAGE_MILLICORES"],
        cpu_limit_millicores=cpu_limit,
        memory_usage_bytes=record["memory_usage_bytes"],
        memory_limit_bytes=mem_limit,
        cpu_pct=cpu_pct,
        memory_pct=mem_pct,
        risk_level=risk_level,
        is_init_container=record["is_init_container"],
        tags=tags,
    )


def x_classify_container__mutmut_103(
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
        memory_usage_bytes=record["XXmemory_usage_bytesXX"],
        memory_limit_bytes=mem_limit,
        cpu_pct=cpu_pct,
        memory_pct=mem_pct,
        risk_level=risk_level,
        is_init_container=record["is_init_container"],
        tags=tags,
    )


def x_classify_container__mutmut_104(
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
        memory_usage_bytes=record["MEMORY_USAGE_BYTES"],
        memory_limit_bytes=mem_limit,
        cpu_pct=cpu_pct,
        memory_pct=mem_pct,
        risk_level=risk_level,
        is_init_container=record["is_init_container"],
        tags=tags,
    )


def x_classify_container__mutmut_105(
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
        is_init_container=record["XXis_init_containerXX"],
        tags=tags,
    )


def x_classify_container__mutmut_106(
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
        is_init_container=record["IS_INIT_CONTAINER"],
        tags=tags,
    )

mutants_x_classify_container__mutmut['_mutmut_orig'] = x_classify_container__mutmut_orig # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_1'] = x_classify_container__mutmut_1 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_2'] = x_classify_container__mutmut_2 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_3'] = x_classify_container__mutmut_3 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_4'] = x_classify_container__mutmut_4 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_5'] = x_classify_container__mutmut_5 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_6'] = x_classify_container__mutmut_6 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_7'] = x_classify_container__mutmut_7 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_8'] = x_classify_container__mutmut_8 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_9'] = x_classify_container__mutmut_9 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_10'] = x_classify_container__mutmut_10 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_11'] = x_classify_container__mutmut_11 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_12'] = x_classify_container__mutmut_12 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_13'] = x_classify_container__mutmut_13 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_14'] = x_classify_container__mutmut_14 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_15'] = x_classify_container__mutmut_15 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_16'] = x_classify_container__mutmut_16 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_17'] = x_classify_container__mutmut_17 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_18'] = x_classify_container__mutmut_18 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_19'] = x_classify_container__mutmut_19 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_20'] = x_classify_container__mutmut_20 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_21'] = x_classify_container__mutmut_21 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_22'] = x_classify_container__mutmut_22 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_23'] = x_classify_container__mutmut_23 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_24'] = x_classify_container__mutmut_24 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_25'] = x_classify_container__mutmut_25 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_26'] = x_classify_container__mutmut_26 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_27'] = x_classify_container__mutmut_27 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_28'] = x_classify_container__mutmut_28 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_29'] = x_classify_container__mutmut_29 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_30'] = x_classify_container__mutmut_30 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_31'] = x_classify_container__mutmut_31 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_32'] = x_classify_container__mutmut_32 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_33'] = x_classify_container__mutmut_33 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_34'] = x_classify_container__mutmut_34 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_35'] = x_classify_container__mutmut_35 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_36'] = x_classify_container__mutmut_36 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_37'] = x_classify_container__mutmut_37 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_38'] = x_classify_container__mutmut_38 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_39'] = x_classify_container__mutmut_39 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_40'] = x_classify_container__mutmut_40 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_41'] = x_classify_container__mutmut_41 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_42'] = x_classify_container__mutmut_42 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_43'] = x_classify_container__mutmut_43 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_44'] = x_classify_container__mutmut_44 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_45'] = x_classify_container__mutmut_45 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_46'] = x_classify_container__mutmut_46 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_47'] = x_classify_container__mutmut_47 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_48'] = x_classify_container__mutmut_48 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_49'] = x_classify_container__mutmut_49 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_50'] = x_classify_container__mutmut_50 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_51'] = x_classify_container__mutmut_51 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_52'] = x_classify_container__mutmut_52 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_53'] = x_classify_container__mutmut_53 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_54'] = x_classify_container__mutmut_54 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_55'] = x_classify_container__mutmut_55 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_56'] = x_classify_container__mutmut_56 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_57'] = x_classify_container__mutmut_57 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_58'] = x_classify_container__mutmut_58 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_59'] = x_classify_container__mutmut_59 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_60'] = x_classify_container__mutmut_60 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_61'] = x_classify_container__mutmut_61 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_62'] = x_classify_container__mutmut_62 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_63'] = x_classify_container__mutmut_63 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_64'] = x_classify_container__mutmut_64 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_65'] = x_classify_container__mutmut_65 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_66'] = x_classify_container__mutmut_66 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_67'] = x_classify_container__mutmut_67 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_68'] = x_classify_container__mutmut_68 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_69'] = x_classify_container__mutmut_69 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_70'] = x_classify_container__mutmut_70 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_71'] = x_classify_container__mutmut_71 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_72'] = x_classify_container__mutmut_72 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_73'] = x_classify_container__mutmut_73 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_74'] = x_classify_container__mutmut_74 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_75'] = x_classify_container__mutmut_75 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_76'] = x_classify_container__mutmut_76 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_77'] = x_classify_container__mutmut_77 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_78'] = x_classify_container__mutmut_78 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_79'] = x_classify_container__mutmut_79 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_80'] = x_classify_container__mutmut_80 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_81'] = x_classify_container__mutmut_81 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_82'] = x_classify_container__mutmut_82 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_83'] = x_classify_container__mutmut_83 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_84'] = x_classify_container__mutmut_84 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_85'] = x_classify_container__mutmut_85 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_86'] = x_classify_container__mutmut_86 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_87'] = x_classify_container__mutmut_87 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_88'] = x_classify_container__mutmut_88 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_89'] = x_classify_container__mutmut_89 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_90'] = x_classify_container__mutmut_90 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_91'] = x_classify_container__mutmut_91 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_92'] = x_classify_container__mutmut_92 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_93'] = x_classify_container__mutmut_93 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_94'] = x_classify_container__mutmut_94 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_95'] = x_classify_container__mutmut_95 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_96'] = x_classify_container__mutmut_96 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_97'] = x_classify_container__mutmut_97 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_98'] = x_classify_container__mutmut_98 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_99'] = x_classify_container__mutmut_99 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_100'] = x_classify_container__mutmut_100 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_101'] = x_classify_container__mutmut_101 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_102'] = x_classify_container__mutmut_102 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_103'] = x_classify_container__mutmut_103 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_104'] = x_classify_container__mutmut_104 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_105'] = x_classify_container__mutmut_105 # type: ignore # mutmut generated
mutants_x_classify_container__mutmut['x_classify_container__mutmut_106'] = x_classify_container__mutmut_106 # type: ignore # mutmut generated
