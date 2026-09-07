from __future__ import annotations

from collections import defaultdict

from hexawyn.domain.models.log_search import PodLogMatch, ServiceGroup


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_derive_service_name__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_derive_service_name__mutmut)
def derive_service_name(pod_name: str) -> str:
    """Pod names created by a Deployment follow {deployment}-{rs-hash}-{pod-hash};
    StatefulSet pods follow {statefulset}-{ordinal}. Stripping the last two (or
    one) dash-separated suffixes recovers the owning workload's name — the same
    naming-convention heuristic already duplicated privately, twice, in
    vanilla_adapter.py, relocated here as the single clean domain version."""
    parts = pod_name.rsplit("-", 2)
    if len(parts) >= 2:  # noqa: PLR2004
        return parts[0]
    return pod_name


def x_derive_service_name__mutmut_orig(pod_name: str) -> str:
    """Pod names created by a Deployment follow {deployment}-{rs-hash}-{pod-hash};
    StatefulSet pods follow {statefulset}-{ordinal}. Stripping the last two (or
    one) dash-separated suffixes recovers the owning workload's name — the same
    naming-convention heuristic already duplicated privately, twice, in
    vanilla_adapter.py, relocated here as the single clean domain version."""
    parts = pod_name.rsplit("-", 2)
    if len(parts) >= 2:  # noqa: PLR2004
        return parts[0]
    return pod_name


def x_derive_service_name__mutmut_1(pod_name: str) -> str:
    """Pod names created by a Deployment follow {deployment}-{rs-hash}-{pod-hash};
    StatefulSet pods follow {statefulset}-{ordinal}. Stripping the last two (or
    one) dash-separated suffixes recovers the owning workload's name — the same
    naming-convention heuristic already duplicated privately, twice, in
    vanilla_adapter.py, relocated here as the single clean domain version."""
    parts = None
    if len(parts) >= 2:  # noqa: PLR2004
        return parts[0]
    return pod_name


def x_derive_service_name__mutmut_2(pod_name: str) -> str:
    """Pod names created by a Deployment follow {deployment}-{rs-hash}-{pod-hash};
    StatefulSet pods follow {statefulset}-{ordinal}. Stripping the last two (or
    one) dash-separated suffixes recovers the owning workload's name — the same
    naming-convention heuristic already duplicated privately, twice, in
    vanilla_adapter.py, relocated here as the single clean domain version."""
    parts = pod_name.rsplit(None, 2)
    if len(parts) >= 2:  # noqa: PLR2004
        return parts[0]
    return pod_name


def x_derive_service_name__mutmut_3(pod_name: str) -> str:
    """Pod names created by a Deployment follow {deployment}-{rs-hash}-{pod-hash};
    StatefulSet pods follow {statefulset}-{ordinal}. Stripping the last two (or
    one) dash-separated suffixes recovers the owning workload's name — the same
    naming-convention heuristic already duplicated privately, twice, in
    vanilla_adapter.py, relocated here as the single clean domain version."""
    parts = pod_name.rsplit("-", None)
    if len(parts) >= 2:  # noqa: PLR2004
        return parts[0]
    return pod_name


def x_derive_service_name__mutmut_4(pod_name: str) -> str:
    """Pod names created by a Deployment follow {deployment}-{rs-hash}-{pod-hash};
    StatefulSet pods follow {statefulset}-{ordinal}. Stripping the last two (or
    one) dash-separated suffixes recovers the owning workload's name — the same
    naming-convention heuristic already duplicated privately, twice, in
    vanilla_adapter.py, relocated here as the single clean domain version."""
    parts = pod_name.rsplit(2)
    if len(parts) >= 2:  # noqa: PLR2004
        return parts[0]
    return pod_name


def x_derive_service_name__mutmut_5(pod_name: str) -> str:
    """Pod names created by a Deployment follow {deployment}-{rs-hash}-{pod-hash};
    StatefulSet pods follow {statefulset}-{ordinal}. Stripping the last two (or
    one) dash-separated suffixes recovers the owning workload's name — the same
    naming-convention heuristic already duplicated privately, twice, in
    vanilla_adapter.py, relocated here as the single clean domain version."""
    parts = pod_name.rsplit("-", )
    if len(parts) >= 2:  # noqa: PLR2004
        return parts[0]
    return pod_name


def x_derive_service_name__mutmut_6(pod_name: str) -> str:
    """Pod names created by a Deployment follow {deployment}-{rs-hash}-{pod-hash};
    StatefulSet pods follow {statefulset}-{ordinal}. Stripping the last two (or
    one) dash-separated suffixes recovers the owning workload's name — the same
    naming-convention heuristic already duplicated privately, twice, in
    vanilla_adapter.py, relocated here as the single clean domain version."""
    parts = pod_name.split("-", 2)
    if len(parts) >= 2:  # noqa: PLR2004
        return parts[0]
    return pod_name


def x_derive_service_name__mutmut_7(pod_name: str) -> str:
    """Pod names created by a Deployment follow {deployment}-{rs-hash}-{pod-hash};
    StatefulSet pods follow {statefulset}-{ordinal}. Stripping the last two (or
    one) dash-separated suffixes recovers the owning workload's name — the same
    naming-convention heuristic already duplicated privately, twice, in
    vanilla_adapter.py, relocated here as the single clean domain version."""
    parts = pod_name.rsplit("XX-XX", 2)
    if len(parts) >= 2:  # noqa: PLR2004
        return parts[0]
    return pod_name


def x_derive_service_name__mutmut_8(pod_name: str) -> str:
    """Pod names created by a Deployment follow {deployment}-{rs-hash}-{pod-hash};
    StatefulSet pods follow {statefulset}-{ordinal}. Stripping the last two (or
    one) dash-separated suffixes recovers the owning workload's name — the same
    naming-convention heuristic already duplicated privately, twice, in
    vanilla_adapter.py, relocated here as the single clean domain version."""
    parts = pod_name.rsplit("-", 3)
    if len(parts) >= 2:  # noqa: PLR2004
        return parts[0]
    return pod_name


def x_derive_service_name__mutmut_9(pod_name: str) -> str:
    """Pod names created by a Deployment follow {deployment}-{rs-hash}-{pod-hash};
    StatefulSet pods follow {statefulset}-{ordinal}. Stripping the last two (or
    one) dash-separated suffixes recovers the owning workload's name — the same
    naming-convention heuristic already duplicated privately, twice, in
    vanilla_adapter.py, relocated here as the single clean domain version."""
    parts = pod_name.rsplit("-", 2)
    if len(parts) > 2:  # noqa: PLR2004
        return parts[0]
    return pod_name


def x_derive_service_name__mutmut_10(pod_name: str) -> str:
    """Pod names created by a Deployment follow {deployment}-{rs-hash}-{pod-hash};
    StatefulSet pods follow {statefulset}-{ordinal}. Stripping the last two (or
    one) dash-separated suffixes recovers the owning workload's name — the same
    naming-convention heuristic already duplicated privately, twice, in
    vanilla_adapter.py, relocated here as the single clean domain version."""
    parts = pod_name.rsplit("-", 2)
    if len(parts) >= 3:  # noqa: PLR2004
        return parts[0]
    return pod_name


def x_derive_service_name__mutmut_11(pod_name: str) -> str:
    """Pod names created by a Deployment follow {deployment}-{rs-hash}-{pod-hash};
    StatefulSet pods follow {statefulset}-{ordinal}. Stripping the last two (or
    one) dash-separated suffixes recovers the owning workload's name — the same
    naming-convention heuristic already duplicated privately, twice, in
    vanilla_adapter.py, relocated here as the single clean domain version."""
    parts = pod_name.rsplit("-", 2)
    if len(parts) >= 2:  # noqa: PLR2004
        return parts[1]
    return pod_name

mutants_x_derive_service_name__mutmut['_mutmut_orig'] = x_derive_service_name__mutmut_orig # type: ignore # mutmut generated
mutants_x_derive_service_name__mutmut['x_derive_service_name__mutmut_1'] = x_derive_service_name__mutmut_1 # type: ignore # mutmut generated
mutants_x_derive_service_name__mutmut['x_derive_service_name__mutmut_2'] = x_derive_service_name__mutmut_2 # type: ignore # mutmut generated
mutants_x_derive_service_name__mutmut['x_derive_service_name__mutmut_3'] = x_derive_service_name__mutmut_3 # type: ignore # mutmut generated
mutants_x_derive_service_name__mutmut['x_derive_service_name__mutmut_4'] = x_derive_service_name__mutmut_4 # type: ignore # mutmut generated
mutants_x_derive_service_name__mutmut['x_derive_service_name__mutmut_5'] = x_derive_service_name__mutmut_5 # type: ignore # mutmut generated
mutants_x_derive_service_name__mutmut['x_derive_service_name__mutmut_6'] = x_derive_service_name__mutmut_6 # type: ignore # mutmut generated
mutants_x_derive_service_name__mutmut['x_derive_service_name__mutmut_7'] = x_derive_service_name__mutmut_7 # type: ignore # mutmut generated
mutants_x_derive_service_name__mutmut['x_derive_service_name__mutmut_8'] = x_derive_service_name__mutmut_8 # type: ignore # mutmut generated
mutants_x_derive_service_name__mutmut['x_derive_service_name__mutmut_9'] = x_derive_service_name__mutmut_9 # type: ignore # mutmut generated
mutants_x_derive_service_name__mutmut['x_derive_service_name__mutmut_10'] = x_derive_service_name__mutmut_10 # type: ignore # mutmut generated
mutants_x_derive_service_name__mutmut['x_derive_service_name__mutmut_11'] = x_derive_service_name__mutmut_11 # type: ignore # mutmut generated
mutants_x_group_by_service__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_group_by_service__mutmut)
def group_by_service(matches: list[PodLogMatch]) -> list[ServiceGroup]:
    """Groups matched (pod, container) results by derived service/deployment
    name for impact assessment — sorted by namespace then service name."""
    by_service: dict[tuple[str, str], list[PodLogMatch]] = defaultdict(list)
    for match in matches:
        service_name = derive_service_name(match.pod_name)
        by_service[(match.namespace, service_name)].append(match)

    return [
        ServiceGroup(
            service_name=service_name,
            namespace=namespace,
            pods=sorted(pods, key=lambda match: (match.pod_name, match.container)),
        )
        for (namespace, service_name), pods in sorted(by_service.items())
    ]


def x_group_by_service__mutmut_orig(matches: list[PodLogMatch]) -> list[ServiceGroup]:
    """Groups matched (pod, container) results by derived service/deployment
    name for impact assessment — sorted by namespace then service name."""
    by_service: dict[tuple[str, str], list[PodLogMatch]] = defaultdict(list)
    for match in matches:
        service_name = derive_service_name(match.pod_name)
        by_service[(match.namespace, service_name)].append(match)

    return [
        ServiceGroup(
            service_name=service_name,
            namespace=namespace,
            pods=sorted(pods, key=lambda match: (match.pod_name, match.container)),
        )
        for (namespace, service_name), pods in sorted(by_service.items())
    ]


def x_group_by_service__mutmut_1(matches: list[PodLogMatch]) -> list[ServiceGroup]:
    """Groups matched (pod, container) results by derived service/deployment
    name for impact assessment — sorted by namespace then service name."""
    by_service: dict[tuple[str, str], list[PodLogMatch]] = None
    for match in matches:
        service_name = derive_service_name(match.pod_name)
        by_service[(match.namespace, service_name)].append(match)

    return [
        ServiceGroup(
            service_name=service_name,
            namespace=namespace,
            pods=sorted(pods, key=lambda match: (match.pod_name, match.container)),
        )
        for (namespace, service_name), pods in sorted(by_service.items())
    ]


def x_group_by_service__mutmut_2(matches: list[PodLogMatch]) -> list[ServiceGroup]:
    """Groups matched (pod, container) results by derived service/deployment
    name for impact assessment — sorted by namespace then service name."""
    by_service: dict[tuple[str, str], list[PodLogMatch]] = defaultdict(None)
    for match in matches:
        service_name = derive_service_name(match.pod_name)
        by_service[(match.namespace, service_name)].append(match)

    return [
        ServiceGroup(
            service_name=service_name,
            namespace=namespace,
            pods=sorted(pods, key=lambda match: (match.pod_name, match.container)),
        )
        for (namespace, service_name), pods in sorted(by_service.items())
    ]


def x_group_by_service__mutmut_3(matches: list[PodLogMatch]) -> list[ServiceGroup]:
    """Groups matched (pod, container) results by derived service/deployment
    name for impact assessment — sorted by namespace then service name."""
    by_service: dict[tuple[str, str], list[PodLogMatch]] = defaultdict(list)
    for match in matches:
        service_name = None
        by_service[(match.namespace, service_name)].append(match)

    return [
        ServiceGroup(
            service_name=service_name,
            namespace=namespace,
            pods=sorted(pods, key=lambda match: (match.pod_name, match.container)),
        )
        for (namespace, service_name), pods in sorted(by_service.items())
    ]


def x_group_by_service__mutmut_4(matches: list[PodLogMatch]) -> list[ServiceGroup]:
    """Groups matched (pod, container) results by derived service/deployment
    name for impact assessment — sorted by namespace then service name."""
    by_service: dict[tuple[str, str], list[PodLogMatch]] = defaultdict(list)
    for match in matches:
        service_name = derive_service_name(None)
        by_service[(match.namespace, service_name)].append(match)

    return [
        ServiceGroup(
            service_name=service_name,
            namespace=namespace,
            pods=sorted(pods, key=lambda match: (match.pod_name, match.container)),
        )
        for (namespace, service_name), pods in sorted(by_service.items())
    ]


def x_group_by_service__mutmut_5(matches: list[PodLogMatch]) -> list[ServiceGroup]:
    """Groups matched (pod, container) results by derived service/deployment
    name for impact assessment — sorted by namespace then service name."""
    by_service: dict[tuple[str, str], list[PodLogMatch]] = defaultdict(list)
    for match in matches:
        service_name = derive_service_name(match.pod_name)
        by_service[(match.namespace, service_name)].append(None)

    return [
        ServiceGroup(
            service_name=service_name,
            namespace=namespace,
            pods=sorted(pods, key=lambda match: (match.pod_name, match.container)),
        )
        for (namespace, service_name), pods in sorted(by_service.items())
    ]


def x_group_by_service__mutmut_6(matches: list[PodLogMatch]) -> list[ServiceGroup]:
    """Groups matched (pod, container) results by derived service/deployment
    name for impact assessment — sorted by namespace then service name."""
    by_service: dict[tuple[str, str], list[PodLogMatch]] = defaultdict(list)
    for match in matches:
        service_name = derive_service_name(match.pod_name)
        by_service[(match.namespace, service_name)].append(match)

    return [
        ServiceGroup(
            service_name=None,
            namespace=namespace,
            pods=sorted(pods, key=lambda match: (match.pod_name, match.container)),
        )
        for (namespace, service_name), pods in sorted(by_service.items())
    ]


def x_group_by_service__mutmut_7(matches: list[PodLogMatch]) -> list[ServiceGroup]:
    """Groups matched (pod, container) results by derived service/deployment
    name for impact assessment — sorted by namespace then service name."""
    by_service: dict[tuple[str, str], list[PodLogMatch]] = defaultdict(list)
    for match in matches:
        service_name = derive_service_name(match.pod_name)
        by_service[(match.namespace, service_name)].append(match)

    return [
        ServiceGroup(
            service_name=service_name,
            namespace=None,
            pods=sorted(pods, key=lambda match: (match.pod_name, match.container)),
        )
        for (namespace, service_name), pods in sorted(by_service.items())
    ]


def x_group_by_service__mutmut_8(matches: list[PodLogMatch]) -> list[ServiceGroup]:
    """Groups matched (pod, container) results by derived service/deployment
    name for impact assessment — sorted by namespace then service name."""
    by_service: dict[tuple[str, str], list[PodLogMatch]] = defaultdict(list)
    for match in matches:
        service_name = derive_service_name(match.pod_name)
        by_service[(match.namespace, service_name)].append(match)

    return [
        ServiceGroup(
            service_name=service_name,
            namespace=namespace,
            pods=None,
        )
        for (namespace, service_name), pods in sorted(by_service.items())
    ]


def x_group_by_service__mutmut_9(matches: list[PodLogMatch]) -> list[ServiceGroup]:
    """Groups matched (pod, container) results by derived service/deployment
    name for impact assessment — sorted by namespace then service name."""
    by_service: dict[tuple[str, str], list[PodLogMatch]] = defaultdict(list)
    for match in matches:
        service_name = derive_service_name(match.pod_name)
        by_service[(match.namespace, service_name)].append(match)

    return [
        ServiceGroup(
            namespace=namespace,
            pods=sorted(pods, key=lambda match: (match.pod_name, match.container)),
        )
        for (namespace, service_name), pods in sorted(by_service.items())
    ]


def x_group_by_service__mutmut_10(matches: list[PodLogMatch]) -> list[ServiceGroup]:
    """Groups matched (pod, container) results by derived service/deployment
    name for impact assessment — sorted by namespace then service name."""
    by_service: dict[tuple[str, str], list[PodLogMatch]] = defaultdict(list)
    for match in matches:
        service_name = derive_service_name(match.pod_name)
        by_service[(match.namespace, service_name)].append(match)

    return [
        ServiceGroup(
            service_name=service_name,
            pods=sorted(pods, key=lambda match: (match.pod_name, match.container)),
        )
        for (namespace, service_name), pods in sorted(by_service.items())
    ]


def x_group_by_service__mutmut_11(matches: list[PodLogMatch]) -> list[ServiceGroup]:
    """Groups matched (pod, container) results by derived service/deployment
    name for impact assessment — sorted by namespace then service name."""
    by_service: dict[tuple[str, str], list[PodLogMatch]] = defaultdict(list)
    for match in matches:
        service_name = derive_service_name(match.pod_name)
        by_service[(match.namespace, service_name)].append(match)

    return [
        ServiceGroup(
            service_name=service_name,
            namespace=namespace,
            )
        for (namespace, service_name), pods in sorted(by_service.items())
    ]


def x_group_by_service__mutmut_12(matches: list[PodLogMatch]) -> list[ServiceGroup]:
    """Groups matched (pod, container) results by derived service/deployment
    name for impact assessment — sorted by namespace then service name."""
    by_service: dict[tuple[str, str], list[PodLogMatch]] = defaultdict(list)
    for match in matches:
        service_name = derive_service_name(match.pod_name)
        by_service[(match.namespace, service_name)].append(match)

    return [
        ServiceGroup(
            service_name=service_name,
            namespace=namespace,
            pods=sorted(None, key=lambda match: (match.pod_name, match.container)),
        )
        for (namespace, service_name), pods in sorted(by_service.items())
    ]


def x_group_by_service__mutmut_13(matches: list[PodLogMatch]) -> list[ServiceGroup]:
    """Groups matched (pod, container) results by derived service/deployment
    name for impact assessment — sorted by namespace then service name."""
    by_service: dict[tuple[str, str], list[PodLogMatch]] = defaultdict(list)
    for match in matches:
        service_name = derive_service_name(match.pod_name)
        by_service[(match.namespace, service_name)].append(match)

    return [
        ServiceGroup(
            service_name=service_name,
            namespace=namespace,
            pods=sorted(pods, key=None),
        )
        for (namespace, service_name), pods in sorted(by_service.items())
    ]


def x_group_by_service__mutmut_14(matches: list[PodLogMatch]) -> list[ServiceGroup]:
    """Groups matched (pod, container) results by derived service/deployment
    name for impact assessment — sorted by namespace then service name."""
    by_service: dict[tuple[str, str], list[PodLogMatch]] = defaultdict(list)
    for match in matches:
        service_name = derive_service_name(match.pod_name)
        by_service[(match.namespace, service_name)].append(match)

    return [
        ServiceGroup(
            service_name=service_name,
            namespace=namespace,
            pods=sorted(key=lambda match: (match.pod_name, match.container)),
        )
        for (namespace, service_name), pods in sorted(by_service.items())
    ]


def x_group_by_service__mutmut_15(matches: list[PodLogMatch]) -> list[ServiceGroup]:
    """Groups matched (pod, container) results by derived service/deployment
    name for impact assessment — sorted by namespace then service name."""
    by_service: dict[tuple[str, str], list[PodLogMatch]] = defaultdict(list)
    for match in matches:
        service_name = derive_service_name(match.pod_name)
        by_service[(match.namespace, service_name)].append(match)

    return [
        ServiceGroup(
            service_name=service_name,
            namespace=namespace,
            pods=sorted(pods, ),
        )
        for (namespace, service_name), pods in sorted(by_service.items())
    ]


def x_group_by_service__mutmut_16(matches: list[PodLogMatch]) -> list[ServiceGroup]:
    """Groups matched (pod, container) results by derived service/deployment
    name for impact assessment — sorted by namespace then service name."""
    by_service: dict[tuple[str, str], list[PodLogMatch]] = defaultdict(list)
    for match in matches:
        service_name = derive_service_name(match.pod_name)
        by_service[(match.namespace, service_name)].append(match)

    return [
        ServiceGroup(
            service_name=service_name,
            namespace=namespace,
            pods=sorted(pods, key=lambda match: None),
        )
        for (namespace, service_name), pods in sorted(by_service.items())
    ]


def x_group_by_service__mutmut_17(matches: list[PodLogMatch]) -> list[ServiceGroup]:
    """Groups matched (pod, container) results by derived service/deployment
    name for impact assessment — sorted by namespace then service name."""
    by_service: dict[tuple[str, str], list[PodLogMatch]] = defaultdict(list)
    for match in matches:
        service_name = derive_service_name(match.pod_name)
        by_service[(match.namespace, service_name)].append(match)

    return [
        ServiceGroup(
            service_name=service_name,
            namespace=namespace,
            pods=sorted(pods, key=lambda match: (match.pod_name, match.container)),
        )
        for (namespace, service_name), pods in sorted(None)
    ]

mutants_x_group_by_service__mutmut['_mutmut_orig'] = x_group_by_service__mutmut_orig # type: ignore # mutmut generated
mutants_x_group_by_service__mutmut['x_group_by_service__mutmut_1'] = x_group_by_service__mutmut_1 # type: ignore # mutmut generated
mutants_x_group_by_service__mutmut['x_group_by_service__mutmut_2'] = x_group_by_service__mutmut_2 # type: ignore # mutmut generated
mutants_x_group_by_service__mutmut['x_group_by_service__mutmut_3'] = x_group_by_service__mutmut_3 # type: ignore # mutmut generated
mutants_x_group_by_service__mutmut['x_group_by_service__mutmut_4'] = x_group_by_service__mutmut_4 # type: ignore # mutmut generated
mutants_x_group_by_service__mutmut['x_group_by_service__mutmut_5'] = x_group_by_service__mutmut_5 # type: ignore # mutmut generated
mutants_x_group_by_service__mutmut['x_group_by_service__mutmut_6'] = x_group_by_service__mutmut_6 # type: ignore # mutmut generated
mutants_x_group_by_service__mutmut['x_group_by_service__mutmut_7'] = x_group_by_service__mutmut_7 # type: ignore # mutmut generated
mutants_x_group_by_service__mutmut['x_group_by_service__mutmut_8'] = x_group_by_service__mutmut_8 # type: ignore # mutmut generated
mutants_x_group_by_service__mutmut['x_group_by_service__mutmut_9'] = x_group_by_service__mutmut_9 # type: ignore # mutmut generated
mutants_x_group_by_service__mutmut['x_group_by_service__mutmut_10'] = x_group_by_service__mutmut_10 # type: ignore # mutmut generated
mutants_x_group_by_service__mutmut['x_group_by_service__mutmut_11'] = x_group_by_service__mutmut_11 # type: ignore # mutmut generated
mutants_x_group_by_service__mutmut['x_group_by_service__mutmut_12'] = x_group_by_service__mutmut_12 # type: ignore # mutmut generated
mutants_x_group_by_service__mutmut['x_group_by_service__mutmut_13'] = x_group_by_service__mutmut_13 # type: ignore # mutmut generated
mutants_x_group_by_service__mutmut['x_group_by_service__mutmut_14'] = x_group_by_service__mutmut_14 # type: ignore # mutmut generated
mutants_x_group_by_service__mutmut['x_group_by_service__mutmut_15'] = x_group_by_service__mutmut_15 # type: ignore # mutmut generated
mutants_x_group_by_service__mutmut['x_group_by_service__mutmut_16'] = x_group_by_service__mutmut_16 # type: ignore # mutmut generated
mutants_x_group_by_service__mutmut['x_group_by_service__mutmut_17'] = x_group_by_service__mutmut_17 # type: ignore # mutmut generated
