from abc import ABC, abstractmethod

from hexawyn.domain.models.rollouts import (
    AnalysisRun,
    Rollout,
    RolloutsDetectionResult,
)


class RolloutsPort(ABC):
    """Port for Argo Rollouts operations — read-only."""

    @abstractmethod
    def detect_rollouts(self) -> RolloutsDetectionResult:
        """Detect if Argo Rollouts is installed and return summary counts."""

    @abstractmethod
    def list_rollouts(self, namespace: str | None = None) -> list[Rollout]:
        """List all Rollouts with strategy and phase."""

    @abstractmethod
    def get_rollout(self, name: str, namespace: str) -> Rollout:
        """Get detailed status of a specific Rollout."""

    @abstractmethod
    def list_analysis_runs(
        self, namespace: str | None = None, rollout_name: str | None = None
    ) -> list[AnalysisRun]:
        """List AnalysisRuns, optionally filtered by rollout name."""
