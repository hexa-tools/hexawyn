from dataclasses import dataclass


@dataclass(frozen=True)
class DiagnoseLatencySpikeUseCaseCommand:
    namespace: str | None = None
