from abc import ABC, abstractmethod

from hexawyn.domain.models.gitops import (
    GitOpsApp,
    GitOpsDetectionResult,
    GitOpsSource,
)


class GitOpsPort(ABC):
    """Port for GitOps engine (Flux CD / Argo CD) operations — read-only."""

    @abstractmethod
    def detect_engine(self) -> GitOpsDetectionResult:
        """Auto-detect Flux CD or Argo CD in the cluster."""

    @abstractmethod
    def list_apps(self, namespace: str | None = None) -> list[GitOpsApp]:
        """List all GitOps applications (HelmRelease, Kustomization, Application)."""

    @abstractmethod
    def get_app(self, name: str, namespace: str) -> GitOpsApp:
        """Get detailed status of a specific GitOps application."""

    @abstractmethod
    def list_sources(self, namespace: str | None = None) -> list[GitOpsSource]:
        """List GitOps sources (GitRepository, HelmRepository, Bucket)."""

    @abstractmethod
    def get_source(self, name: str, namespace: str) -> GitOpsSource:
        """Get detailed status of a specific GitOps source."""
