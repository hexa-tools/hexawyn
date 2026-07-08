from __future__ import annotations

from collections import defaultdict

from hexawyn.domain.models.label_search import MatchedResourceResult, NamespaceGroup


def group_by_namespace(resources: list[MatchedResourceResult]) -> list[NamespaceGroup]:
    """Groups matched resources by namespace for readable display — sorted by
    namespace name, and by (kind, name) within each group for determinism."""
    by_namespace: dict[str, list[MatchedResourceResult]] = defaultdict(list)
    for resource in resources:
        by_namespace[resource.namespace].append(resource)

    return [
        NamespaceGroup(
            namespace=namespace,
            resources=sorted(items, key=lambda resource: (resource.kind, resource.name)),
        )
        for namespace, items in sorted(by_namespace.items())
    ]
