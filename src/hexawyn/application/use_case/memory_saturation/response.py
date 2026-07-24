from dataclasses import dataclass


@dataclass
class MemorySaturationResponse:
    error: str | None = None
