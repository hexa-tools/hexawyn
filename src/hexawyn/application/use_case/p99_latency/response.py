from dataclasses import dataclass


@dataclass
class P99LatencyResponse:
    error: str | None = None
