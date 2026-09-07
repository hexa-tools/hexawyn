"""Pure Cilium bandwidth-manager audit — no infra imports."""

from __future__ import annotations

from hexawyn.domain.models.cilium import (
    CiliumBandwidthAuditResult,
    CiliumBandwidthEntry,
)

_NOT_INSTALLED_NOTE = "Cilium is not installed in this cluster"
_NOT_AVAILABLE_NOTE = "Cilium bandwidth manager is disabled (no bandwidth annotations found)"

_NEAR_LIMIT_THRESHOLD = 0.9


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_build_bandwidth_entry__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_bandwidth_entry__mutmut)
def build_bandwidth_entry(  # noqa: PLR0913
    namespace: str,
    pod: str,
    ingress_limit: str | None,
    egress_limit: str | None,
    usage_ratio: float | None,
    throttled: bool,
) -> CiliumBandwidthEntry:
    """Build one per-pod bandwidth entry with an observed state."""
    return CiliumBandwidthEntry(
        namespace=namespace,
        pod=pod,
        ingress_limit=ingress_limit,
        egress_limit=egress_limit,
        usage_ratio=usage_ratio,
        state=classify_bandwidth(usage_ratio, throttled),
        note=_note_for(usage_ratio, throttled),
    )


def x_build_bandwidth_entry__mutmut_orig(  # noqa: PLR0913
    namespace: str,
    pod: str,
    ingress_limit: str | None,
    egress_limit: str | None,
    usage_ratio: float | None,
    throttled: bool,
) -> CiliumBandwidthEntry:
    """Build one per-pod bandwidth entry with an observed state."""
    return CiliumBandwidthEntry(
        namespace=namespace,
        pod=pod,
        ingress_limit=ingress_limit,
        egress_limit=egress_limit,
        usage_ratio=usage_ratio,
        state=classify_bandwidth(usage_ratio, throttled),
        note=_note_for(usage_ratio, throttled),
    )


def x_build_bandwidth_entry__mutmut_1(  # noqa: PLR0913
    namespace: str,
    pod: str,
    ingress_limit: str | None,
    egress_limit: str | None,
    usage_ratio: float | None,
    throttled: bool,
) -> CiliumBandwidthEntry:
    """Build one per-pod bandwidth entry with an observed state."""
    return CiliumBandwidthEntry(
        namespace=None,
        pod=pod,
        ingress_limit=ingress_limit,
        egress_limit=egress_limit,
        usage_ratio=usage_ratio,
        state=classify_bandwidth(usage_ratio, throttled),
        note=_note_for(usage_ratio, throttled),
    )


def x_build_bandwidth_entry__mutmut_2(  # noqa: PLR0913
    namespace: str,
    pod: str,
    ingress_limit: str | None,
    egress_limit: str | None,
    usage_ratio: float | None,
    throttled: bool,
) -> CiliumBandwidthEntry:
    """Build one per-pod bandwidth entry with an observed state."""
    return CiliumBandwidthEntry(
        namespace=namespace,
        pod=None,
        ingress_limit=ingress_limit,
        egress_limit=egress_limit,
        usage_ratio=usage_ratio,
        state=classify_bandwidth(usage_ratio, throttled),
        note=_note_for(usage_ratio, throttled),
    )


def x_build_bandwidth_entry__mutmut_3(  # noqa: PLR0913
    namespace: str,
    pod: str,
    ingress_limit: str | None,
    egress_limit: str | None,
    usage_ratio: float | None,
    throttled: bool,
) -> CiliumBandwidthEntry:
    """Build one per-pod bandwidth entry with an observed state."""
    return CiliumBandwidthEntry(
        namespace=namespace,
        pod=pod,
        ingress_limit=None,
        egress_limit=egress_limit,
        usage_ratio=usage_ratio,
        state=classify_bandwidth(usage_ratio, throttled),
        note=_note_for(usage_ratio, throttled),
    )


def x_build_bandwidth_entry__mutmut_4(  # noqa: PLR0913
    namespace: str,
    pod: str,
    ingress_limit: str | None,
    egress_limit: str | None,
    usage_ratio: float | None,
    throttled: bool,
) -> CiliumBandwidthEntry:
    """Build one per-pod bandwidth entry with an observed state."""
    return CiliumBandwidthEntry(
        namespace=namespace,
        pod=pod,
        ingress_limit=ingress_limit,
        egress_limit=None,
        usage_ratio=usage_ratio,
        state=classify_bandwidth(usage_ratio, throttled),
        note=_note_for(usage_ratio, throttled),
    )


def x_build_bandwidth_entry__mutmut_5(  # noqa: PLR0913
    namespace: str,
    pod: str,
    ingress_limit: str | None,
    egress_limit: str | None,
    usage_ratio: float | None,
    throttled: bool,
) -> CiliumBandwidthEntry:
    """Build one per-pod bandwidth entry with an observed state."""
    return CiliumBandwidthEntry(
        namespace=namespace,
        pod=pod,
        ingress_limit=ingress_limit,
        egress_limit=egress_limit,
        usage_ratio=None,
        state=classify_bandwidth(usage_ratio, throttled),
        note=_note_for(usage_ratio, throttled),
    )


def x_build_bandwidth_entry__mutmut_6(  # noqa: PLR0913
    namespace: str,
    pod: str,
    ingress_limit: str | None,
    egress_limit: str | None,
    usage_ratio: float | None,
    throttled: bool,
) -> CiliumBandwidthEntry:
    """Build one per-pod bandwidth entry with an observed state."""
    return CiliumBandwidthEntry(
        namespace=namespace,
        pod=pod,
        ingress_limit=ingress_limit,
        egress_limit=egress_limit,
        usage_ratio=usage_ratio,
        state=None,
        note=_note_for(usage_ratio, throttled),
    )


def x_build_bandwidth_entry__mutmut_7(  # noqa: PLR0913
    namespace: str,
    pod: str,
    ingress_limit: str | None,
    egress_limit: str | None,
    usage_ratio: float | None,
    throttled: bool,
) -> CiliumBandwidthEntry:
    """Build one per-pod bandwidth entry with an observed state."""
    return CiliumBandwidthEntry(
        namespace=namespace,
        pod=pod,
        ingress_limit=ingress_limit,
        egress_limit=egress_limit,
        usage_ratio=usage_ratio,
        state=classify_bandwidth(usage_ratio, throttled),
        note=None,
    )


def x_build_bandwidth_entry__mutmut_8(  # noqa: PLR0913
    namespace: str,
    pod: str,
    ingress_limit: str | None,
    egress_limit: str | None,
    usage_ratio: float | None,
    throttled: bool,
) -> CiliumBandwidthEntry:
    """Build one per-pod bandwidth entry with an observed state."""
    return CiliumBandwidthEntry(
        pod=pod,
        ingress_limit=ingress_limit,
        egress_limit=egress_limit,
        usage_ratio=usage_ratio,
        state=classify_bandwidth(usage_ratio, throttled),
        note=_note_for(usage_ratio, throttled),
    )


def x_build_bandwidth_entry__mutmut_9(  # noqa: PLR0913
    namespace: str,
    pod: str,
    ingress_limit: str | None,
    egress_limit: str | None,
    usage_ratio: float | None,
    throttled: bool,
) -> CiliumBandwidthEntry:
    """Build one per-pod bandwidth entry with an observed state."""
    return CiliumBandwidthEntry(
        namespace=namespace,
        ingress_limit=ingress_limit,
        egress_limit=egress_limit,
        usage_ratio=usage_ratio,
        state=classify_bandwidth(usage_ratio, throttled),
        note=_note_for(usage_ratio, throttled),
    )


def x_build_bandwidth_entry__mutmut_10(  # noqa: PLR0913
    namespace: str,
    pod: str,
    ingress_limit: str | None,
    egress_limit: str | None,
    usage_ratio: float | None,
    throttled: bool,
) -> CiliumBandwidthEntry:
    """Build one per-pod bandwidth entry with an observed state."""
    return CiliumBandwidthEntry(
        namespace=namespace,
        pod=pod,
        egress_limit=egress_limit,
        usage_ratio=usage_ratio,
        state=classify_bandwidth(usage_ratio, throttled),
        note=_note_for(usage_ratio, throttled),
    )


def x_build_bandwidth_entry__mutmut_11(  # noqa: PLR0913
    namespace: str,
    pod: str,
    ingress_limit: str | None,
    egress_limit: str | None,
    usage_ratio: float | None,
    throttled: bool,
) -> CiliumBandwidthEntry:
    """Build one per-pod bandwidth entry with an observed state."""
    return CiliumBandwidthEntry(
        namespace=namespace,
        pod=pod,
        ingress_limit=ingress_limit,
        usage_ratio=usage_ratio,
        state=classify_bandwidth(usage_ratio, throttled),
        note=_note_for(usage_ratio, throttled),
    )


def x_build_bandwidth_entry__mutmut_12(  # noqa: PLR0913
    namespace: str,
    pod: str,
    ingress_limit: str | None,
    egress_limit: str | None,
    usage_ratio: float | None,
    throttled: bool,
) -> CiliumBandwidthEntry:
    """Build one per-pod bandwidth entry with an observed state."""
    return CiliumBandwidthEntry(
        namespace=namespace,
        pod=pod,
        ingress_limit=ingress_limit,
        egress_limit=egress_limit,
        state=classify_bandwidth(usage_ratio, throttled),
        note=_note_for(usage_ratio, throttled),
    )


def x_build_bandwidth_entry__mutmut_13(  # noqa: PLR0913
    namespace: str,
    pod: str,
    ingress_limit: str | None,
    egress_limit: str | None,
    usage_ratio: float | None,
    throttled: bool,
) -> CiliumBandwidthEntry:
    """Build one per-pod bandwidth entry with an observed state."""
    return CiliumBandwidthEntry(
        namespace=namespace,
        pod=pod,
        ingress_limit=ingress_limit,
        egress_limit=egress_limit,
        usage_ratio=usage_ratio,
        note=_note_for(usage_ratio, throttled),
    )


def x_build_bandwidth_entry__mutmut_14(  # noqa: PLR0913
    namespace: str,
    pod: str,
    ingress_limit: str | None,
    egress_limit: str | None,
    usage_ratio: float | None,
    throttled: bool,
) -> CiliumBandwidthEntry:
    """Build one per-pod bandwidth entry with an observed state."""
    return CiliumBandwidthEntry(
        namespace=namespace,
        pod=pod,
        ingress_limit=ingress_limit,
        egress_limit=egress_limit,
        usage_ratio=usage_ratio,
        state=classify_bandwidth(usage_ratio, throttled),
        )


def x_build_bandwidth_entry__mutmut_15(  # noqa: PLR0913
    namespace: str,
    pod: str,
    ingress_limit: str | None,
    egress_limit: str | None,
    usage_ratio: float | None,
    throttled: bool,
) -> CiliumBandwidthEntry:
    """Build one per-pod bandwidth entry with an observed state."""
    return CiliumBandwidthEntry(
        namespace=namespace,
        pod=pod,
        ingress_limit=ingress_limit,
        egress_limit=egress_limit,
        usage_ratio=usage_ratio,
        state=classify_bandwidth(None, throttled),
        note=_note_for(usage_ratio, throttled),
    )


def x_build_bandwidth_entry__mutmut_16(  # noqa: PLR0913
    namespace: str,
    pod: str,
    ingress_limit: str | None,
    egress_limit: str | None,
    usage_ratio: float | None,
    throttled: bool,
) -> CiliumBandwidthEntry:
    """Build one per-pod bandwidth entry with an observed state."""
    return CiliumBandwidthEntry(
        namespace=namespace,
        pod=pod,
        ingress_limit=ingress_limit,
        egress_limit=egress_limit,
        usage_ratio=usage_ratio,
        state=classify_bandwidth(usage_ratio, None),
        note=_note_for(usage_ratio, throttled),
    )


def x_build_bandwidth_entry__mutmut_17(  # noqa: PLR0913
    namespace: str,
    pod: str,
    ingress_limit: str | None,
    egress_limit: str | None,
    usage_ratio: float | None,
    throttled: bool,
) -> CiliumBandwidthEntry:
    """Build one per-pod bandwidth entry with an observed state."""
    return CiliumBandwidthEntry(
        namespace=namespace,
        pod=pod,
        ingress_limit=ingress_limit,
        egress_limit=egress_limit,
        usage_ratio=usage_ratio,
        state=classify_bandwidth(throttled),
        note=_note_for(usage_ratio, throttled),
    )


def x_build_bandwidth_entry__mutmut_18(  # noqa: PLR0913
    namespace: str,
    pod: str,
    ingress_limit: str | None,
    egress_limit: str | None,
    usage_ratio: float | None,
    throttled: bool,
) -> CiliumBandwidthEntry:
    """Build one per-pod bandwidth entry with an observed state."""
    return CiliumBandwidthEntry(
        namespace=namespace,
        pod=pod,
        ingress_limit=ingress_limit,
        egress_limit=egress_limit,
        usage_ratio=usage_ratio,
        state=classify_bandwidth(usage_ratio, ),
        note=_note_for(usage_ratio, throttled),
    )


def x_build_bandwidth_entry__mutmut_19(  # noqa: PLR0913
    namespace: str,
    pod: str,
    ingress_limit: str | None,
    egress_limit: str | None,
    usage_ratio: float | None,
    throttled: bool,
) -> CiliumBandwidthEntry:
    """Build one per-pod bandwidth entry with an observed state."""
    return CiliumBandwidthEntry(
        namespace=namespace,
        pod=pod,
        ingress_limit=ingress_limit,
        egress_limit=egress_limit,
        usage_ratio=usage_ratio,
        state=classify_bandwidth(usage_ratio, throttled),
        note=_note_for(None, throttled),
    )


def x_build_bandwidth_entry__mutmut_20(  # noqa: PLR0913
    namespace: str,
    pod: str,
    ingress_limit: str | None,
    egress_limit: str | None,
    usage_ratio: float | None,
    throttled: bool,
) -> CiliumBandwidthEntry:
    """Build one per-pod bandwidth entry with an observed state."""
    return CiliumBandwidthEntry(
        namespace=namespace,
        pod=pod,
        ingress_limit=ingress_limit,
        egress_limit=egress_limit,
        usage_ratio=usage_ratio,
        state=classify_bandwidth(usage_ratio, throttled),
        note=_note_for(usage_ratio, None),
    )


def x_build_bandwidth_entry__mutmut_21(  # noqa: PLR0913
    namespace: str,
    pod: str,
    ingress_limit: str | None,
    egress_limit: str | None,
    usage_ratio: float | None,
    throttled: bool,
) -> CiliumBandwidthEntry:
    """Build one per-pod bandwidth entry with an observed state."""
    return CiliumBandwidthEntry(
        namespace=namespace,
        pod=pod,
        ingress_limit=ingress_limit,
        egress_limit=egress_limit,
        usage_ratio=usage_ratio,
        state=classify_bandwidth(usage_ratio, throttled),
        note=_note_for(throttled),
    )


def x_build_bandwidth_entry__mutmut_22(  # noqa: PLR0913
    namespace: str,
    pod: str,
    ingress_limit: str | None,
    egress_limit: str | None,
    usage_ratio: float | None,
    throttled: bool,
) -> CiliumBandwidthEntry:
    """Build one per-pod bandwidth entry with an observed state."""
    return CiliumBandwidthEntry(
        namespace=namespace,
        pod=pod,
        ingress_limit=ingress_limit,
        egress_limit=egress_limit,
        usage_ratio=usage_ratio,
        state=classify_bandwidth(usage_ratio, throttled),
        note=_note_for(usage_ratio, ),
    )

mutants_x_build_bandwidth_entry__mutmut['_mutmut_orig'] = x_build_bandwidth_entry__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_bandwidth_entry__mutmut['x_build_bandwidth_entry__mutmut_1'] = x_build_bandwidth_entry__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_bandwidth_entry__mutmut['x_build_bandwidth_entry__mutmut_2'] = x_build_bandwidth_entry__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_bandwidth_entry__mutmut['x_build_bandwidth_entry__mutmut_3'] = x_build_bandwidth_entry__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_bandwidth_entry__mutmut['x_build_bandwidth_entry__mutmut_4'] = x_build_bandwidth_entry__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_bandwidth_entry__mutmut['x_build_bandwidth_entry__mutmut_5'] = x_build_bandwidth_entry__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_bandwidth_entry__mutmut['x_build_bandwidth_entry__mutmut_6'] = x_build_bandwidth_entry__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_bandwidth_entry__mutmut['x_build_bandwidth_entry__mutmut_7'] = x_build_bandwidth_entry__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_bandwidth_entry__mutmut['x_build_bandwidth_entry__mutmut_8'] = x_build_bandwidth_entry__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_bandwidth_entry__mutmut['x_build_bandwidth_entry__mutmut_9'] = x_build_bandwidth_entry__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_bandwidth_entry__mutmut['x_build_bandwidth_entry__mutmut_10'] = x_build_bandwidth_entry__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_bandwidth_entry__mutmut['x_build_bandwidth_entry__mutmut_11'] = x_build_bandwidth_entry__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_bandwidth_entry__mutmut['x_build_bandwidth_entry__mutmut_12'] = x_build_bandwidth_entry__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_bandwidth_entry__mutmut['x_build_bandwidth_entry__mutmut_13'] = x_build_bandwidth_entry__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_bandwidth_entry__mutmut['x_build_bandwidth_entry__mutmut_14'] = x_build_bandwidth_entry__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_bandwidth_entry__mutmut['x_build_bandwidth_entry__mutmut_15'] = x_build_bandwidth_entry__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_bandwidth_entry__mutmut['x_build_bandwidth_entry__mutmut_16'] = x_build_bandwidth_entry__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_bandwidth_entry__mutmut['x_build_bandwidth_entry__mutmut_17'] = x_build_bandwidth_entry__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_bandwidth_entry__mutmut['x_build_bandwidth_entry__mutmut_18'] = x_build_bandwidth_entry__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_bandwidth_entry__mutmut['x_build_bandwidth_entry__mutmut_19'] = x_build_bandwidth_entry__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_bandwidth_entry__mutmut['x_build_bandwidth_entry__mutmut_20'] = x_build_bandwidth_entry__mutmut_20 # type: ignore # mutmut generated
mutants_x_build_bandwidth_entry__mutmut['x_build_bandwidth_entry__mutmut_21'] = x_build_bandwidth_entry__mutmut_21 # type: ignore # mutmut generated
mutants_x_build_bandwidth_entry__mutmut['x_build_bandwidth_entry__mutmut_22'] = x_build_bandwidth_entry__mutmut_22 # type: ignore # mutmut generated
mutants_x_classify_bandwidth__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_classify_bandwidth__mutmut)
def classify_bandwidth(usage_ratio: float | None, throttled: bool) -> str:
    """Classify a pod's bandwidth state from observed inputs."""
    if throttled:
        return "throttled"
    if usage_ratio is not None and usage_ratio >= _NEAR_LIMIT_THRESHOLD:
        return "near_limit"
    if usage_ratio is not None:
        return "ok"
    return "UNKNOWN"


def x_classify_bandwidth__mutmut_orig(usage_ratio: float | None, throttled: bool) -> str:
    """Classify a pod's bandwidth state from observed inputs."""
    if throttled:
        return "throttled"
    if usage_ratio is not None and usage_ratio >= _NEAR_LIMIT_THRESHOLD:
        return "near_limit"
    if usage_ratio is not None:
        return "ok"
    return "UNKNOWN"


def x_classify_bandwidth__mutmut_1(usage_ratio: float | None, throttled: bool) -> str:
    """Classify a pod's bandwidth state from observed inputs."""
    if throttled:
        return "XXthrottledXX"
    if usage_ratio is not None and usage_ratio >= _NEAR_LIMIT_THRESHOLD:
        return "near_limit"
    if usage_ratio is not None:
        return "ok"
    return "UNKNOWN"


def x_classify_bandwidth__mutmut_2(usage_ratio: float | None, throttled: bool) -> str:
    """Classify a pod's bandwidth state from observed inputs."""
    if throttled:
        return "THROTTLED"
    if usage_ratio is not None and usage_ratio >= _NEAR_LIMIT_THRESHOLD:
        return "near_limit"
    if usage_ratio is not None:
        return "ok"
    return "UNKNOWN"


def x_classify_bandwidth__mutmut_3(usage_ratio: float | None, throttled: bool) -> str:
    """Classify a pod's bandwidth state from observed inputs."""
    if throttled:
        return "throttled"
    if usage_ratio is not None or usage_ratio >= _NEAR_LIMIT_THRESHOLD:
        return "near_limit"
    if usage_ratio is not None:
        return "ok"
    return "UNKNOWN"


def x_classify_bandwidth__mutmut_4(usage_ratio: float | None, throttled: bool) -> str:
    """Classify a pod's bandwidth state from observed inputs."""
    if throttled:
        return "throttled"
    if usage_ratio is None and usage_ratio >= _NEAR_LIMIT_THRESHOLD:
        return "near_limit"
    if usage_ratio is not None:
        return "ok"
    return "UNKNOWN"


def x_classify_bandwidth__mutmut_5(usage_ratio: float | None, throttled: bool) -> str:
    """Classify a pod's bandwidth state from observed inputs."""
    if throttled:
        return "throttled"
    if usage_ratio is not None and usage_ratio > _NEAR_LIMIT_THRESHOLD:
        return "near_limit"
    if usage_ratio is not None:
        return "ok"
    return "UNKNOWN"


def x_classify_bandwidth__mutmut_6(usage_ratio: float | None, throttled: bool) -> str:
    """Classify a pod's bandwidth state from observed inputs."""
    if throttled:
        return "throttled"
    if usage_ratio is not None and usage_ratio >= _NEAR_LIMIT_THRESHOLD:
        return "XXnear_limitXX"
    if usage_ratio is not None:
        return "ok"
    return "UNKNOWN"


def x_classify_bandwidth__mutmut_7(usage_ratio: float | None, throttled: bool) -> str:
    """Classify a pod's bandwidth state from observed inputs."""
    if throttled:
        return "throttled"
    if usage_ratio is not None and usage_ratio >= _NEAR_LIMIT_THRESHOLD:
        return "NEAR_LIMIT"
    if usage_ratio is not None:
        return "ok"
    return "UNKNOWN"


def x_classify_bandwidth__mutmut_8(usage_ratio: float | None, throttled: bool) -> str:
    """Classify a pod's bandwidth state from observed inputs."""
    if throttled:
        return "throttled"
    if usage_ratio is not None and usage_ratio >= _NEAR_LIMIT_THRESHOLD:
        return "near_limit"
    if usage_ratio is None:
        return "ok"
    return "UNKNOWN"


def x_classify_bandwidth__mutmut_9(usage_ratio: float | None, throttled: bool) -> str:
    """Classify a pod's bandwidth state from observed inputs."""
    if throttled:
        return "throttled"
    if usage_ratio is not None and usage_ratio >= _NEAR_LIMIT_THRESHOLD:
        return "near_limit"
    if usage_ratio is not None:
        return "XXokXX"
    return "UNKNOWN"


def x_classify_bandwidth__mutmut_10(usage_ratio: float | None, throttled: bool) -> str:
    """Classify a pod's bandwidth state from observed inputs."""
    if throttled:
        return "throttled"
    if usage_ratio is not None and usage_ratio >= _NEAR_LIMIT_THRESHOLD:
        return "near_limit"
    if usage_ratio is not None:
        return "OK"
    return "UNKNOWN"


def x_classify_bandwidth__mutmut_11(usage_ratio: float | None, throttled: bool) -> str:
    """Classify a pod's bandwidth state from observed inputs."""
    if throttled:
        return "throttled"
    if usage_ratio is not None and usage_ratio >= _NEAR_LIMIT_THRESHOLD:
        return "near_limit"
    if usage_ratio is not None:
        return "ok"
    return "XXUNKNOWNXX"


def x_classify_bandwidth__mutmut_12(usage_ratio: float | None, throttled: bool) -> str:
    """Classify a pod's bandwidth state from observed inputs."""
    if throttled:
        return "throttled"
    if usage_ratio is not None and usage_ratio >= _NEAR_LIMIT_THRESHOLD:
        return "near_limit"
    if usage_ratio is not None:
        return "ok"
    return "unknown"

mutants_x_classify_bandwidth__mutmut['_mutmut_orig'] = x_classify_bandwidth__mutmut_orig # type: ignore # mutmut generated
mutants_x_classify_bandwidth__mutmut['x_classify_bandwidth__mutmut_1'] = x_classify_bandwidth__mutmut_1 # type: ignore # mutmut generated
mutants_x_classify_bandwidth__mutmut['x_classify_bandwidth__mutmut_2'] = x_classify_bandwidth__mutmut_2 # type: ignore # mutmut generated
mutants_x_classify_bandwidth__mutmut['x_classify_bandwidth__mutmut_3'] = x_classify_bandwidth__mutmut_3 # type: ignore # mutmut generated
mutants_x_classify_bandwidth__mutmut['x_classify_bandwidth__mutmut_4'] = x_classify_bandwidth__mutmut_4 # type: ignore # mutmut generated
mutants_x_classify_bandwidth__mutmut['x_classify_bandwidth__mutmut_5'] = x_classify_bandwidth__mutmut_5 # type: ignore # mutmut generated
mutants_x_classify_bandwidth__mutmut['x_classify_bandwidth__mutmut_6'] = x_classify_bandwidth__mutmut_6 # type: ignore # mutmut generated
mutants_x_classify_bandwidth__mutmut['x_classify_bandwidth__mutmut_7'] = x_classify_bandwidth__mutmut_7 # type: ignore # mutmut generated
mutants_x_classify_bandwidth__mutmut['x_classify_bandwidth__mutmut_8'] = x_classify_bandwidth__mutmut_8 # type: ignore # mutmut generated
mutants_x_classify_bandwidth__mutmut['x_classify_bandwidth__mutmut_9'] = x_classify_bandwidth__mutmut_9 # type: ignore # mutmut generated
mutants_x_classify_bandwidth__mutmut['x_classify_bandwidth__mutmut_10'] = x_classify_bandwidth__mutmut_10 # type: ignore # mutmut generated
mutants_x_classify_bandwidth__mutmut['x_classify_bandwidth__mutmut_11'] = x_classify_bandwidth__mutmut_11 # type: ignore # mutmut generated
mutants_x_classify_bandwidth__mutmut['x_classify_bandwidth__mutmut_12'] = x_classify_bandwidth__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_bandwidth_audit__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_bandwidth_audit__mutmut)
def build_bandwidth_audit(entries: list[CiliumBandwidthEntry]) -> CiliumBandwidthAuditResult:
    """Wrap the entries with an overall status, anomalies first."""
    anomalies = [entry for entry in entries if entry.state in ("throttled", "near_limit")]
    ordered = [*anomalies, *[entry for entry in entries if entry not in anomalies]]
    return CiliumBandwidthAuditResult(
        installed=True,
        status="anomalies" if anomalies else "ok",
        total_pods=len(entries),
        entries=ordered,
        note=None,
    )


def x_build_bandwidth_audit__mutmut_orig(entries: list[CiliumBandwidthEntry]) -> CiliumBandwidthAuditResult:
    """Wrap the entries with an overall status, anomalies first."""
    anomalies = [entry for entry in entries if entry.state in ("throttled", "near_limit")]
    ordered = [*anomalies, *[entry for entry in entries if entry not in anomalies]]
    return CiliumBandwidthAuditResult(
        installed=True,
        status="anomalies" if anomalies else "ok",
        total_pods=len(entries),
        entries=ordered,
        note=None,
    )


def x_build_bandwidth_audit__mutmut_1(entries: list[CiliumBandwidthEntry]) -> CiliumBandwidthAuditResult:
    """Wrap the entries with an overall status, anomalies first."""
    anomalies = None
    ordered = [*anomalies, *[entry for entry in entries if entry not in anomalies]]
    return CiliumBandwidthAuditResult(
        installed=True,
        status="anomalies" if anomalies else "ok",
        total_pods=len(entries),
        entries=ordered,
        note=None,
    )


def x_build_bandwidth_audit__mutmut_2(entries: list[CiliumBandwidthEntry]) -> CiliumBandwidthAuditResult:
    """Wrap the entries with an overall status, anomalies first."""
    anomalies = [entry for entry in entries if entry.state not in ("throttled", "near_limit")]
    ordered = [*anomalies, *[entry for entry in entries if entry not in anomalies]]
    return CiliumBandwidthAuditResult(
        installed=True,
        status="anomalies" if anomalies else "ok",
        total_pods=len(entries),
        entries=ordered,
        note=None,
    )


def x_build_bandwidth_audit__mutmut_3(entries: list[CiliumBandwidthEntry]) -> CiliumBandwidthAuditResult:
    """Wrap the entries with an overall status, anomalies first."""
    anomalies = [entry for entry in entries if entry.state in ("XXthrottledXX", "near_limit")]
    ordered = [*anomalies, *[entry for entry in entries if entry not in anomalies]]
    return CiliumBandwidthAuditResult(
        installed=True,
        status="anomalies" if anomalies else "ok",
        total_pods=len(entries),
        entries=ordered,
        note=None,
    )


def x_build_bandwidth_audit__mutmut_4(entries: list[CiliumBandwidthEntry]) -> CiliumBandwidthAuditResult:
    """Wrap the entries with an overall status, anomalies first."""
    anomalies = [entry for entry in entries if entry.state in ("THROTTLED", "near_limit")]
    ordered = [*anomalies, *[entry for entry in entries if entry not in anomalies]]
    return CiliumBandwidthAuditResult(
        installed=True,
        status="anomalies" if anomalies else "ok",
        total_pods=len(entries),
        entries=ordered,
        note=None,
    )


def x_build_bandwidth_audit__mutmut_5(entries: list[CiliumBandwidthEntry]) -> CiliumBandwidthAuditResult:
    """Wrap the entries with an overall status, anomalies first."""
    anomalies = [entry for entry in entries if entry.state in ("throttled", "XXnear_limitXX")]
    ordered = [*anomalies, *[entry for entry in entries if entry not in anomalies]]
    return CiliumBandwidthAuditResult(
        installed=True,
        status="anomalies" if anomalies else "ok",
        total_pods=len(entries),
        entries=ordered,
        note=None,
    )


def x_build_bandwidth_audit__mutmut_6(entries: list[CiliumBandwidthEntry]) -> CiliumBandwidthAuditResult:
    """Wrap the entries with an overall status, anomalies first."""
    anomalies = [entry for entry in entries if entry.state in ("throttled", "NEAR_LIMIT")]
    ordered = [*anomalies, *[entry for entry in entries if entry not in anomalies]]
    return CiliumBandwidthAuditResult(
        installed=True,
        status="anomalies" if anomalies else "ok",
        total_pods=len(entries),
        entries=ordered,
        note=None,
    )


def x_build_bandwidth_audit__mutmut_7(entries: list[CiliumBandwidthEntry]) -> CiliumBandwidthAuditResult:
    """Wrap the entries with an overall status, anomalies first."""
    anomalies = [entry for entry in entries if entry.state in ("throttled", "near_limit")]
    ordered = None
    return CiliumBandwidthAuditResult(
        installed=True,
        status="anomalies" if anomalies else "ok",
        total_pods=len(entries),
        entries=ordered,
        note=None,
    )


def x_build_bandwidth_audit__mutmut_8(entries: list[CiliumBandwidthEntry]) -> CiliumBandwidthAuditResult:
    """Wrap the entries with an overall status, anomalies first."""
    anomalies = [entry for entry in entries if entry.state in ("throttled", "near_limit")]
    ordered = [*anomalies, *[entry for entry in entries if entry in anomalies]]
    return CiliumBandwidthAuditResult(
        installed=True,
        status="anomalies" if anomalies else "ok",
        total_pods=len(entries),
        entries=ordered,
        note=None,
    )


def x_build_bandwidth_audit__mutmut_9(entries: list[CiliumBandwidthEntry]) -> CiliumBandwidthAuditResult:
    """Wrap the entries with an overall status, anomalies first."""
    anomalies = [entry for entry in entries if entry.state in ("throttled", "near_limit")]
    ordered = [*anomalies, *[entry for entry in entries if entry not in anomalies]]
    return CiliumBandwidthAuditResult(
        installed=None,
        status="anomalies" if anomalies else "ok",
        total_pods=len(entries),
        entries=ordered,
        note=None,
    )


def x_build_bandwidth_audit__mutmut_10(entries: list[CiliumBandwidthEntry]) -> CiliumBandwidthAuditResult:
    """Wrap the entries with an overall status, anomalies first."""
    anomalies = [entry for entry in entries if entry.state in ("throttled", "near_limit")]
    ordered = [*anomalies, *[entry for entry in entries if entry not in anomalies]]
    return CiliumBandwidthAuditResult(
        installed=True,
        status=None,
        total_pods=len(entries),
        entries=ordered,
        note=None,
    )


def x_build_bandwidth_audit__mutmut_11(entries: list[CiliumBandwidthEntry]) -> CiliumBandwidthAuditResult:
    """Wrap the entries with an overall status, anomalies first."""
    anomalies = [entry for entry in entries if entry.state in ("throttled", "near_limit")]
    ordered = [*anomalies, *[entry for entry in entries if entry not in anomalies]]
    return CiliumBandwidthAuditResult(
        installed=True,
        status="anomalies" if anomalies else "ok",
        total_pods=None,
        entries=ordered,
        note=None,
    )


def x_build_bandwidth_audit__mutmut_12(entries: list[CiliumBandwidthEntry]) -> CiliumBandwidthAuditResult:
    """Wrap the entries with an overall status, anomalies first."""
    anomalies = [entry for entry in entries if entry.state in ("throttled", "near_limit")]
    ordered = [*anomalies, *[entry for entry in entries if entry not in anomalies]]
    return CiliumBandwidthAuditResult(
        installed=True,
        status="anomalies" if anomalies else "ok",
        total_pods=len(entries),
        entries=None,
        note=None,
    )


def x_build_bandwidth_audit__mutmut_13(entries: list[CiliumBandwidthEntry]) -> CiliumBandwidthAuditResult:
    """Wrap the entries with an overall status, anomalies first."""
    anomalies = [entry for entry in entries if entry.state in ("throttled", "near_limit")]
    ordered = [*anomalies, *[entry for entry in entries if entry not in anomalies]]
    return CiliumBandwidthAuditResult(
        status="anomalies" if anomalies else "ok",
        total_pods=len(entries),
        entries=ordered,
        note=None,
    )


def x_build_bandwidth_audit__mutmut_14(entries: list[CiliumBandwidthEntry]) -> CiliumBandwidthAuditResult:
    """Wrap the entries with an overall status, anomalies first."""
    anomalies = [entry for entry in entries if entry.state in ("throttled", "near_limit")]
    ordered = [*anomalies, *[entry for entry in entries if entry not in anomalies]]
    return CiliumBandwidthAuditResult(
        installed=True,
        total_pods=len(entries),
        entries=ordered,
        note=None,
    )


def x_build_bandwidth_audit__mutmut_15(entries: list[CiliumBandwidthEntry]) -> CiliumBandwidthAuditResult:
    """Wrap the entries with an overall status, anomalies first."""
    anomalies = [entry for entry in entries if entry.state in ("throttled", "near_limit")]
    ordered = [*anomalies, *[entry for entry in entries if entry not in anomalies]]
    return CiliumBandwidthAuditResult(
        installed=True,
        status="anomalies" if anomalies else "ok",
        entries=ordered,
        note=None,
    )


def x_build_bandwidth_audit__mutmut_16(entries: list[CiliumBandwidthEntry]) -> CiliumBandwidthAuditResult:
    """Wrap the entries with an overall status, anomalies first."""
    anomalies = [entry for entry in entries if entry.state in ("throttled", "near_limit")]
    ordered = [*anomalies, *[entry for entry in entries if entry not in anomalies]]
    return CiliumBandwidthAuditResult(
        installed=True,
        status="anomalies" if anomalies else "ok",
        total_pods=len(entries),
        note=None,
    )


def x_build_bandwidth_audit__mutmut_17(entries: list[CiliumBandwidthEntry]) -> CiliumBandwidthAuditResult:
    """Wrap the entries with an overall status, anomalies first."""
    anomalies = [entry for entry in entries if entry.state in ("throttled", "near_limit")]
    ordered = [*anomalies, *[entry for entry in entries if entry not in anomalies]]
    return CiliumBandwidthAuditResult(
        installed=True,
        status="anomalies" if anomalies else "ok",
        total_pods=len(entries),
        entries=ordered,
        )


def x_build_bandwidth_audit__mutmut_18(entries: list[CiliumBandwidthEntry]) -> CiliumBandwidthAuditResult:
    """Wrap the entries with an overall status, anomalies first."""
    anomalies = [entry for entry in entries if entry.state in ("throttled", "near_limit")]
    ordered = [*anomalies, *[entry for entry in entries if entry not in anomalies]]
    return CiliumBandwidthAuditResult(
        installed=False,
        status="anomalies" if anomalies else "ok",
        total_pods=len(entries),
        entries=ordered,
        note=None,
    )


def x_build_bandwidth_audit__mutmut_19(entries: list[CiliumBandwidthEntry]) -> CiliumBandwidthAuditResult:
    """Wrap the entries with an overall status, anomalies first."""
    anomalies = [entry for entry in entries if entry.state in ("throttled", "near_limit")]
    ordered = [*anomalies, *[entry for entry in entries if entry not in anomalies]]
    return CiliumBandwidthAuditResult(
        installed=True,
        status="XXanomaliesXX" if anomalies else "ok",
        total_pods=len(entries),
        entries=ordered,
        note=None,
    )


def x_build_bandwidth_audit__mutmut_20(entries: list[CiliumBandwidthEntry]) -> CiliumBandwidthAuditResult:
    """Wrap the entries with an overall status, anomalies first."""
    anomalies = [entry for entry in entries if entry.state in ("throttled", "near_limit")]
    ordered = [*anomalies, *[entry for entry in entries if entry not in anomalies]]
    return CiliumBandwidthAuditResult(
        installed=True,
        status="ANOMALIES" if anomalies else "ok",
        total_pods=len(entries),
        entries=ordered,
        note=None,
    )


def x_build_bandwidth_audit__mutmut_21(entries: list[CiliumBandwidthEntry]) -> CiliumBandwidthAuditResult:
    """Wrap the entries with an overall status, anomalies first."""
    anomalies = [entry for entry in entries if entry.state in ("throttled", "near_limit")]
    ordered = [*anomalies, *[entry for entry in entries if entry not in anomalies]]
    return CiliumBandwidthAuditResult(
        installed=True,
        status="anomalies" if anomalies else "XXokXX",
        total_pods=len(entries),
        entries=ordered,
        note=None,
    )


def x_build_bandwidth_audit__mutmut_22(entries: list[CiliumBandwidthEntry]) -> CiliumBandwidthAuditResult:
    """Wrap the entries with an overall status, anomalies first."""
    anomalies = [entry for entry in entries if entry.state in ("throttled", "near_limit")]
    ordered = [*anomalies, *[entry for entry in entries if entry not in anomalies]]
    return CiliumBandwidthAuditResult(
        installed=True,
        status="anomalies" if anomalies else "OK",
        total_pods=len(entries),
        entries=ordered,
        note=None,
    )

mutants_x_build_bandwidth_audit__mutmut['_mutmut_orig'] = x_build_bandwidth_audit__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_bandwidth_audit__mutmut['x_build_bandwidth_audit__mutmut_1'] = x_build_bandwidth_audit__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_bandwidth_audit__mutmut['x_build_bandwidth_audit__mutmut_2'] = x_build_bandwidth_audit__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_bandwidth_audit__mutmut['x_build_bandwidth_audit__mutmut_3'] = x_build_bandwidth_audit__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_bandwidth_audit__mutmut['x_build_bandwidth_audit__mutmut_4'] = x_build_bandwidth_audit__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_bandwidth_audit__mutmut['x_build_bandwidth_audit__mutmut_5'] = x_build_bandwidth_audit__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_bandwidth_audit__mutmut['x_build_bandwidth_audit__mutmut_6'] = x_build_bandwidth_audit__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_bandwidth_audit__mutmut['x_build_bandwidth_audit__mutmut_7'] = x_build_bandwidth_audit__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_bandwidth_audit__mutmut['x_build_bandwidth_audit__mutmut_8'] = x_build_bandwidth_audit__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_bandwidth_audit__mutmut['x_build_bandwidth_audit__mutmut_9'] = x_build_bandwidth_audit__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_bandwidth_audit__mutmut['x_build_bandwidth_audit__mutmut_10'] = x_build_bandwidth_audit__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_bandwidth_audit__mutmut['x_build_bandwidth_audit__mutmut_11'] = x_build_bandwidth_audit__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_bandwidth_audit__mutmut['x_build_bandwidth_audit__mutmut_12'] = x_build_bandwidth_audit__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_bandwidth_audit__mutmut['x_build_bandwidth_audit__mutmut_13'] = x_build_bandwidth_audit__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_bandwidth_audit__mutmut['x_build_bandwidth_audit__mutmut_14'] = x_build_bandwidth_audit__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_bandwidth_audit__mutmut['x_build_bandwidth_audit__mutmut_15'] = x_build_bandwidth_audit__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_bandwidth_audit__mutmut['x_build_bandwidth_audit__mutmut_16'] = x_build_bandwidth_audit__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_bandwidth_audit__mutmut['x_build_bandwidth_audit__mutmut_17'] = x_build_bandwidth_audit__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_bandwidth_audit__mutmut['x_build_bandwidth_audit__mutmut_18'] = x_build_bandwidth_audit__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_bandwidth_audit__mutmut['x_build_bandwidth_audit__mutmut_19'] = x_build_bandwidth_audit__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_bandwidth_audit__mutmut['x_build_bandwidth_audit__mutmut_20'] = x_build_bandwidth_audit__mutmut_20 # type: ignore # mutmut generated
mutants_x_build_bandwidth_audit__mutmut['x_build_bandwidth_audit__mutmut_21'] = x_build_bandwidth_audit__mutmut_21 # type: ignore # mutmut generated
mutants_x_build_bandwidth_audit__mutmut['x_build_bandwidth_audit__mutmut_22'] = x_build_bandwidth_audit__mutmut_22 # type: ignore # mutmut generated
mutants_x_not_installed_bandwidth_audit__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_not_installed_bandwidth_audit__mutmut)
def not_installed_bandwidth_audit() -> CiliumBandwidthAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated bandwidth data."""
    return CiliumBandwidthAuditResult(
        installed=False,
        status="not_installed",
        total_pods=0,
        entries=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_bandwidth_audit__mutmut_orig() -> CiliumBandwidthAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated bandwidth data."""
    return CiliumBandwidthAuditResult(
        installed=False,
        status="not_installed",
        total_pods=0,
        entries=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_bandwidth_audit__mutmut_1() -> CiliumBandwidthAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated bandwidth data."""
    return CiliumBandwidthAuditResult(
        installed=None,
        status="not_installed",
        total_pods=0,
        entries=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_bandwidth_audit__mutmut_2() -> CiliumBandwidthAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated bandwidth data."""
    return CiliumBandwidthAuditResult(
        installed=False,
        status=None,
        total_pods=0,
        entries=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_bandwidth_audit__mutmut_3() -> CiliumBandwidthAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated bandwidth data."""
    return CiliumBandwidthAuditResult(
        installed=False,
        status="not_installed",
        total_pods=None,
        entries=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_bandwidth_audit__mutmut_4() -> CiliumBandwidthAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated bandwidth data."""
    return CiliumBandwidthAuditResult(
        installed=False,
        status="not_installed",
        total_pods=0,
        entries=None,
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_bandwidth_audit__mutmut_5() -> CiliumBandwidthAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated bandwidth data."""
    return CiliumBandwidthAuditResult(
        installed=False,
        status="not_installed",
        total_pods=0,
        entries=[],
        note=None,
    )


def x_not_installed_bandwidth_audit__mutmut_6() -> CiliumBandwidthAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated bandwidth data."""
    return CiliumBandwidthAuditResult(
        status="not_installed",
        total_pods=0,
        entries=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_bandwidth_audit__mutmut_7() -> CiliumBandwidthAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated bandwidth data."""
    return CiliumBandwidthAuditResult(
        installed=False,
        total_pods=0,
        entries=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_bandwidth_audit__mutmut_8() -> CiliumBandwidthAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated bandwidth data."""
    return CiliumBandwidthAuditResult(
        installed=False,
        status="not_installed",
        entries=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_bandwidth_audit__mutmut_9() -> CiliumBandwidthAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated bandwidth data."""
    return CiliumBandwidthAuditResult(
        installed=False,
        status="not_installed",
        total_pods=0,
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_bandwidth_audit__mutmut_10() -> CiliumBandwidthAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated bandwidth data."""
    return CiliumBandwidthAuditResult(
        installed=False,
        status="not_installed",
        total_pods=0,
        entries=[],
        )


def x_not_installed_bandwidth_audit__mutmut_11() -> CiliumBandwidthAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated bandwidth data."""
    return CiliumBandwidthAuditResult(
        installed=True,
        status="not_installed",
        total_pods=0,
        entries=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_bandwidth_audit__mutmut_12() -> CiliumBandwidthAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated bandwidth data."""
    return CiliumBandwidthAuditResult(
        installed=False,
        status="XXnot_installedXX",
        total_pods=0,
        entries=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_bandwidth_audit__mutmut_13() -> CiliumBandwidthAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated bandwidth data."""
    return CiliumBandwidthAuditResult(
        installed=False,
        status="NOT_INSTALLED",
        total_pods=0,
        entries=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_bandwidth_audit__mutmut_14() -> CiliumBandwidthAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated bandwidth data."""
    return CiliumBandwidthAuditResult(
        installed=False,
        status="not_installed",
        total_pods=1,
        entries=[],
        note=_NOT_INSTALLED_NOTE,
    )

mutants_x_not_installed_bandwidth_audit__mutmut['_mutmut_orig'] = x_not_installed_bandwidth_audit__mutmut_orig # type: ignore # mutmut generated
mutants_x_not_installed_bandwidth_audit__mutmut['x_not_installed_bandwidth_audit__mutmut_1'] = x_not_installed_bandwidth_audit__mutmut_1 # type: ignore # mutmut generated
mutants_x_not_installed_bandwidth_audit__mutmut['x_not_installed_bandwidth_audit__mutmut_2'] = x_not_installed_bandwidth_audit__mutmut_2 # type: ignore # mutmut generated
mutants_x_not_installed_bandwidth_audit__mutmut['x_not_installed_bandwidth_audit__mutmut_3'] = x_not_installed_bandwidth_audit__mutmut_3 # type: ignore # mutmut generated
mutants_x_not_installed_bandwidth_audit__mutmut['x_not_installed_bandwidth_audit__mutmut_4'] = x_not_installed_bandwidth_audit__mutmut_4 # type: ignore # mutmut generated
mutants_x_not_installed_bandwidth_audit__mutmut['x_not_installed_bandwidth_audit__mutmut_5'] = x_not_installed_bandwidth_audit__mutmut_5 # type: ignore # mutmut generated
mutants_x_not_installed_bandwidth_audit__mutmut['x_not_installed_bandwidth_audit__mutmut_6'] = x_not_installed_bandwidth_audit__mutmut_6 # type: ignore # mutmut generated
mutants_x_not_installed_bandwidth_audit__mutmut['x_not_installed_bandwidth_audit__mutmut_7'] = x_not_installed_bandwidth_audit__mutmut_7 # type: ignore # mutmut generated
mutants_x_not_installed_bandwidth_audit__mutmut['x_not_installed_bandwidth_audit__mutmut_8'] = x_not_installed_bandwidth_audit__mutmut_8 # type: ignore # mutmut generated
mutants_x_not_installed_bandwidth_audit__mutmut['x_not_installed_bandwidth_audit__mutmut_9'] = x_not_installed_bandwidth_audit__mutmut_9 # type: ignore # mutmut generated
mutants_x_not_installed_bandwidth_audit__mutmut['x_not_installed_bandwidth_audit__mutmut_10'] = x_not_installed_bandwidth_audit__mutmut_10 # type: ignore # mutmut generated
mutants_x_not_installed_bandwidth_audit__mutmut['x_not_installed_bandwidth_audit__mutmut_11'] = x_not_installed_bandwidth_audit__mutmut_11 # type: ignore # mutmut generated
mutants_x_not_installed_bandwidth_audit__mutmut['x_not_installed_bandwidth_audit__mutmut_12'] = x_not_installed_bandwidth_audit__mutmut_12 # type: ignore # mutmut generated
mutants_x_not_installed_bandwidth_audit__mutmut['x_not_installed_bandwidth_audit__mutmut_13'] = x_not_installed_bandwidth_audit__mutmut_13 # type: ignore # mutmut generated
mutants_x_not_installed_bandwidth_audit__mutmut['x_not_installed_bandwidth_audit__mutmut_14'] = x_not_installed_bandwidth_audit__mutmut_14 # type: ignore # mutmut generated
mutants_x_not_available_bandwidth_audit__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_not_available_bandwidth_audit__mutmut)
def not_available_bandwidth_audit() -> CiliumBandwidthAuditResult:
    """Bandwidth manager enabled on Cilium but no bandwidth annotations found."""
    return CiliumBandwidthAuditResult(
        installed=True,
        status="not_available",
        total_pods=0,
        entries=[],
        note=_NOT_AVAILABLE_NOTE,
    )


def x_not_available_bandwidth_audit__mutmut_orig() -> CiliumBandwidthAuditResult:
    """Bandwidth manager enabled on Cilium but no bandwidth annotations found."""
    return CiliumBandwidthAuditResult(
        installed=True,
        status="not_available",
        total_pods=0,
        entries=[],
        note=_NOT_AVAILABLE_NOTE,
    )


def x_not_available_bandwidth_audit__mutmut_1() -> CiliumBandwidthAuditResult:
    """Bandwidth manager enabled on Cilium but no bandwidth annotations found."""
    return CiliumBandwidthAuditResult(
        installed=None,
        status="not_available",
        total_pods=0,
        entries=[],
        note=_NOT_AVAILABLE_NOTE,
    )


def x_not_available_bandwidth_audit__mutmut_2() -> CiliumBandwidthAuditResult:
    """Bandwidth manager enabled on Cilium but no bandwidth annotations found."""
    return CiliumBandwidthAuditResult(
        installed=True,
        status=None,
        total_pods=0,
        entries=[],
        note=_NOT_AVAILABLE_NOTE,
    )


def x_not_available_bandwidth_audit__mutmut_3() -> CiliumBandwidthAuditResult:
    """Bandwidth manager enabled on Cilium but no bandwidth annotations found."""
    return CiliumBandwidthAuditResult(
        installed=True,
        status="not_available",
        total_pods=None,
        entries=[],
        note=_NOT_AVAILABLE_NOTE,
    )


def x_not_available_bandwidth_audit__mutmut_4() -> CiliumBandwidthAuditResult:
    """Bandwidth manager enabled on Cilium but no bandwidth annotations found."""
    return CiliumBandwidthAuditResult(
        installed=True,
        status="not_available",
        total_pods=0,
        entries=None,
        note=_NOT_AVAILABLE_NOTE,
    )


def x_not_available_bandwidth_audit__mutmut_5() -> CiliumBandwidthAuditResult:
    """Bandwidth manager enabled on Cilium but no bandwidth annotations found."""
    return CiliumBandwidthAuditResult(
        installed=True,
        status="not_available",
        total_pods=0,
        entries=[],
        note=None,
    )


def x_not_available_bandwidth_audit__mutmut_6() -> CiliumBandwidthAuditResult:
    """Bandwidth manager enabled on Cilium but no bandwidth annotations found."""
    return CiliumBandwidthAuditResult(
        status="not_available",
        total_pods=0,
        entries=[],
        note=_NOT_AVAILABLE_NOTE,
    )


def x_not_available_bandwidth_audit__mutmut_7() -> CiliumBandwidthAuditResult:
    """Bandwidth manager enabled on Cilium but no bandwidth annotations found."""
    return CiliumBandwidthAuditResult(
        installed=True,
        total_pods=0,
        entries=[],
        note=_NOT_AVAILABLE_NOTE,
    )


def x_not_available_bandwidth_audit__mutmut_8() -> CiliumBandwidthAuditResult:
    """Bandwidth manager enabled on Cilium but no bandwidth annotations found."""
    return CiliumBandwidthAuditResult(
        installed=True,
        status="not_available",
        entries=[],
        note=_NOT_AVAILABLE_NOTE,
    )


def x_not_available_bandwidth_audit__mutmut_9() -> CiliumBandwidthAuditResult:
    """Bandwidth manager enabled on Cilium but no bandwidth annotations found."""
    return CiliumBandwidthAuditResult(
        installed=True,
        status="not_available",
        total_pods=0,
        note=_NOT_AVAILABLE_NOTE,
    )


def x_not_available_bandwidth_audit__mutmut_10() -> CiliumBandwidthAuditResult:
    """Bandwidth manager enabled on Cilium but no bandwidth annotations found."""
    return CiliumBandwidthAuditResult(
        installed=True,
        status="not_available",
        total_pods=0,
        entries=[],
        )


def x_not_available_bandwidth_audit__mutmut_11() -> CiliumBandwidthAuditResult:
    """Bandwidth manager enabled on Cilium but no bandwidth annotations found."""
    return CiliumBandwidthAuditResult(
        installed=False,
        status="not_available",
        total_pods=0,
        entries=[],
        note=_NOT_AVAILABLE_NOTE,
    )


def x_not_available_bandwidth_audit__mutmut_12() -> CiliumBandwidthAuditResult:
    """Bandwidth manager enabled on Cilium but no bandwidth annotations found."""
    return CiliumBandwidthAuditResult(
        installed=True,
        status="XXnot_availableXX",
        total_pods=0,
        entries=[],
        note=_NOT_AVAILABLE_NOTE,
    )


def x_not_available_bandwidth_audit__mutmut_13() -> CiliumBandwidthAuditResult:
    """Bandwidth manager enabled on Cilium but no bandwidth annotations found."""
    return CiliumBandwidthAuditResult(
        installed=True,
        status="NOT_AVAILABLE",
        total_pods=0,
        entries=[],
        note=_NOT_AVAILABLE_NOTE,
    )


def x_not_available_bandwidth_audit__mutmut_14() -> CiliumBandwidthAuditResult:
    """Bandwidth manager enabled on Cilium but no bandwidth annotations found."""
    return CiliumBandwidthAuditResult(
        installed=True,
        status="not_available",
        total_pods=1,
        entries=[],
        note=_NOT_AVAILABLE_NOTE,
    )

mutants_x_not_available_bandwidth_audit__mutmut['_mutmut_orig'] = x_not_available_bandwidth_audit__mutmut_orig # type: ignore # mutmut generated
mutants_x_not_available_bandwidth_audit__mutmut['x_not_available_bandwidth_audit__mutmut_1'] = x_not_available_bandwidth_audit__mutmut_1 # type: ignore # mutmut generated
mutants_x_not_available_bandwidth_audit__mutmut['x_not_available_bandwidth_audit__mutmut_2'] = x_not_available_bandwidth_audit__mutmut_2 # type: ignore # mutmut generated
mutants_x_not_available_bandwidth_audit__mutmut['x_not_available_bandwidth_audit__mutmut_3'] = x_not_available_bandwidth_audit__mutmut_3 # type: ignore # mutmut generated
mutants_x_not_available_bandwidth_audit__mutmut['x_not_available_bandwidth_audit__mutmut_4'] = x_not_available_bandwidth_audit__mutmut_4 # type: ignore # mutmut generated
mutants_x_not_available_bandwidth_audit__mutmut['x_not_available_bandwidth_audit__mutmut_5'] = x_not_available_bandwidth_audit__mutmut_5 # type: ignore # mutmut generated
mutants_x_not_available_bandwidth_audit__mutmut['x_not_available_bandwidth_audit__mutmut_6'] = x_not_available_bandwidth_audit__mutmut_6 # type: ignore # mutmut generated
mutants_x_not_available_bandwidth_audit__mutmut['x_not_available_bandwidth_audit__mutmut_7'] = x_not_available_bandwidth_audit__mutmut_7 # type: ignore # mutmut generated
mutants_x_not_available_bandwidth_audit__mutmut['x_not_available_bandwidth_audit__mutmut_8'] = x_not_available_bandwidth_audit__mutmut_8 # type: ignore # mutmut generated
mutants_x_not_available_bandwidth_audit__mutmut['x_not_available_bandwidth_audit__mutmut_9'] = x_not_available_bandwidth_audit__mutmut_9 # type: ignore # mutmut generated
mutants_x_not_available_bandwidth_audit__mutmut['x_not_available_bandwidth_audit__mutmut_10'] = x_not_available_bandwidth_audit__mutmut_10 # type: ignore # mutmut generated
mutants_x_not_available_bandwidth_audit__mutmut['x_not_available_bandwidth_audit__mutmut_11'] = x_not_available_bandwidth_audit__mutmut_11 # type: ignore # mutmut generated
mutants_x_not_available_bandwidth_audit__mutmut['x_not_available_bandwidth_audit__mutmut_12'] = x_not_available_bandwidth_audit__mutmut_12 # type: ignore # mutmut generated
mutants_x_not_available_bandwidth_audit__mutmut['x_not_available_bandwidth_audit__mutmut_13'] = x_not_available_bandwidth_audit__mutmut_13 # type: ignore # mutmut generated
mutants_x_not_available_bandwidth_audit__mutmut['x_not_available_bandwidth_audit__mutmut_14'] = x_not_available_bandwidth_audit__mutmut_14 # type: ignore # mutmut generated
mutants_x__note_for__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__note_for__mutmut)
def _note_for(usage_ratio: float | None, throttled: bool) -> str | None:
    if throttled:
        return "Pod is being throttled by the Cilium bandwidth manager"
    if usage_ratio is not None and usage_ratio >= _NEAR_LIMIT_THRESHOLD:
        return f"Pod at {usage_ratio * 100:.0f}% of its bandwidth limit"
    return None


def x__note_for__mutmut_orig(usage_ratio: float | None, throttled: bool) -> str | None:
    if throttled:
        return "Pod is being throttled by the Cilium bandwidth manager"
    if usage_ratio is not None and usage_ratio >= _NEAR_LIMIT_THRESHOLD:
        return f"Pod at {usage_ratio * 100:.0f}% of its bandwidth limit"
    return None


def x__note_for__mutmut_1(usage_ratio: float | None, throttled: bool) -> str | None:
    if throttled:
        return "XXPod is being throttled by the Cilium bandwidth managerXX"
    if usage_ratio is not None and usage_ratio >= _NEAR_LIMIT_THRESHOLD:
        return f"Pod at {usage_ratio * 100:.0f}% of its bandwidth limit"
    return None


def x__note_for__mutmut_2(usage_ratio: float | None, throttled: bool) -> str | None:
    if throttled:
        return "pod is being throttled by the cilium bandwidth manager"
    if usage_ratio is not None and usage_ratio >= _NEAR_LIMIT_THRESHOLD:
        return f"Pod at {usage_ratio * 100:.0f}% of its bandwidth limit"
    return None


def x__note_for__mutmut_3(usage_ratio: float | None, throttled: bool) -> str | None:
    if throttled:
        return "POD IS BEING THROTTLED BY THE CILIUM BANDWIDTH MANAGER"
    if usage_ratio is not None and usage_ratio >= _NEAR_LIMIT_THRESHOLD:
        return f"Pod at {usage_ratio * 100:.0f}% of its bandwidth limit"
    return None


def x__note_for__mutmut_4(usage_ratio: float | None, throttled: bool) -> str | None:
    if throttled:
        return "Pod is being throttled by the Cilium bandwidth manager"
    if usage_ratio is not None or usage_ratio >= _NEAR_LIMIT_THRESHOLD:
        return f"Pod at {usage_ratio * 100:.0f}% of its bandwidth limit"
    return None


def x__note_for__mutmut_5(usage_ratio: float | None, throttled: bool) -> str | None:
    if throttled:
        return "Pod is being throttled by the Cilium bandwidth manager"
    if usage_ratio is None and usage_ratio >= _NEAR_LIMIT_THRESHOLD:
        return f"Pod at {usage_ratio * 100:.0f}% of its bandwidth limit"
    return None


def x__note_for__mutmut_6(usage_ratio: float | None, throttled: bool) -> str | None:
    if throttled:
        return "Pod is being throttled by the Cilium bandwidth manager"
    if usage_ratio is not None and usage_ratio > _NEAR_LIMIT_THRESHOLD:
        return f"Pod at {usage_ratio * 100:.0f}% of its bandwidth limit"
    return None


def x__note_for__mutmut_7(usage_ratio: float | None, throttled: bool) -> str | None:
    if throttled:
        return "Pod is being throttled by the Cilium bandwidth manager"
    if usage_ratio is not None and usage_ratio >= _NEAR_LIMIT_THRESHOLD:
        return f"Pod at {usage_ratio / 100:.0f}% of its bandwidth limit"
    return None


def x__note_for__mutmut_8(usage_ratio: float | None, throttled: bool) -> str | None:
    if throttled:
        return "Pod is being throttled by the Cilium bandwidth manager"
    if usage_ratio is not None and usage_ratio >= _NEAR_LIMIT_THRESHOLD:
        return f"Pod at {usage_ratio * 101:.0f}% of its bandwidth limit"
    return None

mutants_x__note_for__mutmut['_mutmut_orig'] = x__note_for__mutmut_orig # type: ignore # mutmut generated
mutants_x__note_for__mutmut['x__note_for__mutmut_1'] = x__note_for__mutmut_1 # type: ignore # mutmut generated
mutants_x__note_for__mutmut['x__note_for__mutmut_2'] = x__note_for__mutmut_2 # type: ignore # mutmut generated
mutants_x__note_for__mutmut['x__note_for__mutmut_3'] = x__note_for__mutmut_3 # type: ignore # mutmut generated
mutants_x__note_for__mutmut['x__note_for__mutmut_4'] = x__note_for__mutmut_4 # type: ignore # mutmut generated
mutants_x__note_for__mutmut['x__note_for__mutmut_5'] = x__note_for__mutmut_5 # type: ignore # mutmut generated
mutants_x__note_for__mutmut['x__note_for__mutmut_6'] = x__note_for__mutmut_6 # type: ignore # mutmut generated
mutants_x__note_for__mutmut['x__note_for__mutmut_7'] = x__note_for__mutmut_7 # type: ignore # mutmut generated
mutants_x__note_for__mutmut['x__note_for__mutmut_8'] = x__note_for__mutmut_8 # type: ignore # mutmut generated
