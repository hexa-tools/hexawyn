from dataclasses import dataclass


@dataclass(frozen=True)
class RunWhatIfSimulationCommand:
    target_service: str
    namespace: str
    proposed_replicas: int
    current_replicas: int | None = None
    current_cpu_utilization: float | None = None
