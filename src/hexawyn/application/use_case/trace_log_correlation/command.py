from dataclasses import dataclass


@dataclass(frozen=True)
class TraceLogCorrelationCommand:
    trace_id: str
