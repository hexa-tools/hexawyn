from dataclasses import dataclass


@dataclass
class ErrorAttributionResponse:
    error: str | None = None
