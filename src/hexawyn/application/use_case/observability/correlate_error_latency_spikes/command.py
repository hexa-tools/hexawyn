from dataclasses import dataclass


@dataclass(frozen=True)
class CorrelateErrorLatencySpikesUseCaseCommand:
    namespace: str | None = None
