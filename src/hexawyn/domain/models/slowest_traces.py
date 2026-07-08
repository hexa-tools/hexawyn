from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SlowTrace:
    trace_id: str
    duration_ms: float
    operation: str
    span_count: int


@dataclass(frozen=True)
class SlowestTracesRequest:
    pod_name: str
    time_window_minutes: int = 60
    top_n: int = 5


@dataclass(frozen=True)
class SlowestTracesResult:
    pod_name: str
    time_window_minutes: int
    top_n: int
    slowest_traces: list[SlowTrace]
    total_traces_found: int
    note: str

    @staticmethod
    def compute(
        request: SlowestTracesRequest,
        traces: list[SlowTrace],
    ) -> SlowestTracesResult:
        sorted_traces = sorted(traces, key=lambda t: t.duration_ms, reverse=True)
        top = sorted_traces[: request.top_n]

        if not traces:
            note = f"No traces found for pod '{request.pod_name}'"
        elif len(traces) < request.top_n:
            note = f"Only {len(traces)} trace(s) found (fewer than requested {request.top_n})"
        else:
            note = f"Top {len(top)} of {len(traces)} traces shown"

        return SlowestTracesResult(
            pod_name=request.pod_name,
            time_window_minutes=request.time_window_minutes,
            top_n=request.top_n,
            slowest_traces=top,
            total_traces_found=len(traces),
            note=note,
        )
