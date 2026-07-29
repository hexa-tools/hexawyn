from __future__ import annotations

from collections import defaultdict

from hexawyn.domain.models.log_search import PodLogMatch, ServiceGroup


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
