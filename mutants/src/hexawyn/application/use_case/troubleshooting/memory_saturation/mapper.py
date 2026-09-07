from dataclasses import asdict

from hexawyn.domain.models.memory_saturation import MemoryPrediction


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_predictions_to_dicts__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_predictions_to_dicts__mutmut)
def predictions_to_dicts(
    critical_pods: list[MemoryPrediction],
) -> list[dict[str, object]]:
    return [asdict(p) for p in critical_pods]


def x_predictions_to_dicts__mutmut_orig(
    critical_pods: list[MemoryPrediction],
) -> list[dict[str, object]]:
    return [asdict(p) for p in critical_pods]


def x_predictions_to_dicts__mutmut_1(
    critical_pods: list[MemoryPrediction],
) -> list[dict[str, object]]:
    return [asdict(None) for p in critical_pods]

mutants_x_predictions_to_dicts__mutmut['_mutmut_orig'] = x_predictions_to_dicts__mutmut_orig # type: ignore # mutmut generated
mutants_x_predictions_to_dicts__mutmut['x_predictions_to_dicts__mutmut_1'] = x_predictions_to_dicts__mutmut_1 # type: ignore # mutmut generated
mutants_x_attach_otel_root_cause__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_attach_otel_root_cause__mutmut)
def attach_otel_root_cause(
    pod: MemoryPrediction,
    cause: str,
) -> MemoryPrediction:
    return MemoryPrediction(
        pod_name=pod.pod_name,
        namespace=pod.namespace,
        current_memory_mb=pod.current_memory_mb,
        limit_mb=pod.limit_mb,
        growth_rate_mb_per_min=pod.growth_rate_mb_per_min,
        saturation_in_minutes=pod.saturation_in_minutes,
        otel_root_cause=cause,
        risk=pod.risk,
    )


def x_attach_otel_root_cause__mutmut_orig(
    pod: MemoryPrediction,
    cause: str,
) -> MemoryPrediction:
    return MemoryPrediction(
        pod_name=pod.pod_name,
        namespace=pod.namespace,
        current_memory_mb=pod.current_memory_mb,
        limit_mb=pod.limit_mb,
        growth_rate_mb_per_min=pod.growth_rate_mb_per_min,
        saturation_in_minutes=pod.saturation_in_minutes,
        otel_root_cause=cause,
        risk=pod.risk,
    )


def x_attach_otel_root_cause__mutmut_1(
    pod: MemoryPrediction,
    cause: str,
) -> MemoryPrediction:
    return MemoryPrediction(
        pod_name=None,
        namespace=pod.namespace,
        current_memory_mb=pod.current_memory_mb,
        limit_mb=pod.limit_mb,
        growth_rate_mb_per_min=pod.growth_rate_mb_per_min,
        saturation_in_minutes=pod.saturation_in_minutes,
        otel_root_cause=cause,
        risk=pod.risk,
    )


def x_attach_otel_root_cause__mutmut_2(
    pod: MemoryPrediction,
    cause: str,
) -> MemoryPrediction:
    return MemoryPrediction(
        pod_name=pod.pod_name,
        namespace=None,
        current_memory_mb=pod.current_memory_mb,
        limit_mb=pod.limit_mb,
        growth_rate_mb_per_min=pod.growth_rate_mb_per_min,
        saturation_in_minutes=pod.saturation_in_minutes,
        otel_root_cause=cause,
        risk=pod.risk,
    )


def x_attach_otel_root_cause__mutmut_3(
    pod: MemoryPrediction,
    cause: str,
) -> MemoryPrediction:
    return MemoryPrediction(
        pod_name=pod.pod_name,
        namespace=pod.namespace,
        current_memory_mb=None,
        limit_mb=pod.limit_mb,
        growth_rate_mb_per_min=pod.growth_rate_mb_per_min,
        saturation_in_minutes=pod.saturation_in_minutes,
        otel_root_cause=cause,
        risk=pod.risk,
    )


def x_attach_otel_root_cause__mutmut_4(
    pod: MemoryPrediction,
    cause: str,
) -> MemoryPrediction:
    return MemoryPrediction(
        pod_name=pod.pod_name,
        namespace=pod.namespace,
        current_memory_mb=pod.current_memory_mb,
        limit_mb=None,
        growth_rate_mb_per_min=pod.growth_rate_mb_per_min,
        saturation_in_minutes=pod.saturation_in_minutes,
        otel_root_cause=cause,
        risk=pod.risk,
    )


def x_attach_otel_root_cause__mutmut_5(
    pod: MemoryPrediction,
    cause: str,
) -> MemoryPrediction:
    return MemoryPrediction(
        pod_name=pod.pod_name,
        namespace=pod.namespace,
        current_memory_mb=pod.current_memory_mb,
        limit_mb=pod.limit_mb,
        growth_rate_mb_per_min=None,
        saturation_in_minutes=pod.saturation_in_minutes,
        otel_root_cause=cause,
        risk=pod.risk,
    )


def x_attach_otel_root_cause__mutmut_6(
    pod: MemoryPrediction,
    cause: str,
) -> MemoryPrediction:
    return MemoryPrediction(
        pod_name=pod.pod_name,
        namespace=pod.namespace,
        current_memory_mb=pod.current_memory_mb,
        limit_mb=pod.limit_mb,
        growth_rate_mb_per_min=pod.growth_rate_mb_per_min,
        saturation_in_minutes=None,
        otel_root_cause=cause,
        risk=pod.risk,
    )


def x_attach_otel_root_cause__mutmut_7(
    pod: MemoryPrediction,
    cause: str,
) -> MemoryPrediction:
    return MemoryPrediction(
        pod_name=pod.pod_name,
        namespace=pod.namespace,
        current_memory_mb=pod.current_memory_mb,
        limit_mb=pod.limit_mb,
        growth_rate_mb_per_min=pod.growth_rate_mb_per_min,
        saturation_in_minutes=pod.saturation_in_minutes,
        otel_root_cause=None,
        risk=pod.risk,
    )


def x_attach_otel_root_cause__mutmut_8(
    pod: MemoryPrediction,
    cause: str,
) -> MemoryPrediction:
    return MemoryPrediction(
        pod_name=pod.pod_name,
        namespace=pod.namespace,
        current_memory_mb=pod.current_memory_mb,
        limit_mb=pod.limit_mb,
        growth_rate_mb_per_min=pod.growth_rate_mb_per_min,
        saturation_in_minutes=pod.saturation_in_minutes,
        otel_root_cause=cause,
        risk=None,
    )


def x_attach_otel_root_cause__mutmut_9(
    pod: MemoryPrediction,
    cause: str,
) -> MemoryPrediction:
    return MemoryPrediction(
        namespace=pod.namespace,
        current_memory_mb=pod.current_memory_mb,
        limit_mb=pod.limit_mb,
        growth_rate_mb_per_min=pod.growth_rate_mb_per_min,
        saturation_in_minutes=pod.saturation_in_minutes,
        otel_root_cause=cause,
        risk=pod.risk,
    )


def x_attach_otel_root_cause__mutmut_10(
    pod: MemoryPrediction,
    cause: str,
) -> MemoryPrediction:
    return MemoryPrediction(
        pod_name=pod.pod_name,
        current_memory_mb=pod.current_memory_mb,
        limit_mb=pod.limit_mb,
        growth_rate_mb_per_min=pod.growth_rate_mb_per_min,
        saturation_in_minutes=pod.saturation_in_minutes,
        otel_root_cause=cause,
        risk=pod.risk,
    )


def x_attach_otel_root_cause__mutmut_11(
    pod: MemoryPrediction,
    cause: str,
) -> MemoryPrediction:
    return MemoryPrediction(
        pod_name=pod.pod_name,
        namespace=pod.namespace,
        limit_mb=pod.limit_mb,
        growth_rate_mb_per_min=pod.growth_rate_mb_per_min,
        saturation_in_minutes=pod.saturation_in_minutes,
        otel_root_cause=cause,
        risk=pod.risk,
    )


def x_attach_otel_root_cause__mutmut_12(
    pod: MemoryPrediction,
    cause: str,
) -> MemoryPrediction:
    return MemoryPrediction(
        pod_name=pod.pod_name,
        namespace=pod.namespace,
        current_memory_mb=pod.current_memory_mb,
        growth_rate_mb_per_min=pod.growth_rate_mb_per_min,
        saturation_in_minutes=pod.saturation_in_minutes,
        otel_root_cause=cause,
        risk=pod.risk,
    )


def x_attach_otel_root_cause__mutmut_13(
    pod: MemoryPrediction,
    cause: str,
) -> MemoryPrediction:
    return MemoryPrediction(
        pod_name=pod.pod_name,
        namespace=pod.namespace,
        current_memory_mb=pod.current_memory_mb,
        limit_mb=pod.limit_mb,
        saturation_in_minutes=pod.saturation_in_minutes,
        otel_root_cause=cause,
        risk=pod.risk,
    )


def x_attach_otel_root_cause__mutmut_14(
    pod: MemoryPrediction,
    cause: str,
) -> MemoryPrediction:
    return MemoryPrediction(
        pod_name=pod.pod_name,
        namespace=pod.namespace,
        current_memory_mb=pod.current_memory_mb,
        limit_mb=pod.limit_mb,
        growth_rate_mb_per_min=pod.growth_rate_mb_per_min,
        otel_root_cause=cause,
        risk=pod.risk,
    )


def x_attach_otel_root_cause__mutmut_15(
    pod: MemoryPrediction,
    cause: str,
) -> MemoryPrediction:
    return MemoryPrediction(
        pod_name=pod.pod_name,
        namespace=pod.namespace,
        current_memory_mb=pod.current_memory_mb,
        limit_mb=pod.limit_mb,
        growth_rate_mb_per_min=pod.growth_rate_mb_per_min,
        saturation_in_minutes=pod.saturation_in_minutes,
        risk=pod.risk,
    )


def x_attach_otel_root_cause__mutmut_16(
    pod: MemoryPrediction,
    cause: str,
) -> MemoryPrediction:
    return MemoryPrediction(
        pod_name=pod.pod_name,
        namespace=pod.namespace,
        current_memory_mb=pod.current_memory_mb,
        limit_mb=pod.limit_mb,
        growth_rate_mb_per_min=pod.growth_rate_mb_per_min,
        saturation_in_minutes=pod.saturation_in_minutes,
        otel_root_cause=cause,
        )

mutants_x_attach_otel_root_cause__mutmut['_mutmut_orig'] = x_attach_otel_root_cause__mutmut_orig # type: ignore # mutmut generated
mutants_x_attach_otel_root_cause__mutmut['x_attach_otel_root_cause__mutmut_1'] = x_attach_otel_root_cause__mutmut_1 # type: ignore # mutmut generated
mutants_x_attach_otel_root_cause__mutmut['x_attach_otel_root_cause__mutmut_2'] = x_attach_otel_root_cause__mutmut_2 # type: ignore # mutmut generated
mutants_x_attach_otel_root_cause__mutmut['x_attach_otel_root_cause__mutmut_3'] = x_attach_otel_root_cause__mutmut_3 # type: ignore # mutmut generated
mutants_x_attach_otel_root_cause__mutmut['x_attach_otel_root_cause__mutmut_4'] = x_attach_otel_root_cause__mutmut_4 # type: ignore # mutmut generated
mutants_x_attach_otel_root_cause__mutmut['x_attach_otel_root_cause__mutmut_5'] = x_attach_otel_root_cause__mutmut_5 # type: ignore # mutmut generated
mutants_x_attach_otel_root_cause__mutmut['x_attach_otel_root_cause__mutmut_6'] = x_attach_otel_root_cause__mutmut_6 # type: ignore # mutmut generated
mutants_x_attach_otel_root_cause__mutmut['x_attach_otel_root_cause__mutmut_7'] = x_attach_otel_root_cause__mutmut_7 # type: ignore # mutmut generated
mutants_x_attach_otel_root_cause__mutmut['x_attach_otel_root_cause__mutmut_8'] = x_attach_otel_root_cause__mutmut_8 # type: ignore # mutmut generated
mutants_x_attach_otel_root_cause__mutmut['x_attach_otel_root_cause__mutmut_9'] = x_attach_otel_root_cause__mutmut_9 # type: ignore # mutmut generated
mutants_x_attach_otel_root_cause__mutmut['x_attach_otel_root_cause__mutmut_10'] = x_attach_otel_root_cause__mutmut_10 # type: ignore # mutmut generated
mutants_x_attach_otel_root_cause__mutmut['x_attach_otel_root_cause__mutmut_11'] = x_attach_otel_root_cause__mutmut_11 # type: ignore # mutmut generated
mutants_x_attach_otel_root_cause__mutmut['x_attach_otel_root_cause__mutmut_12'] = x_attach_otel_root_cause__mutmut_12 # type: ignore # mutmut generated
mutants_x_attach_otel_root_cause__mutmut['x_attach_otel_root_cause__mutmut_13'] = x_attach_otel_root_cause__mutmut_13 # type: ignore # mutmut generated
mutants_x_attach_otel_root_cause__mutmut['x_attach_otel_root_cause__mutmut_14'] = x_attach_otel_root_cause__mutmut_14 # type: ignore # mutmut generated
mutants_x_attach_otel_root_cause__mutmut['x_attach_otel_root_cause__mutmut_15'] = x_attach_otel_root_cause__mutmut_15 # type: ignore # mutmut generated
mutants_x_attach_otel_root_cause__mutmut['x_attach_otel_root_cause__mutmut_16'] = x_attach_otel_root_cause__mutmut_16 # type: ignore # mutmut generated
