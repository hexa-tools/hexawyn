from __future__ import annotations

from hexawyn.application.ports.driven.rollouts_port import RolloutsPort
from hexawyn.domain.errors import ComponentNotInstalledError
from hexawyn.domain.models.rollouts import (
    AnalysisRun,
    Rollout,
    RolloutsDetectionResult,
)


class ArgoRolloutsDetector(RolloutsPort):
    """Detects Argo Rollouts by checking for CRDs and provides read-only access.

    All tools are read-only — promote, abort, and retry are never triggered.
    """

    def detect_rollouts(self) -> RolloutsDetectionResult:
        return RolloutsDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_rollouts=0,
            healthy=0,
            progressing=0,
            degraded=0,
            paused=0,
        )

    def list_rollouts(self, namespace: str | None = None) -> list[Rollout]:
        raise ComponentNotInstalledError(
            "Argo Rollouts", "https://argo-rollouts.readthedocs.io/en/stable/installation/"
        )

    def get_rollout(self, name: str, namespace: str) -> Rollout:
        raise ComponentNotInstalledError(
            "Argo Rollouts", "https://argo-rollouts.readthedocs.io/en/stable/installation/"
        )

    def list_analysis_runs(
        self, namespace: str | None = None, rollout_name: str | None = None
    ) -> list[AnalysisRun]:
        raise ComponentNotInstalledError(
            "Argo Rollouts", "https://argo-rollouts.readthedocs.io/en/stable/installation/"
        )
