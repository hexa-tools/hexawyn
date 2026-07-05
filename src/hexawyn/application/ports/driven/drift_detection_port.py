from abc import ABC, abstractmethod
from typing import TypedDict


class ResourceManifestRaw(TypedDict):
    kind: str
    name: str
    namespace: str
    data: dict[str, object]


class DriftDetectionPort(ABC):
    """Driven port: renders the desired-state manifests from a source (a
    Helm release name, or a Kustomize overlay path) and checks whether that
    source still exists. Implemented by both HelmDriftAdapter and
    KustomizeDriftAdapter, sharing one interface."""

    @abstractmethod
    def render_desired_manifests(self, source: str, namespace: str) -> list[ResourceManifestRaw]:
        """Renders the desired-state manifests for the given source.

        Raises HelmNotFoundError/KustomizeNotFoundError if the CLI binary
        is not installed.
        Raises ManifestRenderError on a genuine render failure (malformed
        chart/path/YAML, command error) — distinct from the source not
        existing, which is `source_exists() -> False`.
        """

    @abstractmethod
    def source_exists(self, source: str, namespace: str) -> bool:
        """Whether the source (Helm release, or Kustomize path) still
        exists — used to detect orphaned resources."""
