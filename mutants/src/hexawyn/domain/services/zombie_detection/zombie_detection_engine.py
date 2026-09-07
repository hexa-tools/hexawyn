from __future__ import annotations

from hexawyn.domain.models.zombie_detection import ZombieCandidate, ZombieDetectionResult

_PROBE_NOISE_THRESHOLD = 0.005  # RPS — anything below is considered health-check only


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁZombieDetectionEngineǁdetect__mutmut: MutantDict = {}  # type: ignore


class ZombieDetectionEngine:
    """Pure domain service — no infra deps, no try/catch."""

    @_mutmut_mutated(mutants_xǁZombieDetectionEngineǁdetect__mutmut)
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

    def xǁZombieDetectionEngineǁdetect__mutmut_orig(
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

    def xǁZombieDetectionEngineǁdetect__mutmut_1(
        self,
        pods: list[dict[str, object]],
        analysis_window_hours: int = 25,
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

    def xǁZombieDetectionEngineǁdetect__mutmut_2(
        self,
        pods: list[dict[str, object]],
        analysis_window_hours: int = 24,
    ) -> ZombieDetectionResult:
        zombie_candidates: list[ZombieCandidate] = None
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

    def xǁZombieDetectionEngineǁdetect__mutmut_3(
        self,
        pods: list[dict[str, object]],
        analysis_window_hours: int = 24,
    ) -> ZombieDetectionResult:
        zombie_candidates: list[ZombieCandidate] = []
        total_wasted_cores = None
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

    def xǁZombieDetectionEngineǁdetect__mutmut_4(
        self,
        pods: list[dict[str, object]],
        analysis_window_hours: int = 24,
    ) -> ZombieDetectionResult:
        zombie_candidates: list[ZombieCandidate] = []
        total_wasted_cores = 1.0
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

    def xǁZombieDetectionEngineǁdetect__mutmut_5(
        self,
        pods: list[dict[str, object]],
        analysis_window_hours: int = 24,
    ) -> ZombieDetectionResult:
        zombie_candidates: list[ZombieCandidate] = []
        total_wasted_cores = 0.0
        total_wasted_gb = None

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

    def xǁZombieDetectionEngineǁdetect__mutmut_6(
        self,
        pods: list[dict[str, object]],
        analysis_window_hours: int = 24,
    ) -> ZombieDetectionResult:
        zombie_candidates: list[ZombieCandidate] = []
        total_wasted_cores = 0.0
        total_wasted_gb = 1.0

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

    def xǁZombieDetectionEngineǁdetect__mutmut_7(
        self,
        pods: list[dict[str, object]],
        analysis_window_hours: int = 24,
    ) -> ZombieDetectionResult:
        zombie_candidates: list[ZombieCandidate] = []
        total_wasted_cores = 0.0
        total_wasted_gb = 0.0

        for pod in pods:
            if _is_excluded(None):
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

    def xǁZombieDetectionEngineǁdetect__mutmut_8(
        self,
        pods: list[dict[str, object]],
        analysis_window_hours: int = 24,
    ) -> ZombieDetectionResult:
        zombie_candidates: list[ZombieCandidate] = []
        total_wasted_cores = 0.0
        total_wasted_gb = 0.0

        for pod in pods:
            if _is_excluded(pod):
                break
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

    def xǁZombieDetectionEngineǁdetect__mutmut_9(
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
            if _is_zero_traffic(pod):
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

    def xǁZombieDetectionEngineǁdetect__mutmut_10(
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
            if not _is_zero_traffic(None):
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

    def xǁZombieDetectionEngineǁdetect__mutmut_11(
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
                break

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

    def xǁZombieDetectionEngineǁdetect__mutmut_12(
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

            risk, reason = None
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

    def xǁZombieDetectionEngineǁdetect__mutmut_13(
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

            risk, reason = _classify_risk(None)
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

    def xǁZombieDetectionEngineǁdetect__mutmut_14(
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
            cpu = None
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

    def xǁZombieDetectionEngineǁdetect__mutmut_15(
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
            cpu = _as_float(None)
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

    def xǁZombieDetectionEngineǁdetect__mutmut_16(
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
            cpu = _as_float(pod.get(None))
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

    def xǁZombieDetectionEngineǁdetect__mutmut_17(
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
            cpu = _as_float(pod.get("XXcpu_coresXX"))
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

    def xǁZombieDetectionEngineǁdetect__mutmut_18(
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
            cpu = _as_float(pod.get("CPU_CORES"))
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

    def xǁZombieDetectionEngineǁdetect__mutmut_19(
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
            mem = None

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

    def xǁZombieDetectionEngineǁdetect__mutmut_20(
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
            mem = _as_float(None)

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

    def xǁZombieDetectionEngineǁdetect__mutmut_21(
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
            mem = _as_float(pod.get(None))

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

    def xǁZombieDetectionEngineǁdetect__mutmut_22(
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
            mem = _as_float(pod.get("XXmemory_gbXX"))

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

    def xǁZombieDetectionEngineǁdetect__mutmut_23(
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
            mem = _as_float(pod.get("MEMORY_GB"))

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

    def xǁZombieDetectionEngineǁdetect__mutmut_24(
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
                None
            )
            total_wasted_cores += cpu
            total_wasted_gb += mem

        return ZombieDetectionResult(
            analysis_window_hours=analysis_window_hours,
            zombie_candidates=zombie_candidates,
            total_wasted_cores=round(total_wasted_cores, 2),
            total_wasted_gb=round(total_wasted_gb, 2),
        )

    def xǁZombieDetectionEngineǁdetect__mutmut_25(
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
                    pod_name=None,
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

    def xǁZombieDetectionEngineǁdetect__mutmut_26(
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
                    namespace=None,
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

    def xǁZombieDetectionEngineǁdetect__mutmut_27(
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
                    age_days=None,
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

    def xǁZombieDetectionEngineǁdetect__mutmut_28(
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
                    traffic_rps=None,
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

    def xǁZombieDetectionEngineǁdetect__mutmut_29(
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
                    cpu_cores=None,
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

    def xǁZombieDetectionEngineǁdetect__mutmut_30(
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
                    memory_gb=None,
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

    def xǁZombieDetectionEngineǁdetect__mutmut_31(
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
                    risk=None,
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

    def xǁZombieDetectionEngineǁdetect__mutmut_32(
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
                    reason=None,
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

    def xǁZombieDetectionEngineǁdetect__mutmut_33(
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

    def xǁZombieDetectionEngineǁdetect__mutmut_34(
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

    def xǁZombieDetectionEngineǁdetect__mutmut_35(
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

    def xǁZombieDetectionEngineǁdetect__mutmut_36(
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

    def xǁZombieDetectionEngineǁdetect__mutmut_37(
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

    def xǁZombieDetectionEngineǁdetect__mutmut_38(
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

    def xǁZombieDetectionEngineǁdetect__mutmut_39(
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

    def xǁZombieDetectionEngineǁdetect__mutmut_40(
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

    def xǁZombieDetectionEngineǁdetect__mutmut_41(
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
                    pod_name=str(None),
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

    def xǁZombieDetectionEngineǁdetect__mutmut_42(
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
                    pod_name=str(pod.get(None, "")),
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

    def xǁZombieDetectionEngineǁdetect__mutmut_43(
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
                    pod_name=str(pod.get("pod_name", None)),
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

    def xǁZombieDetectionEngineǁdetect__mutmut_44(
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
                    pod_name=str(pod.get("")),
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

    def xǁZombieDetectionEngineǁdetect__mutmut_45(
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
                    pod_name=str(pod.get("pod_name", )),
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

    def xǁZombieDetectionEngineǁdetect__mutmut_46(
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
                    pod_name=str(pod.get("XXpod_nameXX", "")),
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

    def xǁZombieDetectionEngineǁdetect__mutmut_47(
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
                    pod_name=str(pod.get("POD_NAME", "")),
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

    def xǁZombieDetectionEngineǁdetect__mutmut_48(
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
                    pod_name=str(pod.get("pod_name", "XXXX")),
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

    def xǁZombieDetectionEngineǁdetect__mutmut_49(
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
                    namespace=str(None),
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

    def xǁZombieDetectionEngineǁdetect__mutmut_50(
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
                    namespace=str(pod.get(None, "")),
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

    def xǁZombieDetectionEngineǁdetect__mutmut_51(
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
                    namespace=str(pod.get("namespace", None)),
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

    def xǁZombieDetectionEngineǁdetect__mutmut_52(
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
                    namespace=str(pod.get("")),
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

    def xǁZombieDetectionEngineǁdetect__mutmut_53(
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
                    namespace=str(pod.get("namespace", )),
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

    def xǁZombieDetectionEngineǁdetect__mutmut_54(
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
                    namespace=str(pod.get("XXnamespaceXX", "")),
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

    def xǁZombieDetectionEngineǁdetect__mutmut_55(
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
                    namespace=str(pod.get("NAMESPACE", "")),
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

    def xǁZombieDetectionEngineǁdetect__mutmut_56(
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
                    namespace=str(pod.get("namespace", "XXXX")),
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

    def xǁZombieDetectionEngineǁdetect__mutmut_57(
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
                    age_days=int(None),
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

    def xǁZombieDetectionEngineǁdetect__mutmut_58(
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
                    age_days=int(_as_float(None)),
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

    def xǁZombieDetectionEngineǁdetect__mutmut_59(
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
                    age_days=int(_as_float(pod.get(None))),
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

    def xǁZombieDetectionEngineǁdetect__mutmut_60(
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
                    age_days=int(_as_float(pod.get("XXage_daysXX"))),
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

    def xǁZombieDetectionEngineǁdetect__mutmut_61(
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
                    age_days=int(_as_float(pod.get("AGE_DAYS"))),
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

    def xǁZombieDetectionEngineǁdetect__mutmut_62(
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
                    traffic_rps=_as_float(None),
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

    def xǁZombieDetectionEngineǁdetect__mutmut_63(
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
                    traffic_rps=_as_float(pod.get(None)),
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

    def xǁZombieDetectionEngineǁdetect__mutmut_64(
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
                    traffic_rps=_as_float(pod.get("XXtraffic_rpsXX")),
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

    def xǁZombieDetectionEngineǁdetect__mutmut_65(
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
                    traffic_rps=_as_float(pod.get("TRAFFIC_RPS")),
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

    def xǁZombieDetectionEngineǁdetect__mutmut_66(
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
            total_wasted_cores = cpu
            total_wasted_gb += mem

        return ZombieDetectionResult(
            analysis_window_hours=analysis_window_hours,
            zombie_candidates=zombie_candidates,
            total_wasted_cores=round(total_wasted_cores, 2),
            total_wasted_gb=round(total_wasted_gb, 2),
        )

    def xǁZombieDetectionEngineǁdetect__mutmut_67(
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
            total_wasted_cores -= cpu
            total_wasted_gb += mem

        return ZombieDetectionResult(
            analysis_window_hours=analysis_window_hours,
            zombie_candidates=zombie_candidates,
            total_wasted_cores=round(total_wasted_cores, 2),
            total_wasted_gb=round(total_wasted_gb, 2),
        )

    def xǁZombieDetectionEngineǁdetect__mutmut_68(
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
            total_wasted_gb = mem

        return ZombieDetectionResult(
            analysis_window_hours=analysis_window_hours,
            zombie_candidates=zombie_candidates,
            total_wasted_cores=round(total_wasted_cores, 2),
            total_wasted_gb=round(total_wasted_gb, 2),
        )

    def xǁZombieDetectionEngineǁdetect__mutmut_69(
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
            total_wasted_gb -= mem

        return ZombieDetectionResult(
            analysis_window_hours=analysis_window_hours,
            zombie_candidates=zombie_candidates,
            total_wasted_cores=round(total_wasted_cores, 2),
            total_wasted_gb=round(total_wasted_gb, 2),
        )

    def xǁZombieDetectionEngineǁdetect__mutmut_70(
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
            analysis_window_hours=None,
            zombie_candidates=zombie_candidates,
            total_wasted_cores=round(total_wasted_cores, 2),
            total_wasted_gb=round(total_wasted_gb, 2),
        )

    def xǁZombieDetectionEngineǁdetect__mutmut_71(
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
            zombie_candidates=None,
            total_wasted_cores=round(total_wasted_cores, 2),
            total_wasted_gb=round(total_wasted_gb, 2),
        )

    def xǁZombieDetectionEngineǁdetect__mutmut_72(
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
            total_wasted_cores=None,
            total_wasted_gb=round(total_wasted_gb, 2),
        )

    def xǁZombieDetectionEngineǁdetect__mutmut_73(
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
            total_wasted_gb=None,
        )

    def xǁZombieDetectionEngineǁdetect__mutmut_74(
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
            zombie_candidates=zombie_candidates,
            total_wasted_cores=round(total_wasted_cores, 2),
            total_wasted_gb=round(total_wasted_gb, 2),
        )

    def xǁZombieDetectionEngineǁdetect__mutmut_75(
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
            total_wasted_cores=round(total_wasted_cores, 2),
            total_wasted_gb=round(total_wasted_gb, 2),
        )

    def xǁZombieDetectionEngineǁdetect__mutmut_76(
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
            total_wasted_gb=round(total_wasted_gb, 2),
        )

    def xǁZombieDetectionEngineǁdetect__mutmut_77(
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
            )

    def xǁZombieDetectionEngineǁdetect__mutmut_78(
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
            total_wasted_cores=round(None, 2),
            total_wasted_gb=round(total_wasted_gb, 2),
        )

    def xǁZombieDetectionEngineǁdetect__mutmut_79(
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
            total_wasted_cores=round(total_wasted_cores, None),
            total_wasted_gb=round(total_wasted_gb, 2),
        )

    def xǁZombieDetectionEngineǁdetect__mutmut_80(
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
            total_wasted_cores=round(2),
            total_wasted_gb=round(total_wasted_gb, 2),
        )

    def xǁZombieDetectionEngineǁdetect__mutmut_81(
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
            total_wasted_cores=round(total_wasted_cores, ),
            total_wasted_gb=round(total_wasted_gb, 2),
        )

    def xǁZombieDetectionEngineǁdetect__mutmut_82(
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
            total_wasted_cores=round(total_wasted_cores, 3),
            total_wasted_gb=round(total_wasted_gb, 2),
        )

    def xǁZombieDetectionEngineǁdetect__mutmut_83(
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
            total_wasted_gb=round(None, 2),
        )

    def xǁZombieDetectionEngineǁdetect__mutmut_84(
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
            total_wasted_gb=round(total_wasted_gb, None),
        )

    def xǁZombieDetectionEngineǁdetect__mutmut_85(
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
            total_wasted_gb=round(2),
        )

    def xǁZombieDetectionEngineǁdetect__mutmut_86(
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
            total_wasted_gb=round(total_wasted_gb, ),
        )

    def xǁZombieDetectionEngineǁdetect__mutmut_87(
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
            total_wasted_gb=round(total_wasted_gb, 3),
        )

mutants_xǁZombieDetectionEngineǁdetect__mutmut['_mutmut_orig'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_orig # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_1'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_1 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_2'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_2 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_3'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_3 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_4'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_4 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_5'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_5 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_6'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_6 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_7'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_7 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_8'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_8 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_9'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_9 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_10'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_10 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_11'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_11 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_12'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_12 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_13'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_13 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_14'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_14 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_15'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_15 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_16'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_16 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_17'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_17 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_18'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_18 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_19'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_19 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_20'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_20 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_21'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_21 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_22'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_22 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_23'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_23 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_24'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_24 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_25'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_25 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_26'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_26 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_27'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_27 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_28'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_28 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_29'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_29 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_30'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_30 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_31'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_31 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_32'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_32 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_33'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_33 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_34'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_34 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_35'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_35 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_36'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_36 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_37'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_37 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_38'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_38 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_39'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_39 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_40'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_40 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_41'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_41 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_42'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_42 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_43'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_43 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_44'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_44 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_45'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_45 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_46'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_46 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_47'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_47 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_48'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_48 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_49'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_49 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_50'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_50 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_51'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_51 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_52'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_52 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_53'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_53 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_54'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_54 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_55'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_55 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_56'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_56 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_57'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_57 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_58'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_58 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_59'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_59 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_60'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_60 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_61'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_61 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_62'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_62 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_63'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_63 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_64'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_64 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_65'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_65 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_66'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_66 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_67'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_67 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_68'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_68 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_69'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_69 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_70'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_70 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_71'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_71 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_72'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_72 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_73'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_73 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_74'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_74 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_75'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_75 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_76'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_76 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_77'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_77 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_78'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_78 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_79'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_79 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_80'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_80 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_81'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_81 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_82'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_82 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_83'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_83 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_84'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_84 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_85'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_85 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_86'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_86 # type: ignore # mutmut generated
mutants_xǁZombieDetectionEngineǁdetect__mutmut['xǁZombieDetectionEngineǁdetect__mutmut_87'] = ZombieDetectionEngine.xǁZombieDetectionEngineǁdetect__mutmut_87 # type: ignore # mutmut generated
mutants_x__is_excluded__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__is_excluded__mutmut)
def _is_excluded(pod: dict[str, object]) -> bool:
    if _as_bool(pod.get("is_terminating")):
        return True
    return False


def x__is_excluded__mutmut_orig(pod: dict[str, object]) -> bool:
    if _as_bool(pod.get("is_terminating")):
        return True
    return False


def x__is_excluded__mutmut_1(pod: dict[str, object]) -> bool:
    if _as_bool(None):
        return True
    return False


def x__is_excluded__mutmut_2(pod: dict[str, object]) -> bool:
    if _as_bool(pod.get(None)):
        return True
    return False


def x__is_excluded__mutmut_3(pod: dict[str, object]) -> bool:
    if _as_bool(pod.get("XXis_terminatingXX")):
        return True
    return False


def x__is_excluded__mutmut_4(pod: dict[str, object]) -> bool:
    if _as_bool(pod.get("IS_TERMINATING")):
        return True
    return False


def x__is_excluded__mutmut_5(pod: dict[str, object]) -> bool:
    if _as_bool(pod.get("is_terminating")):
        return False
    return False


def x__is_excluded__mutmut_6(pod: dict[str, object]) -> bool:
    if _as_bool(pod.get("is_terminating")):
        return True
    return True

mutants_x__is_excluded__mutmut['_mutmut_orig'] = x__is_excluded__mutmut_orig # type: ignore # mutmut generated
mutants_x__is_excluded__mutmut['x__is_excluded__mutmut_1'] = x__is_excluded__mutmut_1 # type: ignore # mutmut generated
mutants_x__is_excluded__mutmut['x__is_excluded__mutmut_2'] = x__is_excluded__mutmut_2 # type: ignore # mutmut generated
mutants_x__is_excluded__mutmut['x__is_excluded__mutmut_3'] = x__is_excluded__mutmut_3 # type: ignore # mutmut generated
mutants_x__is_excluded__mutmut['x__is_excluded__mutmut_4'] = x__is_excluded__mutmut_4 # type: ignore # mutmut generated
mutants_x__is_excluded__mutmut['x__is_excluded__mutmut_5'] = x__is_excluded__mutmut_5 # type: ignore # mutmut generated
mutants_x__is_excluded__mutmut['x__is_excluded__mutmut_6'] = x__is_excluded__mutmut_6 # type: ignore # mutmut generated
mutants_x__is_zero_traffic__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__is_zero_traffic__mutmut)
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


def x__is_zero_traffic__mutmut_orig(pod: dict[str, object]) -> bool:
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


def x__is_zero_traffic__mutmut_1(pod: dict[str, object]) -> bool:
    traffic = None
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


def x__is_zero_traffic__mutmut_2(pod: dict[str, object]) -> bool:
    traffic = _as_float(None)
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


def x__is_zero_traffic__mutmut_3(pod: dict[str, object]) -> bool:
    traffic = _as_float(pod.get(None))
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


def x__is_zero_traffic__mutmut_4(pod: dict[str, object]) -> bool:
    traffic = _as_float(pod.get("XXtraffic_rpsXX"))
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


def x__is_zero_traffic__mutmut_5(pod: dict[str, object]) -> bool:
    traffic = _as_float(pod.get("TRAFFIC_RPS"))
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


def x__is_zero_traffic__mutmut_6(pod: dict[str, object]) -> bool:
    traffic = _as_float(pod.get("traffic_rps"))
    has_sidecar = None
    sidecar_traffic = _as_float(pod.get("sidecar_traffic_rps"))

    total_traffic = traffic + (sidecar_traffic if has_sidecar else 0.0)

    if total_traffic > _PROBE_NOISE_THRESHOLD:
        return False

    is_cronjob = _as_bool(pod.get("is_cronjob"))
    if is_cronjob:
        seven_day_traffic = _as_float(pod.get("seven_day_traffic_rps"))
        return seven_day_traffic <= _PROBE_NOISE_THRESHOLD

    return True


def x__is_zero_traffic__mutmut_7(pod: dict[str, object]) -> bool:
    traffic = _as_float(pod.get("traffic_rps"))
    has_sidecar = _as_bool(None)
    sidecar_traffic = _as_float(pod.get("sidecar_traffic_rps"))

    total_traffic = traffic + (sidecar_traffic if has_sidecar else 0.0)

    if total_traffic > _PROBE_NOISE_THRESHOLD:
        return False

    is_cronjob = _as_bool(pod.get("is_cronjob"))
    if is_cronjob:
        seven_day_traffic = _as_float(pod.get("seven_day_traffic_rps"))
        return seven_day_traffic <= _PROBE_NOISE_THRESHOLD

    return True


def x__is_zero_traffic__mutmut_8(pod: dict[str, object]) -> bool:
    traffic = _as_float(pod.get("traffic_rps"))
    has_sidecar = _as_bool(pod.get(None))
    sidecar_traffic = _as_float(pod.get("sidecar_traffic_rps"))

    total_traffic = traffic + (sidecar_traffic if has_sidecar else 0.0)

    if total_traffic > _PROBE_NOISE_THRESHOLD:
        return False

    is_cronjob = _as_bool(pod.get("is_cronjob"))
    if is_cronjob:
        seven_day_traffic = _as_float(pod.get("seven_day_traffic_rps"))
        return seven_day_traffic <= _PROBE_NOISE_THRESHOLD

    return True


def x__is_zero_traffic__mutmut_9(pod: dict[str, object]) -> bool:
    traffic = _as_float(pod.get("traffic_rps"))
    has_sidecar = _as_bool(pod.get("XXhas_sidecarXX"))
    sidecar_traffic = _as_float(pod.get("sidecar_traffic_rps"))

    total_traffic = traffic + (sidecar_traffic if has_sidecar else 0.0)

    if total_traffic > _PROBE_NOISE_THRESHOLD:
        return False

    is_cronjob = _as_bool(pod.get("is_cronjob"))
    if is_cronjob:
        seven_day_traffic = _as_float(pod.get("seven_day_traffic_rps"))
        return seven_day_traffic <= _PROBE_NOISE_THRESHOLD

    return True


def x__is_zero_traffic__mutmut_10(pod: dict[str, object]) -> bool:
    traffic = _as_float(pod.get("traffic_rps"))
    has_sidecar = _as_bool(pod.get("HAS_SIDECAR"))
    sidecar_traffic = _as_float(pod.get("sidecar_traffic_rps"))

    total_traffic = traffic + (sidecar_traffic if has_sidecar else 0.0)

    if total_traffic > _PROBE_NOISE_THRESHOLD:
        return False

    is_cronjob = _as_bool(pod.get("is_cronjob"))
    if is_cronjob:
        seven_day_traffic = _as_float(pod.get("seven_day_traffic_rps"))
        return seven_day_traffic <= _PROBE_NOISE_THRESHOLD

    return True


def x__is_zero_traffic__mutmut_11(pod: dict[str, object]) -> bool:
    traffic = _as_float(pod.get("traffic_rps"))
    has_sidecar = _as_bool(pod.get("has_sidecar"))
    sidecar_traffic = None

    total_traffic = traffic + (sidecar_traffic if has_sidecar else 0.0)

    if total_traffic > _PROBE_NOISE_THRESHOLD:
        return False

    is_cronjob = _as_bool(pod.get("is_cronjob"))
    if is_cronjob:
        seven_day_traffic = _as_float(pod.get("seven_day_traffic_rps"))
        return seven_day_traffic <= _PROBE_NOISE_THRESHOLD

    return True


def x__is_zero_traffic__mutmut_12(pod: dict[str, object]) -> bool:
    traffic = _as_float(pod.get("traffic_rps"))
    has_sidecar = _as_bool(pod.get("has_sidecar"))
    sidecar_traffic = _as_float(None)

    total_traffic = traffic + (sidecar_traffic if has_sidecar else 0.0)

    if total_traffic > _PROBE_NOISE_THRESHOLD:
        return False

    is_cronjob = _as_bool(pod.get("is_cronjob"))
    if is_cronjob:
        seven_day_traffic = _as_float(pod.get("seven_day_traffic_rps"))
        return seven_day_traffic <= _PROBE_NOISE_THRESHOLD

    return True


def x__is_zero_traffic__mutmut_13(pod: dict[str, object]) -> bool:
    traffic = _as_float(pod.get("traffic_rps"))
    has_sidecar = _as_bool(pod.get("has_sidecar"))
    sidecar_traffic = _as_float(pod.get(None))

    total_traffic = traffic + (sidecar_traffic if has_sidecar else 0.0)

    if total_traffic > _PROBE_NOISE_THRESHOLD:
        return False

    is_cronjob = _as_bool(pod.get("is_cronjob"))
    if is_cronjob:
        seven_day_traffic = _as_float(pod.get("seven_day_traffic_rps"))
        return seven_day_traffic <= _PROBE_NOISE_THRESHOLD

    return True


def x__is_zero_traffic__mutmut_14(pod: dict[str, object]) -> bool:
    traffic = _as_float(pod.get("traffic_rps"))
    has_sidecar = _as_bool(pod.get("has_sidecar"))
    sidecar_traffic = _as_float(pod.get("XXsidecar_traffic_rpsXX"))

    total_traffic = traffic + (sidecar_traffic if has_sidecar else 0.0)

    if total_traffic > _PROBE_NOISE_THRESHOLD:
        return False

    is_cronjob = _as_bool(pod.get("is_cronjob"))
    if is_cronjob:
        seven_day_traffic = _as_float(pod.get("seven_day_traffic_rps"))
        return seven_day_traffic <= _PROBE_NOISE_THRESHOLD

    return True


def x__is_zero_traffic__mutmut_15(pod: dict[str, object]) -> bool:
    traffic = _as_float(pod.get("traffic_rps"))
    has_sidecar = _as_bool(pod.get("has_sidecar"))
    sidecar_traffic = _as_float(pod.get("SIDECAR_TRAFFIC_RPS"))

    total_traffic = traffic + (sidecar_traffic if has_sidecar else 0.0)

    if total_traffic > _PROBE_NOISE_THRESHOLD:
        return False

    is_cronjob = _as_bool(pod.get("is_cronjob"))
    if is_cronjob:
        seven_day_traffic = _as_float(pod.get("seven_day_traffic_rps"))
        return seven_day_traffic <= _PROBE_NOISE_THRESHOLD

    return True


def x__is_zero_traffic__mutmut_16(pod: dict[str, object]) -> bool:
    traffic = _as_float(pod.get("traffic_rps"))
    has_sidecar = _as_bool(pod.get("has_sidecar"))
    sidecar_traffic = _as_float(pod.get("sidecar_traffic_rps"))

    total_traffic = None

    if total_traffic > _PROBE_NOISE_THRESHOLD:
        return False

    is_cronjob = _as_bool(pod.get("is_cronjob"))
    if is_cronjob:
        seven_day_traffic = _as_float(pod.get("seven_day_traffic_rps"))
        return seven_day_traffic <= _PROBE_NOISE_THRESHOLD

    return True


def x__is_zero_traffic__mutmut_17(pod: dict[str, object]) -> bool:
    traffic = _as_float(pod.get("traffic_rps"))
    has_sidecar = _as_bool(pod.get("has_sidecar"))
    sidecar_traffic = _as_float(pod.get("sidecar_traffic_rps"))

    total_traffic = traffic - (sidecar_traffic if has_sidecar else 0.0)

    if total_traffic > _PROBE_NOISE_THRESHOLD:
        return False

    is_cronjob = _as_bool(pod.get("is_cronjob"))
    if is_cronjob:
        seven_day_traffic = _as_float(pod.get("seven_day_traffic_rps"))
        return seven_day_traffic <= _PROBE_NOISE_THRESHOLD

    return True


def x__is_zero_traffic__mutmut_18(pod: dict[str, object]) -> bool:
    traffic = _as_float(pod.get("traffic_rps"))
    has_sidecar = _as_bool(pod.get("has_sidecar"))
    sidecar_traffic = _as_float(pod.get("sidecar_traffic_rps"))

    total_traffic = traffic + (sidecar_traffic if has_sidecar else 1.0)

    if total_traffic > _PROBE_NOISE_THRESHOLD:
        return False

    is_cronjob = _as_bool(pod.get("is_cronjob"))
    if is_cronjob:
        seven_day_traffic = _as_float(pod.get("seven_day_traffic_rps"))
        return seven_day_traffic <= _PROBE_NOISE_THRESHOLD

    return True


def x__is_zero_traffic__mutmut_19(pod: dict[str, object]) -> bool:
    traffic = _as_float(pod.get("traffic_rps"))
    has_sidecar = _as_bool(pod.get("has_sidecar"))
    sidecar_traffic = _as_float(pod.get("sidecar_traffic_rps"))

    total_traffic = traffic + (sidecar_traffic if has_sidecar else 0.0)

    if total_traffic >= _PROBE_NOISE_THRESHOLD:
        return False

    is_cronjob = _as_bool(pod.get("is_cronjob"))
    if is_cronjob:
        seven_day_traffic = _as_float(pod.get("seven_day_traffic_rps"))
        return seven_day_traffic <= _PROBE_NOISE_THRESHOLD

    return True


def x__is_zero_traffic__mutmut_20(pod: dict[str, object]) -> bool:
    traffic = _as_float(pod.get("traffic_rps"))
    has_sidecar = _as_bool(pod.get("has_sidecar"))
    sidecar_traffic = _as_float(pod.get("sidecar_traffic_rps"))

    total_traffic = traffic + (sidecar_traffic if has_sidecar else 0.0)

    if total_traffic > _PROBE_NOISE_THRESHOLD:
        return True

    is_cronjob = _as_bool(pod.get("is_cronjob"))
    if is_cronjob:
        seven_day_traffic = _as_float(pod.get("seven_day_traffic_rps"))
        return seven_day_traffic <= _PROBE_NOISE_THRESHOLD

    return True


def x__is_zero_traffic__mutmut_21(pod: dict[str, object]) -> bool:
    traffic = _as_float(pod.get("traffic_rps"))
    has_sidecar = _as_bool(pod.get("has_sidecar"))
    sidecar_traffic = _as_float(pod.get("sidecar_traffic_rps"))

    total_traffic = traffic + (sidecar_traffic if has_sidecar else 0.0)

    if total_traffic > _PROBE_NOISE_THRESHOLD:
        return False

    is_cronjob = None
    if is_cronjob:
        seven_day_traffic = _as_float(pod.get("seven_day_traffic_rps"))
        return seven_day_traffic <= _PROBE_NOISE_THRESHOLD

    return True


def x__is_zero_traffic__mutmut_22(pod: dict[str, object]) -> bool:
    traffic = _as_float(pod.get("traffic_rps"))
    has_sidecar = _as_bool(pod.get("has_sidecar"))
    sidecar_traffic = _as_float(pod.get("sidecar_traffic_rps"))

    total_traffic = traffic + (sidecar_traffic if has_sidecar else 0.0)

    if total_traffic > _PROBE_NOISE_THRESHOLD:
        return False

    is_cronjob = _as_bool(None)
    if is_cronjob:
        seven_day_traffic = _as_float(pod.get("seven_day_traffic_rps"))
        return seven_day_traffic <= _PROBE_NOISE_THRESHOLD

    return True


def x__is_zero_traffic__mutmut_23(pod: dict[str, object]) -> bool:
    traffic = _as_float(pod.get("traffic_rps"))
    has_sidecar = _as_bool(pod.get("has_sidecar"))
    sidecar_traffic = _as_float(pod.get("sidecar_traffic_rps"))

    total_traffic = traffic + (sidecar_traffic if has_sidecar else 0.0)

    if total_traffic > _PROBE_NOISE_THRESHOLD:
        return False

    is_cronjob = _as_bool(pod.get(None))
    if is_cronjob:
        seven_day_traffic = _as_float(pod.get("seven_day_traffic_rps"))
        return seven_day_traffic <= _PROBE_NOISE_THRESHOLD

    return True


def x__is_zero_traffic__mutmut_24(pod: dict[str, object]) -> bool:
    traffic = _as_float(pod.get("traffic_rps"))
    has_sidecar = _as_bool(pod.get("has_sidecar"))
    sidecar_traffic = _as_float(pod.get("sidecar_traffic_rps"))

    total_traffic = traffic + (sidecar_traffic if has_sidecar else 0.0)

    if total_traffic > _PROBE_NOISE_THRESHOLD:
        return False

    is_cronjob = _as_bool(pod.get("XXis_cronjobXX"))
    if is_cronjob:
        seven_day_traffic = _as_float(pod.get("seven_day_traffic_rps"))
        return seven_day_traffic <= _PROBE_NOISE_THRESHOLD

    return True


def x__is_zero_traffic__mutmut_25(pod: dict[str, object]) -> bool:
    traffic = _as_float(pod.get("traffic_rps"))
    has_sidecar = _as_bool(pod.get("has_sidecar"))
    sidecar_traffic = _as_float(pod.get("sidecar_traffic_rps"))

    total_traffic = traffic + (sidecar_traffic if has_sidecar else 0.0)

    if total_traffic > _PROBE_NOISE_THRESHOLD:
        return False

    is_cronjob = _as_bool(pod.get("IS_CRONJOB"))
    if is_cronjob:
        seven_day_traffic = _as_float(pod.get("seven_day_traffic_rps"))
        return seven_day_traffic <= _PROBE_NOISE_THRESHOLD

    return True


def x__is_zero_traffic__mutmut_26(pod: dict[str, object]) -> bool:
    traffic = _as_float(pod.get("traffic_rps"))
    has_sidecar = _as_bool(pod.get("has_sidecar"))
    sidecar_traffic = _as_float(pod.get("sidecar_traffic_rps"))

    total_traffic = traffic + (sidecar_traffic if has_sidecar else 0.0)

    if total_traffic > _PROBE_NOISE_THRESHOLD:
        return False

    is_cronjob = _as_bool(pod.get("is_cronjob"))
    if is_cronjob:
        seven_day_traffic = None
        return seven_day_traffic <= _PROBE_NOISE_THRESHOLD

    return True


def x__is_zero_traffic__mutmut_27(pod: dict[str, object]) -> bool:
    traffic = _as_float(pod.get("traffic_rps"))
    has_sidecar = _as_bool(pod.get("has_sidecar"))
    sidecar_traffic = _as_float(pod.get("sidecar_traffic_rps"))

    total_traffic = traffic + (sidecar_traffic if has_sidecar else 0.0)

    if total_traffic > _PROBE_NOISE_THRESHOLD:
        return False

    is_cronjob = _as_bool(pod.get("is_cronjob"))
    if is_cronjob:
        seven_day_traffic = _as_float(None)
        return seven_day_traffic <= _PROBE_NOISE_THRESHOLD

    return True


def x__is_zero_traffic__mutmut_28(pod: dict[str, object]) -> bool:
    traffic = _as_float(pod.get("traffic_rps"))
    has_sidecar = _as_bool(pod.get("has_sidecar"))
    sidecar_traffic = _as_float(pod.get("sidecar_traffic_rps"))

    total_traffic = traffic + (sidecar_traffic if has_sidecar else 0.0)

    if total_traffic > _PROBE_NOISE_THRESHOLD:
        return False

    is_cronjob = _as_bool(pod.get("is_cronjob"))
    if is_cronjob:
        seven_day_traffic = _as_float(pod.get(None))
        return seven_day_traffic <= _PROBE_NOISE_THRESHOLD

    return True


def x__is_zero_traffic__mutmut_29(pod: dict[str, object]) -> bool:
    traffic = _as_float(pod.get("traffic_rps"))
    has_sidecar = _as_bool(pod.get("has_sidecar"))
    sidecar_traffic = _as_float(pod.get("sidecar_traffic_rps"))

    total_traffic = traffic + (sidecar_traffic if has_sidecar else 0.0)

    if total_traffic > _PROBE_NOISE_THRESHOLD:
        return False

    is_cronjob = _as_bool(pod.get("is_cronjob"))
    if is_cronjob:
        seven_day_traffic = _as_float(pod.get("XXseven_day_traffic_rpsXX"))
        return seven_day_traffic <= _PROBE_NOISE_THRESHOLD

    return True


def x__is_zero_traffic__mutmut_30(pod: dict[str, object]) -> bool:
    traffic = _as_float(pod.get("traffic_rps"))
    has_sidecar = _as_bool(pod.get("has_sidecar"))
    sidecar_traffic = _as_float(pod.get("sidecar_traffic_rps"))

    total_traffic = traffic + (sidecar_traffic if has_sidecar else 0.0)

    if total_traffic > _PROBE_NOISE_THRESHOLD:
        return False

    is_cronjob = _as_bool(pod.get("is_cronjob"))
    if is_cronjob:
        seven_day_traffic = _as_float(pod.get("SEVEN_DAY_TRAFFIC_RPS"))
        return seven_day_traffic <= _PROBE_NOISE_THRESHOLD

    return True


def x__is_zero_traffic__mutmut_31(pod: dict[str, object]) -> bool:
    traffic = _as_float(pod.get("traffic_rps"))
    has_sidecar = _as_bool(pod.get("has_sidecar"))
    sidecar_traffic = _as_float(pod.get("sidecar_traffic_rps"))

    total_traffic = traffic + (sidecar_traffic if has_sidecar else 0.0)

    if total_traffic > _PROBE_NOISE_THRESHOLD:
        return False

    is_cronjob = _as_bool(pod.get("is_cronjob"))
    if is_cronjob:
        seven_day_traffic = _as_float(pod.get("seven_day_traffic_rps"))
        return seven_day_traffic < _PROBE_NOISE_THRESHOLD

    return True


def x__is_zero_traffic__mutmut_32(pod: dict[str, object]) -> bool:
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

    return False

mutants_x__is_zero_traffic__mutmut['_mutmut_orig'] = x__is_zero_traffic__mutmut_orig # type: ignore # mutmut generated
mutants_x__is_zero_traffic__mutmut['x__is_zero_traffic__mutmut_1'] = x__is_zero_traffic__mutmut_1 # type: ignore # mutmut generated
mutants_x__is_zero_traffic__mutmut['x__is_zero_traffic__mutmut_2'] = x__is_zero_traffic__mutmut_2 # type: ignore # mutmut generated
mutants_x__is_zero_traffic__mutmut['x__is_zero_traffic__mutmut_3'] = x__is_zero_traffic__mutmut_3 # type: ignore # mutmut generated
mutants_x__is_zero_traffic__mutmut['x__is_zero_traffic__mutmut_4'] = x__is_zero_traffic__mutmut_4 # type: ignore # mutmut generated
mutants_x__is_zero_traffic__mutmut['x__is_zero_traffic__mutmut_5'] = x__is_zero_traffic__mutmut_5 # type: ignore # mutmut generated
mutants_x__is_zero_traffic__mutmut['x__is_zero_traffic__mutmut_6'] = x__is_zero_traffic__mutmut_6 # type: ignore # mutmut generated
mutants_x__is_zero_traffic__mutmut['x__is_zero_traffic__mutmut_7'] = x__is_zero_traffic__mutmut_7 # type: ignore # mutmut generated
mutants_x__is_zero_traffic__mutmut['x__is_zero_traffic__mutmut_8'] = x__is_zero_traffic__mutmut_8 # type: ignore # mutmut generated
mutants_x__is_zero_traffic__mutmut['x__is_zero_traffic__mutmut_9'] = x__is_zero_traffic__mutmut_9 # type: ignore # mutmut generated
mutants_x__is_zero_traffic__mutmut['x__is_zero_traffic__mutmut_10'] = x__is_zero_traffic__mutmut_10 # type: ignore # mutmut generated
mutants_x__is_zero_traffic__mutmut['x__is_zero_traffic__mutmut_11'] = x__is_zero_traffic__mutmut_11 # type: ignore # mutmut generated
mutants_x__is_zero_traffic__mutmut['x__is_zero_traffic__mutmut_12'] = x__is_zero_traffic__mutmut_12 # type: ignore # mutmut generated
mutants_x__is_zero_traffic__mutmut['x__is_zero_traffic__mutmut_13'] = x__is_zero_traffic__mutmut_13 # type: ignore # mutmut generated
mutants_x__is_zero_traffic__mutmut['x__is_zero_traffic__mutmut_14'] = x__is_zero_traffic__mutmut_14 # type: ignore # mutmut generated
mutants_x__is_zero_traffic__mutmut['x__is_zero_traffic__mutmut_15'] = x__is_zero_traffic__mutmut_15 # type: ignore # mutmut generated
mutants_x__is_zero_traffic__mutmut['x__is_zero_traffic__mutmut_16'] = x__is_zero_traffic__mutmut_16 # type: ignore # mutmut generated
mutants_x__is_zero_traffic__mutmut['x__is_zero_traffic__mutmut_17'] = x__is_zero_traffic__mutmut_17 # type: ignore # mutmut generated
mutants_x__is_zero_traffic__mutmut['x__is_zero_traffic__mutmut_18'] = x__is_zero_traffic__mutmut_18 # type: ignore # mutmut generated
mutants_x__is_zero_traffic__mutmut['x__is_zero_traffic__mutmut_19'] = x__is_zero_traffic__mutmut_19 # type: ignore # mutmut generated
mutants_x__is_zero_traffic__mutmut['x__is_zero_traffic__mutmut_20'] = x__is_zero_traffic__mutmut_20 # type: ignore # mutmut generated
mutants_x__is_zero_traffic__mutmut['x__is_zero_traffic__mutmut_21'] = x__is_zero_traffic__mutmut_21 # type: ignore # mutmut generated
mutants_x__is_zero_traffic__mutmut['x__is_zero_traffic__mutmut_22'] = x__is_zero_traffic__mutmut_22 # type: ignore # mutmut generated
mutants_x__is_zero_traffic__mutmut['x__is_zero_traffic__mutmut_23'] = x__is_zero_traffic__mutmut_23 # type: ignore # mutmut generated
mutants_x__is_zero_traffic__mutmut['x__is_zero_traffic__mutmut_24'] = x__is_zero_traffic__mutmut_24 # type: ignore # mutmut generated
mutants_x__is_zero_traffic__mutmut['x__is_zero_traffic__mutmut_25'] = x__is_zero_traffic__mutmut_25 # type: ignore # mutmut generated
mutants_x__is_zero_traffic__mutmut['x__is_zero_traffic__mutmut_26'] = x__is_zero_traffic__mutmut_26 # type: ignore # mutmut generated
mutants_x__is_zero_traffic__mutmut['x__is_zero_traffic__mutmut_27'] = x__is_zero_traffic__mutmut_27 # type: ignore # mutmut generated
mutants_x__is_zero_traffic__mutmut['x__is_zero_traffic__mutmut_28'] = x__is_zero_traffic__mutmut_28 # type: ignore # mutmut generated
mutants_x__is_zero_traffic__mutmut['x__is_zero_traffic__mutmut_29'] = x__is_zero_traffic__mutmut_29 # type: ignore # mutmut generated
mutants_x__is_zero_traffic__mutmut['x__is_zero_traffic__mutmut_30'] = x__is_zero_traffic__mutmut_30 # type: ignore # mutmut generated
mutants_x__is_zero_traffic__mutmut['x__is_zero_traffic__mutmut_31'] = x__is_zero_traffic__mutmut_31 # type: ignore # mutmut generated
mutants_x__is_zero_traffic__mutmut['x__is_zero_traffic__mutmut_32'] = x__is_zero_traffic__mutmut_32 # type: ignore # mutmut generated
mutants_x__classify_risk__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__classify_risk__mutmut)
def _classify_risk(pod: dict[str, object]) -> tuple[str, str]:
    has_service = _as_bool(pod.get("has_service"))

    if has_service:
        return "review_needed", "No traffic but has service pointing to it"

    return "safe_to_remove", "No traffic for 24h, no deps"


def x__classify_risk__mutmut_orig(pod: dict[str, object]) -> tuple[str, str]:
    has_service = _as_bool(pod.get("has_service"))

    if has_service:
        return "review_needed", "No traffic but has service pointing to it"

    return "safe_to_remove", "No traffic for 24h, no deps"


def x__classify_risk__mutmut_1(pod: dict[str, object]) -> tuple[str, str]:
    has_service = None

    if has_service:
        return "review_needed", "No traffic but has service pointing to it"

    return "safe_to_remove", "No traffic for 24h, no deps"


def x__classify_risk__mutmut_2(pod: dict[str, object]) -> tuple[str, str]:
    has_service = _as_bool(None)

    if has_service:
        return "review_needed", "No traffic but has service pointing to it"

    return "safe_to_remove", "No traffic for 24h, no deps"


def x__classify_risk__mutmut_3(pod: dict[str, object]) -> tuple[str, str]:
    has_service = _as_bool(pod.get(None))

    if has_service:
        return "review_needed", "No traffic but has service pointing to it"

    return "safe_to_remove", "No traffic for 24h, no deps"


def x__classify_risk__mutmut_4(pod: dict[str, object]) -> tuple[str, str]:
    has_service = _as_bool(pod.get("XXhas_serviceXX"))

    if has_service:
        return "review_needed", "No traffic but has service pointing to it"

    return "safe_to_remove", "No traffic for 24h, no deps"


def x__classify_risk__mutmut_5(pod: dict[str, object]) -> tuple[str, str]:
    has_service = _as_bool(pod.get("HAS_SERVICE"))

    if has_service:
        return "review_needed", "No traffic but has service pointing to it"

    return "safe_to_remove", "No traffic for 24h, no deps"


def x__classify_risk__mutmut_6(pod: dict[str, object]) -> tuple[str, str]:
    has_service = _as_bool(pod.get("has_service"))

    if has_service:
        return "XXreview_neededXX", "No traffic but has service pointing to it"

    return "safe_to_remove", "No traffic for 24h, no deps"


def x__classify_risk__mutmut_7(pod: dict[str, object]) -> tuple[str, str]:
    has_service = _as_bool(pod.get("has_service"))

    if has_service:
        return "REVIEW_NEEDED", "No traffic but has service pointing to it"

    return "safe_to_remove", "No traffic for 24h, no deps"


def x__classify_risk__mutmut_8(pod: dict[str, object]) -> tuple[str, str]:
    has_service = _as_bool(pod.get("has_service"))

    if has_service:
        return "review_needed", "XXNo traffic but has service pointing to itXX"

    return "safe_to_remove", "No traffic for 24h, no deps"


def x__classify_risk__mutmut_9(pod: dict[str, object]) -> tuple[str, str]:
    has_service = _as_bool(pod.get("has_service"))

    if has_service:
        return "review_needed", "no traffic but has service pointing to it"

    return "safe_to_remove", "No traffic for 24h, no deps"


def x__classify_risk__mutmut_10(pod: dict[str, object]) -> tuple[str, str]:
    has_service = _as_bool(pod.get("has_service"))

    if has_service:
        return "review_needed", "NO TRAFFIC BUT HAS SERVICE POINTING TO IT"

    return "safe_to_remove", "No traffic for 24h, no deps"


def x__classify_risk__mutmut_11(pod: dict[str, object]) -> tuple[str, str]:
    has_service = _as_bool(pod.get("has_service"))

    if has_service:
        return "review_needed", "No traffic but has service pointing to it"

    return "XXsafe_to_removeXX", "No traffic for 24h, no deps"


def x__classify_risk__mutmut_12(pod: dict[str, object]) -> tuple[str, str]:
    has_service = _as_bool(pod.get("has_service"))

    if has_service:
        return "review_needed", "No traffic but has service pointing to it"

    return "SAFE_TO_REMOVE", "No traffic for 24h, no deps"


def x__classify_risk__mutmut_13(pod: dict[str, object]) -> tuple[str, str]:
    has_service = _as_bool(pod.get("has_service"))

    if has_service:
        return "review_needed", "No traffic but has service pointing to it"

    return "safe_to_remove", "XXNo traffic for 24h, no depsXX"


def x__classify_risk__mutmut_14(pod: dict[str, object]) -> tuple[str, str]:
    has_service = _as_bool(pod.get("has_service"))

    if has_service:
        return "review_needed", "No traffic but has service pointing to it"

    return "safe_to_remove", "no traffic for 24h, no deps"


def x__classify_risk__mutmut_15(pod: dict[str, object]) -> tuple[str, str]:
    has_service = _as_bool(pod.get("has_service"))

    if has_service:
        return "review_needed", "No traffic but has service pointing to it"

    return "safe_to_remove", "NO TRAFFIC FOR 24H, NO DEPS"

mutants_x__classify_risk__mutmut['_mutmut_orig'] = x__classify_risk__mutmut_orig # type: ignore # mutmut generated
mutants_x__classify_risk__mutmut['x__classify_risk__mutmut_1'] = x__classify_risk__mutmut_1 # type: ignore # mutmut generated
mutants_x__classify_risk__mutmut['x__classify_risk__mutmut_2'] = x__classify_risk__mutmut_2 # type: ignore # mutmut generated
mutants_x__classify_risk__mutmut['x__classify_risk__mutmut_3'] = x__classify_risk__mutmut_3 # type: ignore # mutmut generated
mutants_x__classify_risk__mutmut['x__classify_risk__mutmut_4'] = x__classify_risk__mutmut_4 # type: ignore # mutmut generated
mutants_x__classify_risk__mutmut['x__classify_risk__mutmut_5'] = x__classify_risk__mutmut_5 # type: ignore # mutmut generated
mutants_x__classify_risk__mutmut['x__classify_risk__mutmut_6'] = x__classify_risk__mutmut_6 # type: ignore # mutmut generated
mutants_x__classify_risk__mutmut['x__classify_risk__mutmut_7'] = x__classify_risk__mutmut_7 # type: ignore # mutmut generated
mutants_x__classify_risk__mutmut['x__classify_risk__mutmut_8'] = x__classify_risk__mutmut_8 # type: ignore # mutmut generated
mutants_x__classify_risk__mutmut['x__classify_risk__mutmut_9'] = x__classify_risk__mutmut_9 # type: ignore # mutmut generated
mutants_x__classify_risk__mutmut['x__classify_risk__mutmut_10'] = x__classify_risk__mutmut_10 # type: ignore # mutmut generated
mutants_x__classify_risk__mutmut['x__classify_risk__mutmut_11'] = x__classify_risk__mutmut_11 # type: ignore # mutmut generated
mutants_x__classify_risk__mutmut['x__classify_risk__mutmut_12'] = x__classify_risk__mutmut_12 # type: ignore # mutmut generated
mutants_x__classify_risk__mutmut['x__classify_risk__mutmut_13'] = x__classify_risk__mutmut_13 # type: ignore # mutmut generated
mutants_x__classify_risk__mutmut['x__classify_risk__mutmut_14'] = x__classify_risk__mutmut_14 # type: ignore # mutmut generated
mutants_x__classify_risk__mutmut['x__classify_risk__mutmut_15'] = x__classify_risk__mutmut_15 # type: ignore # mutmut generated
mutants_x__as_float__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__as_float__mutmut)
def _as_float(value: object) -> float:
    if value is None:
        return 0.0
    try:
        return float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0.0


def x__as_float__mutmut_orig(value: object) -> float:
    if value is None:
        return 0.0
    try:
        return float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0.0


def x__as_float__mutmut_1(value: object) -> float:
    if value is not None:
        return 0.0
    try:
        return float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0.0


def x__as_float__mutmut_2(value: object) -> float:
    if value is None:
        return 1.0
    try:
        return float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0.0


def x__as_float__mutmut_3(value: object) -> float:
    if value is None:
        return 0.0
    try:
        return float(None)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0.0


def x__as_float__mutmut_4(value: object) -> float:
    if value is None:
        return 0.0
    try:
        return float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 1.0

mutants_x__as_float__mutmut['_mutmut_orig'] = x__as_float__mutmut_orig # type: ignore # mutmut generated
mutants_x__as_float__mutmut['x__as_float__mutmut_1'] = x__as_float__mutmut_1 # type: ignore # mutmut generated
mutants_x__as_float__mutmut['x__as_float__mutmut_2'] = x__as_float__mutmut_2 # type: ignore # mutmut generated
mutants_x__as_float__mutmut['x__as_float__mutmut_3'] = x__as_float__mutmut_3 # type: ignore # mutmut generated
mutants_x__as_float__mutmut['x__as_float__mutmut_4'] = x__as_float__mutmut_4 # type: ignore # mutmut generated
mutants_x__as_bool__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__as_bool__mutmut)
def _as_bool(value: object) -> bool:
    if value is None:
        return False
    if isinstance(value, bool):
        return value
    return bool(value)


def x__as_bool__mutmut_orig(value: object) -> bool:
    if value is None:
        return False
    if isinstance(value, bool):
        return value
    return bool(value)


def x__as_bool__mutmut_1(value: object) -> bool:
    if value is not None:
        return False
    if isinstance(value, bool):
        return value
    return bool(value)


def x__as_bool__mutmut_2(value: object) -> bool:
    if value is None:
        return True
    if isinstance(value, bool):
        return value
    return bool(value)


def x__as_bool__mutmut_3(value: object) -> bool:
    if value is None:
        return False
    if isinstance(value, bool):
        return value
    return bool(None)

mutants_x__as_bool__mutmut['_mutmut_orig'] = x__as_bool__mutmut_orig # type: ignore # mutmut generated
mutants_x__as_bool__mutmut['x__as_bool__mutmut_1'] = x__as_bool__mutmut_1 # type: ignore # mutmut generated
mutants_x__as_bool__mutmut['x__as_bool__mutmut_2'] = x__as_bool__mutmut_2 # type: ignore # mutmut generated
mutants_x__as_bool__mutmut['x__as_bool__mutmut_3'] = x__as_bool__mutmut_3 # type: ignore # mutmut generated
