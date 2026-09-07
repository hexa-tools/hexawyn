from __future__ import annotations

from hexawyn.application.ports.driven.gitops_port import GitOpsPort
from hexawyn.domain.models.gitops import (
    GitOpsApp,
    GitOpsDetectionResult,
    GitOpsEngine,
    GitOpsSource,
)


class GitOpsDetector(GitOpsPort):
    """Auto-detects Flux CD or Argo CD by checking for CRDs in the cluster.

    Delegates to FluxAdapter or ArgoCDAdapter once the engine is detected.
    Detection order: Flux CRDs first, then Argo CD CRDs.
    """

    def __init__(self) -> None:
        self._delegate: GitOpsPort | None = None

    def _ensure_detected(self) -> GitOpsPort:
        if self._delegate is not None:
            return self._delegate
        from hexawyn.domain.errors import GitOpsEngineNotFoundError

        raise GitOpsEngineNotFoundError()

    def detect_engine(self) -> GitOpsDetectionResult:
        from hexawyn.domain.errors import GitOpsEngineNotFoundError

        try:
            self._ensure_detected()
            return self._delegate.detect_engine()  # type: ignore[union-attr]
        except GitOpsEngineNotFoundError:
            return GitOpsDetectionResult(
                engine=GitOpsEngine.NONE,
                version=None,
                namespace=None,
                apps_count=0,
                out_of_sync_count=0,
                failed_count=0,
            )

    def list_apps(self, namespace: str | None = None) -> list[GitOpsApp]:
        return self._ensure_detected().list_apps(namespace=namespace)

    def get_app(self, name: str, namespace: str) -> GitOpsApp:
        return self._ensure_detected().get_app(name=name, namespace=namespace)

    def list_sources(self, namespace: str | None = None) -> list[GitOpsSource]:
        return self._ensure_detected().list_sources(namespace=namespace)

    def get_source(self, name: str, namespace: str) -> GitOpsSource:
        return self._ensure_detected().get_source(name=name, namespace=namespace)
