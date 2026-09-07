from __future__ import annotations

from hexawyn.domain.models.label_search import MatchedResourceResult

_UNHEALTHY_PHASES = frozenset(
    {
        "CrashLoop",
        "CrashLoopBackOff",
        "Error",
        "ImagePullBackOff",
        "Pending",
        "Unknown",
        "Terminating",
        "Failed",
    }
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_is_pod_healthy__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_is_pod_healthy__mutmut)
def is_pod_healthy(phase: str | None) -> bool | None:
    """`None` when the resource has no phase concept at all (non-pod kinds) —
    distinct from `False`, which means a real unhealthy pod status."""
    if phase is None:
        return None
    return phase not in _UNHEALTHY_PHASES


def x_is_pod_healthy__mutmut_orig(phase: str | None) -> bool | None:
    """`None` when the resource has no phase concept at all (non-pod kinds) —
    distinct from `False`, which means a real unhealthy pod status."""
    if phase is None:
        return None
    return phase not in _UNHEALTHY_PHASES


def x_is_pod_healthy__mutmut_1(phase: str | None) -> bool | None:
    """`None` when the resource has no phase concept at all (non-pod kinds) —
    distinct from `False`, which means a real unhealthy pod status."""
    if phase is not None:
        return None
    return phase not in _UNHEALTHY_PHASES


def x_is_pod_healthy__mutmut_2(phase: str | None) -> bool | None:
    """`None` when the resource has no phase concept at all (non-pod kinds) —
    distinct from `False`, which means a real unhealthy pod status."""
    if phase is None:
        return None
    return phase in _UNHEALTHY_PHASES

mutants_x_is_pod_healthy__mutmut['_mutmut_orig'] = x_is_pod_healthy__mutmut_orig # type: ignore # mutmut generated
mutants_x_is_pod_healthy__mutmut['x_is_pod_healthy__mutmut_1'] = x_is_pod_healthy__mutmut_1 # type: ignore # mutmut generated
mutants_x_is_pod_healthy__mutmut['x_is_pod_healthy__mutmut_2'] = x_is_pod_healthy__mutmut_2 # type: ignore # mutmut generated
mutants_x_summarize_health__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_summarize_health__mutmut)
def summarize_health(resources: list[MatchedResourceResult], label_selector: str) -> str:
    if not resources:
        return f"No resources found matching label selector '{label_selector}'."

    unhealthy = [resource for resource in resources if resource.is_healthy is False]
    if not unhealthy:
        return f"All {len(resources)} resources healthy (matching '{label_selector}')."

    flagged = ", ".join(f"{resource.name} ({resource.phase})" for resource in unhealthy)
    return (
        f"{len(resources)} resources matched, {len(unhealthy)} unhealthy: {flagged} "
        f"(matching '{label_selector}')."
    )


def x_summarize_health__mutmut_orig(resources: list[MatchedResourceResult], label_selector: str) -> str:
    if not resources:
        return f"No resources found matching label selector '{label_selector}'."

    unhealthy = [resource for resource in resources if resource.is_healthy is False]
    if not unhealthy:
        return f"All {len(resources)} resources healthy (matching '{label_selector}')."

    flagged = ", ".join(f"{resource.name} ({resource.phase})" for resource in unhealthy)
    return (
        f"{len(resources)} resources matched, {len(unhealthy)} unhealthy: {flagged} "
        f"(matching '{label_selector}')."
    )


def x_summarize_health__mutmut_1(resources: list[MatchedResourceResult], label_selector: str) -> str:
    if resources:
        return f"No resources found matching label selector '{label_selector}'."

    unhealthy = [resource for resource in resources if resource.is_healthy is False]
    if not unhealthy:
        return f"All {len(resources)} resources healthy (matching '{label_selector}')."

    flagged = ", ".join(f"{resource.name} ({resource.phase})" for resource in unhealthy)
    return (
        f"{len(resources)} resources matched, {len(unhealthy)} unhealthy: {flagged} "
        f"(matching '{label_selector}')."
    )


def x_summarize_health__mutmut_2(resources: list[MatchedResourceResult], label_selector: str) -> str:
    if not resources:
        return f"No resources found matching label selector '{label_selector}'."

    unhealthy = None
    if not unhealthy:
        return f"All {len(resources)} resources healthy (matching '{label_selector}')."

    flagged = ", ".join(f"{resource.name} ({resource.phase})" for resource in unhealthy)
    return (
        f"{len(resources)} resources matched, {len(unhealthy)} unhealthy: {flagged} "
        f"(matching '{label_selector}')."
    )


def x_summarize_health__mutmut_3(resources: list[MatchedResourceResult], label_selector: str) -> str:
    if not resources:
        return f"No resources found matching label selector '{label_selector}'."

    unhealthy = [resource for resource in resources if resource.is_healthy is not False]
    if not unhealthy:
        return f"All {len(resources)} resources healthy (matching '{label_selector}')."

    flagged = ", ".join(f"{resource.name} ({resource.phase})" for resource in unhealthy)
    return (
        f"{len(resources)} resources matched, {len(unhealthy)} unhealthy: {flagged} "
        f"(matching '{label_selector}')."
    )


def x_summarize_health__mutmut_4(resources: list[MatchedResourceResult], label_selector: str) -> str:
    if not resources:
        return f"No resources found matching label selector '{label_selector}'."

    unhealthy = [resource for resource in resources if resource.is_healthy is True]
    if not unhealthy:
        return f"All {len(resources)} resources healthy (matching '{label_selector}')."

    flagged = ", ".join(f"{resource.name} ({resource.phase})" for resource in unhealthy)
    return (
        f"{len(resources)} resources matched, {len(unhealthy)} unhealthy: {flagged} "
        f"(matching '{label_selector}')."
    )


def x_summarize_health__mutmut_5(resources: list[MatchedResourceResult], label_selector: str) -> str:
    if not resources:
        return f"No resources found matching label selector '{label_selector}'."

    unhealthy = [resource for resource in resources if resource.is_healthy is False]
    if unhealthy:
        return f"All {len(resources)} resources healthy (matching '{label_selector}')."

    flagged = ", ".join(f"{resource.name} ({resource.phase})" for resource in unhealthy)
    return (
        f"{len(resources)} resources matched, {len(unhealthy)} unhealthy: {flagged} "
        f"(matching '{label_selector}')."
    )


def x_summarize_health__mutmut_6(resources: list[MatchedResourceResult], label_selector: str) -> str:
    if not resources:
        return f"No resources found matching label selector '{label_selector}'."

    unhealthy = [resource for resource in resources if resource.is_healthy is False]
    if not unhealthy:
        return f"All {len(resources)} resources healthy (matching '{label_selector}')."

    flagged = None
    return (
        f"{len(resources)} resources matched, {len(unhealthy)} unhealthy: {flagged} "
        f"(matching '{label_selector}')."
    )


def x_summarize_health__mutmut_7(resources: list[MatchedResourceResult], label_selector: str) -> str:
    if not resources:
        return f"No resources found matching label selector '{label_selector}'."

    unhealthy = [resource for resource in resources if resource.is_healthy is False]
    if not unhealthy:
        return f"All {len(resources)} resources healthy (matching '{label_selector}')."

    flagged = ", ".join(None)
    return (
        f"{len(resources)} resources matched, {len(unhealthy)} unhealthy: {flagged} "
        f"(matching '{label_selector}')."
    )


def x_summarize_health__mutmut_8(resources: list[MatchedResourceResult], label_selector: str) -> str:
    if not resources:
        return f"No resources found matching label selector '{label_selector}'."

    unhealthy = [resource for resource in resources if resource.is_healthy is False]
    if not unhealthy:
        return f"All {len(resources)} resources healthy (matching '{label_selector}')."

    flagged = "XX, XX".join(f"{resource.name} ({resource.phase})" for resource in unhealthy)
    return (
        f"{len(resources)} resources matched, {len(unhealthy)} unhealthy: {flagged} "
        f"(matching '{label_selector}')."
    )

mutants_x_summarize_health__mutmut['_mutmut_orig'] = x_summarize_health__mutmut_orig # type: ignore # mutmut generated
mutants_x_summarize_health__mutmut['x_summarize_health__mutmut_1'] = x_summarize_health__mutmut_1 # type: ignore # mutmut generated
mutants_x_summarize_health__mutmut['x_summarize_health__mutmut_2'] = x_summarize_health__mutmut_2 # type: ignore # mutmut generated
mutants_x_summarize_health__mutmut['x_summarize_health__mutmut_3'] = x_summarize_health__mutmut_3 # type: ignore # mutmut generated
mutants_x_summarize_health__mutmut['x_summarize_health__mutmut_4'] = x_summarize_health__mutmut_4 # type: ignore # mutmut generated
mutants_x_summarize_health__mutmut['x_summarize_health__mutmut_5'] = x_summarize_health__mutmut_5 # type: ignore # mutmut generated
mutants_x_summarize_health__mutmut['x_summarize_health__mutmut_6'] = x_summarize_health__mutmut_6 # type: ignore # mutmut generated
mutants_x_summarize_health__mutmut['x_summarize_health__mutmut_7'] = x_summarize_health__mutmut_7 # type: ignore # mutmut generated
mutants_x_summarize_health__mutmut['x_summarize_health__mutmut_8'] = x_summarize_health__mutmut_8 # type: ignore # mutmut generated
