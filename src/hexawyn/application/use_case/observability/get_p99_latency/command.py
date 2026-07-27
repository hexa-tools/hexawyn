from dataclasses import dataclass


@dataclass(frozen=True)
class GetP99LatencyUseCaseCommand:
    namespace: str | None = None
