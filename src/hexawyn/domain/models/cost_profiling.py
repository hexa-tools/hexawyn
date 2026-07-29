from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class EndpointCPUProfile:
    endpoint: str
    avg_cpu_ms_per_request: float
    request_count: int
    total_cpu_ms: float

    @property
    def cost_score(self) -> float:
        return round(self.avg_cpu_ms_per_request * self.request_count, 2)


@dataclass(frozen=True)
class OptimisationCandidate:
    endpoint: str
    avg_cpu_ms_per_request: float
    request_count: int
    reason: str


@dataclass(frozen=True)
class CostProfilingRequest:
    time_window_minutes: int = 60
    top_n: int = 5


@dataclass(frozen=True)
class CostProfilingResult:
    time_window_minutes: int
    ranked_endpoints: list[EndpointCPUProfile]
    optimisation_candidates: list[OptimisationCandidate]

    @staticmethod
    def compute(
        request: CostProfilingRequest,
        endpoints: list[EndpointCPUProfile],
    ) -> CostProfilingResult:
        with_cpu = [e for e in endpoints if e.total_cpu_ms > 0]
        ranked = sorted(with_cpu, key=lambda e: e.cost_score, reverse=True)
        top = ranked[: request.top_n]
        candidates: list[OptimisationCandidate] = []
        if top:
            candidates.append(
                OptimisationCandidate(
                    endpoint=top[0].endpoint,
                    avg_cpu_ms_per_request=top[0].avg_cpu_ms_per_request,
                    request_count=top[0].request_count,
                    reason=f"Highest total CPU cost ({top[0].total_cpu_ms}ms over {request.time_window_minutes}min)",  # noqa: E501
                )
            )
        high_per_request = max(ranked, key=lambda e: e.avg_cpu_ms_per_request, default=None)
        if high_per_request and high_per_request.endpoint != (
            candidates[0].endpoint if candidates else None
        ):
            candidates.append(
                OptimisationCandidate(
                    endpoint=high_per_request.endpoint,
                    avg_cpu_ms_per_request=high_per_request.avg_cpu_ms_per_request,
                    request_count=high_per_request.request_count,
                    reason=f"Highest CPU per request ({high_per_request.avg_cpu_ms_per_request}ms)",
                )
            )
        return CostProfilingResult(
            time_window_minutes=request.time_window_minutes,
            ranked_endpoints=top,
            optimisation_candidates=candidates,
        )
