from __future__ import annotations

from collections import defaultdict

from hexawyn.domain.models.label_search import MatchedResourceResult, NamespaceGroup


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_group_by_namespace__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_group_by_namespace__mutmut)
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


def x_group_by_namespace__mutmut_orig(resources: list[MatchedResourceResult]) -> list[NamespaceGroup]:
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


def x_group_by_namespace__mutmut_1(resources: list[MatchedResourceResult]) -> list[NamespaceGroup]:
    """Groups matched resources by namespace for readable display — sorted by
    namespace name, and by (kind, name) within each group for determinism."""
    by_namespace: dict[str, list[MatchedResourceResult]] = None
    for resource in resources:
        by_namespace[resource.namespace].append(resource)

    return [
        NamespaceGroup(
            namespace=namespace,
            resources=sorted(items, key=lambda resource: (resource.kind, resource.name)),
        )
        for namespace, items in sorted(by_namespace.items())
    ]


def x_group_by_namespace__mutmut_2(resources: list[MatchedResourceResult]) -> list[NamespaceGroup]:
    """Groups matched resources by namespace for readable display — sorted by
    namespace name, and by (kind, name) within each group for determinism."""
    by_namespace: dict[str, list[MatchedResourceResult]] = defaultdict(None)
    for resource in resources:
        by_namespace[resource.namespace].append(resource)

    return [
        NamespaceGroup(
            namespace=namespace,
            resources=sorted(items, key=lambda resource: (resource.kind, resource.name)),
        )
        for namespace, items in sorted(by_namespace.items())
    ]


def x_group_by_namespace__mutmut_3(resources: list[MatchedResourceResult]) -> list[NamespaceGroup]:
    """Groups matched resources by namespace for readable display — sorted by
    namespace name, and by (kind, name) within each group for determinism."""
    by_namespace: dict[str, list[MatchedResourceResult]] = defaultdict(list)
    for resource in resources:
        by_namespace[resource.namespace].append(None)

    return [
        NamespaceGroup(
            namespace=namespace,
            resources=sorted(items, key=lambda resource: (resource.kind, resource.name)),
        )
        for namespace, items in sorted(by_namespace.items())
    ]


def x_group_by_namespace__mutmut_4(resources: list[MatchedResourceResult]) -> list[NamespaceGroup]:
    """Groups matched resources by namespace for readable display — sorted by
    namespace name, and by (kind, name) within each group for determinism."""
    by_namespace: dict[str, list[MatchedResourceResult]] = defaultdict(list)
    for resource in resources:
        by_namespace[resource.namespace].append(resource)

    return [
        NamespaceGroup(
            namespace=None,
            resources=sorted(items, key=lambda resource: (resource.kind, resource.name)),
        )
        for namespace, items in sorted(by_namespace.items())
    ]


def x_group_by_namespace__mutmut_5(resources: list[MatchedResourceResult]) -> list[NamespaceGroup]:
    """Groups matched resources by namespace for readable display — sorted by
    namespace name, and by (kind, name) within each group for determinism."""
    by_namespace: dict[str, list[MatchedResourceResult]] = defaultdict(list)
    for resource in resources:
        by_namespace[resource.namespace].append(resource)

    return [
        NamespaceGroup(
            namespace=namespace,
            resources=None,
        )
        for namespace, items in sorted(by_namespace.items())
    ]


def x_group_by_namespace__mutmut_6(resources: list[MatchedResourceResult]) -> list[NamespaceGroup]:
    """Groups matched resources by namespace for readable display — sorted by
    namespace name, and by (kind, name) within each group for determinism."""
    by_namespace: dict[str, list[MatchedResourceResult]] = defaultdict(list)
    for resource in resources:
        by_namespace[resource.namespace].append(resource)

    return [
        NamespaceGroup(
            resources=sorted(items, key=lambda resource: (resource.kind, resource.name)),
        )
        for namespace, items in sorted(by_namespace.items())
    ]


def x_group_by_namespace__mutmut_7(resources: list[MatchedResourceResult]) -> list[NamespaceGroup]:
    """Groups matched resources by namespace for readable display — sorted by
    namespace name, and by (kind, name) within each group for determinism."""
    by_namespace: dict[str, list[MatchedResourceResult]] = defaultdict(list)
    for resource in resources:
        by_namespace[resource.namespace].append(resource)

    return [
        NamespaceGroup(
            namespace=namespace,
            )
        for namespace, items in sorted(by_namespace.items())
    ]


def x_group_by_namespace__mutmut_8(resources: list[MatchedResourceResult]) -> list[NamespaceGroup]:
    """Groups matched resources by namespace for readable display — sorted by
    namespace name, and by (kind, name) within each group for determinism."""
    by_namespace: dict[str, list[MatchedResourceResult]] = defaultdict(list)
    for resource in resources:
        by_namespace[resource.namespace].append(resource)

    return [
        NamespaceGroup(
            namespace=namespace,
            resources=sorted(None, key=lambda resource: (resource.kind, resource.name)),
        )
        for namespace, items in sorted(by_namespace.items())
    ]


def x_group_by_namespace__mutmut_9(resources: list[MatchedResourceResult]) -> list[NamespaceGroup]:
    """Groups matched resources by namespace for readable display — sorted by
    namespace name, and by (kind, name) within each group for determinism."""
    by_namespace: dict[str, list[MatchedResourceResult]] = defaultdict(list)
    for resource in resources:
        by_namespace[resource.namespace].append(resource)

    return [
        NamespaceGroup(
            namespace=namespace,
            resources=sorted(items, key=None),
        )
        for namespace, items in sorted(by_namespace.items())
    ]


def x_group_by_namespace__mutmut_10(resources: list[MatchedResourceResult]) -> list[NamespaceGroup]:
    """Groups matched resources by namespace for readable display — sorted by
    namespace name, and by (kind, name) within each group for determinism."""
    by_namespace: dict[str, list[MatchedResourceResult]] = defaultdict(list)
    for resource in resources:
        by_namespace[resource.namespace].append(resource)

    return [
        NamespaceGroup(
            namespace=namespace,
            resources=sorted(key=lambda resource: (resource.kind, resource.name)),
        )
        for namespace, items in sorted(by_namespace.items())
    ]


def x_group_by_namespace__mutmut_11(resources: list[MatchedResourceResult]) -> list[NamespaceGroup]:
    """Groups matched resources by namespace for readable display — sorted by
    namespace name, and by (kind, name) within each group for determinism."""
    by_namespace: dict[str, list[MatchedResourceResult]] = defaultdict(list)
    for resource in resources:
        by_namespace[resource.namespace].append(resource)

    return [
        NamespaceGroup(
            namespace=namespace,
            resources=sorted(items, ),
        )
        for namespace, items in sorted(by_namespace.items())
    ]


def x_group_by_namespace__mutmut_12(resources: list[MatchedResourceResult]) -> list[NamespaceGroup]:
    """Groups matched resources by namespace for readable display — sorted by
    namespace name, and by (kind, name) within each group for determinism."""
    by_namespace: dict[str, list[MatchedResourceResult]] = defaultdict(list)
    for resource in resources:
        by_namespace[resource.namespace].append(resource)

    return [
        NamespaceGroup(
            namespace=namespace,
            resources=sorted(items, key=lambda resource: None),
        )
        for namespace, items in sorted(by_namespace.items())
    ]


def x_group_by_namespace__mutmut_13(resources: list[MatchedResourceResult]) -> list[NamespaceGroup]:
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
        for namespace, items in sorted(None)
    ]

mutants_x_group_by_namespace__mutmut['_mutmut_orig'] = x_group_by_namespace__mutmut_orig # type: ignore # mutmut generated
mutants_x_group_by_namespace__mutmut['x_group_by_namespace__mutmut_1'] = x_group_by_namespace__mutmut_1 # type: ignore # mutmut generated
mutants_x_group_by_namespace__mutmut['x_group_by_namespace__mutmut_2'] = x_group_by_namespace__mutmut_2 # type: ignore # mutmut generated
mutants_x_group_by_namespace__mutmut['x_group_by_namespace__mutmut_3'] = x_group_by_namespace__mutmut_3 # type: ignore # mutmut generated
mutants_x_group_by_namespace__mutmut['x_group_by_namespace__mutmut_4'] = x_group_by_namespace__mutmut_4 # type: ignore # mutmut generated
mutants_x_group_by_namespace__mutmut['x_group_by_namespace__mutmut_5'] = x_group_by_namespace__mutmut_5 # type: ignore # mutmut generated
mutants_x_group_by_namespace__mutmut['x_group_by_namespace__mutmut_6'] = x_group_by_namespace__mutmut_6 # type: ignore # mutmut generated
mutants_x_group_by_namespace__mutmut['x_group_by_namespace__mutmut_7'] = x_group_by_namespace__mutmut_7 # type: ignore # mutmut generated
mutants_x_group_by_namespace__mutmut['x_group_by_namespace__mutmut_8'] = x_group_by_namespace__mutmut_8 # type: ignore # mutmut generated
mutants_x_group_by_namespace__mutmut['x_group_by_namespace__mutmut_9'] = x_group_by_namespace__mutmut_9 # type: ignore # mutmut generated
mutants_x_group_by_namespace__mutmut['x_group_by_namespace__mutmut_10'] = x_group_by_namespace__mutmut_10 # type: ignore # mutmut generated
mutants_x_group_by_namespace__mutmut['x_group_by_namespace__mutmut_11'] = x_group_by_namespace__mutmut_11 # type: ignore # mutmut generated
mutants_x_group_by_namespace__mutmut['x_group_by_namespace__mutmut_12'] = x_group_by_namespace__mutmut_12 # type: ignore # mutmut generated
mutants_x_group_by_namespace__mutmut['x_group_by_namespace__mutmut_13'] = x_group_by_namespace__mutmut_13 # type: ignore # mutmut generated
