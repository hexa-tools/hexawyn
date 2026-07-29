from dataclasses import asdict

from hexawyn.domain.models.memory_saturation import MemoryPrediction


def predictions_to_dicts(
    critical_pods: list[MemoryPrediction],
) -> list[dict[str, object]]:
    return [asdict(p) for p in critical_pods]


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
