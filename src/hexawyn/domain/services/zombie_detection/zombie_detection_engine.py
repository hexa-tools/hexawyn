from __future__ import annotations

from hexawyn.domain.models.zombie_detection import ZombieCandidate, ZombieDetectionResult

_PROBE_NOISE_THRESHOLD = 0.005  # RPS — anything below is considered health-check only


class ZombieDetectionEngine:
    """Pure domain service — no infra deps, no try/catch."""

    def detect(
        self,
        pods: list[dict[str, object]],
        analysis_window_hours: int = 24,
    ) -> ZombieDetectionResult:
        zombie_candidates: list[ZombieCandidate] = []
        total_wasted_cores = 0.0
        total_wasted_gb = 0.0

        for pod in pods:
            if _is_excluded(pod):
                continue
            if not _is_zero_traffic(pod):
                continue

            risk, reason = _classify_risk(pod)
            cpu = _as_float(pod.get("cpu_cores"))
            mem = _as_float(pod.get("memory_gb"))

            zombie_candidates.append(
                ZombieCandidate(
                    pod_name=str(pod.get("pod_name", "")),
                    namespace=str(pod.get("namespace", "")),
                    age_days=int(_as_float(pod.get("age_days"))),
                    traffic_rps=_as_float(pod.get("traffic_rps")),
                    cpu_cores=cpu,
                    memory_gb=mem,
                    risk=risk,
                    reason=reason,
                )
            )
            total_wasted_cores += cpu
            total_wasted_gb += mem

        return ZombieDetectionResult(
            analysis_window_hours=analysis_window_hours,
            zombie_candidates=zombie_candidates,
            total_wasted_cores=round(total_wasted_cores, 2),
            total_wasted_gb=round(total_wasted_gb, 2),
        )


def _is_excluded(pod: dict[str, object]) -> bool:
    if _as_bool(pod.get("is_terminating")):
        return True
    return False


def _is_zero_traffic(pod: dict[str, object]) -> bool:
    traffic = _as_float(pod.get("traffic_rps"))
    has_sidecar = _as_bool(pod.get("has_sidecar"))
    sidecar_traffic = _as_float(pod.get("sidecar_traffic_rps"))

    total_traffic = traffic + (sidecar_traffic if has_sidecar else 0.0)

    if total_traffic > _PROBE_NOISE_THRESHOLD:
        return False

    is_cronjob = _as_bool(pod.get("is_cronjob"))
    if is_cronjob:
        seven_day_traffic = _as_float(pod.get("seven_day_traffic_rps"))
        return seven_day_traffic <= _PROBE_NOISE_THRESHOLD

    return True


def _classify_risk(pod: dict[str, object]) -> tuple[str, str]:
    has_service = _as_bool(pod.get("has_service"))
    is_cronjob = _as_bool(pod.get("is_cronjob"))

    if has_service:
        return "review_needed", "No traffic but has service pointing to it"

    if is_cronjob:
        return "safe_to_remove", "No traffic for 24h, no deps"

    return "safe_to_remove", "No traffic for 24h, no deps"


def _as_float(value: object) -> float:
    if value is None:
        return 0.0
    try:
        return float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0.0


def _as_bool(value: object) -> bool:
    if value is None:
        return False
    if isinstance(value, bool):
        return value
    return bool(value)
