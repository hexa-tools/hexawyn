from __future__ import annotations

from dataclasses import dataclass, field

FAILING_PHASES: frozenset[str] = frozenset(
    {"CrashLoopBackOff", "Error", "ImagePullBackOff", "Evicted"}
)
RESTART_THRESHOLD: int = 5


@dataclass(frozen=True)
class HistoricalPod:
    name: str
    namespace: str
    phase: str
    restart_count: int
    queried_timestamp: str
    currently_exists: bool = True
    status_changed_since: bool = False


@dataclass
class HistoricalStateSnapshot:
    namespace: str
    resource_type: str
    queried_timestamp: str
    total_resources: int
    pods: list[HistoricalPod] = field(default_factory=list)

    def get_restarting_pods(self, threshold: int = RESTART_THRESHOLD) -> list[HistoricalPod]:
        return [pod for pod in self.pods if pod.restart_count > threshold]

    def get_failing_pods(self) -> list[HistoricalPod]:
        return [pod for pod in self.pods if pod.phase in FAILING_PHASES]


@dataclass(frozen=True)
class StateComparison:
    namespace: str
    historical_timestamp: str
    historical_count: int
    current_count: int
    pods_added: int
    pods_removed: int
    added_pod_names: list[str] = field(default_factory=list)
    removed_pod_names: list[str] = field(default_factory=list)

    @staticmethod
    def compare(
        namespace: str,
        historical_pods: list[HistoricalPod],
        current_pods: list[HistoricalPod],
        historical_timestamp: str,
    ) -> StateComparison:
        historical_names = {pod.name for pod in historical_pods}
        current_names = {pod.name for pod in current_pods}
        added = sorted(current_names - historical_names)
        removed = sorted(historical_names - current_names)
        return StateComparison(
            namespace=namespace,
            historical_timestamp=historical_timestamp,
            historical_count=len(historical_pods),
            current_count=len(current_pods),
            pods_added=len(added),
            pods_removed=len(removed),
            added_pod_names=added,
            removed_pod_names=removed,
        )


@dataclass(frozen=True)
class PodRestartStatus:
    pod_name: str
    is_restarting: bool
    is_failing: bool

    @staticmethod
    def from_pod(pod: HistoricalPod) -> PodRestartStatus:
        return PodRestartStatus(
            pod_name=pod.name,
            is_restarting=pod.restart_count > RESTART_THRESHOLD or pod.phase in FAILING_PHASES,
            is_failing=pod.phase in FAILING_PHASES,
        )
