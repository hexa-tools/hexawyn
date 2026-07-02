from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ServiceErrorCount:
    service_name: str
    error_count: int
    percentage: float


@dataclass(frozen=True)
class ErrorAttributionRequest:
    gateway: str
    time_window_minutes: int = 30


@dataclass(frozen=True)
class ErrorAttributionResult:
    gateway: str
    time_window_minutes: int
    total_errors: int
    attribution: list[ServiceErrorCount]
    pareto_culprit: str | None

    @staticmethod
    def compute(
        request: ErrorAttributionRequest,
        raw_errors: list[dict[str, object]],
    ) -> ErrorAttributionResult:
        total = sum(int(str(r.get("count", 0))) for r in raw_errors)
        if total == 0:
            return ErrorAttributionResult(
                gateway=request.gateway,
                time_window_minutes=request.time_window_minutes,
                total_errors=0,
                attribution=[],
                pareto_culprit=None,
            )

        ranked: list[ServiceErrorCount] = []
        for r in sorted(raw_errors, key=lambda x: int(str(x.get("count", 0))), reverse=True):
            count = int(str(r.get("count", 0)))
            svc = str(r.get("service", "unknown"))
            pct = round((count / total) * 100.0, 1)
            ranked.append(ServiceErrorCount(service_name=svc, error_count=count, percentage=pct))

        culprit = ranked[0].service_name if ranked and ranked[0].percentage >= 80.0 else None
        return ErrorAttributionResult(
            gateway=request.gateway,
            time_window_minutes=request.time_window_minutes,
            total_errors=total,
            attribution=ranked,
            pareto_culprit=culprit,
        )
